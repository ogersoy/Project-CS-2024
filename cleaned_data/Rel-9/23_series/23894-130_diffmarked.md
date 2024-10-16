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
Due to the increasing volume of data traffic exchanged by mobile users and the
rapid decrease of roaming rates that is being imposed by the regulator, mobile
operators will most likely have to revisit their roaming agreements, moving
towards a more extensive usage of local breakout. This will allow to reduce
the cost per bit of data traffic exchanged by roaming customers, since at
least part of it will be handled directly by the visited operator, with no
need to waste bandwidth on the international links between home and visited
networks; moreover, local breakout would allow to offer better performance to
the customers.
Based on the analysis of the requirements on local breakout and on the
increasing number of the services controlled by IMS that operators are
expected to face, it has been proposed that system enhancements are needed to
enable extensive usage of IMS services in local breakout.
Furthermore, international communications and terminal roaming introduce a
number of scenarios where sessions may traverse multiple IMS networks. The use
of Border Control Function makes both the signalling and bearer path traverse
through the same networks path and could make the media path not optimized.
In order to ensure Quality of Service (QoS) and, in certain cases, minimal
routeing costs, there is a need to enable the routeing of media traffic via an
optimal path between those networks, without necessarily being linked to the
path that the signalling flow needs to take. The optimal media path between
two endpoints may involve IP transit networks, which in normal circumstances
are not included in the SIP signalling path. Current QoS reservation is
negotiated based on the SIP pre-conditions model, and hence the lack of SIP
signalling in the transit network presents a problem for the negotiation of
QoS between the end-points.
# 1 Scope
This study intends to investigate the general problem of system enhancements
for the use of IMS services in local breakout and optimal routeing of media.
In particular the above issues will be addressed identifying
\- solutions for the home operator to control
\- whether the IMS user may connect to a PDN in the visited network, and
\- whether connections to PDNs provided from the home and visited network may
exist in parallel;
\- solutions to enable the IMS network to be aware of whether local breakout
can be invoked or not;
\- solutions to allow the home operator to determine which of the IMS sessions
(for a given UE) can be handled in local breakout and which in home routed
mode, and what information (e.g. operator\'s policies, customer\'s
subscription profile, UE connectivity, and location of the remote end
terminal/service) is needed for the decision;
\- solutions to allow the UE to concurrently use IMS services through local
breakout and other IMS services through home routeing;
\- the feasibility of having the local breakout option in IMS service nodes:
\- is there a need for a P-CSCF at both PDN accesses?
\- if one P-CSCF is enough, what requirements are there for connectivity
between the PDNs?
\- if methods are necessary to discover an additional P-CSCF in the visited
network after the UE has moved to the visited network, even if the network-
layer mobility mechanisms can sustain IP connectivity to the previously
discovered P-CSCF in the home network;
\- the exact location of the decision point in the home network whether to use
local breakout (application or delegated to IP-CAN);
\- solutions for SIP/SDP signalling related to the use of IMS services through
local breakout.
\- interactions with network entities such as NAT (as specified in TS 23.228
[8]) when providing IMS services through local breakout;
\- interactions with and support of PCC to provide IMS services through local
breakout;
\- security implications if there is need for multiple P-CSCFs per UE.
Moreover:
\- describing a set of scenarios where the selection of an alternative media
path (i.e., different to the signalling path) provides benefits to IMS
operators by reducing the number of network entities in the media path;
\- providing requirements for suitable mechanisms to achieve optimal media
routeing;
\- analysing the potential solution(s) to solve those scenarios in line with
IMS procedures, while taking into account any impact of extensions required to
existing functions/procedures (e.g., NAT, transcoding, Security, PCC, BCF, LI,
etc.);
\- reducing the number of options for solving the same requirement and agree
on a preferred solution.
In the end this study will provide conclusions with respects to what further
specification work is required in order to fulfil the requirements for the use
of IMS services through local breakout and achieve optimal routeing of media.
# 2 References
The following documents contain provisions which, through reference in this
text, constitute provisions of the present document.
  * References are either specific (identified by date of publication, > edition number, version number, etc.) or non‑specific.
  * For a specific reference, subsequent revisions do not apply.
  * For a non-specific reference, the latest version applies. In the > case of a reference to a 3GPP document (including a GSM document), > a non-specific reference implicitly refers to the latest version > of that document _in the same Release as the present document_.
[1] 3GPP TR 21.905: \"Vocabulary for 3GPP Specifications\".
[2] 3GPP TS 22.258: \"Service requirements for the AIPN\".
[3] 3GPP TS 22.278: \"Service requirements for evolution of the 3GPP system\".
[4] 3GPP TS 23.401: \"GPRS enhancements for E-UTRAN access\".
[5] 3GPP TS 23.402: \"Architecture enhancements for non-3GPP accesses\".
[6] 3GPP TS 23.203: \"Policy and charging control architecture\".
[7] GSMA PRD IR.34: \"Inter-Service Provider IP Backbone Guidelines\".
[8] 3GPP TS 23.228: \"IP Multimedia Subsystem (IMS)\".
# 3 Definitions and abbreviations
## 3.1 Definitions
For the purposes of the present document, the definitions given in TR 21.905
[1] and the following apply:
**IP gateway:** The node in the operator\'s network that is responsible for
allocating an IP address to a subscriber.
## 3.3 Abbreviations
For the purposes of the present document, the abbreviations given in TR 21.905
[1] and the following apply. An abbreviation defined in the present document
takes precedence over the definition of the same abbreviation, if any, in TR
21.905 [1].
EPC Evolved Packet Core
EPS Evolved Packet System
GW GateWay
IP Internet Protocol
P-CSCF Proxy-Call Session Control Function
SDP Session Description Protocol
UE User Equipment
LBO Local Breakout
OMR Optimal Media Routeing
# 4 Overall Requirements
The overall requirements to provide IMS services through local breakout are
defined in TS 23.401 [4].
# 5 Architectural Requirements and Assumptions
The following general architecture principles shall be used when developing
solutions for LBO and OMR:
\- Radio impacts/Access network procedures like IDLE mobility should not be
affected;
\- S-CSCF is the service control entity for IMS, as per current IMS core
principle; even though media may be routed according to LBO or OMR procedures;
(except for emergency case where E-CSCF is used as described in TS 23.167);
\- Backward compatibility with Rel-7 (e.g. Rel-8 Terminal shall be able to
connect to a Rel-7 IMS system and Rel-7 terminal shall be able to connect to
Rel-8 IMS) shall be maintained and impacts from the development within Rel-8
IMS system shall be addressed before reaching final conclusion;
\- UE battery consumption and complexity/cost of impacts must be considered;
\- An UE shall not use the same IP address simultaneously across multiple
accesses;
\- Any solution(s) developed should work in single PLMN scenario as well as
roaming scenarios.
NOTE: According to current specifications, LBO can not be used when GPRS-IMS
Bundled Authentication is used.
In addition to the general requirements above, the following requirements
shall be used when developing solutions for Optimal Media Routeing (OMR):
\- OMR shall apply to IMS systems that use IBCF and TrGW for interconnection.
\- OMR shall establish an optimal media path for each of the media streams of
an IMS session, subject to the Home operator\'s policy, system constraints
(such as transcoding function location) and the information available within
SIP signalling;
\- All media components of a session that traverse the same un-optimized
sequence of IBCFs/TrGWs and networks shall, subject to Home operators\'
policy, traverse the same optimized sequence of IBCFs/TrGWs and networks. This
ensures similar end to end path delay characteristics for media components
that may be synchronized;
\- Where end points are located within the same residence or enterprise
network, OMR should be able to support the routeing of the media path such
that it does not egress that network;
\- OMR should be capable of optimizing the media paths for a session where the
same interconnect network is used for multiple legs of the un-optimized media
path;
\- OMR should be capable of optimizing the media paths for a session between
two UEs where the same serving network is used by the UEs;
\- Home operators (of both calling and called UE) may be informed, upon
session establishment/modification, of the successful enforcement or removal
of OMR for that session;
\- On session establishment, OMR shall establish an optimal media path
separately for each remote endpoint of the session;
\- OMR should re-establish an optimal media path for a session in the event of
session modification (SDP offer/answer exchange);
\- Impacts on IMS shall be minimized. Solutions should be based on existing
IMS functional entities, use existing message flows and avoid the addition of
new protocols or new messages between network elements;
\- A single bandwidth reservation mechanism shall be used (for both roaming
and non-roaming cases and for optimized and non-optimized sessions);
\- Entities in one network shall not need to be aware of the internal
structure of other networks;
\- The routeing of media within a network shall not be constrained by OMR;
\- OMR shall not be dependant on the direct peering of policies across a
network boundary. No peering of Policy and Charging Rules Function (PCRF) [6]
across network boundaries shall be required (since this does not represent a
likely commercially acceptable solution);
\- The service disruption of an on-going session when establishing OMR should
be minimised;
\- The impacts of OMR on the transport layers shall be minimised;
\- The effects of introducing OMR on EPS shall be minimised;
\- OMR shall provide mechanisms supporting media optimizations across multiple
transit networks supporting homogenous interconnect agreements (e.g. IPX [7]);
\- The originating or terminating networks shall be able to apply OMR on a
session by session basis (e.g. for lawful intercept reasons, for media streams
that need transcoding, or for services that require announcements to be played
from the home network);
# 6 Scenarios and Solutions for local breakout
## 6.1 Scenarios
Editor\'s Note: PCC considerations are for FFS in following the scenarios.
### 6.1.1 P-CSCF located in home network -- dual IP address
The user has the subscription through home operator H. The user is roaming and
is currently served by a different operator. Figure 6.1.1-1 shows the
signalling and media paths for this scenario. In this scenario, the UE uses
two distinct IP addresses, one for IMS signalling and one for media. The IP
address allocated by the home network is used for IMS signalling and the IP
address allocated by the local IP gateway in the serving network is used for
the media.
NOTE: The scenario where both IP addresses (e.g. one from home network and one
from local IP gateway) are identical (e.g. overlapping private IP address) is
out of the scope of this study.
Figure 6.1.1-1: P-CSCF located in home network -- dual IP address
Before starting IMS sessions, the UE sets up IP connectivity. In this
scenario, the UE roams to a local access network, is assigned an IP gateway
(GW-H) in the operator H\'s network and obtains an IP address (IP-H).
Regarding the establishment of connectivity to the local IP gateway for local
breakout, the UE can set up IP connectivity with the local IP gateway before
IMS registration based on policies pre-configured on the UE. In this case, the
UE is assigned an IP gateway (GW-L) in the local network and obtains an IP
address (IP-L) for local breakout of IMS sessions. After that, the UE
discovers a P-CSCF in the operator H\'s network and performs IMS registration.
Alternatively, the UE performs IMS registration before establishing
connectivity with a local IP gateway, and upon indication by the IMS, it sets
up IP connectivity with the local IP gateway.
Editor\'s Note: The method for indication by the IMS is FFS.
When the user wishes to establish an IMS session with another user and this
session uses local breakout, the UE indicates, in the SDP offer, IP-L as the
address to which media is to be sent. Operator H authorizes the use of local
breakout for the user for this session. The other user accepts the offer and
indicates its own IP address as the address to which media is to be sent.
After the IMS session is established, the media does not traverse through the
network of operator H, but is handled by the local IP gateway in serving
operator\'s network.
This scenario permits the home operator to exercise control over the
utilization of local breakout on a per IMS session basis.
This scenario is also applicable when operator H provides service over a large
geographic area. The main difference from the above is that the GW-L will be
in operator H\'s administrative domain and may even have IP connectivity to
the P-CSCF.
### 6.1.2 P-CSCF located in home network -- single IP address
The user is roaming and is currently served by the operator L. Figure 6.1.2-1
shows the signalling and media paths for this scenario. In this scenario, the
UE uses the same IP address for both IMS signalling and the media. This IP
address is allocated by the local IP gateway in the serving network.
Figure 6.1.2-1: P-CSCF located in home network -- single IP address
The UE discovers an IP gateway (GW-L) in the operator L\'s network and obtains
an IP address (IP-L). Then the UE discovers a P-CSCF in the operator H\'s
network and performs IMS registration.
The user wishes to establish a session with another user and indicates, in the
SDP offer, IP-L as the address to which media is to be sent. The other user
accepts the offer and indicates its own IP address as the address to which
media is to be sent.
After the session is established, the media does not traverse through the
network of operator H, but is handled by the local IP gateway in the serving
operator\'s network.
This scenario assumes that the operator H has authorized the UE to utilize
local breakout for all the IMS sessions.
Some non-3GPP IMS networks provide the capability to locate the P-CSCF in the
home network even when the UE is roaming.
### 6.1.3 P-CSCF located in serving network
The user has the subscription through home operator H. The user is roaming and
is currently served by operator L. Figure 6.1.3-1 shows the signalling and
media paths for this scenario. In this scenario, the UE uses the same IP
address for both IMS signalling and media. This IP address is allocated by the
IP gateway (GW-L) in the serving network.
Figure 6.1.3-1: P-CSCF located in serving network
The UE discovers an IP gateway (GW-L) in the serving operator\'s network and
obtains an IP address (IP-L). Then the UE discovers a P-CSCF in the serving
operator\'s network and performs IMS registration.
The user wishes to establish a session with another user and indicates, in the
SDP offer, IP-L as the address to which media is to be sent. The other user
accepts the offer and indicates its own IP address as the address to which
media is to be sent.
After the session is established, the media does not traverse through the
network of the home operator, but is handled by the local IP gateway in the
serving operator\'s network.
This scenario assumes that the operator H has authorized the UE to utilize
local breakout for all the IMS sessions.
## 6.2 Alternative 1: Dual IP address
### 6.2.1 Description
In this scenario, there are two PDN GWs:
\- PDN GW1 used for anchoring of SIP signalling and IMS bearer traffic; it is
located in the Home network;
\- PDN GW2 used for anchoring of IMS bearer traffic and located in the Visited
network.
For the sake of simplicity, only 3GPP access and trusted non-3GPP access is
depicted in Figure 6.2.1-1. S7c is present only with PMIP-based S8 (S8b).
Figure 6.2.1-1: Local Breakout for IMS services with Dual IP addresses
From EPS perspective this looks like concurrent access to Multiple PDNs.
S9 is used in order to provide PCC rules to the vPCRF function in the Visited
network, which then distributes the PCC information towards PDN GW2 via S7. In
addition, in case of PMIP-based S8, S9 is also used for conveyance of QoS
rules to the Serving GW or the trusted non-3GPP access via S7c and S7a,
respectively.
Inter-PLMN handovers are supported by re-assigning a new PDN GW2 in the target
VPLMN (note that PDN GW1 is not re-assigned).
For intra-PLMN handovers involving Serving GW change it may be possible to
defer the re-assignment of a new PDN GW2 until the completion of any ongoing
calls.
Figures 6.2.1-2 and 6.2.1-3 illustrates the two types of handovers involving
Serving GW relocation:
Figure 6.2.1-2: Handover involving Serving GW relocation: PDN GW2 relocation
is postponed until there are no ongoing RT sessions
In Figure 6.2.1-2 the Serving GW is relocated while keeping the original PDN
GW2. This is achieved by instantiating an S5 interface between the target
Serving GW and the original PDN GW2. The bearer path after handover in this
approach may thus not be optimised, however the advantage of this approach is
that it minimises the service break, which is in particular important for real
time traffic (e.g. VoIP). Once the ongoing VoIP sessions are terminated, it
should be possible for the network to trigger a streamlining procedure by
which the old PDN GW2 is released and a new PDN GW is assigned in order to
optimise the bearer path for future VoIP sessions.
In Figure 6.2.1-3 the visited PDN GW (PDN GW2) is relocated at the same time
as the Serving GW. This would typically be the case in inter-PLMN handovers.
In this approach a new visited PDN GW (PDN GW3) is assigned, which implies a
new IP address for the bearer plane (hosted on SGi 3), as well as relocation
of the S7/S7c legs.
Editor\'s Note: The change of local IP address requires that the UE shall send
a re-INVITE (or UPDATE) to the remote party to inform of the new media stream
IP address for any established media streams using local breakout. The service
interruption in the Figure X3 case is therefore longer than in the Figure X2
case. Nevertheless, as SA2 has already pointed out in a liaison reply to RAN3
(S2-062566): \"However SA2 believe that MME/UPE relocation should be a
relatively infrequent event, and does not need to have the same performance as
intra-UPE handover, which should be the main way of supporting intra-LTE
handover\".
Figure 6.2.1-3: Handover involving Serving GW relocation: the visited PDN GW
(PDN GW2) is relocated at the same time (e.g. Inter-PLMN handover)
### 6.2.2 Impact on IMS
Rel-7 IMS supports the usage of different IP addresses for the SIP signalling
and for the bearer traffic, so there is no IMS impact from that perspective.
The decision on whether a particular IMS media stream should be home routed or
routed in local breakout is made by the IMS in the home network. How this is
achieved is FFS.
It is FFS whether the IMS in the home network indicates to the UE upon
registration whether it needs to establish connectivity with a local PDN GW
for local breakout.
### 6.2.3 Impact on EPS
It is FFS whether the two PDN connections can be set up as part of the Attach
procedure.
Among the two approaches for NAT traversal described in TS 23.288, only the
ICE and Outbound approach is applicable for the IMS bearer traffic breaking
out of the visited PDN GW (PDN GW2), given that in this solution the P‑CSCF is
assigned in the home network.
It is FFS whether and how EPS is involved in dynamic decisions on whether a
particular IMS session should be home routed or broken out locally.
### 6.2.4 Impact on UE
How the IMS client in the terminal is instructed about the usage of the two IP
addresses is FFS. For example, the IMS client in the terminal may be
instructed about the usage of the two IP addresses either based on the pre-
configured policy or during the IMS registration.
In case of handover involving PDN GW change (e.g. inter-PLMN handover), the
IMS client may have to manage the change of the IP address in the bearer plane
(e.g. by sending SIP re-INVITE to the remote party).
## 6.3 Comparison of the scenarios
The following table summarizes the differences between the three scenarios and
identifies areas where additional work is needed.
* * *
                                              Dual IP address                                                                                                                                  Single IP address - Home P-CSCF                    Single IP address - Visited P-CSCF
Number of IP addresses obtained by the UE 2 1 1 IMS signalling anchored in the
Home Yes No No NAT traversal for media ICE/Outbound ICE/Outbound IMS ALG or
ICE/Outbound Serving network support of IMS Not needed Not needed Needed PCC
impact FFS None S9 may need to include both Rx and Gx functionality (FFS) UE
impact Handling of two IP addresses None None IMS impact Indication for
establishment of local PDN connectivity during IMS registration (FFS);
Decision about Local Breakout on per-session basis (FFS) Procedures for
discovery of a P-CSCF in the home None Other EPS impact Establishment of
additional PDN connectivity upon Attach (FFS) None None
* * *
NOTE: The Dual IP address scenario allows for co-existence of IMS signalling
anchored in the home network, along with media streams anchored in the home
network, in the visited network or in both.
# 7 Scenarios and Solutions for optimal routeing of media
Editor\'s Note: This section i) will identify the possible scenarios where the
selection of an alternative media path (i.e. different to the signalling path)
provides benefits to IMS operators by reducing the number of network entities
in the media path and ii) will document the detailed reference architectures,
including network elements, interfaces and reference points, suitable to carry
out the identified scenarios.
## 7.1 Scenarios
The following scenarios are considered to be priority for OMR:
a) UE A and UE B are in the same visited network.
b) The visited networks of UE A and UE B are close by (e.g. same
country/area).
c) UE A is visiting the home network of UE B or vice versa.
d) UE A is visiting a close by network of the Home of UE B or vice versa.
e) UE A is in a visited network and connects to UE B via PSTN gateway in the
same visited network.
Where Close-by above is limited to cases of direct interconnect (or indirect
interconnect with similar properties, such as transparent mode).
Optimizations of scenarios that traverse the same network multiple times on
the path could be considered but with lower priority.
NOTE: Using interconnects without direct interconnect property can impose
problems e.g. due to intermediate proxies, which may have properties impacting
potential solution that cannot be foreseen.
## 7.2 Alternative 1: Extension to SDP for TrGW bypass
### 7.2.1 Introduction
The IP Multimedia Subsystem has the option to deploy TrGWs between the IP
realms defined by each network. Within an IP realm every endpoint is reachable
from any other endpoint using a common address space. Each of these TrGWs
typically provides a firewall or Network Address Port Translator (NAPT) to
limit access to endpoints within a realm. An Interconnection Border Control
Function (IMS-ALG) controls each TrGW to allocate new IP addresses and ports
as necessary for each SDP media line and updates the SDP connection and port
information in each forwarded SDP offer and answer to effectively insert the
TrGW into each end-to-end multimedia stream.
The media path associated with a multimedia stream may traverse an arbitrary
number of IP realms between endpoints. If the TrGWs in the media path only
have connections to its directly connected IP realms on the media path then
the media path cannot be optimized using the allocated TrGW resources.
However, if either of the endpoints, or any TrGW on the path, also has direct
access to one of the other IP realms on the path then a shorter media path
exists.
A sequence of IMS-ALGs implementing the proposed procedures (where each IMS-
ALG can determine the IP address and port information for entities on the
media path in its interconnected IP realms) will be able to establish a media
path with the minimum number of TrGWs without compromising any of the access
controls associated with the TrGWs on the path.
If one or more IMS-ALGs on the signalling path do not implement these proposed
procedures then some TrGW bypass can still occur but some potentially
bypassable TrGWs may remain in the media path.
This solution works by adding information to existing SDP offer/answer
messages. It is thus an extension to SDP and builds on IMS-ALG/TrGW NAT
traversal.
The solution requires two SDP extension attributes and some extensions to IMS-
ALG procedures for forwarding SDP offers and answers. IMS-ALGs on the path
manipulate the SDP as necessary within a single end-to-end SDP offer/answer
transaction to minimize the number of TrGWs on the end-to-end media path. The
SDP extension attributes describe media connection and port information for
each IP realm on the path that is a candidate to bypass one or more TrGWs on
the path.
The base algorithm, while requiring the use of IMS-ALGs, has the following
advantages:
\- avoids the need to deploy STUN servers.
\- requires no additional signalling beyond what is needed for a single end-
to-end SDP offer/answer transaction.
\- applies independently to each media stream established by an SDP
offer/answer transaction.
\- applies to media streams established between any types of endpoints (e.g.,
UEs, media servers, media gateways).
\- applies to media streams established using SIP 3pcc procedures.
\- requires no new procedures to be supported by endpoints.
\- allows TrGWs to limit access to known IP source addresses.
\- allows TrGWs to predictably manage aggregate bandwidth usage for all
sessions.
It should also be noted that this solution can still provide optimization of
the media path, even if not all of the networks involved in the signalling
path have deployed TrGWs. As long as at least two TrGWs have been deployed the
algorithm may be able to optimize the media path. If only one TrGW is
deployed, no optimization is possible.
Within the context of the base algorithm, an IMS-ALG may also include
information about secondary TrGWs that may provide additional opportunities
for optimization.
In addition to the base algorithm, an \"active-bypass\" option is also
described. This provides the ability to attempt to find a shorter media path
segment between existing TrGWs associated with the path. This option shares
most of the advantages of the base algorithm, but requires additional SIP
signalling to establish a SIP dialog for each alternate media path segment
candidate. Due to this additional signalling overhead, this option should only
be used when it can be determined that dramatic improvement is possible for a
media path segment.
### 7.2.2 Reference Architecture
The following figures show existing 3GPP architecture figures. In the
description of this solution the term IMS-ALG has been used, rather than
referring to IBCFs or P-CSCFs. The first figure is taken from Annex I of TS
23.228 [8], and shows the IMS Border Control Functions.
Figure 7.2.2-1: Border Control Functions
In addition, TS 23.228 [8] Annex G contains NAT traversal reference models as
shown below:
Figure 7.2.2-2: Reference model for IMS access when both the signalling and
media traverses NAT
Figure 7.2.2-3: Reference model for IMS access when NAT is needed between the
IP-CAN and the IMS domain
### 7.2.3 Description of base algorithm
#### 7.2.3.1 Overview
Figure 7.2.3.1-1 shows a typical call configuration between endpoints UE1 and
UE2, where the SIP signalling goes between the UEs via at least one IMS-ALG
(four are shown) and other SIP servers not shown, and one RTP multimedia
stream goes between the UEs via the TrGWs and possibly a residential
gateway/NAT (RG) associated with each UE (only one RG is shown associated with
UE2). Each TrGW is controlled by its corresponding IMS-ALG. R1, R2, etc., in
the figure represent the IP realms associated with each segment of the media
path.
The media path for each multimedia stream between the UEs is established via
an end-to-end SDP offer/answer exchange where each IMS-ALG may choose to
modify the connection and port information associated with each media line in
the SDP to insert its TrGW in the media path according to normal IMS-ALG
procedures. Each IMS-ALG may also identify when one or more TrGWs and/or RGs
can be bypassed and to modify the forwarded SDP messages to implement the
corresponding changes in the media path to bypass the TrGWs.
The example in figure 7.2.3.1-1 shows UE1 and UE2 as the endpoints for a
single media stream, but the algorithm applies independently to each media
stream (media line) established by an SDP offer/answer transaction, and to any
combination of media stream endpoints including UEs, media servers and media
gateways, even when the SDP offer/answer transactions are interworked between
SIP dialogs using SIP 3pcc procedures.
Figure 7.2.3.1-1: Example Call Configuration
The TrGW bypass base algorithm assumes that ICE is not used by any entity in
the architecture. Although hybrid procedures are possible, they are beyond the
scope of this document.
It is assumed that the UAs participate in standard SDP offer/answer
negotiation by presenting standard connection and port information for each
media line according to RFC 4566 [x], RFC 3264 [x] and possibly other
extensions.
The TrGW bypass base algorithm is only implemented by the IMS-ALGs, also
considering the reference model shown in Figures 7.2.2-2 and 7.2.2-3. A basic
assumption for the algorithm is that IMS-ALGs are pre-configured with a list
of peer networks, which allow the optimization of the media path. The
procedures have no impact on any aspect of SDP offer/answer negotiation other
than the connection and port information associated with each media line.
An SDP extension attribute \'visited-realm\' provides connection and port
information for an IP realm on the signalling path associated with a single
media line. Each instance of visited-realm associated with a media line has a
unique instance number, a realm identifier, connection/port data, and optional
cryptographic signature computed using an algorithm private to each IP realm
so as to ensure the integrity of the visited-realm data. There may be a
separate visited-realm attribute inserted in the SDP for each media line and
for each unique IP realm visited during an SDP offer/answer transaction.
Pre-configuration of the IMS-ALGs with a list of peer networks allows for
simplification of the base algorithm, based on realm information.
The realm attributes in received offers assist IMS-ALGs in the determination
of TrGWs to be bypassed. Upon inspection of the realm attribute, IMS-ALGs may
decide on the TrGW allocation.
If an IMS ALG decides that previous TrGWs can be bypassed, it indicates this
to their controlling IMS-ALGs based on the realm identifier in the SDP answer.
For example in Figure 7.2.3.1-1, if IMS-ALG2 is an egress node and IMS-ALG4 is
an ingress node in the same domain, based on the SDP offer/answer transaction
IMS-ALG4 will detect a media path optimization based on the detection of the
realm identifier in the realm attribute, determining that TrGW controlled by
intermediate nodes (i.e. IMS-ALG3, IMS-ALG2), as well as its own can be
bypassed and unnecessary resources can be released.
Note that the connection and port information in each SDP offer/answer
transaction within a SIP dialog must be handled the same way, re-allocating
and de-allocating TrGWs as necessary with each SDP offer/answer transaction to
accommodate any potential changes in the IP realms associated with the session
endpoints.
#### 7.2.3.2 Use of secondary TrGWs
Figure 7.2.3.2-1 shows another example call configuration where secondary
TrGWs are used to establish a media path with fewer TrGWs. IMS-ALG1 through
IMS-ALG5 initially allocate TrGW1a, TrGW2, TrGW3, TrGW4 and TrGW5a as IMS-ALGs
forward the initial SDP offer towards UA2 from UA1. These TrGWs enable
traversal of unique IP realms R1 through R6 (not labelled in the figure).
Since these TrGWs do not create any loop in the media path, it is not possible
to bypass any of them if the algorithm is limited to finding loops in a fixed
media path.
Figure 7.2.3.2-1: Example Configuration using Secondary TrGWs
While forwarding the initial SDP, if an IMS-ALG along the way, such as IMS-
ALG1, controls TrGW(s) that have access to IP realm(s) other than those IP
realms that it controls on the default media path (i.e. not R1 or R2), then
the IMS-ALG can advertise its ability to access additional IP realm(s) by
including information about them in the forwarded SDP.
An SDP extension attribute \'secondary-realm\' is also proposed that provides
connection and port information for secondary IP realms associated with the
signalling path. The secondary-realm attribute includes the same types of
information as the visited-realm attribute.
If a subsequent IMS-ALG (e.g., IMS-ALG5) determines that it controls a TrGW
(e.g. TrGW5b) that has a direct connection to an IP realm accessible from a
TrGW controlled by a previous IMS-ALG in the path (e.g., IMS-ALG1 and TrGW1b),
then the IMS-ALG may choose to use this alternative media path if it appears
to be an improvement over the initial path. In this example, the algorithm
establishes an alternative media path from UA1 to UA2 via TrGW1b and TrGW5b
while significantly reducing the number of TrGWs traversed. Note that the IP
realm between TrGW1b and TrGW5b in the example (R7) will not match any of the
IP realms R1 through R6. If the connections exist, the algorithm may also
generate alternative paths either via TrGW1a and TrGW5b, via TrGW1b and
TrGW5a, or via TrGW1a and TrGW5a, for example (not shown).
#### 7.2.3.3 Procedures and call flows
##### 7.2.3.3.1 Example flow for base algorithm
Figure 7.2.3.3.1-1 shows a call flow that corresponds to the configuration in
figure 7.2.3.2-1.
{width="6.972916666666666in" height="2.4652777777777777in"} Figure
7.2.3.3.1-1: Example Flow with base algorithm
Steps 1a to 1f describe the progression of SDP offers via the IMS-ALGs from
UA1 to UA2 and steps 2a to 2f describe the corresponding progression of SDP
answers according to the base algorithm.
1a. UE1 (or other SIP user agent) sends an SDP offer associated with a
controlled media resource.
1b. IMS-ALG1 determines that the outgoing IP realm is different from the
incoming IP realm and allocates a TrGW for each media line based on existing
procedures. The IMS-ALG1 adds visited-realm attributes for the incoming and
outgoing IP realms to the forwarded SDP for each media line and changes the
connection information in the forwarded SDP to match the allocated TrGW. The
IMS-ALG1 may allocate secondary TrGWs for alternate outgoing IP realm options
for each media line and add the corresponding secondary-realm attributes to
the forwarded SDP. No TrGWs are bypassed.
1c. If IMS-ALG2 determines that the outgoing IP realm is different from all
visited-realm and secondary-realm attributes associated with a media line, and
the IMS-ALG2 controls no TrGW with access to an earlier visited-realm or
secondary-realm, it allocates a TrGW for the media line based on existing
procedures. The IMS-ALG2 adds a visited-realm attribute for the outgoing IP
realm to the forwarded SDP for the media line and changes the connection
information in the forwarded SDP to match the allocated TrGW. The IMS-ALG2 may
allocate secondary TrGWs for alternate outgoing IP realm options for each
media line and add the corresponding secondary-realm attributes to the
forwarded SDP. No TrGWs are bypassed.
If IMS-ALG2 determines that the outgoing IP realm matches a visited-realm or
secondary-realm attribute associated with the media line, it deletes any
visited-realm and secondary-realm attributes for the media line with instance
number greater than the matching attribute and changes the connection
information in the forwarded SDP to that of the matching attribute. Note that
the IMS-ALG2 does not allocate a TrGW, effectively bypassing its own TrGW and
zero or more previous TrGWs.
If IMS-ALG2 determines that it controls a TrGW with access to an earlier
visited-realm or secondary-realm associated with a media line, it allocates
the TrGW, deletes any visited-realm and secondary-realm attributes for the
media line with instance number greater than the matching attribute, and
changes the connection information in the forwarded SDP to that of the
allocated TrGW. Note that the IMG-ALG2 effectively bypasses one or more
previous TrGWs.
1d through 1f. Each subsequent IMS-ALG applies the same algorithm as IMS-ALG2
in step 1c.
2a. UE2 (or other SIP user agent) responds to the received SDP offer by
sending an SDP answer with a media line associated with a controlled media
resource. UE2 ignores visited-realm and secondary-realm attributes for the
media line in the received SDP offer.
2b. If IMS-ALG5 previously allocated a TrGW for the media line and bypassed no
previous TrGWs for the media line when previously handling the SDP offer, it
changes the connection information for the media line in the forwarded SDP
answer to that of the allocated TrGW.
If IMS-ALG5 previously bypassed its own TrGW and zero or more previous TrGWs
for a media line when previously handling the SDP offer, it adds a visited-
realm attribute for the previous connected IP realm to the media line in the
forwarded SDP answer, and changes the connection information for the media
line in the forwarded SDP answer to the unspecified address.
If IMS-ALG5 previously allocated a TrGW for a media line and bypassed one or
more previous TrGWs for the media line when previously handling the SDP offer,
it adds a visited-realm attribute for the incoming side of the allocated TrGW
to the media line in the forwarded SDP answer, and changes the connection
information for the media line in the forwarded SDP answer to the unspecified
address.
2c. If IMS-ALG4 receives valid connection information for the media line in
the received SDP answer, it applies the same algorithm as IMS-ALG5 in step 2b.
If IMS-ALG4 receives the unspecified address as the connection information for
a media line in the received SDP answer, and the visited-realm for the media
line in the received SDP answer matches the incoming IP realm for the media
line of the previously received SDP offer, it changes the connection
information for the media line in the forwarded SDP answer to the connection
information in the visited-realm for the media line from the received SDP
answer. IMS-ALG4 now de-allocates and bypasses its TrGW if it has not already
done so.
If IMS-ALG4 receives the unspecified address as the connection information for
a media line in the received SDP answer, and the visited-realm for the media
line in the received SDP answer matches an earlier visited-realm or secondary-
realm previously received in the SDP offer, it forwards the received SDP
answer for the media line without change. IMS-ALG4 now de-allocates and
bypasses its TrGW if it has not already done so.
2d and 2e. Each subsequent IMS-ALG applies the same algorithm as IMS-ALG4 in
step 2c.
2f. IMS-ALG1 applies the same algorithm as IMS-ALG4 in step 2c, but always
forwards valid connection information for each media line in the forwarded SDP
answer, since IMS-ALG1 never bypasses itself during the previous processing of
the SDP offer for the media line. The TrGW associated with IMS-ALG1 may or may
not be bypassed depending on which case applies.
### 7.2.4 Description of active bypass option
#### 7.2.4.1 Overview of Operation of the Active-Bypass Option
The Active-Bypass option can be used in addition to the proposal described
above to discover alternative paths not discovered by the base algorithm.
Figure 7.2.4.1-1 shows an example of the use of the base algorithm with the
active-bypass option. If the initial TrGW allocations traversing IP realms R1
through R6 do not offer an opportunity to bypass any TrGWs (as in figure 2),
and if no connections exist to offer any of the alternative options available
in the base algorithm, then the active-bypass option can discover additional
alternative(s). Note that in this case TrGW1b and TrGW5b do not share a common
IP realm (in fact, all of the IP realms are different in this example), so the
active-bypass option creates a new signalling path via IMS-ALG6 to establish a
new media path segment via TrGW6.
Figure 7.2.4.1-1: Example Configuration with Active-Bypass Option
When implementing the active-bypass option, the following additional
information may be included in each visited-realm and secondary-realm
attribute generated by the base algorithm for an SDP offer, if available: the
approximate geo-location of the corresponding TrGW; the approximate delay of
IP packets on the previous media path segment between this TrGW and the
immediately preceding TrGW or endpoint; the approximate packet loss rate on
the same media path segment; and if the IMS-ALG is reachable via a globally
unique host name, then a globally reachable address of the IMS-ALG with a
unique instance id for the corresponding SIP dialog and media line, in the
form of a temporary GRUU [8].
Each IMS-ALG should include the geo-location, delay and loss information in
the first visited-realm attribute that it generates for an SDP offer, and may
include them for other visited-realm or secondary-realm attributes if the
information differs significantly from the first. Each IMS-ALG may include the
GRUU in the first visited-realm attribute that it generates for a media line
in an SDP offer. There is no need to repeat the GRUU in subsequent visited-
realm or secondary-realm attributes for the same media line.
When processing the SDP answer in the second phase of the base algorithm,
after determining which TrGWs (if any) are to be bypassed as a result of the
base algorithm, each IMS-ALG that still controls a TrGW determines if there is
the possibility that a significantly shorter media path segment can be
established via another IMS-ALG reachable via a GRUU. Each IMS-ALG makes this
determination based on the available geo-location, delay and packet loss
information associated with each TrGW and media path segment.
If an IMS-ALG determines that it may be able to establish a shorter media path
segment, the IMS-ALG (e.g., IMS-ALG5) sends a SIP INVITE request to the
\"best\" IMS-ALG reachable via a GRUU (e.g., IMS-ALG1) to establish a separate
dialog and corresponding alternate media path segment (e.g., via IMS-ALG6 and
TrGW6). If the IMS-ALG is successful in establishing the alternate media path
segment and it appears to be significantly better than the corresponding one
determined by the base algorithm, then the IMS-ALGs instruct the TrGWs to
insert the shorter path segment into the overall media path.
#### 7.2.4.2 Example flow for Active Bypass Option
Figure 7.2.4.2-1 shows a call flow that corresponds to the configuration in
figure 7.2.4.1-1.
Figure 7.2.4.2-1: Example Flow with Active-Bypass Option
Steps 1a to 1f describe the progression of SDP offers via the IMS-ALGs from
UA1 to UA2 and steps 2a to 2f describe the corresponding progression of SDP
answers according to the base algorithm. After step 2a, IMS-ALG5 determines
that it may be able to establish a shorter media path segment via IMS-ALG1 and
sends an empty SIP INVITE request to IMS-ALG1 via IMS-ALG6 in steps 3a and 3b.
Steps 4a, 4b, 5a and 5b describe a new SDP offer/answer transaction between
IMS-ALG1 and IMS-ALG5 via IMS-ALG6 which attempts to establish an alternate
media path segment. If an alternate media path segment is successfully
established and is a significant improvement, IMS-ALG5 signals the selection
of the alternate media path segment to IMS-ALG1 in steps 2b through 2e. IMS-
ALG1 incorporates the alternate media path segment into the media path for the
primary dialog before forwarding the final SDP answer to UA1 in step 2f.
1a through 1f. See steps 1a through 1f of figure 7.2.3.3.1-1.
2a. See step 2a of figure 7.2.3.3.1-1.
3a. If IMS-ALG5 retains TrGW5a for a media line after processing of the base
algorith, if IMS-ALG5 determines that a shorter media path may exist to an
earlier IP realm remaining in the path based on geo-location, delay and error
rate information available from visited-realm and secondary-realm attributes
previously received in the SDP offer for the media line in step 1e, and if
there is a temporary GRUU available from the visited-realm or secondary-realm
attribute associated with the earlier IP realm, then IMS-ALG5 may attempt to
initiate the active-bypass option for the media line by sending an empty SIP
INVITE request to the IMS-ALG (IMS-ALG1) associated with the earlier IP realm
by setting the Request URI to the temporary GRUU for the media line associted
with IMS-ALG1.
3b. IMS-ALG6 forwards the empty SIP INVITE request to IMS-ALG1.
4a. IMS-ALG1 responds to the empty INVITE request by sending an SDP offer in a
200 OK response. The SDP offer includes a media line for each media line
forwarded in the SDP offer of the original dialog in step 1b for which IMS-
ALG1 previously allocated a TrGW. Each media line in the new SDP offer
includes a copy of the codec information from the previously forwarded SDP
offer, connection information for TrGW1b, and a visited-realm attribute with
temporary GRUU.
4b. IMS-ALG6 forwards the 200 OK response to IMS-ALG5.
5a and 5b. IMS-ALG5 responds to the 200 OK response with the ACK request
including an SDP answer to establish the alternate media path segment between
TrGW1b and TrGW5b.
2b. If the geo-location, delay and error information associated with the
alternate path segment for the media line indicates that it is substantially
better than the corresponding media path segment established by the original
dialog, then IMS-ALG5 forwards the SDP answer for the media line from step 2a
after changing the connection information to the unspecified address and
including a visited-realm attribute with unique connection information
indicating that there is no matching IP realm along the original media path.
2c through 2e. Since the visited-realm attribute in the received SDP answer
does not match any of the IP realms associated with the IMS-ALGs, the IMS-ALGs
forward the SDP answer without change, de-allocating TrGWs along the way if
necessary.
2f. IMS-ALG1 waits for receipt of both of the SDP answers in steps 5b and 2e.
If the visited-realm attribute for the media line in step 2e indicates no
matching IP realm on the original media path, then IMS-ALG1 completes the
insertion of the alternate media path segment into the original media path by
substituting connection information for TrGW1b into the forwarded SDP answer.
### 7.2.5 Interactions with Transcoding
#### 7.2.5.1 Transcoding with the base algorithm
The existing IBCF procedures for transcoding in TS 23.228 [8] either allow the
IBCF to add codec options to an SDP offer before forwarding (called proactive
transcoding), or allow the session to fail if none of the initial codecs are
supported by the terminating side, in which case the IBCF adds codec options
to a second SDP offer (called reactive transcoding).
With reactive transcoding, the IMS-ALG adds the transcoding function and
anchors its TrGW only when transcoding is needed. The alternative 1 OMR
procedure is fully consistent with reactive transcoding and supports the same
degree of media optimization whether or not transcoding is used for a
particular session.
With proactive transcoding, the IMS-ALG may or may not allocate a TrGW at the
beginning of the SDP offer/answer transaction, and may need to add or remove
the TrGW when the SDP offer/answer transaction completes by initiating a
second SDP offer/answer transaction.
If the IMS-ALG does not allocate a TrGW and forwards the received connection
information in the SDP offer, it should also forward any OMR SDP extension
attributes to allow full OMR to occur. This assures that if the terminating
side selects one of the original codecs and no transcoding is needed, the
media path can be correctly established with OMR in one SDP offer/answer
transaction. If the terminating side selects one of the additional codecs, the
IMS-ALG allocates a TrGW for transcoding and anchors the TrGW in the media
path during the second SDP offer/answer transaction without forwarding any OMR
extension attributes for prior IP realms in the forwarded SDP offer. This
assures that OMR is separately applied to the incoming and outgoing media legs
of the anchored TrGW.
If the IMS-ALG allocates a TrGW and forwards the TrGW connection information
in the SDP offer, it shall not include any OMR extension attributes for prior
IP realms. This assures that if the terminating side selects one of the
additional codecs associated with the TrGW, the media path can be correctly
established with OMR separately applied to the incoming and outgoing media
legs of the anchored TrGW within one SDP offer/transaction. If the terminating
side selects one of the original codecs and transcoding is not needed, the
IMS-ALG may remove the TrGW during a second SDP offer/answer transaction,. The
alternative 1 OMR procedure performs the appropriate optimizations to the
entire media path during the second SDP offer/answer transaction.
For both reactive and proactive transcoding, if a second SDP offer/answer
transaction is required to establish the optimized session, the IMS-ALG that
allocates the transcoding function initiates and completes the second SDP
offer/answer transaction on the outgoing leg before returning an SDP answer
for the first SDP offer/answer transaction. If an active-bypass is created
during the first SDP offer/answer transaction that becomes invalid or is
modified during the second SDP offer/answer transaction, the IMS-ALG
establishing the active-bypass during the first SDP offer/answer transaction
ensures that it is deleted or modified as necessary during the second SDP
offer/answer transaction.
For both reactive and proactive transcoding, the alternative 1 OMR procedures
apply without change to the existing SDP offer/answer transactions.
#### 7.2.5.2 Codec-aware option
##### 7.2.5.2.1 General
While the base algorithm provides media path optimization with or without
transcoding, certain improvements are possible by sharing information about
codec changes made by the IMS-ALGs. By allowing an IMS-ALG to report codec
changes it makes to subsequent IMS-ALGs, the following improvements can be
made to the base algorithm without loss of any functions or options associated
with the base algorithm:
\- For the proactive transcoding methods, it is possible for an IMS-ALG to
remove the transcoding options associated with a previous IMS-ALG and offer a
codec list with the same or a different set of transcoding options. This
allows for either the deletion of a potential transcoding point on the media
path, or the relocation of a potential transcoding point from an earlier TrGW
on the media path to a later TrGW on the media path. This may be desirable,
for example, if the second TrGW is anchored anyway, thus allowing the bypass
of an extra TrGW. This may also be desirable if anchoring of the second TrGW
rather than the previous TrGW can be identified as leading to a shorter end-
to-end media path.
\- An IMS-ALG has the option to restore codecs deleted by a previous IMS-ALG
if the previous IMS-ALG can be bypassed.
\- If an IMS-ALG invokes the proactive transcoding method with gateway
reservation and a later IMS-ALG that anchors its own TrGW in the media path
then determines that transcoding is not needed, the later IMS-ALG may be able
to bypass the earlier TrGW allocated for transcoding without requiring a
second SDP offer/answer transaction.
\- If an IMS-ALG invokes the proactive transcoding method with gateway
reservation and a later IMS-ALG that does not anchor a TrGW in the media path
then determines that transcoding is not needed, the later IMS-ALG may be able
to initiate a second SDP offer/answer transaction to update the terminating
side and bypass the earlier TrGW allocated for transcoding. While not
eliminating the second SDP offer/answer transaction in this case, it reduces
the required signalling.
While not eliminating all need for a second SDP offer/answer transaction in
transcoding scenarios, the codec-aware option provides the greatest potential
for reduction in signalling when used with the proactive transcoding method
with gateway reservation. Furthermore, the codec aware option has the
potential to reduce the number of calls where transcoding or even multiple
occurrences of transcoding are applied, to reach a more optimal allocation of
transcoding points and to reach a shorter end-to-end media path.
##### 7.2.5.2.2 Procedures
The changes required to the base algorithm for the codec-aware option are as
follows:
1\. While processing an SDP offer, an IMS-ALG may add or delete codecs in the
codec list for a media line according to local policy. When adding codecs for
potential transcoding, the IMS-ALG may use the reactive method, the proactive
method without gateway reservation, or the proactive method with gateway
reservation, according to local policy. The IMS-ALG choosing to modify the
codec list for a media line shall include a copy of the media line for the
incoming SDP offer in the visited realm attribute and alternate realm
attribute(s) for the realms associated with the outgoing SDP offer. .\ \ Note
that there may be more than one visited realm or alternate realm attribute
associated with the same realm, and there may be separate attributes for the
incoming and outgoing SDP offer if there is a change in the codec list for the
media line even if no gateway is reserved and they are associated with the
same realm. .\ \ When processing an SDP answer, if an IMS-ALG that offers
transcoding according to one of the three transcoding options is not bypassed
by a later IMS-ALG, it may perform a second SDP offer/answer transaction as
needed according to the transcoding option selected and the base algorithm.
2\. While processing an SDP offer, if an IMS-ALG identifies a previous TrGW in
the media path that is associated with additions to the codec list (i.e.,
transcoding options) for a media line and that can be bypassed if the
additions are not needed (i.e., an earlier visited realm is reachable), and if
the IMS-ALG determines according to local policy either that the codec
additions are not needed or that the IMS-ALG can offer the codec additions
locally (e.g., by providing transcoding options via a TrGW), then the IMS-ALG
may bypass the previous TrGW, thus removing its codec additions, and
optionally make other codec additions locally before forwarding the SDP
offer.\ \ In effect, this allows for either the deletion of a potential
transcoding point on the media path, or the relocation of a potential
transcoding point from an earlier TrGW on the media path to a later TrGW on
the media path. This may be desirable, for example, if the second TrGW is
anchored anyway, thus allowing the bypass of an extra TrGW. This may also be
desirable if anchoring of the second TrGW rather than the previous TrGW can be
identified as leading to a shorter end-to-end media path. .\ \ If a previous
TrGW adding codecs to a media line in an SDP offer also deletes any of the
original offered codecs, the IMG-ALG bypassing the previous TrGW may restore
any of the deleted codecs to the forwarded SDP offer according to local policy
before making other local codec additions. .\ \ Note that a previous TrGW in
the media path that adds to the codec list shall not otherwise be bypassed
during processing of the SDP offer.
3\. While processing an SDP offer, if an IMS-ALG identifies a previous TrGW in
the media path that is associated with deletions to the codec list (and no
additions) for a media line, the IMS-ALG shall treat the previous TrGW as a
candidate for bypass according to the base algorithm. If the IMS-ALG bypasses
the previous TrGW, it may restore any of the codecs deleted by the previous
TrGW to the forwarded SDP offer according to local policy.
4\. When processing an SDP answer, if an IMS-ALG anchoring a TrGW on the media
path identifies a previous TrGW that could have been bypassed according to the
base algorithm but was not bypassed due to the addition of codecs for
potential transcoding, and the IMS-ALG determines that none of the additional
codecs associated with the previous TrGW were selected in the SDP answer, then
the IMS-ALG may bypass the previous TrGW.\ \ When the IMS-ALG associated with
the previous TrGW in this case uses the proactive transcoding method with
gateway reservation, this procedure avoids the second SDP offer/answer
transaction that would otherwise be required to remove the previous TrGW from
the media path.
5\. When processing an SDP answer, if an IMS-ALG that does not anchor a TrGW
on the media path 1) identifies a previous TrGW that could have been bypassed
according to the base algorithm but was not bypassed due to the addition of
codecs for potential transcoding, 2) determines that none of the additional
codecs associated with the previous TrGW were selected in the SDP answer, and
3) determines that the IMS-ALG associated with the previous TrGW used the
proactive transcoding method with gateway reservation, then the IMS-ALG may
bypass the previous TrGW after initiating and completing a second SDP
offer/answer transaction on the outgoing leg with the media line and
connection information associated with the earliest reachable realm prior to
the previous TrGW according to the base algorithm. .\ \ This procedure allows
an IMS-ALG closer to the SDP answerer to initiate and complete the second SDP
offer/answer in this case, rather than requiring this to be done by the IMS-
ALG offering the transcoding options, thus reducing the signalling needed to
remove the previous TrGW from the media path.
### Interworking with PSTN
Since many IMS sessions will be interworked with the CS domain, it would be
beneficial to apply optimization to the entire path between endpoints.
Alternative 1 applies throughout interconnected IMS networks until the point
of interworking with the CS domain (typically the MGCF), but not within the
existing CS domain. In the future, IMS may provide more of the transit
infrastructure for the CS domain using features like ICS, or by collocating
MGCF and MSC functionality, but media optimization within the CS domain is out
of scope.
### Interaction with local breakout
There are no special considerations when applying OMR to the single IP address
form with visited P-CSCF, and the dual IP address form of local breakout is
not recommended. This discussion focuses on the single IP address form of
local breakout with home P-CSCF. In this case, the UE will normally be
assigned a globally reachable public IP address to avoid the use of a NAT
between the visited and home networks.
The use of IMS-ALGs and TrGWs in the home network raises the concern that the
media path for a session using local breakout may be anchored in the home
network if an OMR algorithm cannot remove the TrGWs allocated in the home
network, thus limiting the potential for media path optimization.
Nevertheless, the home network may have legitimate security concerns requiring
the use of IMS-ALGs and TrGWs at its border to protect internal network
resources. If the home network allocates media resources for a session to
provide a media function such as transcoding, conferencing or announcements,
any TrGW allocated at the home network border serves the purpose of protecting
the internal network resources and shall not be subject to bypass.
To achieve OMR for sessions that traverse the home network without need of an
internal media function, an OMR algorithm must identify this case and ensure
that TrGWs are either not allocated at its border or are de-allocated. In the
most common case where the home network can interconnect to other networks
using globally reachable public IP addresses, then Alternative 1 provides the
means to ensure that OMR can be achieved. The Alternative 1 algorithm
identifies that since both the UE and the next interconnected network are
reachable using public IP addresses, the media path for the session can bypass
the home network and its TrGWs altogether. Thus the Alternative 1 OMR
algorithm allows for the complete bypass of any network that does not provide
media functions for a session, particularly when each network has available
globally reachable public IP addresses for external media connections.
### Protecting network resources
It is necessary to assure that a TrGW cannot be bypassed when it is allocated
to protect a network media resource such as a transcoder or conference bridge.
Alternative 1 only bypasses a TrGW when an authorized alternate media path
exists. If a media resource is allocated within a network, Alternative 1 can
assure that the media resource can only be accessed either from another
endpoint within the network or via a TrGW protecting access from another
network. This is accomplished by labelling media connection information with a
realm name that is only valid within its network.
### Network interconnect issues
Alternative 1 assumes that interconnect agreements are in place to allow the
application of the algorithm at the boundary between networks. Media may
completely bypass a home or transit network when no media resources are needed
in the network. Interconnect agreements must allow for transit of the SDP
extensions needed for Alternative 1 and for transit of SIP signalling with or
without associated media. Every ALG in a supporting network must support the
algorithm. Alternative 1 allows any network to force the media through its
network if necessary for media functions or to satisfy regulatory
requirements, by either terminating the session at a media server or endpoint,
or by removing the SDP extensions from forwarded SDP.
Since Alternative 1 is based on a proposed SDP extension, any non-supporting
network should ignore the extension according to standard procedures and use
the connection information normally populated in SDP. The result is that any
media resource or endpoint in the non-supporting network will be anchored in
the path and not subject to bypass. If the non-supporting network introduces
no media function in the media path, then it should transit the SDP messages
without change, maintaining the ability to apply OMR to the end-to-end media
path.
If some peer networks have interoperability issues with the proposed SDP
extension, there may be a local policy in the IMS-ALG to delete the OMR SDP
extension attributes from SIP messages towards these networks. This policy
should be applied selectively since opportunities for media optimization may
be lost if the non-supporting network inserts no media functions in the media
path.
The extension is not consistent with ICE, but since ICE requires the
cooperation of both endpoints, Alternative 1 will take precedence and apply
throughout the supporting portions of the end-to-end path.
### Resource admission control
Resource admission control in the RAN is triggered by the completion of the
SDP negotiation. Since the Alternative 1 algorithm is concurrent with the SDP
negotiation and completes by the end of the SDP offer/answer signalling,
resource admission control begins only after media optimization completes,
thus assuring correct resource allocation.
### Lawful Intercept
Alternative 1 allows a network to insert a non-bypassable media resource, such
as one needed for lawful intercept, in the path of any IMS session as
necessary. Since this media resource cannot be bypassed, it reduces options
for media optimization. Optimization is still separately possible on the media
legs from the resource to the two endpoints.
Insertion of a media resource in a media path may be visible by an endpoint as
a change in connection information if there is no intervening TrGW in the
path, compared to a similar session without the media resource.
Editor\'s note: Whether this possibility of detection is an issue for the use
of Alternative 1 with LI is FFS, even though there are many possible valid
reasons for a network to manipulate connection information in an IMS session.
### Charging
Charging records should include sufficient information to capture the
allocation and/or bypass of TrGWs in the media path of an IMS session. This
information should be used to facilitate reconciliation of charging data
between networks.
### Common transit scenario
The most common transit scenario for a network is to use globally reachable IP
addresses to reach peer networks. Thus any network on the path that deploys
IMS-ALGs and TrGWs at its border to protect internal media resources has the
ability to bypass the TrGWs for sessions that do not require the allocation of
media resources within the network. Figure 7.2.13-1 shows how Alternative 1
ensures that TrGWs are bypassed in this case.
Figure 7.2.13-1: TrGW bypass in common transit scenario
  1. IMS-ALG1 receives an incoming SDP offer from external realm EXT. The SDP offer includes IP address E1 within the external realm EXT and a visited realm attribute for the same address. IMS-ALG1 and IMS-ALG2 are associated with the incoming and outgoing IBCFs for a protected network with realm INT.
  2. IMS-ALG1 allocates a TrGW with outgoing address I1 and forwards an SDP offer with address I1 that is valid within the realm INT and two visited realm attributes associated with the incoming and outgoing SDP offers.
  3. IMS-ALG2 notes that a visited realm attribute from the incoming SDP offer includes an address that is valid in the outgoing realm. IMS-ALG2 does not allocate a TrGW, remembers that it must bypass the previous TrGW, and forwards the address E1 that is valid in the outgoing realm EXT.
  4. The terminating side returns an SDP answer with a valid address E2 in the realm EXT.
  5. IMS-ALG2, recalling that it must bypass the previous TrGW, forwards an unspecified address (0.0.0.0) for realm INT in the SDP answer and includes a visited realm attribute with a valid address for realm EXT.
  6. Upon receiving an SDP answer with an unspecified address for realm INT, IMS-ALG1 extracts the valid address E2 for realm EXT from the visited realm attribute and forwards the SDP answer with address E2.
## 7.3 Alternative 2: Transcoding aware
### 7.3.1 Description of the base algorithm
This alternative introduces a transcoding aware procedure for OMR, that is,
identify when one or more TrGWs and/or RGs can be bypassed, or, an alternative
media path can be used, during SDP answer forwarding phase.
During SDP offer forwarding phase, each IMS-ALG supporting OMR shall provide
IP realm information on the incoming signalling path in the forwarded SDP
offer for each media stream. If an IMS-ALG along the signalling path controls
additional TrGW(s), and the additional TrGW(s) has access to the IP realm(s)
other than those IP realms that it controls on the default media path, then
the IMS-ALG can advertise its ability to access additional IP realm(s) by
appending the related information in the forwarded SDP offer for the media
stream, which can help the later IMS-ALG(s) to find the secondary optimized
media path. The information of the additional IP realm(s) is on the outgoing
signalling path.
NOTE 1: If an IMS-ALG does not provide TrGW for a media stream, then the IMS-
ALG can forward the IP realm(s) information for the media stream received in
the SDP offer or the SDP answer.
The IP realm information for the default media path and the additional TrGW(s)
contains at least realm identifier, connection/port data, and the codec
number. The codec number stands for the quantity of codecs in the SDP offer
received by the IMS-ALG, which is the vital information to determine whether
proactive transcoding can be applied by previous IMS-ALG or not.
NOTE 2: If auxiliary formats such as DTMF and comfort noise included in the
SDP offer, then if auxiliary formats are well known, e.g. telephone-event, the
auxiliary formats must not be counted into the codec number, otherwise, the
IMS-ALG(s) providing transcoding options must move the auxiliary formats to
the bottom and correct the codec number of the received IP realms, which are
successive from the end and have identical codec number.
A new SDP media-level attribute \"realm\" can be used for providing IP realm
information. The new attribute shall include a sequence number. The IP
realm(s) provided by an IMS-ALG should be included in one \"a=realm:\"
attribute line.
Another new SDP session-level attribute \"pathp\" can be optionally included
to contain the Path Parameters for all media lines, such as connection data of
the media line(s). The \"pathp\" attribute shall include a sequence number
corresponding to the \"realm\" attribute, and may include cryptographic
signature to ensure the integrity of the IP realm data and Path Parameters
data. If the Path Parameters related to an IMS-ALG contains connection data,
there is no need to repeat the connection data in the IP realms related to the
IMS-ALG for all media lines if they are same.
> During SDP answer forwarding phase, each IMS-ALG may identify one or more
> TrGWs and/or RGs can be bypassed, or, an alternative media path can be used.
> The optimized alternative media path is determined based on the received IP
> realm(s) information during SDP offer phase, all the IP realms information
> for a media stream makes up an ordered IP realm list.
When an IMS-ALG receives an SDP answer, the IMS-ALG shall:
1\. if a media line in the SDP answer does not contain IP realm, check the IP
realm list from the beginning and:
a. identify whether a controlled TrGW has a direct connection to an IP realm,
which is on the outgoing or incoming signalling path;
NOTE 3: If the IMS-ALG provides transcoding options, and a transcoding option
is selected, do not consider the IP realm on the outgoing signalling path
(i.e. the TrGW controlled by the IMS-ALG is included in the media path).
b. if an IP realm is identified,findy contain cs from the ceived SDP offer one
by one from beginning into a codec list until the quantity of codecs in the
codec list equals to the minimal codecof the identified IP realm; and,
c. if the selected codec (indicated in the SDP answer or selected by the IMS-
ALG) is in the codec list, then provide an IP realm for the media line in the
forwarded SDP answer, and
\- if the identified IP realm is on the outgoing signalling path, provide the
connection information of the SDP answer in the IP realm to bypass the
controlled TrGW; or
\- if the identified IP realm is on the incoming signalling path, use the
connection information of the identified IP realm and provide connection
information of the controlled TrGW in the IP realm.
\- set the sequence number of the \"realm\" attribute line containing the IP
realm to that of the \"realm\" attribute line containing the identified IP
realm.
NOTE 4: The IMS-ALG must release the controlled TrGW if it can be bypassed,
and in order to release the bypassed TrGW(s) prior to the controlled TrGW, the
IMS-ALG must set the connection information of the media stream in the SDP
answer to the unspecified address.
d. otherwise, proceed with step a - c until no IP realm can be identified.
2\. if a media line in the SDP answer contains an IP realm:
a. if the sequence number of the \"realm\" attribute line containing the IP
realm is the same as that of the added \"realm\" attribute line in the
forwarded SDP offer, and the realm identifier of the IP realm is the same as
that of the added IP realm(s) in the forwarded SDP offer, then:
NOTE 5: IP realm data may be encrypted, so, it is better to check the sequence
number first.
\- if the IP realm is on the incoming signalling path, forward an SDP answer
with the connection information of the IP realm and bypass the controlled
TrGW. The IMS-ALG shall remove the IP realm and corresponding Path Parameters
from the forwarded SDP answer; or,
\- if the IP realm is on the outgoing signalling path, use the connection
information of the IP realm and forward an SDP answer with the connection
information of the controlled TrGW. The IMS-ALG shall proceed with step 1 for
IP realm on the incoming signalling path before forwarding the SDP answer.
b. otherwise, forward an SDP answer with the IP realm to bypass the controlled
TrGW.
If an IMS-ALG is the last one to the remote UE or is the last one in an OMR
domain (successive IMS-ALGs supporting OMR consist of an OMR domain), and the
TrGW controlled by the last IMS-ALG can be bypassed, and the connection
information of the identified IP realm is different from that of the forwarded
SDP offer, then an extra SDP offer/answer exchange is required.
An IMS-ALG can determine that it is the last one based on deployment. Another
alternative is that each IMS-ALG includes IP realm information in the SDP
answer. If an IMS-ALG receives an SDP answer without IP realm, the IMS-ALG
decides that it is the last one. And if an IMS-ALG receives an SDP answer that
carries IP realm information containing unspecified address, which means that
the next IMS-ALG can not find out an optimized media path or an alternative
media path and the IP realm is an invalid IP realm, then the IMS-ALG proceeds
with step 1.
### 7.3.2 Procedures and call flows
#### 7.3.2.1 Call flow for base algorithm
Figure 7.3.2.1-1 shows a call flow for transcoding aware OMR that the last
TrGW can not be bypassed.
Figure 7.3.2.1-1: Transcoding aware
NOTE: The number in the brackets is codec number of the IP realm. The codecs
at the bottom of the figure show the codecs in the corresponding SDP offer.
The codec below the line is added by IMS-ALG1. Remote UE2 selects Codec1 in
the SDP answer.
Steps 1a to 1e describe the progression of SDP offers via the IMS-ALGs from
UE1 to UE2. The IMS-ALG1 adds Codec3 as transcoding option. Steps 2a to 2e
describe the corresponding progression of SDP answers according to the
algorithm.
The TrGW controlled by each IMS-ALG has two IP realms, one is on the incoming
signalling path that needs to be recorded in the SDP offer during SDP offer
phase, and the other is on the outgoing signalling path. In the flow, IMS-ALGn
identifies that the IP realm identifier on the incoming signalling path of
IMS-ALGn (realm2) is the same as that of IMS-ALG2 (realm2), then IMS-ALGn gets
a codec list containing Codec1 and Codec2, because selected codec Codec1 is in
the gotten codec list, so TrGWs controlled by IMS-ALG2, IMS-ALG3 ... and IMS-
ALGm can be bypassed. The connection/port data in the IP realm of step 2b, 2c,
and 2d represent the transport address of TrGW controlled by IMS-ALGn.
#### 7.3.2.2 Last TrGW can be bypassed
Figure 7.3.2.2-1 shows a call flow for transcoding aware OMR in case that the
last TrGW can be bypassed without additional signalling.
Figure 7.3.2.2-1: Transcoding aware - last TrGW can be bypassed without
additional signalling
NOTE 1: The number in the brackets is codec number of the IP realm. If IMS-
ALGn does not provide TrGW for the media, then last TrGW is controlled by IMS-
ALGm, and realm N is realm 2, and the SDP offer in step 1e does not carry
realmN(3).
Steps 1a to 1e describe the progression of SDP offers via the IMS-ALGs from
UE1 to UE2, step 2a describes the SDP answer from UE2, step 3a describes the
new SDP offer with connection/port information of previous IP realm 2, and
steps 4a to 4e describe the corresponding progression of SDP answers according
to the algorithm.
NOTE 2: If the IMS-ALGn knows that an UPDATE transaction is needed, steps 2a
and 3a are optional and then the confirmation ACK of step 4a can be SIP 18x
response, otherwise, the UE1 will send out a PRACK request without SDP after
step 4e, the IMS-ALGn must stop forwarding the PRACK request and send out 200
OK response to the PRACK request. In some case, the PRACK request may contain
SDP offer, if terminating UE support UPDATE method, then the IMS-ALGn must
send out UPDATE request to terminating side, otherwise the IMS-ALGn must
follow the procedure shown in figure 7.3.2.2-1 after receiving answer message.
In the flow, the IP realm identifier on the outgoing signalling path of IMS-
ALGn (realm2) is the same as the IP realm identifier on the incoming
signalling path of IMS-ALG2 (realm2), so TrGWs controlled by IMS-ALG2 to IMS-
ALGn can be bypassed. Because the IMS-ALGn is the last IMS-ALG to the remote
UE, an extra SDP offer/answer exchange is needed as shown in step 2a and 3a.
The connection/port data in the IP realm of step 4b, 4c, and 4d represent the
transport address of UE2.
Figure 7.3.2.2-2 shows another call flow for transcoding aware OMR that the
last TrGW can be bypassed with additional signalling cost.
Figure 7.3.2.2-2: Transcoding aware - last TrGW can be bypassed with
additional signalling cost
NOTE 3: The number in the brackets is codec number of the IP realm. If IMS-
ALGn does not provide TrGW for the media, then last TrGW is controlled by IMS-
ALGm, and realm N is realm 2, and the SDP offer in step 1e does not carry
realmN(3).
Steps 1a to 1e describe the progression of SDP offers via the IMS-ALGs from
UE1 to UE2, steps 2a to 2e describe the SDP answer from UE2 to UE1, step 3
describes that IMS-ALGn requests UE2 to initiate an SDP offer/answer
transaction, step 4a describes the new SDP offer from UE2, and step 5a
describes the new SDP answer with connection/port information of previous IP
realm 2 and selected codec indicated in SDP answer of 2a.
NOTE 4: SDP offer in step 4a is SDP answer in step 2a with additional codecs,
so, SDP answer in step 5a is SDP offer in step 1d with replaced connection
information and selected codecs.
7.3.2.3 IMS-ALG controls additional TrGW(s)
Figure 7.3.2.3-1 shows a call flow for transcoding aware OMR in case that an
IMS-ALG has additional TrGW(s).
Figure 7.3.2.3-1: Transcoding aware - additional TrGW provided
NOTE: The number in the brackets is codec number of the IP realm.
Steps 1a to 1e describe the progression of SDP offers via the IMS-ALGs from
UE1 to UE2. The TrGW1 controlled by the IMS-ALG1 is default TrGW for the media
path, the additional TrGW2 controlled by the IMS-ALG1 can access IP realm N on
the outgoing signalling path. Steps 2a to 2e describe the corresponding
progression of SDP answers according to the algorithm.
### 7.3.3 Handling of removed codec
If an IMS-ALG decides to remove some codec from the received SDP offer per
local policy, the IMS-ALG shall record the removed codec and the related
position in the last IP realm in the forwarded SDP offer.
NOTE 1: If the IMS-ALG does not provide TrGW for the media, then the IMS-ALG
will not add IP realm in the forwarded SDP offer, the IMS-ALG will recode the
information of the removed codec into the last IP realm received in the SDP
offer.
During SDP answer forwarding phase, if an IMS-ALG receives an SDP answer that
a media line does not contain IP realm, the IMS-ALG shall apply procedures as
specified in subclause 7.3.1 with following additions:
\- after identifying an IP realm and before getting a codec list, restore the
removed codecs in the IP realms after the identified one (including the
identified one) into the codecs of the received SDP offer.
NOTE 2: The restoration must be performed as restoration of incremental
backup, so that if two or more IP realms containing information of removed
codec, the removed codecs can be correctly restored. For example, if original
codecs are C1, C2, and C3, firstly C2 is removed by some IMS-ALG, the position
of C2 is 2, secondly C3 is removed by another IMS-ALG, the position of C3 also
is 2, then the IMS-ALG first restore C3 in the second place, then restore C2
in the second place and move C3 to the third place.
NOTE 3: If the IMS-ALG provides transcoding options, and a transcoding option
is selected, and the transcoding option is a removed codec by previous IMS-
ALG, the TrGW controlled by the IMS-ALG may be bypassed, i.e. the IP realm on
the outgoing signalling path still need to be considered.
Figure 7.3.3-1 shows an example flow of recording information of removed codec
in the IP realm, which shows that a transcoding option is selected, and the
transcoding option is removed by previous IMS-ALG, and the optimized media
path does not involve transcoding.
Figure 7.3.3-1: Handling of removed codec - record information of removed
codec in the IP realm
NOTE 4: The number in the brackets is codec number of the IP realm. The codecs
at the bottom of the figure show the codecs in the corresponding SDP offer.
Remote UE2 selects codec C2 in the SDP answer.
Steps 1a to 1e describe the progression of SDP offers via the IMS-ALGs from
UE1 to UE2. The IMS-ALG1 removes codec C2 and records C2 and the related
position of 2 in the forwarded IP realm. The IMS-ALG2 adds codec C2 again as
transcoding option. Steps 2a to 2e describe the corresponding progression of
SDP answers according to the algorithm.
In this case, the UE2 select codec C2, UE1 can use codec C2 for the media
stream, and TrGW controlled by IMS-ALGn can have directly access to UE1 (both
of them can access IP realm 1), so the best optimized media path only includes
the TrGW controlled by IMS-ALGn. The algorithm can get the best optimized
media path.
### 7.3.4 Interactions with Transcoding
In TS 23.228 [8], IBCF is allowed to use proactive transcoding (provide
transcoding options in the first SDP offer) and reactive transcoding (provide
transcoding options after first SDP offer has been rejected for the reason
that no codec can be used).
For reactive transcoding, when the first SDP offer has been rejected, the
algorithm has been aborted for the first SDP offer/answer transaction, and
will be applied during another SDP offer/answer transaction. The IMS-ALG, who
initiates the second SDP offer/answer transaction for providing transcoding
options, shall remove all the SDP extensions and unspecified codecs from the
forwarded SDP offer.
For proactive transcoding, when the IMS-ALG provides additional transcoding
options in the first SDP offer, the behaviour of the IMS-ALG can be
categorized as follows:
A. allocates TrGW for transcoding when forwarding SDP offer, and triggers
second SDP offer/answer transaction when no transcoding option is selected;
B. allocates TrGW for transcoding when forwarding SDP offer, and does not
trigger second SDP offer/answer transaction when no transcoding option is
selected;
C. does not allocate TrGW for transcoding when forwarding SDP offer, and
triggers second SDP offer/answer transaction when transcoding option is
selected.
D. does not allocate TrGW for transcoding when forwarding SDP offer, and does
not trigger second SDP offer/answer transaction when transcoding option is
selected.
If the IMS-ALG provides proactive transcoding options, the IMS-ALG shall
include behaviour indication in the last added IP realm.
Addition to the procedure as specified in subclause 7.3.1, if:
\- the behaviour indication of an IP realm in the checked IP realms (excluding
the identified IP realm) is Category A, and no transcoding option need to be
applied in this realm; or,
\- the behaviour indication of an IP realm in the checked IP realms (excluding
the identified IP realm) is Category C, and transcoding option need to be
applied in this realm.
NOTE: In these cases, the transcoding IMS-ALG will initiate an extra SDP
offer/answer transaction. If the selected codec is in the codec list generated
based on the codecs in the received SDP offer and the codec number of the IP
realm, then no transcoding option is needed in this realm, otherwise,
transcoding option is needed.
The last IMS-ALG shall not initiate the second SDP offer/answer transaction,
and shall apply procedures as specified in subclause 7.3.5.1.
### 7.3.5 Enhancement of the algorithm
#### 7.3.5.1 Improvement to successive SDP exchanges
During the first SDP offer/answer transaction, the IMS-ALG, who found an
optimized media path, shall save the position of the identified IP realm in
the received IP realm list and related realm identifier.
During the successive SDP offer/answer transactions, before forwarding the
other SDP offer, the IMS-ALG shall check whether the IP realm at the position
in the received IP realm list contains the same realm identifier as the saved
one. If they are same, then the IMS-ALG shall:
\- if the IP realm is on the outgoing signalling path, replace connection
information in the forwarded SDP offer with that of the IP realm;
\- if the IP realm is on the incoming signalling path, use the connection
information of the IP realm.
When an SDP answer is received, the IMS-ALG shall provide an IP realm in the
forwarded SDP answer. The provided IP realm can be directly connected by the
TrGW controlled by previous IMS-ALG.
Figure 7.3.5.1-1 shows a call flow for the second SDP offer/answer
transaction.
Figure 7.3.5.1-1: Transcoding aware - Second SDP offer/answer transaction
Steps 3a to 3e describe the progression of the second SDP offers via the IMS-
ALGs from UE1 to UE2, SDP offer in step 3e uses the connection information of
the received IP realm2, and steps 4a to 4e describe the corresponding
progression of SDP answers according to the algorithm.
#### 7.3.5.2 Pre-identify method
Base algorithm in subclause 7.3.1 identifies the IP realm during SDP answer
forwarding phase, but during SDP offer forwarding phase, if an IMS-ALG does
not provide transcoding options, or provides transcoding options with Category
C or D way, the IMS-ALG may pre-identify an IP realm as follows:
\- check the IP realms in the received IP realm list from the end;
\- if an IP realm containing behaviour indication with value of Category A or
B can be found, then continue pre-identify procedures for the checked IP realm
list (excluding the found one);
NOTE 1: This assures that if the terminating side selects one of the
additional codecs, the media path can be correctly established with OMR
applied to the outgoing media legs of the transcoding TrGW within one SDP
offer/transaction. If the terminating side selects one of the original codecs
and transcoding is not needed, the procedures as specified in subclause 7.3.1
will get a best optimized media path, and in this case, when both the TrGWs
controlled by the IMS-ALG and the transcoding provider can be bypassed, an
extra SDP offer/answer transaction may be needed between the IMS-ALG and
terminating UE.
\- otherwise, continue pre-identify procedures for the whole received IP realm
list;
NOTE 2: This assures that if the terminating side selects one of the original
codecs and no transcoding is needed, the media path can be correctly
established with OMR in one SDP offer/answer transaction. If transcoding
options are provided and the terminating side selects one of the additional
codecs, the procedures as specified in subclause 7.3.1 will get a correct
optimized media path, and in this case, if Category C proactive transcoding is
provided, an extra SDP exchange will be initiate by the transcoding provider,
if Category D proactive transcoding is provided, and both the TrGWs controlled
by the IMS-ALG and the transcoding provider were bypassed during SDP offer
forwarding phase, the extra SDP offer/answer transaction may be needed between
the IMS-ALG and terminating UE.
Continuing pre-identify procedures for an IP realm list, when forwarding an
SDP offer, the IMS-ALG shall identify whether a controlled TrGW has a direct
connection to an IP realm in the IP realm list. If an IP realm can be
identified and the IP realm is for the outgoing signalling path, the IMS-ALG
shall apply procedures as specified in subclause 7.3.1 with following
additions:
\- replace connection information of the forwarded SDP offer with that of the
identified IP realm.
According to interworking agreement, an IMS-ALG can know whether it is the
boundary of an OMR domain. If an IMS-ALG is a boundary of an OMR domain on the
side of outgoing signalling path or is in visited network of the terminating
UE, especially collocated with P-CSCF, and the IMS-ALG applies pre-identify
method, then additional SDP offer/answer transaction can be eliminated or
improved when the last TrGW can be bypassed.
Figure 7.3.5.2-1 shows an example flow for transcoding aware OMR that an IMS-
ALG applies pre-identify method.
Figure 7.3.5.2-1: Transcoding aware - IMS-ALGn applies pre-identify method
NOTE 3: The number in the brackets is codec number of the IP realm.
Steps 1a to 1e describe the progression of SDP offers via the IMS-ALGs from
UE1 to UE2 and steps 2a to 2e describe the corresponding progression of SDP
answers according to the algorithm.
### 7.3.6 Improvement to proactive transcoding
#### 7.3.6.1 Prevent additional SDP exchange
If an IMS-ALG decides to provide transcoding options per local policy when
forwarding an SDP offer, in additional of applying procedures specified in
subclause 7.3.1, the IMS-ALG shall allocate a TrGW for transcoding, and
include two additional IP realms in the forwarded SDP offer. Both additional
IP realms contain the realm identifier on the outgoing signalling path. One of
them contains the connection information for the default media path, and the
codec number is the quantity of codecs in the received SDP offer. The other,
which shall be the last IP realm in the forwarded SDP offer, contains the
connection information of the TrGW for transcoding, and the codec number is
the quantity of codecs in the forwarded SDP offer. The IMS-ALG shall not
include the behaviour indication in any of the IP realms added in the
forwarded SDP offer, and shall forward the connection information for the
default media path in the SDP offer.
NOTE 1: If a TrGW controlled by a next IMS-ALG can access the IP realm
identified by the additional IP realms, the additional IP realm for default
media path will be checked first, and this will make sure that media path not
containing transcoding TrGW(s) has priority.
An IMS-ALG may control more than one TrGWs at an IP realm boundary, some of
them are for media relay, and some of them are for transcoding. If a TrGW for
transcoding has corresponding TrGW for media relay, then the TrGW for media
relay has priority to be used except it can not support the selected codec. If
the IMS-ALG controls additional TrGWs for transcoding and they have
corresponding TrGWs for media relay, then during SDP offer forwarding phase,
the IMS-ALG may apply procedures as specified in subclause 7.3.1 to provide IP
realms for the corresponding TrGWs for media relay, and add other IP realms
for the additional TrGWs for transcoding after the two additional IP realms.
During SDP answer forwarding phase, the IMS-ALG shall apply procedures as
specified in subclause 7.3.1 with following additions:
\- if transcoding option is selected, then use the TrGW for transcoding in the
media path;
NOTE 2: To use the TrGW for transcoding in the media path, the IMS-ALG must
forward an SDP answer with the connection information of the TrGW. If the IMS-
ALG is the last one in an OMR domain, an extra SDP offer/answer transaction
may be needed.
Figure 7.3.6.1-1 shows an example call flow for preventing extra SDP
offer/answer transaction.
Figure 7.3.6.1-1: Transcoding aware -- prevent extra SDP exchange
NOTE 3: The number in the brackets is codec number of the IP realm. The IP
realms in bold are the additional IP realms, and the first contains the
connection information of the TrGW2 on outgoing leg, the second contains the
connection information of the TrGW1 on outgoing leg. The IP realms with under-
strike contain same connection information because the SDP offer in step 1b
carries the connection information of the TrGW2 on outgoing leg too. If IMS-
ALG1 does not provide TrGW2 for the default media path (IP realm 1 and IP
realm 2 are same), then the first bold realm2 contains connection information
of UE1.
Steps 1a to 1c describe the progression of SDP offers via the IMS-ALGs from
UE1 to UE2, steps 2a to 2c describe the corresponding progression of SDP
answers according to the algorithm.
#### 7.3.6.2 Move transcoding options close to the end
During SDP offer forwarding phase, an IMS-ALG may check the IP realms in the
received IP realm list one by one from the beginning, if an IP realm contains
behaviour indication, and the value of behaviour indication is not Category A
or B, the IMS-ALG may decide to prevent previous IMS-ALG(s) to perform
transcoding as follows:
NOTE: If an IMS-ALG provides Category B proactive transcoding, when
transcoding option is not selected, then the IMS-ALG may use the TrGW for
transcoding in the media path. If a next IMS-ALG executes transcoding
function, then there will be two TrGWs for transcoding in the media path,
it\'s a kind of wasting we need avoid.
\- get the codec number of the IP realm;
\- replace the codec number from the identified IP realm to the last IP realm
with the gotten codec number, and also remove all the behaviour indication;
\- offer the additional transcoding options.
This improvement has the advantage that an IMS-ALG closer to the terminating
UE, that presumably has more knowledge about the terminating networks
properties (e.g. access type, policies, terminal capabilities, etc) than
upstream nodes can influence if upstream nodes perform transcoding. For
instance, if a call was routed back to the original network only the policies
in that network could be used to select codecs, irrespective of any policies
in intermediate networks.
This improvement has the disadvantage that the original media path may not be
optimized even if it could be optimized without the improvement. An example is
when IMS-ALG2 provides transcoding options, and TrGWs controlled by from IMS-
ALG3 to IMS-ALG6 could be bypassed, but IMS-ALG5 applies the improvement and
transcoding option is selected.
#### 7.3.6.3 Eliminate additional SDP exchange based on the knowledge of
terminating networks
If an IMS-ALG, who does not provide transcoding options, has enough knowledge
about the terminating networks properties (e.g. access type, policies,
terminal capabilities, etc), and transcoding options have been provided in the
received SDP offer, and the IMS-ALG can determine whether it is better for the
terminating UE to select transcoding options or not, then the IMS-ALG may
apply procedures as specified in subclause 7.3.5.2 with following additions:
\- if it is better not to use transcoding options, and the transcoding options
are provided using Category A or B behaviour, then remove transcoding options
from the forwarded SDP offer and continue pre-identify procedures for the
whole IP realm list;
NOTE 1: This assures that the terminating side will selects one of the
original codecs, and the transcoding provider will not initiate an extra SDP
exchange, and the media path can be correctly established with OMR in one SDP
offer/answer transaction.
\- if it is better to use transcoding options, and the transcoding options are
provided using Category C behaviour, then remove original codecs from the
forwarded SDP offer and not continue pre-identify procedures;
NOTE 2: This assures that the terminating side will selects transcoding
options, and the transcoding provider will initiate an extra SDP exchange,
procedures as specified in subclause 7.3.1 and 7.3.5.1 are enough.
\- if it is better to use transcoding options, and the transcoding options are
provided using Category D behaviour, then remove original codecs from the
forwarded SDP offer and continue pre-identify procedures for the checked IP
realm list;
NOTE 3: This assures that the terminating side will selects transcoding
options, and the transcoding provider will not initiate an extra SDP exchange,
and the media path can be correctly established with OMR applied to the
outgoing media legs of the transcoding TrGW within one SDP offer/answer
transaction.
# 8 Evaluation of the Solutions
Editor\'s Note: This section will evaluate the solutions identified in
sections 6 and 7.
## 8.1 Evaluation Criteria
## 8.2 Evaluation Results
### 8.2.1 Relationship between local breakout and optimal media routeing
The scenarios for local breakout documented in Section 6.1 are not equally
effective in order to perform optimal routeing of media.
Let\'s consider a couple of users \"User A\" and \"User B\" that are roaming
in Serving A and Serving B networks respectively (see Figure 8.2.1-1) and
let\'s suppose that scenario with \"P-CSCF located in home network -- dual IP
address\" or scenario with \"P-CSCF located in home network -- single IP
address\" applies.
Figure 8.2.1-1: Optimal media routeing in roaming case.
Scenario with \"P-CSCF located in home network -- dual IP address\" or
scenario with \"P-CSCF located in home network -- single IP address\" are
characterized by IMS signalling that is transported from the UE (in VPLMN) to
the P-CSCF (in HPLMN) in a completely transparent way across the (visited and
transit) networks in between: in both scenarios IMS signalling is encrypted on
the Gm reference point and, in addition, in scenario with \"P-CSCF located in
home network -- dual IP address\" signalling is tunnelled (e.g. into GTP).
This arrangement has an architectural drawback: if UE A and UE B are assigned
globally routable IP addresses from their respective visited networks and no
SDP manipulation is performed by any IMS node, the media could go directly
from User A to User B and vice versa, according to the best optimal routeing
scenario. However, when performing this kind of OMR, we will have a media
stream crossing networks Serving A, TR-3, TR-4 and Serving B with no
associated usable IMS signalling (i.e. plain and not tunnelled) that these
networks could potentially handle to provide the appropriate authorisation of
bearer resources, QoS management and charging functions; this could lead to
serious problems for the home operators when they have to negotiate the
roaming agreement with Serving networks and the commercial agreement with the
carriers owner of the Transit networks. Furthermore in these scenarios OMR
does not rely on IMS routeing within the crossed (Serving and Transit)
networks, but only on IP routeing and IP routeing policies of the carriers: in
the worst case, the media could even be routed from Serving A to Serving B
through other transit networks different from TR-3 and TR-4, which are also
routeing the signalling; this would considerably add complexity to the
commercial settlements between involved operators and carriers. Note that this
is true of these LBO scenarios even without OMR since the home network has no
control of the transit networks used by the serving network.
On the contrary, in scenario with \"P-CSCF located in serving network --
single IP address\" IMS signalling passes through the P-CSCF in VPLMN and,
e.g. a sequence of IBCFs that can manipulate IMS signalling itself, forcing
the media stream to follow the same path as signalling. In the same way, i.e.
manipulating IMS signalling, the networks (Serving, Home or Transit) can
optimize the media stream path in a way potentially controlled by the home
operators and, in any case, making the serving and the transit networks
service aware in a way that there are no more problems of resource reservation
and charging.
Summarizing:
\- when the user is roaming and is currently served by a different operator,
scenario with \"P-CSCF located in home network -- dual IP address\" and
scenario with \"P-CSCF located in home network -- single IP address\" limit
the ability of network elements on the signalling path to control QoS and
charging for the media path; on the contrary scenario with \"P-CSCF located in
serving network -- single IP address\" enables the best control of QoS and
charging for the media path. OMR applies similarly in both cases as long as
NATs are not used in the serving network.
\- when IP GW-H and IP GW-L belong to the same serving network there is no
need to cross border elements (e.g. IBCFs) to complete an MMTel call to
another user in the same serving network; manipulation of IMS signalling is no
more needed to achieve the required QoS or charging detail, cause within the
same serving network standard IP routeing is enough.
# 9 Conclusions
## 9.1 Conclusion on LBO dual IP address solutions
Considering that:
\- LBO single IP address solutions introduced in Rel-8 [8] allows for co-
existence of IMS signalling anchored in the home network, along with media
streams anchored in the home network, in the visited network or in both
\- LBO dual IP address solutions may prevent the routeing optimization of
media or limit its effectiveness
it is recommended to not further develop in Rel-9 any LBO dual IP address
solution for the roaming case as currently described in section 6.1.1, i.e.
with IP GW-H and IP GW-L belonging to serving networks owned by different
operators.
## Conclusion on OMR
It is recommended that a combination of Alternative 1 and Alternative 2, which
are described in clauses 7.2 and 7.3, respectively, should be used as the
basis for specification of an OMR solution, as guided by the principles below.
Any remaining issues identified in clauses 7.2 and 7.3 that are still
applicable should be addressed during specification work.
  1. Whenever possible, optimisation decisions should be made during the forwarding of the SDP offer to minimize the amount of TrGW allocation and signalling required.
  2. When an IMS-ALG uses the proactive transcoding method with gateway reservation, further optimisation decisions should be made during the forwarding of the SDP answer to minimize the need for a second SDP offer/answer transaction under some cases and to otherwise reduce the signalling required for optimisation.
  3. When a second SDP offer/answer transaction is required for optimisation during transcoding, it is preferred to complete the second SDP offer/answer transaction before forwarding the SDP answer for the first SDP offer/answer transaction. SIP procedures sometimes make this difficult. This problem is associated with the proactive transcoding solutions and not specific to OMR. Solutions should be agreed for proactive transcoding and should then be applicable to OMR with transcoding.
  4. IMS-ALGs making codec list changes should clearly represent the changes in the forwarded SDP in a robust way to represent additions, deletions and reordering of codecs in the list, as well as unambiguous handling of auxiliary codecs. The details of representing the codec changes are deferred to stage 3 work.
  5. The description of SDP extensions required for OMR should be functional with representation details deferred to stage 3 work.
  6. Means of handling forking are not yet addressed and details will be handled during specification work.
  7. The Active Bypass option is not recommended for standardisation.
  8. During the forwarding of the SDP answer, the first IMS-ALG to recognize that a second SDP offer/answer transaction is required for further optimisation and that is able to successfully complete the required optimisations will initiate the second SDP offer/answer transaction.
  9. All SDP offer/answer procedures associated with OMR will follow RFC 3264 and other relevant specifications.
There may be actions at interconnect that affect OMR and examples of these are
discussed in Annex B.
###### ### Annex A: OMR use cases
# A.1 Discussion
The following clauses describe use cases to be included in the OMR feasibility
study. Figure A.1-1 below shows a configuration of networks that is used as
the basis for the use cases.
In this example the transit network (TR) provides interconnect between all of
the other networks. The dotted line shows the media path without OMR
procedures.
In each of the following use cases:
\- A network, in this context, is a network bounded by IBCF\'s/TrGW\'s.
\- The signalling path is not shown
\- It is a precondition that services are subject to local breakout
It should be noted that all of the configurations are examples only, and other
configurations are possible. It is not required that all networks in a
configuration have deployed TrGWs, but in order for optimization to be
applicable, at least two TrGWs need to have been deployed.
Figure A.1-1: Example of network configuration
# A.2 Common Transit Network
In this example the transit network provides interconnect between all of the
other networks. In Figure A.2-1 below, if a connection exists between Serving
A and B then the alternative optimized media path is possible, as shown.
Figure A.2-1: Common transit network example configuration
# A.3 Common Serving Network
In this example the transit network provides interconnect between all of the
other networks. A common serving network is being used by both users, allowing
the media path to stay within the same network.
Figure A.3-1: Common serving network example configuration
The media path may be further optimized where the users are in the same
residential or enterprise network (see Figure A.3-2). The priority for support
of this further optimization is lower than for supporting the optimization
through the serving network.
Figure A.3-2: Users in same residential/enterprise network
# A.4 Two Transit Networks (1)
In this example TR-1 provides interconnect between all of the other networks
but for restricted scenarios in the case of Home A and Home B, so TR-2 also
provides interconnect between those networks.
Figure A.4-1: Two transit networks example configuration (1)
# A.5 Two Transit Networks (2)
## A.5.1 Two Transit Networks (2) -- Example optimization
In this example TR-1 provides interconnect between Serving A and the two home
networks and TR-2 provides interconnect between Serving B and Home B only.
The optimal media path will depend on which connections are available between
networks. The media path shown by the solid line is certainly possible, and
more optimal paths are possible. For example, if there is a connection
available between TR-1 and TR-2 then the path via Home B can be eliminated.
Other optimizations are possible. They are dependent on connections existing
between networks and are shown in clause A.5.2.
Figure A.5.1-1: Two transit networks example configuration (2)
## A.5.2 Two Transit Networks (2) -- Alternative optimizations
Figure A.5.2-1: Connection between TR-1 and TR-2
Figure A.5.2-2: Connection between TR-1 and Serving B
Figure A.5.2-3: Connection between TR-2 and Serving A
# A.6 Four transit networks
In this example the four transit networks are fully interconnected. This is
envisaged as a likely scenario since each of the home and serving networks is
served by a transit network and each of the transit networks is interconnected
with the others. An optimization avoiding Home B will always be possible.
Figure A.6-1: Four transit networks example configuration
The alternative optimization shown below is dependent on a connection existing
between Serving A and TR-4. Other optimizations are possible, depending on
additional connections existing between home/serving networks and transit
networks.
Figure A.6-2: Optimization when connection exists between Serving A and TR-4
# A.7 User performs SC
In this example TR-1 provides interconnect between all of the other networks
but for restricted scenarios in the case of Home A and Home B, so TR-2 also
provides interconnect between those networks.
Access A and Access A\' belong to the same operator. If User A changes access
network (using Service Continuity procedures as specified in TS 23.237) the
new un-optimized and optimized media paths will be via Access A\'.
It is also possible that Access A and Access A\' are connected to different
transit networks.
Figure A.7-1: Before Service Continuity
Figure A.7-2: After Service Continuity
# A.8 User splits media across access networks
In this example TR-1 provides interconnect between all of the other networks
but for restricted scenarios in the case of Home A and Home B, so TR-2 also
provides interconnect between those networks.
User A is using both Serving A1 and Serving A2 to carry media, one for audio
and one for video.
It is also possible that Serving A1 and Serving A2 are connected to different
transit networks.
Figure A.8-1: User splits media across access networks example configuration
# A.9 Media server in Home A
This use case may occur in the case of a conference call being hosted in User
A\'s home network. TR-1 provides interconnect between all of the other
networks, but configurations involving more than one transit network are also
possible.
An MRF exists in User A\'s Home network. The path from User A to the MRF is
already optimal but the path from User B to the MRF can be optimized by
eliminating the loop through User B\'s Home network.
Figure A.9-1: Media server in Home A example configuration
# A.10 No Transit networks
In this example no interconnect networks are used.
The optimal media path will depend on which connections are available between
networks. The dotted line shows the unoptimized media path. The solid line
traversing all of the networks is the case where no optimization is possible
because there are no other interconnections. More optimal paths are shown by
the solid lines. For example, if there is a connection available between Home
A and Serving B then the loop through Home B can be eliminated.
Figure A.10-1: No transit networks example configuration
# A.11 Optimal media routing in PSTN local breakout
Optimal media routing based on PSTN interworking should be considered based on
the local breakout scenario documented in Section 6.1.3 involving a PSTN
interconnected with the Visited network.
It is assumed that the SIP signalling is routed from the home network back to
the visited network using existing BGCF functionality. However, to prevent
that media are also routed through the home network, a new OMR solution is
required.
Figure A.11-1 describes a local breakout scenario with PSTN interworking,
where User A is in an access network served by the Serving or Visited IMS
network, and establishes a session with User B via a PSTN connected to the
same Serving or Visited IMS network.
Figure A.11-1: Optimal media routing in a roaming case with PSTN interworking
The following description illustrates how the base OMR algorithm in clause
7.2.3 is applied in this scenario.
Each IMS-ALG involved in the signalling path will check the passing SDP offer
and add extension attributes defined in the base algorithm (clause 7.2.3) to
indicate the IP realms it connects in the signalling path.
In Figure A.11-1 IMS-ALG S detects possible media path optimization, based on
matching realm identifier in the realm attribute in the SDP offer and
determines gateways that can be bypassed. In this particular case TrGWs
associated with IMS-ALG H and IMS-ALG S can be bypassed for media path
optimization.
###### ### Annex B: Interconnect Assumptions
# B.1 Direct Interconnects
Direct interconnections may take different forms, but in principle this type
of interconnect does not require intermediate signalling functions between the
border functions of the two networks.
For direct interconnects, it is worth to note the geographical aspects. It is
of course possible to have a single direct interconnect between the core sites
of two networks. Though it is also common that several interconnects in
different geographical areas are used to interconnect two Service providers.
Furthermore, one operator cannot normally make any assumptions on how the
other operator has organized the network. Figure B.1 give a example of this.
{width="4.534027777777778in" height="2.564583333333333in"}
Figure B.1: Direct inter-connects between networks (using multiple connection
points)
# B.2 In-direct Inter-connects
## B.2.1 Interconnection over \"Internets\"
Two Service providers may of course agree to interconnect by tunnelling over
the Internet. However, when interconnecting over internet it may problematic
to provide other types of QoS than Best effort.
As no service awareness is possible, and due to security reasons some kind of
tunnels would be used between the SPs. This type of interconnect can from an
OMR perspective be seen as comparable to direct inter-connects.
## B.2.2 Interconnections over IPX networks
### B.2.2.1 General
By IPX networks, we mean here managed IP networks that provide connectivity
between Service provider networks only. There may be many different IPX
networks globally, but the general concept is that the connectivity between
the service provides is provided by one or more IPX carriers, and that the
\"traditional\" business models of the telecommunication world will be kept.
Figure B.2: Example overview of a GSMA IPX interconnect scenario.
Even though there may be several different IPX networks, the rules and
architectures of the IPX networks could be expected to be built on the GSMA
IPX principles (as depicted in Figure B.2).
For the IPX, three different interconnect modes have been defined
\- Transport mode.
\- Service transparent mode.
\- Hubbing mode.
#### B.2.2.2 Transport mode
In this mode the IPX provides a \"tunnel\" between two Service providers that
have a bilateral agreement. In this case the both Service provider would pay
fees to the IPX carrier(s) based on traffic volume on IP-level, and any call
termination fee are exchanged between the SPs without involvement of the IPX.
This case can be seen as a variant of the direct interconnect, although the
SPs may utilise some service provided by the IPX like the IPX ENUM/DNS
service.
#### B.2.2.3 Service transparent mode:
Also in this mode the basis is a bi-lateral agreement between the two Service
Providers. In this scenario, the IPX networks take active part in establishing
both the control plane and media plane connection.
To traverse and route the call across an IPX network, an IPX proxy is used.
The exact details of what an IPX proxy is, is not settled, and the
requirements of the IP Proxy is currently undergoing a review in GSMA.
#### B.2.2.4 Hubbing mode
In this mode, the originating and terminating service providers does not have
any bilateral agreements between each other. Instead the SPs have an SLA with
their IPX carrier(s). The similar SLA exists between all IPX carriers which
provide a \"cascade\" SLA between the two Service providers.
Also in this case an IPX proxy is used to traverse an IPX carrier network.
In this case the settlement method would be that SP1s IPX provider directly or
via a second IPX carrier would provide connectivity to the terminating SP.
I.e. the originating party pays transit, and termination fees to the IPX
carrier and the IPX carrier pays the terminating fee to the terminating SP.
#### B.2.2.5 Roaming Interconnections
Although the GSMA have not studied use of the interconnect modes in other
scenarios that for interconnection between Home networks, it is expected that
at least the two first modes, based on bi-lateral agreements could be expanded
to cater for roaming as well.
The main differences would be in the settlement model, where instead of a
termination fee from the originating to the terminating SP, there would be a
roaming fee from the home SP to the visited SP.
### B.2.3 Interconnection using IMS transit functionality
In additions to the IPX networks, an IMS service provider may also to some
extent offer interconnect services by means of the IMS transit routeing
capabilities. From an interconnect perspective, there would be little
difference between using IMS transit functionality, and using IPX based
interconnect in Hubbing mode.
# B.2 Actions at Interconnects that may affect OMR
## B.2.1 General
An obvious potential action at interconnects that may have effects on OMR is
the need for monitoring controlling the media streams at different
interconnect points.
The reason for monitoring media streams may be for several different reasons,
\- Security.
\- Charging.
\- QoS monitoring.
## B.2.2 Security
Secure is a basic function of interconnects and used to protect from
unauthorised access and misuse of the network. Different interconnects may
have different levels of trust between the parties involved. Border
Controllers are deployed on interconnects for the purpose of providing
security. The functions that can be used for security are among others, Access
Control Lists, Signalling/Media Inspection, NAT/NAPT, etc.
The deployment of Border Controllers to implement these functions will tend to
enforce that the media path follows signalling path, which can in some cases
work against OMR.
In particular, the deployment of Border Controllers or other intermediate
nodes **within** an Interconnect network needs to be considered. When an
interconnect network is provided by multiple Carriers, (e.g. GSMA IPX), then
it is possible that Border Controllers or other intermediate nodes are
deployed within the interconnect network and will try to enforce that the
media path follows the signalling path.
The deployment of Intermediate nodes can make it more difficult to establish
if there are alternate connectivity paths between the two endpoints.
## B.2.3 Charging
Interconnect agreements will include tariff and settlement arrangements. The
current models are based upon the assumption that the media path follows the
signalling path, and the signalling is used to generate CDRs that are used in
settlement. It is unclear how Interconnect Agreements would be set up where
the signalling goes across one set of Carriers, but the media path goes across
a different set of Carriers.
### B.2.4 QoS Monitoring
Interconnect Agreements will include QoS KPIs as part of the SLA. Carriers
need to be able to show that they are meeting the QoS KPI aspects of the SLA.
The QoS monitoring may be done via passive or active monitoring. It is unclear
where SLA responsibility lies if the media path is separately negotiated and
involves other Carriers. Even if Carriers were to contribute QoS KPI
information to a central repository that is visible to all Carriers, it may be
difficult to associate signalling paths with media paths.
The same sort of problems occurs for troubleshooting, following customer
complaints about poor media QoS.
#