
# Code Patterns & Boilerplates for CS-Script (.csx)

## 1. Standard Script Skeleton

Every `.csx` script should follow this established structure:

```csharp
#category "4 • Find Missing Objects"
#name "Find Missing Sounds"
#desc "Finds and logs any referenced sounds that are missing"

#load "Common/Sound.csx"

/*
    Detailed description of the script's purpose, parsing mechanics,
    parallel execution strategy, error handling, and output report generation.
*/

using System.Globalization;
using System.Threading;
using Reality.BF2;
using Reality.BF2.Build;
using Reality.BF2.Console;

public class FindMissingSounds
{
    private static ScriptResult GenerateScriptResult(bool success, string header, string message)
    {
        return new ScriptResult()
        {
            Success = success,
            Header = header,
            Message = message
        };
    }

    public static ScriptResult Main()
    {
        ScriptProgress.Title = "Finding Missing Sounds...";
        ScriptProgress.Text = "Collecting sounds...";
        ScriptProgress.Indeterminate = true;
        ScriptProgress.Value = 0;
        ScriptProgress.Maximum = 0;
        ScriptProgress.Show();

        ParallelOptions parallelOptions = new ParallelOptions()
        {
            MaxDegreeOfParallelism = Build.GetParallelism()
        };

        try
        {
            string[] sounds = SoundUtilities.GetFiles(Directories.CurrentModDirectory).ToArray();
            StringWriter stringWriter = new StringWriter(CultureInfo.InvariantCulture);

            int counter = 0;
            int numMissing = 0;
            string error = null;

            ScriptProgress.Indeterminate = false;
            ScriptProgress.Maximum = sounds.Length;

            Parallel.ForEach(sounds, parallelOptions, (soundFilePath, loopState) =>
            {
                ScriptProgress.Value = Interlocked.Increment(ref counter);
                ScriptProgress.Text = String.Format("Validating sounds • {0}/{1}", ScriptProgress.Value, ScriptProgress.Maximum);

                try
                {
                    Sound sound = SoundUtilities.ValidateFile(soundFilePath);
                    if (sound.MissingSounds.Length > 0)
                    {
                        Interlocked.Increment(ref numMissing);
                        lock (stringWriter)
                        {
                            stringWriter.WriteLine(sound.File);
                            stringWriter.WriteLine("Is missing the following sounds:");
                            foreach (string missing in sound.MissingSounds)
                            {
                                stringWriter.WriteLine("\t" + missing);
                            }
                            stringWriter.WriteLine();
                        }
                    }
                }
                catch (Exception ex)
                {
                    error = ex.ToString();
                    loopState.Break();
                }
            });

            if (error != null)
            {
                return GenerateScriptResult(false, "Error", error);
            }

            string outputPath = Path.Combine(Directories.CurrentModDirectory, "MissingSounds.txt");
            if (numMissing > 0)
            {
                File.WriteAllText(outputPath, stringWriter.ToString());
                return GenerateScriptResult(true, "Scan Complete", "Missing sounds found!\nDetails in:\n\n" + outputPath);
            }
            else
            {
                if (File.Exists(outputPath)) File.Delete(outputPath);
                return GenerateScriptResult(true, "Scan Complete", "There are no missing sounds!");
            }
        }
        catch (Exception e)
        {
            return GenerateScriptResult(false, "Error", e.ToString());
        }
    }
}

FindMissingSounds.Main();
```

---

## 2. Parallel Processing & Thread Safety

- **Degree of Parallelism**: Always configure via `Build.GetParallelism()`.
- **Counters**: Use `Interlocked.Increment(ref counter)` or `Interlocked.Add(ref total, value)`.
- **Writers/Collections**: Protect shared streams (`StringWriter`) or non-thread-safe collections with `lock (syncObject)`.

```csharp
ParallelOptions po = new ParallelOptions()
{
    MaxDegreeOfParallelism = Build.GetParallelism()
};

Parallel.ForEach(items, po, (item, loopState) =>
{
    // Thread-safe operations
});
```

---

## 3. UI Progress Management (`ScriptProgress`)

```csharp
ScriptProgress.Title = "Processing Assets...";
ScriptProgress.Text = "Initializing...";
ScriptProgress.Indeterminate = true;
ScriptProgress.Value = 0;
ScriptProgress.Maximum = 0;
ScriptProgress.Show();

// During execution:
ScriptProgress.Indeterminate = false;
ScriptProgress.Value = currentIndex;
ScriptProgress.Maximum = totalCount;
ScriptProgress.Text = String.Format("Processing • {0}/{1}", ScriptProgress.Value, ScriptProgress.Maximum);
```
