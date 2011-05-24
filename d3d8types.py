##########################################################################
#
# Copyright 2008-2009 VMware, Inc.
# All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
##########################################################################/

"""d3d8types.h"""

from winapi import *

D3DCOLOR = Alias("D3DCOLOR", DWORD)

D3DVECTOR = Struct("D3DVECTOR", [
    (Float, "x"),
    (Float, "y"),
    (Float, "z"),
])

D3DCOLORVALUE = Struct("D3DCOLORVALUE", [
    (Float, "r"),
    (Float, "g"),
    (Float, "b"),
    (Float, "a"),
])

D3DRECT = Struct("D3DRECT", [
    (LONG, "x1"),
    (LONG, "y1"),
    (LONG, "x2"),
    (LONG, "y2"),
])

D3DMATRIX = Struct("D3DMATRIX", [
    (Array(Array(Float, "4"), "4"), "m"),
])

D3DVIEWPORT8 = Struct("D3DVIEWPORT8", [
    (DWORD, "X"),
    (DWORD, "Y"),
    (DWORD, "Width"),
    (DWORD, "Height"),
    (Float, "MinZ"),
    (Float, "MaxZ"),
])

D3DCLIP = Flags(DWORD, [
    "D3DCLIPPLANE0",
    "D3DCLIPPLANE1",
    "D3DCLIPPLANE2",
    "D3DCLIPPLANE3",
    "D3DCLIPPLANE4",
    "D3DCLIPPLANE5",
])

D3DCS = Flags(DWORD, [
    "D3DCS_ALL",
    "D3DCS_LEFT",
    "D3DCS_RIGHT",
    "D3DCS_TOP",
    "D3DCS_BOTTOM",
    "D3DCS_FRONT",
    "D3DCS_BACK",
    "D3DCS_PLANE0",
    "D3DCS_PLANE1",
    "D3DCS_PLANE2",
    "D3DCS_PLANE3",
    "D3DCS_PLANE4",
    "D3DCS_PLANE5",
])

D3DCLIPSTATUS8 = Struct("D3DCLIPSTATUS8", [
    (DWORD, "ClipUnion"),
    (DWORD, "ClipIntersection"),
])

D3DMATERIAL8 = Struct("D3DMATERIAL8", [
    (D3DCOLORVALUE, "Diffuse"),
    (D3DCOLORVALUE, "Ambient"),
    (D3DCOLORVALUE, "Specular"),
    (D3DCOLORVALUE, "Emissive"),
    (Float, "Power"),
])

D3DLIGHTTYPE = Enum("D3DLIGHTTYPE", [
    "D3DLIGHT_POINT",
    "D3DLIGHT_SPOT",
    "D3DLIGHT_DIRECTIONAL",
])

D3DLIGHT8 = Struct("D3DLIGHT8", [
    (D3DLIGHTTYPE, "Type"),
    (D3DCOLORVALUE, "Diffuse"),
    (D3DCOLORVALUE, "Specular"),
    (D3DCOLORVALUE, "Ambient"),
    (D3DVECTOR, "Position"),
    (D3DVECTOR, "Direction"),
    (Float, "Range"),
    (Float, "Falloff"),
    (Float, "Attenuation0"),
    (Float, "Attenuation1"),
    (Float, "Attenuation2"),
    (Float, "Theta"),
    (Float, "Phi"),
])

D3DCLEAR = Flags(DWORD, [
    "D3DCLEAR_TARGET",
    "D3DCLEAR_ZBUFFER",
    "D3DCLEAR_STENCIL",
])

D3DSHADEMODE = Enum("D3DSHADEMODE", [
    "D3DSHADE_FLAT",
    "D3DSHADE_GOURAUD",
    "D3DSHADE_PHONG",
])

D3DFILLMODE = Enum("D3DFILLMODE", [
    "D3DFILL_POINT",
    "D3DFILL_WIREFRAME",
    "D3DFILL_SOLID",
])

D3DLINEPATTERN = Struct("D3DLINEPATTERN", [
    (WORD, "wRepeatFactor"),
    (WORD, "wLinePattern"),
])

D3DBLEND = Enum("D3DBLEND", [
    "D3DBLEND_ZERO",
    "D3DBLEND_ONE",
    "D3DBLEND_SRCCOLOR",
    "D3DBLEND_INVSRCCOLOR",
    "D3DBLEND_SRCALPHA",
    "D3DBLEND_INVSRCALPHA",
    "D3DBLEND_DESTALPHA",
    "D3DBLEND_INVDESTALPHA",
    "D3DBLEND_DESTCOLOR",
    "D3DBLEND_INVDESTCOLOR",
    "D3DBLEND_SRCALPHASAT",
    "D3DBLEND_BOTHSRCALPHA",
    "D3DBLEND_BOTHINVSRCALPHA",
])

D3DBLENDOP = Enum("D3DBLENDOP", [
    "D3DBLENDOP_ADD",
    "D3DBLENDOP_SUBTRACT",
    "D3DBLENDOP_REVSUBTRACT",
    "D3DBLENDOP_MIN",
    "D3DBLENDOP_MAX",
])

D3DTEXTUREADDRESS = Enum("D3DTEXTUREADDRESS", [
    "D3DTADDRESS_WRAP",
    "D3DTADDRESS_MIRROR",
    "D3DTADDRESS_CLAMP",
    "D3DTADDRESS_BORDER",
    "D3DTADDRESS_MIRRORONCE",
])

D3DCULL = Enum("D3DCULL", [
    "D3DCULL_NONE",
    "D3DCULL_CW",
    "D3DCULL_CCW",
])

D3DCMPFUNC = Enum("D3DCMPFUNC", [
    "D3DCMP_NEVER",
    "D3DCMP_LESS",
    "D3DCMP_EQUAL",
    "D3DCMP_LESSEQUAL",
    "D3DCMP_GREATER",
    "D3DCMP_NOTEQUAL",
    "D3DCMP_GREATEREQUAL",
    "D3DCMP_ALWAYS",
])

D3DSTENCILOP = Enum("D3DSTENCILOP", [
    "D3DSTENCILOP_KEEP",
    "D3DSTENCILOP_ZERO",
    "D3DSTENCILOP_REPLACE",
    "D3DSTENCILOP_INCRSAT",
    "D3DSTENCILOP_DECRSAT",
    "D3DSTENCILOP_INVERT",
    "D3DSTENCILOP_INCR",
    "D3DSTENCILOP_DECR",
])

D3DFOGMODE = Enum("D3DFOGMODE", [
    "D3DFOG_NONE",
    "D3DFOG_EXP",
    "D3DFOG_EXP2",
    "D3DFOG_LINEAR",
])

D3DZBUFFERTYPE = Enum("D3DZBUFFERTYPE", [
    "D3DZB_FALSE",
    "D3DZB_TRUE",
    "D3DZB_USEW",
])

D3DPRIMITIVETYPE = Enum("D3DPRIMITIVETYPE", [
    "D3DPT_POINTLIST",
    "D3DPT_LINELIST",
    "D3DPT_LINESTRIP",
    "D3DPT_TRIANGLELIST",
    "D3DPT_TRIANGLESTRIP",
    "D3DPT_TRIANGLEFAN",
])

D3DTRANSFORMSTATETYPE = Enum("D3DTRANSFORMSTATETYPE", [
    "D3DTS_VIEW",
    "D3DTS_PROJECTION",
    "D3DTS_TEXTURE0",
    "D3DTS_TEXTURE1",
    "D3DTS_TEXTURE2",
    "D3DTS_TEXTURE3",
    "D3DTS_TEXTURE4",
    "D3DTS_TEXTURE5",
    "D3DTS_TEXTURE6",
    "D3DTS_TEXTURE7",
])

D3DTS = Flags(DWORD, [
    "D3DTS_WORLD",
    "D3DTS_WORLD1",
    "D3DTS_WORLD2",
    "D3DTS_WORLD3",
])

D3DRENDERSTATETYPE = Enum("D3DRENDERSTATETYPE", [
    "D3DRS_ZENABLE",
    "D3DRS_FILLMODE",
    "D3DRS_SHADEMODE",
    "D3DRS_LINEPATTERN",
    "D3DRS_ZWRITEENABLE",
    "D3DRS_ALPHATESTENABLE",
    "D3DRS_LASTPIXEL",
    "D3DRS_SRCBLEND",
    "D3DRS_DESTBLEND",
    "D3DRS_CULLMODE",
    "D3DRS_ZFUNC",
    "D3DRS_ALPHAREF",
    "D3DRS_ALPHAFUNC",
    "D3DRS_DITHERENABLE",
    "D3DRS_ALPHABLENDENABLE",
    "D3DRS_FOGENABLE",
    "D3DRS_SPECULARENABLE",
    "D3DRS_ZVISIBLE",
    "D3DRS_FOGCOLOR",
    "D3DRS_FOGTABLEMODE",
    "D3DRS_FOGSTART",
    "D3DRS_FOGEND",
    "D3DRS_FOGDENSITY",
    "D3DRS_EDGEANTIALIAS",
    "D3DRS_ZBIAS",
    "D3DRS_RANGEFOGENABLE",
    "D3DRS_STENCILENABLE",
    "D3DRS_STENCILFAIL",
    "D3DRS_STENCILZFAIL",
    "D3DRS_STENCILPASS",
    "D3DRS_STENCILFUNC",
    "D3DRS_STENCILREF",
    "D3DRS_STENCILMASK",
    "D3DRS_STENCILWRITEMASK",
    "D3DRS_TEXTUREFACTOR",
    "D3DRS_WRAP0",
    "D3DRS_WRAP1",
    "D3DRS_WRAP2",
    "D3DRS_WRAP3",
    "D3DRS_WRAP4",
    "D3DRS_WRAP5",
    "D3DRS_WRAP6",
    "D3DRS_WRAP7",
    "D3DRS_CLIPPING",
    "D3DRS_LIGHTING",
    "D3DRS_AMBIENT",
    "D3DRS_FOGVERTEXMODE",
    "D3DRS_COLORVERTEX",
    "D3DRS_LOCALVIEWER",
    "D3DRS_NORMALIZENORMALS",
    "D3DRS_DIFFUSEMATERIALSOURCE",
    "D3DRS_SPECULARMATERIALSOURCE",
    "D3DRS_AMBIENTMATERIALSOURCE",
    "D3DRS_EMISSIVEMATERIALSOURCE",
    "D3DRS_VERTEXBLEND",
    "D3DRS_CLIPPLANEENABLE",
    "D3DRS_SOFTWAREVERTEXPROCESSING",
    "D3DRS_POINTSIZE",
    "D3DRS_POINTSIZE_MIN",
    "D3DRS_POINTSPRITEENABLE",
    "D3DRS_POINTSCALEENABLE",
    "D3DRS_POINTSCALE_A",
    "D3DRS_POINTSCALE_B",
    "D3DRS_POINTSCALE_C",
    "D3DRS_MULTISAMPLEANTIALIAS",
    "D3DRS_MULTISAMPLEMASK",
    "D3DRS_PATCHEDGESTYLE",
    "D3DRS_PATCHSEGMENTS",
    "D3DRS_DEBUGMONITORTOKEN",
    "D3DRS_POINTSIZE_MAX",
    "D3DRS_INDEXEDVERTEXBLENDENABLE",
    "D3DRS_COLORWRITEENABLE",
    "D3DRS_TWEENFACTOR",
    "D3DRS_BLENDOP",
    "D3DRS_POSITIONORDER",
    "D3DRS_NORMALORDER",
])

D3DMATERIALCOLORSOURCE = Enum("D3DMATERIALCOLORSOURCE", [
    "D3DMCS_MATERIAL",
    "D3DMCS_COLOR1",
    "D3DMCS_COLOR2",
])

D3DWRAP = Flags(DWORD, [
    "D3DWRAP_U",
    "D3DWRAP_V",
    "D3DWRAP_W",
])

D3DWRAPCOORD = Flags(DWORD, [
    "D3DWRAPCOORD_0",
    "D3DWRAPCOORD_1",
    "D3DWRAPCOORD_2",
    "D3DWRAPCOORD_3",
])

D3DCOLORWRITEENABLE = Flags(DWORD, [
    "D3DCOLORWRITEENABLE_RED",
    "D3DCOLORWRITEENABLE_GREEN",
    "D3DCOLORWRITEENABLE_BLUE",
    "D3DCOLORWRITEENABLE_ALPHA",
])

D3DTEXTURESTAGESTATETYPE = Enum("D3DTEXTURESTAGESTATETYPE", [
    "D3DTSS_COLOROP",
    "D3DTSS_COLORARG1",
    "D3DTSS_COLORARG2",
    "D3DTSS_ALPHAOP",
    "D3DTSS_ALPHAARG1",
    "D3DTSS_ALPHAARG2",
    "D3DTSS_BUMPENVMAT00",
    "D3DTSS_BUMPENVMAT01",
    "D3DTSS_BUMPENVMAT10",
    "D3DTSS_BUMPENVMAT11",
    "D3DTSS_TEXCOORDINDEX",
    "D3DTSS_ADDRESSU",
    "D3DTSS_ADDRESSV",
    "D3DTSS_BORDERCOLOR",
    "D3DTSS_MAGFILTER",
    "D3DTSS_MINFILTER",
    "D3DTSS_MIPFILTER",
    "D3DTSS_MIPMAPLODBIAS",
    "D3DTSS_MAXMIPLEVEL",
    "D3DTSS_MAXANISOTROPY",
    "D3DTSS_BUMPENVLSCALE",
    "D3DTSS_BUMPENVLOFFSET",
    "D3DTSS_TEXTURETRANSFORMFLAGS",
    "D3DTSS_ADDRESSW",
    "D3DTSS_COLORARG0",
    "D3DTSS_ALPHAARG0",
    "D3DTSS_RESULTARG",
])

D3DTSS = Flags(DWORD, [
    "D3DTSS_TCI_PASSTHRU",
    "D3DTSS_TCI_CAMERASPACENORMAL",
    "D3DTSS_TCI_CAMERASPACEPOSITION",
    "D3DTSS_TCI_CAMERASPACEREFLECTIONVECTOR",
])

D3DTEXTUREOP = Enum("D3DTEXTUREOP", [
    "D3DTOP_DISABLE",
    "D3DTOP_SELECTARG1",
    "D3DTOP_SELECTARG2",
    "D3DTOP_MODULATE",
    "D3DTOP_MODULATE2X",
    "D3DTOP_MODULATE4X",
    "D3DTOP_ADD",
    "D3DTOP_ADDSIGNED",
    "D3DTOP_ADDSIGNED2X",
    "D3DTOP_SUBTRACT",
    "D3DTOP_ADDSMOOTH",
    "D3DTOP_BLENDDIFFUSEALPHA",
    "D3DTOP_BLENDTEXTUREALPHA",
    "D3DTOP_BLENDFACTORALPHA",
    "D3DTOP_BLENDTEXTUREALPHAPM",
    "D3DTOP_BLENDCURRENTALPHA",
    "D3DTOP_PREMODULATE",
    "D3DTOP_MODULATEALPHA_ADDCOLOR",
    "D3DTOP_MODULATECOLOR_ADDALPHA",
    "D3DTOP_MODULATEINVALPHA_ADDCOLOR",
    "D3DTOP_MODULATEINVCOLOR_ADDALPHA",
    "D3DTOP_BUMPENVMAP",
    "D3DTOP_BUMPENVMAPLUMINANCE",
    "D3DTOP_DOTPRODUCT3",
    "D3DTOP_MULTIPLYADD",
    "D3DTOP_LERP",
])

D3DTA = Flags(DWORD, [
    "D3DTA_SELECTMASK",
    "D3DTA_DIFFUSE",
    "D3DTA_CURRENT",
    "D3DTA_TEXTURE",
    "D3DTA_TFACTOR",
    "D3DTA_SPECULAR",
    "D3DTA_TEMP",
    "D3DTA_COMPLEMENT",
    "D3DTA_ALPHAREPLICATE",
])

D3DTEXTUREFILTERTYPE = Enum("D3DTEXTUREFILTERTYPE", [
    "D3DTEXF_NONE",
    "D3DTEXF_POINT",
    "D3DTEXF_LINEAR",
    "D3DTEXF_ANISOTROPIC",
    "D3DTEXF_FLATCUBIC",
    "D3DTEXF_GAUSSIANCUBIC",
])

D3DPV = Flags(DWORD, [
    "D3DPV_DONOTCOPYDATA",
])

D3DFVF = Flags(DWORD, [
    "D3DFVF_RESERVED0",
    "D3DFVF_POSITION_MASK",
    "D3DFVF_XYZ",
    "D3DFVF_XYZRHW",
    "D3DFVF_XYZB1",
    "D3DFVF_XYZB2",
    "D3DFVF_XYZB3",
    "D3DFVF_XYZB4",
    "D3DFVF_XYZB5",
    "D3DFVF_NORMAL",
    "D3DFVF_PSIZE",
    "D3DFVF_DIFFUSE",
    "D3DFVF_SPECULAR",
    "D3DFVF_TEXCOUNT_MASK",
    "D3DFVF_TEXCOUNT_SHIFT",
    "D3DFVF_TEX0",
    "D3DFVF_TEX1",
    "D3DFVF_TEX2",
    "D3DFVF_TEX3",
    "D3DFVF_TEX4",
    "D3DFVF_TEX5",
    "D3DFVF_TEX6",
    "D3DFVF_TEX7",
    "D3DFVF_TEX8",
    "D3DFVF_LASTBETA_UBYTE4",
    "D3DFVF_RESERVED2",
    "D3DFVF_TEXCOORDSIZE3(0)",
    "D3DFVF_TEXCOORDSIZE2(0)",
    "D3DFVF_TEXCOORDSIZE4(0)",
    "D3DFVF_TEXCOORDSIZE1(0)",
    "D3DFVF_TEXCOORDSIZE3(1)",
    "D3DFVF_TEXCOORDSIZE2(1)",
    "D3DFVF_TEXCOORDSIZE4(1)",
    "D3DFVF_TEXCOORDSIZE1(1)",
    "D3DFVF_TEXCOORDSIZE3(2)",
    "D3DFVF_TEXCOORDSIZE2(2)",
    "D3DFVF_TEXCOORDSIZE4(2)",
    "D3DFVF_TEXCOORDSIZE1(2)",
    "D3DFVF_TEXCOORDSIZE3(3)",
    "D3DFVF_TEXCOORDSIZE2(3)",
    "D3DFVF_TEXCOORDSIZE4(3)",
    "D3DFVF_TEXCOORDSIZE1(3)",
])

D3DVSD_TOKENTYPE = Enum("D3DVSD_TOKENTYPE", [
    "D3DVSD_TOKEN_NOP",
    "D3DVSD_TOKEN_STREAM",
    "D3DVSD_TOKEN_STREAMDATA",
    "D3DVSD_TOKEN_TESSELLATOR",
    "D3DVSD_TOKEN_CONSTMEM",
    "D3DVSD_TOKEN_EXT",
    "D3DVSD_TOKEN_END",
])

D3DVSDT = Flags(DWORD, [
    "D3DVSDT_FLOAT1",
    "D3DVSDT_FLOAT2",
    "D3DVSDT_FLOAT3",
    "D3DVSDT_FLOAT4",
    "D3DVSDT_D3DCOLOR",
    "D3DVSDT_UBYTE4",
    "D3DVSDT_SHORT2",
    "D3DVSDT_SHORT4",
    "D3DVSDE_POSITION",
    "D3DVSDE_BLENDWEIGHT",
    "D3DVSDE_BLENDINDICES",
    "D3DVSDE_NORMAL",
    "D3DVSDE_PSIZE",
    "D3DVSDE_DIFFUSE",
    "D3DVSDE_SPECULAR",
    "D3DVSDE_TEXCOORD0",
    "D3DVSDE_TEXCOORD1",
    "D3DVSDE_TEXCOORD2",
    "D3DVSDE_TEXCOORD3",
    "D3DVSDE_TEXCOORD4",
    "D3DVSDE_TEXCOORD5",
    "D3DVSDE_TEXCOORD6",
    "D3DVSDE_TEXCOORD7",
    "D3DVSDE_POSITION2",
    "D3DVSDE_NORMAL2",
    "D3DDP_MAXTEXCOORD",
    "D3DSI_OPCODE_MASK",
])

D3DSHADER_INSTRUCTION_OPCODE_TYPE = Enum("D3DSHADER_INSTRUCTION_OPCODE_TYPE", [
    "D3DSIO_NOP",
    "D3DSIO_MOV",
    "D3DSIO_ADD",
    "D3DSIO_SUB",
    "D3DSIO_MAD",
    "D3DSIO_MUL",
    "D3DSIO_RCP",
    "D3DSIO_RSQ",
    "D3DSIO_DP3",
    "D3DSIO_DP4",
    "D3DSIO_MIN",
    "D3DSIO_MAX",
    "D3DSIO_SLT",
    "D3DSIO_SGE",
    "D3DSIO_EXP",
    "D3DSIO_LOG",
    "D3DSIO_LIT",
    "D3DSIO_DST",
    "D3DSIO_LRP",
    "D3DSIO_FRC",
    "D3DSIO_M4x4",
    "D3DSIO_M4x3",
    "D3DSIO_M3x4",
    "D3DSIO_M3x3",
    "D3DSIO_M3x2",
    "D3DSIO_TEXCOORD",
    "D3DSIO_TEXKILL",
    "D3DSIO_TEX",
    "D3DSIO_TEXBEM",
    "D3DSIO_TEXBEML",
    "D3DSIO_TEXREG2AR",
    "D3DSIO_TEXREG2GB",
    "D3DSIO_TEXM3x2PAD",
    "D3DSIO_TEXM3x2TEX",
    "D3DSIO_TEXM3x3PAD",
    "D3DSIO_TEXM3x3TEX",
    "D3DSIO_TEXM3x3DIFF",
    "D3DSIO_TEXM3x3SPEC",
    "D3DSIO_TEXM3x3VSPEC",
    "D3DSIO_EXPP",
    "D3DSIO_LOGP",
    "D3DSIO_CND",
    "D3DSIO_DEF",
    "D3DSIO_TEXREG2RGB",
    "D3DSIO_TEXDP3TEX",
    "D3DSIO_TEXM3x2DEPTH",
    "D3DSIO_TEXDP3",
    "D3DSIO_TEXM3x3",
    "D3DSIO_TEXDEPTH",
    "D3DSIO_CMP",
    "D3DSIO_BEM",
    "D3DSIO_PHASE",
    "D3DSIO_COMMENT",
    "D3DSIO_END",
])

D3DSP = Flags(DWORD, [
    "D3DSP_WRITEMASK_0",
    "D3DSP_WRITEMASK_1",
    "D3DSP_WRITEMASK_2",
    "D3DSP_WRITEMASK_3",
    "D3DSP_WRITEMASK_ALL",
])

D3DSHADER_PARAM_DSTMOD_TYPE = Enum("D3DSHADER_PARAM_DSTMOD_TYPE", [
    "D3DSPDM_NONE",
    "D3DSPDM_SATURATE",
])

D3DSHADER_PARAM_REGISTER_TYPE = Enum("D3DSHADER_PARAM_REGISTER_TYPE", [
    "D3DSPR_TEMP",
    "D3DSPR_INPUT",
    "D3DSPR_CONST",
    "D3DSPR_ADDR|D3DSPR_TEXTURE",
    "D3DSPR_RASTOUT",
    "D3DSPR_ATTROUT",
    "D3DSPR_TEXCRDOUT",
])

D3DVS_RASTOUT_OFFSETS = Enum("D3DVS_RASTOUT_OFFSETS", [
    "D3DSRO_POSITION",
    "D3DSRO_FOG",
    "D3DSRO_POINT_SIZE",
])

D3DVS_ADDRESSMODE_TYPE = Enum("D3DVS_ADDRESSMODE_TYPE", [
    "D3DVS_ADDRMODE_ABSOLUTE",
    "D3DVS_ADDRMODE_RELATIVE",
])

D3DVS = Flags(DWORD, [
    "D3DVS_X_X",
    "D3DVS_X_Y",
    "D3DVS_X_Z",
    "D3DVS_X_W",
    "D3DVS_Y_X",
    "D3DVS_Y_Y",
    "D3DVS_Y_Z",
    "D3DVS_Y_W",
    "D3DVS_Z_X",
    "D3DVS_Z_Y",
    "D3DVS_Z_Z",
    "D3DVS_Z_W",
    "D3DVS_W_X",
    "D3DVS_W_Y",
    "D3DVS_W_Z",
    "D3DVS_W_W",
    "D3DVS_NOSWIZZLE",
])

D3DSP = Flags(DWORD, [
    "D3DSP_NOSWIZZLE",
    "D3DSP_REPLICATERED",
    "D3DSP_REPLICATEGREEN",
    "D3DSP_REPLICATEBLUE",
    "D3DSP_REPLICATEALPHA",
])

D3DSHADER_PARAM_SRCMOD_TYPE = Enum("D3DSHADER_PARAM_SRCMOD_TYPE", [
    "D3DSPSM_NONE",
    "D3DSPSM_NEG",
    "D3DSPSM_BIAS",
    "D3DSPSM_BIASNEG",
    "D3DSPSM_SIGN",
    "D3DSPSM_SIGNNEG",
    "D3DSPSM_COMP",
    "D3DSPSM_X2",
    "D3DSPSM_X2NEG",
    "D3DSPSM_DZ",
    "D3DSPSM_DW",
])

D3DBASISTYPE = Enum("D3DBASISTYPE", [
    "D3DBASIS_BEZIER",
    "D3DBASIS_BSPLINE",
    "D3DBASIS_INTERPOLATE",
])

D3DORDERTYPE = Enum("D3DORDERTYPE", [
    "D3DORDER_LINEAR",
    "D3DORDER_QUADRATIC",
    "D3DORDER_CUBIC",
    "D3DORDER_QUINTIC",
])

D3DPATCHEDGESTYLE = Enum("D3DPATCHEDGESTYLE", [
    "D3DPATCHEDGE_DISCRETE",
    "D3DPATCHEDGE_CONTINUOUS",
])

D3DSTATEBLOCKTYPE = Enum("D3DSTATEBLOCKTYPE", [
    "D3DSBT_ALL",
    "D3DSBT_PIXELSTATE",
    "D3DSBT_VERTEXSTATE",
])

D3DVERTEXBLENDFLAGS = Enum("D3DVERTEXBLENDFLAGS", [
    "D3DVBF_DISABLE",
    "D3DVBF_1WEIGHTS",
    "D3DVBF_2WEIGHTS",
    "D3DVBF_3WEIGHTS",
    "D3DVBF_TWEENING",
    "D3DVBF_0WEIGHTS",
])

D3DTEXTURETRANSFORMFLAGS = Enum("D3DTEXTURETRANSFORMFLAGS", [
    "D3DTTFF_DISABLE",
    "D3DTTFF_COUNT1",
    "D3DTTFF_COUNT2",
    "D3DTTFF_COUNT3",
    "D3DTTFF_COUNT4",
    "D3DTTFF_PROJECTED",
])

D3DDEVTYPE = Enum("D3DDEVTYPE", [
    "D3DDEVTYPE_HAL",
    "D3DDEVTYPE_REF",
    "D3DDEVTYPE_SW",
])

D3DMULTISAMPLE_TYPE = Enum("D3DMULTISAMPLE_TYPE", [
    "D3DMULTISAMPLE_NONE",
    "D3DMULTISAMPLE_2_SAMPLES",
    "D3DMULTISAMPLE_3_SAMPLES",
    "D3DMULTISAMPLE_4_SAMPLES",
    "D3DMULTISAMPLE_5_SAMPLES",
    "D3DMULTISAMPLE_6_SAMPLES",
    "D3DMULTISAMPLE_7_SAMPLES",
    "D3DMULTISAMPLE_8_SAMPLES",
    "D3DMULTISAMPLE_9_SAMPLES",
    "D3DMULTISAMPLE_10_SAMPLES",
    "D3DMULTISAMPLE_11_SAMPLES",
    "D3DMULTISAMPLE_12_SAMPLES",
    "D3DMULTISAMPLE_13_SAMPLES",
    "D3DMULTISAMPLE_14_SAMPLES",
    "D3DMULTISAMPLE_15_SAMPLES",
    "D3DMULTISAMPLE_16_SAMPLES",
])

D3DFORMAT = Enum("D3DFORMAT", [
    "D3DFMT_UNKNOWN",
    "D3DFMT_R8G8B8",
    "D3DFMT_A8R8G8B8",
    "D3DFMT_X8R8G8B8",
    "D3DFMT_R5G6B5",
    "D3DFMT_X1R5G5B5",
    "D3DFMT_A1R5G5B5",
    "D3DFMT_A4R4G4B4",
    "D3DFMT_R3G3B2",
    "D3DFMT_A8",
    "D3DFMT_A8R3G3B2",
    "D3DFMT_X4R4G4B4",
    "D3DFMT_A2B10G10R10",
    "D3DFMT_G16R16",
    "D3DFMT_A8P8",
    "D3DFMT_P8",
    "D3DFMT_L8",
    "D3DFMT_A8L8",
    "D3DFMT_A4L4",
    "D3DFMT_V8U8",
    "D3DFMT_L6V5U5",
    "D3DFMT_X8L8V8U8",
    "D3DFMT_Q8W8V8U8",
    "D3DFMT_V16U16",
    "D3DFMT_W11V11U10",
    "D3DFMT_A2W10V10U10",
    "D3DFMT_UYVY",
    "D3DFMT_YUY2",
    "D3DFMT_DXT1",
    "D3DFMT_DXT2",
    "D3DFMT_DXT3",
    "D3DFMT_DXT4",
    "D3DFMT_DXT5",
    "D3DFMT_D16_LOCKABLE",
    "D3DFMT_D32",
    "D3DFMT_D15S1",
    "D3DFMT_D24S8",
    "D3DFMT_D16",
    "D3DFMT_D24X8",
    "D3DFMT_D24X4S4",
    "D3DFMT_VERTEXDATA",
    "D3DFMT_INDEX16",
    "D3DFMT_INDEX32",
])

D3DDISPLAYMODE = Struct("D3DDISPLAYMODE", [
    (UINT, "Width"),
    (UINT, "Height"),
    (UINT, "RefreshRate"),
    (D3DFORMAT, "Format"),
])

D3DDEVICE_CREATION_PARAMETERS = Struct("D3DDEVICE_CREATION_PARAMETERS", [
    (UINT, "AdapterOrdinal"),
    (D3DDEVTYPE, "DeviceType"),
    (HWND, "hFocusWindow"),
    (DWORD, "BehaviorFlags"),
])

D3DSWAPEFFECT = Enum("D3DSWAPEFFECT", [
    "D3DSWAPEFFECT_DISCARD",
    "D3DSWAPEFFECT_FLIP",
    "D3DSWAPEFFECT_COPY",
    "D3DSWAPEFFECT_COPY_VSYNC",
])

D3DPOOL = Enum("D3DPOOL", [
    "D3DPOOL_DEFAULT",
    "D3DPOOL_MANAGED",
    "D3DPOOL_SYSTEMMEM",
    "D3DPOOL_SCRATCH",
])

D3DPRESENT = Flags(DWORD, [
    "D3DPRESENT_RATE_DEFAULT",
    "D3DPRESENT_RATE_UNLIMITED",
])

D3DPRESENT_PARAMETERS = Struct("D3DPRESENT_PARAMETERS", [
    (UINT, "BackBufferWidth"),
    (UINT, "BackBufferHeight"),
    (D3DFORMAT, "BackBufferFormat"),
    (UINT, "BackBufferCount"),
    (D3DMULTISAMPLE_TYPE, "MultiSampleType"),
    (D3DSWAPEFFECT, "SwapEffect"),
    (HWND, "hDeviceWindow"),
    (BOOL, "Windowed"),
    (BOOL, "EnableAutoDepthStencil"),
    (D3DFORMAT, "AutoDepthStencilFormat"),
    (DWORD, "Flags"),
    (UINT, "FullScreen_RefreshRateInHz"),
    (UINT, "FullScreen_PresentationInterval"),
])

D3DPRESENTFLAG = Flags(DWORD, [
    "D3DPRESENTFLAG_LOCKABLE_BACKBUFFER",
])

D3DGAMMARAMP = Struct("D3DGAMMARAMP", [
    (Array(WORD, "256"), "red"),
    (Array(WORD, "256"), "green"),
    (Array(WORD, "256"), "blue"),
])

D3DBACKBUFFER_TYPE = Enum("D3DBACKBUFFER_TYPE", [
    "D3DBACKBUFFER_TYPE_MONO",
    "D3DBACKBUFFER_TYPE_LEFT",
    "D3DBACKBUFFER_TYPE_RIGHT",
])

D3DRESOURCETYPE = Enum("D3DRESOURCETYPE", [
    "D3DRTYPE_SURFACE",
    "D3DRTYPE_VOLUME",
    "D3DRTYPE_TEXTURE",
    "D3DRTYPE_VOLUMETEXTURE",
    "D3DRTYPE_CUBETEXTURE",
    "D3DRTYPE_VERTEXBUFFER",
    "D3DRTYPE_INDEXBUFFER",
])

D3DUSAGE = Flags(DWORD, [
    "D3DUSAGE_RENDERTARGET",
    "D3DUSAGE_DEPTHSTENCIL",
    "D3DUSAGE_WRITEONLY",
    "D3DUSAGE_SOFTWAREPROCESSING",
    "D3DUSAGE_DONOTCLIP",
    "D3DUSAGE_POINTS",
    "D3DUSAGE_RTPATCHES",
    "D3DUSAGE_NPATCHES",
    "D3DUSAGE_DYNAMIC",
])

D3DCUBEMAP_FACES = Enum("D3DCUBEMAP_FACES", [
    "D3DCUBEMAP_FACE_POSITIVE_X",
    "D3DCUBEMAP_FACE_NEGATIVE_X",
    "D3DCUBEMAP_FACE_POSITIVE_Y",
    "D3DCUBEMAP_FACE_NEGATIVE_Y",
    "D3DCUBEMAP_FACE_POSITIVE_Z",
    "D3DCUBEMAP_FACE_NEGATIVE_Z",
])

D3DLOCK = Flags(DWORD, [
    "D3DLOCK_READONLY",
    "D3DLOCK_DISCARD",
    "D3DLOCK_NOOVERWRITE",
    "D3DLOCK_NOSYSLOCK",
    "D3DLOCK_NO_DIRTY_UPDATE",
])

D3DVERTEXBUFFER_DESC = Struct("D3DVERTEXBUFFER_DESC", [
    (D3DFORMAT, "Format"),
    (D3DRESOURCETYPE, "Type"),
    (DWORD, "Usage"),
    (D3DPOOL, "Pool"),
    (UINT, "Size"),
    (DWORD, "FVF"),
])

D3DINDEXBUFFER_DESC = Struct("D3DINDEXBUFFER_DESC", [
    (D3DFORMAT, "Format"),
    (D3DRESOURCETYPE, "Type"),
    (DWORD, "Usage"),
    (D3DPOOL, "Pool"),
    (UINT, "Size"),
])

D3DSURFACE_DESC = Struct("D3DSURFACE_DESC", [
    (D3DFORMAT, "Format"),
    (D3DRESOURCETYPE, "Type"),
    (DWORD, "Usage"),
    (D3DPOOL, "Pool"),
    (UINT, "Size"),
    (D3DMULTISAMPLE_TYPE, "MultiSampleType"),
    (UINT, "Width"),
    (UINT, "Height"),
])

D3DVOLUME_DESC = Struct("D3DVOLUME_DESC", [
    (D3DFORMAT, "Format"),
    (D3DRESOURCETYPE, "Type"),
    (DWORD, "Usage"),
    (D3DPOOL, "Pool"),
    (UINT, "Size"),
    (UINT, "Width"),
    (UINT, "Height"),
    (UINT, "Depth"),
])

D3DLOCKED_RECT = Struct("D3DLOCKED_RECT", [
    (INT, "Pitch"),
    (PVOID, "pBits"),
])

D3DBOX = Struct("D3DBOX", [
    (UINT, "Left"),
    (UINT, "Top"),
    (UINT, "Right"),
    (UINT, "Bottom"),
    (UINT, "Front"),
    (UINT, "Back"),
])

D3DLOCKED_BOX = Struct("D3DLOCKED_BOX", [
    (INT, "RowPitch"),
    (INT, "SlicePitch"),
    (PVOID, "pBits"),
])

D3DRANGE = Struct("D3DRANGE", [
    (UINT, "Offset"),
    (UINT, "Size"),
])

D3DRECTPATCH_INFO = Struct("D3DRECTPATCH_INFO", [
    (UINT, "StartVertexOffsetWidth"),
    (UINT, "StartVertexOffsetHeight"),
    (UINT, "Width"),
    (UINT, "Height"),
    (UINT, "Stride"),
    (D3DBASISTYPE, "Basis"),
    (D3DORDERTYPE, "Order"),
])

D3DTRIPATCH_INFO = Struct("D3DTRIPATCH_INFO", [
    (UINT, "StartVertexOffset"),
    (UINT, "NumVertices"),
    (D3DBASISTYPE, "Basis"),
    (D3DORDERTYPE, "Order"),
])

D3DADAPTER_IDENTIFIER8 = Struct("D3DADAPTER_IDENTIFIER8", [
    (CString, "Driver"),
    (CString, "Description"),
    (LARGE_INTEGER, "DriverVersion"),
    (DWORD, "VendorId"),
    (DWORD, "DeviceId"),
    (DWORD, "SubSysId"),
    (DWORD, "Revision"),
    (GUID, "DeviceIdentifier"),
    (DWORD, "WHQLLevel"),
])

D3DRASTER_STATUS = Struct("D3DRASTER_STATUS", [
    (BOOL, "InVBlank"),
    (UINT, "ScanLine"),
])

D3DDEBUGMONITORTOKENS = Enum("D3DDEBUGMONITORTOKENS", [
    "D3DDMT_ENABLE",
    "D3DDMT_DISABLE",
])

D3DDEVINFOID = Flags(DWORD, [
    "D3DDEVINFOID_RESOURCEMANAGER",
    "D3DDEVINFOID_VERTEXSTATS",
])

D3DRESOURCESTATS = Struct("D3DRESOURCESTATS", [
    (BOOL, "bThrashing"),
    (DWORD, "ApproxBytesDownloaded"),
    (DWORD, "NumEvicts"),
    (DWORD, "NumVidCreates"),
    (DWORD, "LastPri"),
    (DWORD, "NumUsed"),
    (DWORD, "NumUsedInVidMem"),
    (DWORD, "WorkingSet"),
    (DWORD, "WorkingSetBytes"),
    (DWORD, "TotalManaged"),
    (DWORD, "TotalBytes"),
])

D3DDEVINFO_RESOURCEMANAGER = Struct("D3DDEVINFO_RESOURCEMANAGER", [
    (Array(D3DRESOURCESTATS, "D3DRTYPECOUNT"), "stats"),
])

D3DDEVINFO_D3DVERTEXSTATS = Struct("D3DDEVINFO_D3DVERTEXSTATS", [
    (DWORD, "NumRenderedTriangles"),
    (DWORD, "NumExtraClippingTriangles"),
])

