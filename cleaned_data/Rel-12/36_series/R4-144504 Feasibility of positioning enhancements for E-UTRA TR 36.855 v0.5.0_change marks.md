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
# 1 Scope
Positioning mechanisms were specified in 3GPP as a key feature for E-UTRA
networks since Release 9, e.g. OTDOA, E-CID etc. They are not only used in
helping meet regulatory requirements, but also utilized with increasing
importance to enable all kinds of location based applications.
The proliferation of heterogeneous network deployments brings some challenges
also in the area of efficient terminal positioning and calls for the study of
enhanced mechanisms and positioning performance requirements.
The addition of multiple nodes in heterogeneous networks can improve the
position accuracy remarkably if the specificities of such deployments are
taken into account in the positioning mechanisms. Some examples include the
support of several transmission points with identical cell IDs and improved
support for positioning in carrier aggregation.
Furthermore, the accuracy of current positioning mechanisms and in particular
OTDOA and E-CID based on UE Rx-Tx time difference measurement is only defined
for limited scenarios:
  * Limited channel bandwidth for the cells to be measured (reference and neighbour cells)
  * Tests defined assuming single Tx antenna. Practical network might have Tx diversity on antenna port 6 which is used for RSTD measurements
It is desirable to study the possibility of enhanced accuracy for other
practical deployment scenarios.
The present document is the Technical Report for the Study Item on positioning
enhancements for E-UTRA.
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
[2] RP-130680, "New SI proposal: Positioning enhancements for E-UTRA", Huawei,
RAN #60
[3] 3GPP TS 36.133: \"Evolved Universal Terrestrial Radio Access (E-UTRA);
Requirements for support of radio resource management\".
[4] T1P1.5/98-110, Evaluation of Positioning Measurement Systems.
\
# 3 Definitions, symbols and abbreviations
## 3.1 Definitions
For the purposes of the present document, the terms and definitions given in
TR 21.905 [1] and the following apply. A term defined in the present document
takes precedence over the definition of the same term, if any, in TR 21.905
[1].
Definition format (Normal)
**\ :** \.
## 3.2 Symbols
For the purposes of the present document, the following symbols apply:
Symbol format (EW)
\ \
## 3.3 Abbreviations
For the purposes of the present document, the abbreviations given in TR 21.905
[1] and the following apply. An abbreviation defined in the present document
takes precedence over the definition of the same abbreviation, if any, in TR
21.905 [1].
Abbreviation format (EW)
\ \
# 4 General
## 4.1 Study item objective
The objective is to study accuracy enhancements for current positioning
mechanisms such as OTDOA and E-CID based on UE Rx-Tx time difference
measurement in heterogeneous deployment scenarios and different system
bandwidths.
The feasibility of improving the existing UE positioning performance
requirements of OTDOA and E-CID based on UE Rx-Tx time difference measurement
shall be studied for the following cases:
  * Larger available bandwidths (e.g. 15 and 20MHz for OTDOA and 10, 15, and 20 MHz for E-CID based on UE Rx-Tx time difference measurement).
  * Smaller available bandwidths (e.g. 1.4 and 3 MHz for OTDOA and E-CID based on UE Rx-Tx time difference measurement)
  * Possible use of downlink Tx diversity for the positioning reference signals (PRS), e.g., schemes transparent to UE, and its impact on the both UE and system performance and/or complexity. Use of non-transparent schemes can be discussed.
  * Deployment of RRHs with identical cell IDs for OTDOA and E-CID based on UE Rx-Tx time difference measurement.
  * Carrier aggregation scenarios (including scenarios with multiple TAs for E-CID based on UE Rx-Tx time difference measurement)
The study includes the definition of the above mentioned scenarios in an
initial phase.
# 5 Feasibility on measurement performance enhancement under Wide-band/Narrow-
band
## 5.1 General
In this section the simulation evaluation for wide-BW and narrow-BW
positioning measurement performance are studied and the possible enhancements
on positioning measurement requirements are proposed.
## 5.2 Scenarios
  * RSTD measurement accuracy evaluation (PRS BW)
> \- Larger bandwidths: 15MHz, 20MHz
>
> \- Smaller bandwidths: 3MHz
  * UE Rx-Tx time difference measurement accuracy evaluation (system BW)
> \- Larger bandwidths: 10MHz, 15MHz, 20MHz
>
> \- Smaller bandwidths: 3MHz
## 5.3 RSTD measurement performance for OTDOA
\
### 5.3.1 Simulation assumptions
In this section, the simulation assumptions for RSTD evaluation are provided.
  * Simulation assumption for RSTD measurement
Table 5.3.1-1 Simulation assumptions for RSTD measurement
+------------------------------+------------------------------+-----+ | **Parameter** | **Value** | | +------------------------------+------------------------------+-----+ | Cell layout | - 3 cells at distinct | | | | > locations | | | | | | | | - the distances between | | | | > each cell and target | | | | > UE are identical | | | | | | | | - Same ISD between cells | | +------------------------------+------------------------------+-----+ | Cell ID scenarios | > (0, 1, 2), | | | | > | | | | > (0, 6, 12) (baseline) | | +------------------------------+------------------------------+-----+ | Network synchronization | - Synchronous with time | | | | > shifts \ | | | | | | | | - Asynchronous with time | | | | > shifts: \ 450us> | | +------------------------------+------------------------------+-----+ | Duplex modes | > FDD and TDD | | +------------------------------+------------------------------+-----+ | TDD specific parameters | Uplink-downlink | > 1 | | | configuration | | +------------------------------+------------------------------+-----+ | | Special subframe | > 6 | | | configuration | | +------------------------------+------------------------------+-----+ | Data and CCH load | > 100% | | +------------------------------+------------------------------+-----+ | Cyclic prefix | > Normal | | +------------------------------+------------------------------+-----+ | DRX | > OFF | | +------------------------------+------------------------------+-----+ | Carrier frequency | > 2 GHz | | +------------------------------+------------------------------+-----+ | UE speed | - 3 km/h | | | | | | | | - 30 km/h | | +------------------------------+------------------------------+-----+ | Carrier bandwidth | - 3MHz, 15 MHz, 20 MHz | | | | | | | | - 10 MHz (baseline for | | | | > benchmarking with | | | | > Rel-9) | | +------------------------------+------------------------------+-----+ | Channel model | > ETU, EPA, AWGN | | +------------------------------+------------------------------+-----+ | _N~oc~_ (does not include | > AWGN, values are TBD | | | received powers of the three | | | | simulated cells), | | | | [dBm/15kHz] | | | +------------------------------+------------------------------+-----+ | SINR for three cells, [dB] | > (Reference cell, neighbour | | | | > cell 1, neighbour cell 2) | | | | > = (-6,-13,-13) | | +------------------------------+------------------------------+-----+ | Number of transmit antennas | PRS | > 1 | +------------------------------+------------------------------+-----+ | | CRS | > 1 | +------------------------------+------------------------------+-----+ | Number of receive antennas | > 2 equal-gain uncorrelated | | | | > antennas | | +------------------------------+------------------------------+-----+ | Positioning subframes | > LIS (no presence of PDSCH | | | | > in PRBs containing PRS), | | | | > full or partial alignment | | +------------------------------+------------------------------+-----+ | Number of consecutive | > 1 for larger bandwidths | | | positioning subframes | > | | | | > 6 for smaller bandwidths | | | | > (non-coherent accumulation | | | | > across positioning | | | | > occasions) | | +------------------------------+------------------------------+-----+ | Number of positioning | > 1 | | | occasions for a positioning | | | | fix | | | +------------------------------+------------------------------+-----+ | PRS pattern | > 6-reuse in frequency, | | | | > v~shift~ = mod(PCI,6) | | +------------------------------+------------------------------+-----+ | PRS transmission bandwidth | > Full carrier bandwidth | | +------------------------------+------------------------------+-----+ | Measurement bandwidth | > Full carrier bandwidth | | +------------------------------+------------------------------+-----+
### 5.3.2 Performance characterization
In this clause the performance gains are evaluated by using link level
simulation based on the simulation assumptions in clause 5.3.1.
#### Link level simulation results
  * Simulation results for larger BWs
Table 5.3.2.1-1 to 5.3.2.1-5 provides the simulation results submitted by
interested companies.
Table 5.3.2.1-1. RSTD link level simulation results (Alcatel-Lucent)
+-------------------+-----------------------+-----------------------+ | Synchronous cases | | | +-------------------+-----------------------+-----------------------+ | | Cell ID =(0, 6, 12) | Cell ID =(0, 1, 2) | +-------------------+-----------------------+-----------------------+ | 10MHz | {width="2.825in" | | | height="2 | height="2 | | | .1277777777777778in"} | .1277777777777778in"} | | | | | | | {width="2.825in" | | | height="2 | height="2 | | | .1277777777777778in"} | .1277777777777778in"} | | | | | | | {width="2.825in" | | | height="2 | height="2 | | | .1277777777777778in"} | .1277777777777778in"} | | | | | | | {width="2.825in" | | | height="2 | height="2 | | | .1277777777777778in"} | .1277777777777778in"} | | | | | | | {width="2.8125in" | | | height="2 | height="2 | | | .1277777777777778in"} | .1277777777777778in"} | +-------------------+-----------------------+-----------------------+ | 15MHz | {width="2.8375in" | | | height="2 | height="2 | | | .1277777777777778in"} | .1277777777777778in"} | | | | | | | {width="2.825in" | | | height="2 | height="2 | | | .1277777777777778in"} | .1277777777777778in"} | | | | | | | {width="2.8375in" | | | height="2 | height="2 | | | .1277777777777778in"} | .1277777777777778in"} | | | | | | | {width="2.8375in" | | | height="2 | height="2 | | | .1277777777777778in"} | .1277777777777778in"} | | | | | | | {width="2.8375in" | | | height="2 | height="2 | | | .1277777777777778in"} | .1277777777777778in"} | +-------------------+-----------------------+-----------------------+ | 20MHz | {width="2.8375in" | | | height="2 | height="2 | | | .1277777777777778in"} | .1277777777777778in"} | | | | | | | {width="2.8375in" | | | height="2 | height="2 | | | .1277777777777778in"} | .1277777777777778in"} | | | | | | | {width="2.8375in" | | | height="2 | height="2 | | | .1277777777777778in"} | .1277777777777778in"} | | | | | | | {width="2.8375in" | | | height="2 | height="2 | | | .1277777777777778in"} | .1277777777777778in"} | | | | | | | {width="2.8375in" | | | height="2 | height="2 | | | .1277777777777778in"} | .1277777777777778in"} | +-------------------+-----------------------+-----------------------+
Table 5.3.2.1-2. RSTD link level simulation results (Huawei)
* * *
Synchronous cases  
Cell ID =(0, 6, 12) Cell ID =(0, 1, 2) 10MHz {width="2.7916666666666665in"
height="2.1277777777777778in"} {width="2.7777777777777777in"
height="2.1131944444444444in"} 15MHz {width="2.790277777777778in"
height="2.14375in"} {width="2.7784722222222222in"
height="2.154166666666667in"} 20MHz {width="2.7569444444444446in"
height="2.1305555555555555in"} {width="2.7756944444444445in"
height="2.138888888888889in"}
Asynchronous cases  
Cell ID =(0, 6, 12) Cell ID =(0, 1, 2) 10MHz {width="2.8027777777777776in"
height="2.2055555555555557in"} {width="2.7847222222222223in" height="2.15in"}
15MHz {width="2.795138888888889in" height="2.1868055555555554in"}
{width="2.779166666666667in" height="2.1819444444444445in"} 20MHz
{width="2.7555555555555555in" height="2.15in"} {width="2.7756944444444445in"
height="2.1590277777777778in"}
* * *
Table 5.3.2.1-3. RSTD link level simulation numeric results (Huawei)
* * *
Time alignment BW[MHz] Cell IDs SINRs [dB] Cell 2 Cell 3  
RSTD error, [Ts] RSTD error, [Ts]  
AWGN EPA ETU AWGN EPA ETU Synchronous cases 10 \ \ 0.6 2.0
5.8 0.6 1.9 5.1 \ \ 0.7 2.1 5.1 0.6 2.2 5.3 15 \
\ 0.2 1.5 3.7 0.2 1.5 3.9 \ \ 0.2 1.5 3.7 0.1
1.5 4.0 20 \ \ 0.2 1.2 3.0 0.2 1.1 3.0 \
\ 0.2 1.2 3.2 0.1 1.1 2.8 Asynchronous cases 10 \
\ 2.3 3.7 5.3 2.4 3.5 5.8 \ \ 2.3 3.7 5.8 2.3
3.8 6.2 15 \ \ 1.0 1.9 3.9 1.0 2.0 3.7 \
\ 1.0 2.1 3.8 1.0 1.9 4.0 20 \ \ 1.0 1.8 2.8
1.0 1.8 2.9 \ \ 1.0 1.8 3.2 1.0 1.7 3.1
* * *
Table 5.3.2.1-4. RSTD link level simulation results (Intel)
* * *
Synchronous cases  
Cell ID =(0, 6, 12) Cell ID =(0, 1, 2) 10MHz {width="3.0347222222222223in"
height="2.125in"} {width="3.042361111111111in" height="2.125in"} 15MHz
{width="2.9277777777777776in" height="2.1645833333333333in"}
{width="2.9277777777777776in" height="2.1645833333333333in"} 20MHz
{width="2.9277777777777776in" height="2.1645833333333333in"}
{width="2.9277777777777776in" height="2.1645833333333333in"}
* * *
Table 5.3.2.1-5. RSTD link level simulation results (Qualcomm)
+----------------------------------+----------------------------------+ | Synchronous cases | | +----------------------------------+----------------------------------+ | Cell ID =(0, 6, 12) | Cell ID =(0, 1, 2) | +----------------------------------+----------------------------------+ | {width="3.125in" | | height="2.3625in"} | height="2.3625in"} | | | | | {width="3.15in" | | height="2.3625in"} | height="2.3625in"} | | | | | {width="3.15in" | | height="2.3625in"} | height="2.3625in"} | | | | | {width="3.15in" | | height="2.3625in"} | height="2.3625in"} | | | | | {width="3.15in" | | height="2.3625in"} | height="2.3625in"} | +----------------------------------+----------------------------------+ | Collective results for all the | | | cases | | | | | | {width="3.15in" | | | height="2.3625in"} | | +----------------------------------+----------------------------------+
  * Simulation results for smaller BWs
Table 5.3.2.1-6 to 5.3.2.1-7 provides the simulation results submitted by
interested companies.
Table 5.3.2.1-6 RSTD link level simulation results (Huawei)
* * *
Synchronous cases  
Cell ID =(0, 6, 12) Cell ID =(0, 1, 2) 1.4MHz {width="2.7729166666666667in"
height="2.361111111111111in"} {width="2.7909722222222224in"
height="2.3631944444444444in"} 3MHz {width="2.7756944444444445in"
height="2.3645833333333335in"} {width="2.7881944444444446in"
height="2.3673611111111112in"} Asynchronous cases  
Cell ID =(0, 6, 12) Cell ID =(0, 1, 2) 1.4MHz {width="2.7736111111111112in"
height="2.2569444444444446in"} {width="2.782638888888889in"
height="2.2618055555555556in"} 3MHz {width="2.783333333333333in"
height="2.186111111111111in"} {width="2.765972222222222in"
height="2.1881944444444446in"}
* * *
Table 5.3.2.1-7. RSTD link level simulation numeric results (Huawei)
* * *
Time alignment BW[MHz] Cell IDs SINRs [dB] Cell 2 Cell 3  
RSTD error, [Ts] RSTD error, [Ts]  
AWGN EPA ETU AWGN EPA ETU Synchronous cases 1.4 \ \ 2.8
4.6 12.0 3.2 5.7 10.0 \ \ 3.1 4.7 11.2 3.3 4.7 10.2 3
\ \ 0.6 4.1 8.1 1.1 4.5 8.4 \ \ 1.0 3.5
8.6 1.0 4.3 8.9 Asynchronous cases 1.4 \ \ 2.6 4.8 10.8
3.4 4.8 10.9 \ \ 2.9 4.3 10.0 3.5 4.3 10.1 3 \
\ 0.8 3.2 8.6 1.1 3.4 8.8 \ \ 1.0 6.0 9.9 1.0
6.0 10.0
* * *
#### Summary
Summary in this section is based on the link level simulation and conclusions
from interested companies.
(1) The link level simulation results show that improvements on RSTD
measurement performance can be achieved by using wider PRS BW.
(2) Simulation results with different quantization show that increasing
reporting granularity to 0.5Ts is beneficial.
(3) The link level simulation results show that RSTD measurement performance
for 3 MHz is better than the performance for 1.4 MHz which was used to define
the existing RSTD requirements.
## 5.4 UE Rx-Tx time difference measurement performance for E-CID
\
### 5.4.1 Simulation assumptions
In this section, the simulation assumptions for UE Rx-Tx time difference
evaluation are provided.
  * Simulation assumption for UE Rx-Tx time difference measurement
Table 5.4.1-1. Simulation assumptions for UE Rx-Tx time difference measurement
+----------------------------------+----------------------------------+ | Parameters | Value | +----------------------------------+----------------------------------+ | Cell layout | 1 cell for UE Rx-Tx time | | | difference measurement | +----------------------------------+----------------------------------+ | Measurement bandwidth | - 5MHz (baseline for | | | benchmarking with Rel-9) | | | | | | - 10MHz, 15MHz, 20MHz for | | | larger bandwidths | | | | | | - 3MHz for smaller bandwidths | +----------------------------------+----------------------------------+ | L1 measurement period | 200ms | +----------------------------------+----------------------------------+ | Measurement sampling rate | 5, | | | | | | sample interval = 40ms | +----------------------------------+----------------------------------+ | Number of Tx Antennas | 1 | +----------------------------------+----------------------------------+ | Number of Rx Antennas | 2, | | | | | | Both antennas with equal gain, | | | no correlation between them | +----------------------------------+----------------------------------+ | DRX/DTX | OFF | +----------------------------------+----------------------------------+ | Propagation conditions | - AWGN | | | | | | - ETU30 | | | | | | - EPA5 | +----------------------------------+----------------------------------+ | Frequency | 2.0GHz | +----------------------------------+----------------------------------+ | Interference from cells not | AWGN | | simulated [Noc] | | +----------------------------------+----------------------------------+ | Geometry factor: Ês/Iot | -3dB | +----------------------------------+----------------------------------+
### 5.4.2 Performance characterization
In this clause the performance gains are evaluated by using link level
simulation based on the simulation assumptions in clause 5.4.1.
#### Link level simulation results
  * Simulation results for larger and smaller BWs
Table 5.4.2.1-1 and 5.4.2.1-2 provides the simulation results.
Table 5.4.2.1-1. UE Rx-Tx time difference link level simulation results
(Huawei)
* * *
CRS Ês/Iot =-3dB, FDD  
AWGN ETU30 EPA5 {width="2.0569444444444445in" height="1.5715277777777779in"}
{width="2.0548611111111112in" height="1.5756944444444445in"}
{width="2.047222222222222in" height="1.5756944444444445in"}
* * *
Table 5.4.2.1-2. UE Rx-Tx time difference RSTD link level simulation numeric
results (Huawei)
* * *
Channel condition CRS Ês/Iot =-3dB, FDD  
AWGN 1.4MHz -3.8\~-2.8 3MHz -1.8\~-1.6 5MHz (benchmark) -1.1\~-1.0 10MHz
-0.6\~-0.5 15MHz -0.32\~-0.29 20MHz -0.24\~-0.24 ETU30 1.4MHz -10.4\~-5.7 3MHz
-8.9\~-1.7 5MHz (benchmark) -5.3\~-1.1 10MHz -1.7\~-0.9 15MHz -1.4\~-1.0 20MHz
-1.1\~-0.8 EPA5 1.4MHz -4.4\~-3.2 3MHz -2.9\~-2.6 5MHz (benchmark) -1.7\~-1.5
10MHz -1.2\~-1.1 15MHz -0.95\~-0.88 20MHz -0.83\~-0.77
* * *
#### Summary
Summary in this section is based on the link level simulation and conclusions
from interested companies.
(1) The link level simulation results show that improvements on UE Rx-Tx time
difference measurement performance can be achieved by using larger BW.
(2) The link level simulation results show that UE Rx-Tx time difference
measurement performance for 3 MHz is better than the performance for 1.4 MHz
which was used to define the existing UE Rx-Tx time different requirements.
# 6 Feasibility on downlink Tx diversity for PRS
## 6.1 General
For studying on the PRS Tx diversity schemes, the following candidates are
involved,
  1. _Antenna switching_
Table 6.1-1 antenna switching
* * *
_Tx antenna #_ _PRS occasion 1_ _PRS occasion 2_ _Antenna #1_ _y~0~=sqrt(2)*r_
_y~0~=0_ _Antenna #2_ _y~1~=0_ _y~1~=sqrt(2)*r_
* * *
  1. _Transmit diversity 1_
Table 6.1-2 transmit diversity 1
* * *
_Tx antenna #_ _PRS occasion 1_ _PRS occasion 2_ _Antenna #1_ _y~0~= r_ _y~0~=
r_ _Antenna #2_ _y~1~=r_ _y~1~= -r_
* * *
  1. _Transmit diversity 2_
Table 6.1-3 transmit diversity 2
* * *
_Tx antenna #_ _PRS occasion 1_ _PRS occasion 2_ _Antenna #1_ _y~0~= r_ _y~0~=
r_ _Antenna #2_ _y~1~=r_ _y~1~= r_
* * *
  1. _Random antenna switching_
For each positioning occasion PRS will be transmitted on one antenna randomly.
The antenna transmission scheme is considered unknown to the UE.
Note: r is the positioning reference signal sequence
## 6.2 Scenarios
For simulation evaluation, the RSTD measurement performance without Tx
diversity shall also be provided as benchmark. Thus the scenarios for
simulation are summarized as,
  * Candidate1: Antenna switching scheme
  * Candidate2: Transmit diversity 1
  * Candidate3: Transmit diversity 2
  * Candidate4: Random antenna switching
  * Benchmark: R9 single antenna transmit scheme
## 6.3 Performance of possible PRS Tx diversity schemes
\
### 6.3.1 Simulation assumptions
In this section, the simulation assumptions for PRS Tx diversity evaluation
are provided.
  * Cell layout
Two cells topology is adopted
• 2 cells at distinct locations
• the distances between each cell and target UE are identical
Figure 6.3.1-1 cell layout
Cell 1 is reference cell and cell 2 is neighbour cell.
  * Occasion number
1 or 2 occasions are used to estimate the RSTD between cell1 and cell2. The
PRS of cell1 and cell2 are transmitted in these 1 or 2 occasions.
  * PRS BW
PRS BW=10MHz is assumed as a typical case and correspondingly one PRS subframe
is within one occasion.
  * Transmit antenna assumptions
Antenna #1 and #2 are geographically co-located.
The detailed assumptions are listed in the following table,
Table 6.3.1-1 simulation assumption for PRS Tx diversity
+-----------------------------+-----------------------------+--------+ | **Parameter** | **Value** | | +-----------------------------+-----------------------------+--------+ | Cell layout | - 2 cells at distinct | | | | locations | | | | | | | | - the distances between | | | | each cell and target UE | | | | are identical | | +-----------------------------+-----------------------------+--------+ | Cell ID scenarios | (0, 3), | | +-----------------------------+-----------------------------+--------+ | Network synchronization | Synchronous | | +-----------------------------+-----------------------------+--------+ | Duplex modes | FDD | | +-----------------------------+-----------------------------+--------+ | Data and CCH load | 100% | | +-----------------------------+-----------------------------+--------+ | Cyclic prefix | Normal | | +-----------------------------+-----------------------------+--------+ | DRX | OFF | | +-----------------------------+-----------------------------+--------+ | Carrier frequency | 2 GHz | | +-----------------------------+-----------------------------+--------+ | UE speed | 3 km/h | | +-----------------------------+-----------------------------+--------+ | Carrier bandwidth | 10 MHz | | +-----------------------------+-----------------------------+--------+ | Channel model | The channel model is the | | | | same for both cells. | | | | | | | | ETU30 (baseline); | | | | | | | | Optional channel model: | | | | | | | | > Urban A, Urban B and Bad | | | | > Urban profiles of T1P1 | | | | > [4] | | +-----------------------------+-----------------------------+--------+ | SINR for two cells, [dB] | (Reference cell, neighbour | | | | cell 1) =(-6,-13) | | +-----------------------------+-----------------------------+--------+ | Number of transmit antennas | PRS | 1 or 2 | +-----------------------------+-----------------------------+--------+ | | CRS | 2 | +-----------------------------+-----------------------------+--------+ | Positioning subframes | LIS (no presence of PDSCH | | | | in PRBs containing PRS) | | +-----------------------------+-----------------------------+--------+ | Number of consecutive | 1 | | | positioning subframes per | | | | occasion | | | +-----------------------------+-----------------------------+--------+ | Number of positioning | For each transmission | | | occasions for an RSTD | scheme: | | | measurement | | | | | 1 (baseline) | | | | | | | | 2 consecutive positioning | | | | occasions | | | | | | | | 2 non-consecutive | | | | positioning occasions | | | | (odd-numbered positioning | | | | occasions) | | +-----------------------------+-----------------------------+--------+ | PRS pattern | 6-reuse in frequency, | | | | v~shift~ = mod(PCI,6), | | | | Tprs=160 ms | | +-----------------------------+-----------------------------+--------+ | PRS transmission bandwidth | 10 MHz | | +-----------------------------+-----------------------------+--------+
### 6.3.2 RSTD Estimation with Diversity
A general structure for TOA estimation with diversity is shown in Figure
6.3.2-1 below, where the diversity system has _P_ branches. The TOA is
estimated independently at each diversity branch of the receiver, and then a
"combining algorithm" is used to process the TOA estimates from all branches
to obtain a desired "optimum" estimate for RSTD calculation.
Figure 6.3.2-1: General Structure of TOA Estimation with Diversity Techniques.
A variety of different combining algorithms can be designed for different
diversity techniques. Two examples were used for the simulation results in
subclause 6.3.3:
  1. ${\hat{\tau}}_{0} = \text{min}\left{ {\hat{\tau}}_{o}^{i} \right}$ ("Method #1")
  2. ${\hat{\tau}}_{0} = \frac{1}{P}\sum_{i = 1}^{P}{\hat{\tau}}_{0}^{(i)}$ ("Method #2")
Other possibilities may be to include a weighting factor, where the estimate
of each diversity branch is weighted with a coefficient that reflects the
quality of the TOA estimation at each branch.
For the simulation results in subclause 6.3.3, _P=2_ has been used as defined
in the simulation assumptions (subclause 6.3.1).
### 6.3.3 Performance characterization
In this clause the performance gains are evaluated by using link level
simulations based on the simulation assumptions in clause 6.3.1.
#### 6.3.3.1 Link level simulation results
##### 6.3.3.1.1 Link level simulation results (Qualcomm)
The results in this subclause were obtained with the combining method #1 in
subclause 6.3.2 (i.e., min. TOA is selected as final TOA for RSTD
calculation).
  * T1P1 Channel Models
{width="3.316666666666667in"
height="2.423611111111111in"}{width="3.2958333333333334in"
height="2.408333333333333in"}
{width="3.2319444444444443in"
height="2.4159722222222224in"}{width="3.2743055555555554in"
height="2.423611111111111in"}
Figure 6.3.3.1.1-1: RSTD link level simulation results (Qualcomm)
  * ETU Channel Models
High Spatial Correlation:
{width="3.2423611111111112in" height="2.4159722222222224in"}
{width="3.2104166666666667in" height="2.4159722222222224in"}
Figure 6.3.3.1.1-2: RSTD link level simulation results (Qualcomm)
Medium Spatial Correlation:
{width="3.2104166666666667in" height="2.423611111111111in"}
{width="3.2104166666666667in" height="2.423611111111111in"}
Figure 6.3.3.1.1-3: RSTD link level simulation results (Qualcomm)
Low Spatial Correlation:
{width="3.2104166666666667in" height="2.423611111111111in"}
{width="3.2104166666666667in" height="2.423611111111111in"}
Figure 6.3.3.1.1-4: RSTD link level simulation results (Qualcomm)
###### 6.3.3.1.1.1 Comparison of TOA Estimation Schemes
The following Figures compare the results with combining method #1 and method
#2 defined in subclause 6.3.2 (i.e., min. TOA is selected as final TOA and
average TOA is selected as the final TOA, respectively) for the Urban A
example:
{width="6.711111111111111in" height="2.688888888888889in"}
Figure 6.3.3.1.1.1-1: RSTD link level simulation results (Qualcomm)
(a) **Time Diversity Benefit:** \ The curves "No Diversity" in Figure
6.3.3.1.1.1-1 show the benefit from time diversity; i.e., a single TX antenna
is used but two PRS occasions which are combined as described in subclause
6.3.2 above. With combining method #1 (min TOA), a time diversity effect is
exploited. The performance is about 1.5 Ts better at the 70^th^ percentile
compared to the use of a single PRS occasion.\ \ Due to the fading, the two
TOAs estimated are slightly different, and picking the smallest TOA among the
two as a final TOA estimate should provide a TOA as close as possible to the
desired line-of-sight TOA.\ \ With combining method #2 (average TOA),
essentially no time diversity benefit is obtained. The "No Diversity" curve in
Figure 6.3.3.1.1.1-1 (right hand side) overlap with the result of a single PRS
occasion (baseline). The average TOA over two consecutive occasions is (on
average) similar to the TOA estimated from a single occasion.
(b) **Antenna Switching Benefit:\** With the given channel models, antenna
switching does not provide an additional performance benefit compared to the
use of a single antenna ("No Diversity").\ \ With combining method #1 (Min
TOA) the benefit is essentially due to time diversity. With combining method
#2 (average TOA), no benefit compared to a single PRS occasion can be obtained
(the same as (a) above).
(c) **TX Diversity 1 (Power splitting with sign flip):\** This technique shows
worse performance compared to no diversity; slightly worse with combining
method #1, and considerably worse with combining method #2. With combining
method #2, the performance is even worse compared to the base line result with
a single PRS occasion.\ \ In the first PRS occasion, the sum of the two TX
signals is used at the receiver; for the second PRS occasion the difference of
the two TX signals is used at the receiver. With the given channel models,
this means that most of the signal is canceled in the second occasion. With
combining method #1, we pick the TOA mostly from the first occasion; with
combining method #2, we compute an average TOA, but since the TOA from the
2^nd^ occasion is quite bad (since components cancel due to the 180 degrees
phase shift), the final TOA get worse compared to the use of a single
occasion.\ \ With combining method #1, we essentially use the TOA from the
first occasion only, and therefore, no additional time diversity. The benefit
here comes primarily from space diversity only, where the two TX signals in
the first occasion are added from the two antennas. With the given channel
models, space diversity alone does not provide the same benefit as time
diversity alone. Therefore, the performance with method #1 is worse compared
to no diversity (i.e., time diversity only), but still better compared to the
baseline with a single PRS occasion only.
(d) **TX Diversity 2 (Power splitting):\** This technique shows the best
performance in the simulations. Here, in both occasions the signal from the
two antennas adds up at the receiver. There are two different TOAs available
(compared to a single "good" TOA as in case of TX Diversity 1, where the
signal in the second occasion mostly cancel), and by picking the smallest
among the two TOAs, both, time and space diversity is exploited. The benefit
with combining method #1 is about 2.5 Ts compared to a single PRS occasion at
the 70^th^ percentile; and about 1.5 Ts compared to time diversity only ("No
Diversity") at the 70^th^ percentile.\ \ Also with combining method #2, a gain
can be obtained, which is however, slightly worse compared to combining
technique #1. The average TOA is always more biased than a single selected
TOA.
#### 6.3.3.2 Conclusions from interested companies
+----------------------+----------------------------------------------+ | Qualcomm (R4-141826) | Under the given simulation assumptions and | | | channel models, some TX Diversity schemes | | | can achieve about 1 -- 2Ts improvement, if | | | the UE processes the PRS occasions | | | accordingly. E.g., processes nonconsecutive | | | occasions and does not treat each occasion | | | equally for estimating a final TOA to | | | calculate the RSTD. Otherwise, it is | | | possible that TX diversity performs worse | | | compared to no diversity. Processing PRS | | | occasions accordingly require at the UE the | | | knowledge that TX diversity for PRS is being | | | used at the eNodeB. If this is not the case, | | | the PRS should not be transmitted from more | | | than a single antenna. | | | | | | The results also show that the performance | | | improvement with TX Diversity depends on the | | | channel model so without channel information | | | at the TX side it may not be possible to | | | obtain any performance gains. | +----------------------+----------------------------------------------+
7 Feasibility on enhancement for OTDOA and E-CID with identical cell ID RRHs
## 7.1 General
\
## 7.2 Network Scenarios
In certain het-net deployments, some non-collocated RRHs have the identical
PCI with the associated Macro cell so that these RRHs transmit the identical
reference signals, and therefore it may cause ambiguousness on reference
signal ToA detection. Scenarios to be studied:
  * OTDOA scenario: RRH with PCI identical to the associated Macro cell
  * E-CID scenario: RRH with PCI identical to the associated Macro cell
## 7.3 Possible enhancements on OTDOA
\
### 7.3.1 Simulation assumptions
\
### 7.3.2 Performance characterization
\
### 7.3.3 Possible enhancement options
\
## 7.4 Possible enhancements on E-CID
\
### 7.4.1 Simulation assumptions
\
### 7.4.2 Performance characterization
\
### 7.4.3 Possible enhancement options
\
# 8 Feasibility on enhancement for E-CID in carrier aggregation
## 8.1 General
\
## 8.2 Network Scenarios
\
## 8.3 Possible enhancement for E-CID in CA
\
### 8.3.1 Possible enhancement options
\
# 9 Conclusions
\
#