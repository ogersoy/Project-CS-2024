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
The present document is a technical report for Inter-band Carrier Aggregation
under Rel-11 time frame. The purpose is to gather the relevant background
information and studies in order to address Inter-band Carrier Aggregation
requirements.
This TR covers relevant background information and studies in order to address
Inter-band Carrier Aggregation requirements for the Rel-11 band combinations
in table 1-1.
Table 1-1: Release 11 inter-band carrier aggregation combinations
* * *
WI code WI title Class LTE_CA_B3_B7 LTE Advanced Carrier Aggregation of Band 3
and Band 7 A3 LTE_CA_B4_B17 LTE Advanced Carrier Aggregation of Band 4 and
Band 17 A2 LTE_CA_B4_B13 LTE Advanced Carrier Aggregation of Band 4 and Band
13 A1 LTE_CA_B4_B12 LTE Advanced Carrier Aggregation of Band 4 and Band 12 A2
LTE_CA_B5_B12 LTE Advanced Carrier Aggregation of Band 5 and Band 12 A3
LTE_CA_B7_B20 LTE Advanced Carrier Aggregation of Band 7 and Band 20 A1
LTE_CA_B2_B17 LTE Advanced Carrier Aggregation of Band 2 and Band 17 A1
LTE_CA_B4_B5 LTE Advanced Carrier Aggregation of Band 4 and Band 5 A1
LTE_CA_B5_B17 LTE Advanced Carrier Aggregation of Band 5 and Band 17 A3
LTE_CA_B3_B20 LTE Advanced Carrier Aggregation of Band 3 and Band 20 A1
LTE_CA_B8_B20 LTE Advanced Carrier Aggregation of Band 8 and Band 20 A3
LTE_CA_B3_B5 LTE Advanced Carrier Aggregation of Band 3 and Band 5 A1
LTE_CA_B4_B7 LTE Advanced Carrier Aggregation of Band 4 and Band 7 A3
LTE_CA_B11_B18 LTE Advanced Carrier Aggregation of Band 11 and Band 18 A5
LTE_CA_B1_B18 LTE Advanced Carrier Aggregation of Band 1 and Band 18 A1
LTE_CA_B1_B19 LTE Advanced Carrier Aggregation of Band 1 and Band 19 A1
LTE_CA_B1_B21 LTE Advanced Carrier Aggregation of Band 1 and Band 21 A5
LTE_CA_B3_B8 LTE Advanced Carrier Aggregation of Band 3 and Band 8 A2
* * *
This TR contains a general part and band specific combination part. The actual
requirements are added to the corresponding technical specifications.
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
[2] 3GPP TR 30.007: \"Guideline on WI/SI for new Operating Bands\"
[3] RP-110702: \"LTE-Advanced Carrier Aggregation of Band 3 and Band 7\"
[4] RP-101391: \"LTE Advanced Carrier Aggregation of Band 4 and Band 17\"
[5] RP-101435: \"LTE Advanced Carrier Aggregation of Band 4 and Band 13\"
[6] RP-111316: \"LTE Advanced Carrier Aggregation of Band 4 and Band 12\"
[7] RP-110372: \"LTE Advanced Carrier Aggregation of Band 5 and Band 12\"
[8] RP-110403: \"LTE Advanced Carrier Aggregation of Band 20 and Band 7\"
[9] RP-110432: \"LTE Advanced Carrier Aggregation of Band 2 and Band 17\"
[10] RP-110433: \"LTE Advanced Carrier Aggregation of Band 4 and Band 5\"
[11] RP-110434: \"LTE Advanced Carrier Aggregation of Band 5 and Band 17\"
[12] Void.
[13] RP-120899: \"LTE Advanced Carrier Aggregation of Band 3 and Band 5\"
[14] RP-111358: \"LTE inter-band Carrier Aggregation (Band 4 + Band 7) \"
[15] RP-111212: \"LTE inter-band carrier aggregation for bands 20+3\"
[16] RP-111213: \"LTE inter-band carrier aggregation for bands 20+8\"
[17] R4-120486: \"CA Band 1 and 19 specific requirements in TS 36.101\", NTT
DOCOMO
[18] R4-120490: \"CA Band 1 and 21 specific requirements in TS 36.101\", NTT
DOCOMO
[19] R4-115502: \"Way forward on interband insertion loss\", Nokia Corporation
[20] RP-120388: \"LTE Advanced Carrier Aggregation of Band 3 and Band 8\"
[21] R4-123308: \"Diplexing and quadplexing between Band 5 and Band 12\",
Qualcomm Incorporated
[22] 3GPP TS 36.101: \"E-UTRA UE radio transmission and reception\".
[23] 3GPP TS 36.133: \"E-UTRA requirements for support of radio resource
management\".
[23] R4-126605: \"TP to 36.850: additional insertion loss for configuration
CA_4A-7A\"
...
# 3 Definitions, symbols and abbreviations
## 3.1 Definitions
For the purposes of the present document, the terms and definitions given in
TR 21.905 [1] and the following apply. A term defined in the present document
takes precedence over the definition of the same term, if any, in TR 21.905
[1].
**Carrier aggregation** : Aggregation of two or more component carriers in
order to support wider transmission bandwidths.
**Channel bandwidth:** The RF bandwidth supporting a single E-UTRA RF carrier
with the transmission bandwidth configured in the uplink or downlink of a
cell. The channel bandwidth is measured in MHz and is used as a reference for
transmitter and receiver RF requirements.
**Inter-band carrier aggregation: Carrier aggregation of component carriers in
different operating bands.**
NOTE: Carriers aggregated in each band can be contiguous or non-contiguous.
## 3.2 Symbols
For the purposes of the present document, the following symbols apply:
F~DL_low~ The lowest frequency of the downlink operating band
F~DL_high~ The highest frequency of the downlink operating band
F~UL_low~ The lowest frequency of the uplink operating band
F~UL_high~ The highest frequency of the uplink operating band
R~IB~ Allowed reference sensitivity relaxation due to support for inter-band
CA operation.
ΔT~IB,c~ Allowed maximum configured output power relaxation due to support for
inter-band CA operation, for serving cell _c_.
## 3.3 Abbreviations
For the purposes of the present document, the abbreviations given in TR 21.905
[1] and the following apply. An abbreviation defined in the present document
takes precedence over the definition of the same abbreviation, if any, in TR
21.905 [1].
A-MPR Additional Maximum Power Reduction
BS Base Station
CA Carrier Aggregation
CA_X-Y CA for band X and band Y where X and Y are the applicable E-UTRA
operating band
CC Component Carrier (bandwidth 1.4, 3, 5, 10, 15 or 20 MHz. Max. 5 CCs
aggregated => max. 100 MHz)
DL Downlink
E-UTRA Evolved UMTS Terrestrial Radio Access
FDD Frequency Division Duplex
PA Power Amplifier
REFSENS Reference Sensitivity power level
TDD Time Division Duplex
UE User Equipment
UL Uplink
# 4 Background
The present document is a technical report for Inter-band Carrier Aggregation
under Rel-11 time frame. It covers both the UE and BS side. The document is
divided in two different parts:
\- Common part: this part covers BS and UE specific which is band combination
independent.
\- Specific band combination part: this part covers each band combination and
its specific issues independently from each other (i.e. one subclause is
defined per band combination)
The specific band combination parts are independent and therefore, the working
speed also differs. Annex A contains a list of all CA combinations covered in
the present document as well as the status of each WI. The content of each
specific combination part can be considered as finalized when the current
status of the WI under Annex A is indicated as "Closed".
## 4.1 TR Maintenance
A single company is responsible for introducing all approved TPs in the
current TR, TR editor. However, it is the responsibility of the rapporteur of
each WI to ensure that the TPs related to the WI have been implemented.
# 5 Inter-band Carrier Aggregation: general part
## 5.1 BS specific
There are four categories of inter-band CA combinations for UE. For BS, it is
typical that different RF modules are used for different bands. Thus, the
categories for BS could be simpler than those for UE. The requirements are
mainly affected by the BS antenna configurations. Currently, the wide band
antenna can support 1.8 GHz to 2.6 GHz frequency range. For the bands lower
than 1 GHz, a separate antenna is needed.
For the approved inter-band CA combinations, the low-high band combinations
using separate antennas can be treated as one category. The situation for
these combinations is similar as current non-CA but co-located BSs. The
requirements are covered by current specifications in this scenario. The other
category is the band combinations which can use the same antenna. The new
issue raised in the antenna sharing scenario is the possible passive
intermodulation.
## 5.2 UE specific
### 5.2.1 Class A1. Low-high band combination without harmonic relation
between bands or intermodulation problem
E-UTRA carrier aggregation class A1 is designed to operate in the operating
bands defined in table 5.2.1-1.
Table 5.2.1-1: Inter-band CA class A1 operating bands
* * *
E-UTRA CA Band E-UTRA Band Uplink (UL) operating band Downlink (DL) operating
band Duplex Mode  
BS receive / UE transmit BS transmit / UE receive  
F~UL_low~ -- F~UL_high~ F~DL_low~ -- F~DL_high~  
CA_1-5 1 1920 MHz -- 1980 MHz 2110 MHz -- 2170 MHz FDD 5 824 MHz -- 849 MHz
869 MHz -- 894MHz  
CA_4-13 4 1710 MHz -- 1755 MHz 2110 MHz -- 2155 MHz FDD 13 777 MHz -- 787 MHz
746 MHz -- 756 MHz  
CA_7-20 7 2500 MHz -- 2570 MHz 2620 MHz -- 2690 MHz FDD 20 832 MHz -- 862 MHz
791 MHz -- 821 MHz  
CA_2-[x] 2 1850 MHz -- 1910 MHz 1930 MHz -- 1990 MHz FDD [x] N/A -- N/A N/A --
N/A  
CA_2-17 2 1850 MHz -- 1910 MHz 1930 MHz -- 1990 MHz FDD 17 704 MHz -- 716 MHz
734 MHz -- 746 MHz  
CA_3-20 3 1710 MHz -- 1785 MHz 1805 MHz -- 1880 MHz FDD 20 832 MHz -- 862 MHz
791 MHz -- 821 MHz
* * *
The lower tolerance of P~CMAX_L~ for constituent bands of a class A1
combination is reduced by the amount given in ∆ _T~IB,c~_ in table 5.2.1-2.
This relaxation is applied for each component carrier when operating either in
single carrier or carrier aggregation configuration with a single uplink CC.
Table 5.2.1-2: ΔT~IB,c~ for the UE that supports inter-band CA class A1
* * *
Inter-band CA Class A1 Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_x-y x 0.3 y
0.3 NOTE: The values in this table reflect what can be achieved with the
present state of the art technology and shall be reconsidered when the state
of the art technology progresses.
* * *
The minimum requirement for reference sensitivity for constituent bands of a
class A1 combination shall be increased by the amount given in ΔR~IB~ in table
5.2.1-3. This relaxation is applied for each component carrier when operating
either in single carrier or carrier aggregation configuration with a single
uplink CC.
Table 5.2.1-3: ΔR~IB~ for the UE that supports inter-band CA class A1
* * *
Inter-band CA Class A1 Configuration E-UTRA Band ΔR~IB~ [dB] CA_x-y x 0 y 0
* * *
### 5.2.2 Class A2. Low-high band combination with harmonic relation between
bands
### 5.2.3 Class A3. Low-low or high-high band combination without
intermodulation problem (low order IM)
### 5.2.4 Class A4. Low-low, low-high or high-high band combination with
intermodulation problem (low order IM)
### 5.2.5 Class A5. Combination except for A1 -- A4
## 5.3 RRM specific
The RRM requirements will be impacted by the relaxation of the reference
sensitivity for UEs supporting inter-band carrier aggregation. table 5.3-1
lists the required modification of the RRM requirements in TS 36.133 [23].
Similar requirements for Rel-10 with only 1 UL carrier will be introduced in
Rel-10 of TS 36.133 [23].
Table 5.3-1: Modification of the RRM requirements in TS 36.133 for Inter-Band
carrier aggregations.
+---------+----------------------------+----------------------------+ | Section | Requirements | Proposed changes in RRM | | | | Requirements | +---------+----------------------------+----------------------------+ | 9.1 | E-UTRAN measurements | | +---------+----------------------------+----------------------------+ | | Table 9.1.2.1-1: RSRP | For the UE which supports | | | Intra frequency absolute | an inter-band carrier | | | accuracy | aggregation configuration | | | | with 1 uplink carrier in | | | | one E-UTRA band, the Io | | | | level in these tables will | | | | be increased by the amount | | | | given in ΔR~IB,~c for 1 | | | | uplink carrier | | | | configuration for the | | | | applicable E-UTRA bands of | | | | the inter-band carrier | | | | aggregation. | | | | | | | | For the UE which supports | | | | an inter-band carrier | | | | aggregation configuration | | | | with 2 uplink carriers, | | | | one in each E-UTRA band, | | | | the Io level in these | | | | tables will be increased | | | | by the amount given in | | | | ΔR~IB,~c for 2 uplink | | | | carrier configuration for | | | | the applicable E-UTRA | | | | bands of the inter-band | | | | carrier aggregation. | +---------+----------------------------+----------------------------+ | | Table 9.1.2.2-1: RSRP | | | | Intra frequency relative | | | | accuracy | | +---------+----------------------------+----------------------------+ | | Table 9.1.2.3-1: RSRP | | | | Intra frequency absolute | | | | accuracy under time domain | | | | measurement resource | | | | restriction | | +---------+----------------------------+----------------------------+ | | Table 9.1.2.4-1: RSRP | | | | Intra frequency relative | | | | accuracy under time domain | | | | measurement resource | | | | restriction | | +---------+----------------------------+----------------------------+ | | Table 9.1.3.1-1: RSRP | | | | Inter frequency absolute | | | | accuracy | | +---------+----------------------------+----------------------------+ | | Table 9.1.3.2-1: RSRP | | | | Inter frequency relative | | | | accuracy | | +---------+----------------------------+----------------------------+ | | Table 9.1.5.1-1: RSRQ | | | | Intra frequency absolute | | | | accuracy | | +---------+----------------------------+----------------------------+ | | Table 9.1.5.2-1: RSRQ | | | | Intra frequency absolute | | | | accuracy under time domain | | | | measurement resource | | | | restriction | | +---------+----------------------------+----------------------------+ | | Table 9.1.6.1-1: RSRQ | | | | Inter frequency absolute | | | | accuracy | | +---------+----------------------------+----------------------------+ | | Table 9.1.6.2-1: RSRQ | | | | Inter frequency relative | | | | accuracy | | +---------+----------------------------+----------------------------+ | | Table 9.1.9.1-1: UE Rx -- | | | | Tx time difference | | | | measurement accuracy | | +---------+----------------------------+----------------------------+ | | Table 9.1.10.1-1: RSTD | | | | measurement accuracy | | +---------+----------------------------+----------------------------+ | | Table 9.1.10.2-1: RSTD | | | | measurement accuracy | | +---------+----------------------------+----------------------------+ | Annex B | **Conditions for RRM | | | | requirements applicability | | | | for operating bands** | | +---------+----------------------------+----------------------------+ | | Table B.1.1-1 Conditions | For the UE which supports | | | for measurements of | an inter-band carrier | | | intra-frequency E-UTRAN | aggregation configuration | | | cells for cell | with 1 uplink carrier in | | | re-selection | one E-UTRA band, the RSRP | | | | and SCH_RP levels in | | | | these tables will be | | | | increased by the amount | | | | given in ΔR~IB,~c for 1 | | | | uplink carrier | | | | configuration for the | | | | applicable E-UTRA bands of | | | | the inter-band carrier | | | | aggregation. | | | | | | | | For the UE which supports | | | | an inter-band carrier | | | | aggregation configuration | | | | with 2 uplink carriers, | | | | one in each E-UTRA band, | | | | the RSRP and SCH_RP | | | | levels in these tables | | | | will be increased by the | | | | amount given in ΔR~IB,~c | | | | for 2 uplink carrier | | | | configuration for the | | | | applicable E-UTRA bands of | | | | the inter-band carrier | | | | aggregation. | +---------+----------------------------+----------------------------+ | | Table B.2.1-1. E-UTRAN | | | | intra-frequency | | | | measurements | | +---------+----------------------------+----------------------------+ | | Table B.2.3-1. E-UTRAN | | | | inter-frequency | | | | measurements | | +---------+----------------------------+----------------------------+ | | Table B.2.4-1. E-UTRAN | | | | inter-frequency | | | | measurements with | | | | autonomous gaps | | +---------+----------------------------+----------------------------+ | | Table B.2.5-1 E-UTRAN | | | | OTDOA intra-frequency RSTD | | | | measurements | | +---------+----------------------------+----------------------------+ | | Table B.2.7-1. | | | | Measurements of the | | | | secondary component | | | | carrier with deactivated | | | | SCell | | +---------+----------------------------+----------------------------+ | | Table B.2.8-1 E-UTRAN | | | | intra-frequency | | | | measurements under time | | | | domain measurement | | | | resource Restriction | | +---------+----------------------------+----------------------------+ | | Table B.3.1-1 | | | | Intra-frequency absolute | | | | RSRP and RSRQ Accuracy | | | | Requirements | | +---------+----------------------------+----------------------------+ | | Table B.3.8-1 | | | | Intra-frequency relative | | | | RSRP accuracy requirements | | +---------+----------------------------+----------------------------+
### 5.3.1 Class A1. Low-high band combination without harmonic relation
between bands or intermodulation problem
All inter-band carrier aggregations that belong to Class A1. Low-high band
combination without harmonic relation between bands shall follow the
requirements defined in this section unless explicitly stated otherwise.
The UE measurement requirements, including OTDOA RSTD, for carrier aggregation
specified in subclause 8.3 and 8.4 in TS 36.133 [23] for primary component
carrier and secondary component carrier are defined in a band agnostic manner.
The measurement accuracy requirements, including OTDOA RSTD, for carrier
aggregation, as defined in subclause 9.1.11 and 9.1.12 in TS 36.133 [23] for
primary component carrier and secondary component carrier are also in a band
agnostic manner.
Since there is no change on reference sensitivity power level (ΔRib= 0 dB) for
2 DL/1 UL for Class A1 CA combinations, there is no need to define additional
measurement requirements specific for Class A1 CA combinations for 2 DL/1 UL
cases.
# 6 Inter-band Carrier Aggregation: band combination specific part
## 6.1 Class A1. Low-high band combination without harmonic relation between
bands or intermodulation problem
### 6.1.1 LTE Advanced Carrier Aggregation of Band 4 and Band 13 (1 UL)
CA_4-13 is designed to operate in the operating bands defined in table
6.1.1-1.
Table 6.1.1-1: Inter-band CA operating bands
* * *
E-UTRA CA Band E-UTRA Band Uplink (UL) operating band Downlink (DL) operating
band Duplex Mode  
BS receive / UE transmit BS transmit / UE receive  
F~UL_low~ -- F~UL_high~ F~DL_low~ -- F~DL_high~  
CA_4-13 4 1710 MHz -- 1755 MHz 2110 MHz -- 2155 MHz FDD 13 777 MHz -- 787 MHz
746 MHz -- 756 MHz
* * *
#### 6.1.1.1 List of specific combination issues
##### 6.1.1.1.1 Channel bandwidths per operating band for CA
Supported channel bandwidths per operating band for CA_4-13 are shown in table
6.1.1.1.1-1.
Table 6.1.1.1.1-1: Supported E-UTRA bandwidths per CA configuration for inter-
band CA
* * *
CA operating / channel bandwidth Bandwidth combination set  
E-UTRA CA Configuration E-UTRA Bands 1.4 MHz 3 MHz 5 MHz 10 MHz 15 MHz 20 MHz  
CA_4-13 4 Yes Yes Yes Yes 0 13 Yes  
4 Yes Yes 1 13 Yes
* * *
##### 6.1.1.1.2 Co-existence studies for CA_4-13 (1 UL)
The 2^nd^ and 3^rd^ order harmonics and IMD products caused in the BS by
transmitting of Band 4 and Band 13 DL carriers can be calculated as shown in
table 6.1.1.1.2-1 below:
Table 6.1.1.1.2-1: Band 4 and Band 13 DL harmonics and IMD products
* * *
BS DL carriers f1_low f1_high f2_low f2_high DL frequency (MHz) 746 756 2110
2155 2^nd^ order harmonics frequency range (MHz) 1492 1512 4220 4310 3^rd^
order harmonics frequency range (MHz) 2238 2268 6330 6465 2^nd^ order IMD
products (f2_low -- f1_high) (f2_high -- f1_low) (f2_low + f1_low) (f2_high +
f1_high) IMD frequency limits (MHz) 1354 1409 2856 2911 3^rd^ order IMD
products (f2_low -- 2*f1_high) (f2_high -- 2*f1_low) (2*f2_low -- f1_high)
(2*f2_high -- f1_low) IMD frequency limits (MHz) 598 663 3464 3564 3^rd^ order
IMD products (2*f1_low + f2_low) (2*f1_high + f2_high) (2*f2_low + f1_low)
(2*f2_high + f1_high) IMD frequency limits (MHz) 3602 3667 4966 5066 3^rd^
order IMD products (f1_low -- f2_high + f2_low) (f1_high + f2_high -- f2_low)
(f2_low -- f1_high + f1_low) (f2_high + f1_high -- f1_low) IMD frequency
limits (MHz) 701 801 2100 2165
* * *
It can be seen from table 6.1.1.1.2-1 that the 2^nd^ and 3^rd^ harmonics as
well as the 2^nd^ IMD products of BS transmitting in Bands 4 and 13 will not
fall into the BS receive band of any frequency band currently defined in 3GPP,
but the 3^rd^ IMD products supporting CA of Band 4 and Band 13 may fall into
the BS receive band of Bands 12, 13, 14, 17, 22, 42 and 43. Note that the
calculation in table 6.1.1.1.2-1 assumes the BS is transmitting with the whole
45 MHz DL frequency of Band 4 and the whole 10 MHz DL frequency of Band 13. If
the BS is only transmitting an up to 20 MHz DL in Band 4 and a 10 MHz DL in
Band 13 as stated in the WIDS, then the 3rd IMD products will not fall into
the BS receive band of Bands 12, 13, 14 and 17.
With the performances of the current BS antenna system, transmit and receive
path components, amplifiers, pre-distortion algorithms and filters, it is
expected that the IMD interference generated within the Band 22, 42 or 43
receiver would be well below the receiver noise floor eliminating the
possibility of receiver desensitization, provided that Bands 4 and 13 BS
transmitters do not share the same antenna with Band 22, 42 or 43 BS receiver.
And it is recommended that Bands 4 and 13 BS transmitters should not share the
same antenna with Band 22, 42 or 43 BS receiver, unless the antenna path meets
very stringent 3rd order PIM specification so that the PIM will not cause Band
22, 42 or 43 BS receiver desensitization.
##### 6.1.1.1.3 ΔT~IB,c~ and ΔR~IB~ (1 UL)
For the UE which supports CA_4A-13A the ΔT~IB,c~ is defined for applicable
bands in table 6.1.1.1.**3** -**1**.
Table 6.1.1.1.3-1: ΔT~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_4A-13A 4 0.3 13 0.3
* * *
For the UE which supports CA_4A-13A the ΔR~IB~ is defined for applicable bands
in table 6.1.1.1.3-2.
Table 6.1.1.1.3-2: ΔR~IB~
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB~ [dB] CA_4A-13A 4 0 13 0
* * *
### 6.1.2 LTE Advanced Carrier Aggregation of Band 7 and Band 20
CA_**7-20** is designed to operate in the operating bands defined in table
**6.1.2-1**.
Table 6.1.2-1: Inter-band CA operating bands
* * *
E-UTRA CA Band E-UTRA Band Uplink (UL) operating band Downlink (DL) operating
band Duplex Mode  
BS receive / UE transmit BS transmit / UE receive  
F~UL_low~ -- F~UL_high~ F~DL_low~ -- F~DL_high~  
CA_7-20 7 2500 MHz -- 2570 MHz 2620 MHz -- 2690 MHz FDD 20 832 MHz -- 862 MHz
791 MHz -- 821 MHz
* * *
#### 6.1.2.1 List of specific combination issues
##### 6.1.2.1.1 Channel bandwidths per operating band for CA
Supported channel bandwidths per operating band for CA_7-20 are shown in table
6.1.2.1.1-1.
Table 6.1.2.1-1: Supported E-UTRA bandwidths per CA configuration for inter-
band CA
* * *
CA operating / channel bandwidth  
E-UTRA CA Configuration E-UTRA Bands 1.4 MHz 3 MHz 5 MHz 10 MHz 15 MHz 20 MHz
CA_7A-20A 7 Yes Yes Yes 20 Yes Yes
* * *
##### 6.1.2.1.2 Co-existence studies for 1 UL/2 DL
Table 6.1.2.1.2-1 gives the intermodulation products for band 20 + band 7 CA
with 2 DLs. For the 3-tone IMD analysis the maximum transmission as defined in
table 6.1.2.1-1 is considered. Three-tone third order IMD products can fall
into the band 20 receiver. However, these products will not fall into the BS
own receive block if the frequency range as defined with the channel
bandwidths given in table 6.1.2.1-1 are used for the more detailed IMD
calculation.
Considering bands in the same geographical area we observe that the BS
distortion could fall into the BS receive bands of Band 22, 38 and 42. With
the performances of the current BS antenna system, transmit and receive path
components, amplifiers, pre-distortion algorithms and filters the IMDs
generated within the band 22, 38 and 42 receiver should be well below the
receiver noise floor eliminating the possibility of receiver desensitization.
Provided that the Bands 20 and 7 BS transmitters should not share the same
antenna with Band 22, 38 or 42 BS receiver.
Table 6.1.2.1.2-1: 2 DLs B7 + B20 IMD products
* * *
BS DL carriers f1_low f1_high f2_low f2_high
DL frequency (MHz) 791 821 2620 2690
2^nd^ order harmonics frequency range (MHz) 1582 to 1642 5240 to 5380
3^rd^ order harmonics frequency range (MHz) 2373 to 2463 7860 to 8070
Two-tone 2^nd^ order IMD products f2_low -- f1_high f2_high -- f1_low
f2_low + f1_low f2_high + f1_high
IMD frequency range (MHz) 1799 to 1899 3411 to 3511
Two-tone 3^rd^ order IMD products 2*f1_low -- f2_high 2*f1_high -- f2_low
2*f2_low -- f1_high 2* f2_high -- f1_low
IMD frequency range (MHz) 978 to 1108 4419 to 4589
Three-tone 3^rd^ order IMD products (f1_low --\ (f1_high +\ (f2_low --\
(f2_high +\ max BW f2) max BW f2) max BW f1) max BW f1)
IMD frequency range (MHz) 771 to 841 2610 to 2700
* * *
Table 6.1.2.1.2-2 gives the intermodulation products for band 20 + band 7 CA
with 1 UL. None of the intermodulation products fall into the own receive
bands. For the case where 3rd order harmonic of band 20 falls into the
downlink of band 38, the current TS 36.101 [22] already has requirements
covering this case. For the case where 3rd order harmonic of band 20 falls
into Band 7 uplink when both carriers are active, since the suppression of
harmonic is relative large (e.g. 80 dB) compared to the power difference
between the two active carriers, the impact to high band transmitter can be
ignored. Hence no further relaxation is needed.
Table 6.1.2.1.2-2: 1 UL B7 + B20 harmonic products
* * *
BS DL carriers f1_low f1_high f2_low f2_high UL frequency (MHz) 832 862 2500
2570 2^nd^ order harmonics frequency range (MHz) 1664 to 1724 5000 to 5140  
3^rd^ order harmonics frequency range (MHz) 2496 to 2586 7500 to 7710
* * *
##### 6.1.2.1.3 Co-existence studies for 2 UL/2 DL
Table 6.1.2.1.3-1 gives the intermodulation products for band 20 + band 7 CA
with 2 ULs. For the 3-tone IMD analysis the maximum transmission BW as defined
in table 6.1.2.1-1 is considered. Two-tone and three-tone third order IMD
products can fall into the band 20 receiver. However, these products will not
fall into the UE own receive block if the frequency range as defined with the
channel bandwidths given in table 6.1.2.1-1 are used for the more detailed IMD
calculation.
Considering bands in the same geographical area we observe that the UE
distortion falls into the UE receive bands of Band 38 and 42. The magnitude of
these possible IMD products have to be further studied with respect to
spurious emission limits into these bands.
Table 6.1.2.1.3-1: 2 ULs B7 + B20 IMD products
* * *
BS DL carriers f1_low f1_high f2_low f2_high
DL frequency (MHz) 832 862 2500 2570
Two-tone 2^nd^ order IMD products f2_low -- f1_high f2_high -- f1_low
f2_low + f1_low f2_high + f1_high
IMD frequency range (MHz) 1638 to 1738 3332 to 3432
Two-tone 3^rd^ order IMD products 2*f1_low -- f2_high 2*f1_high -- f2_low
2*f2_low -- f1_high 2* f2_high -- f1_low
IMD frequency range (MHz) 776 to 906 4138 to 4308
Three-tone 3^rd^ order IMD products (f1_low --\ (f1_high +\ (f2_low --\
(f2_high +\ max BW f2) max BW f2) max BW f1) max BW f1)
IMD frequency range (MHz) 812 to 882 2490 to 2580
* * *
##### 6.1.2.1.4 ΔT~IB,c~ and ΔR~IB~ (1 UL/ 2 DL)
For the UE which supports CA_**7** -**20** the ΔT~IB,c~ is defined for
applicable bands in table 6.1.2.1.**4** -**1**.
Table 6.1.2.1.4-1: ΔT~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_7A-20A 7 0.3 20 0.3
NOTE: The values in the table reflect what can be achieved with the present
state of the art technology. They shall be reconsidered when the state of the
art technology progresses.
* * *
For the UE which supports CA_**7-20** the ΔR~IB~ is defined for applicable
bands in table 6.1.2.1.**4** -**2**.
Table 6.1.2.1.4-2: ΔR~IB~
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB~ [dB] CA_7A-20A 7 0 20 0
* * *
### 6.1.3 LTE-Advanced Carrier Aggregation of Band 2 and Band 17 (1 UL)
#### 6.1.3.1 List of specific combination issues
##### 6.1.3.1.1 Channel bandwidths per operating band for CA
##### 6.1.3.1.2 Co-existence studies for CA_2-17
The 2^nd^ and 3^rd^ order harmonics and IMD products caused in the BS by
transmitting of Band 2 and Band 17 DL carriers can be calculated as shown in
table 6.1.3.1.2-1 below:
Table 6.1.3.1.2-1: Band 2 and Band 17 DL harmonics and IMD products
* * *
BS DL carriers f1_low f1_high f2_low f2_high DL frequency (MHz) 734 746 1930
1990 2^nd^ harmonics frequency limits (MHz) 1468 1492 3860 3980 3^rd^
harmonics frequency limits (MHz) 2202 2238 5790 5970 2^nd^ order IMD products
(f2_low -- f1_high) (f2_high -- f1_low) (f2_low + f1_low) (f2_high + f1_high)
IMD frequency limits (MHz) 1184 1256 2664 2736 3^rd^ order IMD products
(f2_low -- 2*f1_high) (f2_high -- 2*f1_low) (2*f2_low -- f1_high) (2*f2_high
-- f1_low) IMD frequency limits (MHz) 438 522 3114 3246 3^rd^ order IMD
products (2*f1_low + f2_low) (2*f1_high + f2_high) (2*f2_low + f1_low)
(2*f2_high + f1_high) IMD frequency limits (MHz) 3398 3482 4594 4726 3^rd^
order IMD products (f1_low -- f2_high + f2_low) (f1_high + f2_high -- f2_low)
(f2_low -- f1_high + f1_low) (f2_high + f1_high -- f1_low) IMD frequency
limits (MHz) 674 806 1918 2002 3^rd^ order IMD products (with maximum channel
bandwidth) (f1_low -- f2_BWmax) (f1_high + f2_BWmax) (f2_low -- f1_BWmax)
(f2_high + f1_BWmax) IMD frequency limits (MHz) 714 766 1920 2000
* * *
It can be seen from table 6.1.3.1.2-1 that the 2^nd^ and 3^rd^ harmonics of BS
transmitting in Bands 2 and 17 will not fall into the BS receive band of any
frequency band currently defined in 3GPP, but the 2^nd^ IMD products may fall
into the BS receive band of Band 41, and the 3^rd^ IMD products may fall into
the BS receive band of Bands 1, 12, 13, 14, 17, 22, 23, 28, 33, 36, 37, 39, 42
and 44. Note that the calculation in table 6.1.3.1.2-1 (except the last row)
assumes the BS is transmitting with the whole 60 MHz DL frequency of Band 2
and the whole 12 MHz DL frequency of Band 17. If the BS is only transmitting
an up to 20 MHz DL in Band 2 and a 10 MHz DL in Band 17 as stated in the WIDS,
then the 3^rd^ IMD products will not fall into the BS receive band of Bands
13, 14, 23, 33 and 39 as shown in the last row in table 6.1.3.1.2-1.
Note that Bands 1, 28, 33, 39 and 44 are not intended for use in the same
geographical area as Bands 2 and 17. Moreover, co-location of Band (2 + 17)
transmitter and Band 36 or 37 transceiver implies FDD/TDD co-location on
adjacent frequencies which requires the use of certain site-engineering
solutions to avoid mutual interference. Furthermore, the 3^rd^ IMD products
for Band (2 + 17) DL at 714 -- 766 MHz will not fall into the Band 12 or 17 UL
if the UL carrier is located out of this frequency range (e.g. locate the 10
MHz UL carrier for Band 12 or 17 at 704 -- 714 MHz) or the Band 2 DL bandwidth
is limited to not wider than 18 MHz.
With the performances of the current BS antenna system, transmit and receive
path components, amplifiers, pre-distortion algorithms and filters, it is
expected that the IMD interference generated within the Band 22, 41 or 42
receiver would be well below the receiver noise floor eliminating the
possibility of receiver desensitization, provided that Bands 2 and 17 BS
transmitters do not share the same antenna with Band 22, 41 or 42 BS receiver.
Therefore, it is recommended that Bands 2 and 17 BS transmitters should not
share the same antenna with Band 22, 41 or 42 BS receiver, or with Band 12 or
17 BS receiver unless the Band 12 or 17 UL carrier is located out of the
frequency range at 714 -- 766 MHz or the Band 2 DL bandwidth is limited to not
wider than 18 MHz, unless the antenna path meets very stringent 3^rd^ order
PIM specification so that the PIM will not cause Band 12, 17, 22, 41 or 42 BS
receiver desensitization.
### 6.1.4 LTE-Advanced Carrier Aggregation of Band 4 and Band 5 (1 UL)
#### 6.1.4.1 List of specific combination issues
##### 6.1.4.1.1 Channel bandwidths per operating band for CA
##### 6.1.4.1.2 Co-existence studies for CA_4-5
The 2^nd^ and 3^rd^ order harmonics and IMD products caused in the BS by
transmitting of band 4 and band 5 DL carriers can be calculated as shown in
table 6.1.4.1.2-1 below:
Table 6.1.4.1.2-1: Band 4 and Band 5 DL harmonics and IMD products
* * *
BS DL carriers f1_low f1_high f2_low f2_high DL frequency (MHz) 869 894 2110
2155 2^nd^ order harmonics frequency range (MHz) 1738 1788 4220 4310 3^rd^
order harmonics frequency range (MHz) 2607 2682 6330 6465 2^nd^ order IMD
products (f2_low -- f1_high) (f2_high -- f1_low) (f2_low + f1_low) (f2_high +
f1_high) IMD frequency limits (MHz) 1216 1286 2979 3049 3^rd^ order IMD
products (f2_low -- 2*f1_high) (f2_high -- 2*f1_low) (2*f2_low -- f1_high)
(2*f2_high -- f1_low) IMD frequency limits (MHz) 322 417 3326 3441 3^rd^ order
IMD products (2*f1_low + f2_low) (2*f1_high + f2_high) (2*f2_low + f1_low)
(2*f2_high + f1_high) IMD frequency limits (MHz) 3848 3943 5089 5204 3^rd^
order IMD products (f1_low -- f2_high + f2_low) (f1_high + f2_high -- f2_low)
(f2_low -- f1_high + f1_low) (f2_high + f1_high -- f1_low) IMD frequency
limits (MHz) 824 939 2085 2180 3^rd^ order IMD products (with maximum channel
bandwidth) (f1_low -- f2_BWmax) (f1_high + f2_BWmax) (f2_low -- f1_BWmax)
(f2_high + f1_BWmax) IMD frequency limits (MHz) 849 914 2090 2175
* * *
It can be seen from table 6.1.4.1.2-1 that the 2^nd^ and 3^rd^ harmonics of BS
transmitting in band 5 may fall into the BS receive band of bands 3, 4, 9, 10,
38 and 41, while the 3^rd^ IMD products caused by BS supporting carrier
aggregation of band 4 and band 5 may fall into the BS receive band of bands 5,
6, 8, 18, 19, 20, 22, 26 and 42. Note that the calculation in table
6.1.4.1.2-1 (except the last row) assumes the BS is transmitting with the
whole 45 MHz DL frequency of and 4 and the whole 25 MHz DL frequency of and 5.
If the BS is only transmitting 10, 15 or 20 MHz DL in band 4 and band 5 as
stated in the WIDS, then the 3^rd^ IMD products will not fall into the BS
receive band of bands 5, 6, 18, 19 and 26 as shown in the last row in table
6.1.4.1.2-1.
Note that bands 3, 6, 8, 9, 18, 19, 20 and 38 are not intended for use in the
same geographical area as bands 4 and 5. With the performances of the current
BS antenna system, transmit and receive path components, amplifiers, pre-
distortion algorithms and filters, it is expected that the harmonics
interference generated within the band 4, 10 or 41 receiver would be well
below the receiver noise floor eliminating the possibility of receiver
desensitization.
On the other hand, it is recommended that bands 4 and 5 BS transmitters should
not share the same antenna with band 22 or 42 BS receiver, unless the antenna
path meets very stringent 3^rd^ order PIM specification so that the PIM will
not cause band 22 or 42 BS receiver desensitization.
### 6.1.5 LTE inter-band carrier aggregation of Band 3 and Band 20
CA_3-20 inter-band combination is designed to operate in the following bands
defined in table 6.1.5-1.
Table 6.1.5-1: Inter-band CA operating bands
+-------+-------+-------+-------+-------+-------+----+-------+-----+ | E | E | U | Dow | D | | | | | | -UTRA | -UTRA | plink | nlink | uplex | | | | | | CA | | (UL) | (DL) | Mode | | | | | | Band | Band | oper | oper | | | | | | | | | ating | ating | | | | | | | | | band | band | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | | | BS | BS | | | | | | | | | re | tra | | | | | | | | | ceive | nsmit | | | | | | | | | / UE | / UE | | | | | | | | | tra | re | | | | | | | | | nsmit | ceive | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | | | F~UL\ | F~DL\ | | | | | | | | | _low~ | _low~ | | | | | | | | | -- | -- | | | | | | | | | F | F | | | | | | | | | ~UL_ | ~DL_ | | | | | | | | | high~ | high~ | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | CA\ | 20 | 832 | -- | 862 | 791 | -- | 821 | FDD | | _3-20 | | MHz | | MHz | MHz | | MHz | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | | 3 | 1710 | -- | 1785 | 1805 | -- | 1880 | | | | | MHz | | MHz | MHz | | MHz | | +-------+-------+-------+-------+-------+-------+----+-------+-----+
#### 6.1.5.1 List of specific combination issues
##### 6.1.5.1.1 Channel bandwidths per operating band for CA
Supported channel bandwidths per operating band for CA_3-20 are shown in table
6.1.5.1.1-1.
Table 6.1.5.1.1-1: Supported E-UTRA bandwidths per CA configuration for inter-
band CA
* * *
E-UTRA band / channel bandwidth
E-UTRA\ E-UTRA Bands 1.4 MHz 3 MHz 5 MHz 10 MHz 15 MHz 20 MHz CA Band
CA_3A-20A 20 Yes Yes
                                    3                                Yes     Yes      Yes      Yes
* * *
##### 6.1.5.1.2 Co-existence studies for 1 UL/2 DL
Table 6.1.5.1.2-1 gives the intermodulation products for band 20 + band 3 CA
with 2 DLs. For the 3-tone IMD analysis the maximum transmission as defined in
table 6.1.2.1-1 is considered. Three-tone third order IMD products can fall
into the band 20 receiver. However, these products will not fall into the BS
own receive block if the frequency range as defined with the channel
bandwidths given in table 6.1.5.1.1-1 are used for the more detailed IMD
calculation.
Considering bands in the same geographical area we observe that the BS
distortion could fall into the BS receive bands of Band 42 and 43. With the
performances of the current BS antenna system, transmit and receive path
components, amplifiers, pre-distortion algorithms and filters the IMDs
generated within the band 42 and 43 receiver should be well below the receiver
noise floor eliminating the possibility of receiver desensitization. Provided
that the Bands 20 and 7 BS transmitters should not share the same antenna with
Band 42 or 43 BS receiver.
Table 6.1.5.1.2-1: 2 DLs B3 + B20 IMD products
+-------------+-------------+-------------+-------------+-------------+ | BS DL | f1_low | f1_high | f2_low | f2_high | | carriers | | | | | +-------------+-------------+-------------+-------------+-------------+ | DL | 791 | 821 | 1805 | 1880 | | frequency | | | | | | (MHz) | | | | | +-------------+-------------+-------------+-------------+-------------+ | 2^nd^ order | 1582 to | 3610 to | | | | harmonics | 1642 | 3760 | | | | frequency | | | | | | range (MHz) | | | | | +-------------+-------------+-------------+-------------+-------------+ | 3^rd^ order | 2373 to | 5415 to | | | | harmonics | 2463 | 5640 | | | | frequency | | | | | | range (MHz) | | | | | +-------------+-------------+-------------+-------------+-------------+ | Two-tone | f2_low -- | f2_high | f2_low + | f2_high + | | 2^nd^ order | f1_high | -- f1_low | f1_low | f1_high | | IMD | | | | | | products | | | | | +-------------+-------------+-------------+-------------+-------------+ | IMD | 984 to 1089 | 2596 to | | | | frequency | | 2701 | | | | range (MHz) | | | | | +-------------+-------------+-------------+-------------+-------------+ | Two-tone | 2*f1_low |  | 2*f2_low | 2* | | 3^rd^ order | -- | 2*f1_high | -- | f2_high -- | | IMD | f2_high | -- f2_low | f1_high | f1_low | | products | | | | | | | & | & | & | & | | | | | | | | | (2*f1_low | ( | (2*f2_low | ( | | | + f2_low) | 2*f1_high | + f1_low) | 2*f1_high | | | | + f2_high) | | + f2_high) | +-------------+-------------+-------------+-------------+-------------+ | IMD | 163 to 298 | 2789 to | | | | frequency | | 2969 | | | | range (MHz) | 3387 to | | | | | | 3522 | 4401 to | | | | | | 4581 | | | +-------------+-------------+-------------+-------------+-------------+ | Three-tone | (f1_low | (f1_high | (f2_low | (f2_high | | 3^rd^ order | --\ | +\ | --\ | +\ | | IMD | max BW f2) | max BW f2) | max BW f1) | max BW f1) | | products | | | | | +-------------+-------------+-------------+-------------+-------------+ | IMD | 771 to 841 | 1795 to | | | | frequency | | 1890 | | | | range (MHz) | | | | | +-------------+-------------+-------------+-------------+-------------+
Table 6.1.2.1.2-2 gives the intermodulation products for band 20 + band 3 CA
with 1 UL. None of the intermodulation products fall into the own receive
bands. For the case when 3rd order harmonics from band 20 UL impact both B38
(TDD) and B7 UL, TS 36.101 [22] already considers this case, and therefore no
further requirements are needed.
Table 6.1.5.1.2-2: 1 UL B3 + B20 harmonic products
* * *
UE UL carriers f1_low f1_high f2_low f2_high UL frequency (MHz) 832 862 1710
1785 2^nd^ order harmonics frequency range (MHz) 1664 to 1724 3420 to 3570  
3^rd^ order harmonics frequency range (MHz) 2496 to 2586 5130 to 5355
* * *
##### 6.1.5.1.3 Co-existence studies for 2 UL/2 DL
Table 6.1.5.1.3-1 gives the intermodulation products for band 20 + band 3 CA
with 2 ULs. For the 3-tone IMD analysis the maximum transmission BW as defined
in table 6.1.5.1.1-1 is considered. Three-tone third order IMD products can
fall into the band 20 receiver. However, these products will not fall into the
UE own receive block if the frequency range as defined with the channel
bandwidths given in table 6.1.5.1.1-1 are used for the more detailed IMD
calculation.
Considering bands in the same geographical area we observe that the UE
distortion could fall into the UE receive bands of Band 7, 8, 38 and 42. The
magnitudes of these possible IMD products have to be further studied with
respect to spurious emission limits into these bands.
Table 6.1.5.1.3-1: 2 ULs B3 + B20 IMD products
+-------------+-------------+-------------+-------------+-------------+ | BS DL | f1_low | f1_high | f2_low | f2_high | | carriers | | | | | +-------------+-------------+-------------+-------------+-------------+ | DL | 832 | 862 | 1710 | 1785 | | frequency | | | | | | (MHz) | | | | | +-------------+-------------+-------------+-------------+-------------+ | Two-tone | f2_low -- | f2_high | f2_low + | f2_high + | | 2^nd^ order | f1_high | -- f1_low | f1_low | f1_high | | IMD | | | | | | products | | | | | +-------------+-------------+-------------+-------------+-------------+ | IMD | 848 to 953 | 2542 to | | | | frequency | | 2647 | | | | range (MHz) | | | | | +-------------+-------------+-------------+-------------+-------------+ | Two-tone | 2*f1_low |  | 2*f2_low | 2* | | 3^rd^ order | -- | 2*f1_high | -- | f2_high -- | | IMD | f2_high | -- f2_low | f1_high | f1_low | | products | | | | | | | & | & | & | & | | | | | | | | | (2*f1_low | ( | (2*f2_low | ( | | | + f2_low) | 2*f1_high | + f1_low) | 2*f1_high | | | | + f2_high) | | + f2_high) | +-------------+-------------+-------------+-------------+-------------+ | IMD | 14 to 121 | 2558 to | | | | frequency | | 2738 | | | | range (MHz) | 3374 to | | | | | | 3509 | 4252 to | | | | | | 4432 | | | +-------------+-------------+-------------+-------------+-------------+ | Three-tone | (f1_low | (f1_high | (f2_low | (f2_high | | 3^rd^ order | --\ | +\ | --\ | +\ | | IMD | max BW f2) | max BW f2) | max BW f1) | max BW f1) | | products | | | | | +-------------+-------------+-------------+-------------+-------------+ | IMD | 812 to 882 | 1700 to | | | | frequency | | 1795 | | | | range (MHz) | | | | | +-------------+-------------+-------------+-------------+-------------+
##### 6.1.5.1.4 ∆T~IB~ and ∆R~IB~ values (1 UL/2 DL)
For 2 DL and 1 UL the ∆T~IB,c~ and ∆R~IB~ values are given in the tables
below:
Table 6.1.5.1.4-1: ΔT~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_3A-20A 20 0.3 3 0.3
NOTE: The values in the table reflect what can be achieved with the present
state of the art technology. They shall be reconsidered when the state of the
art technology progresses.
* * *
Table 6.1.5.1.4-2: ΔR~IB~
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB~ [dB] CA_3A-20A 20 0 3 0
* * *
### 6.1.6 LTE Advanced Carrier Aggregation of Band 3 and Band 5 (1 UL)
Table 6.1.6-1: Inter-band CA
E-UTRA CA Band | E-UTRA Band | Uplink (UL) band | Downlink (DL) band | Duplex mode |  |  |  |  |  |   
---|---|---|---|---|---|---|---|---|---|---  
|  | BS receive / UE transmit | Channel BW (MHz) | BS transmit / UE receive | Channel BW (MHz) |  |  |  |  |   
|  | FUL_low – FUL_high |  | FUL_low – FUL_high |  |  |  |  |  |   
CA_3-5 | 3 | 1710 MHz | – | 1785 MHz | 10, 15, 20  
(note 1) | 1805 MHz | – | 1880 MHz | 10, 15, 20 | FDD  
| 5 | 824 MHz | – | 849 MHz | 10 (note 1) | 869 MHz | – | 894 MHz | 10 |   
NOTE 1: Only one uplink component carrier is to be supported in any of the two frequency bands at any time. |  |  |  |  |  |  |  |  |  |   
#### 6.1.6.1 List of specific combination issues
##### 6.1.6.1.1 Channel bandwidths per operating band for CA
Table 6.1.6.1.1-1: Supported E-UTRA bandwidths per CA configuration for inter-
band CA
* * *
CA operating / channel bandwidth Bandwidth Combination Set  
E-UTRA CA Configuration E-UTRA Bands 1.4 MHz 3 MHz 5 MHz 10 MHz 15 MHz 20 MHz  
CA_3A-5A 3 Yes Yes Yes 0 5 Yes Yes  
3 Yes 1 5 Yes Yes
* * *
##### 6.1.6.1.2 Co-existence studies for CA_3-5
As shown in table below, the harmonic frequencies of band 3 and band 5 in UL
are away from the receive bands of interest in the DL and we can conclude that
there is no issue on UL harmonic interference.
Table 6.1.6.1.2-1: Impact of UL Harmonic Interference
* * *
                                                                                       2^nd^ Harmonic     3^rd^ Harmonic
Band UL Low Band Edge UL High Band Edge DL Low Band Edge DL High Band Edge UL
Low Band Edge UL High Band Edge UL Low Band Edge UL High Band Edge 3 1710 1785
1805 1880 3420 3570 5130 5355 5 824 849 869 894 1648 1698 2472 2547
* * *
###### 6.1.6.1.2.1 Co-existence studies for 1 UL/2 DL
The 2^nd^ and 3^rd^ order harmonics and IMD products caused in the BS by
transmitting of Band 3 and Band 5 DL carriers can be calculated as shown in
table 6.1.6.1.2.1-1 below:
Table 6.1.6.1.2.1-1: Band 3 and Band 5 DL harmonics and IMD products
* * *
BS DL carriers f1_low f1_high f2_low f2_high DL frequency (MHz) 869 894 1805
1880 2^nd^ order harmonics frequency range (MHz) 1738 1788 3610 3760 3^rd^
order harmonics frequency range (MHz) 2607 2682 5415 5640 2^nd^ order IMD
products (f2_low -- f1_high) (f2_high -- f1_low) (f2_low + f1_low) (f2_high +
f1_high) IMD frequency limits (MHz) 911 1011 2674 2774 3^rd^ order IMD
products (f2_low -- 2*f1_high) (f2_high -- 2*f1_low) (2*f2_low -- f1_high)
(2*f2_high -- f1_low) IMD frequency limits (MHz) 17 142 2716 2891 3^rd^ order
IMD products (2*f1_low + f2_low) (2*f1_high + f2_high) (2*f2_low + f1_low)
(2*f2_high + f1_high) IMD frequency limits (MHz) 3543 3668 4479 4654 3^rd^
order IMD products (f1_low -- f2_high + f2_low) (f1_high + f2_high -- f2_low)
(f2_low -- f1_high + f1_low) (f2_high + f1_high -- f1_low) IMD frequency
limits (MHz) 794 969 1780 1905 3^rd^ order IMD products (with maximum channel
bandwidth) (f1_low -- f2_BWmax) (f1_high + f2_BWmax) (f2_low -- f1_BWmax)
(f2_high + f1_BWmax) IMD frequency limits (MHz) 849 914 1795 1890
* * *
It can be seen from table 6.1.6.1.2.1-1 that the 2^nd^ harmonics of BS
transmitting in Band 3 and Band 5 may fall into the BS receive band of Bands
3, 4, 9, 10 and 43, and the 3^rd^ harmonics of BS transmitting in Band 5 may
fall into the BS receive band of Bands 38 and 41, while the 2^nd^ IMD products
of BS supporting CA of Band 3 and Band 5 may fall into the BS receive band of
Bands 8 and 41, and the 3^rd^ IMD products may fall into the BS receive band
of Bands 2, 3, 5, 6, 8, 9, 14, 18, 19, 20, 25, 26, 27, 33, 35, 39, 42, 43 and
44. Note that the calculation in table 6.1.6.1.2.1-1 (except the last row)
assumes the BS is transmitting with the whole 75 MHz DL frequency of Band 3
and the whole 25 MHz DL frequency of Band 5. If the BS is only transmitting an
up to 20 MHz DL in Band 3 and an up to 10 MHz DL in Band 5 as stated in the
WIDS, then the 3^rd^ IMD products will not fall into the BS receive band of
Band 3, 5, 6, 9, 14, 18, 19, 26, 27, 33 or 44. Moreover, only the highest 10
MHz frequency spectrum in Band 8 (905 -- 915 MHz for UL and 950 -- 960 MHz for
DL) is allocated for mobile services in South Korea, thus the 2^nd^ IMD
products may only fall into the BS receive band of Band 8 frequency spectrum
used in South Korea (905 -- 915 MHz) under the transmit configurations shown
in table 6.1.6.1.2.1-2 below.
Table 6.1.6.1.2.1-2: Band (3 + 5) BS transmit configurations with 2nd IMD
within 905 -- 915 MHz
* * *
Band 3 DL channel bandwidth (MHz) Band 5 DL channel bandwidth (MHz) Lower edge
of Band 3 DL frequency block minus higher edge of Band 5 DL frequency block
(MHz) IMD frequency limits (MHz) 5, 10, 15 or 20 5 or 10 ≤ 915 911 -- 915
* * *
And the 3rd IMD products may only fall into the BS receive band of Band 8
frequency spectrum used in South Korea (905 -- 915 MHz) under the transmit
configurations (with a 15 or 20 MHz DL in Band 3) shown in table 6.1.6.1.2.1-3
below.
Table 6.1.6.1.2.1-3: Band (3 + 5) BS transmit configurations with 3^rd^ IMD
within 905 -- 915 MHz
* * *
Band 5 DL channel bandwidth (MHz) Band 5 DL frequency block (MHz) Band 3 DL
channel bandwidth (MHz) IMD frequency limits (MHz) 5 889 -- 894 15 874 -- 909
5 889 -- 894 20 869 -- 914 10 884 -- 894 15 869 -- 909 10 884 -- 894 20 864 --
914 5 884 -- 889 20 864 -- 909 10 879 -- 889 20 859 -- 909
* * *
Note that Bands 2, 4, 6, 9, 10, 14, 18, 19, 20, 25, 27, 33, 35, 38, 39, 41,
42, 43 and 44 are not intended for use in the same geographical area as Bands
3 and 5. Moreover, the 3rd IMD products will not fall into the BS receive band
of Band 3, 5 or 26 if the BS is only transmitting an up to 20 MHz DL in Band 3
and an up to 10 MHz DL in Band 5, Consequently, the focus here will be on the
harmonics and IMD products falling into Band 8 (3rd IMD products at 849 -- 914
MHz). As shown above, the 2nd and 3rd order IMD products caused by mixing of
Bands 3 and 5 DL carriers may fall within Band 8 UL used in South Korea if
certain BS transmit configurations are used, and hence BS receiver
desensitization may be an issue.
Therefore, it is recommended that Bands 3 and 5 BS transmitters should not
share the same antenna with Band 8 BS receiver for the affected frequency
ranges if the aforementioned BS transmit configurations are used, unless the
antenna path meets very stringent 2^nd^ and 3^rd^ order PIM specification so
that the PIM will not cause Band 8 BS receiver desensitization.
##### 6.1.6.1.3 ∆T~IB~ and ∆R~IB~ values
For two simultaneous DL and only one UL, the tentative ∆T~IB,c~ and ∆R~IB~
values are given in the tables.
Table 6.1.6.1.3-1: ΔT~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB~,c [dB] CA_3A-5A 3 0.3^1)^ 5
0.3^1)^ NOTE 1: The values in the table reflect what can be achieved with the
present state of the art technology. They shall be reconsidered when the state
of the art technology progresses
* * *
Table 6.1.6.1.3-2: ΔR~IB~
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB~ [dB] CA_3A-5A 3 0 5 0
* * *
### 6.1.7 LTE Advanced Carrier Aggregation of Band 1 and Band 18
CA_1-18 is designed to operate in the operating bands defined in table
6.1.7-1.
Table 6.1.7-1: Inter-band CA operating bands
E-UTRA CA Band | E-UTRA Band | Uplink (UL) band | Downlink (DL) band | Duplex mode |  |  |  |  |  |   
---|---|---|---|---|---|---|---|---|---|---  
|  | BS receive / UE transmit | Channel BW (MHz) | BS transmit / UE receive | Channel BW (MHz) |  |  |  |  |   
|  | FUL_low – FUL_high |  | FDL_low – FDL_high |  |  |  |  |  |   
CA_1-18 | 1 | 1920 MHz | – | 1980 MHz | 5, 10, 15, 20 | 2110 MHz | – | 2170 MHz | 5, 10, 15, 20 | FDD  
| 18 | 815 MHz | – | 830 MHz | 5, 10, 15 | 860 MHz | – | 875 MHz | 5, 10, 15 |   
#### 6.1.7.1 List of specific combination issues
##### 6.1.7.1.1 Channel bandwidths per operating band for CA
Table 6.1.7.1.1-1: Supported E-UTRA bandwidths per CA configuration for inter-
band CA
* * *
CA operating / channel bandwidth  
E-UTRA CA Configuration E-UTRA Bands 1.4 MHz 3 MHz 5 MHz 10 MHz 15 MHz 20 MHz
CA_1A-18A 1 Yes Yes Yes Yes 18 Yes Yes Yes
* * *
##### 6.1.7.1.2 Co-existence studies for CA 1-18
Although Band 1 and Band 18 are a High-Low band combination, the harmonic
frequencies do not fall into the frequency ranges of both bands as observed in
table 6.1.7.1.2-1. Therefore we can conclude that there is no issue on
harmonic interference.
Table 6.1.7.1.2-1: Impact of UL/DL Harmonic Interference
* * *
                                                                                       2^nd^ Harmonic     3^rd^ Harmonic      2^nd^ Harmonic     3^rd^ Harmonic
Band UL Low Band Edge UL High Band Edge DL Low Band Edge DL High Band Edge UL
Low Band Edge UL High Band Edge UL Low Band Edge UL High Band Edge DL Low Band
Edge DL High Band Edge DL Low Band Edge DL High Band Edge 1 1920 1980 2110
2170 3840 3960 5760 5940 4220 4340 6330 6510 18 815 830 860 875 1630 1660 2445
2490 1720 1750 2580 2625
* * *
Table 6.1.7.1.2-2 and 6.1.7.1.2-3 gives the frequency range of the third and
fifth order intermodulation product when two simultaneous ULs/DLs are active
in Band 1 and band 18. It can be seen that the intermodulation products are
not falling within the two inter-bands and therefore no further relaxation is
needed.
Table 6.1.7.1.2-2: Third order and fifth order intermodulation products (UL)
+------+--------------+--------------+--------------+--------------+ | Band | UL Low band | UL High band | UL 3^rd^ | UL 5^th^ | | | edge | edge | order | order | | | | | products | products | +------+--------------+--------------+--------------+--------------+ | 1 | 1920 MHz | 1980 MHz | N/A | N/A | | | | | | | | | | | 3010 -- 3145 | 4100 -- 4310 | | | | | MHz | MHz | +------+--------------+--------------+--------------+--------------+ | 18 | 815 MHz | 830 MHz | | | +------+--------------+--------------+--------------+--------------+
Table 6.1.7.1.2-3: Third order and fifth order intermodulation products (UL)
+------+--------------+--------------+--------------+--------------+ | Band | UL Low band | UL High band | UL 3^rd^ | UL 5^th^ | | | edge | edge | order | order | | | | | products | products | +------+--------------+--------------+--------------+--------------+ | 1 | 2110 MHz | 2170 MHz | N/A | N/A | | | | | | | | | | | 3345 -- 3480 | 4580 -- 4790 | | | | | MHz | MHz | +------+--------------+--------------+--------------+--------------+ | 18 | 830 MHz | 875 MHz | | | +------+--------------+--------------+--------------+--------------+
##### 6.1.7.1.3 ∆T~IB~ and ∆R~IB~ values
Following relaxations are allowed for the UE which supports inter-band carrier
aggregation of Band 1 and Band 18. Values are applicable both for 1 UL and 2
UL.
Table 6.1.7.1.3-1: ∆Τ~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_1A-18A 1 0.3 18 0.3
* * *
Table 6.1.7.1.3-2: ∆R~IB~
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB~ [dB] CA_1A-18A 1 0 18 0
* * *
### 6.1.8 LTE Advanced Carrier Aggregation of Band 1 and Band 19 (1 UL)
Table 6.1.8-1: Inter-band CA
+-------+-------+-------+-------+-------+-------+----+-------+-----+ | E | E | U | Dow | D | | | | | | -UTRA | -UTRA | plink | nlink | uplex | | | | | | CA | | (UL) | (DL) | Mode | | | | | | Band | Band | band | band | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | | | BS | BS | | | | | | | | | re | tra | | | | | | | | | ceive | nsmit | | | | | | | | | / UE | / UE | | | | | | | | | t | re | | | | | | | | | ransm | ceive | | | | | | | | | it^1^ | | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | | | F~UL\ | F~DL\ | | | | | | | | | _low~ | _low~ | | | | | | | | | -- | -- | | | | | | | | | F | F | | | | | | | | | ~UL_ | ~DL_ | | | | | | | | | high~ | high~ | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | CA\ | 1 | 1920 | -- | 1980 | 2110 | -- | 2170 | FDD | | _1-19 | | MHz | | MHz | MHz | | MHz | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | | 19 | 830 | -- | 8 | 875 | -- | 890 | | | | | MHz | | 45MHz | MHz | | MHz | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | NOTE | | | | | | | | | | 1: A | | | | | | | | | | s | | | | | | | | | | ingle | | | | | | | | | | u | | | | | | | | | | plink | | | | | | | | | | comp | | | | | | | | | | onent | | | | | | | | | | ca | | | | | | | | | | rrier | | | | | | | | | | of | | | | | | | | | | e | | | | | | | | | | ither | | | | | | | | | | Band | | | | | | | | | | 1 or | | | | | | | | | | Band | | | | | | | | | | 19 | | | | | | | | | | shall | | | | | | | | | | be | | | | | | | | | | used | | | | | | | | | | at | | | | | | | | | | any | | | | | | | | | | time. | | | | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+
#### 6.1.8.1 List of specific combination issues
##### 6.1.8.1.1 Channel bandwidths per operating band for CA
Table 6.1.8.1.1-1: Supported E-UTRA bandwidths per CA configuration for inter-
band CA
* * *
E-UTRA CA Configuration Supported E-UTRA bandwidths per CA configuration for
inter-band CA  
CA_1A-19A E-UTRA Bands Band 1  
Band 19 CBW 5 MHz 10 MHz 15 MHz 20 MHz 5 MHz Yes Yes Yes  
10 MHz Yes Yes Yes  
15 MHz Yes Yes
* * *
##### 6.1.8.1.2 Co-existence studies for CA_1-19
As Band 1 and Band 19 are a low-high band combination the harmonic frequencies
are far away from the receive and transmit bands of interest in the DL and UL
(see table 6.1.8.1.2-1) and therefore we can conclude that there is no issue
on harmonic interference.
Table 6.1.8.1.2-1: Impact of UL/DL Harmonic Interference
* * *
                                                                                       2^nd^ Harmonic     3^rd^ Harmonic      2^nd^ Harmonic     3^rd^ Harmonic
Band UL Low Band Edge UL High Band Edge DL Low Band Edge DL High Band Edge UL
Low Band Edge UL High Band Edge UL Low Band Edge UL High Band Edge DL Low Band
Edge DL High Band Edge DL Low Band Edge DL High Band Edge 1 1920 1980 2110
2170 3840 3960 5760 5940 4220 4340 6330 6510 19 830 845 875 890 1660 1690 2490
2535 1750 1780 2625 2670
* * *
##### 6.1.8.1.3 ∆T~IB~
CA 1A-19A belongs to Class A1. Therefore, according to [17], the followings
can be derived.
Table 6.1.8.1.3-1: ΔT~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_1A-19A 1 0.3 19 0.3
* * *
##### 6.1.8.1.4 ∆R~IB~
CA 1A-19A belongs to Class A1. Therefore, according to [17], the followings
can be derived.
Table 6.1.8.1.4-1: ΔR~IB~
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB~ [dB] CA_1A-19A 1 0 19 0
* * *
## 6.2 Class A2. Low-high band combination with harmonic relation between
bands
### 6.2.1 LTE Advanced Carrier Aggregation of Band 4 and Band 17 (1 UL)
#### 6.2.1.1 List of specific combination issues
##### 6.2.1.1.1 Channel bandwidths per operating band for CA
##### 6.2.1.1.2 Co-existence studies for CA_4-17 (1 UL)
The 2^nd^ and 3^rd^ order harmonics and IMD products caused in the BS by
transmitting of Band 4 and Band 17 DL carriers can be calculated as shown in
table 6.2.1.1.2-1 below:
Table 6.2.1.1.2-1: Band 4 and Band 17 DL harmonics and IMD products
* * *
BS DL carriers f1_low f1_high f2_low f2_high DL frequency (MHz) 734 746 2110
2155 2^nd^ order harmonics frequency range (MHz) 1468 1492 4220 4310 3^rd^
order harmonics frequency range (MHz) 2202 2238 6330 6465 2^nd^ order IMD
products (f2_low -- f1_high) (f2_high -- f1_low) (f2_low + f1_low) (f2_high +
f1_high) IMD frequency limits (MHz) 1364 1421 2844 2901 3^rd^ order IMD
products (f2_low -- 2*f1_high) (f2_high -- 2*f1_low) (2*f2_low -- f1_high)
(2*f2_high -- f1_low) IMD frequency limits (MHz) 618 687 3474 3576 3^rd^ order
IMD products (2*f1_low + f2_low) (2*f1_high + f2_high) (2*f2_low + f1_low)
(2*f2_high + f1_high) IMD frequency limits (MHz) 3578 3647 4954 5056 3^rd^
order IMD products (f1_low -- f2_high + f2_low) (f1_high + f2_high -- f2_low)
(f2_low -- f1_high + f1_low) (f2_high + f1_high -- f1_low) IMD frequency
limits (MHz) 689 791 2098 2167
* * *
It can be seen from table 6.2.1.1.2-1 that the 2^nd^ and 3^rd^ harmonics as
well as the 2^nd^ IMD products of BS transmitting in Bands 4 and 17 will not
fall into the BS receive band of any frequency band currently defined in 3GPP,
but the 3^rd^ IMD products supporting CA of Band 4 and Band 17 may fall into
the BS receive band of Bands 12, 13, 14, 17, 22, 42 and 43. Note that the
calculation in table 6.2.1.1.2-1 assumes the BS is transmitting with the whole
45 MHz DL frequency of Band 4 and the whole 10 MHz DL frequency of Band 17. If
the BS is only transmitting an up to 10 MHz DL in Band 4 and a 10 MHz DL in
Band 17 as stated in the WIDS, then the 3^rd^ IMD products will not fall into
the BS receive band of Bands 12, 13, 14 and 17.
With the performances of the current BS antenna system, transmit and receive
path components, amplifiers, pre-distortion algorithms and filters, it is
expected that the IMD interference generated within the Band 22, 42 or 43
receiver would be well below the receiver noise floor eliminating the
possibility of receiver desensitization, provided that Bands 4 and 17 BS
transmitters do not share the same antenna with Band 22, 42 or 43 BS receiver.
And it is recommended that Bands 4 and 17 BS transmitters should not share the
same antenna with Band 22, 42 or 43 BS receiver, unless the antenna path meets
very stringent 3rd order PIM specification so that the PIM will not cause Band
22, 42 or 43 BS receiver desensitization.
##### 6.2.1.1.3 Maximum Sensitivity Degradation (MSD) for Band 4
The Band 4 + Band 17 CA configuration has been identified as an A2 combination
where the 3^rd^ harmonic from a UE uplink transmission in Band 17 may land
within the downlink of Band 4. Because of the significant overlap of 3^rd^
harmonic interference, the maximum sensitivity degradation (MSD) is defined
for Band 4 when transmitting in Band 17.
###### 6.2.1.1.3.1 Conditions for MSD
The following conditions are defined for the MSD for Band 4 + Band 17 with the
principle that the 3^rd^ harmonic interference should be fully overlapped and
entirely contained within the downlink RB\'s being received in Band 4.
\- For the Band 17 uplink, the channel can be placed anywhere in the band.
While it may not be true for other class A2 band combinations, for the Band 4
+ Band 17 combination, there is always full overlap of the 3^rd^ harmonic of
the uplink into the downlink. The Band 17 downlink is placed according to the
default Band 17 Rx-Tx separation of 30 MHz.
\- For the Band 4 downlink, the channel should be placed at 3x the Band 17
uplink frequency. The Band 4 uplink is placed according to the default Band 4
Rx-Tx separation of 400 MHz.
\- As for all reference sensitivity/MSD tests, the downlink should be fully
allocated for Band 4 downlink and for Band 17 downlink.
\- The Band 17 uplink size should be 1/3 of the Band 4 downlink size; that is,
for 10 MHz CBW in Band 4, the Band 17 uplink should be 16 RB's and for 5 MHz
CBW in Band 4, the Band 17 uplink should be 8 RB's.
\- The uplink allocation in Band 17 can be placed anywhere in the channel
since there is always full overlap no matter where it is placed. We therefore
propose to place the Band 17 uplink in the highest portion of the channel as
close as possible to the Band 17 downlink to represent the worst case.
Examples are provided below:
Table 6.2.1.1.3.1-1: Example MSD configuration of Band 4 and Band 17 channels
* * *
Band 17 UL and DL Band 4 DL  
Bandwidth Frequency of Uplink Frequency of Downlink Bandwidth Frequency of
Downlink 5 706.5 736.5 5 2124 5 707.5 737.5 5 2127 5 712.5 742.5 5 2142 5
713.5 743.5 5 2145 5 706.5 736.5 10 2122 5 707.5 737.5 10 2125 5 712.5 742.5
10 2140 5 713.5 743.5 10 2143 10 709 739 5 2131.6 10 711 741 5 2137.6 10 709
739 10 2129.4 10 711 741 10 2135.4
* * *
Table 6.2.1.1.3.1-2: Uplink configuration for MSD for CA_4-17
CA configuration | E-UTRA Band | CC combination | Duplex Mode |  |  |  |  |  |  |   
---|---|---|---|---|---|---|---|---|---|---  
|  | 25RB+25RB | 25RB+50RB | 50RB+25RB | 50RB+50RB |  |  |  |  |   
CA_4A-17A | 4 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | FDD  
| 17 | n/a | 8 | n/a | 8 | n/a | 16 | n/a | 16 |   
NOTE 1: The CC combination is denoted by the NRB of each component carrier in the CA configuration. For the CA configuration CA_XA-YA, the NRB of the component carriers in band X and band Y are listed in order with CC combination NRB(X) + NRB(Y). NOTE 2: The transmitted power of the PCC shall be set to PUMAX as defined in subclause 6.2.5. |  |  |  |  |  |  |  |  |  |   
###### 6.2.1.1.3.2 Reference architecture
To determine the value of MSD, a reference architecture is adopted where a
harmonic trip filter is used on the Band 17 RF path value to suppress the
3^rd^ harmonic interference term at the output of the duplexer. The block
diagram is shown below
{width="5.532638888888889in" height="2.579861111111111in"}
Figure 6.2.1.1.3.2-1: Reference architecture for Band 4 + Band 17
###### 6.2.1.1.3.3 Analysis of MSD
The analysis is summarized below assuming high linearity component selection
and the implementation of a diplexer at the antenna port.
Table 6.2.1.1.3.3-1: Harmonic interference calculation
* * *
Primary Diversity  
Parameter Value H3 level Value H3 level B17 Tx 27.5 27.5 B17 PA H3 -50 -22.5
-50 -22.5 B17 duplexer 40 -62.5 40 -62.5 Harmonic filter 30.5 -93.0 30.5 -93.0
LB switch -96.5 -91.4 -96.5 -91.4 Diplexer 15 -106.4 15 -106.4 Antenna
isolation 10 -116.4 HB switch attenuation 0.7 -107.1 0.7 -117.1 HB switch H3
-126 -107.0 -111.9 -110.8 B4 duplexer attenuation 1.6 -108.6 1.6 -112.4 B4
duplexer H3 -126 -108.6 -111.9 -109.1 B17 PA to B4 LNA isolation 80 -102.5 80
-102.5 Single chip DA to LNA -100 -100.0 -100 -100.0 Composite -97.7 -97.7
* * *
The analysis also includes an estimate of achievable isolation on the PCB as
well as on the chip for single-chip designs. The composite additional noise
seen at the input to the Band 4 LNA is estimated to be -97.7 dBm. Evaluating
the impact of this additional interference to reference sensitivity and
assuming that the interference impinging upon the primary and diversity
receivers is correlated much in the same way a blocker is tested, we conclude
that the reference sensitivity is degraded by 10.2 dB for the 5 MHz channel
bandwidth case, and by 7.6 dB for the 10 MHz channel bandwidth case. However,
in previous agreement, the diplexer insertion loss should not be included in
reference sensitivity relaxation so the MSD becomes 9.9 dB and 7.3 dB for 5
MHz and 10 MHz channel bandwidths, respectively, which we round to 10 dB and
7.5 dB.
Table 6.2.1.1.3.3-2: Proposed MSD specification for CA_4-17 configuration
+---------+---------+---------+---------+---------+---------+-----+ | CA | E-UTRA | CC | Duplex | | | | | config | Band | comb | Mode | | | | | uration | | ination | | | | | +---------+---------+---------+---------+---------+---------+-----+ | | | 25 | 25 | 50 | 50 | | | | | RB+25RB | RB+50RB | RB+25RB | RB+50RB | | +---------+---------+---------+---------+---------+---------+-----+ | CA\ | 4 | -90 | -90 | -89.5 | -89.5 | FDD | | _4A-17A | | | | | | | +---------+---------+---------+---------+---------+---------+-----+ | | 17 | n/a | n/a | n/a | n/a | | +---------+---------+---------+---------+---------+---------+-----+ | NOTE 1: | | | | | | | | The CC | | | | | | | | comb | | | | | | | | ination | | | | | | | | is | | | | | | | | denoted | | | | | | | | by the | | | | | | | | N~RB~ | | | | | | | | of each | | | | | | | | co | | | | | | | | mponent | | | | | | | | carrier | | | | | | | | in the | | | | | | | | CA | | | | | | | | configu | | | | | | | | ration. | | | | | | | | For the | | | | | | | | CA | | | | | | | | config | | | | | | | | uration | | | | | | | | CA\ | | | | | | | | _XA-YA, | | | | | | | | the | | | | | | | | N~RB~ | | | | | | | | of the | | | | | | | | co | | | | | | | | mponent | | | | | | | | c | | | | | | | | arriers | | | | | | | | in band | | | | | | | | X and | | | | | | | | band Y | | | | | | | | are | | | | | | | | listed | | | | | | | | in | | | | | | | | order | | | | | | | | with CC | | | | | | | | comb | | | | | | | | ination | | | | | | | | N | | | | | | | | ~RB~(X) | | | | | | | | + | | | | | | | | N~ | | | | | | | | RB~(Y). | | | | | | | | | | | | | | | | NOTE 2: | | | | | | | | The | | | | | | | | tran | | | | | | | | smitter | | | | | | | | in the | | | | | | | | lower | | | | | | | | fr | | | | | | | | equency | | | | | | | | band | | | | | | | | shall | | | | | | | | be set | | | | | | | | to | | | | | | | | P~UMAX~ | | | | | | | | as | | | | | | | | defined | | | | | | | | in | | | | | | | | su | | | | | | | | bclause | | | | | | | | 6.2.5. | | | | | | | +---------+---------+---------+---------+---------+---------+-----+
Because the reference architecture and the analysis assume the use of a
harmonic filter in the uplink path of Band 17, an insertion loss in addition
to that of the diplexer must be taken into consideration. As noted previously,
in this architecture, the filter insertion loss only affects Band 17 including
both uplink and downlink. However, as with the diplexer, the insertion loss is
present even when the device is operating in single carrier configuration
since it forms a part of the signal path. The insertion loss of the filter has
been reported by the filter vendor to be 0.5 dB. It has been previously agreed
for class A1 configurations that the insertion loss of the diplexer is to be
accounted for partially by implementation margin and partially by relaxations
to maximum output power and reference sensitivity. We apply the 0.5 dB filter
insertion loss on top of these relaxations for this band combination.
Table 6.2.1.1.3.3-3: ΔT~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_4A-17A 4 0.3 17 0.8
* * *
Table 6.2.1.1.3.3-4: ΔR~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB,c~ [dB] CA_4A-17A 4 0 17 0.5
* * *
##### 6.2.1.1.4 Maximum sensitivity reduction for band 4
When band 4 DL is operated simultaneously with band 17 UL there is a potential
self interference situation as the third harmonic of band 17 UL will be on the
same frequency range as the band 4 DL. It is agreed that 3GPP will set the
limit for this interference by specifying maximum sensitivity degradation
(MSD) in TS 36.101 [22].
For the MSD study we have assumed UE architecture in figure 6.2.1.1.4-1.
Figure 6.2.1.1.4-1: UE architecture for band combination 17+4
MSD for LTE channel bandwidths of 5 and 10 MHz are calculated with typical
component specification values assuming the usage of active antenna tuning or
switching elements. Results are presented in table 6.2.1.1.4-1.
Table 6.2.1.1.4-1: MSD for LTE channel bandwidths of 5 and 10 MHz
{width="6.688194444444444in" height="5.225694444444445in"}
Based on the calculations presented in table 6.2.1.1.4-1 the MSD shall be
specified in following manner into TS 36.101 [22].
Table 6.2.1.1.4-2: MSD
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_4A-17A 4 0.3 17 0.8
* * *
To enable the harmonic suppression used in calculations presented in table
6.2.1.1.4-1 a usage of harmonic rejection filter is assumed. To enable this an
allowance is given to maximum output power of band 17 by defining the ΔTib,c =
0.8 dB. This value contains 0.3 dB for the diplexer as agreed for Hi-low
combinations without harmonic relation and 0.5 dB for the insertion loss of
harmonic trap.
Table 6.2.1.1.4-3: ΔTIB,c
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_4A-17A 4 0 17 0.5
* * *
Similarly to enable the harmonic suppression filter an allowance is given to
REFSENS of band 17 by defining the ΔRib,c = 0.5 dB.
Table 6.2.1.1.4-4: ΔRIB,c
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB,c~ [dB] CA_4A-17A 4 0 17 0.5
* * *
### 6.2.2 LTE-Advanced Carrier Aggregation of Band 4 and Band 12 (1 UL)
Table 6.2.2-1: Inter-band CA
* * *
E-UTRA CA Band E-UTRA Band Uplink (UL) operating band Downlink (DL) operating
band Duplex Mode  
BS receive / UE transmit BS transmit / UE receive  
F~UL_low~ -- F~UL_high~ F~DL_low~ -- F~DL_high~  
CA_4-12 4 1710 MHz -- 1755 MHz 2110 MHz -- 2155 MHz FDD 12 699 MHz -- 716 MHz
729 MHz -- 746 MHz
* * *
#### 6.2.2.1 List of specific combination issues
##### 6.2.2.1.1 Channel bandwidths per operating band for CA
Table 6.2.2.1.1-1: Supported E-UTRA bandwidths per CA configuration for inter-
band CA
* * *
CA operating / channel bandwidth  
E-UTRA CA Configuration E-UTRA Bands 1.4 MHz 3 MHz 5 MHz 10 MHz 15 MHz 20 MHz
CA_4A-12A 4 Yes Yes Yes Yes  
12 Yes Yes
* * *
##### 6.2.2.1.2 Co-existence studies for CA_4-12
The combination of band 4 and band 12 has harmonic frequencies that are far
removed from the component receive and transmit frequencies, in the UL and in
the DL of the CA combination, as shown in table 6.2.2.1.2-1, with the
exception of one 3^rd^ order harmonic falling in the BC4 downlink band. 3^rd^
order harmonics are expected to be significantly attenuated, but further study
will be required to confirm that there is no detrimental impact.
Table 6.2.2.1.2-1: Impact of UL/DL Harmonic Interference
* * *
                                                                                       2^nd^ Harmonic     3^rd^ Harmonic      2^nd^ Harmonic     3^rd^ Harmonic
Band UL Low Band Edge UL High Band Edge DL Low Band Edge DL High Band Edge UL
Low Band Edge UL High Band Edge UL Low Band Edge UL High Band Edge DL Low Band
Edge DL High Band Edge DL Low Band Edge DL High Band Edge 4 1710 1755 2110
2155 3420 3510 5130 5265 4220 4310 6330 6465 12 699 716 729 746 1398 1432 2097
2148 1458 1492 2187 2238
* * *
Table 6.2.1.1.2-2 gives the frequency range of the second and third order
inter-modulation products when two simultaneous ULs are active in band 4 and
band 12. It can be seen that the inter-modulation products are not falling
within the two bands and therefore no further relaxation is needed.
Table 6.2.2.1.2-2: Second-order and third-order inter-modulation products
+------+---------+---------+---------+---------+---------+---------+ | Band | UL low | UL high | DL low | DL high | UL | UL | | | band | band | band | band | 2^nd^ | 3^rd^ | | | edge | edge | edge | edge | order | order | | | | | | | p | p | | | | | | | roducts | roducts | +------+---------+---------+---------+---------+---------+---------+ | 4 | 1710 | 1755 | 2110 | 2155 | 994 -- | 2704 -- | | | MHz | MHz | MHz | MHz | 1056 | 2811 | | | | | | | MHz | MHz | | | | | | | | | | | | | | | 2409 -- | 3108 -- | | | | | | | 2471 | 3187 | | | | | | | MHz | MHz | | | | | | | | | | | | | | | | 4119 -- | | | | | | | | 4226 | | | | | | | | MHz | +------+---------+---------+---------+---------+---------+---------+ | 12 | 699 MHz | 716 MHz | 729 MHz | 746 MHz | | | +------+---------+---------+---------+---------+---------+---------+
###### 6.2.2.1.2.1 Co-existence studies for 1 UL/2 DL
The 2^nd^ and 3^rd^ order harmonics and IMD products caused in the BS by
transmitting of Band 4 and Band 12 DL carriers can be calculated as shown in
table 6.2.2.1.2.1-1 below:
Table 6.2.2.1.2.1-1: Band 4 and Band 12 DL harmonics and IMD products
* * *
BS DL carriers f1_low f1_high f2_low f2_high DL frequency (MHz) 729 746 2110
2155 2^nd^ harmonics frequency limits (MHz) 1458 1492 4220 4310 3^rd^
harmonics frequency limits (MHz) 2187 2238 6330 6465 2^nd^ order IMD products
(f2_low -- f1_high) (f2_high -- f1_low) (f2_low + f1_low) (f2_high + f1_high)
IMD frequency limits (MHz) 1364 1426 2839 22901 3^rd^ order IMD products
(f2_low -- 2*f1_high) (f2_high -- 2*f1_low) (2*f2_low -- f1_high) (2*f2_high
-- f1_low) IMD frequency limits (MHz) 618 697 3474 3581 3^rd^ order IMD
products (2*f1_low + f2_low) (2*f1_high + f2_high) (2*f2_low + f1_low)
(2*f2_high + f1_high) IMD frequency limits (MHz) 3568 3647 4949 5056 3^rd^
order IMD products (f1_low -- f2_high + f2_low) (f1_high + f2_high -- f2_low)
(f2_low -- f1_high + f1_low) (f2_high + f1_high -- f1_low) IMD frequency
limits (MHz) 684 791 2093 2172 3^rd^ order IMD products (with maximum channel
bandwidth) (f1_low -- f2_BWmax) (f1_high + f2_BWmax) (f2_low -- f1_BWmax)
(f2_high + f1_BWmax) IMD frequency limits (MHz) 719 756 2100 2165
* * *
It can be seen from table 6.2.2.1.2.1-1 that the 2^nd^ harmonics of BS
transmitting in Band 12 may fall into the BS receive band of Band 21, while
the 3^rd^ IMD products of BS supporting carrier aggregation of Band 4 and Band
12 may fall into the BS receive band of Bands 12, 13, 14, 17, 22, 28, 42, 43
and 44. Note that the calculation in table 6.2.2.1.2.1-1 (except the last row)
assumes the BS is transmitting with the whole 45 MHz DL frequency of Band 4
and the whole 17 MHz DL frequency of Band 12. If the BS is only transmitting
up to 10 MHz DL in Band 4 and Band 12 as stated in the WIDS, then the 3^rd^
IMD products will not fall into the BS receive band of Bands 12, 13, 14 and 17
as shown in the last row in table 6.2.2.1.2.1-1.
Note that Bands 21, 28 and 44 are not intended for use in the same
geographical area as Bands 4 and 12. Moreover, with the performances of the
current BS antenna system, transmit and receive path components, amplifiers,
pre-distortion algorithms and filters, it is expected that the IMD
interference generated within the Band 22, 42 or 43 receiver would be well
below the receiver noise floor eliminating the possibility of receiver
desensitization, provided that Bands 4 and 12 BS transmitters do not share the
same antenna with Band 22, 42 or 43 BS receiver.
Therefore, it is recommended that Bands 4 and 12 BS transmitters should not
share the same antenna with Band 22, 42 or 43 BS receiver, unless the antenna
path meets very stringent 3^rd^ order PIM specification so that the PIM will
not cause Band 22, 42 or 43 BS receiver desensitization.
##### 6.2.2.1.3 Maximum Sensitivity Degradation (MSD) for band 4
When the uplink of carrier aggregation is allocated in band12, it will have
the opportunity that UL's 3^rd^ harmonic falls in band 4's DL. The 1/3 of 2110
MHz is 703.33 MHz, so if the uplink frequency is in the range of 703.33 -- 716
MHz, the harmonic problem will arise. For the similarity between CA_4-12 and
CA_4-17, the reference architecture, some of the test conditions and MSD
analysis of CA_4-17 can be reused.
###### 6.2.2.1.3.1 Reference architecture
The reference architecture of CA_4-12 is the same with CA_4-17 in subclause
6.2.1.1.3.2. A harmonic filter is used after the duplexer to suppress the 3rd
harmonic of the low band uplink signal.
{width="5.532638888888889in" height="2.579861111111111in"}
Figure 6.2.2.1.3.1-1: Reference architecture for Band 4 + Band 12
###### 6.2.2.1.3.2 Test configuration of MSD
When B12's uplink frequency is in the range of 703.33-716 MHz, the 3^rd^
harmonic will full overlap with band 4's DL. We propose reuse the MSD test
configuration of CA_4-17 in subclause 6.2.1.1.3.1. When testing MSD, the UL
frequency range uses B17 UL's frequency range, 704 MHz-716 MHz. The small
bandwidth not included in CA_4-17 can be deduced from the conditions of bigger
bandwidth.
Examples are provided below:
Table 6.2.2.1.3.2-1: Example MSD configuration of Band 4 and Band 12 channels.
* * *
Band 12 UL and DL Band 4 DL  
Bandwidth Frequency of Uplink Frequency of Downlink Bandwidth Frequency of
Downlink 5 706.5 736.5 1.4 2125.7 5 707.5 737.5 1.4 2128.7 5 712.5 742.5 1.4
2143.7 5 713.5 743.5 1.4 2146.7 5 706.5 736.5 3 2125 5 707.5 737.5 3 2128 5
712.5 742.5 3 2143 5 713.5 743.5 3 2146 5 706.5 736.5 5 2124 5 707.5 737.5 5
2127 5 712.5 742.5 5 2142 5 713.5 743.5 5 2145 5 706.5 736.5 10 2122 5 707.5
737.5 10 2125 5 712.5 742.5 10 2140 5 713.5 743.5 10 2143 10 709 739 1.4 2140
10 711 741 1.4 2146 10 709 739 3 2139 10 711 741 3 2145 10 709 739 5 2138.3 10
711 741 5 2144.3 10 709 739 10 2136.2 10 711 741 10 2142.2
* * *
The uplink configuration is shown in table 6.2.2.1.3.2-2.
Table 6.2.2.1.3.2-2: Uplink configuration for MSD of CA_4-12
* * *
CA Configuration DL Bandwidth of Band 4 [MHz] UL configuration of Band 12 [RB]
CA_4A-12A 1.4 2 3 5 5 8 10 16
* * *
When testing MSD, the uplink power shall be set to P~UMAX~ as defined in
subclause 6.2.5A of TS 36.101 [22].
###### 6.2.2.1.3.3 MSD values
Although the frequency range of band 12 is wider than band 17, the analysis of
MSD of band 4 and the insertion loss of harmonic filter/diplexer for CA_4-17
in subclause 6.2.1.1.3.3 can be used by CA_4-12. For the small bandwidth of
CA_4-12, the harmonic level falling in the DL of high band is the same with
bigger bandwidth, 5 MHz and 10 MHz. So the MSD values are shown in table
6.2.2.1.3.3-1.
Table 6.2.2.1.3.3-1: MSD for CA_4-12
* * *
Maximum sensitivity degradation [dB]  
CA Configuration E-UTRA Bands 1.4 MHz 3 MHz 5 MHz 10 MHz 15 MHz 20 MHz
CA_4A-12A 4 15 12 10 7.5  
12
* * *
For two simultaneous DL and one UL the ∆T~IB,c~ and ∆R~IB~ values are shown in
table 6.2.2.1.3.3-2, and in table 6.2.2.1.3.3-3:
Table 6.2.2.1.3.3-2: ΔT~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_4A-12A 4 0.3 12 0.8
* * *
Table 6.2.2.1.3.3-3: ΔR~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB,c~ [dB] CA_4A-12A 4 0 12 0.5
* * *
It should be noted that the relaxations for CA_4A-12A, ∆T~IB,c~ and ∆R~IB,c~
are applied for each component carrier when operating either in single carrier
or carrier aggregation configuration with a single uplink CC.
### 6.2.3 LTE Advanced Carrier Aggregation of Band 3 and Band 8
Table 6.2.3-1: Inter-band CA operating bands
E-UTRA CA Band | E-UTRA Band | Uplink (UL) band | Downlink (DL) band | Duplex mode |  |  |  |  |  |   
---|---|---|---|---|---|---|---|---|---|---  
|  | BS receive / UE transmit | Channel BW (MHz) | BS transmit / UE receive | Channel BW (MHz) |  |  |  |  |   
|  | FUL_low – FUL_high |  | FDL_low – FDL_high |  |  |  |  |  |   
CA_3-8 | 3 | 1710 MHz | – | 1785 MHz | 10, 15, 20 | 1805 MHz | – | 1880 MHz | 10, 15, 20 | FDD  
| 8 | 880 MHz | – | 915 MHz | 5, 10 | 925 MHz | – | 960 MHz | 5, 10 | FDD  
#### 6.2.3.1 List of specific combination issues
##### 6.2.3.1.1 Channel bandwidths per operating band for CA
Table 6.2.3.1.1-1: Supported E-UTRA bandwidths per CA configuration for inter-
band CA
* * *
CA operating / channel bandwidth Bandwidth Combination Sets  
E-UTRA CA Configuration E-UTRA Bands 1.4 MHz 3 MHz 5 MHz 10 MHz 15 MHz 20 MHz  
CA_3A-8A 3 Yes Yes Yes 0 8 Yes Yes  
3 Yes 1 8 Yes Yes
* * *
NOTE: For the UE that signals support of any bandwidth combination set for
carrier aggregation, the UE shall support all single carrier bandwidths for
the constituent bands as defined in table 5.6.1-1 of TS 36.101 [22] when
operating in single carrier mode.
##### 6.2.3.1.2 Co-existence studies for CA_3-8 (1 UL/2 DL)
Table 6.2.3.1.2-1 summarizes frequency ranges where harmonics occur due to
Band 3 or Band 8 for both UL and DL. It can be seen that distortions caused by
2^nd^ order harmonics of Band 8 locates within the passband of Band 3.
Additional filtering or de-sensitisation may be necessary.
Table 6.2.3.1.2-1: Impact of UL/DL Harmonic Interference
* * *
                                                                                       2^nd^ Harmonic     3^rd^ Harmonic      2^nd^ Harmonic     3^rd^ Harmonic
Band UL Low Band Edge UL High Band Edge DL Low Band Edge DL High Band Edge UL
Low Band Edge UL High Band Edge UL Low Band Edge UL High Band Edge DL Low Band
Edge DL High Band Edge DL Low Band Edge DL High Band Edge 3 1710 1785 1805
1880 3420 3570 5130 5355 3610 3760 5415 5640 8 880 915 925 960 1760 1830 2640
2745 1850 1920 2775 2880
* * *
Table 6.2.3.1.2-2 summarized frequency ranges where IMD occurs due to 2 DL
(Band 3 and Band 8).
**Table 6.2.3.1.2-2: 2^nd^ order and 3^rd^ order IMD Products (DL)**
+------+--------------+--------------+--------------+--------------+ | Band | DL low band | DL high band | DL 2^nd^ | DL 3^rd^ | | | edge | edge | order | order | | | | | products | products | +------+--------------+--------------+--------------+--------------+ | 3 | 1805 MHz | 1880 MHz | 845-955 MHz | 2650 -- 2835 | | | | | | MHz | | | | | 2730 -- 2840 | | | | | | MHz | 3655 -- 3800 | | | | | | MHz | | | | | | | | | | | | 4535 -- 4720 | | | | | | MHz | +------+--------------+--------------+--------------+--------------+ | 8 | 925 MHz | 960 MHz | | | +------+--------------+--------------+--------------+--------------+
##### 6.2.3.1.3 ∆T~IB~ and ∆R~IB~ values
For two simultaneous DL and one UL the ∆T~IB,c~ and ∆R~IB~ values are shown in
table 6.2.3.1.3-1, and in table 6.2.3.1.3-2:
Table 6.2.3.1.3-1: ΔT~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_3-8 3 0.3 8 0.3
* * *
Table 6.2.3.1.3-2: ΔR~IB~
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB~ [dB] CA_3-8 3 0 8 0
* * *
## 6.3 Class A3. Low-low or high-high band combinations
This subclause shall include all inter band CA combinations which can be
included in the group low-low or high-high combinations without transmitter
harmonics.
### 6.3.1 LTE-Advanced Carrier Aggregation of Band 3 and Band 7
Table 6.3.1-1: Inter-band CA
E-UTRA CA Band | E-UTRA Band | Uplink (UL) band | Downlink (DL) band | Duplex mode |  |  |  |  |  |   
---|---|---|---|---|---|---|---|---|---|---  
|  | BS receive / UE transmit | Channel BW (MHz) | BS transmit / UE receive | Channel BW (MHz) |  |  |  |  |   
|  | FUL_low – FUL_high |  | FUL_low – FUL_high |  |  |  |  |  |   
CA_3-7 | 3 | 1710 MHz | – | 1785 MHz | 5, 10, 15, 20  
(note 1) | 1805 MHz | – | 1880 MHz | 5, 10, 15, 20 | FDD  
| 7 | 2500 MHz | – | 2570 MHz | 10, 15, 20 (note 1) | 2620 MHz | – | 2690 MHz | 10, 15, 20 |   
NOTE 1: The first part of the WI considers only one uplink component carrier to be used in any of the two frequency bands at any time. |  |  |  |  |  |  |  |  |  |   
#### 6.3.1.1 List of specific combination issues
##### 6.3.1.1.1 Channel bandwidths per operating band for CA
Table 6.3.1.1.1-1: Supported E-UTRA bandwidths per CA configuration for inter-
band CA
* * *
CA operating / channel bandwidth  
E-UTRA CA Configuration E-UTRA Bands 1.4 MHz 3 MHz 5 MHz 10 MHz 15 MHz 20 MHz
CA_3A-7A 3 Yes Yes Yes Yes 7 Yes Yes Yes
* * *
##### 6.3.1.1.2 Co-existence studies for 1 UL/2 DL
Table 6.3.1.1.2-1 gives the intermodulation products for band 3 + band 7 CA
with 2 DLs. For the 3-tone IMD analysis the maximum transmission as defined in
table 6.3.1.1.1-1 is considered. None of the intermodulation products fall
into the own receive bands. Considering bands in the same geographical area we
observe that the BS distortion could fall into the BS receive bands of Band 8,
20, 22, 42 and 43.
With the performances of the current BS antenna system, transmit and receive
path components, amplifiers, pre-distortion algorithms and filters the IMDs
generated within the band 8, 20, 22, 38, 42 and 43 receiver should be well
below the receiver noise floor eliminating the possibility of receiver
desensitization. Provided that the Bands 3 and 7 BS transmitters should not
share the same antenna with Band 8, 20, 22, 38, 42 or 43 BS receiver.
Table 6.3.1.1.2-1: 2 DLs B3 + B7 IMD products
* * *
BS DL carriers f1_low f1_high f2_low f2_high
DL frequency (MHz) 1805 1880 2620 2690
2^nd^ order harmonics frequency range (MHz) 3610 to 3760 5240 to 5380
3^rd^ order harmonics frequency range (MHz) 5415 to 5640 7860 to 8070
Two-tone 2^nd^ order IMD products \|f2_low -- f1_high\| \|f2_high -- f1_low\|
\|f2_low + f1_low\| \|f2_high + f1_high\|
IMD frequency range (MHz) 740 to 885 4425 to 4570
Two-tone 3^rd^ order IMD products \|2*f1_low -- f2_high\| \|2*f1_high --
f2_low\| \|2*f2_low -- f1_high\| \|2* f2_high -- f1_low\|
IMD frequency range (MHz) 920 to 1140 3360 to 3575
Three-tone 3^rd^ order IMD products \|f1_low --\ \|f1_high +\ \|f2_low --\
\|f2_high +\ max BW f2\| max BW f2\| max BW f1\| max BW f1\|
IMD frequency range (MHz) 1785 to 1900 2600 to 2710
* * *
Table 6.3.1.1.2-2 gives the intermodulation products for band 3 + band 7 CA
with 1 UL. None of the intermodulation products fall into the own receive
bands. For the UE the distortion could fall into the UE receive bands for Band
22 and 43. As a UE does not simultaneous operate in B3 + B7 and any other band
this should be not a problem in case the UE supports these bands. These bands
are also rather far away from band 3 and band 7 and we can assume that the UE
filter can effectively attenuate these IMD products.
Table 6.3.1.1.2-2: 1 UL B3 + B7 harmonic products
* * *
UE UL carriers f1_low f1_high f2_low f2_high UL frequency (MHz) 1710 1785 2500
2570 2^nd^ order harmonics frequency range (MHz) 3420 to 3570 5000 to 5140  
3^rd^ order harmonics frequency range (MHz) 5130 to 5355 7500 to 7710
* * *
##### 6.3.1.1.3 Co-existence studies for 2 UL/2 DL
Table 6.3.1.1.2-1 gives the intermodulation products for band 3 + band 7 CA
with 2 ULs. For the 3-tone IMD analysis the maximum transmission BW as defined
in table 6.3.1.1.1-1 is considered. None of the intermodulation products fall
into the own receive bands.
Considering bands in the same geographical area we observe that the UE
distortion could fall into the UE receive bands of Band 8, 20, 38 and 42\. The
magnitudes of these possible IMD products have to be further studied with
respect to spurious emission limits into these bands.
Table 6.3.1.1.3-1: 2 ULs B3 + B7 IMD products
* * *
UE UL carriers f1_low f1_high f2_low f2_high UL frequency (MHz) 1710 1785 2500
2570 Two-tone 2^nd^ order IMD products \|f2_low -- f1_high\| \|f2_high --
f1_low\| \|f2_low + f1_low\| \|f2_high + f1_high\| IMD frequency range (MHz)
715 to 860 4210 to 4355
Two-tone 3^rd^ order IMD products \|2*f1_low -- f2_high\| \|2*f1_high --
f2_low\| \|2*f2_low -- f1_high\| \|2* f2_high -- f1_low\| IMD frequency range
(MHz) 850 to 1070 3215 to 3430
Three-tone 3^rd^ order IMD products (f1_low -- max BW f2) (f1_high + max BW
f2) (f2_low -- max BW f1) (f2_high + max BW f1) IMD frequency range (MHz) 1690
to 1805 2480 to 2590
* * *
##### 6.3.1.1.4 ∆T~IB~ and ∆R~IB~ values
The following ILs for ETC combining band 3 + 7 were reported:
Table 6.3.1.1.4-1: Reported ILs for band 3 + 7 diplexer and quadplexers for
ETC
* * *
E-UTRA bands IL (dB) IL (dB) IL (dB) IL (dB) 3 0.93 0.85 0.5 0.8 7 1.08 0.8
0.4 1.0
* * *
For the reported IL values there was no or only marginal difference for the
Tx/Rx paths reported. With the average IL given as:
Table 6.3.1.1.4-2: Average Tx and Rx IL for combining band 3 and band 7 for
ETC
* * *
Inter-band CA Configuration E-UTRA Band Tx IL [dB] Rx IL [dB] 3 0.77 0.77 7
0.82 0.82
* * *
For two simultaneous DL and one UL the ∆T~IB,c~ and ∆R~IB~ values are given in
the tables below:
Table 6.3.1.1.4-3: ΔT~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_3A-7A 3 0.5 7 0.5
* * *
NOTE To meet the ΔT~IB,c~ requirements with state-of-the-art technology, an
increase in power consumption of the UE may be required. It is also expected
that as the state-of-the-art technology evolves in the future, this possible
power consumption increase can be reduced or eliminated.
Table 6.3.1.1.4-4: ΔR~IB~
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB~ [dB] CA_3A-7A 3 0 7 0
* * *
### 6.3.2 LTE-Advanced Carrier Aggregation of Band 5 and Band 12 (1 UL)
Table 6.3.2-1: Inter-band CA
+-------+-------+-------+-------+-------+-------+----+-------+-----+ | E | E | U | Dow | D | | | | | | -UTRA | -UTRA | plink | nlink | uplex | | | | | | CA | | (UL) | (DL) | Mode | | | | | | Band | Band | band | band | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | | | BS | BS | | | | | | | | | re | tra | | | | | | | | | ceive | nsmit | | | | | | | | | / UE | / UE | | | | | | | | | tra | re | | | | | | | | | nsmit | ceive | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | | | F~UL\ | F~DL\ | | | | | | | | | _low~ | _low~ | | | | | | | | | -- | -- | | | | | | | | | F | F | | | | | | | | | ~UL_ | ~DL_ | | | | | | | | | high~ | high~ | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | CA\ | 5 | 824 | -- | 849 | 869 | -- | 894 | FDD | | _5-12 | | MHz | | MHz | MHz | | MHz | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | | 12 | 699 | -- | 716 | 729 | -- | 746 | | | | | MHz | | MHz | MHz | | MHz | | +-------+-------+-------+-------+-------+-------+----+-------+-----+
#### 6.3.2.1 List of specific combination issues
##### 6.3.2.1.1 Channel bandwidths per operating band for CA
Table 6.3.2.1.1-1: Supported E-UTRA bandwidths per CA configuration for inter-
band CA
* * *
E-UTRA band / channel bandwidth
E-UTRA\ E-UTRA Bands 1.4 MHz 3 MHz 5 MHz 10 MHz 15 MHz 20 MHz CA Band
CA_5A-12A 5 Yes
                                    12                                       Yes
* * *
##### 6.3.2.1.2 Co-existence studies for CA_5-12
The combination of band 5 and band 12 has harmonic frequencies that are far
removed from the component receive and transmit frequencies, in the UL and in
the DL of the CA combination, as shown in table 6.3.2.1.2-1. Since there are
no harmonics that coincide with the Rx bandwidth of either of the two bands
participating in the CA, additional filtering or de-sensitization impacts are
not anticipated.
Table 6.3.2.1.2-1: Impact of UL/DL Harmonic Interference
* * *
                                                                                       2^nd^ Harmonic     3^rd^ Harmonic      2^nd^ Harmonic     3^rd^ Harmonic
Band UL Low Band Edge UL High Band Edge DL Low Band Edge DL High Band Edge UL
Low Band Edge UL High Band Edge UL Low Band Edge UL High Band Edge DL Low Band
Edge DL High Band Edge DL Low Band Edge DL High Band Edge 5 824 849 869 894
1648 1698 2472 2547 1738 1788 2607 2682 12 699 716 729 746 1398 1432 2097 2148
1458 1492 2187 2238
* * *
Table 6.3.1.1.2-2 gives the frequency range of the second and third order
inter-modulation products when two simultaneous ULs are active in band 5 and
band 12. It can be seen that the inter-modulation products are not falling
within the two bands and therefore no further relaxation is needed.
Table 6.3.2.1.2-2: Second-order and third-order inter-modulation products
+------+---------+---------+---------+---------+---------+---------+ | Band | UL low | UL high | DL low | DL high | UL | UL | | | band | band | band | band | 2^nd^ | 3^rd^ | | | edge | edge | edge | edge | order | order | | | | | | | p | p | | | | | | | roducts | roducts | +------+---------+---------+---------+---------+---------+---------+ | 5 | 824 MHz | 849 MHz | 869 MHz | 894 MHz | 1523 -- | 2097 -- | | | | | | | 1565 | 2148 | | | | | | | MHz | MHz | | | | | | | | | | | | | | | | 2347 -- | | | | | | | | 2414 | | | | | | | | MHz | | | | | | | | | | | | | | | | 2472 -- | | | | | | | | 2547 | | | | | | | | MHz | +------+---------+---------+---------+---------+---------+---------+ | 12 | 699 MHz | 716 MHz | 729 MHz | 746 MHz | | | +------+---------+---------+---------+---------+---------+---------+
##### 6.3.2.1.2.1 Co-existence studies for 1 UL/2 DL
The 2^nd^ and 3^rd^ order harmonics and IMD products caused in the BS by
transmitting of Band 5 and Band 12 DL carriers can be calculated as shown in
table 6.3.2.1.2.1-1 below:
Table 6.3.2.1.2.1-1: Band 5 and Band 12 DL harmonics and IMD products
* * *
BS DL carriers f1_low f1_high f2_low f2_high DL frequency (MHz) 729 746 869
894 2^nd^ order harmonics frequency range (MHz) 1458 1492 1738 1788 3^rd^
order harmonics frequency range (MHz) 2187 2238 2607 2682 2^nd^ order IMD
products (f2_low -- f1_high) (f2_high -- f1_low) (f2_low + f1_low) (f2_high +
f1_high) IMD frequency limits (MHz) 123 165 1598 1640 3^rd^ order IMD products
(2*f1_low -- f2_high) (2*f1_high -- f2_low) (2*f2_low -- f1_high) (2*f2_high
-- f1_low) IMD frequency limits (MHz) 564 623 992 1059 3^rd^ order IMD
products (2*f1_low + f2_low) (2*f1_high + f2_high) (2*f2_low + f1_low)
(2*f2_high + f1_high) IMD frequency limits (MHz) 2327 2386 2467 2534 3^rd^
order IMD products (f1_low -- f2_high + f2_low) (f1_high + f2_high -- f2_low)
(f2_low -- f1_high + f1_low) (f2_high + f1_high -- f1_low) IMD frequency
limits (MHz) 704 771 852 911
* * *
It can be seen from table 6.3.2.1.2.1-1 that the 2^nd^ and 3^rd^ harmonics of
Band 5 and Band 12 DL carriers may fall into the BS receive band of Bands 3,
4, 9, 10, 21, 38 and 41, while the 2^nd^ IMD products caused by BS supporting
carrier aggregation of Band 5 and Band 12 may fall into the BS receive band of
Band 24, and the 3^rd^ IMD products may fall into the BS receive band of Bands
7, 8, 12, 17, 20, 40 and 41. Note that the calculation in table 6.3.2.1.2.1-1
assumes the BS is transmitting with the whole 25 MHz DL frequency of Band 5
and the whole 17 MHz DL frequency of Band 12. If the BS is only transmitting
an up to 10 MHz DL in Band 5 and a 10 MHz DL in Band 17 as stated in the WIDS,
then the 3^rd^ IMD products will not fall into the BS receive band of Bands 7,
12, 17, 40 and 41. In particular, the 3^rd^ IMD products will not fall into
the BS receive band of Bands 12 and 17 if the Band 5 DL bandwidth is not wider
than 13 MHz.
Since Bands 3, 8, 9, 20, 21 and 38 are not intended for use in the same
geographical area as Bands 5 and 12, the focus here will be on the harmonics
and IMD falling into Bands 4, 10, 24 and 41.
With the performances of the current BS antenna system, transmit and receive
path components, amplifiers, pre-distortion algorithms and filters, it is
expected that the IMD interference generated within the Band 4, 10, 24 or 41
receiver would be well below the receiver noise floor eliminating the
possibility of receiver desensitization, provided that Bands 5 and 12 BS
transmitters do not share the same antenna with Band 4, 10, 24 or 41 BS
receiver.
And it is recommended that Bands 5 and 12 BS transmitters should not share the
same antenna with Band 4, 10, 24 or 41 BS receiver, unless the antenna path
meets very stringent 2^nd^ and 3^rd^ order PIM specification so that the PIM
will not cause Band 4, 10, 24 or 41 BS receiver desensitization. Note that
antenna sharing may be allowed as the state-of-the-art continues to evolve in
the future.
##### 6.3.2.1.3 ∆T~IB~ and ∆R~IB~ values
The reported additional IL (Insertion Loss) values, based on
implementation/simulation data, under ETC (Extreme Temperature Conditions) for
combining band 5 and band 12, for each of the Tx and Rx paths, from [21], are
shown in table 6.3.2.1.3-1.
Table 6.3.2.1.3-1: IL values for band 5 + 12 diplexer and quadplexers (under
ETC)
* * *
E-UTRA bands IL (dB) IL (dB) IL (dB) IL (dB) 5 Tx 0.7 0.6 2.3 0.7 5 Rx 0.7 0.7
1.8 0.8 12 Tx 0.5 0.3 1.2 0.5 12 Rx 0.5 0.3 1.8 0.5
* * *
For the reported additional IL values, the corresponding average additional IL
values for the Tx and the Rx paths, from [21], are shown in table 6.3.2.1.3-2:
Table 6.3.2.1.3-2: Average Tx and Rx IL for combining band 5 and band 12
(under ETC)
* * *
Inter-band CA Configuration E-UTRA Band Tx IL [dB] Rx IL [dB] 5 1.1 1.0 12 0.6
0.8
* * *
For two simultaneous DLs and one UL the ∆T~IB,c~ and ∆R~IB~ values, from [21],
are shown in table 6.3.2.1.3-3, and in table 6.3.2.1.3-4:
Table 6.3.2.1.3-3: ΔT~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_5A-12A 5 0.8 12 0.4
* * *
Table 6.3.2.1.3-4: ΔR~IB~
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB~ [dB] CA_5A-12A 5 0.5 12 0.3
* * *
### 6.3.3 LTE-Advanced Carrier Aggregation of Band 5 and Band 17 (1 UL)
Table 6.3.3-1: Inter-band non-contiguous CA
+-------+-------+-------+-------+-------+-------+----+-------+-----+ | E | E | U | Dow | D | | | | | | -UTRA | -UTRA | plink | nlink | uplex | | | | | | CA | | (UL) | (DL) | Mode | | | | | | Band | Band | oper | oper | | | | | | | | | ating | ating | | | | | | | | | band | band | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | | | BS | BS | | | | | | | | | re | tra | | | | | | | | | ceive | nsmit | | | | | | | | | / UE | / UE | | | | | | | | | tra | re | | | | | | | | | nsmit | ceive | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | | | F~UL\ | F~DL\ | | | | | | | | | _low~ | _low~ | | | | | | | | | -- | -- | | | | | | | | | F | F | | | | | | | | | ~UL_ | ~DL_ | | | | | | | | | high~ | high~ | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | CA\ | 5 | 824 | -- | 849 | 869 | -- | 894 | FDD | | _5-17 | | MHz | | MHz | MHz | | MHz | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | | 17 | 704 | -- | 716 | 734 | -- | 746 | | | | | MHz | | MHz | MHz | | MHz | | +-------+-------+-------+-------+-------+-------+----+-------+-----+
#### 6.3.3.1 List of specific combination issues
##### 6.3.3.1.1 Channel bandwidths per operating band for CA
Table 6.3.3.1.1-1: Supported E-UTRA bandwidths per CA configuration for inter-
band CA
* * *
E-UTRA band / channel bandwidth
E-UTRA\ E-UTRA Bands 1.4 MHz 3 MHz 5 MHz 10 MHz 15 MHz 20 MHz CA Band
CA_5A-17A 5 Yes Yes
                                    17                               Yes     Yes
* * *
##### 6.3.3.1.2 Co-existence studies for CA_5-17
The 2^nd^ and 3^rd^ order harmonics and IMD products caused in the BS by
transmitting of band 5 and band 17 DL carriers can be calculated as shown in
table 6.3.3.1.2-1 below:
Table 6.3.3.1.2-1: Band 5 and Band 17 DL harmonics and IMD products
* * *
BS DL carriers f1_low f1_high f2_low f2_high DL frequency (MHz) 734 746 869
894 2^nd^ order harmonics frequency range (MHz) 1468 1492 1738 1788 3^rd^
order harmonics frequency range (MHz) 2202 2238 2607 2682 2^nd^ order IMD
products (f2_low -- f1_high) (f2_high -- f1_low) (f2_low + f1_low) (f2_high +
f1_high) IMD frequency limits (MHz) 123 160 1603 1640 3^rd^ order IMD products
(f2_low -- 2*f1_high) (f2_high -- 2*f1_low) (2*f2_low -- f1_high) (2*f2_high
-- f1_low) IMD frequency limits (MHz) 574 623 992 1054 3^rd^ order IMD
products (2*f1_low + f2_low) (2*f1_high + f2_high) (2*f2_low + f1_low)
(2*f2_high + f1_high) IMD frequency limits (MHz) 2337 2386 2472 2534 3^rd^
order IMD products (f1_low -- f2_high + f2_low) (f1_high + f2_high -- f2_low)
(f2_low -- f1_high + f1_low) (f2_high + f1_high -- f1_low) IMD frequency
limits (MHz) 709 771 857 906 3^rd^ order IMD products (with maximum channel
bandwidth) (f1_low -- f2_BWmax) (f1_high + f2_BWmax) (f2_low -- f1_BWmax)
(f2_high + f1_BWmax) IMD frequency limits (MHz) 714 766 859 904
* * *
It can be seen from table 6.3.3.1.2-1 that the 2^nd^ and 3^rd^ harmonics of
band 5 carriers may fall into the BS receive band of bands 3, 4, 9, 10, 38 and
41, while the 2^nd^ IMD products caused by BS supporting carrier aggregation
of band 5 and band 17 may fall into the BS receive band of band 24, and the
3^rd^ IMD products may fall into the BS receive band of bands 7, 8, 12, 17,
20, 28, 40, 41 and 44. Note that the calculation in table 6.3.3.1.2-1 (except
the last row) assumes the BS is transmitting with the whole 25 MHz DL
frequency of band 5 and the whole 12 MHz DL frequency of band 17. Even if the
BS is only transmitting 10, 15 or 20 MHz DL in band 5 and band 17 as stated in
the WIDS, the 3^rd^ IMD products may still fall into the same set of BS
receive bands as shown in the last row in table 6.3.3.1.2-1.
Note that bands 3, 7, 8, 9, 20, 28, 38, 40 and 44 are not intended for use in
the same geographical area as bands 5 and 17. Furthermore, the 3^rd^ IMD
products for band (5 + 17) DL at 714 -- 766 MHz will not fall into the band 12
or 17 UL if the UL carrier is located out of this frequency range (e.g. locate
the 10 MHz UL carrier for band 12 or 17 at 704 -- 714 MHz) or the band 5 DL
bandwidth is limited to not wider than 18 MHz.
With the performances of the current BS antenna system, transmit and receive
path components, amplifiers, pre-distortion algorithms and filters, it is
expected that the IMD interference generated within the band 4, 10 or 41
receiver would be well below the receiver noise floor eliminating the
possibility of receiver desensitization, provided that bands 5 and 17 BS
transmitters do not share the same antenna with band 4, 10 or 41 BS receiver.
Therefore, it is recommended that bands 5 and 17 BS transmitters should not
share the same antenna with band 4, 10 or 41 BS receiver, or with band 12 or
17 BS receiver unless the band 12 or 17 UL carrier is located out of the
frequency range at 714 -- 766 MHz or the band 5 DL bandwidth is limited to not
wider than 18 MHz, unless the antenna path meets very stringent 3^rd^ order
PIM specification so that the PIM will not cause band 4, 10, 12, 17 or 41 BS
receiver desensitization.
##### 6.3.3.1.3 ∆T~IB~ and ∆R~IB~ values
The insertion loss and ∆T~IB~ and ∆R~IB~ values for CA_5-17 are the same as
those for CA_5-12.
The reported additional IL (Insertion Loss) values, based on
implementation/simulation data, under ETC (Extreme Temperature Conditions) for
combining band 5 and band 12 (same value used for combining band 5 and band
17), for each of the Tx and Rx paths, from [21], are shown in table
6.3.3.1.3-1.
Table 6.3.3.1.3-1: IL values for band 5 + 17 diplexer and quadplexers (under
ETC)
* * *
E-UTRA bands IL (dB) IL (dB) IL (dB) IL (dB) 5 Tx 0.7 0.6 2.3 0.7 5 Rx 0.7 0.7
1.8 0.8 17 Tx 0.5 0.3 1.2 0.5 17 Rx 0.5 0.3 1.8 0.5
* * *
For the reported additional IL values, the corresponding average additional IL
values for the Tx and the Rx paths, from [21], are shown in table 6.3.3.1.3-2:
Table 6.3.3.1.3-2: Average Tx and Rx IL for combining band 5 and band 17
(under ETC)
* * *
Inter-band CA Configuration E-UTRA Band Tx IL [dB] Rx IL [dB] 5 1.1 1.0 17 0.6
0.8
* * *
For two simultaneous DLs and one UL the ∆T~IB,c~ and ∆R~IB~ values, from [21],
are shown in table 6.3.3.1.3-3, and in table 6.3.3.1.3-4:
Table 6.3.3.1.3-3: ΔT~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_5A-17A 5 0.8 17 0.4
* * *
Table 6.3.3.1.3-4: ΔR~IB~
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB~ [dB] CA_5A-17A 5 0.5 17 0.3
* * *
### 6.3.4 LTE inter-band carrier aggregation for bands 8+20 (1 UL)
CA_8-20 inter-band combination is designed to operate in the following bands
defined in table 6.3.4-1. In this section only 2DL and 1UL case in considered.
Table 6.3.4-1: Inter band CA operating bands
* * *
E-UTRA CA Band E-UTRA Band Uplink (UL) operating band Downlink (DL) operating
band Duplex Mode  
BS receive / UE transmit BS transmit / UE receive  
F~UL_low~ -- F~UL_high~ F~DL_low~ -- F~DL_high~  
CA_8-20 8 880 MHz -- 915 MHz 925 MHz -- 960 MHz FDD 20 832 MHz -- 862 MHz 791
MHz -- 821 MHz
* * *
#### 6.3.4.1 List of specific combination issues
##### 6.3.4.1.1 Channel bandwidths per operating band for CA
Supported channel bandwidths per operating band for CA_8-20 are shown in table
6.3.4.1.1-1.
Table 6.3.4.1.1-1: Supported E-UTRA bandwidths per CA configuration for inter-
band CA
* * *
CA operating / channel bandwidth  
E-UTRA CA Configuration E-UTRA Bands 1.4 MHz 3 MHz 5 MHz 10 MHz 15 MHz 20 MHz
CA_8A-20A 8 Yes Yes  
20 Yes Yes
* * *
##### 6.3.4.1.2 Co-existence studies for for CA_8-20 (1 UL/2 DL)
The 2^nd^ and 3^rd^ order harmonics and IMD products caused in the BS by
transmitting of Band 8 and Band 20 DL carriers can be calculated as shown in
table 6.3.4.1.2-1 below:
Table 6.3.4.1.2-1: Band 8 and Band 20 DL harmonics and IMD products
* * *
BS DL carriers f1_low f1_high f2_low f2_high DL frequency (MHz) 791 821 925
960 2^nd^ harmonics frequency limits (MHz) 1582 1642 1850 1920 3^rd^ harmonics
frequency limits (MHz) 2373 2463 2775 2880 2^nd^ order IMD products (f2_low --
f1_high) (f2_high -- f1_low) (f2_low + f1_low) (f2_high + f1_high) IMD
frequency limits (MHz) 104 169 1716 1781 3^rd^ order IMD products (2*f1_low
--f2_high) (f2*1_high --f2_low) (2*f2_low -- f1_high) (2*f2_high -- f1_low)
IMD frequency limits (MHz) 622 717 1029 1129 3^rd^ order IMD products
(2*f1_low + f2_low) (2*f1_high + f2_high) (2*f2_low + f1_low) (2*f2_high +
f1_high) IMD frequency limits (MHz) 2507 2602 2461 2741 3^rd^ order IMD
products (f1_low -- f2_high + f2_low) (f1_high + f2_high -- f2_low) (f2_low --
f1_high + f1_low) (f2_high + f1_high -- f1_low) IMD frequency limits (MHz) 756
856 895 990 3^rd^ order IMD products (with maximum channel bandwidth) (f1_low
-- f2_BWmax) (f1_high + f2_BWmax) (f2_low -- f1_BWmax) (f2_high + f1_BWmax)
IMD frequency limits (MHz) 781 831 915 970
* * *
It can be seen from table 6.3.4.1.2-1 that the 2^nd^ harmonics of BS
transmitting in Bands 8 and 20 may fall into the BS receive band of Bands 2,
24, 25, 33, 35, 37 and 39, and the 3^rd^ harmonics may fall into the BS
receive band of Band 40, while the 2^nd^ IMD products of BS supporting CA of
Band 8 and Band 20 may fall into the BS receive band of Bands 3, 4, 9 and 10,
and the 3^rd^ IMD products may fall into the BS receive band of Bands 5, 6, 7,
8, 12, 13, 14, 17, 18, 19, 20, 26, 27, 28, 38, 41 and 44. Note that the
calculation in table 6.3.4.1.2-1 (except the last row) assumes the BS is
transmitting with the whole 35 MHz DL frequency of Band 8 and the whole 30 MHz
DL frequency of Band 20. If the BS is only transmitting up to 10 MHz DL in
Band 8 and Band 20 as prioritized in the WIDS, then the 3^rd^ IMD products
will not fall into the BS receive band of Bands 8 and 20 as shown in the last
row in table 6.3.4.1.2-1.
Note that Bands 2, 4, 5, 6, 9, 10, 12, 13, 14, 17, 18, 19, 24, 25, 26, 27, 28,
35, 37, 39, 40, 41 and 44 are not intended for use in the same geographical
area as Bands 8 and 20. Moreover, with the performances of the current BS
antenna system, transmit and receive path components, amplifiers, pre-
distortion algorithms and filters, it is expected that the IMD interference
generated within the Band 3, 7, 33 or 38 receiver would be well below the
receiver noise floor eliminating the possibility of receiver desensitization,
provided that Bands 8 and 20 BS transmitters do not share the same antenna
with Band 3, 7, 33 or 38 BS receiver.
Therefore, it is recommended that Bands 8 and 20 BS transmitters should not
share the same antenna with Band 3, 7, 33 or 38 BS receiver, unless the
antenna path meets very stringent 3rd order PIM specification so that the PIM
will not cause Band 3, 7, 33 or 38 BS receiver desensitization.
If channel bandwidths larger than 10 MHz, i.e. 15 MHz and 20 MHz, would be
supported for either Band 8 or Band 20, the 3^rd^ order IMD products may fall
into part of Band 8 and Band 20 receive band for some configurations (certain
carrier location and channel bandwidth combinations). In such cases, it could
be necessary to avoid sharing the same RF path for both transmitter and
receiver side, or avoid such configurations in the BS.
##### 6.3.4.1.3 ∆TIB and ∆RIB values
For 2 DL and 1 UL the ∆T~IB,c~ the incremental additional losses created by
the need for a quadplexer design compared to independent duplexer filter are
presented in table below:
Table 6.3.4.1.3-1: Reported incremental ILs for band 8 + 20 quadplexer
compared to duplexer
* * *
E-UTRA bands B8 UL B20 UL B8 DL B20 DL Vendor 1D1 0.9 1 0.7 0.8 Vendor 1D2 0.7
0.8 1.3 0.8 Vendor 1D3 0.6 0.9 0.8 0.9 Vendor 2 0.8 0.8 0.8 0.8 Vendor 3 0.5
0.5 0.5 0.5 Vendor 4 0.47 0.45 0.23 0.54 Vendor 5 1 0.8 1.2 1.4 Vendor 6 1 1
0.9 0.3 0.75 0.78 0.8 0.76
* * *
For 2 DL and 1 UL the ∆T~IB,c~ and ∆R~IB~ values are given in the tables
below:
Table 6.3.4.1.3-2: ΔT~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_8A-20A 8 0.4 20 0.4
* * *
Table 6.3.4.1.3-3: ΔR~IB~
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB~ [dB] CA_8A-20A 8 0 20 0
* * *
### 6.3.5 LTE inter-band Carrier Aggregation Band 4 and Band 7 (1 UL)
Table 6.3.5.1 shows the operating bands for CA Band 4 and Band 7.
Table 6.3.5.1: Inter band CA operating bands
E-UTRA CA Band | E-UTRA Band | Uplink (UL) band | Downlink (DL) band | Duplex mode |  |  |  |  |  |   
---|---|---|---|---|---|---|---|---|---|---  
|  | BS receive / UE transmit | Channel BW (MHz) | BS transmit / UE receive | Channel  
BW (MHz) |  |  |  |  |   
|  | FUL_low – FUL_high |  | FDL_low – FDL_high |  |  |  |  |  |   
CA_4-7 | 4 | 1710 MHz | – | 1755 MHz | 5, 10 | 2110 MHz | – | 2155 MHz | 5, 10 | FDD  
| 7 | 2500 MHz | – | 2570 MHz | 5, 10, 15, 20 | 2620 MHz | – | 2690 MHz | 5, 10, 15, 20 | FDD  
#### 6.3.5.1 List of specific combination issues
##### 6.3.5.1.1 Channel bandwidths per operating band for CA
Table 6.3.5.1.1: Supported E-UTRA bandwidths per CA configuration for inter-
band CA
* * *
E-UTRA band / channel bandwidth
E-UTRA\ E-UTRA Bands 1.4 MHz 3 MHz 5 MHz 10 MHz 15 MHz 20 MHz CA Band
CA_4A-7A 4 Yes Yes
                                    7                                Yes     Yes      Yes      Yes
* * *
##### 6.3.5.1.2 Co-existence studies for CA_4-7
Table 6.3.5.1.2-1 includes the 2^nd^ and 3^rd^ order harmonic products for
band 3 + band 7 CA with 1 UL. Table 6.3.5.1.2-2 shows the 2^nd^ and 3^rd^
order harmonics and IMD products identified for Band 4 and Band 7 DL:
Table 6.3.5.1.2-1: Band 4 and Band 7 UL harmonics products
* * *
UE UL carriers f1_low f1_high f2_low f2_high UL frequency (MHz) 1710 1735 2500
2570 2^nd^ harmonics frequency limits (MHz) 3420 3510 5000 5140 3^rd^
harmonics frequency limits (MHz) 5130 5265 7500 7710
* * *
Table 6.3.5.1.2-2: Band 4 and Band 7 DL harmonics and IMD products
+-------------+-------------+-------------+-------------+-------------+ | BS DL | f1_low | f1_high | f2_low | f2_high | | carriers | | | | | +-------------+-------------+-------------+-------------+-------------+ | DL | 2110 | 2155 | 2620 | 2690 | | frequency | | | | | | (MHz) | | | | | +-------------+-------------+-------------+-------------+-------------+ | 2^nd^ | 4220 | 4310 | 5240 | 5380 | | harmonics | | | | | | frequency | | | | | | limits | | | | | | (MHz) | | | | | +-------------+-------------+-------------+-------------+-------------+ | 3^rd^ | 6330 | 6465 | 7860 | 8070 | | harmonics | | | | | | frequency | | | | | | limits | | | | | | (MHz) | | | | | +-------------+-------------+-------------+-------------+-------------+ | 2^nd^ order | (f2_low -- | (f2_high | (f2_low + | (f2_high + | | IMD | f1_low) / | -- f1_ | f1_low) / | f1_low) / | | products | f2_low -- | high) / | f2_low + | f2_high + | | | f1_high | (f2_high | f1_ high) | f1_high) | | | | -- f1_ | | | | | | high) | | | +-------------+-------------+-------------+-------------+-------------+ | MD | 510 / 465 | 580 / 545 | 4730 / 4775 | 4800 / 4845 | | frequency | | | | | | limits | | | | | | (MHz) | | | | | +-------------+-------------+-------------+-------------+-------------+ | 2^nd^ order | 465-580 | 4730-4845 | | | | IMD | | | | | | frequency | | | | | | range (MHz) | | | | | +-------------+-------------+-------------+-------------+-------------+ | 3^rd^ order | (2*f1_low | ( | (2*f2_low | ( | | IMD | -- | 2*f1_high | -- f1_low) | 2*f2_high | | products | f2_low)/\ | -- f2_low) | /\ | -- f1_low) | | | (2*f1_low | /\ | 2*f2_low | /\ | | | -- | (2* | -- | 2*f2_high | | | f2_high) | f1_high -- | f1_high) | -- | | | | f2_high) | | f1_high) | +-------------+-------------+-------------+-------------+-------------+ | IMD | 1600 / 1530 | 1690 / 1620 | 3130 / 3085 | 3270 /3225 | | frequency | | | | | | limits | | | | | | (MHz) | | | | | +-------------+-------------+-------------+-------------+-------------+ | 3rd order | (2*f1_low | ( | (2*f2_low | ( | | IMD | + f2_low) | 2*f1_high | + f1_low) | 2*f2_high | | products | /\ | + f2_low) | /\ | + f1_low) | | | 2*f1_low | /\ | 2*f2_low | /\ | | | + f2_high) | (2* | + f1_high) | 2*f2_high | | | | f1_high + | | + f1_high) | | | | f2_high) | | | +-------------+-------------+-------------+-------------+-------------+ | IMD | 6840 / 6910 | 6930 / 7000 | 7350 / 7395 | 7490 / 7535 | | frequency | | | | | | limits | | | | | | (MHz) | | | | | +-------------+-------------+-------------+-------------+-------------+ | 3^rd^ order | 1530 -- | 3085 -- | | | | IMD | 1690 | 3270 | | | | frequency | | | | | | range (MHz) | 6840 - 7000 | 7350 - 7535 | | | +-------------+-------------+-------------+-------------+-------------+
With reference to the above tables, it can be seen that there are neither
harmonic nor inter-modulation products falling within inter-band CA_4+7
operating frequency ranges. 2^nd^ harmonics from the UE can fall into Band 22.
However, it can be assumed that the harmonics will be attenuated by the duplex
filter. It can be concluded that there is no issue on harmonic and
intermodulation interference.
##### 6.3.5.1.3 ∆T~IB~ and ∆R~IB~ values
The insertion loss and ∆T~IB~ and ∆R~IB~ values for CA_4-7 are derived by
using the requirements and data for the configurations CA_1-7 and CA_3_7 as
proxy.
For CA_4-7
1\. the response for Band 7 TX needs to supply large attenuation at Band 4 RX
and Band 7 RX, where Band 4 RX is a subset of Band 1 RX (cf. CA_1-7);
2\. the response for Band 4 TX, a subset of Band 3 TX, needs to supply large
attenuation at Band 4 RX and Band 7 RX, where Band 4 RX is at larger
separation from the Band 4 TX compared to Band 3 RX;
3\. the response for Band 7 RX needs to supply large attenuation at Band 4 TX
and Band 7 TX, where Band 4 TX is a subset of Band 3 TX (cf. CA_3-7).
4\. the response for Band 4 RX, a subset of Band 1 TX, needs to supply large
attenuation at Band 4 TX and Band 7 TX, where Band 4 TX is at larger
separation compared to Band 1 RX.
For the Band 7 TX of CA_4-7 (Item 1), the same requirement as for Band 7 TX of
CA_3-7 is proposed: CA_3-7 has the same average reported IL as CA_1-7 for Band
7 TX (table 6.3.5.1.3-2).
For the Band 4 TX of CA_4-7 (Item 2), the same requirement as for Band 3 TX of
CA_3-7 is proposed (table 6.3.1.1.4-3): even if the narrower Band 4 RX is at
larger separation than the wider Band 3 RX, duplexer characteristics typically
display fly-back, a decreased attenuation as the frequency is increased above
the TX passband.
For the Band 7 RX of CA_4-7 (Item 3), the same requirement as for Band 7 RX of
CA_3-7 could possibly be used. However, a penalty of ΔR~IB~ = 0.5 dB for Band
7 RX is proposed in view of the average reported IL of Band 7 RX for CA_1-7
(table 6.3.5.1.3-2) with the same frequency separation between the lower
receive band and the high transmit band.
For the Band 4 RX of CA_4-7 (Item 4), a ΔR~IB~ = 0.5 dB is proposed for Band 4
RX in view of the challenging matching for Band 4 and the legacy Band 4
reference sensitivity requirements.
For two simultaneous DL(s) and one UL the ∆T~IB,c~ and ∆R~IB~ values are shown
in table 6.3.5.1.3-1 and table 6.3.5.1.3-2 [23]:
Table 6.3.5.1.3-1: ΔT~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_4A-7A 4 0.5 7 0.5
* * *
Table 6.3.5.1.3-2: ΔR~IB~
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB~ [dB] CA_4A-7A 4 0.5 7 0.5
* * *
## 6.4 Class A4. Low-low, low-high or high-high band combination with
intermodulation problem (low order IM)
This subclause shall include all inter band CA combinations which can be
included in the group low-low or high-high combinations with transmitter
harmonics.
## 6.5 Class A5. Combination except for A1 -- A4
### 6.5.1 LTE Advanced Carrier Aggregation of Band 11 and Band 18
Table 6.5.1-1: Inter-band CA operating bands
E-UTRA CA Band | E-UTRA Band | Uplink (UL) band | Downlink (DL) band | Duplex mode |  |  |  |  |  |   
---|---|---|---|---|---|---|---|---|---|---  
|  | BS receive / UE transmit | Channel BW (MHz) | BS transmit / UE receive | Channel BW (MHz) |  |  |  |  |   
|  | FUL_low – FUL_high |  | FDL_low – FDL_high |  |  |  |  |  |   
CA_11-18 | 11 | 1427.9 MHz | – | 1447.9 MHz | 5, 10 | 1475.9 MHz | – | 1495.9 MHz | 5, 10 | FDD  
| 18 | 815 MHz | – | 830 MHz | 5, 10, 15 | 860 MHz | – | 875 MHz | 5, 10, 15 |   
#### 6.5.1.1 List of specific combination issues
##### 6.5.1.1.1 Channel bandwidths per operating band for CA
Table 6.5.1.1.1-1: Supported E-UTRA bandwidths per CA configuration for inter-
band CA
* * *
CA operating / channel bandwidth  
E-UTRA CA Configuration E-UTRA Bands 1.4 MHz 3 MHz 5 MHz 10 MHz 15 MHz 20 MHz
CA_11A-18A 11 Yes Yes  
18 Yes Yes Yes
* * *
##### 6.5.1.1.2 Co-existence studies for CA_11-18
Although Band 11 and Band 18 are not categorized as A1 -- A4, frequency
separation between two bands are at least more than 500 MHz. In addition, as
observed in table 6.5.1.1.2-1, the harmonic frequencies do not fall into the
frequency ranges of both bands. Therefore we can conclude that there is no
issue on harmonic interference.
Table 6.5.1.1.2-1: Impact of UL/DL Harmonic Interference
* * *
                                                                                       2^nd^ Harmonic     3^rd^ Harmonic      2^nd^ Harmonic     3^rd^ Harmonic
Band UL Low Band Edge UL High Band Edge DL Low Band Edge DL High Band Edge UL
Low Band Edge UL High Band Edge UL Low Band Edge UL High Band Edge DL Low Band
Edge DL High Band Edge DL Low Band Edge DL High Band Edge 11 1427.9 1447.9
1475.9 1495.9 2855.8 2895.8 4283.7 4343.7 2951.8 2991.8 4427.7 4487.7 18 815
830 860 875 1630 1660 2445 2490 1720 1750 2580 2625
* * *
Table 6.5.1.1.2-2 and 6.5.1.1.2-3 give the frequency range of the third and
fifth order intermodulation product when two simultaneous ULs/DLs are active
in Band 11 and Band 18. It can be seen that the intermodulation products are
not falling within the two inter-bands and therefore no further relaxation is
needed.
Table 6.5.1.1.2-2: Third order and fifth order intermodulation products (UL)
+------+--------------+--------------+--------------+--------------+ | Band | UL Low Band | UL High Band | UL 3^rd^ | UL 5^th^ | | | Edge | Edge | order | order | | | | | products | products | +------+--------------+--------------+--------------+--------------+ | 11 | 1920 MHz | 1980 MHz | 182.1 -- | N/A | | | | | 232.1 MHz | | | | | | | 2623.7 -- | | | | | 2025.8 -- | 2713.7 MHz | | | | | 2080.8 MHz | | +------+--------------+--------------+--------------+--------------+ | 18 | 815 MHz | 830 MHz | | | +------+--------------+--------------+--------------+--------------+
Table 6.1.7.1.2-3: Third order and fifth order intermodulation products (DL)
+------+--------------+--------------+--------------+--------------+ | Band | UL Low Band | UL High Band | UL 3^rd^ | UL 5^th^ | | | Edge | Edge | order | order | | | | | products | products | +------+--------------+--------------+--------------+--------------+ | 11 | 2110 MHz | 2170 MHz | 224.1 -- | N/A | | | | | 274.1 MHz | | | | | | | 2677.7 -- | | | | | 2076.8 -- | 4790 MHz | | | | | 2131.8 MHz | | +------+--------------+--------------+--------------+--------------+
##### 6.5.1.1.3 ∆T~IB~ and ∆R~IB~ values
Following values are reported for IL values of diplexer regarding Band 11 and
Band. Note that maximum values are displayed.
Table 6.5.1.1.3-1: Reported ILs for Band 11 + 18 diplexer and quadplexers for
ETC
* * *
                                                                                                         Maximum IL value (dB)   Average IL value (dB)                             
                                                                                                         Company A               Company B               Company C
Tx Band 11 UL 0.6 0.65 0.31 (Note) 0.52 Band 18 UL 0.6 0.80 0.21 (Note) 0.54
Rx Band 11 DL 0.6 0.65 0.22 (Note) 0.52 Band 18 DL 0.6 0.80 0.34 (Note) 0.58
NOTE: Values are typical and reference due to its architecture (diplexer and
duplexer are combined).
* * *
According to information from table 6.5.1.1.3-1, following relaxations are
allowed for the UE which supports inter-band carrier aggregation of Band 11
and Band 18. Values are applicable both for 1 UL and 2 UL.
Table 6.5.1.1.3-2: ∆Τ~IB,c~
* * *
Inter-band CA Configuration E-UTRA Band ΔT~IB,c~ [dB] CA_11A-18A 11 0.6 18 0.6
* * *
Table 6.5.1.1.3-3: ΔR~IB~
* * *
Inter-band CA Configuration E-UTRA Band ΔR~IB~ [dB] CA_11A-18A 11 0.6 18 0.6
* * *
### 6.5.2 LTE Advanced Carrier Aggregation of Band 1 and Band 21 (1 UL)
Table 6.5.2-1: Inter-band CA
+-------+-------+-------+-------+-------+-------+----+-------+-----+ | E | E | U | Dow | D | | | | | | -UTRA | -UTRA | plink | nlink | uplex | | | | | | CA | | (UL) | (DL) | Mode | | | | | | Band | Band | oper | oper | | | | | | | | | ating | ating | | | | | | | | | band | band | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | | | BS | BS | | | | | | | | | re | tra | | | | | | | | | ceive | nsmit | | | | | | | | | / UE | / UE | | | | | | | | | t | re | | | | | | | | | ransm | ceive | | | | | | | | | it^1^ | | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | | | F~UL\ | F~DL\ | | | | | | | | | _low~ | _low~ | | | | | | | | | -- | -- | | | | | | | | | F | F | | | | | | | | | ~UL_ | ~DL_ | | | | | | | | | high~ | high~ | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | CA\ | 1 | 1920 | -- | 1980 | 2100 | -- | 2170 | FDD | | _1-21 | | MHz | | MHz | MHz | | MHz | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | | 21 | 1 | -- | 1 | 1 | -- | 1 | | | | | 447.9 | | 462.9 | 495.9 | | 510.9 | | | | | MHz | | MHz | MHz | | MHz | | +-------+-------+-------+-------+-------+-------+----+-------+-----+ | NOTE | | | | | | | | | | 1: A | | | | | | | | | | s | | | | | | | | | | ingle | | | | | | | | | | u | | | | | | | | | | plink | | | | | | | | | | comp | | | | | | | | | | onent | | | | | | | | | | ca | | | | | | | | | | rrier | | | | | | | | | | of | | | | | | | | | | e | | | | | | | | | | ither | | | | | | | | | | Band | | | | | | | | | | 1 or | | | | | | | | | | Band | | | | | | | | | | 21 | | | | | | | | | | shall | | | | | | | | | | be | | | | | | | | | | used | | | | | | | | | | at | | | | | | | | | | any | | | | | | | | | | time. | | | | | | | | | +-------+-------+-------+-------+-------+-------+----+-------+-----+
#### 6.5.2.1 List of specific combination issues
##### 6.5.2.1.1 Channel bandwidths per operating band for CA
Table 6.5.2.1.1-1: Supported E-UTRA bandwidths per CA configuration for inter-
band CA
* * *
E-UTRA CA Configuration Supported E-UTRA bandwidths per CA configuration for
inter-band CA  
CA_1A-21A E-UTRA Bands Band 1  
Band 21 CBW 5 MHz 10 MHz 15 MHz 20 MHz 5 MHz Yes Yes Yes Yes 10 MHz Yes Yes
Yes Yes 20 MHz Yes Yes Yes Yes
* * *
##### 6.5.2.1.2 Co-existence studies for CA_1-21
As the harmonic frequencies are far away from the receive and transmit bands
of interest in the DL and UL (see table 6.5.2.1.2-1) and therefore we can
conclude that there is no issue on harmonic interference.
Table 6.5.2.1.2-1: Impact of UL/DL Harmonic Interference
* * *
                                                                                       2^nd^ Harmonic     3^rd^ Harmonic      2^nd^ Harmonic     3^rd^ Harmonic
Band UL Low Band Edge UL High Band Edge DL Low Band Edge DL High Band Edge UL
Low Band Edge UL High Band Edge UL Low Band Edge UL High Band Edge DL Low Band
Edge DL High Band Edge DL Low Band Edge DL High Band Edge 1 1920 1980 2110
2170 3840 3960 5760 5940 4220 4340 6330 6510 21 1447.9 1462.9 1495.9 1510.9
2895.8 2925.8 4343.7 4388.7 2991.8 3021.8 4487.7 4532.7
* * *
##### 6.5.2.1.3 ∆TIB and ∆RIB values
###### 6.5.2.1.3.1 Diplexer data
###### # 6.5.2.1.3.1.1 Summary of diplexer data
The data of devices to deal with inter band CA from four device vendors are
summarized in table 6.5.2.1.3.1.1-1.
Table 6.5.2.1.3.1.1-1: Diplexer/Quadplexer data from four device vendors (ETC)
| Vendor |  |  |  |  |  |  |  |   
---|---|---|---|---|---|---|---|---|---  
| 1 | 2 | 3 | 4 |  |  |  |  |   
| Min [dB] | Max [dB] | Min [dB] | Max [dB] | Min [dB] | Max [dB] | Min [dB] | Max [dB] |   
IL | B21 Tx | − | 0.43 | − | 0.64 | − | 0.30 | − | 0.59  
| B21 Rx | − | 0.45 | − | 0.64 | − | 0.30 | − | 0.62  
| B1 Tx | − | 0.65 | − | 0.76 | − | 0.50 | − | 0.49  
| B1 Rx | − | 0.50 | − | 0.76 | − | 0.50 | − | 0.52  
###### # 6.5.2.1.3.1.2 Details of the data in table 6.5.2.1.3.1.1-1
###### # 6.5.2.1.3.1.2.1 Vendor 1
{width="3.8006944444444444in" height="2.953472222222222in"}
Figure 6.5.2.1.3.1.2.1-1: Diplexer simulation data from Vendor 1
###### # 6.5.2.1.3.1.2.2 Vendor 2
{width="4.121527777777778in" height="2.686111111111111in"}
Figure 6.5.2.1.3.1.2.2-1: Diplexer data of real device from Vendor 2
{width="4.297916666666667in" height="2.7979166666666666in"}
Figure 6.5.2.1.3.1.2.2-2: Diplexer data of real device from Vendor 2
###### # 6.5.2.1.3.1.2.3 Vendor 3
Table 6.5.2.1.3.1.2.3-1: Quadplexer data from vendor 3
* * *
        Frequency (MHz)   Duplexer   Quadplexer            Difference \[dB\]         
                          Max        Typ/Min      Max                                
                          \[dB\]     \[dB\]       \[dB\]
IL B21 Tx 1448 1463 1.9 − 2.2 0.30 B21 Rx 1496 1511 2.0 − 2.3 0.30 B1 Tx 1920
1980 2.1 − 2.6 0.50 B1 Rx 2110 2170 2.5 − 3.0 0.50 ISO Tx to B21 Rx 1920 1980
− 61.2/55 − − B21 Tx to B1 Rx 1448 1463 − 63/55 − −
* * *
###### # 6.5.2.1.3.1.2.4 Vendor 4
In this sub-clause, a possible RF FE architecture is studied, which can obtain
sufficient ISO between the two bands, reduce insertion loss, and minimize its
size impact. In order to demonstrate its feasibility and effects, we compare
the performances of three RF FE prototypes as explained in figure
6.5.2.1.3.1.2.4-1.
{width="6.684722222222222in" height="1.5909722222222222in"}
Figure 6.5.2.1.3.1.2.4-1: Prototype RF FE architectures to study
\- (1) Non_CA type
This architecture is considered for comparison purpose, where it can not
realize CA.
\- (2) CA type w/o diplexer
In this architecture, ISO between B1 and B21 can be obtained through a
combiner implemented in LTCC substrate.
\- (3) CA type w diplexer
This architecture is also considered for comparison purpose.
Table 6.5.2.1.3.1.2.4-1 summarizes the data for the above three architectures.
Note that RF FE IL in the table means the insertion loss including line losses
and duplexer and switch losses or a combiner or diplexer losses.
Table 6.5.2.1.3.1.2.4-1: Comparison of three architectures for NTC
+-------+-------+-------+-------+-------+-------+-------+-------+-------+ | | Freq | (1) | (2) | (3) | (2 | (3 | (3 | | | | uency | | | | )-(1) | )-(1) | )-(2) | | | | [ | No | CA\ | CA\ | | | | | | | MHz] | n_CA | _type | _type | \ | \ | \ | | | | | | w/o | w dip | [dB] | [dB] | [dB] | | | | | \ | dip | | | | | | | | | [dB] | | \ | | | | | | | | | \ | [dB] | | | | | | | | | [dB] | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+-------+ | B1 | TX RF | 1920 | 2.32 | 2.92 | 3.10 | 0.60 | 0.78 | 0.18 | | | FE | − | | | | | | | | | I.L. | 1980 | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+-------+ | | RX RF | 2110 | 2.53 | 3.10 | 3.26 | 0.57 | 0.73 | 0.16 | | | FE | − | | | | | | | | | I.L. | 2170 | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+-------+ | B21 | TX RF | 1 | 2.13 | 2.68 | 3.01 | 0.55 | 0.88 | 0.33 | | | FE | 447.9 | | | | | | | | | I.L. | − | | | | | | | | | | 1 | | | | | | | | | | 462.9 | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+-------+ | | RX RF | 1 | 2.11 | 2.65 | 2.96 | 0.54 | 0.85 | 0.31 | | | FE | 495.9 | | | | | | | | | I.L. | − | | | | | | | | | | 1 | | | | | | | | | | 510.9 | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+-------+ | B | B1 TX | 1920 | 57.10 | 58.11 | 53.01 | − | − | −5.10 | | 1-B21 | - B21 | − | | | | | | | | | RX | 1980 | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+-------+ | | B1 TX | 1 | 69.70 | 42.56 | 61.58 | − | − | 19.01 | | | - B21 | 495.9 | | | | | | | | | RX | − | | | | | | | | | | 1 | | | | | | | | | | 510.9 | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+-------+ | | B21 | 1 | 79.70 | 55.45 | 63.05 | − | − | 7.60 | | | TX - | 447.9 | | | | | | | | | B1 RX | − | | | | | | | | | | 1 | | | | | | | | | | 462.9 | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+-------+ | | B21 | 2110 | 65.30 | 54.38 | 55.24 | − | − | 0.86 | | | TX - | − | | | | | | | | | B1 RX | 2170 | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+-------+ | NOTE: | | | | | | | | | | (1) | | | | | | | | | | Based | | | | | | | | | | on 2 | | | | | | | | | | sam | | | | | | | | | | ples. | | | | | | | | | | (2) | | | | | | | | | | Based | | | | | | | | | | on 8 | | | | | | | | | | sam | | | | | | | | | | ples. | | | | | | | | | | (3) | | | | | | | | | | Based | | | | | | | | | | on 8 | | | | | | | | | | sam | | | | | | | | | | ples. | | | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+-------+
Table 6.5.2.1.3.1.2.4-2: Comparison of three architectures for ETC (-30～+85
degrees)
+-------+-------+-------+-------+-------+-------+-------+-------+------+ | | Freq | (1) | (2) | (3) | (2 | (3 | (3 | | | | uency | | | | )-(1) | )-(1) | )-(2) | | | | [ | No | CA\ | CA\ | | | | | | | MHz] | n_CA | _type | _type | \ | \ | \ | | | | | | w/o | w dip | [dB] | [dB] | [dB] | | | | | \ | dip | | | | | | | | | [dB] | | \ | | | | | | | | | \ | [dB] | | | | | | | | (W | [dB] | | | | | | | | | orst) | | (W | | | | | | | | | (W | orst) | | | | | | | | | orst) | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+------+ | B1 | TX RF | 1920 | 2.81 | 3.30 | 3.70 | 0.49 | 0.89 | 0.40 | | | FE | − | | | | | | | | | I.L. | 1980 | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+------+ | | RX RF | 2110 | 3.03 | 3.55 | 3.93 | 0.52 | 0.90 | 0.38 | | | FE | − | | | | | | | | | I.L. | 2170 | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+------+ | B21 | TX RF | 1 | 2.38 | 2.97 | 3.28 | 0.59 | 0.90 | 0.31 | | | FE | 447.9 | | | | | | | | | I.L. | − | | | | | | | | | | 1 | | | | | | | | | | 462.9 | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+------+ | | RX RF | 1 | 2.25 | 2.87 | 3.23 | 0.62 | 0.98 | 0.36 | | | FE | 495.9 | | | | | | | | | I.L. | − | | | | | | | | | | 1 | | | | | | | | | | 510.9 | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+------+ | NOTE: | | | | | | | | | | (1) | | | | | | | | | | Based | | | | | | | | | | on 2 | | | | | | | | | | sam | | | | | | | | | | ples. | | | | | | | | | | (2) | | | | | | | | | | Based | | | | | | | | | | on 5 | | | | | | | | | | sam | | | | | | | | | | ples. | | | | | | | | | | (3) | | | | | | | | | | Based | | | | | | | | | | on 5 | | | | | | | | | | sam | | | | | | | | | | ples. | | | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+------+
From the above table, the followings can be observed.
\- In the worst case, the total RF FE Tx IL post PA is 3.7 dB for the CA
architecture with diplexer solution (3).
\- On the other hand, for the CA architecture without diplexer solution (2),
RF FE Tx IL post PA is 3.23 dB.
\- The additional insertion loss of this CA architecture (2) is quite smaller
than that of the CA architecture with diplexer (3).
###### 6.5.2.1.3.2 Summary
The average insertion loss of the data presented in the above sub-clause is
summarized in table 6.5.2.1.3.2-1.
Table 6.5.2.1.3.2-1: Additional insertion loss of diplexer and quadplexer
(ETC)
+----+---------+--------+--------+--------+---------+-----+ | | Vendors | | | | | | +----+---------+--------+--------+--------+---------+-----+ | | 1 | 2 | 3 | 4 | Average | | +----+---------+--------+--------+--------+---------+-----+ | | Max | Max | Max | Max | [dB] | | | | | | | | | | | | [dB] | [dB] | [dB] | [dB] | | | +----+---------+--------+--------+--------+---------+-----+ | IL | B21 Tx | 0.43 | 0.64 | 0.30 | 0.59 | 0.5 | +----+---------+--------+--------+--------+---------+-----+ | | B21 Rx | 0.45 | 0.64 | 0.30 | 0.62 | 0.5 | +----+---------+--------+--------+--------+---------+-----+ | | B1 Tx | 0.65 | 0.76 | 0.50 | 0.49 | 0.6 | +----+---------+--------+--------+--------+---------+-----+ | | B1 Rx | 0.5 | 0.76 | 0.50 | 0.52 | 0.6 | +----+---------+--------+--------+--------+---------+-----+
#