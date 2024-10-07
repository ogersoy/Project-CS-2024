# Foreword {#foreword .list-paragraph}
This Technical Specification has been produced by the 3rd Generation
Partnership Project (3GPP).
The contents of the present document are subject to continuing work within the
TSG and may change following formal TSG approval. Should the TSG modify the
contents of the present document, it will be re-released by the TSG with an
identifying change of release date and an increase in version number as
follows:
Version x.y.z
where:
x the first digit:
1 presented to TSG for information;
2 presented to TSG for approval;
3 or greater indicates TSG approved document under change control.
y the second digit is incremented for all changes of substance, i.e. technical
enhancements, corrections, updates, etc.
z the third digit is incremented when editorial only changes have been
incorporated in the document.
# Introduction {#introduction .list-paragraph}
[TBA]
# 1 Scope {#scope .list-paragraph}
[TBA]
{#section .list-paragraph}
# 2 References {#references .list-paragraph}
[1] 3GPP TS 26.441: \"Codec for Enhanced Voice Services (EVS); General
overview\".
[2] 3GPP TS 26.445: \"Codec for Enhanced Voice Services (EVS); Detailed
Algorithmic Description\".
[3] 3GPP TS 26.442: \"Codec for Enhanced Voice Services (EVS); ANSI C code
(fixed-point)\".
[4] 3GPP TS 26.443: \"Codec for Enhanced Voice Services (EVS); ANSI C code
(floating point)\".
[5] 3GPP TS 26.447: \"Codec for Enhanced Voice Services (EVS); Error
Concealment of Lost Packets\".
[6] ITU-R BS.2051-1: "Advanced sound system for programme production".
[7] 3GPP TS 26.118: "3GPP Virtual reality profiles for streaming
applications".
# Definitions, symbols and abbreviations
[TBA]
# General description of the coder
{width="6.743055555555555in" height="3.670138888888889in"}
The SPAR coder contains the following key components:
a. **Content ingestion engine** can accept inputs containing objects, HoA
(scenes), and channel based content. The maximum number of objects, channels,
and scenes are not constrained, but practical limits associated with memory
generally mean that ingestion has a practical limit of 64 channels, 8^th^
order HoA, and 64 objects. The ingestion engine simplifies the output to an
nth order HoA scene with M objects. If the content ingestion engine is
provided only with a higher order HoA input, then objects can be extracted at
this point from the HoA scene and are handled as objects from that point
onward. The encoder and decoder is limited to a maximum of 3^rd^ order HoA and
15 objects. The order, n, of the HoA scene, and the number of objects provided
to the encoder are determined by a target bit rate for metadata stream.
Metadata bit rates can range from 4 to 128 kbps.
b. The **SPAR Metadata encoder** performs operations such as the downmix to a
four channel First Order Ambisonics (B-Format) bed for encoding, metadata
modeling for the residuals to higher order ambisonics, object metadata, and
metadata associated with WXYZ energy compaction.
c. The **4 x EVS encoder** encodes WX'Y'Z', a B format representation where an
energy compaction has been performed on the B-format downmix, WXYZ. The
encoder makes the decision of bit rate for each channel depending on the
overall target bit rate. Significantly more bits are allocated to the W
channel ensuring that the W channel is always of highest quality. This
provides an additional benefit that this mono downmix can be extracted
independently from the bit stream and decoded independently.
> The SPAR decoder contains the following key components:
a. A **mode switch** that determines from metadata in the bitstream, whether
the content has been encoded as First order Ambisonics only, eg, with no
objects, or in High immersive quality, defined as content that contains 2^nd^
or 3^rd^ order HoA and one or more objects.
b. The **FoA decoder** (PC mode) implements a 4 x EVS decode of the four
channel FoA stream and recovers WXYZ from WX'Y'Z' and predictor coefficients
(PC). This creates a first order ambisonics output which is presented to the
renderer.
c. The **SPAR decoder** takes the four channel FoA stream and implements the
full SPAR decode which recreates the Nth order ambisonics format and M objects
that was specified by the content ingestion engine.
d. The nth order HoA scene and M objects are presented to the renderer.
e. As additional functionality, the encoded bit stream can be parsed so as to
extract a high quality Mono EVS bit stream which can be decoded with a
standard mono EVS decoder.
```{=html}
``` 5\. Functional description of the decoder
=====================================
    1.  Functional description of EVS decoder
        -------------------------------------
The EVS codec including EVS decoder is fully specified in 3GPP TS 26.445 [2].
EVS encoder and decoder source code is specified in 3GPP TSs 26.442 [3] and
26.443 [4].
  1. Functional description of SPAR and PC decoder \---------------------------------------------
    1. ### Introduction
The spatial audio reconstruction (SPAR) tool is a coding tool for improved
coding of a large number of audio channels and objects. To gain coding
efficiency this tool supports the reconstruction of audio channels and objects
out of a lower number of joint input audio channels and low overhead side
information.
  1. ### Interface
    1. #### Inputs
> **audio_buf**
>
> _A (N x nFOA) audio buffer containing PCM audio input. This audio has been
> decoded from the bitstream by the EVS decoder._
>
> **audio_buf_idx**
>
> Index into the first sample of **audio_buf** representing the first sample
> of the current audio frame.
**bitstream**
Coded MDF bitstream for the current frame (clauses 6.6, 6.7).
**FOA_Mode**
Boolean value indicating PC or SPAR mode for the current frame. It is computed
> from the MDT (clause 6.4.2) as _FOA_Mode_ = 1 -- _MDT_.
**MDC**
Metadata Coding configuration field (clause 6.4.3) for the current frame.
#### Outputs
> **nHOA**
>
> Number of HOA channels in the current frame
>
> **nObj**
>
> Number of audio objects in the current frame
**FOA_Mode**
> Indicates PC or SPAR mode for the current frame.
>
> **hoa_sig** \ _A (WindowSize x nHOA) matrix containing the reconstructed
> ambisonics PCM audio for the current frame._
>
> **obj_sig**
>
> A (WindowSize x nObj) matrix containing the reconstructed object PCM audio
> for the current frame.
>
> **obj_xyz**
>
> A (3 x nObj) matrix containing the decoded object positions for the current
> frame.
>
> **audio_out**
>
> A (WindowSize x nObj + nHOA) matrix containing the rendered PCM audio for
> the current frame.
The **hoa_sig,** **obj_sig** , and **obj_xyz** matrices are intended to be
used as input to an external loudspeaker or binaural renderer. The
_WindowSize_ is fixed at 4096 audio samples.
#### Controls
The control information for the SPAR tool consists of decoded and dequantized
SPAR side information. Decoding and dequantization of the MDF is described in
clause 5.2.3.4.
  1. ### Processing
    1. #### Windowing and Overlap-add Synthesis
The SPAR and PC decoders operate on 4096-sample audio frames with a
1920-sample step (stride). This results in an overlap of 2176 samples between
consecutive windows. The window step size corresponds to the length of two
consecutive EVS frames. Input audio frames are time-windowed using the
_SPAR_Window_ array, and decoded audio frames are windowed using the
_SPAR_OutWindow_ array. Windowed output frames are intended to be written to
the output audio buffer using Overlap-add Synthesis (OLA). The construction of
the input and output time windows is specified in Pseudocode 1.
Pseudocode 1
// SPAR Window construction
function [SPAR_Window, SPAR_OutWindow] = SPAR_window_contruct()
{
WindowSize = 4096
// Initialize the windows with zeros
for k = 0 to WindowSize - 1
{
SPAR_Window[k] = 0
SPAR_OutWindow[k] = 0
}
// Create the up-ramp at the start of the SPAR_Window
for k = 200 to 711
{
SPAR_Window[k] = sin( (k-199.5) * pi / 1024 ) \^ 2
}
// Create the flat-top of the SPAR_Window
for k = 712 to 2119
{
SPAR_Window[k] = 1
}
// Create the down-ramp at the end of the SPAR_Window
for k = 2120 to 2631
{
SPAR_Window[k] = cos( (k-2119.5) * pi / 1024 ) \^ 2
}
// Create the up-ramp at the start of the SPAR_OutWindow
for k = 0 to 99
{
SPAR_OutWindow[k] = sin( (k+0.5) * pi / 200 ) \^ 2
}
// Create the flat-top of the SPAR_OutWindow
for k = 100 to 3995
{
SPAR_OutWindow[k] = 1
}
// Create the down-ramp at the end of the SPAR_OutWindow
for k = 3996 to 4095
{
SPAR_OutWindow[k] = cos( (k-3995.5) * pi / 200 ) \^ 2
}
}
#### Modified Discrete Fourier Transform (MDFT)
The SPAR and PC decoders operate in the MDFT domain. A reference
implementation of the forward and inverse MDFT transforms are specified in
Pseudocode 2.
Pseudocode 2
// Modified Discrete Fourier Transform (MDFT)
// input: array X (2*N x num_cols) real values
// output: array Y (N x num_cols) complex values
function Y = mdft( X )
{
[sizeX_1,sizeX_2] = size(X)
// The length of columns should be an even number
assert( sixeX_1 mod 2 == 0 )
N = sizeX_1 / 2
num_cols = sizeX_2
// Process each column
for c = 0 to num_cols - 1
{
// Compute each MDFT output bin
for j = 0 to N - 1
{
Y[j,c] = 0
for k = 0 to 2*N - 1
{
Y[j,c] = Y[j,c] + X[k,c] * exp( -1i * pi * k * (j+0.5) / N ) // i = sqrt(-1)
}
}
}
}
// IMDFT:
// input: array X (N x num_cols) complex values
// output: array Y (2*N x num_cols) real values
function Y = imdft( X )
{
[sizeX_1,sizeX_2] = size(X)
N = sizeX_1
num_cols = sizeX_2
// Process each column
for c = 0 to num_cols - 1
{
// Compute each IMDFT output sample (a real value)
for k = 0 to 2*N - 1
{
Y[k,c] = 0
for j = 0 to N - 1
{
Y[k,c] = Y[k,c] + real( X[j,c] * exp( 1i * pi * k * (j+0.5) / N ) / N )
}
}
}
}
#### Parameter band to MDFT coefficient mapping
The SPAR parameters inside the MDF (clause 6.2) are transmitted separately for
each of the _12_ parameter bands. The mapping of MDFT coefficients to
parameter bands is provided by the **FR2Band** matrix, which is constructed as
specified in Pseudocode 3.
Pseudocode 3
// SPAR_make_FR2Band
// output: array FR2Band (12 x 2048)
//
function FR2Band = SPAR_make_FR2Band()
{
N = 2048;
FSample = 48000;
MinStepAdd = 49.28/3;
MinStepMult = 2\^(1.75/3);
numBands = 12;
FR2Band=zeros(12,N);
LastBin=8;
NextBin = 24;
for k = 0 to 11
{
if k==11
{
for n = 0 to N-1
{
FR2Band[k, n] = 1 - LastLP[n]
}
} else {
// Make a prototype LowPass filter:
for n = 0 to LastBin - 1
{
NewLP[n] = 1
}
for n = LastBin to NextBin - 1
{
r = (n-LastBin) / (NextBin - LastBin)
NewLP[n] = 1 + r*r * (2*r - 3)
}
for n = NextBin to N - 1
{
NewLP[n] = 0
}
// Now that we have LP, we make the band-pass by subtracting
// the prior low-pass (unless we\'re computing band0)
for n = 0 to N-1
{
if k == 0
{
FR2Band[k,n] = NewLP[n]
} else {
FR2Band[k,n] = NewLP[n] - LastLP[n]
}
}
}
LastLP = NewLP
LastBin = NextBin
NextBin = round(max( LastBin + MinStepAdd , LastBin * MinStepMult ))
}
}
#### Differential decoding and dequantization
This clause provides pseudocode for decoding and dequantizing each metadata
field contained in the MDF. The pseudocode for decoding of the **G** , **P** ,
and **M** matrices makes use of the huffman_decode() function. The
huffman_decode() function takes in a _bitstream_ array, an index into the
current bit (_b_idx_), and uses the _coding_strategy_idx_ and _huff_idx_
indices to select a Huffman decoding table from Annex B to decode a single
value from the bitstream. The function returns the decoded value as its first
output and the number of bits read from the bitstream as its second output.
The **G** matrix contained in the PC MDF is decoded and dequantized according
to Pseudocode 4.
Pseudocode 4
// differential decoding of Gfoa
// input: array bitstream (array of huffman-coded bits)
// b_idx_in (index into bitstream indicating the start of Gfoa)
// coding_strategy_idx (used to select correct Huffman table)
// output: G_foa (decoded prediction metadata matrix (nFOA - 1 x 12)
// b_idx_out (bitstream position after reading Gfoa)
[G_foa, b_idx_out] = md_diff_decode_G_foa(bitstream, b_idx_in,
coding_strategy_idx)
{
n_bands=12
b_idx = b_idx_in
nFOA = 4
huff_idx = 1
for b = 0 to (n_bands - 1)
{
if b==0
{
useDiff = false
}
else
{
useDiff = bitstream[b_idx++]
}
if useDiff == false
{
last_G = {0, 0, 0}
}
// differential decoding
for c = 0 to nFOA - 2
{
[G_foa[c,b], bits_read] = huffman_decode(bitsteam, b_idx, coding_strategy_idx,
huff_idx)
\+ last_G[c]
b_idx += bits_read
last_G[c] = G_foa[c,b]
}
}
b_idx_out = b_idx //bitstream position after decode
}
The **P** matrix contained in the SPAR MDF is decoded and dequantized
according to Pseudocode 5.
Pseudocode 5
// differential decoding of Pspar
// input: array bitstream (array of huffman-coded bits)
// b_idx_in (index into bitstream indicating the start of Gfoa)
// coding_strategy_idx (used to select correct Huffman table)
// nOut (number of channels (HOA + Objects)
// nDeco (number of decorrelators)
// output: P_spar (decoded SPAR metadata matrix (nHOA + nObj x nDeco x 12))
// b_idx_out (bitstream position after reading Gfoa)
[P_spar, b_idx_out] = md_diff_decode_P_spar(bitstream, b_idx_in,
coding_strategy_idx, nOut, nDeco)
{
n_bands=12
b_idx = b_idx_in
huff_idx = 1
for b = 0 to (n_bands - 1)
{
if b==0
{
useDiff = false
}
else
{
useDiff = bitstream[b_idx++]
}
if useDiff == false
{
for i = 0 to nOut - 1
{
for j = 0 to nDeco - 1
{
last_P[i,j] = 0;
}
}
}
//differential decoding
for c = 0 to nDeco - 1
for k = 0 to nOut - 1
{
[P_spar[k,c,b], bits_read] = huffman_decode(bitsteam, b_idx,
coding_streategy_idx, huff_idx)
\+ last_P[k,c]
b_idx += bits_read
last_P[k,c] = P_spar[k,c,b]
}
}
b_idx_out = b_idx //bitstream position after decode
}
The **M** matrix contained in the SPAR MDF is decoded and dequantized
according to Pseudocode 6. The number of HoA channels _nHOA_ is calculated
from the _hoa_order_idx_ metadata contained is the MDC (subclause 6.4.3) as
_nHOA =_ (_hoa_order_idx +_ 2)^2^_._
Pseudocode 6
// differential decoding of Mspar
// input: array bitstream (array of huffman-coded bits)
// b_idx_in (index into bitstream indicating the start of Gfoa)
// coding_strategy_idx (used to select correct Huffman table)
// nHOA (number of Hoa channels)
// nObj (number of objects)
// output: M_spar (decoded SPAR metadata matrix (nHOA + nObj x nFOA x 12))
// b_idx_out (bitstream position after reading Gfoa)
[M_spar, b_idx_out] = md_diff_decode_M_spar(bitstream, b_idx_in,
coding_strategy_idx, nHOA, nObj)
{
n_bands=12
nFOA = 4
b_idx = b_idx_in
hoaStrengths = {1/2, 1/3};
// construct offset matrix (2 x nObj + nHOA x nFOA)
Ms = {0} // set all elements to zero
for i = 0 to 1
{
for j = 0 to nFOA - 1
{
Ms[i, j, j] = hoaStrengths[i];
}
for j = 0 to nObj-1
{
Ms[i,nHOA+j,0] = (1 - hoaStrengths[i]) / nObj
}
}
for b = 0 to (n_bands - 1)
{
if b==0
{
useDiff = false
}
else
{
useDiff = bitstream[b_idx++]
}
if useDiff == false
{
m_choose = bitstream[b_idx++];
for i = 0 to nObj + nHOA - 1
{
for j = 0 to nFOA - 1
{
last_M[i,j] = Ms[m_choose, i, j];
}
}
}
//differential decoding
for c = 0 to nFOA - 1
for k = 0 to nObj + nHOA - 1
{
[M_spar[k,c,b], bits_read] = huffman_decode(bitsteam, b_idx,
coding_streategy_idx) + last_M[k,c]
b_idx += bits_read
last_M[k,c] = M_spar[k,c,b]
}
}
b_idx_out = b_idx //bitstream position after decode
}
The matrix of object positions (**obj_xyz)** is decoded and dequantized
according to Pseudocode 7.
Pseudocode 7
// input: array bitstream (array of huffman-coded bits)
// b_idx_in (index into bitstream indicating the start of Gfoa)
// Nobj (number of objects)
// output: obj_xyz (decoded object position matrix (3 x Nobj)
// b_idx_out (bitstream position after reading obj_xyz)
[obj_xyz, b_idx_out] = md_decode_obj( bitstream, b_idx_in, Nobj )
{
b_idx = b_idx_in
for o = 0 to Nobj - 1
{
bits2 = bitstream[b_idx]*2 + bitstream[b_idx+1]
b_idx = b_idx + 2
if bits2 == 3
{
// we have a corner or edge
bits2 = bitstream[b_idx]*2 + bitstream[b_idx+1]
b_idx = b_idx + 2
if bits2 == 3
{
// we have a corner
for k = 0 to 2
{
xyz[k] = 64 * bitstream[b_idx++]
}
}
else
{
// we have an edge
for k = 0 to 1
{
t[k] = 64 * bitstream[b_idx++]
}
v1 = 0
for k = 0 to 5
{
v1 += 2\^(6-k) * bitstream[b_idx++]
}
tmp = {t[1], t[2], v1};
for k = 0 to 2
{
xyz[mod(k+bits2+1, 3)] = tmp[k];
}
}
}
else
{
// we have a face
t2 = 64 * bitstream[b_idx++]
for k = 0 to 5
{
v1 += 2\^(6-k) * bitstream[b_idx++]
}
for k = 0 to 5
{
v2 += 2\^(6-k) * bitstream[b_idx++]
}
tmp = {v1, v2, t2};
for k = 0 to 2
{
xyz[mod(k+bits2+1, 3)] = tmp[k];
}
}
offset = {0, 0, 32}
scale = {1/64, 1/64, 1/32}
for k = 0 to 2
{
obj_xyz(k,o) = (xyz[k]-offset[k])*scale[k]
}
}
b_idx_out = b_idx //bitstream position after decode
}
#### SPAR and PC Audio Decoding
The SPAR and PC decoder takes in 4 channels of PCM audio and uses either **M**
and **P** metadata (SPAR mode) or **G** metadata (PC mode) to produce a set of
output audio channels. In SPAR mode, the output channels consist of an HOA and
Object audio presentation.
The SPAR and PC decoder is specified in Pseudocode 8.
Pseudocode 8
// SPAR Audio Decoder
// Decodes a frame of nFOA-channel PCM audio, producing a frame of
// audio with nObj + nHOA channels
// input: audio_buf (nFOA-channel PCM audio buffer)
// b_idx (index into buffer indicating the start of frame)
// coding_strategy_idx (used to select correct Huffman table)
// output: hoa_sig (decoded HOA pcm frame (nHOA channels))
// obj_sig (decoded Object pcm frame (nObj channels))
// MetaData (Metadata structure with the following fields)
// FOA_Mode (Boolean indicating FOA or HiQ mode)
// G (FOA Prediction matrix (FOA mode only))
// M (HiQ reconstruction matrix)
// P (HiQ decorrelation matrix)
function [hoa_sig, obj_sig] = SPAR_decode(audio_buf, audio_buf_idx, MetaData)
{
WindowSize = 4096
nFOA = 4;
// Audio Blocks overlap by 2176
// samples, because they are 4096-samples long and the stride is 1920
for j = 0 to WindowSize - 1
{
for k = 0 to nFOA - 1
{
// Fetch the input signals (nFOA channels) with windowing
foa[j,k] = SPAR_Window[j] .* audio_buf[j, k + audio_buf_idx];
}
}
//Modified DFT
foaFR = mdft(foa);
// Now - we need to know what kind of metadata we have for this block. If
it\'s
// FOA_Mode, the processing is simpler. If it\'s not FOA_Mode, we do a full
// matrix plus decorrelation:
if MetaData.FOA_Mode
{
//Do the FOA recovery only
G = MetaData.G
nHOA = nFOA
outFR = foaFR
// For each band, b, the recovered signal (outFR) is made by taking the input
// (sparsened) signal (foaFR) and mixing some of the first channel
// into the other nFOA - 1 channels, according to the gains, G
for b = 0 to nBands - 1
{
for ch = 1 to nFOA - 1
{
for k = 0 to WindowSize/2 - 1
outFR[k,ch] += FR2Band[b,k] * outFR[k,1] * G[ch-1,b]
}
}
}else
{
//Use HOA mode
// Get the xyz location of the objects (objects have a fixed location for the
// duration of one block)
obj_xyz = MetaData.XYZ
// Get the M and P matrices:
M = MetaData.M // M is (nSigs x nFOA x nBands)
P = MetaData.P // P is (nSigs x nDeco x nBands)
nObj = NumberOfColumns(obj_xyz)
nSigs = NumberOfRows(M)
nHOA = nSigs-nObj;
nDeco = NumberOfColumns(P)
outFR = {0} //set all elements to zero
// For each band, b, the recovered signal (outFR) is made by taking the input
// (sparsened) signal (foaFR) and mixing it according to M. In
// addition, a set of decorrelated signals are made from the first input
// channel, and mixed in according P
for b = 0 to nBands - 1
{
for k = 0 to WindowsSize/2 - 1
{
for ch_out = 0 to nSigs - 1
{
acc = 0 //accumulator
for ch_in = 0 to nFOA - 1
{
acc += foaFR[k,ch_in] * M[ch_out,ch_in,b]
}
for d = 0 to nDeco - 1
{
acc += foaFR[k,1] * Decos[k,d] * P[h_out,d,b]
}
outFR[k,ch_out] += FR2Band[b,k] * acc
}
}
}
}
// Figure out the HOA part of the result
for k = 0 to WindowsSize/2 - 1
{
for ch_out = 0 to nSigs - 1
{
if ch_out \ 0.5
{
gainZ[k] = 2*z2[k]-1
}
if z2[k] \= pannerData.Uangs[i]
{
for j = 0 to lengthOf(pannerData.Uchans) - 1
{
d = pannerData.Uangs[i+1] - pannerData.Uangs[i]
v2 = (az[k] - pannerData.Uangs[i])/d
v1 = (pannerData.Uangs[i+1] - az[k])/ d
gAz = v1 * pannerData.Umap[i,j] + v2 * pannerData.Umap[i+1,j]
gAz = gAz + 0.5*gAz*(1-gAz)
gAz *= gainU[k]
G[pannerData.Uchans[j]-1, k] += gAz
}
}
}
}
if isempty(pannerData.Lchans)
{
gainM[k] = gainM[k] + gainL[k]
}else
{
gainL[k] = gainL[k] + 0.5*gainL[k].*(1-gainL[k])
//linearly interpolate gains according to map and angles
minVal = Inf
minj = -1
for i = 0 to lengthOf(pannerData.Langs) - 2
{
if az[k] \= pannerData.Langs[i]
{
for j = 0 to lengthOf(pannerData.Lchans) - 1
{
d = pannerData.Langs[i+1] - pannerData.Langs[i]
v2 = (az[k] - pannerData.Langs[i])/d
v1 = (pannerData.Langs[i+1] - az[k])/ d
gAz = v1 * pannerData.Lmap[i,j] + v2 * pannerData.Lmap[i+1,j]
gAz = gAz + 0.5*gAz*(1-x)
gAz *= gainL[k]
G[pannerData.Lchans[j]-1, k] += gAz
}
}
}
}
gainM[k] = gainM[k] + 0.5*gainM[k].*(1-gainM[k])
//linearly interpolate gains according to map and angles
minVal = Inf
minj = -1
for i = 0 to lengthOf(pannerData.Mangs) - 2
{
if az[k] \= pannerData.Mangs[i]
{
for j = 0 to lengthOf(pannerData.Mchans) - 1
{
d = pannerData.Mangs[i+1] - pannerData.Mangs[i]
v2 = (az[k] - pannerData.Mangs[i])/d
v1 = (pannerData.Mangs[i+1] - az[k])/ d
gAz = v1 * pannerData.Mmap[i,j] + v2 * pannerData.Mmap[i+1,j]
gAz = gAz + 0.5*gAz*(1-x)
gAz *= gainM[k]
G[pannerData.Mchans[j]-1, k] += gAz
}
}
}
}
The reference object panner for loudspeaker output uses data in the
_pannerData_ structure that is dependent on the renderer output mode. Values
for several loudspeaker output layouts are provided in Annex D.
The reference object panner for HOA3 renderer output is specified in
Pseudocode 12.
Pseudocode 12
// HOA3_XYZ_to_Pan
// Cpmputes 3rd-order Ambisonics gains in ACN channel order
// with SN3D scaling
//
// input: array xyz ( 3 x num_cols) unit-vectors
// output: array Gains (16 x num_cols) Ambisonics gains
function Gains = HOA3_XYZ_to_Pan( xyz )
{
[sizeX_1,sizeX_2] = size(xyz)
// The length of columns should be 3
assert( sixeX_1 == 3 )
num_cols = sizeX_2
for c = 0 to num_cols - 1
{
// For convenience, fetch the 3 coordinates from
// the column of the xyz array:
x = xyz[1,c]
y = xyz[2,c]
z = xyz[3,c]
// Now compute the Ambisonics gains
Gains[ 0,c] = 1
Gains[ 1,c] = y
Gains[ 2,c] = z
Gains[ 3,c] = x
Gains[ 4,c] = 1.7320508075688771930 * x * y
Gains[ 5,c] = 1.7320508075688771930 * y * z
Gains[ 6,c] = 0.5 * (3*z*z - 1)
Gains[ 7,c] = 1.7320508075688771930 * x * z
Gains[ 8,c] = 0.8660254037844385966 * (x*x - y*y)
Gains[ 9,c] = 0.7905694150420948807 * y * (3*x*x - y*y)
Gains[10,c] = 3.8729833462074170210 * x * y * z
Gains[11,c] = 0.6123724356957944703 * y * (5*z*z - 1)
Gains[12,c] = 0.5 * z * (5*z*z - 3)
Gains[13,c] = 0.6123724356957944703 * x * (5*z*z - 1)
Gains[14,c] = 1.9364916731037085110 * z * (x*x - y*y)
Gains[14,c] = 0.7905694150420948807 * x * (x*x - 3*y*y)
}
}
## Frame loss handling
Frame loss handling is supported by relying on the specified frame loss
handling strategies of the EVS codec [5] and by freezing the parameters of the
spatial metadata frameworks. Freezing the spatial metadata parameters is
achieved by repetition of the metadata frame of the previous valid superframe.
  1. Detailed bit allocation and bit semantics of the bitstream ==========================================================
    1. General \-------
This chapter defines the superframe structure of the metadata-assisted EVS
codec with all necessary signalling and data elements enabling a receiver to
decode metadata-assisted EVS codec data.
The superframe structure contains all necessary signalling elements to
  * Indicate the EVS codec modes used for EVS coding of the N~ch~ downmix signals.\ The default is N~ch~ = 4, meaning that there are 4 EVS codec downmix channels W, X', Y', Z'.
  * Indicate the selected operation mode of the metadata-assisted EVS code,
  * Indicate the metadata bitrate.
  * Provide the possibility to signal potential future extensions.
Certain signaling elements are only conditionally provided inband in the
superframe. If they are provided, these signaling elements can be dynamically
adapted on superframe basis. There is also the possibility to keep these
signaling elements static and to provide them only once, for instance as an
out-of-band message. The signaling elements may also be semi-dynamic in which
case they are provided inband only in certain superframes.
Note: In case the signaling elements are provided both out-of-band and inband,
the signaling obtained with the most recently received superframe shall
prevail.
The superframe is designed to enable the following features:
> • Full decoding and rendering of metadata-assisted EVS coded superframes.
>
> • Partial mono decoding of metadata-assisted EVS coded superframes.
>
> • Low-complexity extraction of superframe size information from a sequence
> of concatenated superframe data without need to decode the superframe data,
> e.g. to put it into a secondary format (ISOBMFF) that provides/needs that
> information.
>
> • Low-complexity bit rate determination without need to decode the
> superframe data.
>
> • Low-complexity feed-forward and skip of superframes without need to decode
> the superframe data.
>
> • Low-complexity feed-backward without need to decode the superframe data
> (requires constant bit rate operation).
>
> • Easy re-sync and superframe skip in case of bit errors in arithmetic and
> entropy coded EVS and metadata bitstream portions.
>
> • Editable superframes, which allows allowing replacing metadata or EVS data
> frames.
## Superframe of metadata-assisted EVS codec
A coded bit superframe of the metadata-assisted EVS codec corresponds to a
coding stride of 40ms. It is composed of the following elementary bit fields:
  * Base Header field (BH)
> This field carries a Configuration field Presence Indicator (CPI), a
> MetaData field size Adjustment indicator (MDA) and an Extension Indicator
> (EI).\ The CPI indicates whether the Configuration Information (CI) field is
> supplied in the present superframe.
>
> The MDA signals the difference between the signaled maximum metadata frame
> size and the actual metadata frame size.
>
> The EI signals if the superframe is extended by a Frame Extender (FE).
  * Configuration Information field (CI)
> This field carries signaling information related to the used configurations
> of the EVS, SPAR and Predictive Coefficient coding tools, such as frame type
> (coding mode), bit rate and other configuration parameters that are detailed
> below.
  * EVS bit field
> This field carries the bits of a single EVS frame (without EVS payload
> header), as specified in 26.445, section 7 [2].
  * SPAR bit field (SPAR)
> This field carries the bits of a single SPAR metadata frame, zero-padded at
> the end to make it byte-aligned.
  * Predictive Coefficient bit field (PC)
> This field carries the bits of a single predictive coefficient metadata
> frame, zero-padded at the end to make it byte-aligned.
  * Frame Extender (FE)
> This field is defined for future use and can carry extension data. Except
> for the size element contained in the FE, any other data carried by the FE
> is ffs.
Note: All elementary bit fields are byte-aligned and -- if necessary -- zero-
padded at the end up to their defined size.
These elementary fields are composed to a superframe in the following sequence
order. A superframe comprises
  * One Base Header (BH) containing
    * The Configuration field Presence Indicator (CPI),
    * The Metadata field size adjustment indicator (MDA) and
    * The Extension Indicator (EI).
  * One **optional** Configuration Information field (CI). The presence of the CI field is signaled by the CPI.
  * The data of NCH EVS encoded downmix channel signals S~1~ ... S~NCH~, two successive frames each, carried by 2* N~ch~ elementary EVS bit fields: EVS(.).In default operation with 4 downmix channel signals there are 8 successive EVS bit fields representing two frames of the downmix channels W, X', Y', Z'.
  * One metadata frame (MDF), either SPAR or predictive coefficients, carried by
    * One elementary SPAR bit field, or
    * One elementary PC bit field.
  * One optional Frame Extender (FE). The presence of the FE field is indicated by the EI.
Thus, a superframe has a structure as shown in table 6.2.a.
Table 6.2.a: Generic Superframe structure for NCH EVS coded downmix channels
* * *
**Bits (MSB‑LSB)** **Name** **Description** 8 BH Base Header, containing CPI,
MDA, EI Variable CI Configuration Information field (optional, depending on
CPI) Variable EVS (S~1,1~) EVS frame data for a first frame of 1st dmx channel
Variable EVS (S~2,1~) EVS frame data for a first frame of 2nd dmx channel
Variable EVS (S~...,1~) ... Variable EVS (S~NCH,1~) EVS frame data for a first
frame of NCH^th^ dmx channel Variable EVS (S~1~,2) EVS frame data for a second
frame of 1st dmx channel Variable EVS (S~2~,2) EVS frame data for a second
frame of 2nd dmx channel Variable EVS (S~...,2~) ... Variable EVS (S~NCH~,2)
EVS frame data for a second frame of NCH^th^ dmx channel Variable MDF Metadata
frame containing either a SPAR or a PC field Variable FE Frame Extender
(optional, depending on EI)
* * *
The default is that there are 4 EVS coded downmix channels. The superframe
structure for that default is shown in the following table 6.2.b.
Table 6.2.b: Superframe structure for default of 4 EVS coded downmix channels
* * *
**Bits (MSB‑LSB)** **Name** **Description** 8 BH Base Header, containing CPI,
MDA, EI 72 CI Configuration Information field (optional, depending on CPI)
Variable EVS (W(1)) EVS frame data for a first frame of signal W Variable EVS
(X'(1)) EVS frame data for a first frame of signal X\' Variable EVS (Y'(1))
EVS frame data for a first frame of signal Y\' Variable EVS (Z'(1)) EVS frame
data for a first frame of signal Z\' Variable EVS(W(2)) EVS frame data for a
second frame of signal W Variable EVS (X'(2)) EVS frame data for a second
frame of signal X\' Variable EVS (Y'(2)) EVS frame data for a second frame of
signal Y\' Variable EVS (Z'(2)) EVS frame data for a second frame of signal
Z\' Variable MDF Metadata frame containing either a SPAR or a PC field
Variable FE Frame Extender (optional, depending on EI)
* * *
The elementary bit fields are detailed in the following clauses.
  1. Base Header (BH) \----------------
    1. ### Base Header structure
The Base Header (BH) carries a Configuration field Presence Indicator (CPI), a
MetaData field size Adjustment indicator (MDA) and an Extension Indicator
(EI). This byte-field is always the first element in a superframe.
The structure of the BH is shown in table 6.3.a.
Table 6.3.a: Base Header (BH)
* * *
**Bits (MSB‑LSB)** **Name** **Description** 1 CPI Configuration field Presence
Indicator 6 MDA MetaData field size Adjustment 1 EI Extension Indicator
* * *
### Configuration field Presence Indicator (CPI)
The Configuration field Presence Indicator (CPI) is a single bit used to
signal the presence of the Configuration Information (CI) field in the present
superframe.
The CPI has the following meaning:
> CPI = '0': This indicates that the Configuration Information field is
> **not** provided in the present superframe. Note that the Configuration
> Information may instead be provided as static out-of-band information or
> from the most recent previously received superframe carrying the
> Configuration Information field.
>
> CPI = '1': This indicates that the Configuration Information field is
> provided in present superframe. The configuration information is valid for
> this and any future superframe until the next superframe carrying the
> Configuration Information field.
### MetaData field size Adjustment indicator (MDA)
The CPI bit is followed by the metadata field size adjustment indicator (MDA).
This 6-bit indicator signals the difference between the length of the MDF as
signaled by the MDR element (defined in clause 6.4.4) and the actual size of
the MDF. Using MDA as an index, the difference is found by look-up in the
following table 6.3.b. Note that the series of Adjustment values is specified
in Matlab style: start-value:step-size:end-value. The non-constant adjustment
parameter step sizes shown in the table are designed following an
approximative model of the distribution of the total entropy code length of
the metadata. This allows minimizing the number of unused bits in the MDF and
thus the transmission overhead.
Table 6.3.b: MDF Adjustment values for given MDA
* * *
MDA 0...47 48...55 56...59 60...61 62 63 Adjustment value 0:1:47 49:2:63
67:4:79 87:8:95 111 143
* * *
Depending on the maximum MDF size the adjustment value represents single-byte
or two-byte units. For maximum MDF sizes up to 275 bytes the adjustment unit
is single-byte, otherwise two-byte.
### Extension Indicator (EI)
The MDA indicator is followed by a single Extension Indicator bit (EI). If
this bit is set to 1, the present superframe is appended by a Frame Extender
(FE) element.
## Configuration Information field (CI)
The optionally supplied Configuration Information field carries the following
signaling elements as illustrated in the following table 6.4.a. It consists of
8 bytes of data.
Table 6.4.a: Configuration Information field (CI)
* * *
**Bits (MSB‑LSB)** **Name** **Description** 3 NCH-I Indicator for number of
EVS codec downmix channels 1 MDT Metadata Type indication 11 MDC Metadata
Coding configuration 5 MDR Metadata bit rate signaling 3 BND Number of
metadata coding bands 1 RES Reserved, ffs. 6 FT-1,1 EVS FT for first frame of
1st dmx channel 6 FT-2,1 EVS FT for first frame of 2nd dmx channel 6 ... ... 6
FT-NCH,1 EVS FT for first frame of NCHth dmx channel 6 FT-1,2 EVS FT for
second frame of 1st dmx channel 6 FT-2,2 EVS FT for second frame of 2nd dmx
channel 6 ... ... 6 FT-NCH,2 EVS FT for second frame of NCHth dmx channel
variable zero-pad Zero-Padding to fill up byte
* * *
Table 6.4.b illustrates the optional Configuration Information field for the
default case with 4 EVS coded downmix channels. In that case the CI field
consists of 9 bytes of data.
Table 6.4.b: Configuration Information field (CI) for default of 4 EVS coded
downmix channels
* * *
**Bits (MSB‑LSB)** **Name** **Description** 3 NCH-I \'011\' indicating 4 EVS
codec downmix channels 1 MDT Metadata Type indication 11 MDC Metadata Coding
configuration 5 MDR Metadata bit rate signaling 3 BND Number of metadata
coding bands 1 RES Reserved, ffs. 6 FT-1,1 EVS FT for coding of W(1) 6 FT-2,1
EVS FT for coding of X\'(1) 6 FT-3,1 EVS FT for coding of Y\'(1) 6 FT-4,1 EVS
FT for coding of Z\'(1) 6 FT-1,2 EVS FT for coding of W(2) 6 FT-2,2 EVS FT for
coding of X\'(2) 6 FT-3,2 EVS FT for coding of Y\'(2) 6 FT-4,2 EVS FT for
coding of Z\'(2)
* * *
### Indicator for Number of EVS coded downmix channels (NCH-I)
NCH-I is a 3-bit element that encodes the number NCH of EVS coded downmix
channels. NCH is obtained from the indicator NCH-I by incrementing the number
represented by that 3-bit element by 1. For achieving the default operation
with 4 EVS downmix channels, the NCH-I element must be set to 3 ('011').
### Metadata Type indication (MDT)
The Metadata Type indication bit (MDT) has the following meaning:
> MDT = '0': indicates that the MDF carries a PC bit field.
>
> MDT = '1': indicates that the MDF carries a SPAR bit field.
### MetaData Coding configuration field (MDC)
The Metadata Coding configuration (MDC) field comprises either configuration
information of the used Predictive Coefficient or the SPAR coding tool,
depending on the indication of the MDT bit.
The MDC field is an 11-bit element of the CI. The meaning of its bits depends
on the MDT bit of the CI. Depending on the value of MDT, the MDC bits have the
following meaning:
> MDT = '0': If the MDT bit is zero, the 3 MSBs of the MDC encode a
> configuration parameter of the predictive coefficient coding scheme. The
> remaining 8 bits of the MDC are unused and zero-padded. The structure and
> contents of the MDC field in this case is shown in table 6.4.b
>
> MDT = '1': If the MDT bit is one, the 11 MDC bits encode the SPAR codec
> configuration as illustrated in table 6.4.c
Table 6.4.b: Structure and contents of MDC field if MDT = '0'
* * *
Bits (MSB‑LSB) Name Description Value range 3 coding_strategy_idx Index into
Huffman Table 0 -- 7 8 Zero-padding
* * *
Table 6.4.c: Structure and contents of MDC field if MDT = '1'
* * *
Bits (MSB‑LSB) Name Description Value range 4 n~obj~ Number of audio objects 1
-- 15 2 hoa_order_idx Identifier for HOA order 0 - 2 2 n~deco~ Number of
decorrelators 0 - 3 3 coding_strategy_idx Index into Huffman Table 0 - 7
* * *
> Note: The HOA order is calculated by incrementing hoa_order_idx by 1.
### MetaData Bit rate signalling field (MDR)
The 5 bits of the Metadata bit rate signaling field (MDR) encodes the maximum
size of the MDF. The maximum MDF size is obtained by table lookup, where the
MDR value is an index into the following table 6.4.d. Also shown is the
(maximum) Metadata bit rate in kbps.
Note that the actual MDF size is signaled as the maximum MDF size minus the
adjustment number number indicated by the MDA. This allows signaling of the
actual MDF size with fine resolution (typically byte resolution).
Note also that any unused bit in the MDF is zero-padded, which may happen in
case the actual MDF size offers more space than needed for the coded metadata.
Table 6.4.d: Maximum MDF size and maximum Metadata bit rate for given MDR
value
* * *
**MDR value** **Metadata bit rate (kbps)** **Maximum MDF size (bytes)** 0 4 20
1 5 25 2 6 30 3 7 35 4 8 40 5 10 50 6 12 60 7 15 75 8 18 90 9 21 105 10 24 120
11 28 140 12 32 160 13 36 180 14 40 200 15 42 210 16 45 225 17 47 235 18 50
250 19 55 275 20 60 300 21 65 325 22 70 350 23 75 375 24 80 400 25 85 425 26
90 450 27 95 475 28 100 500 29 105 525 30 110 550 31 128 640
* * *
### Band Number field (BND)
The 3-bit number of the Band Number field (BND) indicates the number of bands
used in metadata coding. The band number is derived from the BND value by
means of lookup in table 6.4.e. In default operation the BND field is set to 5
('101'), which indicates 12 bands.
Table 6.4.e: Number of bands for given BND value
* * *
**BND (3 bits)** **Number of bands** 0 1 1 3 2 5 3 7 4 9 5 12 6 15 7 23
* * *
### Reserved bit (RES)
The use of the Reserved bit is ffs. In default operations this bit shall be
set to '0' and ignored by a receiver.
### EVS FT field (FT-x,y)
The EVS FT-x,y field represents the EVS frame type applied for coding of the
y^th^ frame of the x^th^ downmix channel signal, where x=1...NCH and y=1,2. It
is defined in 3GPP TS 26.445, A2.2.1.2 [2].
Note that the last EVS FT field in the CI field is followed by less than 8
zero-padding bits, which ensure octet-alignment. In case the last EVS FT field
ends octet-aligned, no zero-padding bits are appended. Zero-padding bits shall
be ignored by a receiver.
## EVS bit field
The elementary EVS bit field is defined as specified in 3GPP TS 26.445 [1],
section 7, for the respectively used EVS coding mode. Like in that reference,
no extra signalling bits are defined as part of the elementary EVS frame field
to indicate the bit rate or the EVS operation mode. Note that this kind of
information is part of the optional CI field of this or a previous superframe
or may also be provided out-of-band.
## Detailed bit allocation and bit semantics of the SPAR frame field
The detailed allocation of the coefficients for SPAR metadata is shown table
6.6.a. These tables show the order of the bits as they are inserted in a
frame. Note that the most significant bit (MSB) of each parameter is always
inserted first. As each field is dynamically quantized, their bit allocation
is variable.
Table 6.6.a: Fields of SPAR frame bits
* * *
Name Description Encoding obj_pos Matrix of object positions Position-
dependent quantization **Mspar** HOA SPAR reconstruction matrix Huffman coded
**Pspar** SPAR matrix Huffman coded
* * *
## Detailed bit allocation and bit semantics of predictive coefficient (PC)
frame field
The detailed allocation of the coefficients for PC metadata is shown table
6.7.a. These tables show the order of the bits as they are inserted in a
frame. Note that the most significant bit (MSB) of each parameter is always
inserted first. As each field is dynamically quantized, their bit allocation
is variable.
Table 6.7.a: Fields of PC frame bits
* * *
Name Description Encoding **Gfoa** Matrix of predictive coefficients Huffman
coded
* * *
## Frame Extender (FE)
The FE element always carries in its first two bytes a 16-bit unsigned integer
number that indicates the size of the FE in bytes. That element is called FE-
size. The FE-size number must hence be greater or equal to 2\. The contents
and meaning of the remaining FE-data part of the FE beyond the size indicator
is ffs. In default operation the FE-size element must be parsed and the FE-
data element be skipped and gnored.
The structure and contents of the FE is shown in table 6.8.a.
Table 6.8.a: Structure and contents of FE field
* * *
**Bits (MSB‑LSB)** **Name** **Description** 16 FE-size Size of FE field
Variable FE-data data bits carried in FE field
* * *
  1. Non-normative Reference Renderers =================================
    1. Loudspeaker renderer \--------------------
The non-normative reference loudspeaker renderer of the metadata-assisted EVS
codec is specified in clause 5.2.3.6. This renderer supports a set of
predefined relevant output loudspeaker configurations such as 5.1 (ITU-R
System B), 5.1.4 (System D), 7.1 (System I) and 7.1.4 (System J). ITU
Loudspeaker Systems are specified in [6]. Two configurations for 7.1.4 (System
J) are predefined, one with L/R speakers at +-30 degrees (setting 1) and one
with L/R speakers at +-45 degrees (setting 2). In addition to the predefined
output loudspeaker configurations, the function interfaces of the provided
renderer pseudocode define an API that allows specifying renderer matrices for
arbitrary loudspeaker configurations and an arbitrary number of loudspeaker
channels.
## Binaural renderer
The non-normative reference loudspeaker renderer of the metadata-assisted EVS
codec is specified in 3GPP TS 26.118 [7], clause 4.5.1.2, as Common
Informative Binaural Renderer (CIBR).
# Annex A (informative): Encoder description {#annex-a-informative-encoder-
description .list-paragraph}
The encoder of the metadata-assisted EVS codec is described on high-level in
clause 4. The EVS encoders for the encoding of the 4 downmix channels W, X',
Y', Z' are either based on 3GPP standards compliant implementations of the EVS
fixed-point encoder [3] or the EVS floating-point encoder [4].
# Annex B: Huffman Coding Tables {#annex-b-huffman-coding-tables .list-
paragraph}
Table 1: Huffman table for coding_strategy_idx=0, huff_idx = 0
* * *
Value Code -2.1000 11111111111111111111110 -2 1111111111111111111110 -1.9000
111111111111111111100 -1.8000 11111111111111111100 -1.7000 1111111111111111100
-1.6000 111111111111111100 -1.5000 11111111111111100 -1.4000 1111111111111100
-1.3000 111111111111100 -1.2000 11111111111100 -1.1000 1111111111100 -1
111111111100 -0.9000 11111111100 -0.8000 1111111100 -0.7000 111111100 -0.6000
11111100 -0.5000 1111100 -0.4000 111100 -0.3000 11100 -0.2000 1100 -0.1000 100
0 0 0.1000 101 0.2000 1101 0.3000 11101 0.4000 111101 0.5000 1111101 0.6000
11111101 0.7000 111111101 0.8000 1111111101 0.9000 11111111101 1 111111111101
1.1000 1111111111101 1.2000 11111111111101 1.3000 111111111111101 1.4000
1111111111111101 1.5000 11111111111111101 1.6000 111111111111111101 1.7000
1111111111111111101 1.8000 11111111111111111101 1.9000 111111111111111111101 2
111111111111111111110 2.1000 11111111111111111111111
* * *
Table 2: Huffman table for coding_strategy_idx=0, huff_idx = 1
* * *
Value Code
-0.8000 1111111110 -0.7000 111111110 -0.6000 11111100 -0.5000 1111100 -0.4000 111100 -0.3000 11100 -0.2000 1100 -0.1000 100 0 0 0.1000 101 0.2000 1101 0.3000 11101 0.4000 111101 0.5000 1111101 0.6000 11111101 0.7000 11111110 0.8000 1111111111
* * *
Table 3: Huffman table for coding_strategy_idx=1, huff_idx = 0
* * *
Value Code -2 111111111111111110 -1.8750 11111111111111110 -1.7500
1111111111111100 -1.6250 111111111111100 -1.5000 11111111111100 -1.3750
1111111111100 -1.2500 111111111100 -1.1250 11111111100 -1 1111111100 -0.8750
111111100 -0.7500 11111100 -0.6250 1111100 -0.5000 111100 -0.3750 11100
-0.2500 1100 -0.1250 100 0 0 0.1250 101 0.2500 1101 0.3750 11101 0.5000 111101
0.6250 1111101 0.7500 11111101 0.8750 111111101 1 1111111101 1.1250
11111111101 1.2500 111111111101 1.3750 1111111111101 1.5000 11111111111101
1.6250 111111111111101 1.7500 1111111111111101 1.8750 1111111111111110 2
111111111111111111
* * *
Table 4: Huffman table for coding_strategy_idx=1, huff_idx = 1
* * *
Value Code -0.7500 11111110 -0.6250 1111110 -0.5000 111100 -0.3750 11100
-0.2500 1100 -0.1250 100 0 0 0.1250 101 0.2500 1101 0.3750 11101 0.5000 111101
0.6250 111110 0.7500 11111111
* * *
Table 5: Huffman table for coding_strategy_idx=2, huff_idx = 0
* * *
Value Code -2.1000 1111111111111110 -1.9500 111111111111110 -1.8000
11111111111100 -1.6500 1111111111100 -1.5000 111111111100 -1.3500 11111111100
-1.2000 1111111100 -1.0500 111111100 -0.9000 11111100 -0.7500 1111100 -0.6000
111100 -0.4500 11100 -0.3000 1100 -0.1500 100 0 0 0.1500 101 0.3000 1101
0.4500 11101 0.6000 111101 0.7500 1111101 0.9000 11111101 1.0500 111111101
1.2000 1111111101 1.3500 11111111101 1.5000 111111111101 1.6500 1111111111101
1.8000 11111111111101 1.9500 11111111111110 2.1000 1111111111111111
* * *
Table 6: Huffman table for coding_strategy_idx=2, huff_idx = 1
* * *
Value Code -0.7500 1111110 -0.6000 111110 -0.4500 11100 -0.3000 1100 -0.1500
100 0 0 0.1500 101 0.3000 1101 0.4500 11101 0.6000 11110 0.7500 1111111
* * *
Table 7: Huffman table for coding_strategy_idx=3, huff_idx = 0
Table 8: Huffman table for coding_strategy_idx=3, huff_idx = 1
* * *
Value Code -0.8000 111110 -0.6000 11110 -0.4000 1100 -0.2000 100 0 0 0.2000
101 0.4000 1101 0.6000 1110 0.8000 111111
* * *
Table 9: Huffman table for coding_strategy_idx=4, huff_idx = 0
* * *
Value Code -2 1111111110 -1.7500 111111110 -1.5000 11111100 -1.2500 1111100 -1
111100 -0.7500 11100 -0.5000 1100 -0.2500 100 0 0 0.2500 101 0.5000 1101
0.7500 11101 1 111101 1.2500 1111101 1.5000 11111101 1.7500 11111110 2
1111111111
* * *
Table 10: Huffman table for coding_strategy_idx=4, huff_idx = 1
* * *
Value Code -0.7500 11110 -0.5000 1110 -0.2500 100 0 0 0.2500 101 0.5000 110
0.7500 11111
* * *
Table 11: Huffman table for coding_strategy_idx=5, huff_idx = 0
* * *
Value Code -2.1000 111111110 -1.8000 11111110 -1.5000 1111100 -1.2000 111100
-0.9000 11100 -0.6000 1100 -0.3000 100 0 0 0.3000 101 0.6000 1101 0.9000 11101
1.2000 111101 1.5000 1111101 1.8000 1111110 2.1000 111111111
* * *
Table 12: Huffman table for coding_strategy_idx=5, huff_idx = 1
* * *
Value Code -0.6000 1110 -0.3000 110 0 0 0.3000 10 0.6000 1111
* * *
Table 13: Huffman table for coding_strategy_idx=6, huff_idx = 0
* * *
Value Code -2 1111110 -1.6000 111110 -1.2000 11100 -0.8000 1100 -0.4000 100 0
0 0.4000 101 0.8000 1101 1.2000 11101 1.6000 11110 2 1111111
* * *
Table 14: Huffman table for coding_strategy_idx=6, huff_idx = 1
* * *
Value Code -0.8000 1110 -0.4000 110 0 0 0.4000 10 0.8000 1111
* * *
Table 15: Huffman table for coding_strategy_idx=7, huff_idx = 0
* * *
Value Code -1.2000 1110 -0.6000 110 0 0 0.6000 10 1.2000 1111
* * *
Table 16: Huffman table for coding_strategy_idx=7, huff_idx = 1
* * *
Value Code -0.6000 10 0 0 0.6000 11
* * *
# Annex C: Renderer HOA and FOA Matrices {#annex-c-renderer-hoa-and-foa-
matrices .list-paragraph}
Table 17: HOA3 Matrix for 5.1 Renderer Output Mode
* * *
0.18938131 0.18938131 0.12927546 0.00000000 0.35534804 0.35534804 0.28735138
-0.28735138 0.00000000 0.00000000 0.37766010 -0.37766010 0.00000000 0.00000000
0.00000000 0.00000000 0.00000000 0.00000000 0.22384034 0.22384034 0.30720976
0.00000000 -0.38341603 -0.38341603 0.33934803 -0.33934803 0.00000000
0.00000000 -0.20510557 0.20510557 0.00000000 0.00000000 0.00000000 0.00000000
0.00000000 0.00000000 0.04057068 0.04057068 -0.06298059 0.00000000 0.08402277
0.08402277 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000
-0.08127967 -0.08127967 0.32374045 0.00000000 -0.06190172 -0.06190172
0.11009110 -0.11009110 0.00000000 0.00000000 -0.11207080 0.11207080 0.00000000
0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 0.04004456 -0.04004456
0.00000000 0.00000000 0.05239918 -0.05239918 0.00000000 0.00000000 0.00000000
0.00000000 0.00000000 0.00000000 0.03054520 0.03054520 0.04308090 0.00000000
-0.05333798 -0.05333798 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000
0.00000000 -0.21348566 -0.21348566 0.26965520 0.00000000 0.04020133 0.04020133
* * *
Table 18: HOA2 Matrix for 5.1 Renderer Output Mode
* * *
0.18938131 0.18938131 0.12927546 0.00000000 0.35534804 0.35534804 0.28735138
-0.28735138 0.00000000 0.00000000 0.37766010 -0.37766010 0.00000000 0.00000000
0.00000000 0.00000000 0.00000000 0.00000000 0.22384034 0.22384034 0.30720976
0.00000000 -0.38341603 -0.38341603 0.33934803 -0.33934803 0.00000000
0.00000000 -0.20510557 0.20510557 0.00000000 0.00000000 0.00000000 0.00000000
0.00000000 0.00000000 0.04057068 0.04057068 -0.06298059 0.00000000 0.08402277
0.08402277 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000
-0.08127967 -0.08127967 0.32374045 0.00000000 -0.06190172 -0.06190172
* * *
Table 19: FOA Matrix for 5.1 Renderer Output Mode
* * *
0.18938131 0.18938131 0.12927546 0.00000000 0.35534804 0.35534804 0.28735138
-0.28735138 0.00000000 0.00000000 0.37766010 -0.37766010 0.00000000 0.00000000
0.00000000 0.00000000 0.00000000 0.00000000 0.22384034 0.22384034 0.30720976
0.00000000 -0.38341603 -0.38341603
* * *
Table 20: HOA3 Matrix for 7.1 Renderer Output Mode
* * *
0.12887044 0.12887044 0.12927546 0.00000000 0.20652640 0.20652640 0.19365048
0.19365048 0.21676176 -0.21676176 0.00000000 0.00000000 0.30729570 -0.30729570
0.20804827 -0.20804827 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000
0.00000000 0.00000000 0.00000000 0.21685164 0.21685164 0.30720976 0.00000000
0.00000000 0.00000000 -0.37209755 -0.37209755 0.32351405 -0.32351405
0.00000000 0.00000000 0.00000000 0.00000000 -0.30414077 0.30414077 0.00000000
0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000
-0.06365665 -0.06365665 -0.06298059 0.00000000 0.22553863 0.22553863
-0.09489823 -0.09489823 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000
0.00000000 0.00000000 0.00000000 0.00018659 0.00018659 0.32374045 0.00000000
-0.32365008 -0.32365008 0.16870008 0.16870008 0.19106191 -0.19106191
0.00000000 0.00000000 -0.26973150 0.26973150 0.16428502 -0.16428502 0.00000000
0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000
0.03026938 -0.03026938 0.00000000 0.00000000 0.04253819 -0.04253819 0.02915563
-0.02915563 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000
0.00000000 0.00000000 0.02962656 0.02962656 0.04308090 0.00000000 0.00000000
0.00000000 -0.05176834 -0.05176834 0.00000000 0.00000000 0.00000000 0.00000000
0.00000000 0.00000000 0.00000000 0.00000000 -0.19082699 -0.19082699 0.26965520
0.00000000 0.00000000 0.00000000 0.04158077 0.04158077
* * *
Table 21: HOA2 Matrix for 7.1 Renderer Output Mode
* * *
0.12887044 0.12887044 0.12927546 0.00000000 0.20652640 0.20652640 0.19365048
0.19365048 0.21676176 -0.21676176 0.00000000 0.00000000 0.30729570 -0.30729570
0.20804827 -0.20804827 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000
0.00000000 0.00000000 0.00000000 0.21685164 0.21685164 0.30720976 0.00000000
0.00000000 0.00000000 -0.37209755 -0.37209755 0.32351405 -0.32351405
0.00000000 0.00000000 0.00000000 0.00000000 -0.30414077 0.30414077 0.00000000
0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000
-0.06365665 -0.06365665 -0.06298059 0.00000000 0.22553863 0.22553863
-0.09489823 -0.09489823 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000
0.00000000 0.00000000 0.00000000 0.00018659 0.00018659 0.32374045 0.00000000
-0.32365008 -0.32365008 0.16870008 0.16870008
* * *
Table 22: FOA Matrix for 7.1 Renderer Output Mode
* * *
0.12887044 0.12887044 0.12927546 0.00000000 0.20652640 0.20652640 0.19365048
0.19365048 0.21676176 -0.21676176 0.00000000 0.00000000 0.30729570 -0.30729570
0.20804827 -0.20804827 0.00000000 0.00000000 0.00000000 0.00000000 0.00000000
0.00000000 0.00000000 0.00000000 0.21685164 0.21685164 0.30720976 0.00000000
0.00000000 0.00000000 -0.37209755 -0.37209755
* * *
Table 23: HOA3 Matrix for 5.1.4 Renderer Output Mode
* * *
0.13145141 0.13145141 0.09477013 0.00000000 0.24624146 0.24624146 0.10976274
0.10976274 0.10976274 0.10976274 0.21946196 -0.21946196 0.00000000 0.00000000
0.28847616 -0.28847616 0.11221826 -0.11221826 0.11221826 -0.11221826
-0.12093275 -0.12093275 -0.06383969 0.00000000 -0.22852729 -0.22852729
0.21032200 0.21032200 0.21032200 0.21032200 0.17102822 0.17102822 0.23473710
0.00000000 -0.29292637 -0.29292637 0.11207454 0.11207454 -0.11207454
-0.11207454 0.26763056 -0.26763056 0.00000000 0.00000000 -0.16175244
0.16175244 0.08210867 -0.08210867 -0.08210867 0.08210867 -0.11213636
0.11213636 0.00000000 0.00000000 -0.14732914 0.14732914 0.16801228 -0.16801228
0.16801228 -0.16801228 -0.04597007 -0.04597007 -0.08584085 0.00000000
-0.08164652 -0.08164652 0.11033684 0.11033684 0.11033684 0.11033684
-0.08718537 -0.08718537 -0.11983750 0.00000000 0.14952332 0.14952332
0.16794741 0.16794741 -0.16794741 -0.16794741 -0.06403183 -0.06403183
0.25536699 0.00000000 -0.04876190 -0.04876190 -0.00011287 -0.00011287
-0.00011287 -0.00011287 0.08908808 -0.08908808 0.00000000 0.00000000
-0.09063085 0.09063085 0.00396282 -0.00396282 0.00396282 -0.00396282
-0.12022106 0.12022106 0.00000000 0.00000000 0.07267956 -0.07267956 0.12387604
-0.12387604 -0.12387604 0.12387604 -0.04131687 0.04131687 0.00000000
0.00000000 -0.05458656 0.05458656 0.09216054 -0.09216054 0.09216054
-0.09216054 -0.01318574 -0.01318574 0.03814479 0.00000000 -0.02917577
-0.02917577 -0.02891966 -0.02891966 -0.02891966 -0.02891966 -0.03255723
-0.03255723 -0.04418025 0.00000000 0.05524858 0.05524858 0.09227158 0.09227158
-0.09227158 -0.09227158 0.02892120 0.02892120 -0.11473013 0.00000000
0.02194241 0.02194241 0.00005849 0.00005849 0.00005849 0.00005849 -0.17261106
-0.17261106 0.21806680 0.00000000 0.03239099 0.03239099 -0.00421142
-0.00421142 0.00421142 0.00421142
* * *
Table 24: HOA2 Matrix for 5.1.4 Renderer Output Mode
* * *
0.13145141 0.13145141 0.09477013 0.00000000 0.24624146 0.24624146 0.10976274
0.10976274 0.10976274 0.10976274 0.21946196 -0.21946196 0.00000000 0.00000000
0.28847616 -0.28847616 0.11221826 -0.11221826 0.11221826 -0.11221826
-0.12093275 -0.12093275 -0.06383969 0.00000000 -0.22852729 -0.22852729
0.21032200 0.21032200 0.21032200 0.21032200 0.17102822 0.17102822 0.23473710
0.00000000 -0.29292637 -0.29292637 0.11207454 0.11207454 -0.11207454
-0.11207454 0.26763056 -0.26763056 0.00000000 0.00000000 -0.16175244
0.16175244 0.08210867 -0.08210867 -0.08210867 0.08210867 -0.11213636
0.11213636 0.00000000 0.00000000 -0.14732914 0.14732914 0.16801228 -0.16801228
0.16801228 -0.16801228 -0.04597007 -0.04597007 -0.08584085 0.00000000
-0.08164652 -0.08164652 0.11033684 0.11033684 0.11033684 0.11033684
-0.08718537 -0.08718537 -0.11983750 0.00000000 0.14952332 0.14952332
0.16794741 0.16794741 -0.16794741 -0.16794741 -0.06403183 -0.06403183
0.25536699 0.00000000 -0.04876190 -0.04876190 -0.00011287 -0.00011287
-0.00011287 -0.00011287
* * *
Table 25: FOA Matrix for 5.1.4 Renderer Output Mode
* * *
0.13145141 0.13145141 0.09477013 0.00000000 0.24624146 0.24624146 0.10976274
0.10976274 0.10976274 0.10976274 0.21946196 -0.21946196 0.00000000 0.00000000
0.28847616 -0.28847616 0.11221826 -0.11221826 0.11221826 -0.11221826
-0.12093275 -0.12093275 -0.06383969 0.00000000 -0.22852729 -0.22852729
0.21032200 0.21032200 0.21032200 0.21032200 0.17102822 0.17102822 0.23473710
0.00000000 -0.29292637 -0.29292637 0.11207454 0.11207454 -0.11207454
-0.11207454
* * *
Table 26: HOA3 Matrix for 7.1.4 Renderer Output Mode ('Setting 1')
* * *
0.09447570 0.09447570 0.09477013 0.00000000 0.13337425 0.13337425 0.14194645
0.14194645 0.10976274 0.10976274 0.10976274 0.10976274 0.16555328 -0.16555328
0.00000000 0.00000000 0.23473430 -0.23473430 0.15888607 -0.15888607 0.11221826
-0.11221826 0.11221826 -0.11221826 -0.06350683 -0.06350683 -0.06383969
0.00000000 -0.16921683 -0.16921683 -0.09556458 -0.09556458 0.21032200
0.21032200 0.21032200 0.21032200 0.16568240 0.16568240 0.23473710 0.00000000
0.00000000 0.00000000 -0.28428135 -0.28428135 0.11207454 0.11207454
-0.11207454 -0.11207454 0.25512285 -0.25512285 0.00000000 0.00000000
0.00000000 0.00000000 -0.23982333 0.23982333 0.08210867 -0.08210867
-0.08210867 0.08210867 -0.08461093 0.08461093 0.00000000 0.00000000
-0.11985309 0.11985309 -0.08123688 0.08123688 0.16801228 -0.16801228
0.16801228 -0.16801228 -0.08598911 -0.08598911 -0.08584085 0.00000000
0.05843102 0.05843102 -0.12881695 -0.12881695 0.11033684 0.11033684 0.11033684
0.11033684 -0.08447184 -0.08447184 -0.11983750 0.00000000 0.00000000
0.00000000 0.14510996 0.14510996 0.16794741 0.16794741 -0.16794741 -0.16794741
0.00020807 0.00020807 0.25536699 0.00000000 -0.25529606 -0.25529606 0.13312531
0.13312531 -0.00011287 -0.00011287 -0.00011287 -0.00011287 0.15453231
-0.15453231 0.00000000 0.00000000 -0.21812662 0.21812662 0.13285395
-0.13285395 0.00396282 -0.00396282 0.00396282 -0.00396282 -0.11464933
0.11464933 0.00000000 0.00000000 0.00000000 0.00000000 0.10782882 -0.10782882
0.12387604 -0.12387604 -0.12387604 0.12387604 -0.03119413 0.03119413
0.00000000 0.00000000 -0.04446359 0.04446359 -0.02987736 0.02987736 0.09216054
-0.09216054 0.09216054 -0.09216054 0.03881697 0.03881697 0.03814479 0.00000000
-0.10951750 -0.10951750 0.05775874 0.05775874 -0.02891966 -0.02891966
-0.02891966 -0.02891966 -0.03150061 -0.03150061 -0.04418025 0.00000000
0.00000000 0.00000000 0.05363108 0.05363108 0.09227158 0.09227158 -0.09227158
-0.09227158 0.00009541 0.00009541 -0.11473013 0.00000000 0.11451866 0.11451866
-0.05965501 -0.05965501 0.00005849 0.00005849 0.00005849 0.00005849
-0.15425105 -0.15425105 0.21806680 0.00000000 0.00000000 0.00000000 0.03353969
0.03353969 -0.00421142 -0.00421142 0.00421142 0.00421142
* * *
Table 27: HOA2 Matrix for 7.1.4 Renderer Output Mode ('Setting 1')
* * *
0.09447570 0.09447570 0.09477013 0.00000000 0.13337425 0.13337425 0.14194645
0.14194645 0.10976274 0.10976274 0.10976274 0.10976274 0.16555328 -0.16555328
0.00000000 0.00000000 0.23473430 -0.23473430 0.15888607 -0.15888607 0.11221826
-0.11221826 0.11221826 -0.11221826 -0.06350683 -0.06350683 -0.06383969
0.00000000 -0.16921683 -0.16921683 -0.09556458 -0.09556458 0.21032200
0.21032200 0.21032200 0.21032200 0.16568240 0.16568240 0.23473710 0.00000000
0.00000000 0.00000000 -0.28428135 -0.28428135 0.11207454 0.11207454
-0.11207454 -0.11207454 0.25512285 -0.25512285 0.00000000 0.00000000
0.00000000 0.00000000 -0.23982333 0.23982333 0.08210867 -0.08210867
-0.08210867 0.08210867 -0.08461093 0.08461093 0.00000000 0.00000000
-0.11985309 0.11985309 -0.08123688 0.08123688 0.16801228 -0.16801228
0.16801228 -0.16801228 -0.08598911 -0.08598911 -0.08584085 0.00000000
0.05843102 0.05843102 -0.12881695 -0.12881695 0.11033684 0.11033684 0.11033684
0.11033684 -0.08447184 -0.08447184 -0.11983750 0.00000000 0.00000000
0.00000000 0.14510996 0.14510996 0.16794741 0.16794741 -0.16794741 -0.16794741
0.00020807 0.00020807 0.25536699 0.00000000 -0.25529606 -0.25529606 0.13312531
0.13312531 -0.00011287 -0.00011287 -0.00011287 -0.00011287
* * *
Table 28: FOA Matrix for 7.1.4 Renderer Output Mode ('Setting 1')
* * *
0.09447570 0.09447570 0.09477013 0.00000000 0.13337425 0.13337425 0.14194645
0.14194645 0.10976274 0.10976274 0.10976274 0.10976274 0.16555328 -0.16555328
0.00000000 0.00000000 0.23473430 -0.23473430 0.15888607 -0.15888607 0.11221826
-0.11221826 0.11221826 -0.11221826 -0.06350683 -0.06350683 -0.06383969
0.00000000 -0.16921683 -0.16921683 -0.09556458 -0.09556458 0.21032200
0.21032200 0.21032200 0.21032200 0.16568240 0.16568240 0.23473710 0.00000000
0.00000000 0.00000000 -0.28428135 -0.28428135 0.11207454 0.11207454
-0.11207454 -0.11207454
* * *
Table 29-bis: HOA3 Matrix for 7.1.4 Renderer Output Mode ('Setting 2')
* * *
0.121539 0.121539 0.083516 0.000000 0.130118 0.130118 0.162746 0.162746
0.093765 0.093765 0.099258 0.099258 0.153739 -0.153739 0.000000 0.000000
0.269527 -0.269527 0.186546 -0.186546 0.112794 -0.112794 0.111381 -0.111381
-0.108138 -0.108138 -0.080900 0.000000 -0.112558 -0.112558 -0.156750 -0.156750
0.183547 0.183547 0.188668 0.188668 0.208715 0.208715 0.170158 0.000000
0.014120 0.014120 -0.270492 -0.270492 0.109080 0.109080 -0.125639 -0.125639
0.246893 -0.246893 0.000000 0.000000 0.029551 -0.029551 -0.270446 0.270446
0.109215 -0.109215 -0.110008 0.110008 -0.079495 0.079495 0.000000 0.000000
-0.109142 0.109142 -0.095095 0.095095 0.176624 -0.176624 0.176225 -0.176225
-0.040039 -0.040039 0.001204 0.000000 -0.022643 -0.022643 -0.044890 -0.044890
0.107286 0.107286 0.099708 0.099708 -0.092911 -0.092911 -0.076656 0.000000
-0.007627 -0.007627 0.139145 0.139145 0.175515 0.175515 -0.188829 -0.188829
0.078719 0.078719 0.180177 0.000000 -0.267692 -0.267692 0.101132 0.101132
-0.007640 -0.007640 0.017242 0.017242 0.193549 -0.193549 0.000000 0.000000
-0.213998 0.213998 0.167184 -0.167184 0.027087 -0.027087 0.035387 -0.035387
-0.080642 0.080642 0.000000 0.000000 -0.012671 0.012671 0.089479 -0.089479
0.157798 -0.157798 -0.159340 0.159340 -0.024949 0.024949 0.000000 0.000000
-0.024327 0.024327 -0.035100 0.035100 0.121875 -0.121875 0.123652 -0.123652
-0.016837 -0.016837 -0.030670 0.000000 -0.035308 -0.035308 -0.017114 -0.017114
-0.008139 -0.008139 -0.018579 -0.018579 -0.037050 -0.037050 -0.003105 0.000000
-0.004420 -0.004420 0.048097 0.048097 0.127618 0.127618 -0.119103 -0.119103
-0.009171 -0.009171 -0.044675 0.000000 0.056714 0.056714 -0.034584 -0.034584
-0.004344 -0.004344 0.014411 0.014411 -0.063643 -0.063643 0.163681 0.000000
-0.036786 -0.036786 0.045859 0.045859 -0.044834 -0.044834 0.017573 0.017573
* * *
Table 30-bis: HOA2 Matrix for 7.1.4 Renderer Output Mode ('Setting 2')
* * *
0.12645 0.12645 0.08269 0.00000 0.12128 0.12128 0.17517 0.17517 0.09991
0.09991 0.10503 0.10503 0.15707 -0.15707 0.00000 0.00000 0.24395 -0.24395
0.21263 -0.21263 0.11957 -0.11957 0.11801 -0.11801 -0.10530 -0.10530 -0.07888
0.00000 -0.11477 -0.11477 -0.15238 -0.15238 0.18883 0.18883 0.19381 0.19381
0.21640 0.21640 0.16546 0.00000 0.02227 0.02227 -0.27767 -0.27767 0.11173
0.11173 -0.12694 -0.12694 0.24133 -0.24133 0.00000 0.00000 0.04672 -0.04672
-0.27220 0.27220 0.10574 -0.10574 -0.10620 0.10620 -0.07622 0.07622 0.00000
0.00000 -0.11564 0.11564 -0.08921 0.08921 0.17452 -0.17452 0.17410 -0.17410
-0.04365 -0.04365 0.00647 0.00000 -0.00825 -0.00825 -0.05891 -0.05891 0.10077
0.10077 0.09437 0.09437 -0.08808 -0.08808 -0.07354 0.00000 -0.00638 -0.00638
0.13186 0.13186 0.16920 0.16920 -0.18159 -0.18159 0.08107 0.08107 0.16801
0.00000 -0.23134 -0.23134 0.07010 0.07010 -0.01237 -0.01237 0.00981 0.00981
* * *
Table 31-bis: FOA Matrix for 7.1.4 Renderer Output Mode ('Setting 2')
* * *
0.140726 0.140726 0.083124 0.000000 0.107277 0.107277 0.183459 0.183459
0.113310 0.113310 0.114578 0.114578 0.177191 -0.177191 0.000000 0.000000
0.205945 -0.205945 0.218403 -0.218403 0.138153 -0.138153 0.127151 -0.127151
-0.105877 -0.105877 -0.070636 0.000000 -0.115945 -0.115945 -0.148905 -0.148905
0.195697 0.195697 0.198850 0.198850 0.228860 0.228860 0.163187 0.000000
0.013007 0.013007 -0.280216 -0.280216 0.116659 0.116659 -0.127825 -0.127825
* * *
# Annex D: Object Panner Data {#annex-d-object-panner-data .list-paragraph}
Elements not provided for a particular output mode are assumed to be empty.
Table 32: pannerData Arrays for 7.1.4 Renderer Output Mode ('Setting 1')
* * *
Zpan Npan Uchans Uangs Mchans Mangs 0 0 12 -225 8 -225 0 0 10 -135 6 -135 0 0
9 -45 2 -90 0 0 11 45 3 -45 0 0.612547 135 1 0 0 0.612547 225 5 45 0 0 7 90 0
0 135 0.375214 0 225 0.375214 0 0.375214 0 0.375214 0
* * *
Table 33-bis: pannerData Arrays for 7.1.4 Renderer Output Mode ('Setting 2')
* * *
Zpan Npan Uchans Uangs Mchans Mangs 0 0 12 -225 8 -225 0 0 10 -135 6 -135 0 0
9 -45 2 -90 0 0 11 45 3 -30 0 0.612547 135 1 0 0 0.612547 225 5 30 0 0 7 90 0
0 135 0.375214 0 225 0.375214 0 0.375214 0 0.375214 0
* * *
Table 34: Umap Matrix for 7.1.4 Renderer Output Mode
* * *
0 0 0 1 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 1 0 0 0
* * *
Table 35: Mmap Matrix for 7.1.4 Renderer Output Mode
* * *
0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0
* * *
Table 36: pannerData Arrays for 5.1.4 Renderer Output Mode
* * *
Zpan Npan Uchans Uangs Mchans Mangs 0 0.250998 10 -225 6 -250 0 0.250998 8
-135 2 -110 0 0 7 -45 3 -45 0 0 9 45 1 0 0 0.484068 135 5 45 0 0.484068 225
110 0.375214 0 250 0.375214 0 0.375214 0 0.375214 0
* * *
Table 37: Umap Matrix for 5.1.4 Renderer Output Mode
* * *
0 0 0 1 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 1 0 0 0
* * *
Table 38: Mmap Matrix for 5.1.4 Renderer Output Mode
* * *
0 0 0 0 1 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 1 0 0 0 0
* * *
Table 39: pannerData Arrays for 7.1 Renderer Output Mode
* * *
Zpan Npan Mchans Mangs 0 0 8 -225 0 0 6 -135 0 0 2 -90 0 0 3 -45 0.612547
0.612547 1 0 0.612547 0.612547 5 45 0 0 7 90 0 0 135 225
* * *
Table 40: Mmap Matrix for 7.1 Renderer Output Mode
* * *
0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0
* * *
Table 41: pannerData Arrays for 5.1 Renderer Output Mode
* * *
Zpan Npan Mchans Mangs 0.250998 0.250998 6 -250 0.250998 0.250998 2 -110 0 0 3
-45 0 0 1 0 0.484068 0.484068 5 45 0.484068 0.484068 110
* * *
Table 42: Mmap Matrix for 5.1 Renderer Output Mode
* * *
0 0 0 0 1 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0