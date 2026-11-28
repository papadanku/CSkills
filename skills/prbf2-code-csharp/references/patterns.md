
# Code Patterns & Boilerplates for CS-Script (.csx)

## 1. Standard Script Skeleton

Every `.csx` script should follow this established structure, using 4-space indentation, Allman braces, and detailed variable names:

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
    private static ScriptResult GenerateScriptResult(bool isSuccess, string header, string message)
    {
        return new ScriptResult
        {
            Success = isSuccess,
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

        var parallelOptions = new ParallelOptions
        {
            MaxDegreeOfParallelism = Build.GetParallelism()
        };

        try
        {
            string[] soundFilePaths = SoundUtilities.GetFiles(Directories.CurrentModDirectory).ToArray();
            var reportWriter = new StringWriter(CultureInfo.InvariantCulture);

            int processedFileCount = 0;
            int missingSoundCount = 0;
            string errorMessage = null;

            ScriptProgress.Indeterminate = false;
            ScriptProgress.Maximum = soundFilePaths.Length;

            Parallel.ForEach(soundFilePaths, parallelOptions, (soundFilePath, loopState) =>
            {
                ScriptProgress.Value = Interlocked.Increment(ref processedFileCount);
                ScriptProgress.Text = string.Format(
                    "Validating sounds • {0}/{1}",
                    ScriptProgress.Value,
                    ScriptProgress.Maximum
                );

                try
                {
                    Sound soundRecord = SoundUtilities.ValidateFile(soundFilePath);
                    if (soundRecord.MissingSounds.Length > 0)
                    {
                        Interlocked.Increment(ref missingSoundCount);
                        lock (reportWriter)
                        {
                            reportWriter.WriteLine(soundRecord.File);
                            reportWriter.WriteLine("Is missing the following sounds:");
                            foreach (string missingSoundPath in soundRecord.MissingSounds)
                            {
                                reportWriter.WriteLine("\t" + missingSoundPath);
                            }
                            reportWriter.WriteLine();
                        }
                    }
                }
                catch (Exception loopException)
                {
                    errorMessage = loopException.ToString();
                    loopState.Break();
                }
            });

            if (errorMessage != null)
            {
                return GenerateScriptResult(false, "Error", errorMessage);
            }

            string outputPath = Path.Combine(Directories.CurrentModDirectory, "MissingSounds.txt");
            if (missingSoundCount > 0)
            {
                File.WriteAllText(outputPath, reportWriter.ToString());
                return GenerateScriptResult(true, "Scan Complete", "Missing sounds found!\nDetails in:\n\n" + outputPath);
            }
            else
            {
                if (File.Exists(outputPath))
                {
                    File.Delete(outputPath);
                }
                return GenerateScriptResult(true, "Scan Complete", "There are no missing sounds!");
            }
        }
        catch (Exception unhandledException)
        {
            return GenerateScriptResult(false, "Error", unhandledException.ToString());
        }
    }
}

FindMissingSounds.Main();
```

---

## 2. Parallel Processing & Thread Safety

- **Degree of Parallelism**: Always configure via `Build.GetParallelism()`.
- **Counters**: Use `Interlocked.Increment(ref processedCounter)` or `Interlocked.Add(ref totalBytes, itemSize)`.
- **Writers/Collections**: Protect shared streams (`StringWriter`) or non-thread-safe collections with `lock (syncObject)`.

```csharp
var parallelOptions = new ParallelOptions
{
    MaxDegreeOfParallelism = Build.GetParallelism()
};

Parallel.ForEach(assetFilePaths, parallelOptions, (assetFilePath, loopState) =>
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
ScriptProgress.Maximum = totalFileCount;
ScriptProgress.Text = string.Format("Processing • {0}/{1}", ScriptProgress.Value, ScriptProgress.Maximum);
```
