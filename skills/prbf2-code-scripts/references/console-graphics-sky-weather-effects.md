# Console Graphics: Skydome, Weather, Particles, and Effects

## Skydome

- `skyDome.cloudLerpFactors <Vec2>`
    - Returns: `Vec2`
- `skyDome.cloudTemplate <std::string>`
    - Returns: `std::string`
- `skyDome.cloudTexture <std::string>`
    - Returns: `std::string`
- `skyDome.cloudTexture2 <std::string>`
    - Returns: `std::string`
- `skyDome.domePosition <Vec3>`
    - Returns: `Vec3`
- `skyDome.domeRotation <float>`
    - Returns: `float`
- `skyDome.domeSize <float>`
    - Returns: `float`
- `skyDome.fadeCloudsDistances <Vec2>`
    - Returns: `Vec2`
- `skyDome.flareDirection <Vec3>`
    - Returns: `Vec3`
- `skyDome.flareFadeAdd <float>`
    - Returns: `float`
- `skyDome.flareFadeMul <float>`
    - Returns: `float`
- `skyDome.flareTemplate <std::string>`
    - Returns: `std::string`
- `skyDome.flareTexture <std::string>`
    - Returns: `std::string`
    - Map: `Sky.con`
    - The texture of the sunflare/actual sunflare.
    - When switching to a map with no sunflare, it will still use the previous maps one.
    - So for maps like Fallujah West/Saaremaa, an invisible texture needs to be defined instead to prevent the sunflare bug.
    - Usage: `Skydome.flareTexture common\textures\sunflare\Sunglow_no`
- `skyDome.hasCloudLayer <bool>`
    - Returns: `bool`
- `skyDome.hasCloudLayer2 <bool>`
    - Returns: `bool`
- `skyDome.lightingBlend <float>`
    - Returns: `float`
- `skyDome.lightingColor <Vec3>`
    - Returns: `Vec3`
- `skyDome.scrollDirection <Vec2>`
    - Returns: `Vec2`
- `skyDome.scrollDirection2 <Vec2>`
    - Returns: `Vec2`
- `skyDome.skyTemplate <std::string>`
    - Returns: `std::string`
- `skyDome.skyTexture <std::string>`
    - Returns: `std::string`

## Weather

### weatherManager

- `weatherManager.doubleStrikeMaxDelay <float>`
    - Returns: `float`
- `weatherManager.doubleStrikeMinDelay <float>`
    - Returns: `float`
- `weatherManager.doubleStrikeProbability <float>`
    - Returns: `float`
- `weatherManager.inFadeSegments <float>`
    - Returns: `float`
- `weatherManager.lightningBlendOutTime <float>`
    - Returns: `float`
- `weatherManager.lightningColor <Vec4>`
    - Returns: `Vec4`
- `weatherManager.lightningDuration <float>`
    - Returns: `float`
- `weatherManager.lightningGroundPenetration <float>`
    - Returns: `float`
- `weatherManager.lightningMaxInterval <float>`
    - Returns: `float`
- `weatherManager.lightningMaxPos <Vec3>`
    - Returns: `Vec3`
- `weatherManager.lightningMinInterval <float>`
    - Returns: `float`
- `weatherManager.lightningMinPos <Vec3>`
    - Returns: `Vec3`
- `weatherManager.lightningPertubation <float>`
    - Returns: `float`
- `weatherManager.lightningScale <Vec2>`
    - Returns: `Vec2`
- `weatherManager.lightningSegments <int>`
    - Returns: `int`
- `weatherManager.lightningSFXDelay <float>`
    - Returns: `float`
- `weatherManager.lightningSFXName <std::string>`
    - Returns: `std::string`
- `weatherManager.outFadeSegments <float>`
    - Returns: `float`
- `weatherManager.skyBlendOutTime <float>`
    - Returns: `float`
- `weatherManager.stormEnabled <bool>`
    - Returns: `bool`

### windManager

- `windManager.globalWindDirection <Vec3>`
    - Returns: `Vec3`
- `windManager.globalWindSpeed <float>`
    - Returns: `float`

## Particles

### particles

- `Particles.enableOldParticles <bool>`
    - Returns: `bool`
- `Particles.enableParticles <bool>`
    - Returns: `bool`

### particleSystemManager

- `particleSystemManager.affectedByWind <bool>`
    - Returns: `bool`
- `particleSystemManager.drawBoundingBoxEnable <bool>`
    - Returns: `bool`
- `particleSystemManager.drawStats <bool>`
    - Returns: `bool`
- `particleSystemManager.generateTexture`
    - Returns: `bool`
- `particleSystemManager.overdrawScale <float>`
    - Returns: `float`
- `particleSystemManager.particleSystemShaderQuality <uint>`
    - Returns: `uint`
- `particleSystemManager.qualityLevel <int>`
    - Returns: `int`
- `particleSystemManager.resetStats`
    - Returns: `void`
- `particleSystemManager.startFadePercentageOfViewDistance <float>`
    - Returns: `float`
- `particleSystemManager.startLodPercentageOfLodDistance <float>`
    - Returns: `float`
- `particleSystemManager.viewDistance <float>`
    - Returns: `float`

## Effect Tweak

- `effectTweak.setAgeScaleFactorForAllEffects <float>`
    - Returns: `void`
- `effectTweak.setAlphaIntensityForAllEffects <float>`
    - Returns: `void`
- `effectTweak.setEmitScaleFactorForAllEffects <float>`
    - Returns: `void`
- `effectTweak.setEmitSpeedScaleFactorForAllEffects <float>`
    - Returns: `void`
- `effectTweak.setSoundIntensity <float>`
    - Returns: `void`
- `effectTweak.setStartAgeForAllEffects <float>`
    - Returns: `void`
