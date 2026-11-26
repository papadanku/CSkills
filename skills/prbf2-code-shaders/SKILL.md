---
name: prbf2-code-shaders
description: Expert Shader Assistant for RealityShaders (Project Reality Battlefield 2). Use when finding bugs in HLSL, generating new shader code, or optimizing existing .fx, .fxh, and .mfx files for Direct3D 9 / Shader Model 3.0.
---

# prbf2-code-shaders

Expert Shader Assistant for RealityShaders, specializing in HLSL Shader Model 3.0 (`vs_3_0` / `ps_3_0`) for Project Reality: Battlefield 2 (Direct3D 9 / Refactor 2 engine).

## Workflow

1. **Identify Task & Scope**: Determine whether the request is bug finding, new shader/feature generation, or optimization, and which mesh/pass family it targets (`RaShaderBM`, `RaShaderSM`, `RaShaderSTM`, `TerrainShader`, `Undergrowth`, `RaShaderLeaf`, `RaShaderWater*`, `SkyDome`, `PostProduction_nv3x`, `Particles`, or `Shared/*.fxh`).
2. **Check Shared Libraries & Toggles**: Reuse existing functions in `RealityGraphics.fxh`, `Shared/*.fxh`, and `RaCommon.fxh`, and respect compile-time toggles from `SettingsDefines.fxh` (`PR_LOG_DEPTH`, `PR_LINEARLIGHTING`, `PR_TONEMAPPING`, `PR_PARALLAX`, `PR_BICUBIC_LIGHTMAPPING`, `PR_HASHED_ALPHA`, `PR_ALPHA2MASK`, `PR_IS_REVERSED_Z`).
3. **Apply Conventions & SM3.0 Rules**:
    - **Conventions**: Consult [conventions.md](references/conventions.md) for strict casing, struct prefixes, dual-include guards, sampler macros, and `.mfx` permutation rules.
    - **Bug Finding**: Consult [bug-patterns.md](references/bug-patterns.md) for D3D9 SM3.0 pitfalls, vertex unpacking, logarithmic depth, linear/sRGB mismatches, and TIS thermal invariants.
    - **Optimization**: Consult [optimization-guide.md](references/optimization-guide.md) for interpolator packing, `tex2Dgrad` in loops, 4-tap bicubic sampling, fullscreen triangle rendering, and register budgets.
4. **Verify**: Ensure all structs match across VS/PS, all `Output` structs are zero-initialized `(StructType)0.0`, all techniques compile `vs_3_0` / `ps_3_0`, and no `.mfx` permutation conflicts are introduced.

## PR:BF2 Architecture Overview

- **Directory Layout**:
    - `pr/shaders/` - `.fx` effect files, `.fxh` headers, `.mfx` permutation definitions (`RaShaderBM.mfx`, `RaShaderSM.mfx`, `RaShaderSTM.mfx`).
    - `pr/shaders/Shared/` - Modular utility headers (`RealityDepth.fxh`, `RealityDirectXTK.fxh`, `RealityEffects.fxh`, `RealityPixel.fxh`, `RealityVertex.fxh`).
    - `pr/shaders_high/SettingsDefines.fxh` & `pr/shaders_low/SettingsDefines.fxh` - Quality-tier compile-time `#define` switches included via `RealityGraphics.fxh`.
- **Shared Header Ecosystem**:
    - `RealityGraphics.fxh` (`RGraphics_*`): `RGraphics_PS2FB` / `RGraphics_PS2FB_NoDepth`, `PR_*` depth/Z-func/bias/anisotropy/alpha-ref constants, UNORM/SNORM conversion macros.
    - `Shared/RealityDepth.fxh` (`RDepth_*`): `RDepth_ApplyLogarithmicDepth`, `RDepth_GetSlopedBasedBias`, `RDepth_GetMeshShadowProjection`, `RDepth_GetShadowFactor` (4-tap PCF).
    - `Shared/RealityDirectXTK.fxh` (`RDirectXTK_*`): `RDirectXTK_SRGBToLinearEst`, `RDirectXTK_TonemapAndLinearToSRGBEst` (AMD Resolve / ACES Filmic), `RDirectXTK_ComputeLights` (Half-Lambert Blinn-Phong), `RDirectXTK_CompositeLights`, `RDirectXTK_ComputeFresnelFactor`, `RDirectXTK_CalculateTBN` (tangentless).
    - `Shared/RealityPixel.fxh` (`RPixel_*`): Value/gradient/IG/golden-ratio noise, `RPixel_GetProceduralTiles`, `RPixel_GetParallaxTex` (adaptive POM), `RPixel_SetHashedAlphaTest`, `RPixel_RescaleAlpha`, `RPixel_SampleLightMap` / `RPixel_SampleLightMapProj` (4-tap bicubic).
    - `Shared/RealityVertex.fxh` (`RVertex_*`): `RVertex_GetTangentBasis` (Gram-Schmidt TBN).
    - `Shared/RealityEffects.fxh` (`REffects_*`): FidelityFX Lens (CA, vignette, film grain), `REffects_GetSpiralBlur`.
    - `RaCommon.fxh` (`Ra_*`): `Ra_IsTisActive()`, `Ra_GetFogValue()`, `Ra_ApplyFog()`, `Ra_GetMeshShadowProjection()`, `Ra_GetTerrainLight()`, `DECODE_SHORT()`.

## Guidelines

- **Surgical Changes**: Only modify what is necessary; preserve BF2 engine-bound parameter names and semantics.
- **Strict SM3.0 Target**: Always compile techniques with `vs_3_0` and `ps_3_0`.
- **Convention Strictness**: Follow `README.md` naming (`_SnakeCase` uniforms, `SnakeCase` locals/args/samplers, `ALLCAPS` states/semantics, `ALL_CAPS` macros, `PREFIX_Data` structs, `VS_`/`PS_` entry points).
- **Precision & Space Discipline**: Keep world/projection/depth math in `float`; work in linear space inside `PR_LINEARLIGHTING` blocks; normalize interpolated vectors in PS.

## References

- [Coding Conventions](references/conventions.md)
- [Bug Patterns](references/bug-patterns.md)
- [Optimization Guide](references/optimization-guide.md)
