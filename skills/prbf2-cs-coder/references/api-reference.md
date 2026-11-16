
# Common Utilities & API Reference (`Common/*.csx`)

Project Reality BF2 CS-Script scripts rely heavily on a shared library of helper scripts loaded via `#load "Common/..."`. Below is the API reference for core utility modules.

## 1. `Common/Files.csx`

Provides efficient file/directory enumeration and object template parsing.

- **`EnumerateFiles(string dir, string filter, SearchOption searchOption, int folderOffset = 0, Func<string, bool> predicate = null, bool cutPath = false)`**: Recursively scans directories in parallel (`AsParallel()`), returning matching file paths.
- **`EnumerateDirectories(...)`**: Analogous parallel directory enumeration.
- **`GetTemplates(IEnumerable<string> templateFiles)`**: Parses `.con` and object template files concurrently, returning a `ConcurrentDictionary<string, ObjectTemplate>`.

## 2. `Common/ConFileParser.csx`

Parses Battlefield 2 `.con` configuration files.

- **`ConFileParser.ReadCon(string conFilePath)`**: Reads a `.con` file line by line, handling `ObjectTemplate.create`, `ObjectTemplate.activeSafe`, property assignments, and recursive `include`/`run` directives. Returns a `ConFile` instance containing `ParsedTemplate` objects.

## 3. `Common/Sound.csx`

Validates and collects sound configuration files and audio assets.

- **`SoundUtilities.GetFiles(string modDir)`**: Collects sound configuration files across the mod directory.
- **`SoundUtilities.ValidateFile(string soundFilePath)`**: Validates sound references in `.con`/`.tweak` files against physical files on disk, returning a `Sound` object containing `MissingSounds`.

## 4. `Reality.BF2.Build` & `Reality.BF2.Console`

- **`Build.GetParallelism()`**: Returns the optimal degree of parallel execution configured for the build environment.
- **`ScriptProgress`**: Static UI controller managing `Title`, `Text`, `Value`, `Maximum`, `Indeterminate`, and `Show()`.
- **`ScriptResult`**: Return structure containing `Success` (bool), `Header` (string), and `Message` (string).
- **`Directories`**: Provides mod paths (`Directories.CurrentModDirectory`, `Directories.CurrentModLevelsDirectory`).
