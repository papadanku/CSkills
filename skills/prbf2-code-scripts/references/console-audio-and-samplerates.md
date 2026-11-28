# Console: Audio, Sound, and Sample Rates

## Audio

- `audioSettings.alwaysAllowSystemOpenAL <bool>`
    - Returns: `bool`
- `audioSettings.effectsVolume <float>`
    - Returns: `float`
- `audioSettings.enableEAX <bool>`
    - Returns: `bool`
- `audioSettings.englishOnlyVoices <bool>`
    - Returns: `bool`
- `audioSettings.forceNumberOfVoices <int>`
    - Returns: `int`
- `audioSettings.helpVoiceVolume <float>`
    - Returns: `float`
- `audioSettings.musicVolume <float>`
    - Returns: `float`
- `audioSettings.provider <std::string>`
    - Returns: `std::string`
- `audioSettings.soundQuality <std::string>`
    - Returns: `std::string`
- `audioSettings.voipBoostEnabled <bool>`
    - Returns: `bool`
- `audioSettings.voipCaptureThreshold <float>`
    - Returns: `float`
- `audioSettings.voipCaptureVolume <float>`
    - Returns: `float`
- `audioSettings.voipEnabled <bool>`
    - Returns: `bool`
- `audioSettings.voipPlaybackVolume <float>`
    - Returns: `float`
- `audioSettings.voipUsePushToTalk <bool>`
    - Returns: `bool`
- `bf2Engine.playMovie <std::string int>`
    - Returns: `void`
- `chat.sayAll <std::string>`
    - Returns: `void`
    - Description: All chat
    - Used in: Menu (Hud Elements `Chat.con`), `HudElementsChat.con`
- `chat.sayTeam <std::string>`
    - Returns: `void`
    - Description: Team chat
    - Used in: Menu (Hud Elements `Chat.con`), `HudElementsChat.con`

## Sound

- `sound.addMenuSound <std::string std::string float>`
    - Returns: `void`
- `sound.addSound <std::string>`
    - Returns: `void`
- `sound.addTrigger <std::string>`
    - Returns: `void`
- `sound.dopplerEffect <float>`
    - Returns: `float`
- `sound.getAllSoundTemplates`
    - Returns: `std::string`
- `sound.getProperty <std::string>`
    - Returns: `std::string`
- `sound.getVolumeForGroup <int>`
    - Returns: `float`
- `sound.initialize <int std::string int>`
    - Returns: `SoundInitResult`
- `sound.interactiveMode <bool>`
    - Returns: `bool`
- `sound.listenerReverb <float>`
    - Returns: `float`
- `sound.loadMusic <std::string>`
    - Returns: `bool`
- `sound.masterVolume <float>`
    - Returns: `float`
- `sound.playMusic`
    - Returns: `bool`
- `sound.playSound <std::string>`
    - Returns: `void`
- `sound.removeAllTriggers`
    - Returns: `void`
- `sound.setProperty <std::string float>`
    - Returns: `void`
- `sound.setReverb <std::string>`
    - Returns: `void`
- `sound.setVolumeForGroup <int float>`
    - Returns: `void`
- `sound.showSoundSources <bool>`
    - Returns: `bool`
- `sound.showStats <bool>`
    - Returns: `bool`
- `Sound.startEngines <bool>`
    - Returns: `bool`
- `sound.stopMusic <float>`
    - Returns: `bool`
- `sound.stopSound <std::string>`
    - Returns: `void`
- `sound.tinnitusSetup <std::string float float>`
    - Returns: `void`
- `sound.tweakTemplate <std::string float float>`
    - Returns: `void`
- `sound.windSetup <std::string float>`
    - Returns: `void`

## Sample Rates

This tutorial explains the mass conversion of audio sample rates while preserving sound region markers.

### Sound Forge 12 Pro Suite

Sound Forge 12 Pro Suite is the recommended tool for this task because it preserves sound markers during conversion. It also maintains original mono and stereo settings, preventing engine strain caused by improper stereo conversion of mono audio files.

Loopable sounds, such as engine idle, automatic rifle firing, or helicopter rotors, retain their characteristics when sample rates are modified.

### Identifying Sample Rates

To view the sampling rate of `*.wav` files in Windows Explorer:

1. Set the view to `Details` mode.
2. Enable the `Bit Rate` column:
    - Right-click a column header.
    - Select `More...`.
    - Check `Bit Rate` and click `OK`.

Use the following table to identify sample rates based on bit rates:

- Bit Rate
    - Sample Rate
    - Channels
- 176 kbps
    - 11.025 kHz
    - Stereo
- 352 kbps
    - 22.05 kHz
    - Mono
- 705 kbps
    - 44.1 kHz
    - Mono
- 768 kbps
    - 48 kHz
    - Mono
- 1411 kbps
    - 44.1 kHz
    - Stereo
- 1536 kbps
    - 48 kHz
    - Stereo

Alternatively, use tools such as `MediaInfo` or `Wave Agent Beta` to verify sampling rates, channel counts, and bit depths.

### Converting from 44.1 kHz to 48.0 kHz

Use the Batch Converter in Sound Forge Pro 12 Suite with the following configuration:

1. `Files to convert tab`: Add the target files.
2. `In Process tab`:
    - Select `Resample` from the `Menu` dropdown.
    - Click `Add Effect`.
    - Select the preset `[Sys] Resample to 48,000 Hz with anti-alias filter`.
    - Select `Set the sample rate only (do not resample)`.
    - Click `OK`.
3. `Save tab`:
    - Click `Add Save Options`.
    - Set all three options to `Same as Source`.
    - Click `OK`.
4. Click `Run Job`.

#### Handling Low Sample Rates

When upsampling files below 44.1 kHz (e.g., 11.025 kHz or 22.05 kHz) to 48 kHz, use the `Resample 2` feature. The standard conversion settings (44.1 to 48) can reduce audio quality for these files.

### .ogg Serialization

Battlefield 2 utilizes serialization to enable `*.ogg` sound playback over a network, which is required for offline and online gameplay.

Converting `*.ogg` files removes serialization, causing audio playback failure. To preserve serialization, convert `*.ogg` files to `*.wav` format in Sound Forge without resampling, then resample each sound file individually.
