
# Coding Conventions

Follow these conventions strictly when writing or modifying HLSL code for RealityShaders (aligned with `README.md` and `pr/shaders/`).

## Case Styles & Naming

- **ALLCAPS**:
    - Render state parameters: `BlendOp = ADD;`, `ZEnable = TRUE;`, `ZFunc = PR_ZFUNC_WITHEQUAL;`
    - System / D3D9 semantics: `POSITION`, `SV_POSITION`, `NORMAL`, `TANGENT`, `BLENDWEIGHT`, `BLENDINDICES`, `TEXCOORD0`, `COLOR0`, `DEPTH`
- **ALL_CAPS**:
    - Preprocessor definitions: `#define SHADER_VERSION`, `#define PR_LOG_DEPTH`, `#define PR_MAX_ANISOTROPY 16`
    - Preprocessor macros & arguments: `#define CREATE_SAMPLER(SAMPLER_NAME, TEXTURE, ADDRESS)`
- **_SnakeCase** (leading underscore + PascalCase):
    - Uniform variables bound from the engine: `uniform float _Example`, `float4x4 _ViewProj : matVIEWPROJ;`, `float4 _CameraPos : CAMERAPOS;`
    - *Compatibility note*: Legacy `RaCommon.fxh` / `RaShader*.fxh` headers use un-prefixed engine-bound names (`World`, `ViewProjection`, `WorldViewProjection`, `PosUnpack`, `Lights[1]`, `GeomBones[26]`, `MatBones[26]`) because the BF2 material system binds them by exact name. Never rename existing engine-bound variables.
- **SnakeCase** (PascalCase):
    - Function arguments: `void Function(int ArgumentOne, float3 WorldPos)`
    - Global constants/variables: `static const float4 GlobalVariable = 1.0;`, `static float FarPlane = 10000.0;`
    - Local variables: `float4 LocalVariable = 1.0;`, `float3 WorldNormal`
    - Textures and samplers: `texture2D ExampleTex : TEXLAYER0;`, `sampler2D SampleExampleTex = sampler_state { ... };`
- **SNAKE_Case / PREFIX_Data**:
    - Struct datatypes:
        - `APP2VS` / `APP2VS_Foobar`: Application to Vertex Shader
        - `VS2PS` / `VS2PS_Foobar`: Vertex Shader to Pixel Shader
        - `PS2FB` / `PS2FB_Foobar` (or `RGraphics_PS2FB`, `RGraphics_PS2FB_NoDepth`): Pixel Shader to Frame Buffer
        - `PS2MRT_Foobar`: Pixel Shader to Multiple Render Targets
    - Shader entry points: `VS_Example(...)`, `PS_Example(...)`
- **Shared Header Methods**:
    - Prefix functions with their module/file namespace:
        - `RealityGraphics.fxh` -> `RGraphics_FunctionName()`
        - `Shared/RealityDepth.fxh` -> `RDepth_FunctionName()`
        - `Shared/RealityDirectXTK.fxh` -> `RDirectXTK_FunctionName()`
        - `Shared/RealityEffects.fxh` -> `REffects_FunctionName()`
        - `Shared/RealityPixel.fxh` -> `RPixel_FunctionName()`
        - `Shared/RealityVertex.fxh` -> `RVertex_FunctionName()`
        - `RaCommon.fxh` -> `Ra_FunctionName()`
        - General `shared/<subdir>/RealityLib.fxh` -> `<Subdir>_RealityLib_FunctionName()`

## File Structure & Include Pattern

Every `.fx` and `.fxh` file uses `#line 2 "Filename.fx"` at line 1, a brief block comment, and the dual-include pattern so both the game engine (`shaders/...`) and BF2Editor / standalone compilers resolve headers cleanly:

```hlsl
#line 2 "Example.fx"

/*
    Brief description of what this shader renders.
*/

#include "shaders/RealityGraphics.fxh"
#include "shaders/shared/RealityPixel.fxh"
#if !defined(_HEADERS_)
    #include "RealityGraphics.fxh"
    #include "shared/RealityPixel.fxh"
#endif
```

Header files wrap their body in:

```hlsl
#if !defined(_HEADERS_)
    #define _HEADERS_
#endif

#if !defined(HEADER_NAME_FXH)
    #define HEADER_NAME_FXH
    // ...
#endif
```

## Sampler & Technique Conventions

- Define samplers with a `CREATE_SAMPLER` macro using `PR_MAX_ANISOTROPY` (16) and quality-tier filter macros (`FILTER_BM_DIFF_MIN/MAG`, `FILTER_STM_DIFF_MIN/MAG`, `FILTER_TRN_DIFF_MIN/MAG`) where applicable.
- Always use `PR_ZFUNC_WITHEQUAL` / `PR_ZFUNC_NOEQUAL` and `PR_DEPTHBIAS_*` / `PR_SLOPESCALE_*` from `RealityGraphics.fxh` rather than hardcoded `LESSEQUAL` or raw bias numbers, preserving `PR_IS_REVERSED_Z` portability.
- Always compile techniques with SM3.0 profiles:

    ```hlsl
    VertexShader = compile vs_3_0 VS_Example();
    PixelShader = compile ps_3_0 PS_Example();
    ```

## Permutations (`.mfx`) & Feature Flags

- `RaShaderBM.mfx`, `RaShaderSM.mfx`, and `RaShaderSTM.mfx` define `LITERAL` flags (e.g., `_hasnormalmap_`, `_usehemimap_`, `_hasshadow_`, `_pointlight_`) that the shader permutator injects as uppercase preprocessor defines (`_HASNORMALMAP_`, `_USEHEMIMAP_`, `_HASSHADOW_`, `_POINTLIGHT_`).
- Always guard optional feature defines with `#if !defined(_FLAG_) #define _FLAG_ 0 #endif` defaults, resolve illegal combinations (e.g., `#if _HASGIMAP_ && _HASENVMAP_ #define _HASENVMAP_ 0 #endif`), and keep `#undef _DEBUG_` before any commented `// #define _DEBUG_` block.
