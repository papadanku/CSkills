# Console Other: Editor, Console, Demo, and Runtime Hosts

## Editor

- `Editor.createNewLayer <std::string>`
    - Returns: `void`
- `Editor.deleteAllLayers`
    - Returns: `void`
- `Editor.deleteAllObjects`
    - Returns: `std::string`
- `Editor.deleteObject <world::IObject_ptrproxy>`
    - Returns: `void`
- `Editor.deleteTemplate <world::IObjectTemplate_ptrproxy>`
    - Returns: `void`
- `Editor.getActiveLayer`
    - Returns: `std::string`
- `Editor.getActiveLayerId`
    - Returns: `int`
- `Editor.getActiveObject`
    - Returns: `world::IObject_ptrproxy`
- `Editor.getActiveObjectTemplate`
    - Returns: `world::IObjectTemplate_ptrproxy`
- `Editor.hideLayer <std::string>`
    - Returns: `void`
- `Editor.listAllVehicles`
    - Returns: `std::string`
- `Editor.listLayers`
    - Returns: `std::string`
- `Editor.listMeshes`
    - Returns: `std::string`
- `Editor.listObjects`
    - Returns: `std::string`
- `Editor.listObjectsOfTemplate <world::IObjectTemplate_ptrproxy>`
    - Returns: `std::string`
- `Editor.listTemplates <std::string>`
    - Returns: `std::string`
- `Editor.listTextures`
    - Returns: `std::string`
- `Editor.loadAllObjects <std::string>`
    - Returns: `bool`
- `Editor.loadAllTemplatesAndObjects`
    - Returns: `bool`
- `Editor.printObjectCreationScript <world::IObject_ptrproxy>`
    - Returns: `std::string`
- `Editor.printTemplateCreationScript <world::IObjectTemplate_ptrproxy>`
    - Returns: `std::string`
- `Editor.quickReloadActiveTemplate`
    - Returns: `void`
- `Editor.quickReloadTemplate <world::IObjectTemplate_ptrproxy>`
    - Returns: `void`
- `Editor.removeLayer <std::string>`
    - Returns: `void`
- `Editor.renameLayer <std::string std::string>`
    - Returns: `void`
- `Editor.saveAllEffects`
    - Returns: `void`
- `Editor.saveAllObjects <std::string>`
    - Returns: `bool`
- `Editor.saveAllSpawners`
    - Returns: `bool`
- `Editor.saveAllTemplates`
    - Returns: `bool`
- `Editor.saveAllTemplatesAndObjects`
    - Returns: `bool`
- `Editor.saveAllUsedTemplates <std::string>`
    - Returns: `bool`
- `Editor.saveFolderToArchive <std::string bool bool>`
    - Returns: `int`
- `Editor.saveSpawners <bool bool bool>`
    - Returns: `void`
- `Editor.saveTemplateToFile <std::string std::string>`
    - Returns: `bool`
- `Editor.saveTemplateTreeStructure <std::string std::string>`
    - Returns: `int`
- `Editor.saveVehicles <bool>`
    - Returns: `bool`
- `Editor.setActiveLayer <std::string>`
    - Returns: `void`
- `Editor.setActiveLayerId <int>`
    - Returns: `void`
- `Editor.setActiveObject <world::IObject_ptrproxy>`
    - Returns: `world::IObject_ptrproxy`
- `Editor.setActiveObjectTemplate <world::IObjectTemplate_ptrproxy>`
    - Returns: `world::IObjectTemplate_ptrproxy`
- `Editor.ShowEntryPoints <bool>`
    - Returns: `bool`
- `Editor.showLayer <std::string>`
    - Returns: `void`
- `Editor.start <world::IObject_ptrproxy>`
    - Returns: `void`
- `Editor.stop <world::IObject_ptrproxy>`
    - Returns: `void`
- `Editor.updateAllTemplates`
    - Returns: `void`
- `Editor.updateTemplate <world::IObjectTemplate_ptrproxy>`
    - Returns: `void`

## Console

- `Console.allowMultipleFileLoad <bool>`
    - Returns: `bool`
- `Console.bindKeyToConsoleScript <int std::string>`
    - Returns: `bool`
- `Console.echo <bool>`
    - Returns: `bool`
- `Console.echoErrors <bool>`
    - Returns: `bool`
- `Console.getActiveMethods <std::string>`
    - Returns: `std::string`
- `Console.getArgumentTypes <std::string std::string>`
    - Returns: `std::string`
- `Console.getCategory <std::string std::string>`
    - Returns: `std::string`
- `Console.getDelta <std::string std::string>`
    - Returns: `std::string`
- `Console.getEnumName <std::string std::string int>`
    - Returns: `std::string`
- `Console.getRange <std::string std::string>`
    - Returns: `std::string`
- `Console.getReturnType <std::string std::string>`
    - Returns: `std::string`
- `Console.getTypeDescription <std::string std::string>`
    - Returns: `std::string`
- `Console.hasBundledType <std::string std::string>`
    - Returns: `std::string`
- `Console.hasRange <std::string std::string>`
    - Returns: `std::string`
- `Console.isDynamic <std::string std::string>`
    - Returns: `std::string`
- `Console.isSetGet <std::string std::string>`
    - Returns: `std::string`
- `Console.listConstants <std::string>`
    - Returns: `std::string`
- `Console.listVariables <std::string>`
    - Returns: `std::string`
- `Console.maxCommandHistorySize <int>`
    - Returns: `int`
- `Console.maxHistorySize <int>`
    - Returns: `int`
- `Console.maxLineSize <int>`
    - Returns: `int`
- `Console.run <std::string std::string std::string>`
    - Returns: `std::string`
- `Console.useRelativePaths <bool>`
    - Returns: `bool`
- `Console.workingPath <std::string>`
    - Returns: `std::string`

## Demo

- `demo.recordDemo <std::string>`
    - Returns: `void`

    Starts the Battlerecorder Recording. Needs to specify a name. File is saved in mods/(mod)/Demos. In My Documents/Project Reality/Profile/001 (i.e 002, 003, default) create a demos folder and place both files there.

- `demo.restartDemo`
    - Returns: `void`
- `demo.shutdownDemo`
    - Returns: `void`
- `demo.stopRecording`
    - Returns: `void`

    Console ~ Command

    Stops the Battlerecorder Recording. File is saved in mods/(mod)/Demos. In My Documents/Battlefield 2/Profile/001 etc create a demos folder and place both files there.

- `demo.toggleCameraDemo`
    - Returns: `void`
- `demo.toggleDemoPauseOrPlay`
    - Returns: `void`
- `demo.togglePlayerDemo <bool>`
    - Returns: `void`

## File Manager

- `fileManager.addPath <std::string>`
    - Returns: `void`
- `fileManager.copyFile <std::string std::string>`
    - Returns: `bool`
- `fileManager.deleteFile <std::string>`
    - Returns: `bool`
- `fileManager.fileExists <std::string>`
    - Returns: `bool`
- `fileManager.mountArchive <std::string std::string bool>`
    - Returns: `void`
- `fileManager.moveFile <std::string std::string>`
    - Returns: `bool`

## Swiff Host

- `swiffHost.addAward <int int int>`
    - Returns: `void`
- `swiffHost.addCredit <std::string int>`
    - Returns: `void`
- `swiffHost.addGameMode <std::string std::string>`
    - Returns: `void`
- `swiffHost.addRank <int int int>`
    - Returns: `void`
- `swiffHost.enableScroller <bool>`
    - Returns: `void`
- `swiffHost.loadImage <std::string>`
    - Returns: `bool`
- `swiffHost.serverBrowserFrameSkips <int>`
    - Returns: `int`
- `swiffHost.setScrollerRect <int int int>`
    - Returns: `void`
- `swiffHost.setScrollFadeSpeed <int>`
    - Returns: `void`
- `swiffHost.setScrollSpeed <float>`
    - Returns: `void`

## Python Host

- `pythonHost.reinitialize`
    - Returns: `bool`
- `pythonHost.sendCommand <std::string std::string std::string>`
    - Returns: `bool`

## Portal

- `portal.debugLevel <int>`
    - Returns: `int`
- `portal.showStats <bool>`
    - Returns: `bool`
