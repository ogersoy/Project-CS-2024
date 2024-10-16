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
_The present document captures the results of the feasibility study on Mobile
data applications for GERAN._
# 1 Scope
The present document contains the results from the feasibility study on
efficient support of mobile data applications for human communications in
GERAN.
The following aspects shall be covered in the study:
\- Analysis on relevant traffic profiles from GERAN perspective for the mobile
data applications of human communications
\- Analysis on the impacts on GERAN network based on the identified traffic
profiles
\- GERAN enhancements to alleviate these impacts with regards to: Radio
resource utilization; signalling procedures; RR states and transition between
them and Battery lifetime
\- Common assumptions on simulations and evaluations for candidate solutions
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
[3] 3GPP TR 22.801: \"Study on non-MTC Mobile Data Applications impacts\".
[4] 3GPP TR 43.868: "GERAN Improvements for Machine-type Communications".
[5] 3GPP TR30.03U: "Selection procedures for the choice of radio transmission
technologies of the UMTS".
[6] Anderlind Erik and Jens Zander \" A Traffic Model for Non-Real-Time Data
Users in a Wireless Radio Network\" IEEE Communications letters. Vol 1 No. 2
March 1997.
[7] Miltiades E et al. "A multiuser descriptive traffic source model" IEEE
Transactions on communications, vol 44 no 10, October 1996.
# 3 Definitions, symbols and abbreviations
## 3.1 Definitions
For the purposes of the present document, the terms and definitions given in
TR 21.905 [1] and the following apply. A term defined in the present document
takes precedence over the definition of the same term, if any, in TR 21.905
[1].
**example:** text used to clarify abstract rules by applying them literally.
## 3.2 Symbols
For the purposes of the present document, the following symbols apply:
\ \
## 3.3 Abbreviations
For the purposes of the present document, the abbreviations given in TR 21.905
[1] and the following apply. An abbreviation defined in the present document
takes precedence over the definition of the same abbreviation, if any, in TR
21.905 [1].
GERANEMDA GERAN Enhancements for Mobile Data Applications
HTTP Hypertext Transfer Protocol
IM Instant Message
MDA Mobile Data Applications
> MS Mobile Station
>
> WAP Wireless Application Protocol
>
> UDD Unconstrained Delay Data bearer service
# 4 Objectives
## 4.1 General
The general objectives of this study is to make the GERAN network better
suited for mobile data applications used on multi-tasking capable mobile
stations, e.g. IM chatting, HTTP/WAP browsing services (including streaming),
social network services, etc , this study aims to consider the following
objectives:
  * Study and identify the relevant traffic profiles from GERAN > perspective for the mobile data application of human > communication, e.g. IM chatting, HTTP/WAP browsing (including > streaming), social network service, etc.
  * Study the impact on GERAN network based on the identified traffic > profiles.
  * Study enhancements to alleviate the impacts from these traffic > patterns on the current GERAN networks (if any)
## 4.2 Performance Objectives
The candidate enhancements aiming at alleviating the identified impacts should
consider the following performance objectives. When evaluating the candidate
enhancements, the relative performance gains should be evaluated by comparing
to the reference scenario for which the common assumptions are described in
section 6.
  * Improve radio resource utilization
  * Reduce signalling procedures
  * Minimize the impact on RR states and reduce the transition between > them
  * Reduce the impact on battery lifetime
_[Editor's note: the measurement metric on mobile battery life should be
simple and easy for solution evaluation and detailed metric for MS battery
life is FFS.]_
## 4.3 Compatibility Objectives
The candidate enhancements aiming at solving the identified problems should
consider the following compatibility objectives:
  * Avoid impacts on existing BTS and BSC hardware:
\- This will enable use of already existing hardware and only require a
software upgrade.
  * Be based on the existing network architecture and minimal impact on > core network:
```{=html}
``` \- This will enable an operator to re-use existing network nodes.
```{=html}
``` \- Minimize the impacts on mobile station.
# 5 Analysis on mobile data applications and their impacts on GERAN system
## 5.1 General
In recent years, mobile networks have experienced a significant increase of
mobile data. Diverse mobile applications are introduced by machine type
communication and human type communication. The increase of mobile data has
introduced new challenges to mobile networks.
As the usage and range of applications used today for human communication, the
total amount of related traffic and signalling is increasing significantly,
the transitions of RR states may happen frequently, and the mobile battery
life may also be impacted.
Sub-section 5 captures the study on the traffic characters for the relevant
mobile data applications with considering the use cases in TR22.801 [3] under
SA1 study item- MODAI, and analyzes the impacts on GERAN system.
## 5.2 Use case
### 5.2.1 Frequent Small Packet Transmission
#### 5.2.1.1 Description and Analysis
As described in sec 5.1 in TR22.801 [3], a typical character of a lot of
popular mobile applications is production of frequent small packets which is
different comparing legacy Web browsing service. And the trend of small
packets is expected to be exacerbated as status messages, location messages,
instant messages, and keep alives etc.
One typical small packet application is IM because IM produces a lot of small
packets and the interval between two packet bursts is short. A traffic model
in section 6.3.2 describes the traffic characteristics analyzed for IM
application.
_[Editor's note: This section provides the description and the analysis on the
traffic profile and impacts on GERAN system of relevant mobile data
application._
#### 5.2.1.2 Aspects of required improvements
_[Editor's note: This section provides the analysis on the impacts on GERAN
system and aspects required improvements.]_
### 5.2.2 \
## 5.3 Conclusion for analysis
# 6 Common assumptions
## 6.1 Simulation assumptions
### 6.1.1 General
This section defines the reference scenario and parameters required for the
simulations. The simulation assumptions in this study exclude the function,
which means the BSC is not aware of the service or application type. And
evaluation of CS service on the TCH and SDCCH is not required under this
study. The simulator methodology and the simulation parameters shall be
aligned with those defined in section 6.2.1 and 6.2.2 in TR 43.868 [4] for
SIMTC study, except those explicitly listed in the following sections.
### 6.1.2 Simulator methodology
In order to evaluate the impacts introduced by the mobile data applications, a
reference network scenario should be defined for GERANEMDA study. Moreover,
the reference network scenario allows for the comparison of relative
performance gains in regard to this scenario and it is needed for the
evaluation of any enhancements studied as part of GERANEMDA and possibly also
for the objective setting of GERANEMDA.
It should be noted that the reference network scenario does not include any
Rel-7 (e.g. EGPRS-2, LATRED and etc.) or later (e.g. DTR) features. But it is
not intended to exclude these features from GERANEMDA studies. On the
contrary, the relevant Rel-7 and later features should be studied if similar
enhancements are proposed. It is useful for GERANEMDA study to compare the
performance of the network against the proposed reference network scenario.
Simulation parameters for the reference network scenario are defined in
section 6.1.3.
### 6.1.3 Simulation Parameters
This section defines the parameters required for the simulations which may be
required to conduct the study. The parameters are referenced where
appropriate.
> Table 1. Network level simulator parameters
+-----------------+-----------------+----------+-----------------+---+ | **Parameter** | **Value** | **Unit** | **Comment** | | +-----------------+-----------------+----------+-----------------+---+ | Sectors per | 3 | | | | | site | | | | | +-----------------+-----------------+----------+-----------------+---+ | Sector antenna | 65º deg | dBi | 18 dBi antennas | | | pattern | H-plane,\ | | in 900‑band are | | | | max TX gain 15 | | large and not | | | | | | considered to | | | | | | be common in | | | | | | urban areas. | | +-----------------+-----------------+----------+-----------------+---+ | Path loss model | Per 30.03, | dB | In urban areas, | | | | | | 5 m over | | | | Hb = 5 m, | | average roof | | | | | | height is | | | | | | considered more | | | | | | typical than | | | | | | the default | | | | | | value of 15 m | | | | | | in 30.03. | | +-----------------+-----------------+----------+-----------------+---+ | Minimum | 64 | dB | 1800: TR 25.942 | | | coupling loss | | | 2 GHz. | | | | | | | | | | | | 900: assumed 6 | | | | | | dB lower | | +-----------------+-----------------+----------+-----------------+---+ | Interference | Neighbouring | | The | | | model | cells BCCH | | neighbouring | | | | | | cells according | | | | | | to the BCCH | | | | | | frequency reuse | | | | | | pattern are | | | | | | modelled as if | | | | | | they have full | | | | | | traffic. | | +-----------------+-----------------+----------+-----------------+---+ | Log-normal | Standard | 8 | dB | | | fading | deviation | | | | +-----------------+-----------------+----------+-----------------+---+ | | Correlation | 110 | M | | | | distance | | | | +-----------------+-----------------+----------+-----------------+---+ | Channel | See table 4 | | | | | propagation | | | | | +-----------------+-----------------+----------+-----------------+---+ | Output power | 33 | dBm | Excluding | | | | | | backoff | | | - MS | 43 | | | | | | | | | | | - BTS | | | | | +-----------------+-----------------+----------+-----------------+---+ | Backoff | 6 | dB | | | | | | | | | | - MS | | | | | +-----------------+-----------------+----------+-----------------+---+ | - BTS | 4 | dB | 8PSK modulation | | | | | | assumed. | | +-----------------+-----------------+----------+-----------------+---+ | Noise figure | 10 | dB | | | | | | | | | | - MS | | | | | +-----------------+-----------------+----------+-----------------+---+ | - BTS | 8 | dB | | | +-----------------+-----------------+----------+-----------------+---+ | Inter-site | 0 | | Low correlation | | | log-normal | | | in urban | | | correlation | | | scenarios. | | | coefficient | | | | | +-----------------+-----------------+----------+-----------------+---+
> Table 2. Network scenario
* * *
**Parameter** **Value** **Unit** **Comment** Frequency band 900 MHz  
Cell radius 500 m  
Bandwidth 4.2 MHz  
Number of frequency channels 21  
BCCH frequency reuse 4/12  
TCH frequency reuse 3/9  
BCCH or TCH under interest BCCH and TCH No power control and no frequency
hopping on both BCCH carrier and TCH carrier
* * *
> Table 3. Protocol level parameters
+----------------------+----------------------+----------------------+ | **Parameter** | **Value** | **Comment** | +----------------------+----------------------+----------------------+ | CCCH assumptions | 20 | These default values | | | | shall be included | | - Tx-integer | 109 | among those | | | | evalutated. | | - S | 4 | | | | | See 3GPP TS 44.018 | | - Max. retrans (M) | 5 sec. | for implementation | | | | details | | - T3142 | (Tx+2S)/217=1.1 sec. | | | | | | | - T3146 | | | +----------------------+----------------------+----------------------+ | BCCH configuration | Non-combined | | +----------------------+----------------------+----------------------+ | # PDCHs | 8 | Number of PDCHS | | | | availabale data | | | | traffic. 4 PDCHs are | | | | allocated on BCCH | | | | carrier, and 4 PDCHs | | | | are allocated on the | | | | TCH carrier. | +----------------------+----------------------+----------------------+ | # AGCHs per | 6 | | | 51-multiframe | | | +----------------------+----------------------+----------------------+ | PDCH Resource | MS multislot class | | | Assignment | 12 (BTTI) | | +----------------------+----------------------+----------------------+ | Link adaptation | Enabled | | +----------------------+----------------------+----------------------+ | Service type | 1. EGPRS | | +----------------------+----------------------+----------------------+ | RLC mode of | Acknowledged Mode | | | operation | (AM) | | +----------------------+----------------------+----------------------+
> Table 4. Link specific settings.
* * *
**Parameter** **Value** **Comment** Channel profile TU3  
Receiver type UL MRC  
Incremental redundancy Enabled
* * *
LLC PDU life time is a simulation parameter which defines the maximum time a
downlink LLC PDU can be buffered. This simulation parameter should be reported
with any other parameters not listed in this section and used in simulations.
## 6.2 Evaluation requirements
### 6.2.1 General
In order to evaluate the impacts on GERAN network and compare the GERAN
network performance of different enhancements for different traffic profiles,
network metrics and service metrics should be used to measure GERAN network
performance. The network performance metrics are required and common for all
traffic models, while service performance metrics are defined for each
relevant traffic model separately.
### 6.2.2 Network Metrics
Following network metrics are used to measure the network performance.
  * **Data load** \-- defines how much PDCH resources have been utilized > for data transmissions during a simulation in average in each > direction. The transmissions include blocks on PDTCH and PACCH. > The formula bellow defines the data load per the direction.
> {width="1.8854166666666667in" height="0.34375in"}
>
> Where _DataBLK~Tx~_ is the number of BTTI blocks transmitted during the
> simulation and _DataBLK~Total~_ is the number of all available BTTI blocks.
> _DataBLK~Tx~_ counts all transmitted BTTI blocks on PDCH, i.e. all blocks
> transmitted on PDTCH and PACCH including dummy blocks. _DataBLK~Total~_ can
> be computed from the simulation time _T_ measured in seconds and _N~PDCH~_ ,
> which is the number of PDCHs available for data traffic (i.e. dedicated to
> PS traffic).
>
> {width="1.5729166666666667in" height="0.3333333333333333in"}
>
> It should be noted that the equations above express the data load in the
> downlink direction only. The same equations can be used to calculate the
> data load in the uplink in which case the number of blocks received by the
> network is used.
  * **Control load** \-- defines how much of system resources have been > utilized for signalling on AGCH and PCH during a simulation.
> {width="2.21875in" height="0.34375in"}
>
> Where _ControlBLK~Tx~_ is the number of control blocks transmitted during
> the simulation, excluding L2 fill frames and paging blocks with no MS
> identity, and _ControlBLK~Total~_ is the number of all available AGCH and
> PCH blocks. If (preventive) repetitions of immediate assignment messages and
> repeated paging requests are simulated then those messages should be counted
> in the control load. _ControlBLK~Total~_ can be computed for the proposed
> network configuration in section 6.1.3 as follows
>
> {width="1.75in" height="0.3333333333333333in"}
>
> Because of the multislot structure on CCCH, it is better to define the total
> number of AGCH/PCH blocks per the superframe lasting 6.12 s.
  * **Offered load --** is the data arrival rate to LLC buffers, i.e. > the amount of data generated by traffic models. This metric > represents a load on the network and can be reported in kbps per > cell. The offered load can be reported for uplink and downlink > separately. (Please note that the data load is defined per > direction). The offered load is frequently used in plots of other > metrics as an independent variable on the x-axis.
> {width="2.65625in" height="0.3333333333333333in"}
  * **LLC throughput per cell** \-- is a measure of the amount of LLC > data in octets transmitted in a cell over a simulation in the > uplink respectively downlink direction. It does not take into the > account retransmissions or signalling at RLC.
> {width="2.46875in" height="0.3333333333333333in"}
### 6.2.3 Service metrics
Following service metrics are used in estimations of user experience and
satisfaction with the service according to relevant traffic model.
**[IM model]{.underline}**
  * **Message transmission delay** \-- in MO case it is the time measured > from the message generated at the mobile to the reception of this > message at the BSC, and in MT case it is the time measured from > the message arrival at the BSC to the reception of this message at > the mobile.
  * **Loss of login message --** is the ratio between number of > lost/blocked login messages and total arrived login messages at > the mobile station.
  * **Loss of ordinary message --** in MO case it is the ratio between > number of lost/blocked messages and total arrived messages at the > mobile, and in MT case, it is the ratio between number of > lost/blocked messages and total arrived messages at the BSC.
[]{.underline}
**[Web browsing model]{.underline}**
  * **Packet call throughput** \-- is a measurement of throughput > experienced by the user during a packet call in uplink and > downlink direction respectively. The packet call size is the > amount of the LLC data transmitted during a packet call. The > packet call duration is the sum of the time used for transmitting > each message measured from the arrival of this message at the > mobile/BSC until the reception of this message at the BSC/mobile > in the MO/MT case respectively.
{width="2.8430555555555554in" height="0.34375in"}
_[Editor's note:_ _Other metrics for Web browsing is FFS.]_
### 6.2.4 Evaluation methodology
The Instant Messaging traffic model in section 6.3.2 gives that a session
consists of an average of 15 messages and the average message inter arrival
time is 20 s. Hence the average length of a session in time would ideally be
15*20 = 300 seconds. Hence it will take that long time approximately from the
time instance the simulation starts until the total number of users in the
system has saturated, see Figure 1. It is proposed that for all evaluations,
no metrics should be started until this time has elapsed from the simulation
start, depicted as t1 in Figure 1.
Figure 1 Metric collection methodology
## 6.3 Traffic model
### 6.3.1 General
Both single traffic scenario and mixed traffic scenario should be studied. The
following traffic scenarios provide the primary focus for the evaluations.
Performance evaluation of any enhancements under mixed traffic scenario is
required.
Table 5: Single traffic scenarios
+-----------+----------------------+---------------------------+ | **Label** | **Traffic Scenario** | **Description** | +-----------+----------------------+---------------------------+ | A) | Instant Messaging | Analysis and traffic | | | | model parameters see | | | | section 6.3.2. | +-----------+----------------------+---------------------------+ | B) | Web Browsing | Analysis and traffic | | | | model parameters see | | | | section 6.3.3. | | | | | | | | No need to evaluate this | | | | single traffic scenario | | | | in this study. | +-----------+----------------------+---------------------------+
Table 6: Mixed traffic scenarios
* * *
**Label** **Traffic Scenario** **Description** S1 A + B Instant Messaging +
Web Browsing
* * *
_[Editor's note: more traffic scenarios may be included if required in this
study.]_
### 6.3.2 A) Instant Messaging
Instant messaging traffic comprises a mix of user plane packets conveying the
text data, along with application layer and/or transport layer protocol
signalling to verify message delivery status. Some instant messaging
applications may also display keep-alive behaviours.
This section describes an analytical IM traffic model loosely based on the
network statistic data in Annex A.1. It describes a simple IM session,
considering only login/logout, normal messages and keep-alive traffic.
> {width="5.713888888888889in" height="2.077777777777778in"}
Figure 2 IM session structure
Error: Reference source not found2 shows an overall structure of one IM
session. In the beginning, the IM application logs in to a server. Then the
user types messages or receives messages from the server (other user) with
randomly distributed length and message inter arrival time. At the same time,
the application sends keep alive messages to the server at regular intervals
no matter the user sends other messages or not. The server replies with ack
and status of user's buddies. At session end, the application sends log out
request to the server, which is acknowledged.
Retransmission of the lost or blocked application message is not considered.
If the login message is lost or blocked, the whole session is considered to be
failed/dropped, and if the logout message is lost or blocked, the session is
considered to be ended. If one keep alive message irrespective the UL part or
the DL part is lost or blocked, the whole session is considered to be
failed/dropped.
{width="5.9625in" height="2.704861111111111in"}
Figure 3 Packet structure in an IM session
Error: Reference source not found3 shows that messages, keep alive messages
and login/logout messages consist of blocks of data in DL and UL. Both keep
alive messages and login/logout messages are mobile originated type. Blocks
are then split on RLC layer into packets, creating short bursts of data.
Individual packets on TCP or any higher layer are not modelled explicitly. The
size of data blocks, message interarrival time and the split between outgoing
(MO) and incoming (MT) messages is randomly generated according to parameters
in Table 7.
Table 7. IM traffic generator parameters
+----------------+----------------+----------------+----------------+ | **Parameter** | **Distribution |** Mean value**|** Comment**| | | type** | | | +----------------+----------------+----------------+----------------+ | Session | Poisson | 5/s, 10/s, | | | arrival | | 20/s | | +----------------+----------------+----------------+----------------+ | Session length | geom | 15 messages | cut off: 40 | | | | | messages | +----------------+----------------+----------------+----------------+ | Keep alive | const | 180 s | | | period | | | | +----------------+----------------+----------------+----------------+ | Message | negExp | 20 s | cut off: 50s | | interarrival | | | | | time | | | Note 1 | +----------------+----------------+----------------+----------------+ | MO message | const | 139 Byte | | | size | | | | | | | | | | -- DL part | | | | +----------------+----------------+----------------+----------------+ | MO message | Pareto | 75.3 Byte | α=1.476, | | size | | | k=24.3 | | | | | | | -- UL part | | | cut off: | | | | | 200Byte | | | | | | | | | | Note 2 | +----------------+----------------+----------------+----------------+ | MT message | Pareto | - | α=0.529, | | size | | | k=20.4 | | | | | | | -- DL part | | | cut off: | | | | | 900Byte | | | | | | | | | | Note 2 | +----------------+----------------+----------------+----------------+ | MT message | const | 62 Byte | | | size | | | | | | | | | | -- UL part | | | | +----------------+----------------+----------------+----------------+ | Keep alive | const | 318 Byte | Note 3 | | message size | | | | | DL part | | | | +----------------+----------------+----------------+----------------+ | -- UL part | const | 282 Byte | Note 3 | +----------------+----------------+----------------+----------------+ | Out | uniform | 50/50 | | | going/incoming | | | | | message split | | | | +----------------+----------------+----------------+----------------+ | Login message | const | 1873 Byte | | | DL part | | | | +----------------+----------------+----------------+----------------+ | -- UL part | const | 2056 Byte | Note 4 | +----------------+----------------+----------------+----------------+ | Logout message | const | 201 Byte | | | DL part | | | | +----------------+----------------+----------------+----------------+ | -- UL part | const | 201 Byte | | +----------------+----------------+----------------+----------------+ | MS reaction | const | 20 ms | | | time | | | | +----------------+----------------+----------------+----------------+ | Network | const | 100 ms | | | reaction time | | | | +----------------+----------------+----------------+----------------+
Note 1: Mean value selected for this simulation meets the curve of Packet
Inter arrival of time CDF (DL&UL) Figure A.1 in Annex A.1. Truncated
exponential distribution is used, i.e. if the generated value for the
interarrival time is greater than the cut off, subtract cut off from it and
repeat until the value is less or equal to the cut off.
Note 2: Mean value, α value and k value for UL and DL selected for this
simulation meet the curve of Packet size CDF in UL and DL respectively in
Figure A.3 in Annex A.4.
Note 3: The size of keep alive messages has been derived from the 5 min idle
traffic in the table A.1 in Annex A.1, row 22. It assumed, that only two keep
alive messages were exchanged (with period 3 min, there could be 2 keep alive
transmissions and corresponding responses from the server).
Note 4: The maximum number of information octets in LLC frame equal to 1520 is
used. The generated messages should be segmented using this limitation, if the
message size exceeds this value. The segments should be transmitted
continuously with no interval between any two continuous segments.
The distribution types have been partially taken from WWW traffic model [5],
section. B.1.2.2 (negative exponential distribution instead of geometric) and
the distribution means and fixed message sizes are from IM traffic analysis in
Annex A.1. The message sizes listed in Table 7 represent the amount of data at
the LLC layer.
_[Editor's note: parameters in Table 7 may be optimised to fit the mobile IM
application.]_
### 6.3.3 B) Web Browsing
A WWW browsing traffic model in [5] is used and described as follows in this
study. Figure 4 depicts a typical WWW browsing **session** , which consists of
a sequence of **packet calls**. We only consider the packets from a source
which may be at either end of the link but not simultaneously. The user
initiates a packet call when requesting an information entity. During a packet
call several **packets** may be generated, which means that the packet call
constitutes of a bursty sequence of packets, see [6] and [7]. After receiving
its last packet in a packet call the MS should wait for T_fin period before
terminating the packet call. It is very important to take this phenomenon into
account in the traffic model. The burstyness during the packet call is a
characteristic feature of packet transmission in the fixed network.
Figure 4 Typical characteristic of a packet service session.
A packet service session contains one or several packet calls depending on the
application. For example in a WWW browsing session a packet call corresponds
the downloading of a WWW document. After the document is entirely arrived to
the terminal, the user is consuming certain amount of time for studying the
information. This time interval is called **reading time**. It is also
possible that the session contains only one packet call. In fact this is the
case for a file transfer (FTP). Hence, the following must be modelled in order
to catch the typical behaviour described in Figure 4.
> − Session arrival process
>
> − Number of packet calls per session
>
> − Reading time between packet calls
>
> − Number of packets within a packet call
>
> − Inter arrival time between packets (within a packet call)
>
> − Size of a packet
>
> − Size of Http GET packet, Ack packet, Ack packet, and FIN-ACK packet
> respectively
>
> − Τimer T_fin indicating the waiting period before MS terminating the packet
> call
Note that the session length is modelled implicitly by the number of events
during the session. And Table 8 shows the parameters for the traffic model of
WWW browsing UDD 32 kbit/s.
Table 8 WWW browsing traffic model
+----------------+----------------+----------------+----------------+ | **Parameter** | **Distribution |** Parameter | **Comment** | | | type**| value** | | +----------------+----------------+----------------+----------------+ | Session | Poisson | Mean: 5/hr | | | arrivals | | | | +----------------+----------------+----------------+----------------+ | Number of | Geometric | Mean 5 | Max: 15 | | packet calls | | | | | in session | | | | +----------------+----------------+----------------+----------------+ | Reading time | Geometric | Mean: 425s | Cut off: 600s | | between packet | | | | | calls | | | | +----------------+----------------+----------------+----------------+ | Number of | Geometric | Mean: 25 | Cut off: 40 | | packet in a | | | | | packet call | | | | +----------------+----------------+----------------+----------------+ | Packet size: | Pareto | Mean: 480Byte | alpha = 1.1, k | | | | | = 81.5 | | | | | | | | | | Cut off: 66666 | | | | | Byte | +----------------+----------------+----------------+----------------+ | Packet | Geometric | Mean: 0.125s | Cut off: 0.5s | | inter-arrival | | | | | time | | | | +----------------+----------------+----------------+----------------+ | Http GET | Constant | 350Byte | | +----------------+----------------+----------------+----------------+ | Ack packet | Constant | 66 Byte | | +----------------+----------------+----------------+----------------+ | FIN packet | constant | 66Byte | | +----------------+----------------+----------------+----------------+ | FIN-ACK packet | constant | 66Byte | | +----------------+----------------+----------------+----------------+ | T_fin | constant | 6s | | +----------------+----------------+----------------+----------------+ | MS reaction | const | 20 ms | | | time | | | | +----------------+----------------+----------------+----------------+ | Network | const | 100 ms | | | reaction time | | | | +----------------+----------------+----------------+----------------+
_[Editor's note: parameters in Table 8 may be optimised to fit the mobile web
browsing application.]_
# 7 Recommended enhancements for GERAN system
## 7.1 Enhancement 1
### 7.1.1 Concept description
_[Editor's note: This section clarifies problems solved by this enhancement
and describes the detailed concept and mechanism of the candidate enhancement
to efficiently support the mobile data application in GERAN.]_
7.1.2 Performance gains
_[Editor's note: This section describes performance gains of the candidate
enhancement for GERAN.]_
### 7.1.3 Impacts to GERAN system
#### 7.1.3.1 Impacts to the Mobile Station
_[Editor's note: This section identifies the impacts on Mobile Station
resulting from the functional enhancements.]_
#### 7.1.3.2 Impacts to the BSS
_[Editor's note: This section identifies the impacts on BSS resulting from the
functional enhancements.]_
#### 7.1.3.3 Impacts to the specification
_[Editor's note: This section identifies the impacts on GERAN specifications
resulting from functional enhancements.]_
## 7.2 \
# 8 Summary and conclusions
###### ### Annex A: Network trace and statistic information
Network trace and statistic information are shown as following.
## A.1 Network Data for IM application
Statistics of Mobile QQ chatting application from real network:
Table A.1: network data statictic for Mobile QQ
* * *
No Actions LLC traffic UL（byte） RLC traffic UL（byte） LLC traffic DL（byte） RLC
traffic DL（byte） 1 Log on 2056 2478 1873 2549 2 Add friends 310 449 342 651 3
Accept invitation 714 1093 774 1516 4 Delete friends 155 205 139 305 5 Be
added as friends 155 244 139 305 6 Sending message(10 bytes) 280 263 294 527 7
Sending message(10 bytes) 195 285 139 301 8 Sending message(50 bytes) 275 367
139 267 9 Sending message(50 bytes) 275 367 139 301 10 Sending message(100
bytes) 371 491 139 305 11 Sending message(100 bytes) 371 491 139 305 12
receiving message(10 bytes) 62 82 117 581 13 receiving message(10 bytes) 62 82
125 522 14 receiving message(50 bytes) 62 82 205 663 15 receiving message(50
bytes) 68 123 205 331 16 receiving message(100 bytes) 62 82 309 786 17
receiving message(100 bytes) 62 82 309 616 18 Sending picture of 16Kbytes
20360 22605 2369 3059 21 Sending picture of 18Kbytes 967 1394 1205 1671 19
Sending picture of 20Kbytes 24943 27645 2877 3871 20 Sending picture of
24Kbytes 29174 32189 2555 3498 22 Idle test for 5 minutes 564 856 636 1411 23
Log out 201 287 201 425 24 Re Log on 913 1299 990 1438 27 Check friends'
profile 5726 6591 10422 11932 28 Check friends' profile 5194 6223 9778 11147
* * *
Following are the traces statistics of corresponding instant message
applications (Mobile QQ), which is a typical and popular application in China.
  * The trace data are observed and captured on Gb interface in > EDGE/GPRS network
  * Mobile QQ application is based on TCP protocol, and the packet size > do not include the TCP header
  * The captured packets include the background packet (e.g. heart beat > packet) and active (chatty) packet. So our trace statistics can > reflect the characteristics of the whole traffic.
  * The trace data are collected from more than two hundred cells and > thousands of MSs using mobile QQ application. Hence, the OS of the > MSs are possibly different, including e.g Android, iOS and > Symbian.
{width="5.803472222222222in" height="3.4506944444444443in"}
Figure A.1. IM Traffic (Mobile QQ) - Packet Inter arrival of time CDF (DL&UL)
{width="5.988888888888889in" height="3.4506944444444443in"}
Figure A.2. IM Traffic (Mobile QQ) - Packet size CDF (UL&UL)
Figure A.3 and Figure A.4 show the uplink and downlink original data (Shantou
region in China), fitted total cumulative distribution function for the packet
size, respectively.
{width="5.121527777777778in" height="3.827777777777778in"}
Figure A.3 Original and fitted CDF for uplink QQ packet size, Shantou.
{width="4.998611111111111in" height="3.9583333333333335in"}
Figure A.4 Original and fitted CDF for downlink QQ packet size, Shantou.
#