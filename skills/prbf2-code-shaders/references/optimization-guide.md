
# Optimization Guide

Shader Model 3.0 (`vs_3_0` / `ps_3_0`) optimization practices for Project Reality: Battlefield 2.

## 1. Interpolator & Register Budgets (SM3.0)

- **Hardware Limits**:
    - `vs_3_0`: 256 `float4` constant registers (`c0`-`c255`), 16 vertex input streams, 10-12 `TEXCOORD` output interpolators.
    - `ps_3_0`: 224 `float4` constant registers, 16 texture samplers (`s0`-`s15`), 10 `TEXCOORD` input interpolators.
- **Pack `TEXCOORDn` Interpolators**: Always pack two `float2` UVs or scalar values into a single `float4` interpolator to minimize VS-to-PS bandwidth and avoid hitting interpolator limits:
    - `float4 BaseAndDetail : TEXCOORD1; // .xy = BaseTex; .zw = DetailTex;` (`RaShaderSTM.fx`)
    - `float3 Tex0AndOccShadowTex : TEXCOORD1; // .xy = Tex0; .z = OccShadowTex` (`RaShaderSM.fx`)
    - Pack logarithmic depth into `Pos.w` (`Output.Pos.w = Output.HPos.w + 1.0;`).
- **Keep Bone & Sway Arrays Compact**: `GeomBones[26]` and `MatBones[26]` use `float4x3` (3 registers per bone = 78 registers), leaving room for view/projection/light constants.

## 2. Fullscreen & Post-Processing Optimizations

- **Fullscreen Triangle Trick**: Use `GetFSTriangle()` (`PostProduction_nv3x.fx`) to transform a fullscreen quad into a single oversized triangle, eliminating diagonal quad-seam helper-lane waste and redundant vertex work.
- **Interleaved Gradient / Golden Ratio Noise**: Prefer `RPixel_GetInterleavedGradientNoise()` or `RPixel_GetGoldenRatioNoise()` over multi-octave hash noise for dithering and film grain.

## 3. Texture Sampling & Filtering

- **4-Tap Bicubic Lightmapping**: Use `RPixel_SampleLightMap()` / `RPixel_SampleLightMapProj()` (`RealityPixel.fxh`), which evaluates bicubic B-spline filtering (`RPixel_Cubic`) in only **4 bilinear `tex2Dgrad` taps** instead of 16 point taps.
- **Procedural Tiling**: Use `RPixel_GetProceduralTiles()` for off-map/sky/terrain repetition breaking; it computes `ddx`/`ddy` once and uses 2 `tex2Dgrad` taps blended via value noise.
- **Adaptive Parallax Occlusion Mapping**: `RPixel_GetParallaxTex()` scales ray-march steps from 32 (grazing angles) down to 8 (steep/perpendicular angles) and hoists `ddx(Tex)` / `ddy(Tex)` outside the `while` loop.
- **Alpha Testing Over Alpha Blending**: Prefer `AlphaTestEnable = TRUE` with `PR_ALPHA_REF` + `RPixel_SetHashedAlphaTest()` or `RPixel_RescaleAlpha()` for foliage (`Undergrowth.fx`, `RaShaderLeaf.fx`) to avoid expensive draw-order sorting and overdraw.

## 4. Instruction-Level & Math Optimizations

- **Squared Distance for Attenuation & Morphing**: Avoid `length()` / `distance()` when comparing or attenuating - use `dot(v, v)` (see `RPixel_GetLightAttenuation` and `GetCameraDistance` in `TerrainShader.fxh`).
- **Simultaneous Trig**: Use `sincos(Angle, s, c)` when both `sin` and `cos` are needed (e.g., `REffects_GetSpiralBlur`).
- **Inverse Square Root**: Use `rsqrt(x)` instead of `1.0 / sqrt(x)` (e.g., `RDirectXTK_CalculateTBN`, `RPixel_SetHashedAlphaTest`).
- **Dot Product for Channel Sums/Means**: Use `dot(Color.rgb, 1.0 / 3.0)` (`RPixel_GetMean_FLT3`) or `dot(Color.rgb, 1.0)` instead of `c.r + c.g + c.b`.
- **MAD-Friendly Expressions**: Express affine transforms as `A * Scale + Offset` (`HPos * _TexProjScale + (_TexProjOffset * HPos.w)` in `ProjToLighting`) so the compiler emits single-cycle `mad` instructions.
- **Half-Lambert Lighting**: Use `RDirectXTK_ToHalfNL()` / `RDirectXTK_ComputeLights()` for cheap, smooth wrap-around diffuse lighting (`(dot(N, L) * 0.5 + 0.5)^2`).

## 5. Reuse Shared Headers

Before writing new utility math, check:

- `RealityGraphics.fxh` (`RGraphics_*`)
- `Shared/RealityDepth.fxh` (`RDepth_*`)
- `Shared/RealityDirectXTK.fxh` (`RDirectXTK_*`)
- `Shared/RealityPixel.fxh` (`RPixel_*`)
- `Shared/RealityVertex.fxh` (`RVertex_*`)
- `Shared/RealityEffects.fxh` (`REffects_*`)
- `RaCommon.fxh` (`Ra_*`)
