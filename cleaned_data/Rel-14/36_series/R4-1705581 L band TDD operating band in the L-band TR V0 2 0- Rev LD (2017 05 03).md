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
The present document is a technical report for the work item of introduction
of TDD operating band in the L-band for LTE, which was approved at TSG RAN#74.
The objective of this work item is to specify technical requirements for
deploying LTE TDD operation in the L-band.
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
[2] 3GPP TR 30.007: "Guideline on WI/SI for new Operating Bands"
# 3 Definitions, symbols and abbreviations
Delete from the above heading those words which are not applicable.
Clause numbering depends on applicability and should be renumbered
accordingly.
## 3.1 Definitions
For the purposes of the present document, the terms and definitions given in
TR 21.905 [x] and the following apply. A term defined in the present document
takes precedence over the definition of the same term, if any, in TR 21.905
[x].
Definition format (Normal)
**\ :** \.
**example:** text used to clarify abstract rules by applying them literally.
## 3.2 Symbols
For the purposes of the present document, the following symbols apply:
Symbol format (EW)
\ \
## 3.3 Abbreviations
For the purposes of the present document, the abbreviations given in TR 21.905
[x] and the following apply. An abbreviation defined in the present document
takes precedence over the definition of the same abbreviation, if any, in TR
21.905 [x].
Abbreviation format (EW)
\ \
# 4 Background
## 4.1 Work item objective
**The objective of this work item** **is** **the following:**
  * Study the feasible channelling arrangement(s) of L-band (1427 -- 1518 MHz) considering the above ITU TDD options and relevant protection requirements of EESS below 1 427 MHz and MSS above 1518 MHz, considering the results of relevant ongoing ITU-R studies, including:
    * TDD: 90 MHz (1427 -- 1517 MHz), considering 1 MHz GB with MSS at the upper edge,
    * Note: the upper edge refinement is based on results of ongoing compatibility studies with MSS. For example option of 88 MHz (1427 -- 1515 MHz) considers 3 MHz GB with MSS at the upper edge.
```{=html}
``` \- Specify RF requirements for the feasible plan, band numbering and core
requirements, as necessary.
  * Support of 3, 5, 10, 15 and 20 MHz channel bandwidths
# 5 Band plan allocation and regulatory background
## 5.1 Current regulatory background
## According to international regulation, WRC-15 and previous WRCs (ITU-R)
have allocated the 1427-1518MHz band to mobile service and the WRC15 has
indentified the 1427-1518MHz band for IMT in a large majority of countries
through the world .
## In addition and before the WRC15, CEPT has also allocated a part of the
Lband (1452-1492MHz) to MFCN (Mobile/Fixed Communications Networks) the
03-07-2015. MFCN bands are designed for commercial use as the LTE or the 5G-NR
but not limited to these standards.
## 5.2 TDD band plan
Based on the work item objective, the possible band plan is:
**1427 MHz** |  |  |  |  |  |  |  |  |  |  |  |  | **1517 MHz** |  |  |  |  |   
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
1427 - 1432 | 1432 - 1437 | 1437 - 1442 | 1442 - 1447 | 1447 - 1452 | 1452 - 1457 | 1457 - 1462 | 1462 - 1467 | 1467 - 1472 | 1472 - 1477 | 1477 - 1482 | 1482 - 1487 | 1487 - 1492 | 1492 - 1497 | 1497 - 1502 | 1502 - 1507 | 1507 - 1512 | 1512 - 1517 | 1517 - 1518  
**TDD** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   
**90 MHz (18 blocks of 5 MHz)** | Guard band |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   
Table 5-1: Possible frequency band channelization in the 1427-1518MHz band
## 5.3 In-band services
{width="6.542361111111111in" height="2.0305555555555554in"}
Figure 5-1: 1427 - 1518 MHz spectrum allocation
There are several allocations in the LBand (1427-1518MHz) and in adjacent
frequency bands:
  * EESS (Earth Exploration Satellite Service / adjacent to the new IMT band),
```{=html}
``` \- Radio Astronomy (adjacent to the new IMT band),
  * Fixed Service (FS) (in the new IMT band)
  * Aeronautical service (in the new IMT band)
  * Mobile service (in the new IMT band)
  * Terrestrial broadcasting service (in the new IMT band)
  * Satellite broadcasting service (in the new IMT band)
  * Mobile satellite Service (adjacent to the new IMT band),
For all cases \"in IMT band\", the best option is to move to new frequency
band the incumbent services (e.g. for fixed service, CEPT has study the
possibility to move the narrow band fixed service in a new frequency band as
describe in the ECC Report 219), or, to find another technical solution (e.g.
use fiber). If there is no possible to find a solution to the incumbent users,
at national level or between countries, it is necessary to develop some
specific agreements between incumbent users and IMT systems.
Thus, for the cases \"in IMT band\", there is no direct and immediate need to
adapt the standard to the regulation.
For the cases \"adjacent IMT band\", there will be, maybe, the necessity to
adapt the new standard to guaranty the compatibility between IMT and the
incumbent users in adjacent bands. There are 3 incumbent users in adjacent
frequency bands:
  * Below 1427MHz => For EESS the maximum OOB has already been defined during the last WRC15. Thus, it is necessary to adapt the standardization to these protections levels,
  * Below 1427MHz => For Radio Astronomy and taking into account the low deployment of this service, the best way is to have some specific agreements. The Agreement can be study at national level or if a Radio Astronomy site is near a borderline, between administrations.
  * Above 1518MHz => For Mobile Satellite Service, CEPT has already study the compatibility between MFCN for the base station down link (LTE,...) and MSS. The standard shall comply to the CEPT requests. For the compatibility between IMT uplink terminal and MSS, this report will propose some compatibility studies.
## Thus, there are two services (EESS & MSS) which shall be studied by 3GPP
RAN4 because these two systems will get the protection by the standardization.
The other incumbent services will be protected by relevant regulation
framework at national level or between administrations.
## 5.4 **Earth exploration-satellite service (EESS) (passive) compatibility**
At the last WRC15, some protection levels have defined for the IMT base
station and for the IMT terminal. The RESOLUTION 750 (REV.WRC-15) provides the
protection levels. In the table 5.2-1 below summaries the different protection
levels for the EESS in the 1400-1427MHz band:
* * *
EESS (passive) band Active service band Active service Limits of unwanted
emission power from active service stations in a specified bandwidth within
the EESS (passive) band (1)
1 400-1 427 MHz 1 427-1 452 MHz Mobile −72 dBW in the 27 MHz of the EESS
(passive) band for IMT base stations\ −62 dBW in the 27 MHz of the EESS
(passive) band for IMT mobile stations (2, 3)
* * *
1 The unwanted emission power level is to be understood here as the level
measured at the antenna port.
2 This limit does not apply to mobile stations in the IMT systems for which
the notification information has been received by the Radiocommunication
Bureau by 28 November 2015. For those systems, −60 dBW/27 MHz applies as the
recommended value.
3 The unwanted emission power level is to be understood here as the level
measured with the mobile station transmitting at an average output power of 15
dBm.
Table 5.2-1: Limits of unwanted emission power in the 1400-1427MHz band from
mobile service in the 1427-1452MHz
Thus, it is proposed to study the RF requirements to comply to the regulatory
requests.
## 5.5 Mobile Satellite Service compatibility at 1518MHz
The CEPT has already study the protection levels need between IMT and MSS (see
ECC Report 263). The key conclusions about this protection are cited as below:
> _"Based on the final results of its compatibility studies, it is concluded
> that:_
  * _the minimum in-band blocking characteristic for land mobile earth > stations receivers from a 5 MHz broadband signal interferer (LTE) > operating below 1518 MHz shall be −30dBm above 1520 MHz_ _^1^__,_
  * _the base station unwanted emission limits e.i.r.p. for a broadband > signal interferer (LTE) operating below 1518 MHz shall be > −30dBm/MHz above 1520 MHz. This figure is 10 dB more stringent > than ECC Decision (13)03 due to a different service in the > adjacent band._
> _It is noted that the IMT block ends at 1517 MHz"_
Based on this request, 3GPP RAN 4 needs to study the feasibility of base
station to comply to the CEPT requests.
# 6 List of band specific issues for introduction of TDD operating band in the
L-band for LTE
\- General issues
\- Frequency band arrangement
\- E-UTRA issues
\- UE transmitter requirements
\- UE receiver requirements
\- BS Transmitter requirements
\- BS Receiver requirements
# 7 General issues
\
# 8 Study of E-UTRA specific issues
\
## 8.1 For BS (unwanted regional emission level) in the band(s) 1492 --
[1517/1518] MHz
The regulatory requirements for base stations operating within 1492 --
[1517/1518] MHz are specified by ECC report (for SDL) in terms of EIRP, which
corresponds to the unwanted emission limit of -30dB/MHz in 1MHz MSS (Mobile
Satellite Service) band above 1520MHz. The same requirements may be considered
for FDD and TDD BS in other regions. When that is required, manufacturer
declaration of unwanted emissions may be used to verify the compliance with
the regional requirements.
Table XXXX : Declared emission to 1492-1518 MHz
* * *
Filter centre frequency, F~filter~ Declared emission level [dBm] Measurement
bandwidth 1520.5 MHz ≤ F~filter~ ≤ 1558.5 MHz P~EM,x~ 1 MHz
* * *
_NOTE: The regional requirement is defined in terms of EIRP, which is
dependent on both the BS emissions at the antenna connector and the deployment
(including antenna gain and feeder loss). The requirement defined above
provides the characteristics of the base station needed to verify compliance
with the regional requirement. The assessment of the EIRP level is described
in Annex H of TS36.104_.
## 8.2 For BTS in the band(s) [1427] -- 1452 MHz (low edge of the frequency
range will be aligned on the low edge of the SDL band plan)
Additional spurious emission requirements for the base station are specified
in 36.104 sub-clause 6.6.3.3. These requirements may apply in certain regions
for the protection of other systems operating inside or near each supported
E-UTRA BS downlink operating band. To capture the regulatory requirement for
the base station operating in the frequency range [1427] -- 1452 MHz (low edge
of the frequency range will be aligned on the low edge of the SDL band plan)
for the protection of EESS (passive) operating in the range 1400 -- 1427 MHz,
the following table is proposed to be added to 36.104.
The following requirements may apply in regions. For E-UTRA BS operating in
Band XX [and YY] within [1427] -- 1452 MHz (low edge of the frequency range
will be aligned on the low edge of the SDL band plan), emissions shall not
exceed the maximum levels specified in Tables 6.6.3.3-x.
It is observed that for base stations operating on channels located at the
lower frequency range of this band, the maximum output power may be reduced
since there is no guard band at 1427 MHz to allow for filter transition.
Table XXXXX (Table 6.6.3.3-x in 36.104): Additional operating band unwanted
emission limits for E-UTRA band XX [and YY] within [1427] \-- 1452 MHz
* * *
Operating Band Filter center frequency, F~filter~ Maximum Level [dBW]
Measurement bandwidth XX F~filter~ = 1413.5 MHz -72 27 MHz
* * *
8.3 For UE in the band(s) 1492 -- [1517/1518] MHz to protect MSS
[To protect MSS, need further studies and to take a decision about the level
to protect MSS at the next RAN4 meeting. Technical solution to be consistent
to the MSS protection level should be also proposed at the next RAN4 meeting.]
## 8.4 For UE in the band(s) [1427] -- 1452 MHz (low edge of the frequency
range will be aligned on the low edge of the SDL band plan) to protect EESS
Additional spurious emission requirements for the user equipment are specified
in 36.101. These requirements may apply in regions for the protection of other
systems. To capture the regulatory requirement for the user equipment
operating in the frequency range [1427]-- 1452 MHz (low edge of the frequency
range will be aligned on the low edge of the SDL band plan) for the protection
of EESS (passive) operating in the range 1400 -- 1427 MHz, the following table
is proposed to be added to 36.101.
For UE operating in Band XX within [1427]-- 1452 MHz (low edge of the
frequency range will be aligned on the low edge of the SDL band plan),
emissions shall not exceed the maximum levels specified in Tables XXX-x.
It is observed that for user equipment operating on channels located at the
lower frequency range of this band, the maximum output power may be reduced
since there is no guard band at 1427 MHz to allow for filter transition.
Table XXXXX (Table XXX-x in 36.101): Additional operating band unwanted
emission limits for E-UTRA band XX within [1427] -- 1452 MHz
* * *
Operating Band Filter center frequency, F~filter~ Maximum Level [dBW]
Measurement bandwidth XX F~filter~ = 1413.5 MHz -62 27 MHz
* * *
# 9 Study of MSR specific issues
\
# 10 Channel numbering for E-UTRA, MSR
\
# 11 Required changes to E-UTRA and MSR specifications
The required changes to the 3GPP specifications for the new band are
summarised in a Table 11-1.
Table 11-1: Overview of 3GPP specifications with required changes
* * *
3GPP specification Clause in TR 30.007 where the required changes are given
Clause in the present document identifying additional changes TS 36.101
8.2.1.1  
TS 36.104 8.2.1.2  
TS 36.106 8.2.1.3  
TS 36.113 8.2.1.4  
TS 36.124 8.2.1.5  
TS 36.133 8.2.1.6  
TS 36.141 8.2.1.7  
TS 36.143 8.2.1.8  
TS 36.307 8.2.1.9  
TS 25.101 8.2.2.1  
TS 25.104 8.2.2.3  
TS 25.106 8.2.2.5  
TS 25.123 8.2.2.7  
TS 25.133 8.2.2.9  
TS 25.141 8.2.2.10  
TS 25.143 8.2.2.12  
TS 25.461 8.2.2.15  
TS 25.466 8.2.2.16  
TS 37.104 8.2.3.1  
TS 37.113 8.2.2.2  
TS 37.141 8.2.2.3
* * *
#