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
The solution for support of IMS Emergency calls defined for Rel-7 in TS 23.167
[2] has a number of limitations and potential limitations. These include
restriction only to certain IP-CANs, restriction only to cases where at least
part of the IP-CAN and visited IMS belong to the same operator, possible non-
alignment with the various allowed IETF solutions and possible performance
limitation. While it is possible that none of these limitations will be
significant for some deployments of this service, it is not certain that this
will apply to all deployments. Therefore it has been decided to evaluate both
the service defined in [2] and possible extensions that might overcome these
limitations.
# 1 Scope
The present document provides a study investigating possible limitations of
the solution for IMS emergency calls defined for Rel-7 in 3GPP TS 23.167 [2],
as well as possible extensions of that solution to reduce or eliminate some or
all of the identified limitations.
The study item is expected mainly to concern IMS although some aspects of IP-
CAN support may also be included. The study item has the following objectives
\- Evaluate the feasibility of supporting IMS emergency calls for combinations
of IP access network A and IMS core network B not supported in Rel-7 including
but not limited to the following cases:
\- A is any IP access network and B is the home 3GPP compliant IMS network for
any emergency calling UE with adequate security credentials
\- A is any IP access network and B is a visited 3GPP compliant IMS network
for any emergency calling roaming UE with adequate security credentials
Additional user cases may also be proposed and evaluated during the SI if
deemed applicable.
\- Evaluate other enhancements to the solution for IMS emergency calls in
Release 7 that may improve performance and/or reduce complexity
\- Evaluate the feasibility of better aligning the solution in TS 23.167 with
applicable IETF standards and draft standards (e.g., from the Ecrit and
Geopriv working groups)
\- Any enhancement to the support of IMS emergency calls shall remain backward
compatible to the solution in Rel-7 from the perspective of the UE and any
3GPP network element. Furthermore, any enhancement should be based on the
solution in Rel-7 and should avoid unnecessarily adding new network entities,
protocols and interfaces and moving existing functions from one entity to
another.
The study item is expected to enable TSG SA WG2 to decide which of the above
objectives if any may be worth supporting in Rel-8 and which extensions to the
current solution would then be appropriate.
# 2 References
The following documents contain provisions which, through reference in this
text, constitute provisions of the present document.
  * References are either specific (identified by date of publication, > edition number, version number, etc.) or non‑specific.
  * For a specific reference, subsequent revisions do not apply.
  * For a non-specific reference, the latest version applies. In the > case of a reference to a 3GPP document (including a GSM document), > a non-specific reference implicitly refers to the latest version > of that document _in the same Release as the present document_.
[1] 3GPP TR 21.905: \"Vocabulary for 3GPP Specifications\".
[2] 3GPP TS 23.167: "IP Multimedia Subsystem (IMS) emergency sessions".
> [3] IETF draft-ietf-ecrit-framework-05: "Framework for Emergency Calling
> using Internet Multimedia".
>
> [4] IETF draft-ietf-ecrit-phonebcp-04: "Best Current Practice for
> Communications Services in support of Emergency Calling".
>
> [5] IETF draft-ietf-sip-location-conveyance-09: "Location Conveyance for the
> Session Initiation Protocol".
>
> [6] IETF RFC 4119: "A Presence-based GEOPRIV Location Object Format".
>
> [7] IETF RFC 3856: "A Presence Event Package for the Session Initiation
> Protocol (SIP)".
>
> [8] IETF draft-ietf-geopriv-http-location-delivery-05: "HTTP Enabled
> Location Delivery (HELD)".
>
> [9] IETF draft-winterbottom-geopriv-deref-protocol-00: "An HTTPS Location
> Dereferencing Protocol Using HELD".
>
> [10] ANSI/TIA-1057: "Link Layer Discovery Protocol -- Media Endpoint
> Discovery".
>
> [11] IETF RFC 3825: "Dynamic Host Configuration Protocol Option for
> Coordinate-based Location Configuration Information".
>
> [12] IETF RFC 4676: "Dynamic Host Configuration Protocol (DHCPv4 and DHCPv6)
> Option for Civic Addresses Configuration Information".
# 3 Definitions, symbols and abbreviations
Delete from the above heading those words which are not applicable.
Subclause numbering depends on applicability and should be renumbered
accordingly.
## 3.1 Definitions
For the purposes of the present document, the terms and definitions given in
TR 21.905 [1], TS 23.167 [2] and the following apply. A term defined in the
present document takes precedence over the definition of the same term, if
any, in TR 21.905 [1] or TS 23.167.
Definition format
**\ **: \.
## 3.2 Symbols
For the purposes of the present document, the following symbols apply:
Symbol format
\ \
## 3.3 Abbreviations
For the purposes of the present document, the abbreviations given in TR 21.905
[1], TS 23.167 [2] and the following apply. An abbreviation defined in the
present document takes precedence over the definition of the same
abbreviation, if any, in TR 21.905 [1] or TS 23.167 [2].
Abbreviation format
\ \
CP Control Plane
> DHCP Dynamic Host Configuration Protocol
E-SLP Emergency SLP
> HELD HTTP Enabled Location Delivery
>
> LIS Location Information Server
>
> LLDP-MED Link Layer Discovery Protocol -- Media Endpoint Discovery
SLP SUPL Location Platform
SUPL Secure User Plane Location
UP User Plane
V-SLP Visited SLP
# 4 Overall Requirements
Editor's Note: This section will expand upon the objectives listed in clause
1.
## 4.1 Solution Characteristics
It is intended to extend the solution currently defined in Rel-7 so that it
can support, as far as possible and within the limitations defined in clause 1
above, any IP based emergency call made from any access as long as both the
network providing emergency call handling and the UE are 3GPP IMS compliant.
Preferred characteristics of this extended solution are listed below. Some of
these preferences (e.g. (1)) could be considered as requirements.
1) Support existing interfaces to a PSAP accessed via the PSTN.
2) Support a single interface to a PSAP accessed via IP from a call >
perspective and a single interface from a location access > perspective.
Variants of either single interface may be permitted > (e.g. needed to support
different regional requirements) although > it is preferred to subsume all
variants within a single standard > in each case. If this is not possible, a
single call related > standard and a single location related standard should
be the goal > for each world region.
3) Make use of existing OMA and IETF standards where possible and >
appropriate for new protocols, network elements and signalling > objects -- as
a preference to creating new 3GPP definitions.
4) Minimize the number of different location solutions and location > related
network elements and protocols that need to be supported > (on the network as
opposed to PSAP side) subject to attaining the > various other requirements
defined here.
5) Support reduced call establishment delay through elimination or > reduction
of potential sources of high delay such as interaction > with a home network
(e.g. to support registration and multiple > registration attempts) and
location retrieval (e.g. for routing > purposes).
6) Use a single interface between the serving IMS network and the > IP-CAN
from a call perspective and a single interface from a > location access
perspective that can be reused for any IP-CAN > (e.g. any wireless access
network) -- or at least for as many > IP-CAN types as possible.
7) Use a single interface between the serving IMS network and the UE > from a
call perspective and a single interface from a location > access perspective
that is applicable for any IP-CAN (e.g. any > wireless access network) -- or
at least for as many IP-CAN types > as possible.
# 5 Architectural Requirements and Considerations
Editor's Note: This section will provide a common foundation and set of common
denominators for the architectural alternatives to be considered in clause 6.
## 5.1 Basic Assumptions
The following assumptions are made regarding the architecture for any extended
solution for IMS emergency calls.
1) The IMS network architecture in TS 23.167 [2] will be the basis > for
supporting extended capabilities.
2) Additional types of IP-CAN may be supported if there is no impact to > the
IMS network architecture and if any signalling changes (e.g. > new SIP
parameters or parameter values) are backward compatible.
## 5.2 Architectural Requirements
### 5.2.1 Reference Architecture
Figure 5.2.1-1 shows a simplified reference architecture that is consistent
with both the solution in Rel-7 and the preferred characteristics of an
extended solution listed in clause 4.1.
**Figure 5.2.1-1 -- Reference Architecture**
Some possible example constituents for some of the service entities shown in
the Figure are shown in Table 5.2.1-1 for different types of IP-CAN.
+-------------+-------------+-------------+-------------+-------------+ | **Type of |** IP-CAN IP | **IMS Call |** IP-CAN | **IMS | | IP-CAN** | c | service**| Location | Location | | | onnectivity | | Service** | Service**| | | service** | | | | +-------------+-------------+-------------+-------------+-------------+ | GPRS | GERAN or | P-CSCF, | With a CP | With a CP | | (Rel-8) | UTRAN, | E-CSCF | solution: | solution: | | | SGSN, GGSN | | SGSN, GERAN | LRF, GMLC | | | | | or UTRAN, | | | | | | SMLC | With a UP | | | | | | solution: | | | | | With a UP | LRF, E-SLP | | | | | solution: | | | | | | V-SLP or | | | | | | null | | +-------------+-------------+-------------+-------------+-------------+ | I-WLAN | WLAN, WAG, | P-CSCF, | V-SLP or | LRF, E-SLP | | | PDG, AAA | E-CSCF | DHCP server | | | | server | | | | +-------------+-------------+-------------+-------------+-------------+ | WLAN direct | WLAN, AAA | P-CSCF, | V-SLP or | LRF, E-SLP | | IP access | server | E-CSCF | DHCP server | | +-------------+-------------+-------------+-------------+-------------+
**Table 5.2.1-1 -- Some Service Components in Figure 5.2.1-1**
### 5.2.2 IMS Network
Figure 5.2.2-1 shows the IMS network architecture defined in TS 23.167 [2]
with some potential extension to show possible LRF interaction with the IP-CAN
and/or UE as implied by Figure 5.2.1-1. Interfaces and network elements shown
in heavier font in this figure should be easier to extend and enhance without
violating the backward compatibility requirement since the associated
interactions and functions are either not completely defined in Rel-7 or are
both undefined (or only partially defined) and outside the scope of 3GPP. All
of these interfaces and network elements relate to support of location. The
rest of the figure (in lighter font) relates to support of registration, call
establishment and call back and will be more subject to the backward
compatibility requirement.
**Figure 5.2.2-1 -- IMS Network Architecture**
### 5.2.3 IP-CAN
The following simple definition of an IP-CAN is given in TS 23.167 [2]:
> **P-Connectivity Access Network (IP-CAN):** The collection of network
> entities and interfaces that provides the underlying IP transport
> connectivity between the UE and the IMS entities**.** An example of an \"IP-
> Connectivity Access Network\" is I‑WLAN.
That this definition is more complex than it seems is shown by the following
possible attributes of an IP-CAN in association with the objectives in clause
1:
\- may be entirely owned by a single 3GPP operator (e.g. GPRS IP-CAN)
\- may be split among multiple operators (e.g. I-WLAN where operator A owns
the WLAN AP, operator B owns the WAG and home operator C owns the PDG and AAA
server)
\- for a non-roaming scenario, may or may not be located or partly located in
the H-PLMN
\- for a roaming scenario, may or may not be located or partly located in the
V-PLMN
In order to support such a diversity of IP-CAN types, it is assumed that the
principle already implicit in TS 23.167 [2] will be continued whereby call
handling support is restricted to the serving IMS network and the role of the
IP-CAN is to provide access to the serving IMS network and certain pieces of
essential or useful information such as network (or access point) identity and
location related information.
## 5.3 Session Scenarios
### 5.3.1 Home Network Access to Emergency Services
Figure 5.3.1-1 is a simple adaptation of Figure 5.2.1-1 illustrating home
network access to emergency services.
. **Figure 5.3.1-1 -- Home Network Access to Emergency Services**
The normal assumption in Rel-7 is that Figure 5.3.1-1 applies when the UE is
not roaming and thus generally within the geographic area of coverage of the
home network if this is 3GPP. However, these assumptions would no longer
necessarily apply for an extended solution that enabled the home network
operator to provide emergency services access to its subscribers even when
roaming (e.g. to assist in cases where a V-PLMN does not support IMS emergency
services and to enhance home network IMS services for its roaming
subscribers). In particular, while the UE, serving IP-CAN and PSAP may all lie
within (or partly within) the same local geographic area the home IMS network
may be geographically remote (e.g. in a different state, county or even
country).
### 5.3.2 Visited Network Access to Emergency Services
Figure 5.3.2-1 is a simple adaptation of Figure 5.2.1-1 illustrating visited
network access to emergency services (and not showing the Home IMS network
role for registration).
. **Figure 5.3.2-1 -- Visited Network Access to Emergency Services**
The normal assumption in Rel-7 is that Figure 5.3.2-1 applies when the UE is
roaming and thus generally outside the geographic area of coverage of the home
network if this is 3GPP but within the coverage area of some other visited
3GPP network. However, these assumptions would no longer necessarily apply for
an extended solution that enabled a visited network operator to provide
emergency services access over an extended area to roaming subscribers. In
particular, while the UE, serving IP-CAN and PSAP may all lie within (or
partly within) the same local geographic area the visited IMS network may be
geographically remote (e.g. in a different state or county).
# 6 Architecture Alternatives
Editor's Note: This section will describe and evaluate alternative
architecture additions to the solution in Rel-7 that can support one or more
of the objectives listed in clause 1 and requirements listed in clause 4. Some
of the alternatives may be complimentary (i.e. capable of being combined)
while others may be mutually exclusive.
## 6.1 IMS Emergency Call Redirection
### 6.1.1 Objectives
If a subscriber does not have wireless access at the time an emergency call is
dialled (e.g. the user has just powered on the phone before dialling) or if
the user has access to a data only network without voice call capability (e.g.
has internet access via a WLAN) then the user's expectation of a an emergency
call succeeding and the legal requirements for some VSP supporting the
emergency call will both be significantly lower than if the user is already
accessing a voice capable network (e.g. a 3GPP voice capable VPLMN) at the
time the emergency call is dialled. This suggests that any extended solution
for IMS emergency calls should at least support the latter case in all
scenarios, or in as many scenarios as possible.
A major problem is that in many cases, the VSP accessed by the user will not
be local to the user's current location. For example, the user may be in a
roaming situation and accessing the H-PLMN or some other remote VSP using
direct IP access (e.g. from a WLAN or some other data only access network). In
that case, the VSP may not be able to establish an emergency call to a
suitable local PSAP and there will be no local VSP (e.g. 3GPP VPLMN) already
being accessed to fall back to.
Of course, the serving VSP could just reject an attempt to establish an IMS
emergency call (e.g. via a 380 alternative service response) leaving the UE to
search around for some alternative -- e.g. via scanning for VSPs accessible
from its current IP-CAN or by performing a radio search for other wireless IP-
CANs. But that is hardly a reliable solution and, moreover, the serving VSP
may have some strong interest in helping establish an emergency call -- not
least because as a service to its subscribers, it could be used to increase
the VSP's subscriber base and revenue.
This section and the following one provide two alternative solutions whereby a
serving VSP can direct the call to a more suitable local VSP without requiring
the UE to perform a new search. With the solution in this section, the
original serving VSP employs a SIP 380 response to provide the UE with the URI
of an alternative VSP.
### 6.1.2 Architectural Details
The solution defined here does not require any change to the existing
architecture already defined in TS 23.167 [2]. It just requires that the
serving VSP and new VSP to which the call is redirected both support this
architecture.
### 6.1.3 Information Flows
Figure 6.1.3-1: Redirection of an IMS emergency call
1\. The user initiates an emergency call.
2\. The UE determines its own location or location identifier or obtains
location information from the IP-CAN.
3\. The UE sends a REGISTER with an emergency indication or an INVITE with an
emergency indication to the currently serving IMS core (IMS Core 1). The
REGISTER or INVITE should contain any location information that the terminal
has. For security reasons, the UE may include location information or at least
accurate location information only in an INVITE and not in a REGISTER.
4\. The serving IMS Core (e.g. the P-CSCF) may obtain further location
information from the IP-CAN and/or UE. The serving IMS Core determines from
the location information provided in step 3 and/or from the location
information obtained from the IP-CAN and/or UE that the UE is outside the
emergency serving area for IMS Core 1. The serving IMS Core returns a 3xx
response (e.g. a 380 Alternative Service response) that includes the URI (e.g.
IP address or FQDN) of a P-CSCF in an alternative IMS Core (IMS Core 2) --
e.g. in the SIP Contact Address header of the 3xx response. The serving IMS
Core may include URIs for additional IMS Cores. The provided URIs and their
location association might be configured in the serving IMS Core. For some
locations, no URIs might be configured, in which case a 3xx (e.g. 380)
response not carrying any URI would be returned. The provision of a URI or
URIs might be further constrained according to whether the serving IMS Core is
the home IMS for the UE (e.g. might only be provided if the serving IMS Core
is the home IMS Core) and according to whether reliable location information
is available (e.g. might only be provided if the IP-CAN or UE is able to
provide reliable location information).
5\. The UE sends a REGISTER with an emergency indication to the alternative
IMS Core, or one of the alternative IMS Cores, indicated in step 4. The
REGISTER should contain any location information that the UE has.
6\. If the alternative IMS Core (e.g. a P-CSCF) determines that the UE is
outside its own emergency serving area or that an emergency call cannot be
supported for other reasons (e.g. no agreement with the UE's home network), it
may return a 3xx response carrying one or more URIs for other IMS Cores as in
step 4. In that case, the UE may attempt to use other IMS Core networks in
step 5, if these were provided in step 4 or step 6. Otherwise, the alternative
IMS Core (e.g. a P-CSCF) continues the emergency registration via the UE's
home network. In so doing, the identity of the UE will be authenticated and a
secure IP connection will be established with the UE.
7\. The UE sends an INVITE with an emergency indication to the alternative IMS
core (IMS Core 2). The INVITE should contain any location information that the
UE has. The INVITE may be forwarded within the alternative IMS Core -- e.g.
from a P-CSCF to an E-CSCF -- and additional location information may be
obtained (e.g.; by an LRF).
8\. The alternative IMS core selects an emergency centre or PSAP based on
location information available in step 7.\ 8a. The INVITE is sent to an
MGCF/MGW,\ 8b. The IAM is continued towards the emergency centre or PSAP, or\
8c. The INVITE is sent directly to the emergency centre or PSAP.
9\. The emergency call establishment is completed.
### 6.1.4 Evaluation
The procedure described in clause 6.1.3 is optional and, if supported, impacts
the IMS Core and the UE. Impacts to the IMS Core could be restricted to the
P-CSCF. The impacts can be backward compatible with Release 7 -- at least if a
380 response is used in step 4 of Figure 6.1.3-1. Specifically, if an IMS core
does not support this procedure, then an emergency call attempt in step 3 of
Figure 6.1.3-1 would probably fail but there would not be any protocol or
procedural violations. If the UE supports IMS emergency calls only according
to Release 7, the URI(s) provided by the serving IMS Core in step 4 of Figure
6.1.3-1 would be ignored which would mean that the call might not be resent to
an alternative IMS core via the current IP-CAN. On the other hand, if a 380
response, which is already part of Release 7, is used in step 4, the UE would
be aware of the need to find and register in a local visited network and thus
existing release 7 actions could be used to attempt to setup the call.
Backward compatibility for other 3xx responses is FFS.
The procedure defined here may not be applicable to a UE that has not yet
recognized an emergency call since in that case a pre-Release 7 380 response
may be needed in step 4 of Figure 6.1.3-1 which would not carry any URI.
## 6.2 IMS Emergency Call Forwarding
### 6.2.1 Objectives
IMS Emergency call forwarding is an extension to the solution in Release 7
that has the same objectives and rationale as the extension described in
clause 6.1. It can be viewed as an alternative solution for these objectives.
Instead of redirecting the call back to the UE, the initial serving IMS Core
forwards the call to an alternative IMS Core.
### 6.2.2 Architectural Details
The solution defined here extends the architecture defined in TS 23.167 [2] as
shown in the figure below.
**Figure 6.2.2-1 -- IMS Emergency Call Forwarding Architecture**
In figure 6.2.2-1, P-CSCF 1 and E-CSCF 1 belong to IMS Core Network 1 (e.g.
the Home IMS Core Network or a currently serving IMS Core Network) while
E-CSCF 2 and LRF 2 belong to IMS Core Network 2 -- e.g. one supporting IMS
emergency calls at the current location of the UE. The interface from P-CSCF 1
to E-CSCF 2 and the interface from E-CSCF 1 to E-CSCF 2 are alternatives only
one of which is needed. The S-CSCF would either belong to IMS Core network 1
or to a separate home IMS Core if IMS Core Network 1 is not the UE's home
network.
### 6.2.3 Information Flows
Figure 6.2.3-1: IMS Emergency Call Forwarding
1\. The user initiates an emergency call.
2\. The UE determines its own location or location identifier or obtains
location information from the IP-CAN.
3\. The UE may initiate an IMS Emergency Registration with the currently
serving IMS Core (IMS Core 1) by sending a REGISTER with an emergency
indication to P-CSCF 1. If so, P-CSCF 1 continues the emergency registration
with the home IMS network as defined in TS 23.167 [2]. The IMS Emergency
registration may not be needed if IMS Core 1 is the home network and the UE
assumes it is not roaming.
4\. The UE sends an INVITE with an emergency indication to P-CSCF 1. The
INVITE should contain any location information that the UE has.
5\. Based on the location information received in step 4, P-CSCF 1 may forward
the INVITE to E-CSCF 2 in another IMS Core network (IMS Core 2) that supports
IMS emergency calls for the current location of the UE. In this case, steps 5
and 6 are omitted.
6\. If step 5 is not used, P-CSCF 1 forwards the INVITE to E-CSCF 1 in the
same IMS Core network.
7\. E-CSCF 1 may verify any location information obtained in step 6 and may
obtain additional location information (e.g. from an associated LRF). Based on
this location information, E-CSCF 1 forwards the INVITE to E-CSCF 2 in another
IMS Core network (IMS Core 2) that supports IMS emergency calls for the
current location of the UE. Forwarding in this step or in step 5 requires
agreements between the participating IMS Cores (e.g. IMS Core 1 and IMS Core
2) and associated configuration data (e.g. concerning location mapping to
different IMS Cores) in each IMS Core. Forwarding is also dependent on
location information being available and may not be possible for all IP-CANs.
8\. E-CSCF 2 may itself or using an associated LRF verify any location
information obtained in step 7, obtain additional location information,
determine an emergency centre or PSAP based on this location information and
determine correlation information (e.g. an ESQK).\ 8a. The INVITE is sent to
an MGCF/MGW,\ 8b. The IAM is continued towards the emergency centre or PSAP,
or\ 8c. The INVITE is sent directly to the emergency centre or PSAP.
9\. The emergency call establishment is completed.
### 6.2.4 Evaluation
The procedure described in clause 6.2.3 is optional and, if supported, adds
impacts to IMS Core 1, However, the procedure is transparent to the UE, to the
PSAP and can be transparent to IMS Core 2 provided E-CSCF 2 is configured to
receive IMS emergency calls from IMS Core 1 (e.g. by maintaining secure IP
connections between the communicating entities at all times or by allowing
such secure connections to be established as needed dynamically). Impacts to
IMS Core 1 could be restricted to just the P-CSCF or to just the E-CSCF
depending on whether the P-CSCF or the E-CSCF forwards the call to IMS Core 2
in Figure 6.2.3-1. To avoid impact to a P-CSCF, it may be preferred to retain
only the E-CSCF to E-CSCF interface alternative and not allow the alternative
of forwarding from a P-CSCF. As the UE will only be registered via IMS Core 1,
a trust relationship should exist between IMS Core 1 and IMS core 2 such that
IMS Core 2 can assume that any UE identity and call back URI provided by IMS
Core 1 in step 5 or step 7 of Figure 6.2.3-1 is already authenticated. The
impacts should be backward compatible with Release 7 since only IMS Core
Network 1 is impacted.
Besides enabling support of IMS emergency calls outside the normal coverage
area of a network (IMS Core 1 in Figure 6.2.3-1), the procedure also enables
an IMS Core Network to support IMS Emergency Calls for its users when it does
not possess all the necessary entities (e.g. if there is no E-CSCF and LRF) --
by forwarding all IMS Emergency calls from the P-CSCF to one E-CSCF or to
several alternative E-CSCFs in other networks.
The procedure defined here is applicable to a UE that has not recognized an
emergency call since the forwarding can be transparent to the UE.
The procedure defined here is not applicable internationally -- i.e. in the
case that IMS Core 1 and IMS Core 2 belong to 2 different countries \-- except
if agreements exist. This may be due to regulatory constraints (e.g. on
forwarding an emergency call to another country) and/or due to technical
restrictions related to forwarding between SIP proxies in different countries.
Forwarding of emergency calls may also not be possible due to (legal)
liability uncertainties between the operators involved. The extent of this
restriction and its possible resolution are FFS.
## 6.3 Enhanced Location Support
### 6.3.1 Objectives
The current solution for IMS Emergency calls in TS 23.167 [2] explicitly
references and allows use of the 3GPP Control plane location solution and OMA
SUPL but other possible location solutions are not explicitly supported. To
improve on this, it would be useful to extend the current procedures to allow
use of other solutions. While such other solutions might not be defined by
3GPP and might not even be defined by some other body until later, having an
extended 3GPP solution that allowed for such other location solutions could be
useful to operators and vendors and could help avoid a situation where a
deployed solution did not exactly fit within the 3GPP definition.
### 6.3.2 Architectural Details
Architectural details are outside the scope of 3GPP.
### 6.3.3 Information Flows
Below is the current description of location support from clause 7.6.1 of [2]
with proposed changes to it shown in bold italic.
Figure 6.3.3-1: Handling of location information in IMS emergency calls
1\. The user initiates an emergency call.
2\. The UE determines its own location or location identifier if possible. If
the UE is not able to determine its own location, the UE may, if capable,
request its location information from the IP-CAN, if that is supported for the
used IP-CAN. If applicable, the IP-CAN delivers to the UE the UE\'s
geographical location information and/or the location identifier.
3\. The UE sends an INVITE with an emergency indication to the IMS core. The
INVITE should contain any location information that the terminal has. The
location information may be geographical location information or a location
identifier, which is dependant upon the access network technology. In case the
UE is not able to provide any location information, the IMS core may seek to
determine the UE\'s location from the LRF as described below. The INVITE may
optionally contain information concerning the location solutions and position
methods supported by the UE.
NOTE: the location solutions and position methods conveyed in the INVITE and
the means of inclusion in the INVITE are outside the scope of this
specification.
4\. If the location information provided in step 3 is trusted and sufficient
to determine the correct PSAP, the procedure continues from step 7 onwards. If
the location information is insufficient or if the IMS core requires emergency
routing information, or if the IMS core is required to validate the location
information, or if the IMS core is required to map the location identifier
received from the UE into the corresponding geographical location information,
the IMS core sends a location request to the LRF. The request shall include
information identifying the IP-CAN and the UE and may include means to access
the UE (e.g. UE\'s IP address). The request shall also include any location
information provided by the UE in step 2. The request may optionally include
any information concerning the location solutions and position methods
supported by the UE.
5\. The LRF may already have the information requested by IMS core or LRF may
request the UE\'s location information. The means to obtain the location
information may differ depending on the access technology the UE is using to
access the IMS. **_In general, the LRF may interact with the IP-CAN and/or the
UE to obtain location information. In the case of IP-CAN interaction, the LRF
may communicate with a location server in the IP-CAN (e.g. a GMLC, an OMA SUPL
SLP or some other server) or may communicate with an entity supporting UE IP
connectivity (e.g. an SGSN). This interaction may or may not be defined by
3GPP. One example of a non-3GPP solution is OMA SUPL_** defined in OMA AD
SUPL: \"Secure User Plane Location Architecture\", OMA TS ULP: \"User Plane
Location Protocol\". **_This solution_** may be used if supported by the
terminal and if it is possible to establish a user plane connection between
the UE and the SUPL server. Information provided in step 4 concerning the
location solutions and position methods supported by the UE may optionally be
used by the LRF to help determine the means to obtain the location
information.
The LRF may invoke an RDF to convert the location information received in step
4 or obtained in step 5 into PSAP routing information, but LRF\'s interactions
with RDF are out of scope of the present specification. The LRF may store the
location information, but only for a defined limited time in certain regions,
according to regional requirements.
6\. The LRF sends the location information and/or the routing information to
the IMS core. The LRF may also return correlation information (e.g. ESQK)
identifying itself and any record stored in step 5.
7\. The IMS core uses the routing information provided in step 6 or selects an
emergency centre or PSAP based on location information provided in step 3 or 6
and sends the request including the location information and any correlation
information and possibly location information source, e.g., positioning method
that was used to obtain the location information to the emergency centre or
PSAP.\ 7a. The INVITE is sent to an MGCF/MGW,\ 7b. The IAM is continued
towards the emergency centre or PSAP, or\ 7c. The INVITE is sent directly to
the emergency centre or PSAP.
8\. The emergency call establishment is completed.
9\. The PSAP may send a location request to the LRF to get the initial
location information for the target UE, or to request LRF to get updated, i.e.
current, location information for the target UE. The PSAP may determine the
LRF based on the location and/or correlation information received in step 7.
The PSAP may also include the correlation information in the request to the
LRF.
10\. The LRF determines the target UE\'s location using one of the means
listed in step 5 above. The LRF may use the correlation information received
in step 9 to retrieve information about the UE that was stored in step 5.
11\. The LRF returns the initial or updated location information to the
emergency centre or PSAP. As an option for initial location, the LRF may
instigate the location step 10 before the request in step 9 is received and
may send the initial location to the emergency centre or PSAP either after the
request in step 9 is received or before it is received.
12\. The emergency call is released.
13\. The IMS core may indicate to the LRF that the call is released. The LRF
deletes any record stored in step 5.
### 6.3.4 Evaluation
This extension does not add any new specific impacts and its support by a UE,
IP-CAN and LRF would be optional. The main value is to allow vendors and
operators the possibility of supporting new location solutions in the future
without the need to revisit the basic solution for IMS emergency calls. This
is achieved by an explicit broadening of the solution. While it might be
claimed that the existing Release 7 solution already supports this extension
(and thus what is defined here is really editorial), it is believed that the
explicit extension here will be helpful.
## 6.4 Common Location Access
### 6.4.1 Objectives
The IETF solution for IP based emergency calls is defined in draft-ietf-ecrit-
framework-05 [3] and in draft-ietf-ecrit-phonebcp-04 [5]. This provides access
to location for an IP capable PSAP in a different manner to TS 23.167 [2].
With the IETF solution, a location by value or a location by reference would
be transferred in a new Geolocation SIP header (defined in draft-ietf-sip-
location-conveyance-09 [5]) in a SIP INVITE to the PSAP. A location by value
would be transferred in a message body containing an IETF Geopriv pidf-lo
(defined in IETF RFC 4119 [6]), which is also the solution enabled by TS
23.167 [2]. A location by reference would be transferred by including a SIP,
SIPS, PRES or possibly HELD URI in the Geolocation Header. The URI would refer
to the entity -- e.g. in the IETF solution a Location Information Server (LIS)
-- from which a location by value can subsequently be obtained using a
deferencing procedure. The dereferencing procedure can use the
SUBSCRIBE/NOTIFY mechanism defined in IETF RFC 3856 [7] or might possibly use
an extension to HELD defined in draft-ietf-geopriv-http-location-delivery-05
[8] and draft-winterbottom-geopriv-deref-protocol-00 [9]. The concept of
providing a location by reference URI to a PSAP and supporting dereferencing
to obtain a location value is not explicitly defined in TS 23.167 [2].
Instead, TS 23.167 defines the sending of correlation information to a PSAP
and the use of correlation information by a PSAP to subsequently retrieve
location.
While TS 23.167 is not in direct conflict with the IETF solution, there seems
no advantage in being possibly different, since it would be an advantage to
the PSAP and possibly to the network to support location delivery and
retrieval in the same manner. If that were not the case, the PSAP (and
possibly the network) might have to support 2 different solutions and the PSAP
would need to know which solution to use.
TS 23.167 can be made compatible with the IETF solution by explicitly defining
transfer of a location by reference URI in a SIP INVITE to a PSAP instead of
or in addition to a pidf-lo location value. Furthermore, in doing so, there
would be no requirement to incorporate other parts of the IETF solution such
as a LIS server in the IP-CAN or Location Configuration Protocols like HELD
(draft-ietf-geopriv-http-location-delivery-05 [8]), DHCP (IETF RFC 3825 [11]
and IETF RFC 4676 [12]) and LLDP-MED (ANSI/TIA-1057 [10]) which seem more
suitable for wireline and certain types of WLAN access. Instead, the LRF can
itself assign the location URI and ensure that the URI references the LRF and
the location or call record for the UE. From the perspective of the PSAP, it
will then not make any difference whether the call was originated from IETF
conforming networks or 3GPP conforming networks.
Similar reasoning applies to explicitly supporting IETF defined dereferencing
procedures between the PSAP and LRF.
### 6.4.2 Architectural Details
No architectural changes to TS 23.167 are needed.
### 6.4.3 Information Flows
Detailed information flows could be added to TS 23.167 showing transfer of a
location URI and different types of dereferencing procedures between a PSAP
and LRF. But these would be essentially informative since the source
definitions are provided by IETF already. It is thus proposed to include only
the indicated changes below to section 7.6.1 of TS 23.167 (changes shown in
bold italic) which take advantage of being able to reference IETF standards.
If needed, further clarification could be added to TS 23.167 (e.g. an
informative annex) when the changes were actually submitted.
Figure 6.4.3-1: Handling of location information in IMS emergency calls
1\. The user initiates an emergency call.
2\. The UE determines its own location or location identifier if possible. If
the UE is not able to determine its own location, the UE may, if capable,
request its location information from the IP-CAN, if that is supported for the
used IP-CAN. If applicable, the IP-CAN delivers to the UE the UE\'s
geographical location information and/or the location identifier.
3\. The UE sends an INVITE with an emergency indication to the IMS core. The
INVITE should contain any location information that the terminal has. The
location information may be geographical location information or a location
identifier, which is dependant upon the access network technology. In case the
UE is not able to provide any location information, the IMS core may seek to
determine the UE\'s location from the LRF as described below. The INVITE may
optionally contain information concerning the location solutions and position
methods supported by the UE.
NOTE: the location solutions and position methods conveyed in the INVITE and
the means of inclusion in the INVITE are outside the scope of this
specification.
4\. If the location information provided in step 3 is trusted and sufficient
to determine the correct PSAP, the procedure continues from step 7 onwards. If
the location information is insufficient or if the IMS core requires emergency
routing information, or if the IMS core is required to validate the location
information, or if the IMS core is required to map the location identifier
received from the UE into the corresponding geographical location information,
the IMS core sends a location request to the LRF. The request shall include
information identifying the IP-CAN and the UE and may include means to access
the UE (e.g. UE\'s IP address). The request shall also include any location
information provided by the UE in step 2. The request may optionally include
any information concerning the location solutions and position methods
supported by the UE.
5\. The LRF may already have the information requested by IMS core or LRF may
request the UE\'s location information. The means to obtain the location
information may differ depending on the access technology the UE is using to
access the IMS. The SUPL procedures defined in OMA AD SUPL: \"Secure User
Plane Location Architecture\" [15], OMA TS ULP: \"User Plane Location
Protocol\" [16], may be used if supported by the terminal and if it is
possible to establish a user plane connection between the UE and the SUPL
server. Information provided in step 4 concerning the location solutions and
position methods supported by the UE may optionally be used by the LRF to help
determine the means to obtain the location information.
The LRF may invoke an RDF to convert the location information received in step
4 or obtained in step 5 into PSAP routing information, but LRF\'s interactions
with RDF are out of scope of the present specification. The LRF may store the
location information, but only for a defined limited time in certain regions,
according to regional requirements.
6\. The LRF sends the location information and/or the routing information to
the IMS core. The LRF may also return correlation information (e.g. ESQK)
**_or a location URI (e.g. SIP URI, SIPS URI, HELD URI)_** identifying itself
and any record stored in step 5. The LRF can determine which location related
information to return -- e.g. location estimate, location URI, ESQK --
according to the capabilities and preferences of the PSAP which may be
configured in or otherwise available to the LRF.
7\. The IMS core uses the routing information provided in step 6 or selects an
emergency centre or PSAP based on location information provided in step 3 or 6
and sends the request including the location information and any correlation
information **_or location URI_** and possibly location information source,
e.g., positioning method that was used to obtain the location information to
the emergency centre or PSAP.\ 7a. The INVITE is sent to an MGCF/MGW,\ 7b. The
IAM is continued towards the emergency centre or PSAP, or\ 7c. The INVITE is
sent directly to the emergency centre or PSAP.
8\. The emergency call establishment is completed.
9\. The PSAP may send a location request to the LRF to get the initial
location information for the target UE, or to request LRF to get updated, i.e.
current, location information for the target UE. The PSAP may determine the
LRF based on the location and/or correlation information received in step 7.
The PSAP may also include the correlation information in the request to the
LRF. **_In the case of an IP capable PSAP, the location request may take the
form of a location dereference request -- e.g. a SIP SUBSCRIBE [IETF RFC 3856
[7]) or HELD request (IETF draft-winterbottom-geopriv-deref-protocol-00 [9])
\-- and may then include the location URI received in step 7._**
10\. The LRF determines the target UE\'s location using one of the means
listed in step 5 above. The LRF may use the correlation information received
in step 9 to retrieve information about the UE that was stored in step 5.
11\. The LRF returns the initial or updated location information to the
emergency centre or PSAP. As an option for initial location, the LRF may
instigate the location step 10 before the request in step 9 is received and
may send the initial location to the emergency centre or PSAP either after the
request in step 9 is received or before it is received. **_In the case of a
location dereference request from an IP capable_** **_PSAP in step 9, the LRF
may provide the appropriate location dereference response. In the case of
location dereference using a SIP SUBSCRIBE request in step 9, this would take
the form of a SIP NOTIFY (as defined in IETF draft-ietf-sip-location-
conveyance-09 [5] and IETF RFC 3856 [7]) which would be sent whenever the LRF
has new location information for the UE. In the case of a location dereference
using a HELD request (IETF draft-winterbottom-geopriv-deref-protocol-00 [9]),
this would take the form of a HELD response containing the location value
obtained in step 10._**
12\. The emergency call is released.
13\. The IMS core may indicate to the LRF that the call is released. The LRF
deletes any record stored in step 5.
### 6.4.4 Evaluation
The extensions to location retrieval that need to be supported by an LRF are
consistent with what is already defined in TS 23.167. Mainly, the rather vague
"correlation information" specified in 23.167 is now replaced by specific
types of location URI used by IETF and location retrieval by the PSAP uses
specific IETF dereference capabilities. It is not yet clear whether IETF will
allow several types of location URI and dereference protocols and, if so,
which these will be. A possible way forward is proposed to include what is
defined in existing RFCs and drafts. But it is possible that one specific type
of location URI and dereference protocol might be agreed later for 3GPP use
(in which case the changes to TS 23.167 can be more specific than what is
defined in this TR).
## -
## -
# 7 Conclusions
#