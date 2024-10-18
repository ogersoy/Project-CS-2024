# Foreword
This Technical Report has been produced by the 3^rd^ Generation Partnership
Project (3GPP).
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
# Introduction
The concept of Precoded EGPRS2 -- PC EGPRS2 - DL has recently shown to provide
significant performance gains for EGPRS2. Gains are expected both in
interference and sensitivity limited scenarios, allowing significant increase
to both data capacity and spectral efficiency for EGPRS2.
Performing precoding of EGPRS2 modulated data is expected to increase
robustness of the system significantly while keeping the spectral properties
of the signal intact.
# 1 Scope
The present document contains the results from the 3GPP study item on Signal
Precoding Enhancements for EGPRS2 DL, SPEED.
The following is covered by the study:
  * Objectives for the study
  * Common assumptions to be used in the evaluation
  * Technical work and performance evaluations based on the objectives
# 2 References
The following documents contain provisions which, through reference in this
text, constitute provisions of the present document.
\- References are either specific (identified by date of publication, edition
number, version number, etc.) or non‑specific.
\- For a specific reference, subsequent revisions do not apply.
\- For a non-specific reference, the latest version applies. In the case of a
reference to a 3GPP document (including a GSM document), a non-specific
reference implicitly refers to the latest version of that document _in the
same Release as the present document_.
[1] 3GPP TR 21.905: \"Vocabulary for 3GPP Specifications\".
[2] GP-101088 "New SI proposal: Signal Precoding Enhancements for EGPRS2 DL",
source Telefon AB LM Ericsson, ST-Ericsson SA, Telecom Italia S.p.A, Vodafone
Group Plc, China Mobile Com. Corp. ZTE Corporation, Huawei Technologies Co.
Ltd.
[3] 3GPP TS45.003, v8.3.0 "Channel coding"
[4] 3GPP TS45.005, v9.3.0 "Radio transmission and reception"
# 3 Definitions, symbols and abbreviations
## 3.1 Definitions
For the purposes of the present document, the terms and definitions given in
TR 21.905 [1] and the following apply. A term defined in the present document
takes precedence over the definition of the same term, if any, in TR 21.905
[1].
## 3.2 Symbols
For the purposes of the present document, the following symbols apply:
\ \
## 3.3 Abbreviations
For the purposes of the present document, the abbreviations given in TR 21.905
[1] and the following apply. An abbreviation defined in the present document
takes precedence over the definition of the same abbreviation, if any, in TR
21.905 [1].)
BMD Blind Modulation Detection
CP Cyclic Prefix
DAS Downlink level A modulation and coding scheme
DBS Downlink level B modulation and coding scheme
DFT Discrete Fourier Transform
HSR Higher Symbol Rate
MCS Modulation and coding scheme
NSR Normal Symbol Rate
PAR Peak-to-Average Ratio
PC EGPRS2 Precoded EGPRS2
SPEED Signal Precoding Enhancements for EGPRS2 DL
TSC Training Sequence Code
USF Uplink State Flag
# 4 Objectives
## 4.1 Performance Objectives
### 4.1.1 Improved EGPRS2 throughput
The introduction of Precoded EGPRS2, PC EGPRS2, shall significantly improve
data throughput performance as compared to realistic EGPRS2 performance.
## 4.2 Compatibility Objectives
### 4.2.1 Spectral properties
PC EGPRS2 shall obey the current spectral requirements on spectrum due to
modulation and wideband noise and on switching transients of EGPRS2 DL[4].
### 4.2.2 Impact to legacy service
The impact of PC EGPRS2 on GSM speech codecs, GPRS, EGPRS and EGPRS2 shall be
kept at a minimum. Impact on cell reselection performance of mobile stations
should be avoided by operation of PC EGPRS2 on the BCCH carrier. Impacts from
PAN and USF multiplexing on PC-EGPRS2 and legacy user throughput should be
minimized.
### 4.2.3 Implementation impact to base stations
The introduction of Precoded EGPRS2 in the base station transmitter should
change BTS hardware as little as possible.
### 4.2.4 Implementation impact to mobile station
The introduction of Precoded EGPRS2 in the mobile station receiver should
change MS hardware as little as possible. Both impact to stand-alone PC-EGPRS2
platforms and combined EGPRS2 and PC-EGPRS2 platforms shall be considered.
# 5 Common assumptions for the evaluation
In the following sub-clauses common assumptions for the performance evaluation
are listed
## 5.1 Overall design principles
### 5.1.1 Precoder module
The Inverse Discrete Fourier Transform shall be used as precoder module.
### 5.1.2 Burst length
The length of the active part of the burst (including current tail symbols) of
EGPRS2 shall be kept for PC EGPRS2, i.e.
\- EGPRS2-A: 148 NSR symbols
\- EGPRS2-B: 177 HSR symbols
### 5.1.3 Cyclic prefix
One cyclic prefix length, defined in duration of microseconds, is required.
When applied on PCE2-A and PCE2-B this duration must be translated to CP
lengths defined by normal and higher symbol rate symbols respectively.
### 5.1.4 Positioning of training symbols
To enable easier detection of the precoded bursts only a single positioning
vector of training symbols onto the burst for the respective EGPRS2 level will
be applied, i.e. one for PC EGPRS2-A and one for PC EGPRS2-B.
### 5.1.5 Modulation and coding scheme
All channel coding definitions of EGPRS2 shall be kept intact with regards to
payload size, channel coding and interleaving, except for the highest MCS of
each set, i.e. DAS-12 and DBS-12 for EGPRS2-A and EGPRS2-B, where only the
payload size is required to be kept.
In the following subclauses the new re-defined MCSs are referred to as DAS-12b
and DBS-12b respectively.
#### 5.1.5.1 Modulation scheme
In addition to the modulation schemes defined in [4] for EGPRS2, BPSK and
64QAM can be used for the mapping of bits onto modulation symbols in the
burst.
The definition of the additional modulation schemes are shown in Figure 5.1.
{width="3.7944444444444443in" height="3.176388888888889in"}
{width="3.6770833333333335in" height="3.84375in"}
Figure 5.1 Modulation scheme definitions of BPSK and 64QAM.
#### 5.1.5.1 Channel coding
For the re-definition of channel coding of DAS-12/DBS-12 the definitions in
[1], sub-clause 5.1a.1.3 shall be used as baseline.
## 5.2 Link parameters
The following link level parameters are to be used as base line for the
evaluation. Additional simulations assumptions may be used when deemed
necessary.
Table 5.1 Link level simulation assumptions.
+-------------------------+-----------------------------------+ | Parameter | Value | +-------------------------+-----------------------------------+ | Link direction | Downlink | +-------------------------+-----------------------------------+ | Frequency band | 900MHz, 1900 MHz | +-------------------------+-----------------------------------+ | Interference modulation | GMSK, Precoded modulation schemes | +-------------------------+-----------------------------------+ | MCSs | DAS-5 - DAS-11, DAS-12b | | | | | | DBS-5 - DBS11, DBS-12b. | +-------------------------+-----------------------------------+ | Impairments | Typical TX and RX impairments. | +-------------------------+-----------------------------------+
_[Editor's note: It is discussed whether or not to use a common PA model for
the evaluation.of spectrum impact in the investigation on PAR reduction, see
6.4]_
Table 5.2 Link level simulation scenarios.
+-------------+--------------+--------------+--------------+-------+ | Propagation | Test | | | | | | Scenario | | | | | Conditions | | | | | +-------------+--------------+--------------+--------------+-------+ | | Sensitivity | Co. channel | Adj. channel | DTS-2 | | | Limited | interference | interference | | +-------------+--------------+--------------+--------------+-------+ | Static | X | | | | +-------------+--------------+--------------+--------------+-------+ | TU3noFH | | _X_ | X | | +-------------+--------------+--------------+--------------+-------+ | TU3iFH | | _X_ | _X_ | | +-------------+--------------+--------------+--------------+-------+ | TU50noFH | _X_ | _X_ | _X_ | X | +-------------+--------------+--------------+--------------+-------+ | HT100noFH | X | | | | +-------------+--------------+--------------+--------------+-------+ | RA250noFH | X | X | X | | +-------------+--------------+--------------+--------------+-------+
## 5.3 Evaluation output
When comparing EGPRS2 and PC EGPRS2 performance, as stated in subclause 7,
each of the assumptions and test scenarios proposed in section 5.2 shall be
considered. Ideal link adaptation throughput envelopes shall be used as
baseline in the evaluation.
When evaluating the items of subclause 6, a subset of the listed assumptions
in subclause 5.2, deemed as sufficient for the given evaluation, shall be
used.
To enable comparison of simulations provided by different companies and/or
between different proposals, details on receiver assumptions relevant to both
complexity and performance shall be provided together with simulated results.
Such details should at minimum include RX-filter bandwidth and TX and RX
impairments used.
Absolute performance figures are to be provided when comparing PC EGPRS2 and
EGPRS2 performance.
[Editor's note: Further assumptions can be added.]
# 6 Design and Evaluation
## 6.1 DAS-12b/DBS-12b
A re-definition of DAS-12 and DBS-12, DAS-12b for EGPRS2-A and DBS-12b for
EGPRS2-B respectively is foreseen in order to optimize performance. The
payload size of each MCS, i.e. 3x82 bytes and 4x74 bytes for DAS-12 and DBS-12
respectively are to be kept.
This sub-clause evaluates modifications in the MCS design and its impact on
performance.
### 6.1.1 Burst formatting of DAS-12b and DBS-12b
#### 6.1.1.1 Burst formatting for Single Block PCE2
##### 6.1.1.1.1 Introduction
This sub-clause proposes a new burst formatting design for DAS-12b and DBS-12b
for Single Block PCE2 in terms of
  * Mapping of bits onto modulation symbols and
  * Burst mapping of Header and Data fields.
For the mapping of bits onto modulation symbols the objective is to find the
best mixed mode modulation combination for DAS-12b and DBS-12b in terms of
optimal throughput performance.
**For the** burst mapping of Header and Data fields the objective is to derive
  * header bit swapping, which swaps header bits at weak positions with > data bits at strong positions and
  * burst bit shifting, which circularly shifts each half burst so that > part of, or all header bits end up at higher SNR **region,**
to achieve robust header and incremental redundancy performance.
##### 6.1.1,1.2 Evaluation Method
Several best MMM candidates are first derived, in terms of providing as robust
performance as possible at lower SNR region, which will later lead to robust
data performance when header bit swapping and shifting is used. This
evaluation is done by placing all header/USF/SF bits at high SNR region, and
focusing therefore on the data BLER performance.
The header bit swapping and shifting are then evaluated together with the best
MMM candidates. The best burst formatting for DAS-12b and DBS-12b is then
selected as the one that keeps the relative performance between header and
data BLER (using non-precoded DAS-12 (data BLER\@50% to avoid error floor and
headerBLER\@1%) and DBS-11(data BLER\@10% and headerBLER\@1%) as reference),
meanwhile achieves as low data BLER as possible.
For more information please refer to [6.1-2].
##### 6.1.1.1.3 Simulation Assumptions and Results
###### 6.1.1.1.3.1 Simulation Assumptions
The selection of the optimal burst formatting, including MMM, header bit
swapping and shifting is based on performance simulated in a sensitivity
limited scenario given a TU50nFH propagation environment. The data and header
BLER are then verified in other propagation models and interference scenarios.
A detailed list of simulation assumptions are presented in table 6.1-1.
Table 6.1-1 Simulation assumptions
+------------------------+-------------------------------------+ | Parameter | Value | +------------------------+-------------------------------------+ | MCSs | DAS-12b, | | | | | | DBS-12b | +------------------------+-------------------------------------+ | TSC placement | According to [6.1-3] | +------------------------+-------------------------------------+ | Burst length | According to [6.1-4] | +------------------------+-------------------------------------+ | CP length | PCE2A: 6 | | | | | | PCE2B: 9 | +------------------------+-------------------------------------+ | RX BW | PCE2A: 240kHz | | | | | | PCE2B: 275kHz | +------------------------+-------------------------------------+ | ICI Suppression | No | +------------------------+-------------------------------------+ | Backoff | No | +------------------------+-------------------------------------+ | Channel propagation | TU50nFH, HT100nFH | +------------------------+-------------------------------------+ | Interference | AWGN, CO, DTS-2 modified | +------------------------+-------------------------------------+ | Frequency band | 900 MHz | +------------------------+-------------------------------------+ | Frames | 5000 | +------------------------+-------------------------------------+ | Tx/Rx impairments | Ericsson typical TX/RX impairments: | | | | | - Phase noise | 0.8 / 1.2 [degrees (RMS)] | | | | | - I/Q gain imbalance | 0.1 / 0.2 [dB] | | | | | - I/Q phase imbalance | 0.2 / 2.0 [degrees] | | | | | - DC offset | -45 / -40 [dBc] | | | | | - Frequency error | - / 25 [Hz] | +------------------------+-------------------------------------+
###### 6.1.1.1.3.2 Simulation Results
Evaluation according to 6.1.1.2 shows that the best burst formatting is:
  * For DAS-12b: MMM pattern containing 56 64QAM symbols, one 32QAM and > one 8PSK symbol, with header bit swapping and a right shift of 50 > bits;
  * for DBS-12b: no MMM, with header bit swapping and no shifting.
Simulation results are listed in table 6.1.1-2 and table 6.1.1-3.
Table 6.1-2: Absolute Performance with/without optimal burst format.
+-------+-------+-------+-------+-------+-------+-------+-------+ | | ** ** | * | | | | | | | | | _Data | | | | | | | | | BLER | | | | | | | | | @ | | | | | | | | | 10%__| | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+ | ** | ** |__No | * | * | | | | | MCS_ _| Intf. | b |_ With | _With | | | | | | Sc | itswa | b | b | | | | | | en.__| p/shi | itswa | itswa | | | | | | | fting | p(and | p(and | | | | | | | &__| shift | shif | | | | | | | | ing), | ting) | | | | | | |__no | no | & Opt | | | | | | | MMM_ _| MMM_ _| MMM_ _| | | | +-------+-------+-------+-------+-------+-------+-------+-------+ | | | * | ** | * | ** | * | ** | | | |_ TU50 | HT100 | _TU50 | HT100 |_ Tu50 | HT100 | | | | nFH**| nFH** | nFH**| nFH** | nFH**| nFH** | +-------+-------+-------+-------+-------+-------+-------+-------+ | | CO | 26,5 | 2 | 26,9 | 2 | 26,4 | 2 | | | | | 7,3* | | 9,5* | | 7,5* | +-------+-------+-------+-------+-------+-------+-------+-------+ | DA | DTS-2 | 28,1 | 2 | 28,9 | 3 | 28,2 | 2 | | S-12b | | | 8,8* | | 1,5* | | 9,5* | +-------+-------+-------+-------+-------+-------+-------+-------+ | | AWGN | 27,7 | 2 | 28,8 | 3 | 27,9 | 2 | | | | | 8,7* | | 1,6* | | 9,3* | +-------+-------+-------+-------+-------+-------+-------+-------+ | | CO | 26,6 | | 27,1 | | 27,1 | | +-------+-------+-------+-------+-------+-------+-------+-------+ | DB | DTS-2 | 30,0 | | 31,2 | | 31,2 | | | S-12b | | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+ | | AWGN | 28,4 | | 30,0 | | 30,0 | | +-------+-------+-------+-------+-------+-------+-------+-------+
*Data bler\@30% for HT100nFH;
+-------+-------+-------+-------+-------+-------+-------+-------+ | | | H | | | | | | | | | eader | | | | | | | | | BLER | | | | | | | | | @ 1% | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+ | ** | **In |** No | * | * | | | | | MCS**| tf.** | b | _With |_ With | | | | | | | itswa | bi | b | | | | | | **Sc | p/shi | tswap | itswa | | | | | | en.** | fting | and**| p(and | | | | | | | &** | | shi | | | | | | | | * | fting | | | | | | | **no | *Shif | & Opt | | | | | | | MMM** | ting, | MMM**| | | | | | | | no | | | | | | | | | MMM** | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+ | | | * | ** | * | ** | * | ** | | | | _TU50 | HT100 |_ TU50 | HT100 | _Tu50 | HT100 | | | | nFH_ _| nFH_ _| nFH_ _| nFH_ _| nFH_ _| nFH_ * | +-------+-------+-------+-------+-------+-------+-------+-------+ | | CO | 17,4 | 21 | 13,3 | 13,0 | 13,1 | 12,8 | +-------+-------+-------+-------+-------+-------+-------+-------+ | DA | DTS-2 | 24,7 | 27,4 | 15,0 | 14 | 15,2 | 14 | | S-12b | | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+ | | AWGN | 26,5 | 28,3 | 12,4 | 12,0 | 12,5 | 11,8 | +-------+-------+-------+-------+-------+-------+-------+-------+ | | CO | 18,5 | | 14,6 | | 14,6 | | +-------+-------+-------+-------+-------+-------+-------+-------+ | DB | DTS-2 | 31,9 | | 17,4 | | 17,4 | | | S-12b | | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+ | | AWGN | 31,2 | | 14,3 | | 14,3 | | +-------+-------+-------+-------+-------+-------+-------+-------+
Table 6.1-3: Relative performance using optimal burst formatting, comparing
with DAS-12b/DBS-12b no bitswap & no MMM.
+---------+----------+----------+----------+---------+----------+ | | | Data | Header | | | | | | improvem | improvem | | | | | | ents(dB) | ents(dB) | | | +---------+----------+----------+----------+---------+----------+ | MCS | Intf. | With | With | | | | | Scen. | bit | bit | | | | | | swap(and | swap(and | | | | | | s | s | | | | | | hifting) | hifting) | | | | | | & | & | | | | | | | | | | | | | Opt MMM | Opt MMM | | | +---------+----------+----------+----------+---------+----------+ | | | TU50nFH | HT100nFH | TU50nFH | HT100nFH | +---------+----------+----------+----------+---------+----------+ | DAS-12b | CO | 0,1 | -0,2 | 4,3 | 8,2 | +---------+----------+----------+----------+---------+----------+ | | DTS-2 | -0,1 | -0,7 | 9,5 | 13,4 | +---------+----------+----------+----------+---------+----------+ | | AWGN | -0,2 | -0,6 | 14,0 | 16,5 | +---------+----------+----------+----------+---------+----------+ | DBS-12B | CO | -0,5 | | 3,9 | | +---------+----------+----------+----------+---------+----------+ | | DTS-2 | -1,2 | | 14,5 | | +---------+----------+----------+----------+---------+----------+ | | AWGN | -1,6 | | 16,9 | | +---------+----------+----------+----------+---------+----------+
It can be seen that the use of header bit swap and burst shift significantly
improves the header performance of DAS-12b and DBS-12b, up to 17dB, meanwhile,
the data performance has degraded moderately, in almost all the simulated
scenarios. It should also be noticed that, for DAS-12b, the use of MMM
decreases the degradation in data performance due to header bit swapping and
shifting.
### 6.1.2 References
[6.1-1] GP-100918, "_Precoded EGPRS2 Downlink"_ , source Telefon AB LM
Ericsson, ST-Ericsson SA. GERAN#46.
[6.1-2] GP-101852, "DAS-12b and DBS-12b Burst Formatting", source Telefon AB
LM Ericsson, ST-Ericsson SA, GERAN#48.
[6.1-3] GP-101350, "Training symbol placements in Precoded EGPRS2 DL", source
Telefon AB LM Ericsson, ST-Ericsson. GERAN#47,
[6.1-4] GP-101349, "Aspects of burst formatting of Precoded EGPRS2 DL", source
Telefon AB LM Ericsson, ST-Ericsson SA. GERAN#47,
## 6.2 Burst format
### 6.2.1 DFT length
The length of the Discrete Fourier Transform - DFT -- has a direct relation to
the computational complexity and also the sub-carrier spacing, which will have
impact on performance.
This sub-clause evaluates different DFT sizes, both in terms of computational
complexity and performance.
#### 6.2.1.1 Choice of DFT lengths for Single Block PCE2
At the normal symbol rate, a reasonable choice of $N$, the DFT size, is $N =
\text{142} = \text{116} + \text{26} = 2 \times \text{71}$, since this length
yields the same payload and training symbols as EGPRS/EGPRS2-A. Unfortunately
$N$ is not a highly composite number since 71 is a prime number. The choice $N
= \text{144} = 2 \times 2 \times 2 \times 2 \times 3 \times 3$is proposed
since FFT's of size 144 are typically 3 to 10 times faster than FFT's of size
142, depending on implementation details and hardware capabilities. This also
gives two extra symbols that can be used for training or other purposes.
Although the sub-carrier spacing for $N = \text{144}$ is a little smaller than
for $N = \text{142}$, the difference in performance between the two FFT
lengths is negligible.
At the higher symbol rate, a reasonable choice of $N$ is$N = \text{169} =
\text{138} + \text{31} = \text{13} \times \text{13}$, which gives the same
payload and training symbols as EGPRS2-B. A more convenient value from the
computational point of view is$N = \text{168} = 2 \times 2 \times 2 \times 3
\times 7$. This last value is obtained by the elimination of one training
symbol. Although the sub-carrier spacing for $N = \text{168}$ is a little
larger than for$N = \text{169}$, and even though one training symbol is
removed, the difference in performance between the two DFT lengths is
negligible. Table 6.2-1 summarizes the lengths of the DFT.
Table 6.2-1 DFT length for PCE2
* * *
Symbol rate DFT Length Normal 144 Higher 168
* * *
##### 6.2.1.1.1 Performance Evaluation of DFT lengths
Figures 6.2-1 and 6.2-2 show that a DFT of size 144 for normal symbol rate and
168 for higher symbol rate can be adopted without link performance losses with
respect to the sizes 142 and 169 respectively.
Simulation assumptions include TX and RX impairments from [6.2-1] TSC
positioning based on [6.2-3] and using an RX bandwidth of 240 kHz and 275 kHz
for PCE2-A and PCE2-B respectively.
{width="4.909027777777778in" height="3.6770833333333335in"}
Figure 6.2-1 Performance of PC EGPRS2-A with different DFT lengths
{width="5.085416666666666in" height="3.5194444444444444in"}
Figure 6.2-2 Performance of PC EGPRS2-B with different DFT lengths.
#### 6.2.1.2 DFT length for Padded HOM
##### 6.2.1.2.1 Principle of DFT length choices
For the normal case, the DFT size is determined primarily by the number of
user data symbols, the number of training symbols and some special symbols
(such as padding symbols at the edge of the signal BW). Considering the
efficient of DFT algorithm and the impact on other parts, the final DFT length
should be carefully designed.
At the normal symbol rate, a common choice of N, the DFT size, is N = 142 =
116+26=2*71. Unfortunately N is not a highly composite number since 71 is a
prime number, which will result in high algorithm complexity both in BTS and
MS. So is the N=169=138+31=13*13 at the higher symbol rate.
A good way to achieve highly efficient DFT is to find a number which is highly
composite number with the small prime numbers, such as 2,3,5,7. At the same
time, the change of the DFT size would have little impact on the functionality
of other parts of burst and the performance. The DFT sizes, N = 140 = 2*2*5*7
and N = 144 =2*2*2*2*3*3 are both candidates at the normal symbol rate.
Compared to DFT size N = 142 the increased DFT size N = 144 will result in
even narrower sub-carrier bandwidth which may bring some frequency offset
sensitivity issues. Since the total duration of the burst is kept intact and
it is determined by the guard period, data symbols, CP, training symbols and
other special symbols (if exists), if keeping the guard period, the CP length
will be shortened because of the increased DFT size. It is not expected
especially for the large delay spread channel. At the higher symbol rate, the
DFT size N=168=2*2*2*3*7 is an appropriate highly composite number close to
169.
According to above considerations, a reasonable choice of DFT size N
=140=2*2*5*7 is recommended for NSR and N =168=2*2*2*3*7 for HSR, shown in
Table 6.2-2. This DFT size can be easily obtained by removing 2(for NSR) or
1(for HSR) padding symbols in Padded HOM (reference to the section 6.2.5.2).
Table 6.2-2 DFT sizes for PCE2
* * *
Symbol rate DFT size NSR 140 HSR 168
* * *
##### 6.2.1.2.2 Performance evaluations for the DFT length
Figure 6.2-3 shows that the DFT size of 140 (for NSR) and 168 for HSR can be
adopted without link performance losses compared to the DFT sizes 142 and 169
respectively. The simulation assumptions are depicted in Table 6.2.1.2-4.
{width="3.9972222222222222in" height="3.0909722222222222in"}
Figure 6.2-3 Sensitivity performance with different DFT sizes
6.2.2 CP length
A cyclic prefix is needed to mitigate the impact from channel time dispersion,
on PC EGPRS2 performance.
This sub-clause evaluates different CP lengths.
#### 6.2.2.1 Choice of CP length for Single Block PCE2
The CP introduces overhead, but also helps reduce the complexity of the
demodulator. In order to keep both the duration of the PCE2 time slot, the
length of the DFT as in 6.2.1.1 and maintain the guard period as in EGPRS2,
the following values are proposed.
Table 6.2-3 CP length for PCE.
* * *
Symbol rate CP duration [μs] Normal 6*48/13 Higher 9*40/13
* * *
The proposed duration of the CP covers the time dispersion due to the Tx/Rx
filters, as well as the time dispersion found in the most common propagation
environments (except for Hilly Terrain).
#### 6.2.2.2 Choice of CP length for Padded HOM
In order to keep the duration of the burst intact and maintain the guard
period, the CP length will be increased from 6 symbols to 8 symbols when the
DFT size is decreased from 142 to 140, as described in section 6.2.1.2.1. The
CP length defined in duration of microseconds, given in Table 6.2-4, is very
close for NSR and HSR (with only a difference of 1.8us).
Table 6.2-4 CP length for PCE2
* * *
Symbol rate CP length [μs] NSR 8*3.69=29.52 HSR 9*3.08=27.72
* * *
### 6.2.3 TSC symbol position
This sub-clause evaluates different positioning of the training symbols for
improved performance.
#### 6.2.3.1 TSC symbol position for Single Block PCE2
In Precoded EGPRS2 [6.2-1], the channel estimate is performed based on the
training symbols, which are spread over the transmitted burst. To achieve good
quality of the channel estimate and increased throughput, the placement of the
training symbols should be carefully designed.
In the following sub-clauses two design criteria are presented and evaluated
to find best the placement of the training symbols,
##### 6.2.3.1.1 Minimum Mean Square Error (MMSE) criterion
Under the MMSE criterion, a good training symbol placement
$\text{tsc}_{\text{ind}_{\text{opt}}}$is the one that minimizes the mean
square error of the channel estimate:
$\text{tsc}_{\text{ind}_{\text{opt}}}\ = \ \text{argmin}\left{ E(\sum_{i =
1}^{N}{\left\| \lambda_{i} - {\hat{\lambda}}_{i} \right\|^{2})} \middle|
\middle| \text{tsc}_{\text{ind}} \right}$
where ${\hat{\lambda}}_{i}$is the channel frequency response estimate for the
$i$-th symbol.
Given Additive White Gaussian Noise (AWGN) and flat fading channel, the
optimal training symbol placement based on MMSE criterion are those that are
equally spaced. The training symbol indices can be calculated by:
$\text{tsc}_{\text{ind}_{\text{uniform}}}(\text{sp}) = \text{sp} +
\left\lfloor \frac{L}{\text{Ntr}}\left\lbrack 0:1:\text{Ntr} - 1 \right\rbrack
\right\rfloor$,
with L the DFT size, $\text{Ntr}$ the training sequence length,
and$\text{sp}$the index of the first training symbol.
##### 6.2.3.1.2 Balance Signal-to-Noise Ratio (SNR) criterion
Due to the low-pass characteristic of a GSM/EDGE channel, the instantaneous
SNR for symbols transmitted at the edge of the frequency band in a PCE2 burst
will always be lower than that for those transmitted in the middle of the
frequency band. By placing training symbols at different positions, the
instantaneous SNR can be adjusted.
Consider the signal tap model for PCE2:
$Y_{i} = {\hat{\lambda}}_{i}S_{i} +
\underset{\text{Noise}'_{i}}{\overset{(\lambda_{i} - {\hat{\lambda}}_{i})S_{i}
+ N_{i}}{\underbrace{}}},\ i = 1,\text{.}\text{.}\text{.},N$,
where the noise term consists of both the noise (and interference) _N~i~_ ,
and the channel estimation error${\hat{\lambda}}_{i}$. Expectation of the
instantaneous SNR is calculated as:
with $\text{MSE}(\lambda_{i})$contributing to the SNR calculation. By
modifying the training symbol placement, and hence the MSE, the instantaneous
SNR over the burst can be adjusted towards a more balanced form. Please refer
to [6.2-3] for illustration of the SNR balancing effect.
To make the design feasible, the following constraints are used:
  * The training symbols are placed symmetrically over the part > consisting of payload and training symbols;
  * In the center of the burst, the training symbols are consecutively > placed to achieve a lower MSE in this part (the weak taps), thus > increase the SNR for this part;
  * In other parts of the burst, the training symbols are evenly placed.
A simplified implementation of training symbol placement, denoting as
$\text{tsc}_{\text{ind}}(\text{sp},\text{cn})$is calculated as follows. The
Matlab operators ":" and $\text{fliplr}$will be used.
$\text{tsc}_{\text{ind}_{\text{left}_{\text{concentrated}}}}(\text{sp},\text{cn})
= \left\lbrack \frac{L}{2} - \frac{\text{cn}}{2} + 1:1:\frac{L}{2}
\right\rbrack$ ;
$\text{tsc}_{\text{ind}_{\text{left}_{\text{uniform}}}}(\text{sp},\text{cn}) =
\left\lfloor \text{sp} + \frac{\frac{L}{2} - \frac{\text{cn}}{2} - \text{sp} +
2}{(\text{Ntr} - \text{cn}\frac{)}{2}}\left\lbrack 0:1:(\text{Ntr} -
\text{cn}\frac{)}{2} - 1: \right\rbrack \right\rfloor$;
$\text{tsc}_{\text{ind}_{\text{left}}}(\text{sp},\text{cn}) = \left\lbrack
\text{tsc}_{\text{ind}_{\text{left}_{\text{uniform}}}}\
\text{tsc}_{\text{ind}_{\text{left}_{\text{concentrated}}}} \right\rbrack$;
$\text{tsc}_{\text{ind}}(\text{sp},\text{cn}) = \left\lbrack
\text{tsc}_{\text{ind}_{\text{left}}}\ \text{tsc}_{\text{ind}_{\text{right}}}
\right\rbrack$.
with $\text{sp}$denotes the index of the first training symbol, and
$\text{cn}$the number of training symbols concentrated in the middle of the
burst.
Figure 6.2-4 illustrates the concentrated training symbol placement according
to the above procedure.
Figure 6.2-4: Burst with training symbols intercalated.
##### 6.2.3.1.3 Evaluation of training symbol placement
In this section, performances with different training symbol placements based
on design criteria in 6.2.3.1 are evaluated. The design parameters are tuned
and a recommendation of the training symbol placement is made.
##### 6.2.3.1.3.1 Simulation Assumptions
A detailed list of simulation assumptions are presented in table 6.2-5.
Table 6.2-5. Simulation assumptions.
+------------------------+-------------------------------------+ | Parameter | Value | +------------------------+-------------------------------------+ | MCSs | DAS5-DAS11, and DAS-12b, | | | | | | DBS7-DBS11, and DBS-12b | +------------------------+-------------------------------------+ | Burst length | According to [6.2-4] | +------------------------+-------------------------------------+ | CP length | PCE2A: 6 | | | | | | PCE2B: 9 | +------------------------+-------------------------------------+ | RX BW | PCE2A: 240kHz | | | | | | PCE2B: 275kHz | +------------------------+-------------------------------------+ | Channel propagation | TU50nFH, TU3iFH, Static | +------------------------+-------------------------------------+ | Interference | AWGN, CO, DTS-2 | +------------------------+-------------------------------------+ | Frequency band | 900 MHz | +------------------------+-------------------------------------+ | Frames | 5000 | +------------------------+-------------------------------------+ | Impairments | Ericsson typical TX/RX impairments: | | | | | - Phase noise | 0.8 / 1.0 [degrees (RMS)] | | | | | - I/Q gain imbalance | 0.1 / 0.2 [dB] | | | | | - I/Q phase imbalance | 0.2 / 1.5 [degrees] | | | | | - DC offset | -45 / -40 [dBc] | | | | | - Frequency error | - / 25 [Hz] | +------------------------+-------------------------------------+
The training symbol placements evaluated are the uniform placement based on
MMSE criterion, $\text{tsc}_{\text{ind}_{\text{uniform}}}(4),$ and the
concentrated placements based on balancing SNR criterion,
$\text{tsc}_{\text{ind}}(\text{sp},\ \text{cn}),$ with$\ \text{sp} =
\left\lbrack 1,\cdots,7 \right\rbrack,\text{cn} = 2 \ast \left\lbrack
1,\cdots,\text{10} \right\rbrack$.
The data BLER is used as an indication for the overall impact.
##### 6.2.3.1.3.2 Simulation Results and conclusions
The evaluation process involves:
  * Tuning the concentrated training symbol placement, including the > first training symbol, $\text{sp}$, and the number of concentrated > training symbols, $\text{cn}$in > $\text{tsc}_{\text{ind}}(\text{sp},\ \text{cn}),$in both > sensitivity and interference limited scenarios (single > interference and multiple interferences);
  * Performance comparison with uniform placement and concentrated > placement, in both sensitivity and interference limited scenarios.
An example of performance comparison between uniform and concentrated TSC
placement can be seen in Figure 6.2-5.
{width="5.497222222222222in" height="4.269444444444445in"}
Figure 6.2-5. Performance of different training symbol placements in
sensitivity.
It can be seen that the concentrated placement generally outperforms the
uniform placement, which results from a balanced SNR. In TU channel, the gain
with concentrated placement can be over 1dB for SNR below 24 dB, and in static
channel, an overall improvement up to 2dB is achieved. It can also be noticed
that, in static channel, the gain increases as more training symbols are
concentrated, which is well aligned with the theoretical analysis of a more
balanced SNR.
Please refer to [6.2-3] for a detailed information about the evaluation and
simulation results.
The following conclusions are reached based on the evaluation:
  * Both the MMSE criterion and the balancing SNR criterion can be used > to reach a reasonable design of the training symbol placement;
  * The effectiveness of the balancing SNR criterion is limited by > non-AWGN noise, unknown and fading channel, and constraints made > for design simplicity;
  * For sensitivity, the concentrated placement outperforms the uniform > placement (especially at low SNR region). The gain is up to 1dB in > TU channel and up to 2dB in a Static channel.
  * In single interference case, concentrated placement is outperformed > by the uniform placement. The degradation is up to 1.5dB. The gap > steadily closes as $\text{cn}$increases;
  * In multi-interference case, the concentrated placements generally > outperform the uniform placement. At high C/I region, the uniform > placement outperforms concentrated placements with a lower > $\text{cn}$;
  * The placement of the first training symbol, $\text{sp}$, does not > affect the performance much in both sensitivity and interference > limited scenario. The differences are within 0.2dB for the > simulated scenarios.
It is therefore recommend to use a concentrated training symbol placement,
with moderate amount of concentrated training symbols, to have non-negligible
gain in sensitivity and multi-interference scenario, while only a small
degradation in single interference case. For PCE2A,
$\text{tsc}_{\text{ind}}(7,\text{10})$is recommended; for PCE2B,
$\text{tsc}_{\text{ind}}(8\ ,8)$is recommended.
#### 6.2.3.2 TSC symbol position for Padded HOM
##### 6.2.3.2.1 Principle of TS symbol position generation
Since the padding symbols are already used to balance the SNR in Padded HOM, a
kind of uniform placement of TS symbols are investigated in this section. In
order to simplify the description, the burst format shown in this section is
given in the format before the Symbol swapping. As illustrated in [6.2-5],
symbols before the IDFT are swapped to ensure the performance of USF and
Header which are located in the middle of the burst. That means, in the burst
format shown here the symbols which are located in the middle of the burst are
mapped to the centre of the signal Bandwidth (BW) and the symbols at the both
ends of the burst are mapped to the edge of the signal BW.
The exemplary uniformly placed TS symbol position could be achieved as
follows:
  * Two TS symbols are assigned to each end of the burst;
  * Other TS symbols are evenly placed in the whole burst.
{width="5.379166666666666in" height="0.46875in"}
Figure 6.2-6 TS symbol position
For example, as shown in Figure 6.2-6, when the DFT size N=142, two TS symbols
are allocated at the symbol index 0 and 141. Other TS symbols are evenly
placed in the whole burst according to the TS length. A simple way to
implement this can be elaborated below.
The interval of every two TS symbols could be roughly calculated by:
  * TS_interval = round((N-2)/(NTS-1)), where N is the DFT size and NTS > is the TS length.
Hence, the training symbol indices TS_ind are usually calculated by:
  * TS_ind(1) = 0;
  * TS_ind(NTS)=N-1;
  * TS_ind(k) = TS_ind(k-1)+ TS_interval, for k=2,3,...,NTS-1.
A small adjustment is needed with some exception when TS symbol position index
exceeds the bound of the DFT size.
With respect to the TS length, it should also be taken into account for PCE2.
As we know, the TS symbols are mainly used to estimate the channel property.
The wireless channels change both in time and frequency. The frequency
coherence shows how quickly it changes in frequency. Coherence bandwidth is
the parameter which expresses the frequency coherence. It gives the range of
frequencies over which the channel can be considered \"flat\". Considering the
new characteristics of PCE2, the TS length in EGPRS2 may not be suitable for
PCE2. Within the coherence bandwidth, optimized TS length can give some extra
symbols for other use, such as more padding symbols at the edge of the signal
BW which can bring some performance improvement with little loss on channel
estimation.
Table 6.2-6 shows the resulting TS position index with different TS lengths
according to the principle described above.
Table 6.2-6 TS symbol position index
* * *
level A N=142 TS13 [0:12:132,141] TS17 [0:9:135,141] TS21 [0:7:133,141] TS26
[0,3,6:6:138,141] level B N=169 TS13 [0:14:154,168] TS18 [0:10:160,168] TS25
[0:7:161,168] TS31 [0,3,6:6:165,168]
* * *
##### 6.2.3.2.2 Performance evaluations
Some performance evaluations have been carried out on TS symbol position with
different TS lengths. The simulation assumptions are shown in Table 6.2-7. All
the evaluations in this section are performed in Zero-padded pattern. The
pattern description is in section 6.2.5.2.2.
Table 6.2-7 simulation assumptions
+-------------------------+--------------------------+ | Parameter | Value | +-------------------------+--------------------------+ | Coding Schemes | DAS5,DAS11,DAS12; | | | | | | DBS5, DBS11,DBS12 | +-------------------------+--------------------------+ | Channel propagation | TU3iFH | +-------------------------+--------------------------+ | Frequency band | 900 MHz | +-------------------------+--------------------------+ | Noise/Interference | Sensitivity/CCI, ACI | +-------------------------+--------------------------+ | Interference modulation | GMSK | +-------------------------+--------------------------+ | Tx filter | Lin GMSK | +-------------------------+--------------------------+ | Rx filter | Level A: 270 kHz; | | | | | | Level B: 325 kHz | +-------------------------+--------------------------+ | ICI equalizer | No | +-------------------------+--------------------------+ | Frames | 5000 | +-------------------------+--------------------------+ | Tx /Rx impairments | No | +-------------------------+--------------------------+ | TS position index | According to Table 6.2-6 | +-------------------------+--------------------------+ | Cyclic prefix length | level A: 6\ | | | level B: 8 | +-------------------------+--------------------------+
Table 6.2-8 Absolute performance for Data\@10% BLER with different TS lengths
* * *
Coding schemes Sensitivity (dB) CCI (dB) ACI (dB)  
TS 17 TS 26 TS 17 TS 26 TS 17 TS 26 DAS-5 9.5 9.5 10 9.7 -6.3 -5.5 DAS-11 25.3
25.6 26.1 26 13.5 14.7 DAS-12 39.6 40  
Coding schemes Sensitivity (dB) CCI (dB) ACI (dB)  
TS 18 TS 31 TS 18 TS 31 TS 18 TS 31 DBS-5 10.6 10.4 11.8 11.2 -2.3 -1.1 DSB-11
37.5 37 32 32 26 29 DBS-12 42.2 /
* * *
Table 6.2-9 Performance improvements for Data\@10% BLER with different TS
lengths
* * *
Coding scheme Sensitivity (dB) CCI (dB) ACI (dB) TS 17 TS 17 TS 17 DAS-5 0
-0.3 0.8 DAS-11 0.3 -0.1 1.2 DAS-12 0.4  
Coding scheme Sensitivity (dB) CCI (dB) ACI (dB) TS 18 TS 18 TS 18 DBS-5 -0.2
-0.6 1.2 DBS-11 -0.5 0 3 DBS-12
* * *
In these evaluations, the TS symbols with shorter length are simply
intercepted from the legacy TS symbols. The detailed figures can be found in
[6.2-6].The absolute performance and the relative performance for PCE2-A and
PCE2-B with different TS lengths are given in Table 6.2-8 and Table 6.2-9 .The
gray cell means no simulation has been done in that scenario. The sign "∕"
means 10% BLER cannot be reached in that case. The positive value in Table
6.2-9 refers to the performance gain with the shorter TS length compared to
the legacy TS length while the negative value means the loss.
It can be seen that the performance of shorter TS length has little impact on
the performance in sensitivity and CCI scenario and has about 1 dB gain for
DAS-5, DAS-11 and DBS-5 and up to 3 dB gains for DBS-11 in ACI scenario.
#### 6.2.4 Mapping of block fields
The optimal position of Data, Header, USF and SF fields in EGPRS2 and PC
EGPRS2 is not necessary identical.
This sub-clause evaluates different placements of the burst fields to i)
Ensure similar performance as EGPRS2 USF reception and ii) Ensure incremental
redundancy performance of Precoded EGPRS2.
#### 6.2.4.1 Header bit swap and burst shift of Single Block PCE2
##### 6.2.4.1.1 Introduction
In an EGPRS2 radio block there are different information fields that need to
be mapped on the information symbols of the bursts: Data, Header, USF, SF (and
optionally PAN). The mapping of these information fields are done in a
specific manner to guarantee both absolute and relative performance targets.
In Precoded EGPRS2 (PCE2) the characteristics of the burst is changed and thus
the mapping of these information fields need to be optimized.
This sub-clause presents results from an investigation performed in [6.2-7] on
the use of header bit swap and burst shift for PCE2 Header field to guarantee
robust incremental redundancy performance.
##### 6.2.4.1.2 PCE2 Burst characteristics
In EGPRS2 the training sequence code (TSC), is placed in the middle of the
burst. In general it can be assumed that the further away a data symbol is
from the TSC the weaker the performance gets. In PCE2 the TSC symbols need to
be spread out over the burst to optimize the channel estimation, see [6.2-3].
Further, the quality is no longer as dependent on the distance from the TSC
symbol but rather characterized by the spectral properties of the TX pulse.
Figure 6.2-10 Burst characteristics of a Precoded 16QAM EGPRS2 burst.
##### 6.2.4.1.3 Burst shift and Bit swapper
The MCS used, and the channel coding definitions needed to decode the data
block is signaled in the header. Thus, the header needs to be correctly
decoded for the data block to be correctly decoded. Further, if incremental
redundancy is used the operative range of the MCS will be wider but still the
condition of header decoding is valid.
To enhance header performance and secure a Header BLER performance relative to
the data BLER a burst shift can in combination with a bit swap be used on weak
header bits. The shift of the bits in the burst is done in a cyclic manner for
each half burst as shown in Figure 6.2-11.
Figure 6.2-11 Burst mapping 16QAM, EGPRS2-A with (bottom) and without (top) a
circular shift of 20 bits.
The bit swapper will swap weak header bits to strong bit positions occupied by
data. This is illustrated in Figure 6.2-12.
Figure 6.2-12. Burst mapping 16QAM, EGPRS2-A with 20 bits circular shift and
with (bottom) and without (top) header bit swap.
In order to evaluate the relative performance needed between the Data and
Header BLER the relative performance of EGPRS2 Data and Header BLER has been
used as a reference. Since the channel coding definitions are kept intact for
PCE2 it is reasonable to assume that similar relative performance figures
should be kept.
##### 6.2.4.1.4 Simulation assumptions and Results
Table 6.2-10 summarizes the simulation assumptions used when deriving burst
shift and bit swap required to maintain the relative performance of EGPRS2
Header and Data BLER in PCE2.
Table 6.2-10. Simulation assumptions.
+-------------------------+------------------------+ | Parameter | Value | +-------------------------+------------------------+ | MCS | DAS-5-12, DBS-5-12 | +-------------------------+------------------------+ | Intf/Sens. | N0 | +-------------------------+------------------------+ | Impairments | [6.2-8] | +-------------------------+------------------------+ | Frames | 5000 | +-------------------------+------------------------+ | Max transmission for IR | 5 | +-------------------------+------------------------+ | Channel propagation | TU50nFH | +-------------------------+------------------------+ | Backoff | No | +-------------------------+------------------------+ | TSC placement | According to [6.2-3] | +-------------------------+------------------------+ | Burst length | According to [6.2-4] | +-------------------------+------------------------+ | CP length | PCE2-A: 6 | | | | | | PCE2-B: 9 | +-------------------------+------------------------+ | RX BW | PCE2-A: 240kHz | | | | | | PCE2-B: 275kHz | +-------------------------+------------------------+ | ICI suppression | No | +-------------------------+------------------------+ | MMM | According to [6.2.2] | +-------------------------+------------------------+
The reference relative performance between 1% Header BLER and 10% Data BLER
for EGPRS2-A and EGPRS2-B is depicted in Table 6.2-11.
Table 6.2-11. Relative performance between 1% Header BLER and 10% Data BLER,
EGPRS2-A and EGPRS2-B.
+--------+------------+------------------+------------+ | MCS | Header\@1% | Data\@10% [dB] | Rel. perf. | | | | | | | | [dB] | | [dB] | +--------+------------+------------------+------------+ | DAS-5 | 12.0 | 12.2 | 0.2 | +--------+------------+------------------+------------+ | DAS-6 | | 13.5 | 1.5 | +--------+------------+------------------+------------+ | DAS-7 | | 15.1 | 3.1 | +--------+------------+------------------+------------+ | DAS-8 | 13.6 | 19.1 | 5.5 | +--------+------------+------------------+------------+ | DAS-9 | | 21.4 | 7.8 | +--------+------------+------------------+------------+ | DAS-10 | 14.7 | 25.4 | 10.7 | +--------+------------+------------------+------------+ | DAS-11 | 16.3 | 30.3 | 14.0 | +--------+------------+------------------+------------+ | DAS-12 | 16.3 | 34.5* | 18.2 | +--------+------------+------------------+------------+
+--------+------------+------------------+------------+ | MCS | Header\@1% | Data\@10% [dB] | Rel. perf. | | | | | | | | [dB] | | [dB] | +--------+------------+------------------+------------+ | DBS-5 | 11.4 | 11.8 | 0.4 | +--------+------------+------------------+------------+ | DBS-6 | | 14.1 | 2.7 | +--------+------------+------------------+------------+ | DBS-7 | 17.4 | 21.9 | 4.5 | +--------+------------+------------------+------------+ | DBS-8 | | 24.4 | 7.0 | +--------+------------+------------------+------------+ | DBS-9 | 18.2 | 26.1 | 5.9 | +--------+------------+------------------+------------+ | DBS-10 | 20.2 | 37.5 | 16.7 | +--------+------------+------------------+------------+ | DBS-11 | 21.7 | 35.9** | 14.2 | +--------+------------+------------------+------------+ | DBS-12 | | 38.9** | 17.2 | +--------+------------+------------------+------------+
> *Performance at 20% BLER
>
> ** Performance at 30% BLER
In Table 6.2-12 the swap and shift required to achieve a PCE2 relative
performance similar to EGPRS2, shown in Table 6.2-11, is presented. Achieved
Header and Data BLER at selected swap and shift levels, is presented for
completeness. Swap is not applicable on QPSK modulated MCSes DBS-5 and DBS-6.
Table 6.2-12. Header mapping of PCE2-A and PCE2-B with relative difference
between Data and Header.
* * *
MCS Swap Shift Header\@1% [dB] Data\@10% [dB] Diff [dB] DAS-5 1 50 9,8 9,9 0,1
DAS-6 1 50 9,8 11,5 1,7 DAS-7 1 50 9,8 13,3 3,5 DAS-8 1 45 10,5 15,2 4,7 DAS-9
1 45 10,5 18,0 7,5 DAS-10 1 70 10,5 20,1 9,6 DAS-11 1 75 11,5 25,2 13,7
* * *
* * *
MCS Swap Shift Header\@1% [dB] Data\@10% [dB] Diff [dB] DBS-5 - 45 10.4 10.5
0.1 DBS-6 - 45 10.4 14.2 3.8 DBS-7 1 55 11.1 14.5 3.4 DBS-8 1 55 11.1 18.2 7.1
DBS-9 1 65 11.2 21.1 9.9 DBS-10 1 40 12.6 24.6 12 DBS-11 1 20 14.3 38.2 23.9
* * *
##### 6.2.4.1.5 IR performance
In Figure 6.2-4 and -5 ideal link adaptation envelope curves are shown for
both PCE2-A, EGPRS2-A and PCE2-B, given shift and swap parameters according to
table 6.2-12. Visible impacts from the header is seen at Es/N0 \ in order to detect between a PCE2 and EGPRS2 user;
  * Circular shift of training sequence, which adds negligible > computations.
With the DFT size 144 (2*2*2*2*3*3) and 168 (2*2*2*3*7) [6.1-4] proposed for
PC EGPRS2A and PC EGPRS2B, the FFT calculation can be optimized, thus limiting
the increase of computational complexity due to the addition of FFTs.
To summarize, the computational complexity of blind detection in PCE2, given
method in 6.3.1.2, is roughly twice the complexity of blind detection for
EGPRS2 plus the computation of the FFT.
#### 6.3.1.4 Simulation Assumptions and Results
##### 6.3.1.4.1 Simulation Assumptions
Table 6.3-1 lists the common simulation assumptions in the evaluation.
Table 6.3-1 Simulation assumptions.
+------------------------+-------------------------------------+ | Parameter | Value | +------------------------+-------------------------------------+ | MCSs | DAS5-DAS11 and DAS-12b, | | | | | | DBS7-DBS11 and DBS-12b | +------------------------+-------------------------------------+ | Channel propagation | TU50nFH | +------------------------+-------------------------------------+ | Interference | AWGN, CO, DTS-2 modified [6.3-2] | +------------------------+-------------------------------------+ | Frequency band | 900 MHz | +------------------------+-------------------------------------+ | Frames | 5000 | +------------------------+-------------------------------------+ | TSC placement | According to [6.3-3] | +------------------------+-------------------------------------+ | Burst length | According to [6.3-4] | +------------------------+-------------------------------------+ | CP length | PCE2-A: 6 | | | | | | PCE2-B: 9 | +------------------------+-------------------------------------+ | RX BW | PCE2-A: 240kHz | | | | | | PCE2-B: 275kHz | +------------------------+-------------------------------------+ | ICI Suppression | No | +------------------------+-------------------------------------+ | TX/RX impairments | Ericsson typical TX/RX impairments: | | | | | - Phase noise | 0.8 / 1.2 [degrees (RMS)] | | | | | - I/Q gain imbalance | 0.1 / 0.2 [dB] | | | | | - I/Q phase imbalance | 0.2 / 2.0 [degrees] | | | | | - DC offset | -45 / -40 [dBc] | | | | | - Frequency error | - / 25 [Hz] | +------------------------+-------------------------------------+
The offsets used for each modulation type are listed in Table 6.3-2. The
cross-correlation property of the circular shifted training sequences is
verified and no degradation has been observed in CO-channel interference
scenario.
Table 6.3-2: Offsets used for circular shift training sequence.
* * *
Modulation type 8PSK 16QAM 32QAM 64QAM Offset 0 2 5 7
* * *
##### 6.3.1.4.2 Simulation Results
Figure 6.3-3 shows the PCE2-A and PCE2-B performance of blind detection based
on the circular shifted training sequence, in interference limited and noise
limited scenario respectively. It can be seen that the modulation type
(8PSK/16QAM/32QAM/64QAM), user type (EGPRS2/PCE2) and levels (LevelA/LevelB
for PCE2B) can be correctly detected. The performance difference between ideal
blind detection and blind detection based on circular shift training sequence
is negligible for the simulated scenarios.
* * *
{width="3.45in" height="2.692361111111111in"} {width="3.475in"
height="2.7527777777777778in"}
* * *
Figure 6.3-3: Performance of BD based on circular shift training sequence,
PCE2.
### 6.3.2 References
[6.3-1] GP-101854, "Blind Modulation Detection in PCE2", source Telefon AB LM
Ericsson, ST-Ericsson SA. GERAN#48.
[6.3-2] GP-101847, "Mixed Mode Modulation", source Telefon AB LM Ericsson, ST-
Ericsson SA. GERAN#48.
[6.3-3] GP-101350, "Training symbol placements in Precoded EGPRS2 DL", source
Telefon AB LM Ericsson, ST-Ericsson. GERAN#47,
[6.3-4] GP-101349, "Aspects of burst formatting of Precoded EGPRS2 DL", source
Telefon AB LM Ericsson, ST-Ericsson SA. GERAN#47,
## 6.4 PAR reduction
By applying precoding to EGPRS2 the Peak-to-Average Ratio -- PAR -- of the
signal is increased.
This sub-clause contains methods and evaluations to reduce the PAR of PC
EGPRS2 while maintaining the spectral properties of the signal and minimizing
impact on link level performance.
[Editor's note: Depending on the extent of the PAR reduction, additional
investigations on impact from BCCH average power decrease might be needed.]
### 6.4.1 ...
## 6.5 Impact on legacy services
PC EGPRS2 introduces a new modulation technique in GERAN, which might have
impact on performance of legacy services but also impact on throughput due to
segregation of resource in multiplexing scenarios of USF and PAN transmission.
### 6.5.1 Impact on EGPRS2 throughput performance
#### 6.5.1.1 Impact from Single Block PCE2 interference
##### 6.5.1.1.1 Simulation assumptions and results
Figures 6.5-1 and 6.5-2, originally presented in [6.5-1], show simulated
EGPRS2-A and EGPRS2-B throughput performance when exposed to PCE2-A and PCE2-B
interference, respectively. The impact on performance is compared with the
impact caused by EGPRS2-A and EGPRS2-B interference.
The simulations were performed in a Co-channel interference scenario since
this is expected to most accurately reflect the characteristics of the
interference and expose possible differences between PCE2 and EGPRS2
interference. In each scenario the interfering MCS is chosen to be identical
to the carrier MCS. The detailed simulation assumptions are presented in Table
6.5-1
Table 6.5-1 Simulation assumptions.
+-------------------------+----------------------------------------+ | Parameter | Value | +-------------------------+----------------------------------------+ | Link direction | Downlink | +-------------------------+----------------------------------------+ | MS Type | Non-SAIC | +-------------------------+----------------------------------------+ | Frequency band | 900MHz | +-------------------------+----------------------------------------+ | Channels | TU3iFH | +-------------------------+----------------------------------------+ | Interference scenario | Co-channel interference | +-------------------------+----------------------------------------+ | Interference modulation | PCE2-A, PCE2-B, EGPRS2-A and EGPRS2-B. | +-------------------------+----------------------------------------+ | MCSs | DAS5-DAS12, DBS5-DBS12 | +-------------------------+----------------------------------------+ | TSC placement | According to [6.5-2] | +-------------------------+----------------------------------------+ | Burst length | According to [6.5-3] | +-------------------------+----------------------------------------+ | CP length | PCE2-A: 6 | | | | | | PCE2-B: 9 | +-------------------------+----------------------------------------+ | RX BW | PCE2-A: 240kHz | | | | | | PCE2-B: 275kHz | +-------------------------+----------------------------------------+ | ICI equalization | No | +-------------------------+----------------------------------------+ | Impairments: | Tx / Rx | | | | | -- Phase noise | 0.8 / 1.0 [degrees (RMS)] | | | | | -- I/Q gain imbalance | 0.1 / 0.2 [dB] | | | | | -- I/Q phase imbalance | 0.2 / 1.5 [degrees] | | | | | -- DC offset | -45 / -40 [dBc] | | | | | -- Frequency error | - / 25 [Hz] | +-------------------------+----------------------------------------+
{width="3.9972222222222222in" height="3.1493055555555554in"}
Figure 6.5-1 EGPRS2-A carriers exposed to PCE2-A and EGPRS2-A Co-channel
interference.
{width="4.0in" height="3.2430555555555554in"}
Figure 6.5-2 EGPRS2-B carriers exposed to PCE2-B and EGPRS2-B Co-channel
interference.
##### 6.5.1.1.2 Conclusions
Since PCE2 uses the same transmitter pulse shaping filters as EGPRS2 it can be
concluded that the difference between PCE2 and EGPRS2 signal characteristics
lies within the modulation method of the techniques. PCE2 is a narrow band
OFDM based technique and its characteristics can be roughly approximated as
pulse shaped Gaussian noise, regardless of transmitted MCS.
To conclude, it is expected that the impact from EGPRS2 and PCE2 interference
on EGPRS2 performance is similar. Figure 6.5-1 and 6.5-2 shows that this
assumption is valid as practically no difference can be seen between simulated
EGPRS2 performances when exposed to PCE2 or EGPRS2 interference.
### 6.5.2 References
[6.5-1] GP-101351, "Precoded EGPRS2 DL -- Impact on legacy services", source
Telefon AB LM Ericsson, ST-Ericsson SA. GERAN#47
[6.5-2] GP-101350, "Training symbol placements in Precoded EGPRS2 DL", source
Telefon AB LM Ericsson, ST-Ericsson SA. GERAN#47
[6.5-3] GP-101349, "Aspects of burst formatting of Precoded EGPRS2 DL", source
Telefon AB LM Ericsson, ST-Ericsson SA. GERAN#47
6.6 Impacts on base station and mobile station
6.6.1 ...
## 6.7 Reference performance
This sub-clause contains EGPRS2 reference performance for comparison with PC
EGPRS2 performance.
### 6.7.1 ...
# 7 Comparison of PC EGPRS2 with EGPRS2 performance
This sub-clause contains comparison of PC EGPRS2 with EGPRS2 performance after
the design and evaluation of the items listed in subclause 6 has been
completed.
# 8 Summary and conclusions
[Editor's note: To be added]
#