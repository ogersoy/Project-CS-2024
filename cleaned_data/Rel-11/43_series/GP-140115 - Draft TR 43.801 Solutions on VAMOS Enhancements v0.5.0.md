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
VAMOS has been specified as a Rel-9 feature and was expected to theoretically
double the voice capacity of GERAN per BTS transceiver. Capacity gains of
VAMOS have however been seen from system level simulations to vary
significantly depending on the frequency load of the network. In networks with
relatively high frequency load the possible system capacity increase brought
by VAMOS could thus result in degraded call quality.
Call quality in the network may rely upon factors which were not
modelled/covered in the MUROS study, such as radio resource management and
interference coordination/mitigation mechanisms. Hence it is desirable to
explore standardization ways in these and/or other possible areas to optimize
the call quality of VAMOS networks.
# 1 Scope
The present document contains the results from the 3GPP study item on VAMOS
Enhancements. This includes study of the following aspects:
\- Objectives of the study.
\- Common assumptions for the evaluation of candidate techniques.
\- Candidate techniques including those that utilize network synchronization,
and further those that use inter-cell interference coordination/mitigation and
inter-cell channel state sharing in and between BSS. A candidate technique
shall support frequency hopping.
\- Evaluations of candidate techniques based on the objectives.
VAMOS enhancements will also investigate a new logical interface between BSSs
in A/Gb mode which applies to control plane only and can be utilised by VAMOS
enhancement solutions, since no logical interface between BSSs in A/Gb mode
exists in current specifications.
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
[2] 3GPP TR 41.001: \"GSM Release specifications\".
[3] 3GPP TR 45.914: \"Circuit Switched Voice Capacity Evolution for GERAN\".
# 3 Definitions, symbols and abbreviations
## 3.1 Definitions
For the purposes of the present document, the terms and definitions given in
TR 21.905 [1] and the following apply. A term defined in the present document
takes precedence over the definition of the same term, if any, in TR 21.905
[1].
Editor's note: to be added
## 3.2 Symbols
For the purposes of the present document, the following symbols apply:
Editor's note: to be added
## 3.3 Abbreviations
For the purposes of the present document, the abbreviations given in TR 21.905
[1] and the following apply. An abbreviation defined in the present document
takes precedence over the definition of the same abbreviation, if any, in TR
21.905 [1].
MUROS Multi-User Reusing One Slot
VAMOS Voice services over Adaptive Multi-user Channels on One Slot
RRM Radio Resource Management
# 4 Objectives
## 4.1 Performance Objectives
### 4.1.1 Improved Call quality
The ENHVAMOS candidate techniques shall improve the call quality of both
paired and non-paired mobiles in a VAMOS network.
## 4.2 Compatibility Objectives
### 4.2.1 Impacts to the Core Network
No implementation impacts shall be required for the core network. Any increase
of signalling load on the A interface should be avoided.
### 4.2.2 Impacts to the BSS
No implementation impacts shall be required for the BTS and BSC hardware.
Additional complexity in terms of processing power and memory should be kept
to a minimum for the BSC.
### 4.2.3 Impacts to Mobile Stations
No implementation impacts shall be required for mobile stations.
### 4.2.4 Impacts to Network Planning
The study shall take into consideration the dependency of the gains of an
ENHVAMOS candidate technique upon factors like frequency reuse, frequency
hopping mode (i.e., baseband hopping or synthesized hopping) , and level of
air interface synchronization etc.
# 5 Common Assumptions for Candidate Evaluation
## 5.1 General
The common working assumptions for the performance evaluation of ENHVAMOS
candidate techniques shall be aligned with subclause 5 of the MUROS TR [3],
except those explicitly listed in the following subclauses.
## 5.2 Air Interface Synchronization
For a candidate technique which requires network synchronization as a
precondition, the system level performance should be evaluated in synchronous
network mode. Otherwise the system level performance should be evaluated in
both synchronous network mode and asynchronous network mode.
A candidate technique should indicate the level of synchronization it relies
on, e.g. frame-based or multiframe-based, and possibly the dependency of the
gains on the synchronization accuracy.
## 5.3 Definition of Model for External Interferers for Link Level Evaluations
in Synchronous Network Mode
The link performance per each ENHVAMOS candidate technique shall be specified
for the synchronous interferer scenarios defined in the MUROS TR [3] (i.e.
MTS-1 and MTS-2), and in addition the following synchronous interferer
scenarios:
a) for a new EVTS-1 (ENHVAMOS test) scenario with synchronous interferer.
Table 5-1: ENHVAMOS Test Scenario 1 (EVTS-1) with single synchronous
interferer
+--------------+--------------+--------------+---------+--------------+ | Reference | Interfering | Interferer | TSC | Interferer | | Test | Signal | relative | | Delay range | | Scenario | | power level | | | +--------------+--------------+--------------+---------+--------------+ | 1) EVTS-1 | 1) | 1) 0 dB | 1) TBD | 1) No delay | | | Co-channel | | | | | | 1 | | | | +--------------+--------------+--------------+---------+--------------+
**whereby** Co-channel 1 is either GMSK or AQPSK modulated.
**Interference performance shall be based on C/I for single external cochannel
inteferer, where C is related to the total power of the received VAMOS signal
(i.e. carrying two VAMOS subchannels) and I to the received power of the
single external cochannel interferer.**
b) for a new EVTS-2 (ENHVAMOS test) scenario with multiple synchronous
interferers.
Table 5-2: ENHVAMOS Test Scenario 2 (EVTS-2) with multiple synchronous
interferers
+--------------+--------------+--------------+---------+--------------+ | Reference | Interfering | Interferer | TSC | Interferer | | Test | Signal | relative | | Delay range | | Scenario | | power level | | | +--------------+--------------+--------------+---------+--------------+ | 1) EVTS-2 | 1) | 1) 0 dB | 1) TBD | 1) No delay | | | Co-channel | | | | | | > 1 | 2) -10 dB | 2) TBD | 2) No delay | | | | | | | | | 2) | 3) 3 dB | 3) TBD | 3) No delay | | | Co-channel | | | | | | > 2 | 4) -17 dB | 4) - | 4) - | | | | | | | | | 3) Adjacent | | | | | | > 1 | | | | | | | | | | | | 4) AWGN | | | | +--------------+--------------+--------------+---------+--------------+
whereby Co-channel 1, Co-channel 2 and Adjacent 1 is either GMSK or AQPSK
modulated. Only configurations, where all interferers are using the same
modulation type, are considered.
**Interference performance shall be based on C/I1 for multiple external
cochannel inteferers, where C is related to the total power of the received
VAMOS signal (i.e. carrying two VAMOS subchannels) and I1 to the received
power of the dominant external cochannel interferer.**
## 5.4 Definition of Model for External Interferers for Link Level Evaluations
in Asynchronous Network Mode
The link performance per each ENHVAMOS candidate technique shall be specified
for the asynchronous interferer scenarios defined in the MUROS TR [3] (i.e.
MTS-3 and MTS-4).
## 5.5 Interference Measurement and Recording
### 5.5.1 Uplink Measurement
For the BTS the same measurement period as for the MS is assumed. RXQUAL and
RXLEV are measured.
If a candidate technique utilizes interference measurements on the UL, then
this shall be realistically modeled.
### 5.5.2 Number of Reported Cells
The definition of the number of reported cells is TBD.
The BA list shall be modeled if it is used to determine reported cells.
If the BA list is adapted by a candidate technique then this shall be modeled.
The impact of such an adaptation on handover is expected to be seen in the
speech quality.
_Editor's note: Operator and MS vendor input might be needed on the important
scenarios and the penetration of MS supporting EMR, and on whether EMR could
be utilized during call setup._
### 5.5.3 Definition of Call Set-up Phase
The maximum call set-up phase is defined as 3 seconds.
### 5.5.4 BCCH Carrier Measurements
The BCCH carrier measurement shall be modeled by re-using the approach defined
in subclause 6.5.1.2, 6.5.2 and 6.5.3 of 3GPP TR 45.926 for the MS in
connected mode. Only CS services are assumed on the BCCH carrier.
The backoff used in simulations shall be declared.
## 5.6 Network Configurations
### 5.6.1 Information Sharing at RRM Level
Three levels of information sharing are defined:
a) Level 1, where no information sharing is applied.
b) Level 2, where information sharing is applied only within the BSSs.
c) Level 3, where information sharing is applied in and between the BSSs.
### 5.6.2 Simulation Scenarios
The reference case shall be based on MUROS-1, MUROS-2 and MUROS-3 defined in
the MUROS TR [3].
If a candidate technique relies on network synchronization, it shall be
evaluated against information sharing level 2 and level 3.
### 5.6.3 BSC Area and Inter-BSC Information Exchange
To model the BSC area one BSS-to-BSS border is defined. The number of cells
next to the BSS-to-BSS border and the total number of simulated cells shall be
declared.
To model the information exchange between BSCs, an inter-BSC connection should
be defined. This is done in a vendor specific way, but the assumptions on the
inter-BSC connection shall be declared. Such assumptions shall cover
parameters e.g. delay, bandwidth and reliability.
It is expected that the ENHVAMOS study as an output will give recommendation
on the above mentioned parameters.
### 5.6.4 Impact on TCH FER due to Handover
The impact on traffic channel FER due to handover should be taken into account
for both downlink and uplink, in a vendor specific way.
## 5.7 Link-to-System Mapping
Re-use of the L2S mappings that were generated during the MUROS study (see
section 5.7 of the MUROS TR [3]) is allowed.
In the case of network synchronization the following is taken into
consideration:
a) If dynamic TSC planning methods are utilized then impact from carrier and
interferer TSC cross correlation combinations on interference shall be
modeled.
b) Otherwise an average impact (+/-) from TSC cross correlation shall be
modeled.
_Editor's note: The modeling can be done in a vendor specific manner. The
verification procedure is TBD._
## 5.8 System Performance Evaluation Method
Two system performance evaluation methods are defined:
a) To evaluate the system performance of an ENHVAMOS candidate technique in
terms of capacity gains, the system performance evaluation method defined in
section 5.5 of the MUROS TR [3] is re-used.
b) To evaluate the system performance of an ENHVAMOS candidate technique in
terms of call quality improvements,
b1) the system is first loaded with the usage of VAMOS but without the usage
of the ENHVAMOS candidate technique until the minimum call quality performance
is not any more ensured. This is treated as the reference case.
b2) the system is then loaded with the usage of both VAMOS and the ENHVAMOS
candidate technique, and with the same amount of traffic as the above
reference case.
b3) the system performance of the ENHVAMOS candidate technique in terms of
call quality improvement is then calculated by the decrease of the median
level in the CDF of average call FER.
The evaluation should be done in such a way that switching between non-VAMOS
and VAMOS channel modes based on vendor specific channel mode adaptation
thresholds shall be optimized for each channel mode adaptation type and in
addition for each network configuration as specified in Table 5-8 and Table
5-9 of the MUROS TR [3].
_Editor's note: the definition of system performance evaluation method is open
for further discussion._
## 5.9 Signalling Aspects
For any candidate technique the evaluation should include the impacts to the
signalling loads over any affected interface between network elements. Such
impacts should be taken into account when comparing candidate techniques.
# 6 Candidate Solutions
## 6.1 Coordinated Channel Allocation for VAMOS [6.1-1]
### 6.1.1 General
The proposal is based on the principles depicted in [6.1-2]. In addition to
the modulation types of the interferers, it also takes into account
interference strength. For instance, a large amount of AQPSK modulated
interferers does not necessarily contribute too much to the degradation of
speech quality if the strengths of such interferers are all very low, whilst a
single GMSK modulated interferer may significantly impact the speech quality
if its strength is sufficiently high. Frequency hopping is also considered in
radio resource allocation.
### 6.1.2 Concept Description
In a synchronized GSM network where timeslots are aligned, interferers to a
given traffic channel are limited to those sharing the same timeslot number.
So if the channel occupancy information in all interfering cells is known by
the BSC, it will be possible for the BSC to enumerate all interferers. Further
if additional information like transmission power of each interferer and
relating pathloss can also be obtained or estimated, the BSC will be able to
derive the C/I of that traffic channel. The estimated C/I reflects the quality
of a traffic channel, so it is very useful to the RRM, especially the channel
allocation algorithms.
When a traffic channel needs to be assigned as the result of call setup or
handover, a "required C/I" is first determined based on factors like the
mobile station's capability (e.g. whether it supports DARP Phase I) and the
chosen voice codec etc. The C/I of each idle traffic channel is then evaluated
and a decision is made to choose a suitable traffic channel among those
satisfying the 'required C/I".
It should be noted that the C/I estimation should take into consideration
whether the corresponding idle traffic channel, once allocated, will be in
VAMOS mode or non-VAMOS mode.
As the interferers to a given traffic channel may come from cells managed by
different BSCs, for the above idea to work it is required for BSCs to exchange
information, like TRX and timeslot configurations and channel occupancy etc,
in neighbouring cells belonging to each other.
The C/I estimation applies to both downlink and uplink, and is for users both
in VAMOS mode and non-VAMOS mode.
### 6.1.3 Frequency Hopping
Frame-based synchronization (i.e. the TDMA frame number, FN, of each cell may
not be aligned) is assumed. As FN is an input parameter in hopping sequence
generation, it is required for the BSC to know the FNOFFSET between any two
cells having overlapping MAs.
With random frequency hopping (HSN≠0), the interfering relationship between
two hopping sequences "randomly" changes at TDMA frame level, whereas with
cyclic frequency hopping (HSN=0), the interfering relationship is
deterministic. To ease the interference estimation effort it is assumed here
that cyclic frequency hopping is always used.
For example if the serving cell and the interfering cell share the same MA,
and there is a traffic channel using MAIO1 in the serving cell and another
traffic channel using MAIO2 in the interfering cell, and if the equation
holds, then the interference type is CCI.
When evaluating the C/I of an idle traffic channel, the BSC traverses all
possible MAs and MAIOs configured for the corresponding TRX and calculate the
C/I for each (MA, MAIO) combination. This is also done for all other idle
traffic channels and finally the most suitable (TRX, TSL, MA, MAIO)
combination is identified in terms of C/I.
### 6.1.4 Estimation of Pathloss
The pathloss from one cell to another can be roughly estimated by reusing the
neighbor cell measurement results which have been widely employed for handover
and power control purposes in today's BSCs. Figure 1 illustrates the downlink
case, where the mobile station in dedicated mode reports the RXLEV of neighbor
cell B to the base station, so the BSC can derive a pathloss sample from cell
B to cell A by
where BsPwr_B is the transmission power of the BCCH TRX in cell B.
{width="6.277083333333334in" height="1.6333333333333333in"}
Figure 6.1-1 Pathloss estimation by means of neighbor cell measurements
The BSC maintains a pathloss database where for a given cell the pathloss from
any interfering cell is stored and can be retrieved whenever needed.
The reported RXLEV for cell B may vary to some extent in different MR samples.
The BSC may store a filtered (e.g. running average of) pathloss in the
pathloss database.
It should be noted that the BA list in dedicated mode are normally configured
for handover purpose, so chances are it does not cover any of the interfering
cells. To allow sampling the RXLEV of interfering cells, the BSC should take
these cells into consideration when generating the dedicated mode BA list.
With normal measurement reports the number of reported RXLEVs is 6, which may
not be sufficiently large to include those of interfering cells of interest.
But this is not believed to be a big problem, as the pathloss database stores
long-term estimates of pathlosses between interfering cells, so it does not
require having relevant RXLEV samples in every MR sample.
If there exists mobile stations that support EMR, more cells can be reported
by such mobiles, thus it is easier for the BSC to build up the pathloss
database.
### 6.1.5 Estimation of C/I
The "C/I" of an idle traffic channel here is the C/I of that channel assuming
it has been assigned to a mobile station. The BSC knows exactly the initial
power that will be assigned to that channel so there is a "C" even for an idle
traffic channel. (Note that this is not the C/I as perceived by the mobile
station)
The interference strength is obtained by subtracting the transmission power of
the interferer and the estimated pathloss from the interfering cell to the
serving cell. The "I" is then calculated by applying the relating attenuation
factor to each interferer (assuming for instance GMSK CCI as the reference)
before taking the sum.
When a VAMOS pair acts as an interference source, in downlink it can be
modeled as one interferer with the modulation type set to AQPSK, and in uplink
it can be viewed as comprising two separate GMSK modulated interferers.
### 6.1.6 Channel Allocation
The selection of a radio channel for TCH assignment is based on the CIR
estimation for both downlink and uplink.
### 6.1.7 Inter-BSC Information Exchange
As mentioned above, to allow accurate estimation of C/I, two BSCs managing
mutually interfering cells need to exchange cell configuration and call
information of the affected cells.
Cell configuration information should include e.g. the transmission power of
all active timeslots, the MA configuration, and TRX and timeslot configuration
etc.
The information for each ongoing call should include e.g. the MA, MAIO, speech
codec, and the MS capability etc.
### 6.1.8 References
[6.1-1] GP-111597, "Coordinated Channel Allocation for VAMOS", Huawei
Technologies Co., Ltd., ZTE Corporation, 3GPP GERAN#52.
[6.1-2] GP-100619, "VAMOS system performance optimization by a coordinated RRM
method", China Mobile Com. Corporation, 3GPP GERAN#46.
# 7 Link Level Studies
## 7.1 Investigations by Telefon AB LM Ericsson as Input to Link-to-System
Modelling [7.1-1]
### 7.1.1 General
The purpose of subclause 7.1 is to provide some details on the dependency
between DL receiver performance and carrier/interferer TSC allocation and how
this dependency is affected by
a) Delay between carrier and interferer.
b) The relative strength between interferers.
c) The number of interferers.
### 7.1.2 Simulation Assumptions
General simulation assumptions are presented in Table 7.1-1.
Table 7.1-1 Simulation assumptions.
+-------------------------+-----------------------------+ | > Simulation parameters | | +-------------------------+-----------------------------+ | Band | 900 | +-------------------------+-----------------------------+ | Link | DL | +-------------------------+-----------------------------+ | Receiver | DARP Phase I | +-------------------------+-----------------------------+ | Carrier modulation | GMSK | +-------------------------+-----------------------------+ | Interferer modulation | GMSK | +-------------------------+-----------------------------+ | Channel | TU3 | +-------------------------+-----------------------------+ | Frequency hopping | Ideal | +-------------------------+-----------------------------+ | Frequency band | 900 | +-------------------------+-----------------------------+ | Tx filter | LinGMSK | +-------------------------+-----------------------------+ | Codec | AHS5.90 | +-------------------------+-----------------------------+ | Frames | 20000 | +-------------------------+-----------------------------+ | Tx/Rx impairments | Typical | +-------------------------+-----------------------------+ | Burst misalignment | 0, 5 or 10 symbols | +-------------------------+-----------------------------+ | TSC carrier | TSC set 1 | +-------------------------+-----------------------------+ | TSC interferer | Random bit, TSC set 1 and 2 | +-------------------------+-----------------------------+ | DTX | No | +-------------------------+-----------------------------+
### 7.1.3 Single Co-channel Interferer with No Delay
Figure 7.1-1 below shows the performance for a TCH/AHS5.90 carrier, assigned
TSC 5 from Set 1, when exposed to synchronous co-channel interference (CCI)
assigned one of the 16 TSCs found in TSC set 1 and 2, relative the performance
when exposed to synchronous CCI using random bits in the TSC. The depicted
relative performance is defined as gain/loss in dB at 1% FER, which is
believed to correspond to typical operating conditions for TCH/AHS5.90.
It shall be noted that for the case when both carrier and interferer was
allocated TSC 5 from set 1 the 1% FER target was not meet in the simulated CCI
range. This point is hence excluded in Figure 7.1-1.
{width="3.2944444444444443in" height="2.3159722222222223in"}
Figure 7.1- Relative CCI performance for TCH/AHS5.90 in synchronous networks
with carrier allocated TSC 5 from set 1.
As Figure 7.1-1 only represents a single carrier TSC allocation, the
simulation was repeated eight times with the carrier allocated TSC 1 to TSC 8
from set 1. The left subplot of Figure 7.1-2 depicts the full set of simulated
points while the right subplot depicts and the best, worst and average
performance identified for each simulated carrier and interferer TSC
combination.
* * *
{width="2.8in" height="1.9743055555555555in"} {width="2.8625in"
height="1.93125in"}
* * *
Figure 7.1-2 Relative CCI performance for TCH/AHS5.90 in synchronous networks
with carrier allocated TSC 1-8 from set 1.
It is clear from the results depicted in Figure 7.1-1 and Figure 7.1-2 that a
large spread in end user performance can be expected in a synchronous network
if not great care is taken when TSC planning the network. However, it is also
clear that the new TSC set 2 for VAMOS can bring additional gains compared to
both TSC Set 1 and using random bits in the interferer.
### 7.1.4 Single Co-channel Interferer with Delay
There are different ways to achieve network synchronization, but it can be
assumed that no synchronization algorithm is perfect, and also that
propagation delays will cause delay between carrier and dominant interferer as
depicted in Figure 7.1-3.
Figure 7.1-3 Delay between carrier and interfering burst.
The simulation presented in Figure 7.1-2 was repeated with a delay introduced
between carrier and interferer. To facilitate a comparison between the
simulated results, the reference point used in Figure 7.1-1 and Figure 7.1-2
was reused in Figure 7.1-4 where the best, worst and average performance is
depicted for each simulated carrier and interferer TSC combination. Results
are presented in the left subplot for a delay of 5 symbols and in the right
subplot a delay of 10 symbols.
It should be noted that the power of the interferer was compensated for the
delay introduced, to conserve the interfering power.
* * *
{width="2.85625in" height="2.0506944444444444in"} {width="2.932638888888889in"
height="2.040277777777778in"}
* * *
Figure 7.1-4 Relative CCI performance for TCH/AHS5.90 in synchronous networks
with a delay of 5 or 10 symbols between carrier and interferer.
When comparing the results presented in Figure 7.1-2 with the results shown in
Figure 7.1-4, it is seen that the spread in performance is decreasing, but
still significant, as the delay is introduced and increases to 10 symbols.
It needs to be emphasized that delays of around 10 symbols or more will
introduce effects related to asynchronous networks, for example the
possibility of being interfered by two bursts from the same base station and
ARFCN.
Figure 7.1-5. Carrier and two interfering bursts.
### 7.1.5 Two Co-channel Interferers
The receiver performance of SAIC mobiles is known to be dependent on the
number of interfering signals and their relative strength. It can be expected
that the strongest interferer in a set of interferers will have a dominant
impact on performance and must be accurately modeled in a system simulator L2S
interface. It is however also of interest to consider how a weak interferer
will influence DL receiver performance.
The right subplot of Figure 7.1-6 depicts the DL performance of the
interference scenario shown in the left subplot, relative the performance when
random bits are used as TSC in the non-dominant interferer. The dominating
interferer is always allocated the same fixed TSC, also when random bits are
used for the weaker interferer, while the weaker interferer is allocated a TSC
from set 1 or set 2 according to the x-axis of Figure 7.1-6.
The depicted relative performance is again defined as gain/loss in dB at 1%
FER. Results are presented for a relative power of 4, 8, 12 and 16 dB between
the stronger and weaker interferer.
* * *
{width="2.5965277777777778in" height="1.0916666666666666in"}
{width="3.0381944444444446in" height="2.142361111111111in"}
* * *
Figure 7.1-6 Dual CCI scenario performance.
It can be concluded from Figure 7.1-6 that the performance is closely
dependent on the TSC allocated to the weaker interferer. The dependency
decreases slowly as the relative power between the two interferers increases.
### 7.1.6 Multiple Interferers
Subclauses 7.1.4 and Figure 7.1-6 indicated that DL receiver performance is
dependent not only on the dominant interferer, but also to a large extent to
the configuration of a second weaker interferer. To investigate the impact on
performance from a third co-channel interferer the performance of the three
interferer scenarios depicted in Figure 7.1-7 was simulated.
{width="5.7375in" height="1.2347222222222223in"}
Figure 7.1-7 Single and multiple CCI scenarios.
Figure 7.1-8 depicts the DL performance of the interference scenarios shown
above, when the weakest co-channel interferer is allocated a TSC from set 1 or
set 2 according to the x-axis of Figure and the strongest interferers are
allocated fixed TSCs. The presented performance is derived relative the
performance when random bits are used as TSC in all interferers.
It can be concluded that the allocation of TSC to the weakest interferer has a
clear impact on performance in the single and double interferer scenarios,
while for the multiple interferer scenario, with three interferers, it is
observed that the spread in performance is limited.
{width="3.0194444444444444in" height="2.1840277777777777in"}
Figure 7.1-8 Multiple CCI interferer scenario performance.
### 7.1.7 References
[7.1-1] GP-120598, "Aspects of synchronous interference", Telefon AB LM
Ericsson, 3GPP GERAN#54.
## 7.2 Investigations by Huawei Technologies Co., Ltd. [7.2-1]
### 7.2.1 Methodology
The L2S mapping tables generated for the MUROS study (see [7.2-2]) were
reused.
To model the impacts of TSC correlation in synchronous networks, a correction
table for CIR was derived from link level simulations. The table translates
the following inputs to a Delta CIR:
a) Carrier modulation (GMSK or AQPSK).
b) Carrier training sequence or training sequence pair.
c) SCPIR (-4, 0 or 4 dB, in case the carrier modulation was AQPSK).
d) Dominant interferer modulation (GMSK or AQPSK).
e) Dominant interferer training sequence or training sequence pair. The SCPIR
of an AQPSK interferer was always assumed to be 0 dB.
In system simulations, the Delta CIR was provided to the simulator to correct
the "raw" CIR before it was fed to the normal CIR to FER lookup procedure.
Only SAIC receivers were assumed in the L2S model.
### 7.2.2 Limitations on TSC Assignment
For paired users a TSC pair was defined as (TSC x from TSC Set 1, TSC x from
TSC Set 2), x = 0, 1, ..., 7.
For non-paired users a TSC chosen from TSC Set 1 was always assumed. The
restriction imposed on system level simulations is that when leaving a VAMOS
pair, a user who was formerly allocated TSC x from TSC Set 2 had to change the
TSC to TSC x from TSC Set 1.
### 7.2.3 Verification
#### 7.2.3.1 Basic Assumptions
The simulation assumptions are summarized in Table 7.2-1.
Table 7.2-1: Simulation assumptions
* * *
**Parameter** **Value** Propagation Environment TU Terminal speed 3 km/h
Frequency band 900 MHz Frequency hopping Ideal Interference/noise MTS-1, MTS-2
Antenna diversity No Receiver type SAIC Tx pulse shape Linearized GMSK
Training sequence TSC 0, 1, 2, 3, 4 from TSC Set 1, TSC pair 0, 1, 2, 3, 4
SCPIR 0 dB, -4 dB, 4 dB Interference modulation GMSK, AQPSK (SCPIR = 0 dB)
* * *
#### 7.2.3.2 Results
The verification was performed for both MTS-1 and MTS-2, with SCPIRs of -4, 0
and 4 dB. Some verification results are shown in Figure 7.2-1 through Figure
7.2-3, where "Sim" and "Ver" stand for the link level simulation results and
the verification results based on the mapping tables, respectively. Some
modelling errors are summarized in Table 7.2-2.
{width="5.833333333333333in" height="4.375in"}
Figure 7.2-1. MTS-1, GMSK carrier (TSC 0), QPSK interference (TSC pair
1/2/3/4)
{width="5.833333333333333in" height="4.375in"}
Figure 7.2-2. MTS-2, QPSK carrier (TSC pair 0), QPSK interference (TSC pair 1)
{width="5.833333333333333in" height="4.375in"}
Figure 7.2-3. MTS-2, QPSK carrier (TSC pair 0), QPSK interference (TSC pair 2)
Table 7.2-2: Summary of modelling errors
* * *
**Interferer profile** **Carrier modulation** **Carrier SCPIR (dB)** **Carrier
TSC or TSC pair** **Dominant interferer modulation** **Dominant interferer TSC
or TSC pair** **Modeling error (dB)** MTS-1 GMSK - 0 QPSK 1 0.89 MTS-1 GMSK -
0 QPSK 2 0.89 MTS-1 GMSK - 0 QPSK 3 0.77 MTS-1 GMSK - 0 QPSK 4 0.96 MTS-2 QPSK
-4 0 QPSK 1 0.75 MTS-2 QPSK 0 0 QPSK 1 0.57 MTS-2 QPSK 4 0 QPSK 1 0.63 MTS-2
QPSK -4 0 QPSK 2 0.68 MTS-2 QPSK 0 0 QPSK 2 0.63 MTS-2 QPSK 4 0 QPSK 2 0.46
MTS-2 QPSK -4 0 QPSK 3 0.85 MTS-2 QPSK 0 0 QPSK 3 0.80 MTS-2 QPSK 4 0 QPSK 3
0.23 MTS-2 QPSK -4 0 QPSK 4 0.66 MTS-2 QPSK 0 0 QPSK 4 0.69 MTS-2 QPSK 4 0
QPSK 4 0.57 MTS-2 QPSK -4 1 QPSK 0 0.48 MTS-2 QPSK 0 1 QPSK 0 0.63 MTS-2 QPSK
4 1 QPSK 0 0.57 MTS-2 QPSK -4 1 QPSK 2 0.70 MTS-2 QPSK 0 1 QPSK 2 0.86 MTS-2
QPSK 4 1 QPSK 2 0.74 MTS-2 QPSK -4 1 QPSK 3 0.55 MTS-2 QPSK 0 1 QPSK 3 0.91
MTS-2 QPSK 4 1 QPSK 3 0.57 MTS-2 QPSK -4 1 QPSK 4 0.62 MTS-2 QPSK 0 1 QPSK 4
0.86 MTS-2 QPSK 4 1 QPSK 4 0.69 MTS-2 QPSK -4 2 QPSK 0 0.28 MTS-2 QPSK 0 2
QPSK 0 0.86 MTS-2 QPSK 4 2 QPSK 0 0.34 MTS-2 QPSK -4 2 QPSK 4 0.88 MTS-2 QPSK
0 2 QPSK 4 0.69 MTS-2 QPSK 4 2 QPSK 4 0.17 MTS-2 QPSK -4 4 QPSK 0 0.86 MTS-2
QPSK 0 4 QPSK 0 0.74 MTS-2 QPSK 4 4 QPSK 0 0.40 MTS-2 QPSK -4 4 QPSK 2 0.59
MTS-2 QPSK 0 4 QPSK 2 0.74 MTS-2 QPSK 4 4 QPSK 2 0.34
* * *
It can be seen that there is a good match between the verified and simulated
link performance. In most cases the difference is within 0.3 dB. In other
cases the difference could be up to 0.9 dB.
### 7.2.4 References
[7.2-1] GP-130995, "Link to System Modelling and Verification for ENHVAMOS
(update of GP-130429)", Huawei Technologies Co., Ltd., 3GPP GERAN#60.
[7.2-2] GP-081024, "L2S mapping method for power imbalanced MUROS update",
Huawei Technologies Co., Ltd., 3GPP GERAN#39.
# 8 System Level Studies
## 8.1 Investigations by Huawei Technologies Co., Ltd. [8.1-1]
### 8.1.1 Link to system mapping
The L2S methodology can be found in section 2 of [8.1-3].
### 8.1.2 TSC planning and assignment
A TSC pair was defined as TSC x from TSC Set 1 combined with TSC x from TSC
Set 2, x = 0, 1, ..., 7.
TSC pairs were statically planned on a per cell basis. TSC re-use was assumed
to be 2/6 (TSC pairs 0 to 5 were used in the simulations).
Due to a restriction in the L2S methodology, for non-paired users a TSC chosen
from TSC Set 1 was always assumed. If an MS in a VAMOS pair was assigned TSC x
from TSC Set 2, the TSC was automatically changed to TSC x from TSC Set 1 in
the simulator when the MS left that VAMOS pair.
### 8.1.3 Simulation assumptions
The simulation assumptions are summarized in Table 8.1-1. VAMOS was enabled in
all simulations, with 100% VAMOS I mobile penetration.
In the Coordinated Channel Allocation case, for each cell the BSC was assumed
to know the following configurations of all its interfering cells: BCCH output
power, number of TRXs, timeslot configuration for each TRX, MA configuration.
Further, for each traffic channel the BSC was assumed to know the transmission
power and measurement reports of each ongoing call in all its interfering
cells. The channel allocation policy outlined in [8.1-2] was used, replacing
the one in the reference case which merely allocates a randomly chosen idle
traffic channel.
Table 8.1-1. Simulation assumptions
+----------------------+----------------------+----------------------+ | **Parameter** | **Value** | **Comment** | +----------------------+----------------------+----------------------+ | Type of measurement | MR (MEASUREMENT | | | report | REPORT) | | +----------------------+----------------------+----------------------+ | Number of reported | 6 | | | cells | | | +----------------------+----------------------+----------------------+ | BCCH carrier | See subclause 5.5.4 | | | measurements | of [8.1-4] | | +----------------------+----------------------+----------------------+ | Information sharing | Intra-BSS | Only one BSC was | | | | modelled (i.e. | | | | information sharing | | | | level 2 as defined | | | | in subclause 5.6.1 | | | | of [8.1-5]) | +----------------------+----------------------+----------------------+ | Simulation scenario | MUROS-1, but only 2 | Same as the one used | | | TCH TRX's were | in [8.1-6]. | | | configured for each | | | | cell. MUROS-2. | | +----------------------+----------------------+----------------------+ | Traffic load | For both the | See [8.1-7] for | | | reference case and | the definition of | | | the Coordinated | minimum call quality | | | Channel Allocation | performance. | | | case, the traffic | | | | load was increased | | | | until the minimum | | | | call quality | | | | performance is not | | | | any more ensured. | | +----------------------+----------------------+----------------------+ | Loss of speech | 6 frames | | | frames due to | | | | Handover | | | +----------------------+----------------------+----------------------+ | BCCH or TCH under | TCH | | | interest | | | +----------------------+----------------------+----------------------+ | Frequency hopping | Random frequency | | | | hopping for the | | | | reference case. | | | | | | | | Cyclic frequency | | | | hopping for the | | | | Coordinated Channel | | | | Allocation case. | | +----------------------+----------------------+----------------------+ | Network sync mode | Frame-based | No delay was | | | synchronization | assumed. | +----------------------+----------------------+----------------------+ | Channel mode | D1: AHS 5.9 \ | The channel mode | | adaptation | MUROS (AHS 5.9) | adaptation | | | | thresholds were | | | | optimized for | | | | maximum capacity. | +----------------------+----------------------+----------------------+ | Fast fading type | TU-3 | | +----------------------+----------------------+----------------------+ | Network size | 96 cells for | | | | MUROS-1. | | | | | | | | 81 cells for | | | | MUROS-2. | | +----------------------+----------------------+----------------------+ | Simulation direction | Downlink | | +----------------------+----------------------+----------------------+ | Simulation time | 900 seconds | | +----------------------+----------------------+----------------------+
### 8.1.4 Simulation Results
The capacity (in EFL), call drop rate and handover failure rate are summarized
in Table 8.1-2, 8.1-3, and 8.1-4, respectively.
It can be seen that with Coordinated Channel Allocation, the capacity gains
are very good in the investigated tight reuse network configuration (i.e.
MUROS-1), but are not obvious in the investigated loose reuse network
configuration (i.e. MUROS-2). The major reason is that, the amount of data
collected by the RRM is not always sufficient to reflect the actual
interference level in a cell; hence the interference management and avoidance
method can only perform rough channel quality estimation, which is more likely
to be correct in networks dominated by high interference levels.
Table 8.1-2. Capacity (in EFL) (%)
* * *
                                   **Modified** **MUROS-1**   **MUROS-2**
Reference 31 24 Coordinated Channel Allocation 34.3 24.7 Difference (%) +10.7
+2.9
* * *
Table 8.1-3. Call drop rate (%)
* * *
                                   **Modified** **MUROS-1**   **MUROS-2**
Reference TBD TBD Coordinated Channel Allocation TBD TBD Difference (%) TBD
TBD
* * *
Table 8.1-4. Handover failure rate (%)
* * *
                                   **Modified** **MUROS-1**   **MUROS-2**
Reference TBD TBD Coordinated Channel Allocation TBD TBD Difference (%) TBD
TBD
* * *
### 8.1.5 References
[8.1-1] GP-130997, " Updated System Performance Evaluation for Coordinated
Channel Allocation", Huawei Technologies Co., Ltd, GERAN #60.
[8.1-2] GP-111597, "Coordinated Channel Allocation for VAMOS", Huawei
Technologies Co., Ltd, ZTE Corporation, GERAN #52.
[8.1-3] GP-130995, "Link to System Modelling and Verification for ENHVAMOS
(update of GP-130429)", Huawei Technologies Co., Ltd, GERAN #60.
[8.1-4] GP-120636, "Draft 3GPP TR 45.926 V0.7.0 on Solutions for GSM/EDGE BTS
Energy Saving", SI Rapporteur, GERAN #54.
[8.1-5] GP-130544, "Draft TR 43.801 Solutions on VAMOS Enhancements v0.4.1",
SI Rapporteur, GERAN #58.
[8.1-6] GP-100104, "System Performance Evaluation for Repeated SACCH and
Shifted SACCH", Huawei Technologies Co., Ltd, GERAN #45.
[8.1-7] 3GPP TR 45.914 V9.5.0, "Circuit switched voice capacity evolution for
GSM/EDGE Radio Access Network (GERAN)".
#