# Bug Patterns

Common bugs and engine-specific pitfalls in Project Reality: BF2 Direct3D 9 / Shader Model 3.0 shaders.

## 1. Logarithmic Depth (`PR_LOG_DEPTH`) & Output Structs

- **Missing `HPos.w + 1.0` in VS**: `RDepth_ApplyLogarithmicDepth(Input.Pos.w)` computes `saturate(log2(Depth) * FCoef)`. In the vertex shader, you must pass `Output.Pos.w = Output.HPos.w + 1.0;` (not `HPos.z` and not `HPos.w` without `+ 1.0`, which causes `log2(<= 0)` NaNs near the camera).
- **Wrong `PS2FB` Struct**: Geometry shaders returning depth must return `RGraphics_PS2FB` (which conditionally declares `float Depth : DEPTH;` under `#if PR_LOG_DEPTH`). SkyDome and post-processing shaders must use `RGraphics_PS2FB_NoDepth` (or `float4 : COLOR0`) so they do not overwrite depth.

## 2. BF2 Vertex Unpacking & Bone Skinning

- **Unpacked vs Packed Vertex Streams**: BF2 compresses `BundledMesh` and `StaticMesh` vertices (`PositionPacked`, `NormalPacked8`, `TangentSpacePacked8`, `TBasePacked2D`).
    - Position: `Input.Pos * PosUnpack` (or `float4(Input.Pos.xyz, 1.0) * PosUnpack` in `RaShaderSTM` where `Input.Pos.w` stores binormal flip).
    - Normal/Tangent: `Input.Normal * NormalUnpack.x + NormalUnpack.y` and `Input.Tan * NormalUnpack.x + NormalUnpack.y`.
    - UV: `Input.TexDiffuse * TexUnpack`.
    - Short-encoded streams (`Undergrowth.fx`): `DECODE_SHORT(x)` (`x / 32767.0`).
- **Bone Index Decoding**: Never index `GeomBones` or `MatBones` directly with raw `float4 Input.BlendIndices`. Always decode via `int4 IndexVector = D3DCOLORtoUBYTE4(Input.BlendIndices);`.
- **Binormal Flipping**:
    - `RaShaderBM` / `RaShaderSM`: `1.0 + IndexVector[2] * -2.0`
    - `RaShaderSTM`: `1.0 + Input.Pos.w * -2.0`
    - Pass this flip into `RVertex_GetTangentBasis(ObjectTangent, ObjectNormal, Flip)` so tangent-space normal maps do not invert on mirrored UVs.

## 3. Color Space (sRGB vs Linear) & Tonemapping

- **Double or Missing Conversion**: `RDirectXTK_SRGBToLinearEst()` and `RDirectXTK_TonemapAndLinearToSRGBEst()` are gated by `#if defined(PR_LINEARLIGHTING)` and `#if defined(PR_TONEMAPPING)`.
    - Convert **color/albedo/emissive/envmap** textures with `RDirectXTK_SRGBToLinearEst(...)`.
    - **Do NOT** run `SRGBToLinearEst` on normal maps, height maps, roughness/gloss masks, or lightmaps unless specifically intended.
    - Always call `RDirectXTK_TonemapAndLinearToSRGBEst(Output.Color)` once at the end of the pixel shader (after fog) before returning.

## 4. Thermal Imaging (TIS) Invariants

- `Ra_IsTisActive()` detects active thermals via `FogColor.r == 0.0` (or `_UnderwaterFog.r == 0` in `SkyDome.fx`; always `false` under `#if defined(_EDITOR_)`).
- TIS encodes heat in the **Green** and **Red** channels (`Fog.r = 0.0; Fog.g = (1.0 - Fog.g) + 0.5;` in `Ra_ApplyFog` / `SkyDome`; `float3(Temp, 1.0, 0.0)` in `RaShaderBM`).
- **Bug**: Applying standard RGB lighting or forgetting `if (Ra_IsTisActive())` overrides in custom shaders breaks thermal contrast or causes unlit objects to glow hot.

## 5. Shader Model 3.0 Compiler & Hardware Pitfalls

- **`tex2D` inside Dynamic Loops/Branches**: D3D9 `ps_3_0` cannot compute implicit screen-space derivatives inside divergent loops or branches. Precompute `ddx(UV)` / `ddy(UV)` outside the branch/loop and use `tex2Dgrad(Sampler, UV, Dx, Dy)` (see `RPixel_GetParallaxTex`, `RPixel_SampleCubicTex2D`).
- **`pow(x, y)` with Negative/Zero Base**: In D3D9 HLSL, `pow(x, y)` evaluates `exp2(y * log2(x))`, which produces `NaN` when `x <= 0`. Always guard with `pow(abs(x), y)` or `pow(max(x, 1e-5), y)`.
- **Uninitialized Struct Members**: Always zero-initialize output structs at the start of VS/PS: `VS2PS Output = (VS2PS)0.0;`. Conditional `#if` blocks that skip assigning a member will otherwise fail compilation.
- **Mismatched VS2PS Semantics & `POSITION` Read**: `POSITION` output in `VS2PS` is write-only for the rasterizer and cannot be read in PS. Pass world/clip position in `TEXCOORDn` (e.g., `float4 Pos : TEXCOORD0;`).
- **Interpolator & Texture Coordinate Limits**: Exceeding SM3.0's 10 `TEXCOORD` interpolator limit or conflicting `TEXCOORDn` indices across `#if` permutations causes compilation failures.
- **Shadow Projection & NVIDIA/Sampler Quirks**:
    - Use `Ra_GetMeshShadowProjection()` (which handles `#if NVIDIA` homogeneous depth `(zL * wT) / wL` vs `zL`).
    - Watch for `_CUSTOMSHADOWSAMPLER_` conflicts when `SampleShadowMap` collides with `TEXLAYERn` sampler registers (e.g., `s3` in `Undergrowth.fx`).
- **Illegal `.mfx` Permutation Combos**: In `RaShaderBM`, `_HASGIMAP_` and `_HASENVMAP_` are mutually exclusive; `_POINTLIGHT_` must disable `_HASGIMAP_`, `_HASENVMAP_`, `_USEHEMIMAP_`, and `_HASSHADOW_`.
- **Alpha Test Reference Mismatch**: Under `PR_ALPHA2MASK` or `PR_HASHED_ALPHA`, `PR_ALPHA_REF` is `1` (otherwise `127`). Using `RPixel_SetHashedAlphaTest` or `RPixel_RescaleAlpha` requires matching alpha scaling (e.g., `Undergrowth.fx` multiplies alpha by `2.0` to compensate).
