# Foreword
This Technical Specification has been produced by the 3GPP.
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
The purpose of this TS is to describe the service access procedures as
presented to the user.
Definitions and procedures are provided in this TS for international roaming,
national roaming and regionally provided service. These are mandatory in
relation to the technical realization of the Mobile Station (UE).
## 1.1 References
The following documents contain provisions which, through reference in this
text, constitute provisions of the present document.
  * References are either specific (identified by date of publication, > edition number, version number, etc.) or non‑specific.
  * For a specific reference, subsequent revisions do not apply.
  * For a non-specific reference, the latest version applies. In the > case of a reference to a 3GPP document (including a GSM document), > a non-specific reference implicitly refers to the latest version > of that document _in the same Release as the present document_.
[1] Void
[2] 3GPP TR 21.905: \"Vocabulary for 3GPP Specifications\".
[3] 3GPP TS 23.122: \"Non Access Stratum functions related to Mobile Station
(MS) in idle mode\".
[4] ITU-T Recommendation Q.1001: \"General aspects of Public Land Mobile
Networks\".
[5] 3GPP TS 22.043: \"Support of Localised Service Area (SoLSA). Stage 1\".
[6] 3GPP TS 22.234: \"Requirements on 3GPP system to wireless local area
network (WLAN) interworking\".
[7] 3GPP TS 22.101: \"Service aspects; Service principles\".
[8] 3GPP TS 22.278: \"Service requirements for the Evolved Packet System
(EPS)\".
[9] Void
[10] 3GPP TS 25.304: \"User Equipment (UE) procedures in idle mode and
procedures for cell reselection in connected mode\".
[11] Void
[12] Void
[13] 3GPP TS 36.331: \"E-UTRA Radio Resource Control (RRC)\".
[14] 3GPP TS 22.220: \"Service requirements for Home NodeBs and Home
eNodeBs\".
[15] 3GPP2 C.S0004-A v6.0: \"Signaling Link Access Control (LAC) Standard for
cdma2000 Spread Spectrum Systems -- Addendum 2\"
[16] 3GPP TS 22.153: \"Multimedia priority service\".
[17] 3GPP TS 36.306: \"Evolved Universal Terrestrial Radio Access (E-UTRA);
User Equipment (UE) radio access capabilities\"
[18] 3GPP TS 43.064: \" General Packet Radio Service (GPRS); Overall
description of the GPRS radio interface; Stage 2\"
[19] ITU-T Recommendation E.212: \"The international identification plan for
public networks and subscriptions\"
[20] 3GPP TS 26.114: \" IP Multimedia Subsystem (IMS); Multimedia Telephony;
Media handling and interaction\".
## 1.2 Definitions and abbreviations
### 1.2.1 Definitions
In addition to those below, abbreviations used in this 3GPP TS are listed in
3GPP TR 21.905 [2].
**3GPP PS Data Off:** A feature which when configured by the HPLMN and
activated by the user prevents transport via PDN connections in 3GPP access of
all IP packets except IP packets required by 3GPP PS Data Off Exempt Services.
**3GPP PS Data Off Exempt Services:** A set of operator services that are
allowed even if the 3GPP PS Data Off feature has been activated in the UE by
the user.
**Disaster Condition:** This is the condition that a government decides
whether applicable or not based on, e.g. a natural disaster or a man-made
disaster. When this condition applies service interruptions and failures will
be mitigated.
**PLMN:** A Public Land Mobile Network (PLMN) is a network established and
operated by an Administration or RPOA for the specific purpose of providing
land mobile communication services to the public. It provides communication
possibilities for mobile users. For communications between mobile and fixed
users, interworking with a fixed network is necessary.
A PLMN may provide service in one, or a combination, of frequency bands.
As a rule, a PLMN is limited by the borders of a country. Depending on
national regulations there may be more than one PLMN per country.
A relationship exists between each subscriber and his home PLMN (HPLMN). If
communications are handled over another PLMN, this PLMN is referred to as the
visited PLMN (VPLMN).
**PLMN Area:** The PLMN area is the geographical area in which a PLMN provides
communication services according to the specifications to mobile users. In the
PLMN area, the mobile user can set up calls to a user of a terminating
network. The terminating network may be a fixed network, the same PLMN,
another PLMN or other types of PLMN.
Terminating network users can also set up calls to the PLMN.
The PLMN area is allocated to a PLMN. It is determined by the service and
network provider in accordance with any provisions laid down under national
law. In general, the PLMN area is restricted to one country. It can also be
determined differently, depending on the different telecommunication services,
or type of UE.
If there are several PLMNs in one country, their PLMN areas may overlap. In
border areas, the PLMN areas of different countries may overlap.
Administrations will have to take precautions to ensure that cross border
coverage is minimized in adjacent countries unless otherwise agreed.
NOTE 1: ITU-T Recommendation Q.1001 [4] does not contain a definition of the
PLMN area.
**System Area:** The System Area is defined as the group of PLMN areas
accessible by UEs.
Interworking of several PLMNs and interworking between PLMNs and fixed
network(s) permit public land mobile communication services at international
level.
NOTE 2: The System Area according to [4] Recommendation Q.1001 corresponds to
the System Area.
**Service Area:** The Service Area is defined in the same way as the Service
Area according to ITU-T Recommendation Q.1001 [4]. In contrast to the PLMN
area it is not based on the coverage of a PLMN. Instead it is based on the
area in which a fixed network user can call a mobile user without knowing his
location. The Service Area can therefore change when the signalling system is
being extended, for example.
**Shared MCC:** MCC assigned by ITU-T as shared MCC according to ITU-T E.212
[19], except within this specification for PLMN selection purposes the MCC of
value 999 is not considered a shared MCC.
**Regionally Provided Service:** Regionally Provided Service is defined as a
service entitlement to only certain geographical part(s) of a PLMN, as
controlled by the network operator.
**Localised Service Area (LSA):** The localised service area concept shall
give the operator a basis to offer subscribers different services (e.g.
tariffs or access rights) depending on the location of the subscriber. An LSA
consists of a cell or a number of cells within a PLMN. (3GPP TS 22.043 [5]).
**Tracking Area:** E-UTRAN utilises Tracking Areas (TA) for UE access control,
location registration, paging and mobility management. The TA is independent
of Location Areas (LA) and Routing Areas (RA). A TA comprises one or more
E-UTRA cells Service requirements for E-UTRAN are specified in 3GPP TS 22.278
[8].
### 1.2.2 Abbreviations
For the purposes of the present document, the abbreviations given in 3GPP TR
21.905 [2] and the following apply. An abbreviation defined in the present
document takes precedence over the definition of the same abbreviation, if
any, in 3GPP TR 21.905 [2].
ACDC Application specific Congestion control for Data Communication
EAB Extended Access Barring
SSAC Service Specific Access Control
# 2 Roaming
## 2.1 General requirements
A UE with a valid IMSI may roam and access service in the area authorized by
the entitlement of the subscription.
If a communication has been established, the UE will in principle not suffer
an interruption within the PLMN area (provided the entitlement of the
subscription allows it). Exceptions are possible if no network resources or
radio coverage are available locally.
However, if the UE leaves the PLMN area, an established communication may
terminate. If the user then wants to continue, another network providing
service has to be selected and a new communication has to be established (see
clause 3).
Subject to roaming agreements, a visited network shall be able to prevent
incoming roamers from using a particular radio access technology (e.g. when
the home network has not implemented this radio access technology).
## 2.2 International roaming
International roaming is a service whereby a UE of a given PLMN is able to
obtain service from a PLMN of another country.
The availability of International Roaming is subject to inter-PLMN agreements.
## 2.3 National roaming
National Roaming is a service whereby a UE of a given PLMN is able to obtain
service from another PLMN of the same country, anywhere, or on a regional
basis.
The availability of National Roaming depends on the home PLMN of the
requesting UE and the visited PLMN; it does not depend on subscription
arrangements.
## 2.4 Roaming in shared networks
The following requirements are applicable to GERAN, UTRAN, E-UTRAN and NG-RAN
sharing scenarios:
\- Mechanisms shall be specified to enable flexible allocation of visiting
roamers among core network operators that have roaming agreements with the
same roaming partners. The core network operators shall be able to pre-define
their relative share of visiting roamers and distribute the visiting roamers
that apply automatic network selection to different core networks connected to
the radio access network accordingly.
\- When network sharing exists between different operators and a user roams
into the shared network it shall be possible for that user to register with a
core network operator (among the network sharing partners) that the user's
home operator has a roaming agreement with, even if the operator is not
operating a radio access network in that area.
\- The selection of a core network operator among those connected to the
shared radio access network can either be manual (i.e. performed by the user
after obtaining a list of available core network operators) or automatic (i.e.
performed by the UE according to user and operator preferred settings). For
further information see clause 3.2.
# 3 Provisions for providing continuity of service
## 3.1 Location registration
PLMNs shall provide a location registration function with the main purpose of
providing continuity of service to UEs over the whole system area. The
location registration function shall be such as to allow:
\- Fixed subscribers to call a UE by only using the directory number of the UE
irrespective of where the UE is located in the system area at the time of the
call.
\- UEs to access the system irrespective of the location of the UE.
\- UEs to identify when a change in location area has taken place in order to
initiate automatic location updating procedures.
## 3.2 Network selection
### 3.2.1 General
The UE shall support both manual and automatic network selection mechanisms
(modes). The UE shall select the last mode used, as the default mode, at every
switch-on.
As an optional feature of the ME, the user shall be able to set a preference
in the ME for the mode that shall be used at switch on. If set, then the ME
shall select this preference rather than the default mode.
NOTE: By defaulting to the last mode used, e.g. manual network selection, the
undesired automatic selection of an adjacent PLMN instead of the desired HPLMN
in border areas, can be avoided at switch-on.
The user shall be given the opportunity to change mode at any time.
Except as defined below, the MMI shall be at the discretion of the UE
manufacturer.
The UE shall contain display functions by which Available PLMNs and the
Selected PLMN can be indicated.
In order not to confuse the user, the same definitions of PLMN names shall be
applied consistently both in registered mode and in the list presented to the
user when in manual mode.
In shared networks a radio access network can be part of more than one PLMN.
This shall be transparent to the user, i.e. the UE shall be able to indicate
those PLMNs to the user, and the UE shall support network selection among
those PLMNs, as in non-shared networks.
### 3.2.2 Procedures
#### 3.2.2.1 General
In the following procedures the UE selects and attempts registration on PLMNs.
In this TS, the term \"PLMN Selection\" defines a UE based procedure, whereby
candidate PLMNs are chosen, one at a time, for attempted registration.
A User Controlled PLMN Selector data field exists on the USIM to allow the
user to indicate a preference for network selection. It shall be possible for
the user to update the User Controlled PLMN Selector data field, but it shall
not be possible to update this data field over the radio interface, e.g. using
SIM Application Toolkit.
It shall be possible to have an Operator Controlled PLMN Selector list and a
User Controlled PLMN Selector list stored on the SIM/USIM card. Both PLMN
Selector lists may contain a list of preferred PLMNs in priority order. It
shall be possible to have an associated Access Technology identifier e.g., NG-
RAN, satellite NG-RAN, E-UTRAN (WB-S1 mode), E-UTRAN (NB-S1 mode), UTRAN,
GERAN or GERAN EC-GSM-IoT associated with each entry in the PLMN Selector
lists.
For UEs supporting any, or a combination, of NB-IoT, GERAN EC-GSM-IoT [18] and
Category M1 or M2 of E-UTRA [17], the 5G system shall support a mechanism to
have an Operator controlled signal threshold per access technology on the USIM
to be used for network selection. The signal threshold is specific for a
certain Access Technology and shall apply to all PLMNs with the corresponding
access technology combinations.
NOTE 1: The use of the Operator controlled signal threshold per access
technology is intended for IoT stationary devices, without user interaction.
NOTE 2: The allowed range of the Operator controlled signal threshold per
access technology is between the cell selection criterion and the high quality
signal as defined in TS 23.122 [3].
The UE shall utilise all the information stored in the USIM related to network
selection, e.g. HPLMN, Operator controlled PLMN Selector list, User Controlled
PLMN Selector list, Forbidden PLMN list, Operator controlled signal threshold.
NOTE 3: A PLMN in a Selector list, including HPLMN, may have multiple
occurrences, with different access technology identifiers.
The UE shall ignore those PLMN + access technology entries in the User
Controlled PLMN selector and Operator Controlled PLMN selector lists where the
associated Access Technology is not supported by the UE. In the case that
there are multiple associated Access Technology identifiers in an entry the UE
shall not ignore the entry if it includes any associated Access Technology
that is supported by the UE.
It shall be possible to handle cases where one network operator accepts access
from access networks with different network IDs. It shall also be possible to
indicate to the UE that a group of PLMNs are equivalent to the registered PLMN
regarding PLMN selection, cell selection/re-selection and handover.
It shall be possible for the home network operator to identify alternative
Network IDs as the HPLMN. It shall be possible for the home network operator
to store in the USIM an indication to the UE that a group of PLMNs are treated
as the HPLMN regarding PLMN selection. Any PLMN to be declared as an
equivalent to the HPLMN shall be present within the EHPLMN list and is called
an EHPLMN. The EHPLMN list replaces the HPLMN derived from the IMSI. When the
EHPLMN list is present, any PLMN in this list shall be treated as the HPLMN in
all the network and cell selection procedures.
If registration on a PLMN is successful, the UE shall indicate this PLMN (the
\"registered PLMN\") and be capable of making and receiving calls on it. The
identity of the registered PLMN shall be stored on the SIM/USIM. However, if
registration is unsuccessful, the UE shall ensure that there is no registered
PLMN stored in the SIM/USIM.
If a registration is unsuccessful because the IMSI is unknown in the home
network, or the UE is illegal, then the UE shall not allow any further
registration attempts on any network, until the UE is next powered‑up or a
SIM/USIM is inserted.
If the registration is unsuccessful due to the lack to service entitlement,
specific behaviour by the UE may be required, see clause 3.2.2.4.
To avoid unnecessary registration attempts, lists of forbidden PLMNs, TAs and
LAs are maintained in the UE, see clause 3.2.2.4 and 3GPP TS 23.122 [3].
Registration attempts shall not be made by UEs without a SIM/USIM inserted.
An UE/ME which has not successfully registered shall nevertheless be able to
make emergency call attempts on an available PLMN (which supports the
emergency call teleservice), without the need for the user to select a PLMN.
An available PLMN is determined by radio characteristics (3GPP TS 23.122 [3]).
#### 3.2.2.2 At switch-on or recovery from lack of coverage
If the Operator controlled signal threshold per access technology is set on
the USIM, it shall be used for the selection of the last registered PLMN
(and/or EHPLMN/HPLMN) and for the automatic mode network selection steps
described in this clause. In particular, if the Operator controlled signal
threshold per access technology is set on the USIM the UE shall only select a
network if
\- the network selection conditions as described below are met and
\- the received signal quality of the candidate PLMN/access technology
combination is equal to or higher than the Operator controlled signal
threshold per access technology.
At switch on, when in coverage of the last registered PLMN as stored in the
SIM/USIM, the UE will attach to that network.
As an option, in automatic selection mode, when no EHPLMN list is present, the
UE may select the HPLMN. When the EHPLMN list is present, the UE may select
the highest priority EHPLMN among the available EHPLMNs. The operator shall be
able to control the UE behaviour by USIM configuration.
As an option, if the UE is in manual network selection mode at switch-on
\- if the last registered PLMN is unavailable and no equivalent PLMN is
available,
\- and the UE finds it is in coverage of either the HPLMN or an EHPLMN
then the UE should register on the corresponding HPLMN or EHPLMN. The UE
remains in manual mode.
If the UE returns to coverage of the PLMN on which it is already registered
(as indicated by the registered PLMN stored in the SIM/USIM), the UE shall
perform a location update to a new location area if necessary. As an
alternative option to this, if the UE is in automatic network selection mode
and it finds coverage of the HPLMN or any EHPLMN, the UE may register on the
HPLMN (if the EHPLMN list is not present) or the highest priority EHPLMN of
the available EHPLMNs (if the EHPLMN list is present) and not return to the
last registered PLMN. If the EHPLMN list is present and not empty, it shall be
used. The operator shall be able to control by USIM configuration whether an
UE that supports this option shall follow this alternative behaviour.
NOTE: At switch-on and at recovery from lack of coverage, a UE in automatic
network selection mode can attempt registration once the RPLMN or, if the
above option is applicable, the HPLMN or EHPLMN is found on an access
technology.
The default behaviour for a UE is to select the last registered PLMN.
If there is no registered PLMN stored in the SIM/USIM, or if this PLMN is
unavailable and no equivalent PLMN is available, or the attempted registration
fails, the UE shall follow one of the following procedures for network
selection:
**A) Automatic network selection mode**
The UE shall select and attempt registration on other PLMNs, if available and
allowable, if the location area is not in the list of \"forbidden LAs for
roaming\" and the tracking area is not in the list of \"forbidden TAs for
roaming\" (see 3GPP TS 23.122 [3]), in the following order:
> i) An EHPLMN if the EHPLMN list is present or the HPLMN (derived from the
> IMSI) if the EHPLMN list is not present for preferred access technologies in
> the order specified. In the case that there are multiple EHPLMNs present
> then the highest priority EHPLMN shall be selected. It shall be possible to
> configure a voice capable UE so that it shall not attempt registration on a
> PLMN if all cells identified as belonging to the PLMN do not support the
> corresponding voice service;
>
> ii) each entry in the \"User Controlled PLMN Selector with Access
> Technology\" data field in the SIM/USIM (in priority order). It shall be
> possible to configure a voice capable UE so that it shall not attempt
> registration on a PLMN if all cells identified as belonging to the PLMN do
> not support the corresponding voice service;
>
> iii) each entry in the \"Operator Controlled PLMN Selector with Access
> Technology\" data field in the SIM/USIM (in priority order). It shall be
> possible to configure a voice capable UE so that it shall not attempt
> registration on a PLMN if all cells identified as belonging to the PLMN do
> not support the corresponding voice service;
>
> iv) other PLMN/access technology combinations with sufficient received
> signal quality (see 3GPP TS 23.122 [3]) in random order. It shall be
> possible to configure a voice capable UE so that it shall not attempt
> registration on a PLMN if all cells identified as belonging to the PLMN do
> not support the corresponding voice service;
>
> v) all other PLMN/access technology combinations in order of decreasing
> signal quality. It shall be possible to configure a voice capable UE so that
> it shall not attempt registration on a PLMN if all cells identified as
> belonging to the PLMN do not support the corresponding voice service.
In the case of a UE operating in UE operation mode A or B, an allowable PLMN
is one which is not in the \"Forbidden PLMN\" data field in the SIM/USIM. This
data field may be extended in the ME memory (see clause 3.2.2.4). In the case
of a UE operating in UE operation mode C, an allowable PLMN is one which is
not in the \"Forbidden PLMN\" data field in the SIM/USIM or in the list of
\"forbidden PLMNs for GPRS service\" in the ME.
If the UE uses the Operator controlled signal threshold per access technology
and no candidate PLMN/access technology combination fulfils the Operator
controlled signal threshold criteria, the UE shall repeat the network
selection without using the Operator controlled signal threshold per access
technology.
If there is no available PLMN except for PLMNs in the \"Forbidden PLMN\" data
field in the SIM/USIM, and the available PLMNs indicate that Disaster
Condition applies, this PLMN shall be considered allowable for registration to
the UE while the Disaster Condition is applicable.
If successful registration is achieved, the UE shall indicate the selected
PLMN.
If registration cannot be achieved on any PLMN and at least one PLMN offering
restricted local operator services has been found, the UE shall obtain user
consent for restricted local operator services and the UE may use a list of
preferred PLMNs for restricted local operator services stored in the ME. If
none of the preferred PLMNs for restricted local operator services is
available, the UE shall select any available PLMN offering restricted local
operator services. If one of these PLMNs for restricted local operator service
is chosen, the UE shall indicate the choice. If none are selected, the UE
shall wait until a new PLMN is detected, or new location areas or tracking
areas of an allowed PLMN are found which are not in the forbidden LA or TA
list(s), and then repeat the procedure.
If registration cannot be achieved on any PLMN and no PLMN offering restricted
local operator services has been found, the UE shall indicate \"no service\"
to the user, wait until a new PLMN is detected, or new location areas or
tracking areas of an allowed PLMN are found which are not in the forbidden LA
or TA list(s), and then repeat the procedure. When registration cannot be
achieved, different (discontinuous) PLMN search schemes may be used in order
to minimize the access time while maintaining battery life, e.g. by
prioritising the search in favour of BCCH carriers which have a high
probability of belonging to an available and allowable PLMN.
**B) Manual network selection mode**
The UE shall indicate PLMNs, including \"Forbidden PLMNs\", which are
available. If there are none, this shall also be indicated. The HPLMN of the
user may provide on the USIM additional information about the available PLMNs,
if this is provided then the UE shall indicate that information to the user.
This information, provided as free text may include:
\- Preferred partner;
\- roaming agreement status;
\- supported services.
Furthermore, the UE may indicate whether the available PLMNs are present on
one of the PLMN selector lists (e.g. EHPLMN, User Controlled, Operator
Controlled or Forbidden) as well as not being present on any of the lists.
For the purpose of presenting the names of the available PLMNs to the user,
the ME shall use the USIM defined names if available or other PLMN naming
rules in priority order as defined in 3GPP TS 22.101 [7] (Country/PLMN
indication).
Any available PLMNs shall be presented in the following order:
> i) HPLMN (if the EHPLMN list is not present); or if one or more of the
> EHPLMNs are available then based on an optional data field on the USIM
> either the highest priority available EHPLMN is to be presented to the user
> or all available EHPLMNs are presented to the user in priority order; if the
> data field is not present, then only the highest priority available EHPLMN
> is presented;
>
> ii) PLMNs contained in the \"User Controlled PLMN Selector\" data field in
> the SIM/USIM (in priority order);
>
> iii) PLMNs contained in the \"Operator Controlled PLMN Selector\" data field
> in the SIM/USIM (in priority order);
>
> iv) other PLMN/access technology combinations with sufficient received
> signal level (see 3GPP TS 23.122 [3]) in random order;
>
> v) all other PLMN/access technology combinations in order of decreasing
> signal strength.
If a PLMN does not support voice services, then this shall be indicated to the
user.
The user may select the desired PLMN and the UE shall attempt registration on
this PLMN. (This may take place at any time during the presentation of PLMNs.)
If registration cannot be achieved on any PLMN and at least one PLMN offering
restricted local operator services has been found, the UE shall obtain user
consent for restricted local operator services and offer the user to select
one of these networks. If one of these networks is selected, the UE shall
indicate the selected PLMN, wait until a new PLMN is detected, or new location
areas or tracking areas of an allowed PLMN are found which are not in the
forbidden LA or TA list(s), and then repeat the procedure.
If the registration cannot be achieved on any PLMN and no PLMN offering
restricted local operator services is selected, the UE shall indicate \"No
Service\". The user may then select and attempt to register on another or the
same PLMN following the above procedure. The UE shall not attempt to register
on a PLMN which has not been selected by the user.
Once the UE has registered on a PLMN selected by the user, the UE shall not
automatically register on a different PLMN unless:
i) The new PLMN is declared as an equivalent PLMN by the registered PLMN;
or,
ii) The user selects automatic mode.
If a PLMN is selected but the UE cannot register on it because registration is
rejected with the cause \"PLMN not allowed\", the UE shall add the PLMN to the
"Forbidden PLMN" list (clause 3.2.2.4.1). The UE shall not re-attempt to
register on that network unless the same PLMN is selected again by the user.
If a PLMN is selected but the UE cannot register for PS services on it because
registration is rejected with the cause \"GPRS services not allowed in this
PLMN\", the UE shall not re-attempt to register for E-UTRAN or UTRAN PS or
GERAN PS on that network. The PLMN is added to the list \"Forbidden PLMN\'s
for GPRS services\". The UE shall not re-attempt to register for E-UTRAN or
UTRAN PS or GERAN PS on that network unless the same PLMN is selected again by
the user. The reception of the cause \"GPRS services not allowed in this
PLMN\", does not affect the CS service.
For requirements to restrict the access of a UE to one or several specific
RATs see section 7.1.
If a PLMN is selected but the UE cannot register on it for other reasons, the
UE shall, upon detection of a new LA (not in a forbidden LA list) of the
selected PLMN, attempt to register on the PLMN.
If the UE is registered on a PLMN but loses coverage, different
(discontinuous) carrier search schemes may be used to minimize the time to
find a new valid BCCH carrier and maintain battery life, e.g. by prioritizing
the search in favour of BCCH carriers of the registered PLMN.
#### 3.2.2.3 User reselection
At any time, the user may request the UE to initiate reselection and
registration onto an alternative available PLMN, according to the following
procedures, dependent upon the operating mode.
**A) Automatic Network Selection Mode**
The UE shall follow the procedure defined in clause 3.2.2.2.A) above,
including the use of Operator signal threshold per access technology, if set
on the USIM, as described in 3.2.2.2.
**B) Manual Network Selection Mode**
The procedure of 3.2.2.2 B) is followed.
#### 3.2.2.4 Mobile Station reactions to indications of service restriction
from the network
Different types of UE behaviour are required to support, for example, national
roaming, regionally provided service and temporary international roaming
restrictions. The behaviour to be followed by the UE is indicated by the
network.
##### 3.2.2.4.1 \"Permanent\" PLMN restriction
When a registration attempt by the UE is rejected by a network with an
indication of \"permanent\" PLMN restriction, the PLMN identity shall be
written to a list of \"Forbidden PLMNs\" stored in a data field in the
SIM/USIM.
If a successful registration is achieved on a PLMN in the \"Forbidden PLMN\"
list, the PLMN shall be deleted from the list. However, if successful
registration is achieved on a PLMN in the \"Forbidden PLMN\" list while
Disaster Condition applies, the PLMN shall not be deleted from \"Forbidden
PLMN\" list.
When in automatic mode, the UE may indicate any PLMNs which will not be
selected due to their presence in the \"Forbidden PLMN\" list.
If a UE receives an equivalent PLMN list containing a PLMN which is included
in the "Forbidden PLMN" list, this PLMN shall be removed from the equivalent
PLMN list before this is stored by the UE.
##### 3.2.2.4.2 \"Partial\" and \"temporary\" PLMN restrictions
When a registration attempt by the UE is rejected by a network due to a
\"partial\" or a \"temporary\" PLMN restriction, the UE shall perform one of
the following procedures determined by the indication in the location update
reject cause sent by the network (see 3GPP TS 23.122 [3]):
i) The UE shall store the tracking area identity or location area identity in
the list of \"5GS forbidden TA, forbidden TAs or forbidden LAs for regional
provision of service\" respectively and shall enter the limited service state.
The UE shall remain in that state until it moves to a cell in a location area
where service is allowed;
ii) The UE shall store the tracking area identity or the location area
identity in the list of \"5GS forbidden TA, forbidden TAs or forbidden LAs for
roaming\" respectively and shall use one of the following procedures according
to the PLMN selection Mode:
A) Automatic network selection mode:
The procedure of 3.2.2.2. A).
B) Manual network selection mode:
The procedure of 3.2.2.2.B).
iii) The UE shall store the tracking area identity or location area identity
in the list of \"5GS forbidden TA, forbidden TAs or forbidden LAs for
roaming\" respectively and shall search for a suitable cell in the same PLMN.
NOTE: A suitable cell will belong to a different TA or LA which is not in the
\"forbidden TAs or LAs for roaming\". When a TA supports multiple systems
(e.g. 5GS and EPS), a cell of the TA may be a suitable cell for one system
while the cell is not a suitable cell for other systems..
##### 3.2.2.4.3 PLMN restrictions for PS services
When a registration attempt for PS services by the UE is rejected by the
network with the cause \"GPRS services not allowed in this PLMN\", the PLMN
identity shall be written to a list of \"forbidden PLMNs for GPRS service\" in
the ME. This list is deleted when the UE is switched off or when the SIM/USIM
is removed; the maximum number of possible entries in this list is
implementation dependent, but must be at least one entry (see 3GPP TS 23.122
[3]).
If a successful registration is achieved on a PLMN in the \"forbidden PLMNs
for GPRS service\" list, the PLMN shall be deleted from the list.
#### 3.2.2.5 Periodic network selection attempts
If the Operator controlled signal threshold per access technology is not set
on the USIM, a UE in Automatic Mode shall make periodic attempts to look for a
higher priority PLMN including associated Access Technology of the same
country as the currently received PLMN including associated Access Technology
or for a higher priority PLMN including associated Access Technology that uses
a Shared MCC (e.g. MCC=901). If the currently received PLMN including
associated Access Technology uses a Shared MCC, also a higher priority PLMN
including associated Access Technology using any non-Shared MCC shall be
considered. For the ranking of PLMNs the UE shall use the order used in clause
3.2.2.2. In the case that there is no associated Access Technology identifier,
the mobile shall assume that all Access Technologies provided by a PLMN are of
equal priority. Moreover, periodic network selection shall not lead to change
of access technology within the registered PLMN.
When a Disaster Condition is applicable, a UE in Automatic Mode that is
registered to a PLMN in the \"Forbidden PLMN\" data field in the SIM/USIM may
make periodic attempts to look for an allowable PLMN of the same country as
the currently received PLMN.
In the case that the UE has stored a list of equivalent PLMNs, the UE shall
only select a PLMN if it has a higher priority than all the PLMNs, in the list
of equivalent PLMNs, which are of the same country as the currently registered
PLMN.
NOTE 1: In the context of this 3GPP TS, the term country is to be interpreted
not as a political entity but as a single Mobile Country Code (MCC). For
example the USA and India have multiple MCC. Such cases are in fact treated as
exceptions in the 3GPP specifications. For all other countries, multiple MCCs
may be used, however the specifications have not taken this into account and
there could be adverse effects such as the UE being unable to detect that
multiple MCCs are within the same country.
NOTE 2: There are some situations where one MCC represents multiple political
entities or where an MCC is independent of political entities. Examples
include Shared MCCs, where international satellite operations typically use
the Shared MCC with value 901.
NOTE 3: For the purposes of PLMN selection, the associated Access Technology
using a Shared MCC is restricted to the satellite NG-RAN.
In the case that there are multiple EHPLMNs available, the UE shall not
attempt to select a higher priority EHPLMN when an EHPLMN has already been
selected. The priorities of EHPLMNs are only applicable when the UE is on a
VPLMN and multiple EHPLMNs are available.
The UE shall only make reselection attempts while in idle mode. In case of
GPRS terminals, the UE shall only make reselection attempts while in Idle or
Stand-by mode. In case of terminals operating E-UTRA and/or NR, the UE shall
only make reselection attempts while in Idle or RRC-Inactive mode.
In the case of a UE receiving an eMBMS transport service when in idle mode,
the UE may postpone the higher priority PLMN search and any reselection
attempt until the eMBMS transport service has finished or been stopped.
The interval between attempts shall be stored in the SIM/USIM.
Only the service provider shall be able to select for which of the previous
situations, periodic network selection shall be attempted and to set the
interval value.
For UEs supporting only Access Technologies other than the following: NB-IoT,
GERAN EC-GSM-IoT and Category M1 [17] of E-UTRAN enhanced-MTC the UE shall
interpret the interval value to be between 6 minutes and 8 hours, with a step
size of 6 minutes.
For UEs only supporting any of the following, or a combination of, NB-IoT,
GERAN EC-GSM-IoT [18], and Category M1[13] of E-UTRAN enhanced-MTC, the UE
shall interpret the interval value to be between 2 and 240 hours, with a step
size of 2 hours between 2 and 80 hours and a step size of 4 hours between 80
and 240 hours.
For UEs supporting a combination of IoT and non-IoT Access Technologies the UE
shall interpret the interval value to determine the timer value as above based
on the Access Technology currently in use by the UE.
One interval value shall be designated to indicate that no periodic attempts
shall be made.
In the absence of a permitted value in the SIM/USIM, or the SIM/USIM is phase
1 and therefore does not contain the datafield, then a default value of 60
minutes, shall be used by the UE except for those UEs only supporting any of
the following, or a combination of: NB-IoT, GERAN EC-GSM-IoT [18], and
Category M1 [17] of E-UTRAN enhanced-MTC. For those UEs a default value of 72
hours shall be used.
NOTE 4: Use of values less than 60 minutes may result in excessive UE battery
drain.
**Periodic network selection based on Operator controlled signal threshold
criteria**
If the Operator controlled signal threshold per access technology is set on
the USIM, the UE shall perform the periodic network selection procedure
considering all PLMNs, of higher or lower priority than the current PLMN, in
the same order as in clause 3.2.2.2, with the following conditions:
\- the UE shall select a higher priority PLMN/access technology combination if
the target PLMN's access technology signal quality is equal to or higher than
the Operator controlled signal threshold per access technology;
\- the UE shall select a lower priority PLMN/access technology combination
only if the RPLMN's access technology signal quality is lower than the
Operator controlled signal threshold per access technology, and the target
PLMN's access technology signal quality is equal or higher than the Operator
controlled signal threshold per access technology.
NOTE 5: The UE does not perform the periodic attempts if the RPLMN is a HPLMN
or EHPLMN, and the RPLMN's access technology signal quality is equal or higher
than the Operator controlled signal threshold per access technology.
If no PLMN, including the RPLMN, fulfils the Operator controlled signal
threshold criteria, the UE shall perform the normal periodic network selection
for higher priority PLMNs (as described above), without applying the Operator
controlled signal threshold per access technology.
#### 3.2.2.6 Investigation PLMN Scan
The operator shall be able to control by SIM/USIM configuration whether a UE
that is capable shall perform an investigation scan. This investigation scan
shall be performed after each successful PLMN selection as well as during
limited service state. The investigation scan shall search for a higher
prioritised PLMN that does not offer CS voice service. If such a PLMN is
available, the user shall be informed. This enables the user to switch to such
a PLMN using manual selection if the user so prefers. The investigation scan
shall not be performed when no SIM/USIM is inserted.
#### 3.2.2.7 Void
#### 3.2.2.8 Steering Of Roaming
**Steering to a specific VPLMN**
It shall be possible for the HPLMN at any time to direct a UE, that is in
automatic mode, to search for a specific VPLMN and, if it is available, move
to that VPLMN as soon as possible. This VPLMN shall then be regarded as the
highest priority VPLMN as defined by the operator, though any EHPLMN or PLMN
on the User Controlled PLMN list shall have higher priority. This process
shall be done transparently and without inconvenience to the user.
If the Operator controlled signal threshold per access technology is set on
the USIM, the UE shall only select the VPLMN if the signal quality is equal to
or higher than the Operator controlled signal threshold per access technology,
otherwise the steering request shall be ignored.
If the UE is in manual mode, the steering request shall be ignored.
If the UE is registered on a VPLMN that is present on the User Controlled PLMN
List, the steering request shall be ignored. PLMNs contained on the User
Controlled PLMN List shall have priority over the steered-to-PLMN.
The UE shall attempt to register on the specified VPLMN even if the specified
VPLMN is present on a Forbidden List.
This mechanism shall be available to the HPLMN even if the VPLMN the UE is
registered on is compliant to an earlier release of the 3GPP specifications.
**VPLMN Redirection**
It shall be possible for the HPLMN to request a UE, that is in automatic mode,
to find and register on a different VPLMN from the one it is currently using
or trying to register on, if another VPLMN, that is not in a Forbidden List,
is available. The original VPLMN shall then be treated as the lowest priority
VPLMN and would not be selected by the UE unless it is the only one available
to the UE or has been selected in manual mode. This process shall be done
transparently and without inconvenience to the user.
If the UE is in manual mode, the redirection request shall be ignored.
If the UE is registered on a VPLMN that is present on the User Controlled PLMN
List, the redirection request shall be ignored.
This mechanism shall be available to the HPLMN even if the VPLMN the UE is
registered on is compliant to an earlier release of the 3GPP specifications.
### 3.2.3 Network selection for Multi-mode terminals with 3GPP Capability
Different types of Multi-mode terminals combining different technologies and
systems in one terminal can be produced. It is not possible to foresee all
possible configurations and provide a detailed technical specification for
network and system selection for all possible multi-mode terminal
configurations. The following provides the generic requirements for network
and system selection for Multi-mode terminals with 3GPP Capability. These
requirements are mandatory for a 3GPP capable multi-mode terminal, unless
otherwise is explicitly specified elsewhere in the 3GPP Technical
Specifications.
\- a multi-mode terminal, when in 3GPP mode of operation shall be compliant to
the 3GPP specifications, including PLMN selection, cell selection and re-
selection, paging reception etc.,
\- As consequence, the multi-mode terminal when entering 3GPP mode of
operation shall act as if it were a 3GPP only UE which had just been switched-
on. Similarly, when leaving the 3GPP mode of operation the multimode terminal
shall act as if it were a 3GPP only UE which had just been switched-off
When the multimode terminal is in 3GPP mode, the switching between modes in
the multi-mode terminal is considered an overlay functionality selecting mode
of operation. For the design of the overlay functionality the following
requirements shall be fulfilled:
\- The overlay functionality shall include a mechanism to avoid ping-pong
between systems, e.g., a timer or hysteresis function;
\- The overlay functionality shall not include network priority mechanisms,
which conflict with the network priority mechanisms specified in 3GPP
specifications, e.g., the Periodic network selection attempts scanning within
3GPP based systems for PLMNs of higher priority than the current serving PLMN;
\- Any functionality in the overlay system, such as background scan of other
systems, shall not impact the fulfilment of 3GPP protocol requirements (in
particular in regard to paging, cell selection, cell re-selection and PLMN
selection);
\- As specified in this technical specification, the 3GPP technical
specification provides the capability for the user to set their own 3GPP PLMN
selection preferences; as well as the user can manually select any 3GPP PLMN.
This has been done to ensure a fair competition environment. These principles
shall be maintained in the design of the overlay functionality.
# 4 Access control
## 4.1 Purpose
Under certain circumstances, it will be desirable to prevent UE users from
making access attempts (including emergency call attempts) or responding to
pages in specified areas of a PLMN. Such situations may arise during states of
emergency, or where 1 of 2 or more co-located PLMNs has failed.
Broadcast messages should be available on a cell by cell basis indicating the
class(es) or categories of subscribers barred from network access.
The use of these facilities allows the network operator to prevent overload of
the access channel under critical conditions.
It is not intended that access control be used under normal operating
conditions.
It should be possible to differentiate access control between CS and PS
domains. Details are specified in TS23.122[3] and TS25.304 [10]. Not all RATs
need to support this functionality.
## 4.2 Allocation
All UEs are members of one out of ten randomly allocated mobile populations,
defined as Access Classes 0 to 9. The population number is stored in the
SIM/USIM. In addition, UEs may be members of one or more out of 5 special
categories (Access Classes 11 to 15), also held in the SIM/USIM. These are
allocated to specific high priority users as follows. (The enumeration is not
meant as a priority sequence):
Class 15 - PLMN Staff;
-\"- 14 - Emergency Services;
-\"- 13 - Public Utilities (e.g. water/gas suppliers);
-\"- 12 - Security Services;
-\"- 11 - For PLMN Use.
## 4.3 Operation
### 4.3.1 Access Class Barring
If the UE is a member of at least one Access Class which corresponds to the
permitted classes as signalled over the radio interface, and the Access Class
is applicable in the serving network, access attempts are allowed.
Additionally, in the case of the access network being UTRAN the serving
network can indicate that UEs are allowed to respond to paging and perform
location registration (see, sec 3.1), even if their access class is not
permitted. Otherwise access attempts are not allowed. **Also, the serving
network can indicate that UEs are restricted to perform location registration,
although common access is permitted.** If the UE responded to paging it shall
follow the normal defined procedures and react as specified to any network
command.
NOTE: The network operator can take the network load into account when
allowing UEs access to the network.
Access Classes are applicable as follows:
Classes 0 - 9 - Home and Visited PLMNs;
Classes 11 and 15 - Home PLMN only if the EHPLMN list is not present or any
EHPLMN;
> Classes 12, 13, 14 - Home PLMN and visited PLMNs of home country only. For
> this purpose the home country is defined as the country of the MCC part of
> the IMSI.
Any number of these classes may be barred at any one time.
In the case of multiple core networks sharing the same access network, the
access network shall be able to apply Access Class Barring for the different
core networks individually.
The following are the requirements for enhanced Access control on E-UTRAN.
\- The serving network shall be able to broadcast mean durations of access
control and barring rates (e.g. percentage value) that commonly applied to
Access Classes 0-9 to the UE. The same principle as in UMTS is applied for
Access Classes 11-15;
\- E-UTRAN shall be able to support access control based on the type of access
attempt (i.e. mobile originating data or mobile originating signalling), in
which indications to the UEs are broadcasted to guide the behaviour of UE.
E-UTRAN shall be able to form combinations of access control based on the type
of access attempt e.g. mobile originating and mobile terminating, mobile
originating, or location registration. The 'mean duration of access control'
and the barring rate are broadcasted for each type of access attempt (i.e.
mobile originating data or mobile originating signalling);
\- The UE determines the barring status with the information provided from the
serving network, and perform the access attempt accordingly. The UE draws a
uniform random number between 0 and 1 when initiating connection establishment
and compares with the current barring rate to determine whether it is barred
or not. When the uniform random number is less than the current barring rate
and the type of access attempt is indicated allowed, then the access attempt
is allowed; otherwise, the access attempt is not allowed. If the access
attempt is not allowed, further access attempts of the same type are then
barred for a time period that is calculated based on the 'mean duration of
access control' provided by the network and the random number drawn by the UE;
\- The serving network shall be able to indicate whether or not a UE shall
apply Access Class Barring for SMS access attempts in SMS over SGs, SMS over
IMS (SMS over IP), and SMS over S102. This indication is valid for Access
Classes 0-9 and 11-15;
\- The serving network shall be able to indicate whether or not a UE shall
apply Access Class Barring for MMTEL voice access attempts. This indication is
valid for Access Classes 0-9 and 11-15;
\- The serving network shall be able to indicate whether or not a UE shall
apply Access Class Barring for MMTEL video access attempts. This indication is
valid for Access Classes 0-9 and 11-15.
### 4.3.2 Service Specific Access Control
Additionally to the above requirements in 4.3.1;
\- In E-UTRAN it shall be possible to support a capability called Service
Specific Access Control (SSAC) to apply independent access control for
telephony services (MMTEL) for mobile originating session requests from idle-
mode and connected-mode as following:
\- The serving network shall be able to indicate (as specified in sub-clause
4.3.1) whether or not a UE subject to SSAC shall also apply Access Class
Barring.
\- EPS shall provide a capability to assign a service probability factor [13]
and mean duration of access control for each of MMTEL voice and MMTEL video:
\- assign a barring rate (percentage) commonly applicable for Access Classes
0-9;
\- assign a flag barring status (barred /unbarred) for each Access Class in
the range 11-15;
\- SSAC shall not apply to Access Class 10;
\- SSAC can be provided by the VPLMN based on operator policy without
accessing the HPLMN;
\- SSAC shall provide mechanisms to minimize service availability degradation
(i.e. radio resource shortage) due to the mass simultaneous mobile originating
session requests and maximize the availability of the wireless access
resources for non-barred services;
\- The serving network shall be able to broadcast mean durations of access
control, barring rates for Access Classes 0-9, barring status for Access class
in the range 11-15 to the UE;
\- The UE determines the barring status with the information provided from the
serving network, and perform the access attempt accordingly. The UE draws a
uniform random number between 0 and 1 when initiating connection establishment
and compares with the current barring rate to determine whether it is barred
or not. When the uniform random number is less than the current barring rate
and the type of access attempt is indicated allowed, then the access attempt
is allowed; otherwise, the access attempt is not allowed. If the access
attempt is not allowed, further access attempts of the same type are then
barred for a time period that is calculated based on the 'mean duration of
access control' provided by the network and the random number drawn by the UE.
### 4.3.3 Access Control for CSFB
Access control for CSFB provides a mechanism to prohibit UEs to access E-UTRAN
to perform CSFB. It minimizes service availability degradation (i.e. radio
resource shortage, congestion of fallback network) caused by mass simultaneous
mobile originating requests for CSFB and increases the availability of the
E-UTRAN resources for UEs accessing other services.
When an operator determines that it is appropriate to apply access control for
CSFB, the network may broadcast necessary information to provide access
control for CSFB for each class to UEs in a specific area. The network shall
be able to separately apply access control for CSFB, SSAC and enhanced Access
control on E-UTRAN.
The following requirements apply for CSFB to 1xRTT:
\- In E-UTRAN, the network may apply access control for mobile originating
session requests on CSFB from 1xRTT/E-UTRAN UE, The parameters received by the
UE are dealt with in accordance with CDMA2000 procedures in 3GPP2 C.S0004-A:
\"Signaling Link Access Control (LAC) Standard for cdma2000 Spread Spectrum
Systems -- Addendum 2\" [15].
For CSFB to UTRAN or GERAN, the necessary information in the broadcast to
provide access control for CSFB is the same as that specified in Clause 4.3.1.
In addition to those requirements the following apply:
\- Access control for CSFB shall apply for Access Class 0-9 and Access Class
11-15.It shall not apply for Access Class 10;
\- Access control for CSFB shall be applied for idle mode UE;
\- Access control for CSFB shall apply to all CSFB services;
\- Access control for CSFB may be provided by the VPLMN based on operator
policy without accessing the HPLMN;
\- If Access control for CSFB, according to the UE\'s access class, disallows
originating session requests for CSFB then a UE shall not send mobile
originating session requests for CSFB;
\- If Access control for CSFB is applied by the UE for a mobile originating
session request for CSFB, the UE shall bypass enhanced Access control on
E-UTRAN for that session.
\- The criteria on which a UE determines whether Access control for CSFB
allows or disallows originating session requests for CSFB are equivalent to
those for enhanced Access control on E-UTRAN, as described in clause 4.3.1;
\- If access is not granted for the UE, mobile originating session requests
for CSFB shall be restricted for a certain period of time to avoid overload of
E-UTRAN due to continuous mobile originating session requests from the same
UE. The duration of the period shall be determined using the same operation
specified in Clause 4.3.1;
\- In case the network does not provide the Access control for CSFB
information, the UE shall be subject to access class barring for Access
Classes 0-9 and 11-15 as described in Clause 4.3.1.
### 4.3.4 Extended Access Barring
#### 4.3.4.1 General
Extended Access Barring (EAB) is a mechanism for the operator(s) to control
Mobile Originating access attempts from UEs that are configured for EAB in
order to prevent overload of the access network and/or the core network. In
congestion situations, the operator can restrict access from UEs configured
for EAB while permitting access from other UEs. UEs configured for EAB are
considered more tolerant to access restrictions than other UEs. When an
operator determines that it is appropriate to apply EAB, the network
broadcasts necessary information to provide EAB control for UEs in a specific
area. The following requirements apply for EAB:
  * The UE is configured for EAB by the HPLMN;
> \- EAB shall be applicable to all 3GPP Radio Access Technologies used in EPS
> or UMTS;
NOTE: When a UE configured for EAB is located in 5G system, the UE is
considered as configured for delay tolerant service.
\- EAB shall be applicable regardless of whether the UE is in a Home or a
Visited PLMN;
\- A network may broadcast EAB information;
\- EAB information shall define whether EAB applies to UEs within one of the
following categories:
a) UEs that are configured for EAB;
b) UEs that are configured for EAB and are neither in their HPLMN nor in a
PLMN that is equivalent to it;
c) UEs that are configured for EAB and are neither in the PLMN listed as most
preferred PLMN of the country where the UE is roaming in the operator-defined
PLMN selector list on the SIM/USIM, nor in their HPLMN nor in a PLMN that is
equivalent to their HPLMN.
\- EAB information shall also include extended barring information for Access
Classes 0-9;
\- A UE configured for EAB shall use its allocated Access Class(es), as
defined in sub-clause 4.2, when evaluating the EAB information that is
broadcast by the network, in order to determine if its access to the network
is barred;
\- If a UE that is configured for EAB answers to paging, initiates an
emergency call or, is a member of an Access Class in the range 11-15 and
according to clause 4.3.1 that Access Class is permitted by the network, then
the UE shall ignore any EAB information that is broadcast by the network;
\- If the network is not broadcasting the EAB information, the UE shall be
subject to access barring as described in clause 4.3.1;
\- If the EAB information that is broadcast by the network does not bar the
UE, the UE shall be subject to access barring as described in clause 4.3.1;
\- In the case of multiple core networks sharing the same access network, the
access network shall be able to apply the EAB for the different core networks
individually.
#### 4.3.4.2 Overriding extended access barring
Overriding Extended Access Barring is a mechanism for the operator to allow
UEs that are configured for EAB to access the network under EAB conditions.
The following requirements apply:
\- The UE configured with EAB may be configured by the HPLMN with a permission
to override EAB;
\- For a UE configured with the permission to override EAB, the user or
application (upper layers in UE) may request the UE to activate PDN
connection(s) for which EAB does not apply;
\- The UE shall override any EAB restriction information that is broadcast by
the network as long as it has an active PDN connection for which EAB does not
apply.
### 4.3.5 Application specific Congestion control for Data Communication
(ACDC)
#### 4.3.5.1 Service description
Application specific Congestion control for Data Communication (ACDC) is an
access control mechanism for the operator to allow/prevent new access attempts
from particular, operator-identified applications in the UE in idle mode. ACDC
does not apply to UEs in connected mode. The network can prevent/mitigate
overload of the access network and/or the core network. This feature is
optional.
#### 4.3.5.2 Requirements
##### 4.3.5.2.1 General
The following requirements apply:
\- This feature shall be applicable to UTRAN PS Domain and E-UTRAN;
\- This feature shall be applicable to UEs in idle mode only that are not a
member of one or more of Access Classes 11 to 15;
\- ACDC shall not apply to MMTEL voice, MMTEL video, SMS over IMS (SMS over
IP) emergency call and paging response;
NOTE 1: Even if any of the above services are initiated by application, ACDC
does not apply, but they are subject to other applicable access control
methods.
\- The home network shall be able to configure a UE with at least four and a
maximum of sixteen ACDC categories to each of which particular, operator-
identified applications are associated. The categories shall be ordered as
specified in sub-clause 4.3.5.2.2;
NOTE 2: Provisioning of the ACDC categories in the UE is the responsibility of
the home network, and the categorization is outside the scope of 3GPP.
NOTE 3: A mechanism needs to be provided that enables the UE to verify that
the provisioning of the configuration originates from a trusted source.
\- The serving network shall be able to broadcast, in one or more areas of the
RAN, control information, indicating barring information per each ACDC
category, and whether a roaming UE shall be subject to ACDC control;
NOTE 4: The barring information may be similar to ACB information, and include
mean durations of access control (i.e., barring timer) and barring rates
(i.e., percentage value). If the barring timer is running due to a previous
access attempt from an application in a certain given matched ACDC category,
the UE may only allow access attempts from applications in higher ACDC
categories (according to the corresponding barring information for those
higher categories). If the barring timer is running due to a previous access
attempt from an application in a certain given unmatched ACDC category or a
uncategorised application, the UE may only allow access attempts from
applications in higher ACDC categories than the lowest ACDC category broadcast
(according to the corresponding barring information for those higher
categories).
\- The UE shall be able to control whether or not an access attempt for a
certain application is allowed, based on this broadcast barring information
and the configuration of ACDC categories in the UE;
\- The serving network shall be able to simultaneously indicate ACDC with
other forms of access control;
\- When both ACDC and ACB controls are indicated, ACDC shall override ACB;
\- If a UE is configured for both EAB and ACDC, and the serving network
simultaneously broadcasts EAB information and ACDC barring information:
\- If the UE determines as specified in sub-clause 4.3.4.1 that access to the
network is not barred or as specified in sub-clause 4.3.4.2 that it is
permitted to override an EAB restriction, then access to the network is
subject to ACDC;
\- If the UE determines as specified in sub-clause 4.3.4.1 that access to the
network is barred and as specified in sub-clause 4.3.4.2 that it is not
permitted to override the EAB restriction, then access to the network is
barred.
\- In the case of multiple core networks sharing the same access network, the
access network shall be able to apply ACDC for the different core networks
individually. For the mitigation of congestion in a shared RAN, barring rates
should be set equal for all Participating Operators.
##### 4.3.5.2.2 ACDC Categories
When configuring the UE with categories of applications, the home network
shall proceed as follows:
\- Applications whose use is expected to be restricted the least shall be
assigned the highest ACDC category; and
\- Applications whose use is expected to be restricted more than applications
in the highest category shall be assigned the second-to-highest ACDC category,
and so on; and
\- Applications whose use is expected to be restricted the most shall either
be assigned the lowest ACDC category, or not be categorised at all.
For a UE with ACDC categories configured, the applications on the UE that are
not assigned to any ACDC category shall be treated by the UE as part of the
lowest ACDC category broadcast by the serving network. If the operator
requires differentiation with respect to these uncategorized applications, the
operator should avoid assigning applications to the lowest ACDC category. When
applying ACDC, the serving network broadcasts barring information starting
from the highest to the lowest ACDC category. The home network and the serving
network may use different categorisation. The serving network decides if ACDC
applies to roaming UEs.
The number of ACDC categories in the UE may not be the same as the number of
ACDC categories broadcast by the serving network. This may happen, e.g. when
the UE is roaming and the number of categories broadcast by the serving
network is different from the home network. Therefore, the following rules
shall apply:
\- If the serving network broadcasts more ACDC categories than the UE\'s
configuration, the UE shall use barring information for the matching ACDC
category and shall bar uncategorised applications using the barring
information for the lowest category broadcast by the serving network, and
shall ignore barring information for unmatched categories.
\- If the serving network broadcasts barring information for fewer ACDC
categories than the UE\'s configuration, the UE shall use barring information
for the matching ACDC category and shall bar other applications using the
barring information for the lowest category broadcast by the serving network.
NOTE: A matching ACDC category is an ACDC category for which barring
information is broadcast by the serving network and that has the same rank as
the rank of a configured ACDC category in the UE. An unmatched ACDC category
is either an ACDC category for which barring information is broadcast by the
serving network but with no corresponding ACDC category configured in the UE,
or an ACDC category configured in the UE but with no corresponding barring
information broadcast by the serving network.
### 4.3.6 Access Control for Indirect 3GPP Communications
For the case where an Evolved ProSe Remote UE is trying to access the network
via an Evolved ProSe UE-to-Network Relay, the following requirements apply:
\- Access control for CSFB shall not apply to an Indirect 3GPP Communication;
\- ACB, EAB and ACDC shall apply when the Evolved ProSe UE-to-Network Relay is
in IDLE mode and when the access control information for the respective access
control is broadcast by the network;
\- SSAC shall apply when the Evolved ProSe UE-to-Network Relay is either in
IDLE or CONNECTED mode and when the access control information for SSAC is
broadcast by the network;
\- The interaction between ACDC, EAB and ACB (defined in paragraph 4.3.5.2.1)
shall be based on the Evolved ProSe Remote UE's configuration;
\- During the access control procedure, the requirements in subsections of
4.3.1, 4.3.2, 4.3.4 and 4.3.5 shall be performed by Evolved Prose Remote UE
using the following parameters:
\- Access control parameters broadcast by the cell where the Evolved ProSe UE-
to-Network Relay is camped on or connected to shall be used in all access
control procedures;
\- Access Class of the Evolved ProSe Remote UE shall be used;
\- For ACB, the type of access attempt (i.e. mobile originating data, mobile
originating signalling, response to paging or emergency call) of the Evolved
ProSe Remote UE shall be used;
\- For EAB, the following information shall be used:
\- Whether or not the Evolved ProSe Remote UE is configured with EAB;
\- Whether or not the Evolved ProSe Remote UE is configured with a permission
to override EAB;
\- Whether the PLMN is the Evolved ProSe Remote UE's Home PLMN, equivalent
PLMN or preferred PLMN. The PLMN where the Evolved ProSe UE-to-Network Relay
is camped/connected shall be used to make this determination.
\- For SSAC, the type of access attempt (MMTEL voice or MMTEL video) of the
Evolved ProSe Remote UE shall be used;
\- For ACDC, the ACDC category of the application that triggered the access
attempt in the Evolved ProSe Remote UE shall be used.
## 4.4 Emergency Calls
An additional control bit known as \"Access Class 10\" is also signalled over
the radio interface to the UE. This indicates whether or not network access
for Emergency Calls is allowed for UEs with access classes 0 to 9 or without
an IMSI. For UEs with access classes 11 to 15, Emergency Calls are not allowed
if both \"Access class 10\" and the relevant Access Class (11 to 15) are
barred. Otherwise, Emergency Calls are allowed.
## 4.4a Multimedia Priority Service
Multimedia Priority Service (TS 22.153 [16]) shall be assigned its own unique
access class value (i.e., one of the special access classes 11 to 15). The
assigned access class value for Multimedia Priority Service is based on
regional/national regulatory requirements and operator policy.
## 4.5 Control of UE Capabilities
To protect the user from the effects of a misbehaving UE (e.g. causing
additional charges, degraded performance) and to protect the network
operator\'s network capacity, including radio resources and network signalling
and processing, means shall be provided for the HPLMN/EHPLMN and the VPLMN to
provide an indication to the UE as to which network provided services or
functions it is not allowed to use.
The Selective UE Capabilities list shall be maintained in the UE and the UE
shall not request any services indicated as disabled. At registration the
HPLMN/EHPLMN or VPLMN may interrogate the status of the list and provide a new
list.
The Selective UE Capabilities list shall not be deleted at switch off and will
remain valid until a new list is provided by the network. The Selective UE
Capabilities list relates to the ME and not to the subscription.
It should be ensured that UEs are not maliciously disabled, including
malicious disabling by a VPLMN, or accidentally disabled, or kept disabled,
and there shall be a mechanism for restoring disabled UEs in all situations
(e.g. in the case that the serving network does not support the control of UE
Capabilities).
The UE should use the indications given in the Selective UE Capabilities list
to inform the user of the non-availability of services or functions.
There shall be a means for the network to provide an optional customer service
number(s) which can be used, by the user, to assist in determining the cause
of non-availability of specific services. The specifications should also
provide the capability for the network to include an optional text string that
will be displayed by the UE.
The UE Capabilities list shall take precedence over subscribed services.
The services to be included in the list are:
\- Call Control functions;
\- Supplementary Services;
\- Emergency Calls (including the (U)SIM-less case and subject to regional
regulatory requirements, i.e. emergency calls shall not be disabled in regions
where support of them is required);
\- SMS, via CS and PS;
\- LCS, via CS and PS;
\- GPRS based services;
\- MBMS;
\- IMS.
## 4.6 Prevention of mobile-originating signalling and/or data traffic
The network shall be able to control the behavior of UEs in E-UTRAN in
connected mode to prevent mobile originating signalling and/or data traffic,
while the access barring mechanisms specified under Clause 4.3 are being
applied to UEs in idle mode.
# 5 Support of Localised Service Area (SoLSA)
SoLSA consists of a set of service features that give the operator a basis to
offer subscribers different services (e.g. tariffs or access rights) depending
on the location of the subscriber. (3GPP TS 22.043 [5]). The following section
is only applicable to the support of SoLSA functionality in GERAN.
## 5.1 Network selection
The standard automatic and manual network selection procedures will be used.
Manual network selection may be required when the PLMN providing the users
SoLSA service is not the one on which the user is currently registered.
At manual network selection the UE shall provide the means to present the
subscribers LSA(s) for each PLMN presented.
## 5.2 The Idle-mode operation
The UE shall always select a valid LSA with the highest priority.
### 5.2.1 Subscriber moving from a normal environment to his localised service
area
The UE shall have the ability to prioritise allowed LSA cells in reselection,
making it possible to camp on a LSA cell earlier (the function shall be
network controlled).
### 5.2.2 Subscriber moving away from his localised service area to a normal
environment
The UE shall have the ability to prioritise allowed LSA cells in reselection,
making it possible to camp on a LSA cell longer (the function shall be network
controlled).
### 5.2.3 Subscriber staying in his localised service area
The UE shall have the ability to prioritise allowed LSA cells in reselection
by being more persistent (the function shall be network controlled).
NOTE: Typically in indoor environments there are occasional reflections and
\"disturbances\" due to macro cells, e.g. near the windows. In such a case LSA
cells should be favoured even though there is higher field strength available
from the outdoor cells.
## 5.3 LSA only access
It shall be possible to allow LSA user to access PLMN only within his LSAs. A
LSA user is not allowed to receive and/or originate a call outside the allowed
LSA area.
When UE is out of the allowed LSA area it shall be registered in PLMN but
indicate subscriber/service specific \"out of LSA area\" notification. It
shall be a network-controlled function to prevent terminated or/and originated
calls. Emergency calls are however always allowed.
## 5.4 Exclusive access
Access to exclusive access cells is restricted to defined LSA subscribers.
Non-LSA subscriber shall consider exclusive access cells as not suitable, only
allowing to camp for emergency calls (limited service state 3GPP TS 23.122
[3]).
## 5.5 Preferential access
As a network-controlled function, it shall be possible in LSA to allocate
resources at call setup and during the active mode to LSA users compared to
non-LSA users.
# 6 Support of 3GPP - WLAN Interworking
Support of 3GPP-WLAN interworking and network selection is captured in TS
22.234 [6]
NOTE: The requirement specification 22.234 is no longer maintained from
Release 12 onwards.
## 6.1 Void
## 6.2 Void
## 6.3 Void
# 7 Administrative restriction of subscribers' access
## 7.1 Allowed Location and Routing Area identities access
Means shall be standardised for an administrative restriction of subscribers'
access without the need of having explicit Tracking/Location/Routing Area
identities in the individual subscription profiles.
To achieve this it shall be possible to indicate per subscriber, in
subscription data, allowed categories of Tracking/ Location/Routing Areas. It
shall be possible to use this subscription information to restrict
subscribers' access to categories of Tracking/Location/Routing Areas in
serving networks accordingly.
As a minimum, at least one of the following categories shall be available:
a) GERAN;
b) UTRAN;
c) E-UTRAN;
d) NG-RAN.
There might be cases where the visited network has not separated the
Location/Routing area categories, in which case the administrative restriction
of subscribers\' access to only GERAN or UTRAN will not be possible.
In EPS, an operator may introduce subscriptions supporting the 5G NR Dual
Connectivity in E-UTRAN. It shall be possible to indicate in subscription data
that a subscriber´s access to the 5G NR Dual Connectivity in E-UTRAN service
is restricted.
This administrative restriction of subscribers' access shall be an optional
feature.
## 7.2 Void
## 7.3 UE configured radio technology restriction
A UE shall support a Man Machine Interface setting for the user to disable use
of one or more of the UE's radio technologies, regardless of PLMNs. Radio
technologies that individually can be disabled is dependent on supported radio
technology of the UE such as GSM/EDGE, WCDMA, E-UTRA, and NR.
A UE shall support a Man Machine Interface setting enabling the user to re-
enable use of one or more of the ME's radio technologies for access to a radio
access network, regardless of PLMNs. The user can only re-allow a radio
technology that the user has previously disallowed.
NOTE: The described MMI user setting is a proprietary function of most legacy
UE products to allow a user of a UE to change the radio capabilities of the
UE. Legacy radio technologies may lack means to mitigate some security attack.
If severe enough, the home operator may want to disallow their subscribers to
access a radio access network with such radio technology. This configuration
of the UE is valid for all PLMNs.
A UE shall support a secure mechanism for the home operator to disallow
selection of one or more of the UE's radio technologies for access to a radio
access network, regardless of PLMNs. Radio technologies that individually can
be disallowed are at least GSM/EDGE, WCDMA, E-UTRA, and NR.
A UE shall support a secure mechanism for the home operator to re-allow
selection of one or more of the UE's radio technologies for access to a radio
access network, regardless of PLMNs. Radio technologies that individually can
be re-allowed are at least GSM/EDGE, WCDMA, E-UTRA, and NR. The home operator
can only re-allow a radio technology that the home operator has previously
disallowed.
For a prioritized service (e.g., Emergency Services, MPS, Mission Critical
Services), the UE shall support a mechanism to automatically override user and
network disallowed RATs when there are no PLMNs on the allowed radio
technologies identified that the UE is able to access.
Upon power-cycle or when the USIM is disabled, the UE configuration of
enabled/disabled radio technologies configured by the user shall remain as it
was before such events happen. The radio technologies disallowed by the HPLMN
shall remain as it was before a power cycle. The radio technologies disallowed
by the HPLMN shall be bound to the USIM
# 8 Support of Home NodeB and Home E-NodeB
The service requirements for Home NodeB and Home eNodeB can be found in [14].
# 9 Control of traffic from UE-based applications toward associated server
## 9.1 Description
This feature allows operators to control traffic from UEs to an application on
a third-party server or the third-party server itself. When an application on
a third-party server or the third-party server itself becomes congested or
fails the traffic towards that server need to be controlled to avoid/mitigate
potential issues caused by resulting unproductive use of 3GPP network
resource. This will also make it possible to allow 3GPP network to help third
party servers to handle overload and recover from failures (see [7]).
## 9.2 Requirements
Under network control, the UE shall be able to control (i.e. block and/or
prioritize) traffic from UEs to an application on a third-party server or the
third-party server itself without affecting traffic to other applications on
the third-party server or to other third-party servers.
For this purpose, the UE shall be able to identify the traffic towards the
third-party server or the application on the third-party server.
When congestion or failure of the application on the third-party server or the
third-party server abates, the control shall be applied in a phased manner to
gradually restore traffic according to operator policy.
This feature and other forms of access control shall be able to be applied
simultaneously.
In case of simultaneous application of ACDC and this feature, this feature
shall take precedence over ACDC to control traffic from applications in the
UE, only when such traffic is allowed by ACDC.
This feature shall be applicable both to new connections being set up and to
existing connections from the UE towards an application on a third-party
server or the third-party server.
# 10 3GPP PS Data Off
## 10.1 Description
3GPP PS Data Off is a feature which, when configured by the HPLMN and
activated by the user, prevents transport via PDN connections in 3GPP access
networks of all data packets except IP packets required by 3GPP PS Data Off
Exempt Services.
## 10.2 Requirements
The 3GPP system shall provide a mechanism by which an operator can configure
which operator services are defined as 3GPP PS Data Off Exempt Services for
their own subscribers.
When 3GPP PS Data Off is activated in the UE, in order to preserve charging
consistency:
\- the UE shall inform the network that 3GPP PS Data Off is activated;
\- the UE shall cease the sending of uplink IP Packets of all services that
are not 3GPP PS Data Off Exempt Services via PDN connections in 3GPP access
networks;
\- the network shall cease the sending of downlink IP Packets to the UE for
all services that are not 3GPP PS Data Off Exempt Services via PDN connections
in 3GPP access networks;
\- the UE shall cease the sending of uplink traffic over non-IP PDN types via
PDN connections in 3GPP access networks; and
\- the network shall cease the sending of downlink traffic over non-IP PDN
types via PDN connections in 3GPP access networks.
NOTE 1: Disabling of traffic on both the uplink and downlink is needed in
order to provide consistency of charging between HPLMN and VPLMN, as well as
consistency between what the user expects and what the user may be billed for.
Each of the following operator services shall be configurable by the HPLMN
operator to be part of the 3GPP PS Data Off Exempt Services:
\- MMTel Voice;
\- SMS over IMS;
\- USSD over IMS (USSI);
\- MMTel Video;
\- Services over IMS Data Channel;
\- Particular IMS services not defined by 3GPP, where each such IMS service is
identified by an IMS communication service identifier;
\- Device Management over PS;
\- Management of USIM files over PS (e.g. via Bearer Independent Protocol);
and
\- IMS Supplementary Service configuration via the Ut interface using XCAP.
NOTE 1a: IMS Data Channel is defined in 3GPP TS 26.114[20].
3GPP PS Data Off may be activated based on roaming status, and the HPLMN may
configure up to two sets of 3GPP PS Data Off Exempt Services for its
subscribers: one is used when in HPLMN and another when roaming.
NOTE 2: The updating to the sets of configured 3GPP Data Off Exempt Services
in the VPLMNs and HPLMN is not guaranteed to take effect in real time. The
updating to the sets of configured 3GPP Data Off Exempt Services in the UEs is
not guaranteed take effect in real time.
The user should be made aware of the operator services that are 3GPP PS Data
Off Exempt Services.
NOTE 3: The system can support falling back to operate over the CS domain in
case an operator service is not configured to be a 3GPP PS Data Off Exempt
Service and an equivalent CS domain operator service exists for the operator
service.
###### ## Annex A (informative): Change history