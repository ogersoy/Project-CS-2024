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
The rapid globalisation of the smart phone market is putting pressure on
legacy EDGE networks to improve throughput and spectrum efficiency.
To meet the demands on throughput and spectrum efficiency, MIMO for downlink
provides an interesting prospect because it neither puts too high requirements
on LTE enabled smart devices nor on legacy EDGE networks. All LTE enabled
smart devices come with two receive antennas, which is a valuable radio asset
that should be fully utilised. Similarly, legacy EDGE networks are often
configured with two transmit antennas to support air combining or transmit
diversity.
Performance evaluation submitted to GERAN#54 in GP-120762, to GERAN#55 in
GP-121019 and GP-121030 and to GERAN#56 in GP-121248 shows potential of this
technique to support significantly higher data peak throughput compared to
EGPRS and EGPRS2-A and as well as improving the spectral efficiency.
# 1 Scope
The present document contains investigations carried out and during the 3GPP
study item on MIMO for Downlink.
The following items are covered in this study report:
  * Objectives for the study
  * Overview of MIMO for Downlink concept
  * Conceptual design of several functional blocks of this solution
  * Performance evaluations related to envisaged functional blocks belonging to MIMO for Downlink
  * Compatibility analysis
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
[2] GP-130288 "New Study Item on Downlink MIMO", source Nokia Siemens
Networks, NOKIA Corporation, Com-Research GmbH, TELECOM ITALIA S.p.A.
[3] 3GPP TS 45.005 V7.25.0 Radio transmission and reception (Release 7).
[4] 3GPP TR 45.860 V11.5.0 Signal Precoding Enhancements for EGPRS2 DL.
[5] 3GPP TS 45.002 V11.0.0 Multiplexing and multiple access on the radio path
[6] 3GPP TS 44.060 V11.6.0 Radio Link Control / Medium Access Control
(RLC/MAC) protocol
[7] 3GPP TS 36.101 V11.0.0 Evolved Universal Terrestrial Radio Access
(E-UTRA); User Equipment (UE) radio transmission and reception (Release 11).
[8] 3GPP TR 25.814 V7.1.0 Physical layer aspects for evolved Universal
Terrestrial Radio Access (UTRA) (Release 7).
[9] 3GPP TR 25.996 V10.0.0 Spatial channel model for Multiple Input Multiple
Output (MIMO) simulations (Release 10)
# 3 Definitions and abbreviations
## 3.1 Definitions
For the purposes of the present document, the terms and definitions given in
TR 21.905 [1] and the following apply. A term defined in the present document
takes precedence over the definition of the same term, if any, in TR 21.905
[1].
## 3.3 Abbreviations
For the purposes of the present document, the abbreviations given in TR 21.905
[1] and the following apply. An abbreviation defined in the present document
takes precedence over the definition of the same abbreviation, if any, in TR
21.905 [1].)
BMD Blind Modulation Detection
DAS Downlink level A modulation and coding scheme
MCS Modulation and coding scheme
MSRD Mobile Station Receive Diversity
NSR Normal Symbol Rate
> SCPIR Sub Channel Power Imbalance Ratio
SINR Signal to Interference and Noise Ratio
TSC Training Sequence Code
USF Uplink State Flag
# 4 Objectives
The objective of the study is to investigate the feasibility of single user
MIMO in the downlink for PS data services including EGPRS and EGPRS2-A.
For MIMO support, two operational modes are foreseen:
a) spatial multiplexing mode based on dual stream 2x2 MIMO and
```{=html}
``` a) single stream diversity mode based on either MSRD or Tx diversity in
combination with MSRD.
In general, the study item re-uses as much as possible existing functionality
in GERAN and existing spatial channel models and principles used for UTRAN and
E-UTRAN. Different aspects of MIMO, as outlined in MIMO study item proposal
[2], are studied based on the following performance and compatibility
objectives.
## 4.1 Performance Objectives
The introduction of MIMO for downlink shall significantly improve data
throughput performance as compared to realistic EGPRS and EGPRS2-A
performance. The performance of MIMO shall be evaluated over the SINR range
relevant in GERAN networks.
## 4.2 Compatibility Objectives
The impact of MIMO for downlink on GSM speech codecs, GPRS, EGPRS and EGPRS2
shall be kept at a minimum. There should be no negative HW impact due to the
introduction of MIMO to the base station and mobile station, assuming the
mobile station already supports diversity antenna reception.
Any technique that requires changes to MCS design for GSM/EDGE are not part of
the study.
# 5 Overview of 2x2 MIMO System
## 5.1 Spatial multiplexing mode (dual stream)
In this mode, two different encoded bit-streams with orthogonal training
sequences are modulated and transmitted simultaneously through two different
antennas to the same mobile having two receiving antennas. In this 'dual
stream transmission mode', there are in effect 4 different propagation paths.
When the spatial correlation between the propagation paths is sufficiently
low, it should be possible for MIMO receiver to estimate the propagation paths
(a minimum SINR might be needed to estimate the propagation paths with
sufficient accuracy) and to jointly or iteratively detect each of the two
streams. When the above conditions are met, the throughput is maximised by
transmitting independent data streams from both transmitters. Henceforth this
is referred to as spatial multiplexing mode.
Figure 5.1.1: 2x2 MIMO Transmission in Spatial Multiplexing Mode
## 5.2 Diversity mode (single stream)
When the spatial correlation between the propagation paths is insufficient to
support spatial multiplexing, a single bit-stream with legacy training
sequence is modulated and transmitted either through two antennas or single
antenna. It should be possible for the receiver to benefit from transmit
diversity (Figure 5.2.1(a)) and/or receive diversity (Figure 5.2.1(b)).
Henceforth this is referred to as diversity mode. A popular transmit diversity
scheme is Delay Diversity, whereby the second transmit path is delayed
relative to the first to create an artificial propagation path that can be
exploited by a conventional equalizer. If an MS with dual receiver
architecture experiences significant blocking in one of its receivers, it can
still benefit from single antenna reception if network switches to transmit
diversity mode.
(a) (b)
Figure 5.2.1: Single Stream Transmission in Diversity Mode. (a) Transmit
Diversity, (b) Receive Diversity
# 6 MIMO Channel Model
To obtain a realistic evaluation of the performance of MIMO receiver, the
channel model will need to consider the correlation between the propagation
channels (e.g. due to the spatial proximity of the antennas or due to the
orientation of the polarization of the antennas).
## 6.1 MSRD Antenna Correlation Model
In [3] Annex N, a Single-Input-Multiple-Output (SIMO) model has been defined
(depicted in Figure 6.1.1 in this document) which is based on a magnitude of
complex correlation parameter ρ and an antenna gain imbalance G. To use the
model in the performance evaluation, the model would need to be extended to a
MIMO system comprising independent paths for a second transmit antenna and
with realistic spatial correlation values for the transmit antennas and the
receive antennas (two values of ρ are given in the MSRD performance
requirements, but these only loosely correspond to best and worse case
values).
{width="3.975in" height="1.7368055555555555in"}
Figure 6.1.1: Single-Input-Multiple-Output channel model for MS Receiver
Diversity.
## 6.2 Spatial Channel Model (SCM)
Spatial Channel Models were first introduced to 3GPP RAN4 based on work in the
WINNER project for systems beyond 3G, for a bandwidth up to 20MHz. The spatial
channel model for use in system-level simulations is described in 3GPP TR
25.996 (section 5) [9] for generic antenna configurations in the Node-B and
UE. For performing link simulations, the model requires a significant amount
of simulation time. Therefore, taking into consideration specific antenna
configurations for the Node-B and UE, relevant aspects of the channel
properties and reasonable simulation assumptions, simplified models have been
defined for four scenarios namely SCM-A, SCM-B, SCM-C and SCM-D (see [8]). The
model used in this study is SCM-A unless otherwise stated.
The simplified model consists of two components:
\- a tapped delay line propagation model similar to the GSM models in 3GPP TS
45.005 Appendix C.3 [3], and,
\- covariance matrices for describing the correlation between the propagation
paths .
These covariance matrices assume antenna configurations consisting of two
spatially separated +45/-45 degree slant cross-polarized antennas in the
Node-B and one double-polarized antenna (V and H) in the mobile station. For
each tap a distinct covariance matrix is defined.
The per-tap covariance matrix **R** _~tap~_ is obtained from the Kronecker
product of the polarization covariance matrix **Г** and the Node B and UE
spatial correlation matrices **A** and **B** , further weighted by the antenna
gains at Node B and UE:
> {width="2.75in" height="0.2638888888888889in"} (6.2.1)
where _p~tap~_ is the relative power of the tap, {width="0.5833333333333334in"
height="0.2638888888888889in"} is the effective antenna gain at the Node B,
{width="0.44375in" height="0.2638888888888889in"} is the antenna gain at the
UE, {width="0.94375in"
height="0.5833333333333334in"},{width="0.9583333333333334in"
height="0.5833333333333334in"} and _α_ and _β_ are the spatial correlation
parameters of Node B and UE respectively. {width="0.17777777777777778in"
height="0.19722222222222222in"}denotes Kronecker multiplication.
The values of _α_ , _β_ , **Г** and _p~tap~_ can be found for all the four
scenarios in the tables A.1.3-2 to A.1.3.-5 of TR 25.814 [8].
{width="0.5833333333333334in" height="0.2638888888888889in"}and
{width="0.44375in" height="0.2638888888888889in"}are assumed to be unity.
The antenna polarization correlation matrix **Г** is organised as
[NodeB+45UEvert, NodeB-45UEvert, NodeB+45UEhor, NodeB-45UEhor]. Here the
notation NodeB+45UEvert refers to "from +45° slant element at NodeB to
vertically polarized element of UE".
For the performance evaluation of the downlink MIMO concept with 2 transmit
antennas and 2 receive antennas, it is possible to simplify these models
further and apply these in the GSM link simulations.
To derive a 2x2 configuration it can be assumed that one +45/-45 degree slant
cross-polarized antenna at the BTS and one double-polarized antenna (V and H)
at the MS are used. With this assumption we can ignore both spatial
correlation matrices **A** and **B** and use only the 4x4 polarization
covariance matrix **Г** for computing the per-tap covariance matrix for 2x2
MIMO simulation. We can also extend the assumption of unity antenna gains at
transmitting and receiving antennas for simplicity.
In tables A.1.3-2 to A.1.3.-5 of TR 25.814 [8], the delay values and the power
of taps for each profile are given in six clusters, with 3 taps in each
cluster. The 3 taps in each cluster are each 12.5 nanoseconds apart. Also the
relative powers of taps within the cluster is same in all clusters. This fine
resolution is applicable only to wideband carriers; hence for narrowband GSM,
we can simply take a single value from each cluster without loss of precision.
This study takes the first value from each cluster. So, we have six delay
values and six corresponding tap powers for GSM simulation.
Further details about the realization of the modified SCM can be found in the
Annex A.
In case of MSRD simulation (see section 6.1), there are only two paths. So the
4x4 correlation matrix **Г** is unsuitable. Since the **Г** matrix is
organised as [NodeB+45UEvert, NodeB-45UEvert, NodeB+45UEhor, NodeB-45UEhor],
we can take the 1^st^ and 3^rd^ element of the 1^st^ and 3^rd^ row of each 4x4
matrix to form the 2x2 correlation matrix. The correlation matrix computed in
this way is applied in the same way as the 4x4 correlation matrix is applied
but for two paths (_L_ =2) (see Annex A).
## 6.3 Channel model with variable correlation
Although the modified SCMs described in section 6.2 are sufficient enough in
most scenarios, there is no flexibility to change the amount of correlation
between the propagation paths. Performance of a MIMO receiver largely depends
on correlation between the multiple propagation paths between the transmitter
and receiver. Moreover, MS possibly needs to detect the channel rank and thus
indicate to the network if MIMO with spatial multiplexing is the better mode
of transmission. Therefore, to evaluate such detection performance, it is
essential to use a channel model with variable correlation.
MIMO Channel Correlation Matrices for 3G and LTE system is defined in annex
B.2.3.1 of [7] for 1x2, 2x2, 4x2 and 4x4 antenna configurations. The overall
spatial correlation matrix, _R~spat~_ is expressed as the Kronecker product of
correlation matrix for the eNodeB (_R~eNB~_) and the UE (_R~UE~_) i.e.
> {width="1.2638888888888888in" height="0.2638888888888889in"} (6.3.1.1)
The 2x2 MIMO system in this study assumed 2 spatially separated antennas at
the transmitter and 2 spatially separated antennas at the receiver. For this
configuration, _R~eNB~_ and _R~UE~_ are defined using correlation parameters
_α_ and _β_ as:
> $R_{\text{eNB}} = \begin{matrix} \left( 1\text{\ \ \ \ \ \ \ \ }\alpha
> \middle| \right) \ \ \end{matrix}$ and $R_{\text{UE}} = \begin{matrix}
> \left( 1\text{\ \ \ \ \ \ \ \ }\beta \middle| \right) \ \ \end{matrix}$
> (6.3.1.2)
Using equations 6.3.1.1 and 6.3.1.2, it is possible to compute the channel
correlation matrix for 2x2 MIMO simulation for any value of _α_ and _β_
between 0 and 1.
It is necessary to note that Annex B.2.3A of [7] also defines spatial
correlation matrix for cross polarised antennas according to
$R_{\text{spat}} = P\left( R_{\text{eNB}} \otimes \Gamma \otimes R_{\text{UE}}
\right)P^{T}$ (6.3.1.3)
where, **Г** is the polarization correlation matrix and P is the permutation
matrix whose elements depend on antenna element labelling system. However,
**Г** is defined for at least one pair of cross polarised antennas at eNodeB
and one pair of cross polarised antennas at the UE. So, for a 2x2 MIMO system,
the spatial correlation matrix _R~eNB~_ and _R~UE~_ become redundant in
equation (6.3.1.3) and the _R~spat~_ matrix turns into the polarisation
covariance matrix of the SCM profiles described in section 6.2. Therefore, 2x2
MIMO simulations with variable correlation spatial channel model assumes only
spatially separated antennas at the transmitter and receiver.
The realisation of the correlation in the simulation as described in Annex A
is also applicable here. Instead of the principle square root of polarisation
covariance matrix, it is necessary to apply the principle square root of
_R~spat~_ to the independent Rayleigh faded waveforms to achieve the desired
correlation between the paths.
In the single stream receive diversity mode, _R~eNB~_ is ignored in the
computation of the _R~spat~_ matrix using equation (6.3.1.1). Therefore, the
amount of correlation can be varied only by varying _β_.
# 7 Concepts
## 7.1 Training sequences
When estimating the channel taps of the four spatial propagation channels
(depicted in Figure 5.1.1), it would be advantageous if the training sequences
assumed orthogonal properties.
Already, orthogonal training sequences were introduced in Rel-9 for VAMOS.
These training sequences, referred to as TSC Set 2, were optimised to give low
cross-correlation when used pair-wise with the legacy training sequence set,
which has been referred to as TSC Set 1 (Table 5.2.3a and Table 5.2.3b in
45.002).
While both TSC Set 1 and TSC Set 2 are binary, TSC Set 1 has been modified for
use with 8-PSK and higher order modulations by mapping each binary value of
GMSK bit-mapping to each of the constellation points of the respective
modulation scheme (see Normal burst for 8-PSK, 16-QAM and 32-QAM in 45.002
Section 5.2.3).
Hence, a straight-forward procedure to obtain an orthogonal set for 8-PSK and
higher order modulations is to apply the same antipodal mapping for TSC Set 2.
## 7.2 Modulations
### 7.2.1 Impact of Mixed Modulations
A comprehensive analysis is done in [7.2-1] to evaluate the impact of same or
different modulations used on both streams in spatial multiplexing mode in a
number of scenarios. In [7.2-1], the impact is analysed using 8-PSK, 16-QAM
and 32-QAM modulations and associated EGPRS2-A coding schemes. When different
modulations are used in two MIMO streams, all possible MCSs in each modulation
is simulated. GMSK modulation is not used in this investigation because GMSK
modulation is attractive only at low SINR region and in that region dual
stream MIMO throughput with GMSK modulation will likely be outperformed by
transmission in diversity mode.
In the dual stream MIMO transmission mode, however, GMSK is considered to be a
candidate modulation for one stream or two streams if mixed modulation is
used. For instance, the control channel messages on PACCH are sent with GMSK
modulation in one stream, while the traffic channel messages on the other
stream are sent using either 8-PSK, QAM or GMSK modulation depending on radio
channel quality.
A simple MIMO receiver is used for the analysis in [7.2-1]. This receiver
employs channel estimation, followed by separate interference cancellation and
bit-detection for each stream. This is neither a successive interference
cancellation (SIC) type of receiver, nor a joint detection (JD) receiver, but
it is expected that performance will be similar if SIC or JD receivers were
used instead. Blind modulation detection (BMD) is enabled in the receiver. BMD
is performed after the channel estimation assuming all possible modulations
schemes including GMSK. The BMD mechanism is similar to what is used in
[7.2-2].
#### 7.2.1.1 Simulation Parameters
Table 7.2.1.1.1: Simulation Parameters
+----------------------+----------------------+----------------------+ | **Parameter** | **Value** | | +----------------------+----------------------+----------------------+ | Frequency bands | 1800 MHz | | +----------------------+----------------------+----------------------+ | Propagation | SCM-A | | | conditions | | | +----------------------+----------------------+----------------------+ | Mobile speed | 3 km/hr | | +----------------------+----------------------+----------------------+ | Frequency hopping | Ideal | | +----------------------+----------------------+----------------------+ | BTS/MS RF | Typical Tx/Rx (see | | | impairments | Table 7.2.1.1.3 and | | | | Table 7.2.1.1.4) | | +----------------------+----------------------+----------------------+ | Interference | Single co-channel | | | | interference, with | | | | 8PSK modulation. | | +----------------------+----------------------+----------------------+ | Channel Correlation | SCM-A specific for | | | | wanted signal, 0.7 | | | | for interference | | +----------------------+----------------------+----------------------+ | SCPIR [dB] | CCI: 0dB and 6dB | | | | Sensitivity: 0, 2, | | | 10log~10~(Power of | 4, 6, 8 and 10dB | | | stream 1/power of | | | | stream 2) | | | +----------------------+----------------------+----------------------+ | Back-off [dB] | Sensitivity: | | | | Theoretical PAR | | | | taken from TR45.860, | | | | section 8: 3.2dB for | | | | 8PSK, 4.7dB for | | | | 16-QAM and 5.1dB for | | | | 32-QAM. | | | | | | | | CCI: 0dB for all | | | | modulations. | | | | | | | | Additional back-off | | | | based on SCPIR | | | | (given in Table | | | | 7.2.1.1.2) is used | | | | in the transmit | | | | power in spatial | | | | multiplexing mode, | | | | for both sensitivity | | | | and CCI, to compare | | | | with single antenna | | | | transmission power | | | | (see Table 7.2e | | | | 7.2.1.1.2). | | +----------------------+----------------------+----------------------+ | MCSs | EGPRS2-A | 8-PSK | | | | (DAS-5...DAS-7) | | | | | | | | 16-QAM | | | | (DAS-8...DAS-9) | | | | | | | | 32-QAM | | | | (DAS-10...DAS-12) | +----------------------+----------------------+----------------------+ | | EGPRS | Not used | +----------------------+----------------------+----------------------+ | Blind modulation | Enabled where | | | detection | mentioned | | +----------------------+----------------------+----------------------+ | Blind MIMO mode | Ideal | | | detection | | | +----------------------+----------------------+----------------------+ | MCS link adaptation | Ideal | | +----------------------+----------------------+----------------------+ | Rank adaptation | Ideal | | +----------------------+----------------------+----------------------+ | Training sequence | 1^st^ Stream: 5 from | | | codes | VAMOS Set 1 | | | | | | | | 2^nd^ Stream: 5 from | | | | VAMOS Set 2 | | +----------------------+----------------------+----------------------+
In order to make a fair comparison of throughput between dual stream
transmission mode and single stream mode, it is necessary to use appropriate
back-off on the transmitted power of dual stream transmission mode. However,
the back-off value depends on the SCPIR used. At SCPIR=0 dB, a 3 dB back-off
from the total power is needed to compare with the transmitted power in the
single stream transmission mode. However, if a non-zero SCPIR is used, we need
to apply lower back-off assuming the total transmitted power is the limiting
factor and should be kept same as the power in single stream transmission
mode. The formula used for back-off calculation in the dual stream
transmission mode is given in equation 7.2.1.1.1 and the values computed from
the equation are given in Table 7.27.2.1.1.2.
> $\text{backoff} = \text{10}\text{log}_{\text{10}}(1 + \text{10}^{\frac{-
> \text{SCPIR}}{\text{10}}})$ (7.2.1.1.1)
Table 7.2.1.1.2: Back-off in dual stream transmission mode
* * *
**SCPIR (dB)** **Back-off (dB)** 0 3.00 2 2.12 4 1.46 6 0.97 8 0.64 10 0.41
* * *
Table 7.2.1.1.3: Transmitter Impairments
* * *
**Impairment** **Legacy single carrier BTS (per TRX)**
Phase noise [degrees (RMS)] 1.2
I/Q gain imbalance [dB] 0.1
I/Q phase imbalance [degrees] 0.1
DC offset [dBc] -45
Frequency error [Hz] 15 (900 MHz)\ 30 (1800 MHz)
Tx path time misalignment [normal symbol periods] 0.25
* * *
Table 7.2.1.1.4: Receiver Impairments
* * *
**Impairment** **Rx diversity capable device (per Rx path) (Taken from 3GPP TR
45.860 [4])**
Phase noise [degrees (RMS)] 1.2
I/Q gain imbalance [dB] 0.2
I/Q phase imbalance [degrees] 2.0
DC offset [dBc] -40
Frequency error [Hz] 25 (900 MHz)\ 50 (1800 MHz)
Rx path time misalignment [symbols] negligible
* * *
#### 7.2.1.2 Simulation Results
Before presenting the impact of mixed modulation on combined MIMO throughput,
it is worthwhile to show the impact of mixed modulation on throughput of the
first stream when a different modulations is used in the second stream. Figure
7.2.1.2.1 presents this in a group of plots with legends in each plot showing
modulation type of first stream on the left hand side of "+" sign and that of
the second stream on the right hand side.
From these figures, it is quite evident that the impact on the first stream\'s
throughput is minor regardless of the modulation scheme used in the second
stream.
{width="2.9902777777777776in"
height="2.189583333333333in"}{width="2.9902777777777776in"
height="2.189583333333333in"}{width="2.9902777777777776in"
height="2.189583333333333in"}{width="2.9902777777777776in"
height="2.189583333333333in"}{width="2.9930555555555554in"
height="2.154166666666667in"}{width="2.9930555555555554in"
height="2.154166666666667in"}
Figure 7.2.1.2.1: Throughput of Stream 1 with same or different modulation in
stream 2 in 2x2 MIMO.
It should be noted that acceptable throughput is achieved from different
modulations at different Es/No or C/I ranges. Therefore, it is worthwhile to
look at combined MIMO throughput for different modulation mixes over a wider
range of Es/No or C/I.
In order to analyse the impact of mixed modulation on the combined throughput
of both streams, following two scenarios are considered.
a. Same modulation is used on both streams but coding schemes within the
modulation are flexible. Simulation is run over all possible pairs of EGPRS2-A
coding schemes in a particular modulation over a range of Es/No or C/I. At
each Es/No or C/I point, maximum throughput among all possible pairs of coding
schemes (within the same modulation) is taken to compute MIMO throughput at
that Es/No or C/I point.
b. Different modulations and coding schemes are used in both streams. In this
case, simulation is run over all possible EGPRS2-A MCS combinations (with the
restriction that both streams do not have same modulation) and at each Es/No
or C/I point, throughput of the MCS pair providing maximum combined throughput
is chosen in computing the combined MIMO throughput at that Es/No or C/I
point.
Results of both scenarios a) and b) are plotted in Figure7.2.1.2.2 using solid
and dashed lines respectively. Since, in case of non-zero SCPIR, second stream
is weaker than first stream, plots for mixed modulation schemes are presented
twice for each modulation combination i.e. one plot is shown, for example, for
8PSK+16QAM and another for 16QAM+8PSK. {width="5.854166666666667in"
height="3.339583333333333in"}{width="5.854166666666667in"
height="3.339583333333333in"}{width="5.854166666666667in"
height="3.339583333333333in"}
{width="5.854166666666667in" height="3.339583333333333in"}
Figure 7.2.1.2.2: Combined MIMO throughput with the same or different
modulations in the two streams.
From Figure 7.2.1.2.2, it is obvious that overall maximum throughput is
achieved over the entire range of simulated Es/No if the same modulation is
used in both MIMO streams provided that there is no imbalance between the
powers of the two MIMO streams. The situation changes, however, at higher
power imbalance. As the SCPIR increases, the throughput from a mixed
modulation pair gets higher than that from a same modulation pair in the mid
range of Es/No.
Similar analyses are also done in [7.5-1] and [7.2-3] showing same observation
as in [7.2-1].
### 7.2.2 Blind Modulation Detection
Performance of blind modulation detection is evaluated in [7.2-1] and [7.5-1].
In both technical contributions, it is assumed that the receiver detects the
modulation separately for each MIMO stream. With separate detection per
stream, the total number of hypothesis to verify for each stream is 4 (GMSK,
8-PSK, 16-QAM and 32-QAM), i.e. 8 in total for MS supporting EGPRS2-A MIMO.
The computational complexity involved in blind modulation detection in MIMO
is, therefore, similar to that for EGPRS2-B, which involves a total of 7
hypotheses.
Figure 7.2.2.1 shows the impact of blind modulation detection in overall MIMO
throughput when ideal link and mode adaptation is assumed. The plots in this
figure are taken from [7.2-1]; the simulation parameter setting is given in
Table 7.2.1.1.1 to 7.2.1.1.4. The plots are in fact the envelope of the mixed
modulation throughputs shown in section 7.2.1. It is clear that the BMD error
in the modelled MIMO receiver has almost no impact on the performance. The
observation is in line with what is shown in [7.5-1] although a SIC type of
receiver is used with similar simulation parameter settings as in [7.2-1].
It is evident that the BMD error has almost no impact on the MIMO peak
throughput in spatial multiplexing mode.
{width="4.664583333333334in" height="3.1354166666666665in"}
{width="4.678472222222222in" height="3.1243055555555554in"}
Figure 7.2.2.1: Impact of blind modulation detection on combined MIMO
throughput.
### 7.2.3 Impact of SCPIR
Overall throughput with mixed modulation pairs and at different SCPIR values
is shown in Error: Reference source not found7.2.3.1 (taken from [7.2-1]). The
figure shows the overall peak throughput decreasing with the increase in
SCPIR. For comparison, EGPRS2-A MSRD performance in the same condition is
shown in the same figure. The Es/No at which spatial multiplexing mode
outperforms diversity mode varies between 15dB (SCPIR=0) and 22dB
(SCPIR=10dB).
{width="6.500694444444444in" height="4.091666666666667in"}
Figure 7.2.3.1: Impact of SCPIR on combined MIMO throughput.
Similar results are also presented in [7.2-3] using a SIC type of receiver and
different training sequence pairs. In [7.2-3], it is shown that, with SCPIR
10dB MIMO still outperforms MSRD at SNR > 25dB. It is also shown in [7.5-2],
that if a legacy MS is multiplexed with MIMO capable MS, spatial multiplexing
mode can be used to transmit data to MIMO capable MS and USF to the legacy MS.
Generally a large SCPIR is needed to meet the USF performance requirement by
the legacy MS in such case. MIMO performance in general degrades with
increased SCPIR. Therefore, the network should ensure that there is
performance benefit to the MIMO MS by applying spatial multiplexing mode with
a large SCPIR instead of applying single stream transmission.
### 7.2.4 Conclusion
This sub-clause presents the performance of 2x2 MIMO in spatial multiplexing
mode when same or different modulations are used in the MIMO streams. The
following conclusions can be drawn from the study in this sub-clause:
The impact of mixed modulation on the overall peak throughput depends on the
power imbalance between the streams. In case of SCPIR=0dB (i.e. equal power in
both streams), the overall maximum throughput is achieved if both streams have
the same modulation. As the SCPIR increases, the throughput with a mixed
modulation pair gets higher than that with a same modulation pair in the mid
range of C/I or Es/No.
The BMD error has almost no impact on the MIMO peak throughput in spatial
multiplexing mode. In this evaluation BMD is performed in the two streams
separately.
However, the overall peak throughput decreases with the increase of the
absolute value of the SCPIR (in dB). The Es/No or C/I at which the spatial
multiplexing mode outperforms the diversity mode depends on the SCPIR.
The advantage of mixed modulation is that the link adaptation can be applied
independently on both streams in the same way as it is done in downlink dual
carrier operation. It may also be beneficial for retransmissions in EGPRS2-A
where otherwise the modulation scheme would have to be aligned between the
streams because not all modulations provide all MCS families. On the other
hand, the receiver is likely to make more modulation detection errors if mixed
modulation is used in the MIMO streams. However, it has been shown that the
impact of the BMD error is negligible.
By analysing the technical contributions in [7.2-1], [7.5-1], [7.2-3] and
[7.5-2], it can be concluded that the usage of mixed modulation for Downlink
MIMO is beneficial in case of non-zero SCPIR. The SCPIR value with a pair of
cross polarised antenna is likely to be zero, but the amount of SCPIR that can
naturally occur in the MIMO transmission system is not clear. Use of
artificially large SCPIR, in order to multiplex legacy user for USF
transmission, should be limited to reasonably high SNR condition only.
### 7.2.5 References
  1. GP-130983, "Impact of Mixed Modulation on Downlink MIMO", source NSN, GERAN#60.
  2. GP-130668, "Blind detection for MIMO", source Telefon AB LM Ericsson, ST-Ericsson SA, GERAN#59.
  3. GP-130469, "_On SCPIR for MIMO", source Telefon AB LM Ericsson, ST-Ericsson SA, GERAN#58._
  4. GP-130470, "_On multiplexing with legacy services in MIMO", source Telefon AB LM Ericsson, ST-Ericsson SA, GERAN#58._
## 7.3 Mode Adaptation
_[Editor's note: This section will treat use cases of different modes, mode
adaptation strategy and blind mode detection.]_
## 7.4 Link Adaptation
_[Editor's note: This section will treat how the link adaptation can be done
in both streams in spatial multiplexing mode. The study will check if the
existing procedure for DLDC can be reused and differences identified.]_
## 7.5 Other RLC/MAC Protocol Aspects
### 7.5.1 Multi-slot Class
It is assumed that an MS supporting DL MIMO supports dual stream transmission
on all assigned timeslots of a DL TBF wherein the maximum number of timeslots
supported for DL MIMO is indicated by the multislot class as defined in TS
45.002 Annex B [5] unless restricted by the DL MIMO multislot reduction
parameter as described below.
A DL MIMO capable MS may need a multislot capability reduction to support the
MS to reduce the baseband processing load as the DL MIMO receiver would be
more complex than a legacy MS receiver. This is taken into account by a new DL
MIMO multislot capability reduction parameter, e.g. signalled by the MS to the
network. In this case, the network will reduce the timeslot assignment for the
MS in DL MIMO configuration in accordance with the signalled multislot class
and multislot capability reduction parameter. The details of the encoding of
the multislot capability reduction parameter are left for the specification
phase.
It is left for further study to find out how multislot capability reduction
signalling can be designed if a DL MIMO capable MS also supports DLDC or DLMC.
### 7.5.2 TBF Establishment
If the network and mobile station both support DL MIMO, the network may send a
packet assignment message or a PS HANDOVER COMMAND message to a mobile station
indicating support for DL MIMO configuration. The configuration can be changed
via a subsequent packet assignment message. There will be a new IE in the
assignment message indicating an assignment type of \'MIMO assignment\'.
The same timeslot (PDCH) assignment is used for both spatial streams in
spatial multiplexing mode. Both streams belong to the same TBF. Block sequence
numbers for both streams belong to the same RLC engine.
In order to avoid added complexity, multiple TBF mode shall not to be
supported with DL MIMO configuration.
### 7.5.3 TBF Operation
A MIMO capable MS in DL MIMO configuration is able to receive both dual stream
and single stream transmission mode. Single stream mode can be used
occasionally in DL MIMO configuration due to radio conditions, or when a
legacy MS is allocated the same timeslot. Whether the MIMO capable MS detects
the transmission mode blindly or it needs signalling from the network about
the used transmission mode is left for further study. It has been demonstrated
in [7.5-1] that even if the MIMO capable MS always operates its receiver in
spatial multiplexing mode, the overall performance loss due to occasional
false detection of spatial multiplexing mode while the network actually used
single stream mode is negligible. Continuous operation of te receiver in
spatial multiplexing mode, however, will lead to additional power consumption
as the complexity of the MIMO receiver for spatial multiplexing mode is higher
than that of the receiver for a dedicated single stream transmission mode.
Different coding schemes and modulations can be used on the two streams in
spatial multiplexing mode.
For Downlink MIMO configurations TBFs shall operate in EGPRS TBF mode (DL MIMO
supports also EGPRS2-A which uses EGPRS TBF mode).
In dual stream transmission, any control message is sent on either stream
(control messages are as defined in 3GPP TS 44.060 [6]). All segments
belonging to each RLC/MAC control message shall be sent on the same stream.
In dual stream transmission the same USF is sent on both streams. However, if
different modulations are used in two streams, the encoded USF bits in the air
interface are different. The mobile transmits in the next RLC block period(s)
according to the signalled USF granularity if the decoded USF is targeted to
itself.
### 7.5.4 Multiplexing of legacy MSs (USF, PAN)
The multiplexing of a MIMO capable MS in DL MIMO configuration on the same
timeslot as a legacy mobile, with the USF/PAN intended for the legacy MS, can
be achieved with either a temporary transmission of a single stream or dual
stream transmission.
When using spatial multiplexing mode, a large SCPIR is typically needed to be
used. This is explained in detail in [7.5-2]. Based on the analysis given in
[7.5-2], it can be deduced that the network will have to decide carefully when
to use this mechanism because spatial multiplexing mode may have negative
impact on USF/PAN decoding performance in some type of legacy MS. The network
should also ensure that there is performance benefit to the MIMO MS by
applying spatial multiplexing mode with a large SCPIR instead of applying
single stream transmission.
### 7.5.5 References
  1. GP-130668, "Blind detection for MIMO", source Telefon AB LM Ericsson, ST-Ericsson SA, GERAN#59.
  2. GP-130470, "_On multiplexing with legacy services in MIMO", source Telefon AB LM Ericsson, ST-Ericsson SA, GERAN#58._
## 7.6 Signalling
## 7.6.1 MS Capability Signalling
_[Editor's note: This section will treat how a MIMO capable MS can signal its
MIMO capabilities (e.g. level of support in terms of MIMO modes and modulation
types) to the network.]_
## 7.6.2 Mode Adaptation Signalling
_[Editor's note: This section will treat the benefit of signalling supported
mode adaptation.]_
# 8 Performance Evaluation
## 8.1 Transmitter assumption
Transmitter impairment values for a typical BTS as given in Table 8.1.1 are
used for performance evaluations [8-1].
Table 8.1.1: Transmitter Impairments
* * *
**Impairment** **Legacy single carrier BTS (per TRX)**
Phase noise [degrees (RMS)] 1.2
I/Q gain imbalance [dB] 0.1
I/Q phase imbalance [degrees] 0.1
DC offset [dBc] -45
Frequency error [Hz] 15 (900 MHz)\ 30 (1800 MHz)
Tx path time misalignment [normal symbol periods] 0.25
* * *
## 8.2 Receiver assumptions
The MIMO receiver being used in the analysis in section 7.2 is also used for
the performance evaluation. The block diagram of the receiver is shown in
Figure 8.2.1. This receiver employs channel estimation, followed by separate
interference cancellation (IRC) and bit-detection for each stream. Before bit
detection, a frequency domain prefiltering is used to convert the system to
minimum phase. The frequency domain prefilter (SC-FDE), shown in Figure 8.2.2,
multiplies FFT output of signal, {R~n~}, by the complex-valued forward
equalizer coefficients {W~n~} (which compensate for the frequency selective
channel's variations of amplitude and phase with frequency). An IFFT operation
brings the weight-equalized complex-valued samples in time-domain sequences.
Finally the time domain sequence goes through the reduced state bit-detection
process for soft bit detection in each stream.
This is neither a successive interference cancellation (SIC) type of receiver,
nor a joint detection (JD) receiver and it is seen in a number of simulations
that the performance is similar to SIC or JD receivers but with much less
complexity.
Blind modulation detection (BMD) is enabled in the receiver. BMD is performed
after the channel estimation assuming all possible modulations schemes
including GMSK. In addition, blind mode detection is enabled. The mode
detection in the receiver is based on SNR estimation after the interference
cancellation. If SNR of the second stream is found to be below the chosen
threshold of 2 dB, the receiver assumes that single stream is transmitted
[8-2]. The blocks with hatched lines in Figure 8.2.1 are used if the mode
detection process detects the presence of second stream.
The blocks with solid white filling constitute the reference MSRD receiver for
legacy non-MIMO operation. Therefore, the complexity of the MIMO receiver is
approximately twice the complexity of the reference non-MIMO receiver.
Receiver impairment values are given in Table 8.2.1.
{width="6.689583333333333in" height="1.3375in"}
Figure 8.2.1: MIMO receiver structure used for performance evaluation
{width="3.607638888888889in" height="0.625in"}
Figure 8.2.2: Single Carrier Frequency Domain Equaliser (SC-FDE)
Table 8.2.1: Receiver Impairments
* * *
**Impairment** **Rx diversity capable device (per Rx path) (Taken from 3GPP TR
45.860 [4])**
Phase noise [degrees (RMS)] 1.2
I/Q gain imbalance [dB] 0.2
I/Q phase imbalance [degrees] 2.0
DC offset [dBc] -40
Frequency error [Hz] 25 (900 MHz)\ 50 (1800 MHz)
Rx path time misalignment [symbols] negligible
* * *
## 8.3 Simulation scenario
The link level performance evaluation is first grouped according to the
correlation models used, i.e. SCM and variable correlation channel model. In
each group the results are divided into sensitivity and interference
scenarios. In each scenario, the results are further grouped according to
propagation conditions. The simulation parameters relevant to simulation
scenarios are listed in Table 8.3.1 [8-1].
Table 8.3.1: Simulation scenarios and parameters
+----------------------+----------------------+----------------------+ | **Parameter** | **Value** | | +----------------------+----------------------+----------------------+ | Transmission Mode | Single stream MSRD | | | | (reference) | | | | | | | | Single stream (in | | | | MIMO mode, blind | | | | mode detection | | | | enabled) | | | | | | | | - with MSRD | | | | | | | | - with Tx | | | | > diversity and | | | | > MSRD | | | | | | | | Dual stream (2x2 | | | | MIMO) | | +----------------------+----------------------+----------------------+ | Training Sequence | Single stream mode: | | | | TSC 5 from TSC Set 1 | | | | | | | | Dual stream mode: | | | | TSC 5 from TSC Set 1 | | | | and TSC Set 2. | | | | | | | | In case of mixed | | | | modulation other | | | | combinations can be | | | | used if benefit is | | | | seen. | | +----------------------+----------------------+----------------------+ | Channel model | A modified SCM as | | | | described in section | | | | 6.2 for dual stream | | | | mode | | | | | | | | Variable correlation | | | | model as described | | | | in section 6.3 for | | | | both dual stream | | | | mode and single | | | | stream mode | | +----------------------+----------------------+----------------------+ | Modulations | Single stream mode: | | | | all supported | | | | modulations in EGPRS | | | | and EGPRS2-A | | | | | | | | Dual stream mode: | | | | all supported | | | | modulations in EGPRS | | | | and EGPRS2-A except | | | | GMSK. Both streams | | | | can have the same or | | | | different | | | | modulations. | | +----------------------+----------------------+----------------------+ | Frequency bands | - 900 MHz (antenna | | | | correlation model) | | | | | | | | -1800 MHz (SCM) | | +----------------------+----------------------+----------------------+ | Propagation | 900 MHz | | | conditions | | | | | - Sensitivity | | | | | | | | - SCM-A3iFH | | | | | | | | - TU3iFH | | | | | | | | - Interference | | | | | | | | - SCM-A3iFH | | | | | | | | - TU3iFH | | | | | | | | 1800 MHz | | | | | | | | - Sensitivity | | | | | | | | - SCM-A3iFH | | | | | | | | - TU3iFH | | | | | | | | - RA130nFH | | | | | | | | - Interference | | | | | | | | - SCM-A3iFH | | | | | | | | - TU3iFH | | | | | | | | - RA130nFH | | +----------------------+----------------------+----------------------+ | Interference | Multiple | | | | interference sources | | | | as defined for DTS-2 | | | | interference profile | | | | with 8PSK | | | | modulation. | | +----------------------+----------------------+----------------------+ | Channel Correlation | Wanted signal: | | | | | | | | For SCM model it is | | | | SCM specific. | | | | | | | | For variable | | | | correlation model: | | | | α, β = {0.0, 0.0}, | | | | {0.0, 0.7} and {0.3, | | | | 0.7} | | | | | | | | Interference: | | | | | | | | 0.7 (if SCM model is | | | | used for wanted | | | | signal) | | | | | | | | β (if variable | | | | correlation model is | | | | used for wanted | | | | signal) | | +----------------------+----------------------+----------------------+ | SCPIR [dB] | 0 dB and 10 dB | | | | [SCPIR = | | | | 10log~10~(Power of | | | | stream 1/power of | | | | stream 2)] | | +----------------------+----------------------+----------------------+ | Back-off [dB] | Sensitivity: | | | | Theoretical PAR | | | | taken from TR | | | | 45.860, section 8: | | | | 3.2 dB for 8PSK, 4.7 | | | | dB for 16-QAM and | | | | 5.1 dB for 32-QAM | | | | | | | | DTS-2: 0 dB for all | | | | modulations | | | | | | | | Additional back-off | | | | based on SCPIR (as | | | | given in Table | | | | 7.2.1.1.2) in the | | | | transmit power in | | | | dual stream mode and | | | | single stream Tx | | | | diversity mode, for | | | | both sensitivity and | | | | DTS-2, to compare | | | | with single antenna | | | | transmission power. | | +----------------------+----------------------+----------------------+ | MCSs | EGPRS2-A | GMSK (MCS-1...MCS-4) | | | | | | | | 8-PSK | | | | (DAS-5...DAS-7) | | | | | | | | 16-QAM | | | | (DAS-8...DAS-9) | | | | | | | | 32-QAM | | | | (DAS-10...DAS-12) | +----------------------+----------------------+----------------------+ | | EGPRS | GMSK (MCS-1...MCS-4) | | | | | | | | 8-PSK | | | | (MCS-5...MCS-9) | +----------------------+----------------------+----------------------+ | Blind modulation | Enabled | | | detection | | | +----------------------+----------------------+----------------------+ | Blind MIMO mode | Enabled | | | detection | | | +----------------------+----------------------+----------------------+ | MCS link adaptation | Ideal | | +----------------------+----------------------+----------------------+
## 8.4 Simulation results using SCM profiles
In these simulations the channel correlation values are taken from the SCM-A
profile as described in section 6.2 and in [8]. The tap-delay settings are
taken from the following three propagation conditions:
  1. SCM-A 3 km/hr with ideal frequency hopping ([8]),
  2. TU 3 km/hr with ideal frequency hopping ([3]) and
  3. RA 130 km/hr with no frequency hopping ([3]).
As mentioned in Table 8.3.1, only the 1800 MHz frequency band is used. In case
of dual stream transmission, modulations in both streams are the same if SCPIR
is 0 dB and mixed otherwise.
The plots below show the envelope throughput with ideal link adaptation in
different scenarios mentioned above (i.e. sensitivity and DTS-2 interference
profile).
{width="3.1506944444444445in"
height="2.1708333333333334in"}{width="3.1506944444444445in"
height="2.1805555555555554in"}
> a) SCM-A 3 km/hr ideal FH b) TU3 km/hr ideal FH
{width="3.1506944444444445in" height="2.178472222222222in"}
c) RA 130 km/hr no FH
Figure 8.4.1: Sensitivity performance with SCM-A correlation, 1800 MHz,
SCPIR=0 dB
From Figures 8.4.1 (a) and (b), it can be seen that the dual stream MIMO mode
offers significant increase in throughput compared with single stream mode at
moderate and high Es/No. While this is true for the low speed scenario, at
high speed (RA 130 km/hr) (see Figure 8.4.1c), we do not see benefit of the
dual stream MIMO mode.
{width="3.1506944444444445in" height="2.175in"}{width="3.1506944444444445in"
height="2.175in"}
> a) SCM-A 3 km/hr ideal FH b) TU3 km/hr ideal FH
{width="3.1506944444444445in" height="2.175in"}
c) RA 130 km/hr no FH
Figure 8.4.2: Sensitivity performance with SCM-A correlation, 1800 MHz,
SCPIR=10 dB
From Figures 8.4.2 (a) and (b), it can be seen that, if the SCPIR is high, the
dual stream MIMO mode offers increased throughput compared with the single
stream mode only at high Es/No. If high SCPIR is combined with high speed
(e.g. RA 130 km/hr in Figure 8.4.2c), single stream MSRD mode actually
outperforms dual stream mode.
{width="3.1506944444444445in"
height="2.1708333333333334in"}{width="3.1506944444444445in"
height="2.1708333333333334in"}
> a) SCM-A 3 km/hr ideal FH b) TU3 km/hr ideal FH
{width="3.1506944444444445in" height="2.1708333333333334in"}
c) RA 130 km/hr no FH
Figure 8.4.3: DTS-2 interference performance SCM-A correlation, 1800 MHz,
SCPIR=0 dB
{width="3.1506944444444445in" height="2.175in"}{width="3.1506944444444445in"
height="2.175in"}
> a) SCM-A 3 km/hr ideal FH b) TU3 km/hr ideal FH
{width="3.1506944444444445in" height="2.175in"}
c) RA 130 km/hr no FH
Figure 8.4.4: DTS-2 interference performance in RA 130 km/hr no FH with SCM-A
correlation, 1800 MHz, SCPIR=10 dB
MIMO performance in case of DTS-2 interference scenario is similar to the
performance in sensitivity scenario as can be seen in Figures 8.4.3 and 8.4.4.
Dual stream MIMO mode offers significant increase in throughput compared with
the single stream mode at moderate and high C/I if SCPIR is low and only at
high C/I if SCPIR is high. If high SCPIR is combined with high speed (e.g. RA
130 km/hr), single stream MSRD mode actually outperforms dual stream mode.
## 8.5 Simulation results with variable channel/antenna correlation
In these simulations, the variable correlation channel model as described in
section 6.3 and in [7] is used. The tap-delaysettings are taken from the
following two propagation conditions:
  1. SCM-A 3 km/hr with ideal frequency hopping ([8]) and
  2. TU 3 km/hr with ideal frequency hopping ([3])
As mentioned in Table 8.3.1, only the 900 MHz frequency band is used. Three
different correlation settings as mentioned in Table 8.3.1 are simulated. In
order to limit the simulation effort only SCPIR of 0 dB is considered. In case
of dual stream transmission, modulations in both streams are considered to be
the same.
The plots below show the envelope throughput with ideal link adaptation in
different scenarios mentioned above (i.e. sensitivity and DTS-2 interference
profile).
{width="3.1506944444444445in"
height="2.1708333333333334in"}{width="3.1506944444444445in"
height="2.1708333333333334in"}
a) SCM-A 3 km/hr ideal FH b) TU3 km/hr ideal FH
Figure 8.5.1: Sensitivity performance in 900 MHz, SCPIR=0 dB, correlation α=0,
β=0
{width="3.1506944444444445in"
height="2.1708333333333334in"}{width="3.1506944444444445in"
height="2.1708333333333334in"}
a) SCM-A 3 km/hr ideal FH b) TU3 km/hr ideal FH
Figure 8.5.2: Sensitivity performance in 900 MHz, SCPIR=0 dB, correlation α=0,
β=0.7
{width="3.1506944444444445in"
height="2.1708333333333334in"}{width="3.1506944444444445in"
height="2.1708333333333334in"}
a) SCM-A 3 km/hr ideal FH b) TU3 km/hr ideal FH
Figure 8.5.3: Sensitivity performance 900 MHz, SCPIR=0 dB, correlation α=0.3,
β=0.7
{width="3.1506944444444445in"
height="2.1708333333333334in"}{width="3.1506944444444445in"
height="2.1708333333333334in"}
a) SCM-A 3 km/hr ideal FH b) TU3 km/hr ideal FH
Figure 8.5.4: DTS-2 interference performance 900 MHz, SCPIR=0 dB, correlation
α=0, β=0
{width="3.1506944444444445in"
height="2.1708333333333334in"}{width="3.1506944444444445in"
height="2.1708333333333334in"}
a) SCM-A 3 km/hr ideal FH b) TU3 km/hr ideal FH
Figure 8.5.5: DTS-2 interference performance in 900 MHz, SCPIR=0 dB,
correlation α=0, β=0.7
{width="3.1506944444444445in"
height="2.1708333333333334in"}{width="3.1506944444444445in"
height="2.1708333333333334in"}
a) SCM-A 3 km/hr ideal FH b) TU3 km/hr ideal FH
Figure 8.5.6: DTS-2 interference performance in 900 MHz, SCPIR=0 dB,
correlation α=0.3, β=0.7
From the figures in this section we can see that the MIMO performance in case
of variable correlation channel model is similar to the performance in SCM-A
model. Dual stream MIMO mode offers significant increase in throughput
compared with the single stream mode at moderate and high Es/No and C/I. In
case of higher correlation settings i.e. α=0.3, β=0.7, there is a slight
degradation in performance.
## 8.6 Performance Summary
_[Editor's note: This section will include a performance summary of the
results reported in sections 8.4 and 8.5.]_
## References
[8-1] GP-140335, "Downlink MIMO Simulation Assumptions for Final Performance
Evaluation", source NSN, GERAN#62.
[8-2] GP-140581, "Mode Adaptation in Downlink MIMO", source Nokia Networks,
GERAN#63.
[8-3] David Falconer, \"Frequency domain Equalisation for Single-Carrier
Broadband Wireless Systems,\" IEEE Communications Magazine, Apr. 2002, pp.
58-66.
[8-4] GP-130686 -- "MIMO Channel Model with Variable Spatial Correlation",
source NSN, GERAN#59.
# 9 Compatibility analysis
_[Editor's note: This section will investigate the impact to speech and data
performance while priority is given to avoid negative impact to legacy speech
service. Impact of the new interference type on legacy channels could be
investigated by link level simulation. It will also investigate hardware
impact due to the introduction of MIMO for Downlink to the base station and
mobile station, assuming the mobile station already supports diversity antenna
reception. Impact to BTS HW and MS HW will be analysed in separate
subsections.]_
# 10 Conclusion
_[Editor's note: This section will conclude if feasibility of MIMO for
Downlink is proven.]_
# Annex A: SCM Realization in GSM
The Spatial Channel Models can be realized for GSM simulation in the following
way.
First we generate independent Rayleigh fading waveforms as a sum-of-sinusoids
representing scatterers emanating from transmitting antenna arriving with
random but uniformly distributed phase at the receiving antenna. A modified
Jakes model can be used to achieve independence between different paths from
transmitting to receiving antennas. The sum of sinusoid is defined in the
equation below.
{width="5.259722222222222in" height="0.5416666666666666in"}
{width="2.2604166666666665in" height="0.3854166666666667in"}
{width="2.3541666666666665in" height="0.17708333333333334in"}
Here,
_t_ = sample time, i.e., from 0 to number of samples in the burst-1 multiplied
by sample duration
_L_ = number of paths between transmitting and receiving antenna (e.g. 4 in
case of 2x2 MIMO)
_K_ = number of channel taps in each path (6 in our case)
_N_ ~0~ = Number of scatterers for each tap in each path (used 200 in our
simulation)
_w~M~_ = maximum Doppler frequency=2π _v_ /_λ_
_v_ = speed of MS, _λ_ =wavelength
and for {width="3.707638888888889in" height="0.17708333333333334in"} are 2
_LKN_ ~0~ independent random phases, each of which is uniformly distributed in
[0, 2π]
{width="0.19791666666666666in" height="0.16666666666666666in"} is random
initial arrival angle which satisfies following condition
{width="2.34375in" height="0.375in"}
Once the independent Rayleigh faded waveforms are generated as above, these
are then correlated with the square-root of the polarization covariance matrix
**Г** to achieve the desired correlation between the paths. These waveforms
are then weighted according to the tap power for each tap and convolved with
the transmitted signal. Finally, appropriate scaling factors are applied to
faded signals to achieve unity power over a long periods of time.
# Annex \: Change history
* * *
**Date** **TSG #** **TSG Doc.** **CR** **Rev** **Subject/Comment** **Version**
2013-05 GERAN#58 GP-130484 First draft with document structure 0.0.1 2013-08
Telco#1 Telco#1 Second draft for DL MIMO Telco#1 submission 0.0.2 2013-11
GERAN#60 GP-130986 3^rd^ Draft for GERAN#60 submission, with added section 7.2
and 7.5 0.0.3 2013-12 GERAN#60 GP-131102 Contents of sections 7.2 and 7.5
removed to get an agreed version to start inclusion of further technical
contents. 0.1.0 2014-02 GERAN#61 GP-140128 Contents of sections 7.2 and 7.5
agreed at GERAN#60 in GP-131104 and GP-131103 respectively and now included in
this version. 0.2.0 2014-02 GERAN#61 GP-140106 Contents of sections 6.2 and
6.3 agreed at GERAN#61 in GP-140200 and included in this version. 0.3.0
2014-11 GERAN#64 GP-140991 pCR 45.871 Downlink MIMO - Performance Evaluation
0.4.0