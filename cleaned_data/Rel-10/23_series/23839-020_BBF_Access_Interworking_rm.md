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
The collaborative work between 3GPP and BBF resulted in a Workshop in February
2010 focusing on Fixed-Mobile Convergence. As a result of this work, it has
been identified that several working groups in 3GPP will need to work on:
requirements, architecture, security and OA&M. This TR focuses on the
architecture aspects of this study. The work includes three building blocks
containing specific aspects of the study which are to be conducted within this
technical report.
# 1 Scope
Based on requirements documented in the stage 1 specifications, this technical
report addresses system architecture impacts to support BBF Access
Interworking. The study includes multiple phases and covers aspects such as
basic connectivity, mobility, authentication and authorisation, policy and QoS
aspects, IP Flow mobility, traffic offload, convergence etc.
In each Building Block, the TR will describe what changes are expected to
normative TSs, e.g TS 23.402 and TS 23.203.
The work is divided into three separate Building Blocks. See clause 4 for an
outline of the content of each building block.
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
[2] 3GPP TS 23.401: _\"_ GPRS Enhancements for E-UTRAN Access _\"_.
[3] 3GPP TS 23 402: \"Architecture enhancements for Non-3GPP Accesses \".
[4] 3GPP TS 23.203 "Policy and charging control architecture"
[5] 3GPP TS 22.278 "Service requirements for the Evolved Packet System (EPS)"
[6] Broadband Forum WT-203 "Interworking between Next Generation Fixed and
3GPP Wireless Access" (work in progress)
[7] Broadband Forum TR-058 " Multi-service Architecture and Framework
Requirements " September 2003,
[8] Broadband Forum TR-101 "Migration to Ethernet-based DSL Aggregation" April
2006,
[9] 3GPP TS 23.261 "IP Flow Mobility and seamless WLAN offload "
[10] Broadband Forum WT-145 "Multi-service Broadband Network Functional
Modules and Architecture " work in progress,
[11] Broadband Forum WT-134 "Policy Control Framework " work in progress,
[12] 3GPP TS 25.467 "UTRAN architecture for 3G Home Node B (HNB); Stage 2"
[13] 3GPP TS 36.300 "Evolved Universal Terrestrial Radio Access (E-UTRA) and
Evolved Universal Terrestrial Radio Access Network (E-UTRAN); Overall
description; Stage 2"
[14] 3GPP TS 22.220 "Service requirements for Home Node B (HNB) and Home eNode
B (HeNB)"
[15] 3GPP TS 33.320 "Security of Home Node B (HNB) / Home evolved Node B
(HeNB)"
[16] 3GPP TS 33.210: "Network Domain Security; IP network layer security"
[17] 3GPP TS 33.310: "Network Domain Security (NDS); Authentication Framework
(AF)"
# 3 Definitions, symbols and abbreviations
## 3.1 Definitions
For the purposes of the present document, the terms and definitions given in
TR 21.905 [x] and the following apply. A term defined in the present document
takes precedence over the definition of the same term, if any, in TR 21.905
[x].
**3GPP Femto** : Refers to the HNB and HeNB NEs as defined by 3GPP. The HNB GW
is always required for the HNB architecture while the HeNB GW is option for
the HeNB.
## 3.2 Symbols
For the purposes of the present document, the following symbols apply:
## 3.3 Abbreviations
For the purposes of the present document, the abbreviations given in TR 21.905
[x] and the following apply. An abbreviation defined in the present document
takes precedence over the definition of the same abbreviation, if any, in TR
21.905 [x].
ANDSF Access Network Discovery and Selection Function
BBF Broadband Forum
BRAS Broadband Remote Access Server
BNG Broadband Network Gateway
BPCF Broadband Policy Control Function
DSMIPv6 Dual-Stack MIPv6
EPC Evolved Packet Core
ePDG Evolved Packet Data Gateway
EPS Evolved Packet System
H‑ANDSF Home-ANDSF
MME Mobility Management Entity
P‑GW PDN Gateway
PMIP/PMIPv6 Proxy Mobile IP version 6
RG Residential Gateway
S‑GW Serving GW
V‑ANDSF Visited-ANDSF
# 4 Building Blocks
The architecture study is planned to be performed within three Building
Blocks, with the following scope for each BB.
Editors note: The text below is copied from the Work Item Description
The following aspects will be covered in Building Block I:
  * **Aspects on basic connectivity, host-based mobility (S2c), and network-based mobility for untrusted accesses (S2b) on top of Release 9 baseline architecture including network discovery/selection functions and IP address allocation;**
  * **Interworking between 3GPP and BBF architectures for authentication, including identities, on top of Release 9 baseline architecture;**
  * **Policy and QoS interworking between 3GPP and BBF architectures considering the following scenarios:**
```{=html}
``` \- When H(e)NB is being used and traffic is routed back to the EPC
  * When WLAN is being used and traffic is routed back to the EPC
```{=html}
``` \- **Multi-access PDN Connectivity;**
  * **IP Flow Mobility and seamless WLAN offloading;**
  * **LIPA and SIPTO for H(e)NB with static QoS policies.**
**The following** aspects **will be covered in Building Block II (building on
interworking functionality of Building Block I):**
  * **Policy and QoS interworking between 3GPP and BBF architectures considering the following scenarios:**
```{=html}
``` \- When H(e)NB is being used and traffic is offloaded in the local
wireline network
  * When WLAN is being used and traffic is offloaded in the local wireline network (i.e. non-seamless WLAN offloading)
**The following** aspects **will be covered in Building Block III (building on
overall results of Building Block I):**
  * **Study of a potential architecture for the case of network based mobility when the BBF access is considered as trusted.**
  * **Further convergence between 3GPP and fixed network architectures beyond basic inter-working such as converged database and further architecture optimizations for operators providing both 3GPP and BBF accesses with input from BBF.**
  * **Policy and QoS interworking between 3GPP and BBF networks with considering scenarios when the services and policies are provided by the BBF network.**
# 5\. Building Block I
Editor's Note: This subclause will contain items being part of Building Block
I.
## 5.1 Architecture
> Editor's Note: This subclause will identify the architectural requirements
> and assumptions as well as architecture common for building block I. Intent
> is to capture the architectural agreements made during the 3GPP-BBF WS.
>
> Editor's Note: if the work with the proceeding building blocks concludes
> that some or all architectural requirements and assumptions can be applied
> to several building blocks then those can be moved to a new chapter
> outlining a baseline architecture for all building blocks.
### 5.1.1 Architectural requirements and assumptions for building block I
The interworking architecture is based EPC reference architecture defined in
TS 23.401 [2] and TS 23.402 [3] and on BBF access network defined by BBF
TR-058 [7], BBF TR-101 [8], WT-134 [11].
The interworking architecture support trusted and untrusted model for the
host-based mobility (S2c) and the network based mobility for the untrusted
model based on s2b. The trusted/untrusted Non-3GPP access network detection is
performed as defined in clause 4.1.4 of TS 23.402.
The architecture support an UE simultaneously connected to the EPC via more
than one access network for different PDN connection or for the same PDN
connection as defined in TS 23.261 [9].
> Editor's Note: The definition of details for supporting MAPCON in in Rel-10
> TS 23.402 and 23.401 are FFS .
The architecture supports the scenario of a single network operator deploying
both the 3GPP EPC and the BBF access network and the scenario of two network
operators one deploying the 3GPP EPC network and one deploying only the
Broadband Forum Access network. Furthermore the architecture supports the
roaming scenario between two PLMN operators.
The architecture supports local breakout of traffic in the EPC network whether
a roaming subscriber is accessing the EPC via a 3GPP or a non 3GPP access
network according to the design principles described in clause 4.1 of TS
23.401.
The reference architecture for the support of HeNB is defined in TS 23.401 and
TS 36.300 [13], for the support of HNB in TS 23.060 and TS 24.467 [12]
> Editor's Note: The reference architecture for LIPA and SIPTO for local
> network is under study in TR 23.829, so the inclusion in this reference
> architecture is FFS.
### 5.1.2 Architecture for building block I BBF interworking via WLAN access
connection
The Figure 5.1.2.-1, 5.1.2-2 and 5.1.2-3 show the reference architecture for
the non-roaming scenario and with the traffic routed to the mobile core
network. The figure 5.1.2-4. 5.1.2-5 and 5.1.2-6 show the reference
architecture for the roaming scenario with the traffic routed to the home
network. The figure 5.1.2-7, 5.1.2-8 and 5.1.2-9 show the reference
architecture for the roaming scenario with the local breakout in Visited PLMN.
> Editor's Note: The reference architecture for LIPA and SIPTO for local
> network is FFS. For more detail refer to 3GPP TR 23.829.
The following considerations apply to interfaces and reference points where
they occur in figures in this clause:
\- S5 and S8 can be GTP-based or PMIP-based.
\- Gxc is used only in the case of PMIP variant of S5 or S8.
\- Gxb* is only needed in case the S9* session is initiated from the PCRF
towards the BPCF.
Editor's note: It is FFS if there are other means than Gxb* to trigger
initialisation of the S9* session from PCRF when using untrusted access
procedures
\- S9 is used between the H-PCRF and V-PCRF in roaming scenario
\- S9* (used between 3GPP and BBF domains) is used between the PCRF and BPCF*
in scenarios where both 3GPP and BBF access networks belong to the same
operator or to different operators.
\- the reference points internal to the BBF access network are defined or are
under definition by Broadband Forum and are out of the scope of this Technical
Report.
NOTE 1: SWu shown in Figure 5.1.2-1 also applies to architectural reference
for untrusted scenario in Figures 5.1.2-3, 5.1.2-4, 5.1.2-6, 5.1.2-7 and
5.1.2-9, for the untrusted scenario with s2c but is not shown for simplicity.
> The ANDSF is not shown in any of the following figures, but it may be used
> in all architectural variants, according to the principles defined in 3GPP
> TS 23.402.
Figure 5.1.2-1: Non-Roaming Architecture for untrusted BBF access network
based on S2b
NOTE 2: The reference architecture is applicable when the 3GPP and BBF access
networks belongs to the same network operator or to different network
operators
Figure 5.1.2-2: Non-Roaming Architecture for trusted BBF access network based
on S2c
NOTE 3: The reference architecture is applicable when both 3GPP and BBF
network belongs to the same network operator or to different network operators
NOTE 4: The connection between the BRAS/BNG and PDN Gateway is IP transport
connection
Figure 5.1.2-3: Non-Roaming Architecture for untrusted BBF access network
based on S2c
NOTE 5: The reference architecture is applicable when both 3GPP and BBF
network belongs to the same network operator or to different network operators
Figure 5.1.2-4: Roaming Architecture for untrusted BBF access network based on
S2b -- Home routed traffic
NOTE 6: The reference architecture is applicable when both 3GPP and BBF
network belongs to the same VPLMN network operator or to different network
operators
Figure 5.1.2-5: Roaming Architecture for trusted BBF access network **using
s2c - Home Routed**
NOTE 7: The reference architecture is applicable when both 3GPP and BBF
network belongs to the same VPLMN network operator or to different network
operators
NOTE 8: The connection between the BRAS/BNG and PDN Gateway is a IP transport
connection
Figure 5.1.2-6: Roaming Architecture for untrusted BBF access network **using
s2c - Home Routed**
NOTE 9: The reference architecture is applicable when both 3GPP and BBF
network belongs to the same VPLMN network operator or to different network
operators
Figure 5.1.2-7: Roaming Architecture for untrusted BBF access network **using
s2b -- Local breakout in V-PLMN**
NOTE 10: The two Rx instances in Figure 5.1.2-7 apply to different application
functions in the HPLMN and VPLMN.
NOTE 11: The reference architecture is applicable when both 3GPP and BBF
network belongs to the same VPLMN network operator or to different network
operators .
Figure 5.1.2-8: Roaming Architecture for trusted BBF access network **using
s2c -- Local breakout in V-PLMN**
NOTE 12: The reference architecture is applicable when both 3GPP and BBF
network belongs to the same VPLMN network operator or to different network
operators.
NOTE 13: The two Rx instances in Figure 5.1.2-8 apply to different application
functions in the HPLMN and VPLMN.
NOTE 14: The connection between the BRAS/BNG and PDN Gateway is a IP transport
connection
Figure 5.1.2-9: Roaming Architecture for untrusted BBF access network **using
s2c -- Local breakout in V-PLMN**
NOTE 15: The reference architecture is applicable when both 3GPP and BBF
network belongs to the same VPLMN network operator or to different network
operators.
NOTE 16: The two Rx instances in Figure 5.1.2-9 apply to different application
functions in the HPLMN and VPLMN.
### 5.1.3 Architectures for H(e)NB interworking
#### 5.1.3.1 Architecture Alternative 1 -- H(e)NB specific policies
##### 5.1.3.1.1 General Principles
The principle behind this architecture assumes that the relationship towards
the fixed access is with the mobile network / H(e)NB operator and not
individual UEs connecting to the H(e)NB. This is especially true if inbound
roamers are permitted to CSG resources.
Since H(e)NB traffic is encapsulated within IPSec whilst traversing the BBF
access, the BRAS/BNG is not able to recognise UE specific traffic when using
the H(e)NB. The policies in this alternative are defined to be H(e)NB specific
and therefore an entity within the H(e)NB subsystem is responsible for the
policy interactions.
The normal PCC architecture, servicing UEs, has no direct interaction with the
3GPP-BBF interworking solution.
The architecture highlights the S9* interface between a H(e)NB policy function
and the BBF PCF (BPCF) for H(e)NB access. The H(e)NB policy function performs
control based on bearers (EPS bearers or PDP contexts) made visible to it.
Editor\'s Note: The node which the H(e)NB PCRF connects into within the H(e)NB
subsystem is FFS along with the reference point that uses i.e. either Rx or
Gx.
The function of the S9* interface is to convey sufficient information to the
BPCF to enable it to identify the BNG the H(e)NB connects to, and perform
admission control based on the bandwidth requirements and QoS attributes of
the bearers or aggregate of bearers with similar QoS characteristics being
established.
The reference architecture focuses on the policy management aspects of the
3GPP-BBF interworking for the packet domain only.
NOTE 1: For HeNB, a HeNB GW may be required to enable BBF interworking
NOTE 2: UE policies applied at the PCRF and the P-GW are independent of H(e)NB
policy function operations
NOTE 3: There may be 2 S9* sessions for a single UE if the UE is
simultaneously connected via H(e)NB and some other access means connected to
the same BBF connection e.g. WLAN.
NOTE 4: An assumption is made that a mapping between IP address used by the
H(e)NB connection (outer IPSec header) and the H(e)NB is made available to
policy architecture.
##### Non-Roaming
Figure 5.1.3.1.2-1 Non-Roaming
NOTE 1: Not all the 3GPP reference points are shown or labelled in Figure
5.1.3.1.2-1.
NOTE 2: The CS domain is not applicable for the HeNB.
##### 5.1.3.1.3 Roaming -- Home Routed Traffic
Figure 5.1.3.1.3-1 Roaming -- Home Routed Traffic
NOTE 1: Not all the 3GPP reference points are shown or labelled in Figure
5.1.3.1.3-1.
NOTE 2: The CS domain is not applicable for the HeNB.
##### 5.1.3.1.4 Roaming -- Visited Access/LBO
Figure 5.1.3.1.4-1 Roaming -- Local breakout
NOTE 1: Not all the 3GPP reference points are shown or labelled in Figure
5.1.3.1.4-1.
NOTE 2: The CS domain is not applicable for the HeNB.
##### 5.1.3.1.5 Interworking functions
###### 5.1.3.1.5.1 H(e)NB policy function
**[General]{.underline}**
The role of the H(e)NB policy function is to convert bearer information (as
received on the S1-MME or Iu) into generic QoS authorisation requests. If no
BPCF is discovered then the H(e)NB policy function will take no further
authorisation decisions and positively acknowledge the bearer action towards
the H(e)NB GW / MME.
The H(e)NB may apply policies associated with the identified fixed access
operator before forwarding any QoS authorisation requests to the BPCFs. The
H(e)NB may perform one or more of the following:
\- Request QoS authorisation on a per bearer basis (e.g. for GBR bearers)
\- aggregate a new bearer action into an existing authorisation for the same
H(e)NB and not forward the request to BPCF (e.g. for non-GBR bearers where the
addition of a bearer does not exceed the resources already authorised)
\- aggregate a new bearer action into an existing authorisation for the same
H(e)NB and forward the request to the BPCF (e.g. for non-GBR bearers where the
new aggregate resource is greater than that which was authorised previously)
\- Reject the bearer action if deemed out of policy for H(e)NB operation (e.g.
VoIP is not permitted over H(e)NB).
NOTE 1: The H(e)NB policy function may apply different actions depending on
whether the request is pertaining to a UE that is accessing the open or closed
side of the H(e)NB, but requires the CSG membership to be signalled from the
node performing access control. For example, H(e)NB policy may map temporary
members / non-members to the lowest priority aggregate whilst a permanent
member maps to the highest priority aggregate.
Editor's Note: It is FFS if and how the CSG membership information will impact
admission control in both H(e)NB policy function and BBF access.
NOTE 2: The H(e)NB policy function is a logical function and may be physically
located independently, within the H(e)NB GW or within a PCRF.
**[BPCF discovery]{.underline}**
The BPCF is discovered by the H(e)NB policy function using the IP address
assigned to the CPE (or H(e)NB if the CPE is operating in bridge mode).
###### 5.1.3.1.5.2 BPCF
Operates as per normal with no H(e)NB specific requirements.
###### 5.1.3.1.5.3 H(e)NB
DSCP marking appropriate for the QoS of the PDP context / EPS bearer in both
inner and outer IP header of the IPSec connection for the UL packets. The
mapping between QoS and DSCP needs to be configured in the H(e)NB (e.g. via
the management system).
###### 5.1.3.1.5.4 H(e)NB GW
The H(e)NB GW passes all bearer activations / modifications / deactivations
towards the H(e)NB policy function for authorisation.
The H(e)NB GW shall select the same H(e)NB policy function for all requests
associated to a H(e)NB.
DSCP marking appropriate for the QoS of the PDP context / EPS bearer.
###### 5.1.3.1.5.5 SeGW
If present, Updates the H(e)NB of the current binding between the IP address
assigned to the CPE (outer IP address) and the IP address assigned to the
H(e)NB (inner IP address) within the H(e)NB subsystem. If the SeGW resides
within the H(e)NB GW, then the H(e)NB GW shall perform in addition the
functions associated with the SeGW.
Editor\'s Note: It is FFS whether this mechanism is necessary or can be
handled through the management system.
Copying the DSCP marking on received DL packets to the outer IP header of the
IPSec tunnel.
###### 5.1.3.1.5.6 MME
If the HeNB GW is not present in a deployment or the S1-MME is encrypted
between MME and HeNB, the MME performs the same functions as the H(e)NB GW as
specified in clause 5.x.2.3.
If the HeNB GW is present in a deployment, there are no H(e)NB interworking
specific requirements on the MME.
###### 5.1.3.1.5.7 SGSN
Due to the mandatory presence of the HNB GW, there are no additional
requirements on the SGSN
###### 5.1.3.1.5.8 MSC
Due to the mandatory presence of the HNB GW, there are no additional
requirements on the MSC
##### 5.1.3.1.6 Reference Points
###### 5.1.3.1.6.1 S9*
**[General]{.underline}**
An S9* session (for the purpose of H(e)NB interworking) represents an
individual H(e)NB and is established for the duration of the H(e)NB being
powered up and connected to the H(e)NB GW/MME. This avoids the need for the
BPCF to discover the H(e)NB policy function and also does not require the
H(e)NB to be specifically identifiable in the fixed access.
Editor's Note: The exact model under which the S9* operates is for further
study.
**[Information Transfer over S9*]{.underline}**
If the Iuh and S1-U is secured with an IPsec tunnel, it is not necessarily
possible to identify individual PDP contexts or EPS bearers at IP level.
Therefore the flow description for authorisation over S9* will contain only
the source and destination IP address (of CPE and H(e)NB GW / MME) and the
DSCP marking on the outer IP header.
However, if the Iuh and S1-U relies on Layer 2 security, then individual PDP
contexts or EPS bearers could be identified if the BNG/BRAS performs packet
inspection to the level of the GTP header, but would require extensions to
existing filtering information. Alternatively it reuses the DSCP marking for
the IPSec case.
###### 5.1.3.1.6.2 S? (H(e)NB GW / MME to H(e)NB policy function)
This reference point is similar to the Rx reference point. A session on S? is
equivalent to each bearer as seen by the H(e)NB GW or MME. In addition to
signalling bearer actions, the H(e)NB GW / MME includes an indication of the
membership status to the CSG of the UE for which the bearer action is being
performed.
#### 5.1.3.2 Architecture Alternative 2 -- Femto Architecture Diagrams
##### 5.1.3.2.1 General
The architecture diagrams highlight the S9* interface between the PCRF and the
BBF PCF (BPCF) for Femto accessto support use cases and requirements per
WT-203 [6], 3GPP TS 22.220 [14] and 3GPP TS 22.278 [5].
The function of the S9* interface is to convey sufficient information to the
BPCF to enable it to identify the BBF network elements the 3GPP Femto connects
to, and perform admission control based on the BW requirements and QoS
attributes of a new/modified UE service data flow/s (via the 3GPP Femto).
The reference architecture focuses on the policy management aspects of the
3GPP-BBF interworking for the packet domain only.
Editor's note: The change to the reference architecture required to support
3GPP Femto location verification requirements per 3GPP TS 33.320 [15] is FFS
The following notes apply to all diagrams in the subsections below.
NOTE 1: The assumption is that the BBF BNG may be enhanced to support new
functionality such as provisioning of policies from the BPCF.
NOTE 2: For simplicity, the connection between the HNG GW and the SGSN over
the Iu-PS interface is not shown
NOTE 3: The diagrams are based on the architecture diagrams agreed at the
3GPP-BBF workshop
NOTE 4: The connection between the BRAS/BNG and the SecGW is IP transport
connection
NOTE 5: When the 3GPP and BBF access networks belong to different Service
Providers security arrangement are analogous to those between the H-PCRF and
the V-PCRF, and can be based on 3GPP TS 33.210 [16] or 3GPP TS 33.310 [17]
.
##### 5.1.3.2.2 Non-Roaming
Figure 5.1.3.2.2-1 Non-Roaming
NOTE 5: The reference architecture is applicable when both 3GPP and BBF
network belong to the same network operator or to different network operators
##### 5.1.3.2.3 Roaming -- Home Routed Traffic
The GTP version of the architecture for the macro network does not require
vPCRF in the connection because the HPLN does not provision QoS rules in the
VPLMN. Since there is no vPCRF in VPLMN the solution relies on the hPCRF to
initiate the S9 session to a selected vPCRF that, in turn, initiates the S9*
session with the BPCF. The HPLMN may provision policies in the VPLMN that take
into account the fact that the UE connects to a 3GPP Femto.
Editor's note: It is FFS whether an alternative would not require the S9
interface
Figure 5.1.3.2.3-2 Roaming -- Home Routed Traffic
NOTE 6: The reference architecture is applicable when both 3GPP VPLMN and BBF
network belong to the same network operator or to different network operators
Editor's note: It is FFS how the H-PCRF discovers the V-PCRF for the GTP
version of the Architecture
Editor's note: It is FFS to determine the S9 enhancements to trigger the
H-PCRF -- V-PCRF interface for the GTP version of the Architecture
##### 5.1.3.2.4 Roaming -- Visited Access/LBO
The H-PCRF need not aware the UE is connected via the 3GPP Femto in the VPLMN
unless SPs require provisioning of HPLN policies in the VPLMN.
Figure 5.1.3.2.4-1 Roaming -- Visited Access/LBO
NOTE 7: The reference architecture is applicable when both 3GPP VPLMN and BBF
network belong to the same network operator or to different network operators
#### 5.1.3.3 Architecture Alternative 3 -- H(e)NB specific policies
##### 5.1.3.3.1 General Principles
Since H(e)NB traffic is encapsulated within IPSec whilst traversing the BBF
access, the BRAS/BNG is not able to recognise UE specific traffic when using
the H(e)NB. The policies in this alternative are defined to be H(e)NB specific
and therefore H(e)NB is responsible for the policy interactions.
The normal PCC architecture, servicing UEs, has no direct interaction with the
3GPP-BBF interworking solution.
The architecture highlights the S9* interface between a H(e)NB policy function
and the BBF PCF (BPCF) for H(e)NB access. The H(e)NB policy function performs
control based on bearers (EPS bearers or PDP contexts) made visible to it.
The function of the S9* interface is to convey sufficient information to the
BPCF to enable it to identify the BNG the H(e)NB connects to, and perform
admission control based on the bandwidth requirements and QoS attributes of
the bearers or aggregate of bearers with similar QoS characteristics being
established.
The reference architecture focuses on the policy management aspects of the
3GPP-BBF interworking for the packet domain only.
NOTE 1: UE policies applied at the PCRF and the P-GW are independent of H(e)NB
policy function operations
NOTE 2: There may be 2 S9* sessions for a single UE if the UE is
simultaneously connected via H(e)NB and some other access means connected to
the same BBF connection e.g. WLAN.
NOTE 3: An assumption is made that a mapping between IP address used by the
H(e)NB connection (outer IPSec header) and the H(e)NB is made available to
policy architecture.
  1. ##### Non-Roaming
Figure 5.1.3.3.2-1 Non-Roaming
NOTE 1: Not all the 3GPP reference points are shown or labelled in Figure
5.1.3.1.2-1.
NOTE 2: The CS domain is not applicable for the H(e)NB.
  1. ##### Roaming -- Home Routed Traffic
Figure 5.1.3.x.3-1 Roaming -- Home Routed Traffic
NOTE 1: Not all the 3GPP reference points are shown or labelled in Figure
5.1.3.1.3-1.
NOTE 2: The CS domain is not applicable for the H(e)NB.
##### Roaming -- Visited Access/LBO
Figure 5.1.3.1.4-1 Roaming -- Local breakout
NOTE 1: Not all the 3GPP reference points are shown or labelled in Figure
5.1.3.1.4-1.
NOTE 2: The CS domain is not applicable for the H(e)NB.
##### 5.1.3.3.5 Network elements
The 3GPP network elements are defined in details in 3GPP TS 23.401 and 3GPP TS
23.402.
The BBF network elements BRAS, BNG, RG, BPCF* are defined in details in BBF
TR-058, TR-101, WT-145 [7] and WT-134.
The newly introduced and enhanced network elements are defined as below:
**[SeGW]{.underline}**
Except for the functions defined in TS33.320, the SeGW has the extra
functions:
> If the IPSec tunnel between the H(e)NB and SeGW transverses NAT, the SeGW
> sends the IPsec tunnel information (IPSec tunnel outer IP address, H(e)NB IP
> address allocated by MNO) to the H(e)NB PF via the T1 interface during the
> IPSec tunnel establishment after the H(e)NB powers on. The IPSec tunnel
> outer IP address is used to identify the BBF BPCF serving the H(e)NB, and
> will be forwarded to BBF BPCF to enable it to identify the backhaul to which
> the H(e)NB connects.
**[H(e)NB]{.underline}**
The H(e)NB shall have the following extra functions:
> If the H(e)NB receives Session Management request from the H(e)NB
> GW/MME/SGSN, e.g. S1: Create Bearer Request, Iu:RAB assignment request, the
> H(e)NB will sent the requested "bandwidth requirements and QoS attributes"
> in the "Resource allocation Request" signalling to the H(e)NB PF via the T2
> interface for admission control of the requested resources in fixed network.
>
> After the H(e)NB receives the "Resource allocation Response" from the H(e)NB
> PF, the H(e)NB will admit or reject the S1 request based on the result from
> the H(e)NB PF.
**[H(e)NB PF]{.underline}**
After receives IPsec tunnel information from the SeGW, the H(e)NB PF shall
initiate the S9* session establishment with BBF BPCF and forward the "IPsec
tunnel information" together with the H(e)NB IP address allocated by the SeGW
to the BBF BPCF in the S9* signalling. The "IPSec tunnel information" will be
used as an identification of the fixed line to which the H(e)NB is connected,
and is associated with the S9* session of the H(e)NB. The H(e)NB PF shall also
store the mapping between the S9* session and the H(e)NB IP address allocated
by the SeGW, the H(e)NB PF may also store the "IPSec tunnel information".
The H(e)NB PF associates the "Resource allocation Request" received from
H(e)NB with corresponding S9* session according to the H(e)NB IP address
allocated by the SeGW, and forward the "Resource allocation Request" the BPCF
via the S9* session.
The H(e)NB PF discovers the BPCF serving the H(e)NB based on IPsec tunnel
information.
**[BPCF]{.underline}**
It is assumed that the BPCF can make a mapping between IP address used by the
H(e)NB connection (outer IPSec header) and the physical line to which the
H(e)NB is connected.
##### 5.1.3.3.6 Reference Point
The reference points S1-MME, S1-U, S3, S4, S10, S11 are defined in TS 23.401 .
The reference points S2b, S2c, S6a, S6b, SWx, SWa, SWm, SWn, SWu, SGi, Rx, Gxc
are defined in TS 23.402.
The newly introduced and enhanced network elements are defined as below:
**[T1 interface:]{.underline}**
Interface T1 is between H(e)NB PF and SeGW, and is used to convey IPsec tunnel
information from SeGW to H(e)NB PF.
**[T2 interface:]{.underline}**
Interface T2 is between H(e)NB and H(e)NB PF, and is used request admission
control in fixed network for a certain service data flow or bearer.
**[S9* interface:]{.underline}**
It provides transfer of dynamic QoS control policies (QoS) from the H(e)NB
Policy Function to the BBF Policy BPCF. The S9* is based on enhancement of S9
reference point for supporting interworking with BBF Policy Framework
### 5.1.4 Network Elements
The 3GPP network elements are defined in details in 3GPP TS 23.401 and 3GPP TS
23.402.
To support initiation of S9* session from the PCRF when using untrusted access
procedures, the ePDG is enhanced to transport the access information of the
UE, e.g. the outer header of the IP-sec tunnel, to the PCRF via the Gxb*
reference point.
> Editor's Note: The enhancement of PCRF for supporting interworking with BBF
> Policy Framework is FFS
>
> Editor's Note: It is FFS if the PDN GW and ePDG need enhancement for
> supporting QoS management for interworking with BBF access network
>
> Editor's Note: It is FFS if there are other ways to trigger the initiation
> of S9* session from the PCRF when using untrusted access procedures.
The BBF network elements BRAS, BNG, RG, BPCF* are defined in details in BBF
TR-058, TR-101, WT-145 [7] and WT-134.
> Editor's Note: It is FFS how to capture the 3GPP assumptions on the BBF
> access network elements functionalities.
The BBF device represents any devices defined by broadband Forum or supported
by BBF access, as a PC, Media center, etc, and they are considered outside the
scope of 3GPP.
NOTE: The definition of BPCF*for enhancements to support Policy & QoS
interworking with mobile networks is under discussion in BBF WT-134 [8]
### 5.1.5 Reference Points
The reference point S1-MME, S1-U, S3, S4, S10, S11 are defined in TS 23.401 .
The reference points S2b, S2c, S6a, S6b, SWx, SWa, SWm, SWn, SWu, SGi, Rx, Gxc
are defined in TS 23.402.
**Gx** It provides transfer of dynamic QoS control policies (QoS) and charging
rules from PCRF to Policy and Charging Enforcement Function (PCEF) in the PDN
GW.
**Gxb*** It connects the ePDG with the PCRF and transports access information,
e.g. the outer header of the IPSec tunnel. It is only used for scenarios in
which the S9* session is initiated from PCRF when using untrusted access
procedures.
**S9** It provides transfer of dynamic QoS control policies (QoS) and charging
control information between the Home PCRF and the Visited PCRF in order to
support local breakout function. In all other roaming scenarios, S9 has
functionality to provide dynamic QoS control policies from the HPLMN.
> Editor's Note: It is FFS whether the enhancement of reference points S9 and
> Gx is required for supporting interworking with BBF access network.
**S9*** For building block 1 it provides transfer of dynamic QoS control
policies (QoS) from the Home PCRF to the BBF Policy BPCF and in roaming
scenario from the Visited PCRF and to the BBF Policy BPCF function in order to
provide the interworking between PCRF and the BBF policy framework. The S9* is
based on enhancement of S9 reference point for supporting interworking with
BBF Policy Framework.
> NOTE: In Building Block 1 traffic is routed back to EPC and charging control
> is done by HPLMN.
**SWa** It connects the BBF AAA proxy with the 3GPP AAA Server/Proxy and
transports access authentication, authorization and charging-related
information in a secure manner.
**STa** It connects the BBF AAA proxy with the 3GPP AAA Server/Proxy and
transports access authentication, authorization, mobility parameters and
charging-related information in a secure manner.
> The Reference points within the BBF access network are defined in BBF
> TR-058, TR-101, WT-145 and WT-134 and they are considered out of the scope
> of 3GPP.
## 5.2 Policy and QoS interworking between 3GPP and BBF architectures
Editors note: The assumption is that an "item" would correspond to a bullet of
BB1 as described in clause 4.
### 5.2.1 Description
Editor's Note: This clause will describe the description for the item.
This item covers Policy and QoS interworking between 3GPP and BBF
architectures for the following two scenarios:
  * When H(e)NB is being used and traffic is routed back to the EPC.
  * When WLAN is being used and traffic is routed back to the EPC
### 5.2.2 Solution
Editor's Note: This clause will describe the solution(s) for the item.
#### 5.2.2.1 Policy interworking principles
##### 5.2.2.1.1 PCRF -- BPCF Functional split
PCRF is the policy and charging control element in 3GPP network. PCRF
functions are described in more detail in TS 23.203 [4]. This clause points
out new functionality as well as some of the existing functionality applicable
to BBF access interworking. (Note that not all applicable existing
functionality is included below).
The BPCF is a policy control entity in the BBF network. This clause describes
functionality assumed to reside in the BPCF to support 3GPP-BBF interworking.
In a non-roaming scenario, the functionality of PCRF includes:
  * Policy decision and PCC Rule generation e.g. based on the information received from the AF via Rx, operator policies and subscription information via Sp (this is existing functionality described in TS 23.203).
  * Installation of PCC Rules in the PCEF over Gx (this is existing functionality described in TS 23.203).
  * Sends the QoS rules to the BPCF over S9* to request admission control in the fixed access.
  * Sends outer IP header information for tunnelled traffic (e.g. UE local IP address) to allow the BBF access to identify the UE traffic that is tunnelled.
Editor's note: Tunnel header information for S2c with trusted non-3GPP access
procedures is already supported on S9 since rel-8. The detailed information
needed for untrusted access procedures is FFS.
The functionality of the BPCF includes the following:
  * Performs admission control in fixed access or delegates admission control decision to other BBF nodes (this aspect is out of scope to 3GPP). Based on the admission control, the BPCF accepts or rejects the request received over S9*. As with current S9, the BPCF may include the acceptable QoS in the reply if the request is rejected.
  * May translate QCI, bit rates, and ARP into access specific QoS parameters applicable in the BBF domain (this aspect is out of scope of 3GPP).
  * May install Policy Filters and QoS for a 3GPP UE session over R interface (this aspect is out of scope to 3GPP).
Additional clarifications are needed for the roaming scenario, where both H-
and V-PCRF are available. No business agreement between HPLMN and BBF operator
for roaming scenario is assumed. In a roaming scenario, the functionality of
the H-PCRF includes the following:
  * Generates PCC Rules based on the information received from the AF via Rx or via S9, operator policies and subscribed information via Sp (this is existing functionality described in TS 23.203).
  * For home routed access, installs PCC Rules in the PCEF over Gx. (this is existing functionality described in TS 23.203).
  * For visited access (local breakout), sends PCC Rules to the V-PCRF over S9 (this is existing functionality described in TS 23.203).
  * For home routed access, sends QoS rules to the V-PCRF to request admission control over S9. (This is new for GTP-based access).
  * For BPCF-initiated S9* session establishment, sendsouter IP header information for tunnelled traffic (e.g. UE local IP address).
The functionality of V-PCRF includes the following:
  * For visited access (local breakout), installs PCC Rules in the PCEF over Gx. (this is existing functionality described in TS 23.203)
  * Applies local policies based on the roaming agreement with HPLMN. Also applies local policies based on the business agreement with BBF operator.
  * Sends QoS rules to the BPCF over S9* to request admission control in the fixed access.
  * For PCRF-initiated S9* session establishment using Gxb*, establishes Gxb* session with the ePDG to receive outer IP header information for tunneled traffic (e.g. UE local IP address).
  * For PCRF-initiated S9* session establishment, sends outer IP header information for tunneled traffic (e.g. UE local IP address) to the BPCF.
The functionality of the BPCF in a roaming scenario would remain the same as
in the non-roaming scenario.
##### 5.2.2.1.2 Procedures on S9*
[General]{.underline}
Even though S9* is based on S9, all the S9 procedures and Information Elements
may not be applicable to BBF accesses. For example, many of the Information
Elements used on S9 applies primarily to 3GPP accesses and other wireless
accesses. On the other hand, new procedures and IEs may need to be added to S9
in order to support BBF accesses. As part of this paper, we will identify the
parts of S9 that do not apply for BBF accesses and those aspects that are
currently missing on S9.
In Building Block 1, policy interworking is considered only for scenarios were
traffic is routed back via EPC. In this case charging will be performed in the
PDN GW and it is reasonable to assume that sending QoS-rule type of
information over S9* is sufficient. Therefore the Gxx variant of S9 is
applicable for Building Block 1. The Rx and Gx parts of the S9 reference point
are not applicable for S9* in the scope of Building Block 1. Below we discuss
the different procedures defined for S9 in TS 23.203 when the Gxx-variant
applies. Note that in TS 23.402 and 23.203, for the home routed case, the same
stage 2 procedures are used over Gxx and S9 reference points. On stage 3
however, they are implemented with different Diameter applications (Gxx
Diameter application and S9 Diameter application. In this contribution we use
stage 2 language and thus keep the same name also for the procedures on S9*.
Note however that there is no assumption that BBERF functionality such as
bearer binding is supported by the fixed access. How S9* is implemented on
stage 3 level is out of scope for this document.
[BPCF-Initiated Gateway Control Session Establishment]{.underline}
The Gateway Control Session Establishment is initiated from the BPCF for S9*
and results in that an S9* session is established. In order for the BPCF to
trigger establishment of an S9* session, it needs to become aware that a 3GPP
UE has attached via the BBF access and the IMSI of the subscriber. The BBF
access network may become aware of the UE if 3GPP-based access authentication
(EAP-AKA/AKA') is performed. For these scenarios the BPCF can initiate the S9*
session using the BPCF-Initiated Gateway Control Session Establishment
procedure.
Editor's note: The feasibility to support 3GPP-based access authentication for
BBF access interworking should be verified with BBF. In the non-roaming case,
the BPCF discovers a suitable PCRF domain based on UE NAI realm part. In the
roaming case, the BPCF discovers a V-PCRF based on configuration, e.g. by
mapping the UE NAI realm part to a suitable VPLMN. However, in some scenarios
EAP is not supported in the WLAN/fixed access and the UE may be located behind
a routed Residential Gateway. In these cases it may be difficult for the BPCF
to detect that a 3GPP UE has connected. .
Editor's note: S9* session setup for these scenarios is FFS. Also, S9* session
setup when UE is accessing over H(e)NB is FFS
The information contained in the request message include e.g. IMSI, IP-CAN
type and local UE IP address. The reply message contains the result code and
may also include QoS Rules as described in TS 23.203.
As a result of the S9* session establishment, the fixed access (BPCF and BNG)
is able to associate the aggregate IP traffic plane (tunnel) used by a 3GPP UE
with the S9* session towards the PCRF.
Figure 5.2.2.1.2-1 BPCF-Initiated GW Control Session Establishment
[PCRF-Initiated Gateway Control Session Establishment]{.underline}
In case the BBF access network does not perform 3GPP-based access
authentication, the BBF access network will not be aware that a 3GPP UE has
attached via the BBF access and will not know the IMSI of the subscriber. In
this case, the PCRF-Initiated S9* session establishment procedure shall be
performed. When using untrusted access procedures, the establishment of Gxb*
session initiated by ePDG triggers the PCRF to initiate S9* session
establishment with the BPCF. When using trusted access with S2c procedures,
the IP-CAN session establishment will trigger the PCRF to initiate the S9*
session establishment. The PCRF can initiate the S9* session using the PCRF-
Initiated Gateway Control Session Establishment procedure. The PCRF discovers
the BPCF serving the UE based on the UE location information provided by the
ePDG via Gxb* reference point (e.g. the outer IP header information of IPSec
tunnel) for untrusted access, or the care of address of the UE provided by the
PDN GW via Gx reference point for trusted access.
Editor's note: It is FFS whether there is other ways to send the IPSec tunnel
Outer IP address to the PCRF and trigger the PCRF to establish the S9* session
toward BPCF when untrusted access is used.
The information contained in the request message sending from the PCRF to the
BPCF includes e.g. IMSI, IP-CAN type, local UE IP address or the outer IP
header information for tunneled traffic or CoA, and QoS Information (e.g. QoS
Rules ) as described in TS23.203. The reply message contains the result code
which indicates whether PCRF-Initiated Gateway Control Session establishment
is successful or not.
As a result of the S9* session establishment, the fixed access (e.g. BPCF and
BNG) is able to associate the aggregate IP traffic plane (tunnel) used by a
3GPP UE with the S9* session towards the PCRF.
Figure 5.2.2.1.2-2 PCRF-Initiated GW Control Session Establishment
When using trusted access with S2c procedures, the Trigger in figure
5.2.2.1.2-2 is the IP-CAN Session establishment from the PDN GW. When using
untrusted access procedures, the Trigger in figure 5.2.2.1.2-2 is the Gxb*
session establishment from the ePDG.
[GW Control and QoS Rules Provisioning (admission control
request)]{.underline}
This procedure would be initiated by the PCRF (non-roaming) or by the V-PCRF
(roaming) for S9*. The PCRF requests the BPCF to perform admission control.
The BPCF takes into account the information contained in the QoS rule but the
details for how admission control is performed in the BBF access is out of
scope to 3GPP. If the request is accepted the BPCF may provision the BNG with
information to allow identification of the traffic flows for a UE and QoS
parameters.
Figure 5.2.2.1.2-3 GW Control and QoS Rule Provisioning
The GW Control and QoS Rule Provisioning includes the following information:
  * QoS-Rule with the QoS information (QCI, GBR, MBR, ARP).
  * Information (e.g. Session ID) that allows the BPCF to associated the request with the existing S9* session so that the fixed access can identify the traffic plane resources that are affected. For encrypted tunnels (for H(e)NB and untrusted access), there is no immediate need to provide the SDF filters. It is sufficient if the BBF access can associate the request with the right session and perform admission control.
Editor's note: The assumptions about QoS treatment performed by the BNG of the
3GPP UE traffic may need to be further clarified. The exact QoS information
that is included in the message to support QoS handling in the BBF access when
using encrypted tunnels is FFS.
[BPCF-Initiated Gateway Control Session Termination]{.underline}
This procedure would be initiated by the BPCF to terminate a S9* session. The
trigger in BPCF for initiating this procedure may be that the 3GPP UE is no
longer connected via the BBF access (e.g. if the lease of the local IP address
used by the 3GPP UE expires), if the BBF access network is aware of the UE's
detachment from the BBF access network. The BPCF may also use this procedure
if an admission control request causes all resources of a UE to be pre-empted
(if allowed by regulations).
Figure 5.2.2.1.2-4 GW Control Session termination
[PCRF-Initiated Gateway Control Session Termination]{.underline}
This procedure would be initiated by the PCRF (non-roaming) or V-PCRF
(roaming) for S9* to terminate a S9* session.
In case the S9* session is initiated from the PCRF and PCRF-initiated S9*
session establishment is triggered by Gxb* session, the Gxb* session
termination from ePDG may serve as a trigger for PCRF-initiated GW Control
session termination toward BPCF.
Figure 5.2.2.1.2-5 PCRF Initiated GW Control Session Termination
[BPCF-Initiated Gateway Control and QoS Rules Request]{.underline}
In a fixed access, there will probably be limited use of this procedure. For
example, the fixed accesses typically do not support UE-initiated resource
requests and would also not be able to detect most of the events that are
defined as event triggers in PCC. This procedure could however be applicable
in case the BPCF has pre-empted some resources and wants to report a QoS rule
failure to the PCRF.
Figure 5.2.2.1.2-6 Gateway Control and QoS Rules Request
##### 5.2.2.1.3 Assumptions about functionality in the BBF access network
In the above analysis, the following assumptions were made about functionality
in the BBF Access Network:
  * The BPCF is able to map the QoS information (QCI, bit rates, ARP) received over S9* to access-specific parameters applicable in the BBF access network
  * The BBF access network (e.g. BPCF) can perform admission control based on the QoS rules received over S9*
  * The BBF access network is able to support 3GPP-based access authentication and forward EAP messages between the UE and EPC..
  * Triggered by the access authentication and/or local IP address assignment, the BPCF initiates establishment of the S9* session with the PCRF. This assumes that the BBF Access becomes aware of the 3GPP UE attaching.
  * BPCF support for PCRF- initiated establishment of S9* session.
Editor's note: Also scenarios where 3GPP-based access authentication is not
supported needs to be studied. The BPCF-initiated S9* session for such
scenarios will be considered.
#### 5.2.2.2 Procedures for the case when WLAN is being used and traffic is
routed back to the EPC with S2b and BPCF-initiated S9* session establishment
##### 5.2.2.2.1 Initial Attach with PMIPv6 on S2b
Editor's note: this procedure is based on TS 23.402, clause 7.2.1
This clause is related to the case when the UE powers-on in an untrusted BBF
access network via S2b interface.
In the non-roaming case, PMIPv6 specification, RFC 5213, is used to setup a
PMIPv6 tunnel between the ePDG and the PDN GW. It is assumed that MAG is
collocated with ePDG. The IPsec tunnel between the UE and the ePDG provides a
virtual point-to-point link between the UE and the MAG functionality on the
ePDG.
Figure 5.2.2.2.1-1. The existing figure from 23.402, v9.4.0
Figure 5.2.2.2.2-2: Initial attachment when Network-based MM mechanism are
used over S2b for roaming, non-roaming and LBO
NOTE 1: Before the UE initiates the setup of an IPsec tunnel with the ePDG it
configures an IP address from an untrusted non-3GPP IP access network. This
address is used for sending all IKEv2 messages and as the source address on
the outer header of the IPsec tunnel.
The home routed roaming, LBO and non-roaming scenarios are depicted in the
figure.
\- In the LBO case, the 3GPP AAA Proxy acts as an intermediary, forwarding
messages from the 3GPP AAA Server in the HPLMN to the PDN GW in the VPLMN and
visa versa. Messages between the PDN GW in the VPLMN and the hPCRF in the
HPLMN are forwarded by the vPCRF in the VPLMN.
\- In the non-roaming case, the vPCRF and the 3GPP AAA Proxy are not involved.
If dynamic policy provisioning over S9* is not deployed, the optional steps 4
and 13 do not occur. Instead, the BBF Access Network may employ static
configured policies.
  1. The UE may perform the 3GPP based (EAP) access authentication procedure involving the BBF access network. As part of this step, the permanent user identity (IMSI) is provided from the 3GPP AAA Server to the BBF access network.
  2. The UE receives a local IP address from the BBF Access Network. How this is done is out of 3GPP scope, but it may involve IP address assignment by an RG or a BNG.
  3. Triggered by steps 1 and 2, the BPCF is informed about the UE accessing over BBF Access. How this is done is out of 3GPP scope.
  4. If the BPCF receives the trigger in step 3 and policy interworking with PCRF is supported, the BPCF initiates S9* session establishment. The BPCF includes the IMSI and IP-CAN type in the message to the PCRF. The details of how the BPCF is notified about the UE connecting in steps 1-3 is out of scope for 3GPP specifications.
Editor's note: Step 4 assumes that the BPCF is informed about the 3GPP UE
accessing the BBF access network. In other scenarios the BPCF may not become
aware of that a 3GPP UE is accessing. How the S9* session is set up for these
scenarios is FFS.
> 5-12. The description of these steps are the same as for steps 1-8 in TS
> 23.402, clause 7.2.1
  1. The Gateway Control and QoS Rules provision procedure may be initiated by the PCRF towards the BPCF.
  2. The BPCF may interact with the BNG, e.g. to download policies. This step is out of 3GPP scope.
##### 5.2.2.2.2 UE/ePDG-initiated Detach Procedure and UE-Requested PDN
Disconnection with PMIPv6
##### Non-Roaming, Home Routed Roaming and Local Breakout Case
Editor's note: this procedure is based on TS 23.402, clause 7.4.1.1
The procedure in this clause applies to Detach Procedures, initiated by UE or
ePDG initiated detach procedure, and to the UE-requested PDN disconnection
procedure.
The UE can initiate the Detach procedure, e.g. when the UE is power off. The
ePDG may initiate the Detach procedure due to administration reason or the
IKEv2 tunnel releasing.
For multiple PDN connectivity, this detach procedure shall be repeated for
each PDN connected.
Figure 5.2.2.2.2-1. The existing figure from 23.402, v9.4.0
Figure 5.2.2.2.2-2: UE/ePDG-initiated detach procedure with PMIPv6
The home routed roaming , LBO and non-roaming scenarios are depicted in the
figure. In the LBO case, the 3GPP AAA Proxy acts as an intermediary,
forwarding messages from the 3GPP AAA Server in the HPLMN to the PDN GW in the
VPLMN and visa versa. Messages between the PDN GW in the VPLMN and the hPCRF
in the HPLMN are forwarded by the vPCRF in the VPLMN. In the non-roaming case,
the vPCRF and the 3GPP AAA Proxy are not involved.
If dynamic policy provisioning over S9* is not deployed, the optional step 6
does not occur. Instead, the BBF access network may employ static configured
policies.
1-5) The description of these steps are the same as for steps 1-5 in 23.402,
clause 7.4.1.1
6) Triggered by the IP-CAN session termination in step 4, the PCRF executes a
Gateway Control and QoS Rules Provision procedure or, if this is the last PDN
Connection for the UE, a PCRF-Initiated Gateway Control Session Termination
Procedure with the BPCF.
7) The description of this step is the same as for step 6 in 23.402, clause
7.4.1.1
Editor's note: SWa interactions not shown in the flow above. It is FFS whether
such interactions should be added.
#####
##### 5.2.2.2.3 HSS/AAA-initiated Detach Procedure with PMIP
##### Non-Roaming, Home Routed Roaming and Local Breakout Case
Editor's note: this procedure is based on TS 23.402, clause 7.4.2.1
HSS/AAA-initiated detach procedure with PMIPv6 for non-roaming case is
illustrated in Figure 7.4.2-1. The HSS can initiate the procedure e.g. when
the user\'s subscription is removed. The 3GPP AAA Server can initiate the
procedure, e.g. instruction from O&M, timer for re-authentication/re-
authorization expired.
{width="6.445138888888889in" height="2.6041666666666665in"}
Figure 5.2.2.2.3-1. The existing figure from 23.402, v9.4.0
Figure 5.2.2.2.3-2: HSS/AAA-initiated detach procedure with PMIPv6
NOTE 1: AAA proxy and vPCRF are only used in the case of home routed roaming
and local breakout.
  1. The description of this step is the same as for step 1 in 23.402, clause 7.4.2.1
  2. This includes the procedure after step 1 in Figure 5.2.2.2.2-2. For multiple PDN connectivity, this step shall be repeated for each PDN Connected.
  3. The description of this step is the same as for step 3 in 23.402, clause 7.4.2.1
Editor's note: SWa interactions not shown in the flow above. It is FFS whether
such interactions should be added.
NOTE 2: The HSS/AAA may also send a detach indication message to the PDN GW.
The PDN GW does not remove the PMIP tunnels on S2b, since the ePDG is
responsible for removing the PMIP tunnels on S2b. The PDN GW acknowledges the
receipt of the detach indication message to the HSS/AAA.
###
##### 5.2.2.2.4 E-UTRAN to Untrusted Non-3GPP IP Access Handover with PMIPv6
on S2b
Editor's note: this procedure is based on TS 23.402, clause 8.2.3
This clause shows a call flow for a handover when a UE moves from an E-UTRAN
to an untrusted non-3GPP access network. PMIPv6 is assumed to be used on the
S5/S8 interface and PMIPv6 is used on the S2b interface.
Figure 5.2.2.2.4-1. The existing figure from 23.402, v9.4.0
Figure 5.2.2.2.4-2: E-UTRAN to Untrusted Non-3GPP IP Access Handover
Both the roaming and non-roaming scenarios are depicted in the figure. In the
roaming case, the vPCRF acts as an intermediary, sending the QoS Policy Rules
Provision from the hPCRF in the HPLMN to the Serving GW in the VPLMN. The
vPCRF receives the Acknowledgment from the Serving GW and forwards it to the
hPCRF. In the non-roaming case, the vPCRF is not involved.
For connectivity to multiple PDNs, step 15 is repeated for each PDN the UE is
connected to. Step 15 can occur in parallel for each PDN. Other impacts
related to the handover for multiple PDNs are described in clause 8.1.
The optional interaction steps between the gateways and the PCRF in the
procedures only occur if dynamic policy provisioning is deployed. Otherwise
policy may be statically configured in the gateway.
1-2) The description of these steps are the same as for steps 1-2 in 23.402,
clause 8.2.3
3) The UE may perform the 3GPP-based (EAP) access authentication procedure
involving the BBF access network. As part of this step, the permanent user
identity (IMSI) is provided from the 3GPP AAA Server to the BBF access
network.
4) The UE receives a local IP address from the BBF Access Network. How this is
done is out of 3GPP scope, but it may involve IP address assignment by an RG
or a BNG.
5) Triggered by steps 3 and 4, the BPCF is informed about the UE accessing
over BBF Access. How this is done is out of 3GPP scope.
6) If the BPCF receives the trigger in step 3 and policy interworking with
fixed accesses is supported, the BPCF initiates S9* session establishment. The
BPCF includes the IMSI and IP-CAN type in the message to the PCRF. The details
of how the BPCF is notified about the UE connecting in steps 3-5 is out of
scope for 3GPP specifications.
Editor's note: Step 4 assumes that the BPCF is informed about the 3GPP UE
accessing the BBF access network. In other scenarios the BPCF may not become
aware of that a 3GPP UE is accessing. How the S9* session is set up for these
scenarios is FFS.
7-11) The description of these steps are the same as for steps 3-7 in 23.402,
clause 8.2.3
12) The Gateway Control and QoS Rules provision procedure may be initiated by
the PCRF towards the BPCF. Depending on the reply from the BPCF, the PCRF may
update the PCC rules in the PCEF.
13) The BPCF may interact with the BNG, e.g. to download policies. This step
is out of 3GPP scope.
14-16) The description of these steps are the same as for steps 8-10 in
23.402, clause 8.2.3
##### 5.2.2.2.5 UE-initiated Connectivity to Additional PDN with PMIPv6 on S2b
Editor's note: this procedure is based on TS 23.402, clause 7.6.1
NOTE: The PDN GW treats each MN-ID+APN as a separate binding and may allocate
a new IP address/prefix for each binding.
This clause is related to the case when the UE has an established PDN
connection and wishes to establish one or more additional PDN connections.
Since PMIPv6 is used to establish connectivity with the additional PDN, the UE
establishes a separate SWu instance (i.e. a separate IPSec tunnel) for each
additional PDN.
There can be more than one PDN connection per APN if both the ePDG and the PDN
GW support that feature. When multiple PDN connections to a given APN are
supported, during the establishment of a new PDN connection, the ePDG creates
and sends a PDN Connection identity to the PDN GW. The PDN connection identity
is unique in the scope of the UE and the APN within an ePDG, i.e. the MN-ID,
the APN, and the PDN connection identity together identify a PDN connection
within an ePDG. In order to be able to identify a specific established PDN
connection, both the ePDG and the PDN GW shall store the PDN Connection
identity. Sending the PDN connection identity is an indication that the ePDG
supports multiple PDN connections to a single APN and the PDN GW shall be able
to indicate if it supports multiple PDN connections to a single APN. Between
the UE and the ePDG the IPSec SA associated with the PDN connection identifies
the PDN connection.
Figure 5.2.2.2.5-1: UE-initiated connectivity to additional PDN from Un-
trusted Non-3GPP IP Access with PMIPv6
1) The UE has performed the Initial S2b Attach procedure as defined in clause
5.x.2.y.z and has an established PDN connection.
2) The UE repeats the procedure of clause 5.2.2.2.2, Figure 5.2.2.2.2-2 for
each additional PDN the UE wants to connect to, with the following exceptions:
a) Steps 1-4 are only performed in the initial attach procedure and not when
connecting to an additional PDN.
b) The IKEv2 tunnel establishment procedure for each additional PDN connection
is initiated with the ePDG that was selected in step 1;
c) The APN information corresponding to the requested PDN connection is
conveyed with IKEv2 as specified in TS 33.402;
d) For network supporting multiple mobility protocols, if there was any
dynamic IPMS decision in step 5, the AAA/HSS enforces the same IPMS decision
for each additional PDN connection.
#### 5.2.2.3 Procedures for trusted BBF WLAN with traffic routed to the EPC
with S2c and BPCF-initiated S9* session establishment
##### 5.2.2.3.1 Initial Attach with DSMIPv6 on S2c to trusted BBF access
Editor's note: this procedure is based on TS 23.402, clause 6.3
This clause is related to the case when the UE attaches to a BBF access which
is considered trusted. In this case only S2c procedures can be used in
building block 1.
Figure 5.2.2.3.1-1. The existing figure from 23.402, v9.4.0
Figure 5.2.2.2.3-2: Initial attachment when S2c is used for roaming, non-
roaming and LBO
The home routed roaming, LBO and non-roaming scenarios are depicted in the
figure.
\- In the LBO case, the 3GPP AAA Proxy acts as an intermediary, forwarding
messages from the 3GPP AAA Server in the HPLMN to the PDN GW in the VPLMN and
visa versa. Messages between the PDN GW in the VPLMN and the hPCRF in the
HPLMN are forwarded by the vPCRF in the VPLMN.
\- In the non-roaming case, the vPCRF and the 3GPP AAA Proxy are not involved.
If dynamic policy provisioning over S9* is not deployed, the optional steps 4
and 13 do not occur. Instead, the BBF Access Network may employ static
configured policies.
  1. The UE may perform the 3GPP based (EAP) access authentication procedure involving the BBF access network. As part of this step, the permanent user identity (IMSI) is provided from the 3GPP AAA Server to the BBF access network
The UE receives a local IP address from the BBF Access Network which is used
as CoA in S2c signaling. How this is done is out of 3GPP scope, but it may
involve IP address assignment by an RG or a BNG
  2. Triggered by steps 1 and 2, the BPCF is informed about the UE accessing over BBF Access. How this is done is out of 3GPP scope.
  3. If the BPCF receives the trigger in step 3 and policy interworking with PCRF is supported, the BPCF initiates S9* session establishment. The BPCF includes the UE identity, and IP-CAN type in the message to the PCRF. The details of how the BPCF is notified about the UE connecting in steps 1-3 is out of scope for 3GPP specifications.
Editor's note: Step 4 assumes that the BPCF is informed about the 3GPP UE
accessing the BBF access network. In other scenarios the BPCF may not become
aware of that a 3GPP UE is accessing. How the S9* session is set up for these
scenarios is FFS.
> 5-10. The description of these steps are the same as for steps 1-8 in TS
> 23.402, clause 6.3
>
> 11\. The Gateway Control and QoS Rules provision procedure may be initiated
> by the PCRF towards the BPCF.
>
> 12\. The BPCF may interact with the BNG, e.g. to download policies. This
> step is out of 3GPP scope.
##### 5.2.2.3.2 UE-initiated Detach Procedure and UE-Requested PDN
Disconnection with S2c in trusted BBF access
Editor's note: this procedure is based on TS 23.402, clause 6.5.2
The procedure in this clause applies to Detach Procedures, initiated by UE,
and to the UE-requested PDN disconnection procedure.The UE can initiate the
Detach procedure, e.g. when the UE is power off. For multiple PDN
connectivity, this detach procedure shall be repeated for each PDN connected.
Figure 5.2.2.3.2-1. The existing figure from 23.402, v9.4.0
Figure5.2.2.3.2-2: UE-initiated detach procedure with DSMIPv6
The home routed roaming, LBO and non-roaming scenarios are depicted in the
figure. In the LBO case, the 3GPP AAA Proxy acts as an intermediary,
forwarding messages from the 3GPP AAA Server in the HPLMN to the PDN GW in the
VPLMN and visa versa. Messages between the PDN GW in the VPLMN and the hPCRF
in the HPLMN are forwarded by the vPCRF in the VPLMN. In the non-roaming case,
the vPCRF and the 3GPP AAA Proxy are not involved.
If dynamic policy provisioning over S9* is not deployed, the optional step 6
does not occur. Instead, the BBF access network may employ static configured
policies.
1-4) The description of these steps are the same as for steps 1-5 in 23.402,
clause 6.5.2
5) Triggered by the IP-CAN session termination in step 3, the PCRF executes a
Gateway Control and QoS Rules Provision procedure or, if this is the last PDN
Connection for the UE, a PCRF-Initiated Gateway Control Session Termination
Procedure with the BPCF.
6) The description of this step is the same as for step 6 in 23.402, clause
6.5.2
7) The description of this step is the same as for step 7 in 23.402, clause
6.5.2
##### 5.2.2.3.3 HSS-initiated Detach Procedure with S2c in trusted BBF access
Editor's note: this procedure is based on TS 23.402, clause 6.5.3
The procedure in this clause applies to Detach Procedures, initiated by HSS.
Figure 5.2.2.3.3-1. The existing figure from 23.402, v9.4.0
Figure5.2.2.3.3-2: HSS-initiated detach procedure with DSMIPv6
1-7) The description of these steps are the same as for steps 1-7 in 23.402,
clause 6.5.3
##### 5.2.2.3.4 PDN GW-initiated PDN disconnection Procedure with S2c in
trusted BBF access
Editor's note: this procedure is based on TS 23.402, clause 6.5.4
The procedure in this clause applies to PDN disconnection procedure initiated
by PDN GW.
Figure 5.2.2.3.4-1. The existing figure from 23.402, v9.4.0
Figure 5.2.2.3.4-2: PDN GW-initiated PDN disconnection procedure with DSMIPv6
1-7) The description of these steps are the same as for steps 1-7 in 23.402,
clause 6.5.4
##### 5.2.2.3.5 E-UTRAN to Trusted BBF access Handover with DSMIPv6 on S2c
Editor's note: this procedure is based on TS 23.402, clause 8.4.2
This clause shows a call flow for a handover when a UE moves from an E-UTRAN
to an trusted BBF access network.
Figure 5.2.2.3.5-1. The existing figure from 23.402, v9.4.0
Figure 5.2.2.3.5-2: E-UTRAN to Trusted BBFAccess Handover
Both the roaming and non-roaming scenarios are depicted in the figure.
For connectivity to multiple PDNs, steps 7-10 are repeated for each PDN the UE
is connected to.
The optional interaction steps between the gateways and the PCRF in the
procedures only occur if dynamic policy provisioning is deployed. Otherwise
policy may be statically configured in the gateway.
1-2) The description of these steps are the same as for steps 1-2 in 23.402,
clause 8.4.2
3) The UE may perform the 3GPP-based (EAP) access authentication procedure
involving the BBF access network. As part of this step, the permanent user
identity (IMSI) is provided from the 3GPP AAA Server to the BBF access
network.
4 The UE receives a local IP address from the BBF Access Network. How this is
done is out of 3GPP scope, but it may involve IP address assignment by an RG
or a BNG.
5) Triggered by steps 3 and 4, the BPCF is informed about the UE accessing
over BBF Access. How this is done is out of 3GPP scope.
6) If the BPCF receives the trigger in step 3 and policy interworking with
fixed accesses is supported, the BPCF initiates S9* session establishment. The
BPCF includes the UE Identity and IP-CAN type in the message to the PCRF. The
details of how the BPCF is notified about the UE connecting in steps 3-5 is
out of scope for 3GPP specifications.
Editor's note: Step 6 assumes that the BPCF is informed about the 3GPP UE
accessing the BBF access network. In other scenarios the BPCF may not become
aware of that a 3GPP UE is accessing. How the S9* session is set up for these
scenarios is FFS.
7-11) The description of these steps are the same as for steps 6-11 in 23.402,
clause 8.3.2, excluding step 10
12) The Gateway Control and QoS Rules provision procedure may be initiated by
the PCRF towards the BPCF. Depending on the reply from the BPCF, the PCRF may
update the PCC rules in the PCEF
13) The BPCF may interact with the BNG, e.g. to download policies. This step
is out of 3GPP scope.
14) The description of these steps are the same as for step 12 in 23.402,
clause 8.3.2
####
##### 5.2.2.3.6 Network-initiated Dynamic PCC for S2c when accessing trusted
BBF access
This procedure is applicable if the UE accesses over a BBF Access network
which is considered trusted.
If dynamic PCC is deployed, the procedure given in Figure 6.6.x-1 is used by
the PCRF to provision rules to the BBF IP access and for the BBF IP access to
enforce the policy by controlling the resources and configuration in the
access. The access specific procedure executed in the BBF access is not within
the scope of this specification.
Figure 5.5.2.3.6-1: Network-initiated dynamic policy control procedure in
Trusted BBF IP Access for S2c
This procedure concerns both the non-roaming (as Figure 4.2.2-1) and roaming
case (as Figure 4.2.3-1). In the roaming case, the vPCRF in the VPLMN forwards
messages between the BPCF and the hPCRF in the HPLMN. In the case of Local
Breakout (as Figure 4.2.3-4), the vPCRF forwards messages sent between the PDN
GW and the hPCRF. In the non-roaming case, the vPCRF is not involved at all.
The optional interaction steps between the gateways and the PCRF in the
procedures only occur if dynamic policy provisioning is deployed. Otherwise
policy may be statically configured with the gateway.
1\. The PCRF initiates the Gateway Control and QoS Policy Rules Provision
Procedure specified in TS 23.203 [19] by sending a message with the QoS rules
to the BPCF.
2\. The BBF Access Network performs admission control based on the rules
provisioned to it, and establishes all necessary resources and configuration
in the BBF access network. The details of this step are out of the scope of
this specification.
3\. The BPCF responds to the PCRF indicating the result of the request
received in Step 1 and thus completing the GW Control and QoS Rules Provision
procedure started in step 1.
4\. The PCRF initiates the PCC Rules Provision Procedure as specified in TS
23.203 [19]. The PCRF provides updated PCC rules to the PCEF for enforcement
by means of a PCC Rules Provision procedure specified in TS 23.203 [19].
NOTE: Step 4 may occur before step 1 or performed in parallel with steps 1‑3
if acknowledgement of resource allocation is not required to update PCC rules
in PCEF. For details please refer to TS 23.203 [19].
##### 5.2.2.3.7 UE-initiated Connectivity to Additional PDN with S2c over
trusted BBF access
Editor's note: this procedure is based on TS 23.402, clause 6.8.3
This clause is related to the case when the UE has an established PDN
connection and wishes to establish one or more additional PDN connections.
There can be more than one PDN connection per APN if the PDN GW supports that
feature.
Figure 5.2.2.3.7-1: UE-initiated connectivity to additional PDN from Trusted
Non-3GPP IP Access with S2c
1) The UE has performed the Initial S2c attach procedure as defined in clause
5.2.2.3.1 and has an established PDN connection.
2) The UE repeats the procedure of clause 5.2.2.3.1, Figure 5.2.2.3.1-2 for
each additional PDN the UE wants to connect to, with the following exceptions:
a) Steps 1-4 are only performed in the initial attach procedure and not when
connecting to an additional PDN.
b) For network supporting multiple mobility protocols, if there was any
dynamic IPMS decision in step 5, the AAA/HSS enforces the same IPMS decision
for each additional PDN connection.
###
#### 5.2.2.4 Procedures for untrusted BBF WLAN with traffic routed to the EPC
with S2c and BPCF-initiated S9* session establishment
##### 5.2.2.4.1 Initial Attach with DSMIPv6 on S2c to untrusted BBF access
Editor's note: this procedure is based on TS 23.402, clause 7.3
This clause is related to the case when the UE attaches to a BBF access which
is considered untrusted. In this case only S2c procedures can be used.
Figure 5.2.2.4.1-1. The existing figure from 23.402, v9.4.0
Figure 5.2.2.4.1-2: Initial attachment when S2c is used for roaming, non-
roaming and LBO
The home routed roaming, LBO and non-roaming scenarios are depicted in the
figure.
\- In the LBO case, the 3GPP AAA Proxy acts as an intermediary, forwarding
messages from the 3GPP AAA Server in the HPLMN to the PDN GW in the VPLMN and
visa versa. Messages between the PDN GW in the VPLMN and the hPCRF in the
HPLMN are forwarded by the vPCRF in the VPLMN.
\- In the non-roaming case, the vPCRF and the 3GPP AAA Proxy are not involved.
If dynamic policy provisioning over S9* is not deployed, the optional steps 4
and 13 do not occur. Instead, the BBF Access Network may employ static
configured policies.
  1. The UE may perform the 3GPP based (EAP) access authentication procedure involving the BBF access network. As part of this step, the permanent user identity (IMSI) is provided from the 3GPP AAA Server to the BBF access network.
  2. The UE receives a local IP address from the BBF Access Network. How this is done is out of 3GPP scope, but it may involve IP address assignment by an RG or a BNG.
  3. Triggered by steps 1 and 2, the BPCF is informed about the UE accessing over BBF Access. How this is done is out of 3GPP scope.
  4. If the BPCF receives the trigger in step 3 and policy interworking with PCRF is supported, the BPCF initiates S9* session establishment. The BPCF includes the UE identity, and IP-CAN type in the message to the PCRF. The details of how the BPCF is notified about the UE connecting in steps 1-3 is out of scope for 3GPP specifications.
Editor's note: Step 4 assumes that the BPCF is informed about the 3GPP UE
accessing the BBF access network. In other scenarios the BPCF may not become
aware of that a 3GPP UE is accessing. How the S9* session is set up for these
scenarios is FFS.
> 5-13. The description of these steps are the same as for steps 1-8 in TS
> 23.402, clause 7.3
>
> 14\. The Gateway Control and QoS Rules provision procedure may be initiated
> by the PCRF towards the BPCF.
>
> 15\. The BPCF may interact with the BNG, e.g. to download policies. This
> step is out of 3GPP scope.
##### 5.2.2.4.2 UE-initiated Detach Procedure and UE-Requested PDN
Disconnection with S2c in untrusted BBF access
Editor's note: this procedure is based on TS 23.402, clause 7.5.2
The procedure in this clause applies to Detach Procedures, initiated by UE,
and to the UE-requested PDN disconnection procedure.The UE can initiate the
Detach procedure, e.g. when the UE is power off. For multiple PDN
connectivity, this detach procedure shall be repeated for each PDN connected.
Figure 5.2.2.4.2-1. The existing figure from 23.402, v9.4.0
Figure 5.2.2.4.2-2: UE-initiated detach procedure with DSMIPv6
The home routed roaming, LBO and non-roaming scenarios are depicted in the
figure. In the LBO case, the 3GPP AAA Proxy acts as an intermediary,
forwarding messages from the 3GPP AAA Server in the HPLMN to the PDN GW in the
VPLMN and visa versa. Messages between the PDN GW in the VPLMN and the hPCRF
in the HPLMN are forwarded by the vPCRF in the VPLMN. In the non-roaming case,
the vPCRF and the 3GPP AAA Proxy are not involved.
If dynamic policy provisioning over S9* is not deployed, the optional step 6
does not occur. Instead, the BBF access network may employ static configured
policies.
1-4) The description of these steps are the same as for steps 1-5 in 23.402,
clause 7.5.2
5) Triggered by the IP-CAN session termination in step 3, the PCRF executes a
Gateway Control and QoS Rules Provision procedure or, if this is the last PDN
Connection for the UE, a PCRF-Initiated Gateway Control Session Termination
Procedure with the BPCF.
6-8) The description of this step is the same as for step 6 in 23.402, clause
7.5.2
##### 5.2.2.4.3 HSS-initiated Detach Procedure with S2c in untrusted BBF
access
Editor's note: this procedure is based on TS 23.402, clause 7.5.3
The procedure in this clause applies to Detach Procedures, initiated by HSS.
Figure 5.2.2.4.3-1. The existing figure from 23.402, v9.4.0
Figure 5.2.2.4.3-2: HSS-initiated detach procedure with DSMIPv6
1-8) The description of these steps are the same as for steps 1-7 in 23.402,
clause 7.5.3
##### 5.2.2.4.4 PDN GW-initiated PDN disconnection Procedure with S2c in
untrusted BBF access
Editor's note: this procedure is based on TS 23.402, clause 7.5.4
The procedure in this clause applies to PDN disconnection procedure initiated
by PDN GW.
Figure 5.2.2.4.4-1. The existing figure from 23.402, v9.4.0
Figure 5.2.2.4.4-2: PDN GW-initiated PDN disconnection procedure with DSMIPv6
1-8) The description of these steps are the same as for steps 1-7 in 23.402,
clause 7.5.4
##### 5.2.2.4.5 E-UTRAN to untrusted BBF access Handover with DSMIPv6 on S2c
Editor's note: this procedure is based on TS 23.402, clause 8.4.3
This clause shows a call flow for a handover when a UE moves from an E-UTRAN
to an untrusted BBF access network.
Figure 5.2.2.4.5-1. The existing figure from 23.402, v9.4.0
Figure 5.2.2.4.5-2: E-UTRAN to untrusted BBFAccess Handover
Both the roaming and non-roaming scenarios are depicted in the figure.
For connectivity to multiple PDNs, steps 7-10 are repeated for each PDN the UE
is connected to.
The optional interaction steps between the gateways and the PCRF in the
procedures only occur if dynamic policy provisioning is deployed. Otherwise
policy may be statically configured in the gateway.
1-2) The description of these steps are the same as for steps 1-2 in 23.402,
clause 8.4.3
3) The UE may perform the 3GPP-based (EAP) access authentication procedure
involving the BBF access network. As part of this step, the permanent user
identity (IMSI) is provided from the 3GPP AAA Server to the BBF access network
4) The UE receives a local IP address from the BBF Access Network. How this is
done is out of 3GPP scope, but it may involve IP address assignment by an RG
or a BNG.
5) Triggered by steps 3 and 4, the BPCF is informed about the UE accessing
over BBF Access. How this is done is out of 3GPP scope.
6) If the BPCF receives the trigger in step 3 and policy interworking with
fixed accesses is supported, the BPCF initiates S9* session establishment. The
BPCF includes the UE Identity and IP-CAN type in the message to the PCRF. The
details of how the BPCF is notified about the UE connecting in steps 3-5 is
out of scope for 3GPP specifications.
Editor's note: Step 4 assumes that the BPCF is informed about the 3GPP UE
accessing the BBF access network. In other scenarios the BPCF may not become
aware of that a 3GPP UE is accessing. How the S9* session is set up for these
scenarios is FFS.
7-14) The description of these steps are the same as for steps 3-9 in 23.402,
clause 8.4.3.
12) The Gateway Control and QoS Rules provision procedure may be initiated by
the PCRF towards the BPCF. Depending on the reply from the BPCF, the PCRF may
update the PCC rules in the PCEF
13) The BPCF may interact with the BNG, e.g. to download policies. This step
is out of 3GPP scope.
14) The description of these steps are the same as for step 10 in 23.402,
clause 8.4.3
##### 5.2.2.4.6 Network-initiated Dynamic PCC for S2c when accessing untrusted
BBF access
This procedure is applicable if the UE accesses over a BBF Access network
which is considered untrusted.
If dynamic PCC is deployed, the procedure given in Figure 6.6.x-1 is used by
the PCRF to provision rules to the BBF IP access and for the BBF IP access to
enforce the policy by controlling the resources and configuration in the
access. The access specific procedure executed in the BBF access is not within
the scope of this specification.
Figure 5.5.2.4.6-1: Network-initiated dynamic policy control procedure in un-
trusted BBF IP Access for S2c
This procedure concerns both the non-roaming (as Figure 4.2.2-1) and roaming
case (as Figure 4.2.3-1). In the roaming case, the vPCRF in the VPLMN forwards
messages between the BPCF and the hPCRF in the HPLMN. In the case of Local
Breakout (as Figure 4.2.3-4), the vPCRF forwards messages sent between the PDN
GW and the hPCRF. In the non-roaming case, the vPCRF is not involved at all.
The optional interaction steps between the gateways and the PCRF in the
procedures only occur if dynamic policy provisioning is deployed. Otherwise
policy may be statically configured with the gateway.
1\. The PCRF initiates the Gateway Control and QoS Policy Rules Provision
Procedure specified in TS 23.203 [19] by sending a message with the QoS rules
to the BPCF.
2\. The BBF Access Network performs admission control based on the rules
provisioned to it, and establishes all necessary resources and configuration
in the BBF access network. The details of this step are out of the scope of
this specification.
3\. The BPCF responds to the PCRF indicating the result of the request
received in Step 1 and thus completing the GW Control and QoS Rules Provision
procedure started in step 1.
4\. The PCRF initiates the PCC Rules Provision Procedure as specified in TS
23.203 [19]. The PCRF provides updated PCC rules to the PCEF for enforcement
by means of a PCC Rules Provision procedure specified in TS 23.203 [19].
NOTE: Step 4 may occur before step 1 or performed in parallel with steps 1‑3
if acknowledgement of resource allocation is not required to update PCC rules
in PCEF. For details please refer to TS 23.203 [19].
##### 5.2.2.4.7 UE-initiated Connectivity to Additional PDN with S2c over
untrusted BBF access
Editor's note: this procedure is based on TS 23.402, clause 7.6.2
This clause is related to the case when the UE has an established PDN
connection and wishes to establish one or more additional PDN connections.
Since DSMIPv6 is used to establish connectivity with the additional PDN, the
UE does not need to establish a separate SWu instance (i.e. a separate IPsec
tunnel) for each additional PDN.
There can be more than one PDN connection per APN if the PDN GW supports that
feature.
Figure 5.2.2.5.7-1: UE-initiated connectivity to additional PDN from un-
trusted Non-3GPP IP Access with DSMIPv6
1) The UE has performed the Initial S2c attach procedure as defined in clause
5.2.2.4.1 and has an established PDN connection.
2) The UE repeats the procedure of clause 5.2.2.4.1, Figure 5.2.2.4.1-2 for
each additional PDN the UE wants to connect to, with the following exceptions:
a) Steps 1-7 are only performed in the initial attach procedure and not when
connecting to an additional PDN.
d) For network supporting multiple mobility protocols, if there was any
dynamic IPMS decision in step 5, the AAA/HSS enforces the same IPMS decision
for each additional PDN connection.
#### 5.2.2.5 Procedures for untrusted WLAN with traffic routed back to the EPC
with S2b and PCRF-initiated S9* session establishment
##### 5.2.2.5.1 Initial Attach with PMIPv6 on S2b
This clause is related to the case when the UE powers-on in an untrusted BBF
access network via S2b interface. Gxb* session is being established between
ePDG and PCRF when UE initial attach to the EPC via BBF access.
In the non-roaming case, PMIPv6 specification, RFC 5213, is used to setup a
PMIPv6 tunnel between the ePDG and the PDN GW. It is assumed that MAG is
collocated with ePDG. The IPsec tunnel between the UE and the ePDG provides a
virtual point-to-point link between the UE and the MAG functionality on the
ePDG.
The home routed roaming, LBO and non-roaming scenarios are depicted in the
following figures.
\- In the LBO case, the 3GPP AAA Proxy acts as an intermediary, forwarding
messages from the 3GPP AAA Server in the HPLMN to the PDN GW in the VPLMN and
visa versa. Messages between the PDN GW in the VPLMN and the hPCRF in the
HPLMN are forwarded by the vPCRF in the VPLMN.
\- In the non-roaming case, the vPCRF and the 3GPP AAA Proxy are not involved.
S9* session is between hPCRF and the BPCF.
\- In home routed roaming and LBO case, the S9* session is between vPCRF and
the BPCF, the hPCRF is not aware of the S9* session.
If dynamic policy provisioning over S9* is not deployed, the optional steps
4-5 and steps 12-13 in Figure 5.2.2.5.1-1 do not occur. Instead, the BBF
Access Network may employ static configured policies.
Figure 5.2.2.5.1-1: Initial attachment when Network-based MM mechanism are
used over S2b for roaming, non-roaming and LBO
  1. If the BBF access network supports 3GPP-based (EAP) authentication, it may be involved in the EAP access authentication procedure performed between the UE and the EPC.
  2. The UE receives a local IP address from the BBF Access Network. How this is done is out of 3GPP scope, but it may involve IP address assignment by an RG or a BNG.
  3. The IKEv2 tunnel establishment procedure is started by the UE. Authentication procedure is performed among UE, ePDG and 3GPP AAA. For detail information, please refer to step 2 in TS23.402, clause 7.2.1.
  4. The ePDG initiates Gxb* session establishment with the PCRF by using Gateway Control Session establishment procedure. The ePDG includes the IMSI, APN, IP-CAN type, UE IP address allocated by EPC and the outer IP header information of the tunnelled traffic in the message to the PCRF.
> Editor's note: It is FFS whether other information is needed to be sent by
> ePDG to the PCRF in this step.
>
> For roaming case (both home routed and LBO), the ePDG initiates Gateway
> Control Session establishment procedure with the v-PCRF. The ePDG contains
> IMSI, APN, IP-CAN type , UE IP address allocated by EPC and outer IP header
> information of the tunnelled traffic in the request message. When the v-PCRF
> receives a Gateway Control Session establishment request, the v-PCRF shall
> initiate S9 session establishment/modification procedure. The v-PCRF sends a
> S9 session establishment request to the h-PCRF with the information received
> over Gxb* interface excluding tunnelled traffic related info (e.g. outer IP
> header info of the tunnelled traffic).
  1. Triggered by the Gxb* session establishment, the PCRF (non-roaming case) or the v-PCRF (roaming case) initiates Gateway Control Session establishment with the BPCF to establish S9* Session. The IMSI, IP-CAN type, and outer IP header information for tunnel traffic needs to be included in the request message which sending to the BPCF.
    1. The description of these steps are the same as for steps 3-9 in TS 23.402, clause 7.2.1
> 12\. In order for the BPCF to perform admission control in the fixed
> network, the PCRF use Gateway Control and QoS Rules provision procedure to
> provide QoS information to the BPCF.
##### 5.2.2.5.2 UE/ePDG-initiated Detach Procedure and UE-Requested PDN
Disconnection with PMIPv6
##### Non-Roaming, Home Routed Roaming and Local Breakout Case
The procedure in this clause applies to Detach Procedures, initiated by UE or
ePDG initiated detach procedure, and to the UE-requested PDN disconnection
procedure.
The UE can initiate the Detach procedure, e.g. when the UE is power off. The
ePDG may initiate the Detach procedure due to administration reason or the
IKEv2 tunnel releasing.
For multiple PDN connectivity, this detach procedure shall be repeated for
each PDN connected.
The home routed roaming, LBO and non-roaming scenarios are depicted in the
following figures. In the LBO case, the 3GPP AAA Proxy acts as an
intermediary, forwarding messages from the 3GPP AAA Server in the HPLMN to the
PDN GW in the VPLMN and visa versa. Messages between the PDN GW in the VPLMN
and the hPCRF in the HPLMN are forwarded by the vPCRF in the VPLMN. In the
non-roaming case, the vPCRF and the 3GPP AAA Proxy are not involved.
If dynamic policy provisioning over S9* is not deployed, the optional step 3
in 5.2.2.5.2-1 does not occur. Instead, the BBF access network may employ
static configured policies.
Figure 5.2.2.5.2-1: UE/ePDG-initiated detach procedure with PMIPv6
1) IKEv2 tunnel release triggers PMIP tunnel release.
2) Triggered by the IKEv2 tunnel release, the ePDG executes Gateway Control
Session termination procedure with the PCRF.
> For roaming case, the ePDG executes Gateway Control Session termination
> procedure with the v-PCRF. Accordingly, the v-PCRF initiates S9 session
> termination/modification with the h-PCRF.
3) After receiving Gateway Control Session Termination from the ePDG, the
PCRF(non-roaming case) or the vPCRF (roaming case) executes a Gateway Control
and QoS Rules Provision procedure with the BPCF or, if this is the last PDN
Connection for the UE, a PCRF-Initiated Gateway Control Session Termination
Procedure with the BPCF would be performed.
4-8) The description of this step is the same as for step 2-6 in 23.402,
clause 7.4.1.1
##### 5.2.2.5.3 HSS/AAA-initiated Detach Procedure with PMIP
##### Non-Roaming, Home Routed Roaming and Local Breakout Case
HSS/AAA-initiated detach procedure with PMIPv6 for non-roaming case is
illustrated in Figure 5.2.2.5.3-1. The HSS can initiate the procedure e.g.
when the user\'s subscription is removed. The 3GPP AAA Server can initiate the
procedure, e.g. instruction from O&M, timer for re-authentication/re-
authorization expired.
Figure 5.2.2.5.3-1: HSS/AAA-initiated detach procedure with PMIPv6
NOTE 1: AAA proxy and vPCRF are only used in the case of home routed roaming
and local breakout.
  1. The description of this step is the same as for step 1 in 23.402, clause 7.4.2.1
  2. This includes the procedure after step 1 in Figure 5.2.2.5.2-1. For multiple PDN connectivity, this step shall be repeated for each PDN Connected.
  3. The description of this step is the same as for step 3 in 23.402, clause 7.4.2.1
Editor's note: The optional SWa interactions are not shown in the flow above.
It is FFS whether such interactions should be added.
NOTE 2: The HSS/AAA may also send a detach indication message to the PDN GW.
The PDN GW does not remove the PMIP tunnels on S2b, since the ePDG is
responsible for removing the PMIP tunnels on S2b. The PDN GW acknowledges the
receipt of the detach indication message to the HSS/AAA.
##### 5.2.2.5.4 E-UTRAN to Untrusted Non-3GPP IP Access Handover with PMIPv6
on S2b
This clause shows a call flow for a handover when a UE moves from an E-UTRAN
to an untrusted non-3GPP access network. PMIPv6 is assumed to be used on the
S5/S8 interface and PMIPv6 is used on the S2b interface.
Both the roaming and non-roaming scenarios are depicted in the figure. In the
roaming case, the vPCRF acts as an intermediary, sending the QoS Policy Rules
Provision from the hPCRF in the HPLMN to the Serving GW in the VPLMN. The
vPCRF receives the Acknowledgment from the Serving GW and forwards it to the
hPCRF. In the non-roaming case, the vPCRF is not involved.
For connectivity to multiple PDNs, step 16 is repeated for each PDN the UE is
connected to. Step 16 can occur in parallel for each PDN. Other impacts
related to the handover for multiple PDNs are described in clause 8.1.
The optional interaction steps between the gateways and the PCRF in the
procedures only occur if dynamic policy provisioning is deployed. Otherwise
policy may be statically configured in the gateway.
Figure 5.2.2.5.4-1: E-UTRAN to Untrusted Non-3GPP IP Access Handover
1-2) The description of these steps are the same as for steps 1-2 in 23.402,
clause 8.2.3
3) If the BBF access network supports 3GPP-based (EAP) authentication, it may
be involved in the EAP access authentication procedure performed between the
UE and the EPC.
4) The UE receives a local IP address from the BBF Access Network. How this is
done is out of 3GPP scope, but it may involve IP address assignment by an RG
or a BNG.
5) The IKEv2 tunnel establishment procedure is started by the UE. For detail
information, please refer to step 3 in TS23.402, clause 8.2.3
6) The ePDG initiates Gxb* session establishment by using Gateway Control
Session establishment procedure with the PCRF. The ePDG includes the IMSI,
APN, IP-CAN type, UE IP address allocated by EPC and the outer IP header
information of the tunnelled traffic in the message to the PCRF.
> Editor's note: It is FFS whether other information is needed to be sent by
> ePDG to the PCRF in this step.
>
> For roaming case, the ePDG initiates Gateway Control Session establishment
> procedure with the v-PCRF. The ePDG contains IMSI, APN, IP-CAN type, UE IP
> address allocated by EPC and outer IP header information of the tunnelled
> traffic in the request message. When the v-PCRF receives a Gateway Control
> Session establishment request, the v-PCRF shall initiate S9 session
> establishment/modification procedure. The v-PCRF sends a S9 session
> establishment request to the h-PCRF with the information received over Gxb*
> interface excluding tunnelled traffice related info (e.g. outer IP header
> info of the tunnelled traffic).
7) Triggered by the Gxb* session establishment, the PCRF (non-roaming case) or
the v-PCRF (roaming case) initiates Gateway Control Session establishment with
the BPCF to establish S9* Session. The IMSI, IP-CAN type, and outer IP header
information for tunnel traffic needs to be included in the request message
which sending to the BPCF.
8-11) The description of these steps are the same as for steps 4-7 in 23.402,
clause 8.2.3
12) In order for the BPCF to perform admission control in the fixed network,
the PCRF use Gateway Control and QoS Rules provision procedure to provide QoS
information to the BPCF.
13-15) The description of these steps are the same as for steps 8-10 in
23.402, clause 8.2.3
##### 5.2.2.5.5 UE-initiated Connectivity to Additional PDN with PMIPv6 on S2b
This clause is related to the case when the UE has an established PDN
connection and wishes to establish one or more additional PDN connections.
Since PMIPv6 is used to establish connectivity with the additional PDN, the UE
establishes a separate SWu instance (i.e. a separate IPSec tunnel) for each
additional PDN.
Figure 5.2.2.5.5-1: UE-initiated connectivity to additional PDN from Un-
trusted Non-3GPP IP Access with PMIPv6
  1. The UE has performed the Initial S2b Attach procedure as defined in clause 5.2.2.5.1 and has an established PDN connection.
  2. The UE repeats the procedure of steps 1, 2, 5 in clause 5.2.2.5.1, Figure 5.2.2.5.1-1 for each additional PDN the UE wants to connect to.
####
#### 5.2.2.6 Procedures for trusted BBF WLAN with traffic is routed back to
the EPC with S2c and PCRF-initiated S9* session establishment
##### 5.2.2.6.1 Initial Attach with DSMIPv6 on S2c to trusted BBF access
This clause is related to the case when the UE attaches to a BBF access which
is considered as trusted. In this case only S2c procedures can be used in
building block I. The PCRF triggered by the IP-CAN Session establishment will
initiate the S9* session establishment.
The home routed roaming, LBO and non-roaming scenarios are depicted in the
figure.
\- In the LBO case, the 3GPP AAA Proxy acts as an intermediary, forwarding
messages from the 3GPP AAA Server in the HPLMN to the PDN GW in the VPLMN and
visa versa. Messages between the PDN GW in the VPLMN and the hPCRF in the
HPLMN are forwarded by the vPCRF in the VPLMN.
\- In the non-roaming case, the vPCRF and the 3GPP AAA Proxy are not involved.
If dynamic policy provisioning over S9* is not deployed, the optional steps
9-10 in Figure 5.2.2.7.1-1 do not occur. Instead, the BBF Access Network may
employ static configured policies.
Figure 5.2.2.6.1-1: Initial attachment when S2c is used for roaming, non-
roaming and LBO
> 1 If the BBF access network supports 3GPP-based (EAP) authentication, it may
> be involved in the EAP access authentication procedure performed between the
> UE and the EPC.
2 The UE receives a local IP address from the BBF Access Network. How this is
done is out of 3GPP scope, but it may involve IP address assignment by an RG
or a BNG.
> 3-8 The description of these steps are the same as for steps 1-8 in TS
> 23.402, clause 6.3
>
> 9 Triggered by the IP-CAN Session establishment from the PDN GW, the PCRF
> initiate the S9* session establishment with the BPCF. The Care of Address,
> IP-CAN type, QoS information, and optionally the IMSI, needs to be included
> in the request message which sending to the BPCF.
10 The BPCF may interact with the BNG, e.g. to download policies. This step is
out of 3GPP scope.
##### 5.2.2.6.2 UE-initiated Detach Procedure and UE-Requested PDN
Disconnection with S2c in trusted BBF access
The procedure for UE-initiated Detach Procedure and UE-Requested PDN
Disconnection with S2c in trusted BBF access and PCRF-initiated S9* session
establishment is same as the procedure defined in section 5.2.2.3.2.
##### 5.2.2.6.3 HSS-initiated Detach Procedure with S2c in trusted BBF access
The procedure for HSS-initiated Detach Procedure with S2c in trusted BBF
access and PCRF-initiated S9* session establishment is same as the procedure
defined in section 5.2.2.3.3.
##### 5.2.2.6.4 PDN GW-initiated PDN disconnection Procedure with S2c in
trusted BBF access
The procedure for PDN GW-initiated PDN disconnection Procedure with S2c in
trusted BBF access and PCRF-initiated S9* session establishment is same as the
procedure defined in section 5.2.2.3.3.
##### 5.2.2.6.5 E-UTRAN to trusted BBF access Handover with DSMIPv6 on S2c
This clause shows a call flow for a handover when a UE moves from an E-UTRAN
to an untrusted BBF access network.
Figure 5.2.2.6.5-1: E-UTRAN to untrusted BBFAccess Handover
Both the roaming and non-roaming scenarios are depicted in the figure.
For connectivity to multiple PDNs, steps 5-8 are repeated for each PDN the UE
is connected to.
The optional interaction steps between the BPCF and the PCRF in the procedures
only occur if dynamic policy provisioning is deployed. Otherwise policy may be
statically configured in the gateway.
1-2) The description of these steps are the same as for steps 1-2 in 23.402,
clause 8.4.3
3) If the BBF access network supports 3GPP-based (EAP) authentication, it may
be involved in the EAP access authentication procedure performed between the
UE and the EPC.
4) The UE receives a local IP address from the BBF Access Network. How this is
done is out of 3GPP scope, but it may involve IP address assignment by an RG
or a BNG.
5-9) The description of these steps are the same as for steps 6-11 in 23.402,
clause 8.3.2, excluding step 10.
10) Triggered by the IP-CAN Session establishment from the PDN GW, the PCRF
initiate the S9* session establishment with the BPCF. The Care of Address, IP-
CAN type, QoS information, and optionally the IMSI, needs to be included in
the request message which sending to the BPCF.
11) The BPCF may interact with the BNG, e.g. to download policies. This step
is out of 3GPP scope.
12) In order for the BPCF to perform admission control in the fixed network,
the PCRF (non-roaming case) or the v-PCRF (roaming case) may also use Gateway
Control and QoS Rules provision procedure to provide QoS information to the
BPCF.
#### 5.2.2.7 Procedures for untrusted BBF WLAN with traffic is routed back to
the EPC with S2c and PCRF-initiated S9* session establishment
##### 5.2.2.7.1 Initial Attach with DSMIPv6 on S2c to untrusted BBF access
This clause is related to the case when the UE attaches to a BBF access which
is considered as untrusted. In this case only S2c procedures can be used in
building block I. Gxb* session is being established between ePDG and PCRF when
UE initial attach to the EPC via BBF access.
The home routed roaming, LBO and non-roaming scenarios are depicted in the
figure.
\- In the LBO case, the 3GPP AAA Proxy acts as an intermediary, forwarding
messages from the 3GPP AAA Server in the HPLMN to the PDN GW in the VPLMN and
visa versa. Messages between the PDN GW in the VPLMN and the hPCRF in the
HPLMN are forwarded by the vPCRF in the VPLMN.
\- In the non-roaming case, the vPCRF and the 3GPP AAA Proxy are not involved.
If dynamic policy provisioning over S9* is not deployed, the optional steps 5
and 15 in Figure 5.2.2.6.1-1 do not occur. Instead, the BBF Access Network may
employ static configured policies.
Figure 5.2.2.7.1-1: Initial attachment when S2c is used for roaming, non-
roaming and LBO
  1. If the BBF access network supports 3GPP-based (EAP) authentication, it may be involved in the EAP access authentication procedure performed between the UE and the EPC.
  2. The UE receives a local IP address from the BBF Access Network. How this is done is out of 3GPP scope, but it may involve IP address assignment by an RG or a BNG.
  3. The IKEv2 tunnel establishment procedure is started by the UE. For detail information, please refer to step 1 in TS 23.402, clause 7.3
  4. The ePDG initiates Gxb* session establishment by using Gateway Control Session establishment procedure with the PCRF. The ePDG includes the IMSI, APN, IP-CAN type, UE IP address allocated by EPC and the outer IP header information of the tunnelled traffic in the message to the PCRF.
> Editor's note: It is FFS whether other information is needed to be sent by
> ePDG to the PCRF in this step.
>
> For roaming case, the ePDG initiates Gateway Control Session establishment
> procedure with the v-PCRF. The ePDG contains IMSI, APN, IP-CAN type, UE IP
> address allocated by EPC and outer IP header information of the tunnelled
> traffic in the request message. When the v-PCRF receives a Gateway Control
> Session establishment request, the v-PCRF shall initiate S9 session
> establishment/modification procedure. The v-PCRF sends a S9 session
> establishment request to the h-PCRF with the information received over Gxb*
> interface excluding tunnelled traffice related info (e.g. outer IP header
> info of the tunnelled traffic).
  1. Triggered by the Gxb* session establishment, the PCRF (non-roaming case) or the v-PCRF (roaming case) initiates Gateway Control Session establishment with the BPCF to establish S9* Session. The IMSI, IP-CAN type, and outer IP header information for tunnel traffic needs to be included in the request message which sending to the BPCF.
> 6-13. The description of these steps are the same as for steps 2-8 in TS
> 23.402, clause 7.3
>
> 14\. In order for the BPCF to perform admission control in the fixed
> network, the PCRF use Gateway Control and QoS Rules provision procedure to
> provide QoS information to the BPCF.
##### 5.2.2.7.2 UE-initiated Detach Procedure and UE-Requested PDN
Disconnection with S2c in untrusted BBF access
The procedure in this clause applies to Detach Procedures, initiated by UE,
and to the UE-requested PDN disconnection procedure. The UE can initiate the
Detach procedure, e.g. when the UE is power off. For multiple PDN
connectivity, this detach procedure shall be repeated for each PDN connected.
The home routed roaming, LBO and non-roaming scenarios are depicted in the
figure. In the LBO case, the 3GPP AAA Proxy acts as an intermediary,
forwarding messages from the 3GPP AAA Server in the HPLMN to the PDN GW in the
VPLMN and visa versa. Messages between the PDN GW in the VPLMN and the hPCRF
in the HPLMN are forwarded by the vPCRF in the VPLMN. In the non-roaming case,
the vPCRF and the 3GPP AAA Proxy are not involved.
If dynamic policy provisioning over S9* is not deployed, the optional step 6
does not occur. Instead, the BBF access network may employ static configured
policies.
Figure 5.2.2.7.2-1: UE-initiated detach procedure with DSMIPv6
1-4) The description of these steps are the same as for steps 1-4 in 23.402,
clause 7.5.2
5) The PCRF executes a Gateway Control and QoS Rules Provision procedure or,
if this is the last PDN Connection for the UE, a PCRF-Initiated Gateway
Control Session Termination Procedure with the BPCF would be performed.
6-8) The description of this step is the same as for step 6 in 23.402, clause
7.5.2
##### 5.2.2.7.3 HSS-initiated Detach Procedure with S2c in untrusted BBF
access
The procedure in this clause applies to Detach Procedures, initiated by HSS.
Figure 5.2.2.7.3-1: HSS-initiated detach procedure with DSMIPv6
1-5) The description of these steps are the same as for steps 1-5 in 23.402,
clause 7.5.3
6) The PCRF (non-roaming case) or the v-PCRF (roaming case) executes a Gateway
Control and QoS Rules Provision procedure or, if this is the last PDN
Connection for the UE, a PCRF-Initiated Gateway Control Session Termination
Procedure with the BPCF would be performed.
7-9) The description of these steps are the same as for steps 6-8 in 23.402,
clause 7.5.3
##### 5.2.2.7.4 PDN GW-initiated PDN disconnection Procedure with S2c in
untrusted BBF access
The procedure in this clause applies to PDN disconnection procedure initiated
by PDN GW.
Figure 5.2.2.7.4-1: PDN GW-initiated PDN disconnection procedure with DSMIPv6
1-4) The description of these steps are the same as for steps 1-4 in 23.402,
clause 7.5.4
5) The PCRF (non-roaming case) or the v-PCRF (roaming case) executes a Gateway
Control and QoS Rules Provision procedure or, if this is the last PDN
Connection for the UE, a PCRF-Initiated Gateway Control Session Termination
Procedure with the BPCF would be performed.
6-8) The description of these steps are the same as for steps 5-6 in 23.402,
clause 7.5.4
##### 5.2.2.7.5 E-UTRAN to untrusted BBF access Handover with DSMIPv6 on S2c
This clause shows a call flow for a handover when a UE moves from an E-UTRAN
to an untrusted BBF access network.
Figure 5.2.2.7.5-1: E-UTRAN to untrusted BBFAccess Handover
Both the roaming and non-roaming scenarios are depicted in the figure.
For connectivity to multiple PDNs, steps 10-13 are repeated for each PDN the
UE is connected to.
The optional interaction steps between the BPCF and the PCRF in the procedures
only occur if dynamic policy provisioning is deployed. Otherwise policy may be
statically configured in the gateway.
1-2) The description of these steps are the same as for steps 1-2 in 23.402,
clause 8.4.3
3) If the BBF access network supports 3GPP-based (EAP) authentication, it may
be involved in the EAP access authentication procedure performed between the
UE and the EPC. As part of this step, the permanent user identity (IMSI) is
provided from the 3GPP AAA Server to the BBF access network. Otherwise, this
step is omitted.
4) The UE receives a local IP address from the BBF Access Network. How this is
done is out of 3GPP scope, but it may involve IP address assignment by an RG
or a BNG.
5) The IKEv2 tunnel establishment procedure is started by the UE. For detail
information, please refer to step 4 in TS 23.402, clause 8.4.3
6) The ePDG initiates Gxb* session establishment by using Gateway Control
Session establishment procedure with the PCRF. The ePDG includes the IMSI,
APN, IP-CAN type, UE IP address allocated by EPC and the outer IP header
information of the tunnelled traffic in the message to the PCRF.
> Editor's note: It is FFS whether other information is needed to be sent by
> ePDG to the PCRF in this step.
>
> For roaming case, the ePDG initiates Gateway Control Session establishment
> procedure with the v-PCRF. The ePDG contains IMSI, APN, IP-CAN type, UE IP
> address allocated by EPC and outer IP header information of the tunnelled
> traffic in the request message. When the v-PCRF receives a Gateway Control
> Session establishment request, the v-PCRF shall initiate S9 session
> establishment/modification procedure. The v-PCRF sends a S9 session
> establishment request to the h-PCRF with the information received over Gxb*
> interface excluding tunnelled traffice related info (e.g. outer IP header
> info of the tunnelled traffic).
7) Triggered by the Gxb* session establishment, the PCRF (non-roaming case) or
the v-PCRF (roaming case) initiates Gateway Control Session establishment with
the BPCF to establish S9* Session. The IMSI, IP-CAN type, and outer IP header
information for tunnel traffic needs to be included in the request message
which sending to the BPCF.
8-14) The description of these steps are the same as for steps 5-10 in 23.402,
clause 8.4.3.
15) In order for the BPCF to perform admission control in the fixed network,
the PCRF use Gateway Control and QoS Rules provision procedure to provide QoS
information to the BPCF.
### 5.2.3 Conclusion
Editor's Note: This clause will provide conclusions and descriptions with
respect to what specification work is required for the item.
## 5.3 Interworking between 3GPP and BBF architectures for authentication,
including identities, when WLAN is used
### 5.3.1 Description
This item covers interworking between 3GPP and BBF architectures for
authentication, including identities, on top of Release 9 baseline
architecture, when the UE accesses over WLAN
### 5.3.2 Solution
3GPP EPS defines several procedures for authentication of a 3GPP UE accessing
over a non-3GPP access. These include:
\- Access authentication procedures based on EAP-AKA and EAP-AKA'. For access
authentication, EAP signaling is forwarded between BBF AAA Server and 3GPP AAA
Server/proxy via the SWa and STa reference points.
\- Tunnel authentication procedures for SWu based on EAP-AKA. This
authentication is transparent to the BBF Access Network.
\- Authentication for S2c (DSMIPv6) based on EAP-AKA. This authentication is
transparent to the BBF Access Network.
Editor's note: The solutions for supporting 3GPP-based access authentication
in BBF access networks are work in progress in BBF.
The basic functionality of the existing SWa and STa reference points is
adequate to support BBF Access Interworking. Minor enhancements of the SWa
reference point, on top of Release 9 baseline architecture, is needed to carry
the permanent user identity (i.e. IMSI) in the successful response from 3GPP
AAA Server to BBF AAA Server.
To support interworking with BBF access networks one scenario for deployment
is that 3GPP-based access authentication is supported by the BBF access
networks. This would make the BBF access aware that a 3GPP terminal is
connecting via BBF access and of the user and operator identity by means of
NAI and would allow the BPCF to initiate a S9* session towards the PCRF for
the UE.
Another scenario for deployment is that 3GPP-based access authentication is
not performed and that the BBF access is not aware of the 3GPP terminal. To
support this scenario, the S9* session could be initiated from the PCRF
towards the BBF access network. The S9* procedures are described in Clause
5.2.
### 5.3.3 Conclusion
The existing release 9 baseline supports all authentication procedures needed
for Building Block 1.
Minor enhancements to SWa is needed to support 3GPP-based authentication for
BBF Access Interworking. Currently the only identified addition to SWa is to
provide the permanent user identity (IMSI) in the reply from 3GPP AAA Server
to BBF AAA Server. (Note that IMSI is already included on STa).
Editor's note: The SWa and STa references points are defined in TS 29.273 and
are using the Diameter protocol. In case the BBF AAA Server only supports
RADIUS some additional interworking mechanisms may be needed. This issue is
FFS.
## 5.4 IP flow mobility support in BBF accesses
### 5.4.1 Description
This item covers support of IP flow mobility for interworking between 3GPP and
BBF architectures.
### 5.4.2 Solution
3GPP TS 23.261 defines extensions to DSMIPv6 to support IP flow mobility
between 3GPP and WLAN accesses. The solution defined in TS 23.261 does not
depend on the access network architecture where the WLAN is located and
therefore there is no BBF-specific considerations to be added to what
documented in the current specification.
One aspect worth noting is that TS 23.261 and TS 23.203 define some extensions
to the PCC architecture to support IP flow mobility. These extensions however
are limited only to Gx reference point. Therefore no impact is foreseen to S9*
or any other PCC interface towards the BBF access.
### 5.4.3 Conclusion
The existing Release 10 IP flow mobility specification supports all procedures
needed to support IP flow mobility between 3GPP accesses and WLAN accesses
located in a BBF access network.
## 5.5 H(e)NB interworking architecture alternative 1
### 5.5.1 Procedures
Editor\'s note: The message names and protocol specific are not finalised.
NOTE: The following procedures are created on the assumption that the result
of authorisation of resources in the fixed access does not need to be known
before completion of radio procedures. Otherwise the S9* authorisation must
complete before the radio procedures are sent onto the H(e)NB.
#### 5.5.1.1 H(e)NB power on
Figure 5.3.4.1-1: Update H(e)NB Binding on H(e)NB power on
1) If configured, H(e)NB establishes an IPSec connection towards the SeGW.
2) The SeGW, if present, informs the H(e)NB policy function of the binding
between the CPE IP address CPE (outer IP address) and the IP address assigned
to the H(e)NB (inner IP address).
3) The H(e)NB Policy Function accepts the updated information.
4) The H(e)NB establishes the S1 or Iuh connection to the H(e)NB GW or MME as
per normal procedures.
5) The H(e)NB GW / MME establishes an S? session to the H(e)NB policy function
including information about the H(e)NB such as CSG ID, IP address assigned to
the H(e)NB.
6) The H(e)NB policy function identifies the IP address associated with the
fixed access over which the H(e)NB is communicating based on information
received during step 2. The H(e)NB policy function establishes an S9* session
towards the BPCF using the IP address of the fixed access. Policies applied
may, for example, be associated with control plane signalling or management
traffic for the H(e)NB.
7) The BPCF responds to the request
8) The H(e)NB policy function responds to the H(e)NB GW / MME.
NOTE: If the CPE is acting as a bridge device, BBF procedures may be applied
for IP-CAN session establishment for the H(e)NB when it is first connected to
the CPE. Once IPSec establishment is complete, the BPCF binds this to the
subsequent request from the H(e)NB policy function
#### 5.5.1.2 UE initial attach and Idle-to-Active transition whilst on H(e)NB
Figure 5.5.1.2-1: UE initial attach to a H(e)NB
NOTE: This flow does not include all the steps associated with Attach
Procedure or UE triggered Service Request from 23.401 and 23.060.
1) The UE performs either an initial attach or Service Request for idle-to-
active transition.
2) The MME / SGSN sends a RAB Assignment Request or Initial Context Setup
Request message towards the H(e)NB.
3) On reception of the RAB Assignment Request or Initial Context Setup Request
message at the H(e)NB GW, the H(e)NB GW requests authorisation for the
bearer(s) that form part of the original request including the IP address
assigned to the H(e)NB and the CSG membership status of the UE.
4) The H(e)NB policy function decides what action to take and may update the
S9* session as a result of the decision. This reuses the S9* session
established at H(e)NB power on.
5) The BPCF acknowledges the changes to the session
6) The H(e)NB policy function responds with the outcome of the authorisation
request
7) The remainder of the attach / service request procedure completes. This
occurs independently of steps 3-6.
#### 5.5.1.3 Idle mode mobility onto H(e)NB
No specific procedures in this scenario. Resource authorisation only needs to
be performed when a bearer is to be established.
#### 5.5.1.4 Bearer Activation / Modification / Deactivation {#bearer-
activation-modification-deactivation .list-paragraph}
Figure 5.5.1.4-1: Bearer establishment / modification / deactviation on a
H(e)NB
NOTE: This flow does not include all the steps associated with Bearer
establishment / modification / deactivation procedures from 23.401 and 23.060.
1) The MME / SGSN receives a Create / Modify / Delete Bearer Request message
from EPC.
2) The MME / SGSN sends a RAB Assignment Request or Bearer Setup Request
message towards the H(e)NB.
3) On reception of the RAB Assignment Request or Bearer Setup Request message
at the H(e)NB GW, the H(e)NB GW requests authorisation for the bearer(s) that
form part of the original request including the IP address assigned to the
H(e)NB and the CSG membership status of the UE.
4) The H(e)NB policy function decides what action to take and may update the
S9* session as a result of the decision. This reuses the S9* session
established at H(e)NB power on.
5) The BPCF acknowledges the changes to the session
6) The H(e)NB policy function responds with the outcome of the authorisation
request
7) The remainder of the bearer establishment / modification / deactivation
procedure completes. This occurs independently of steps 3-6.
#### 5.5.1.5 Inter H(e)NB mobility
##### 5.5.1.5.1 To different H(e)NB GW
Figure 5.5.1.5.1-1: Mobility from H(e)NB to another H(e)NB associated with
another H(e)NB GW
NOTE: This flow does not include all the steps associated with S1-based
handover / SRNS relocation procedure from 23.401.
1) The source H(e)NB sends a Handover Notify towards the target MME / SGSN via
the source MME/SGSN.
2) Handover procedures continue as per TS 23.401 / 23.060. The target MME /
SGSN sends a Handover Request to the target H(e)NB.
3) On reception of the Handover Request message at the target H(e)NB GW, the
target H(e)NB GW requests authorisation for the bearer(s) that form part of
the original request including the IP address assigned to the target H(e)NB
and the CSG membership status of the UE.
4) The target H(e)NB policy function decides what action to take and may
update the S9* session as a result of the decision. This reuses the S9*
session established at target H(e)NB power on.
5) The BPCF acknowledges the changes to the session
6) The H(e)NB policy function responds with the outcome of the authorisation
request
7) The target H(e)NB acknowledges the Handover Request
8) Handover procedures proceed as per TS 23.401 / 23.060. The source MME /
SGSN receives Forward Relocation Complete message.
9) The source MME deletes the UE context in the H(e)NB by sending a UE Context
Release request towards the H(e)NB.
10) On reception of the RAB Assignment Request or UE Context Release Request
message at the H(e)NB GW, the H(e)NB GW requests authorisation for the
bearer(s) that are being released.
11) The H(e)NB policy function decides what action to take and may update the
S9* session as a result of the decision. This reuses the S9* session
established at source H(e)NB power on.
12) The BPCF acknowledges the changes to the session
13) The H(e)NB policy function responds with the outcome of the authorisation
request
14) The remainder of the Handover procedure completes. This occurs
independently of steps 10-13.
#### 5.5.1.6 Mobility to macro network {#mobility-to-macro-network .list-
paragraph}
Figure 5.5.1.6-1: Mobility from H(e)NB to macro (example with CN node
relocation)
NOTE: This flow does not include all the steps associated with S1-based
Handover / SRNS Relocation procedure from 23.401.
1) The source H(e)NB sends a Handover Notify towards the target MME / SGSN via
the source MME/SGSN.
2) Handover procedures continue as per TS 23.401. The source MME / SGSN
receives Forward Relocation Complete message.
3) The source MME deletes the UE context in the H(e)NB by sending a UE Context
Release request towards the H(e)NB.
4) On reception of the RAB Assignment Request or UE Context Release Request
message at the H(e)NB GW, the H(e)NB GW requests authorisation for the
bearer(s) that are being released.
5) The H(e)NB policy function decides what action to take and may update the
S9* session as a result of the decision. This reuses the S9* session
established at H(e)NB power on.
6) The BPCF acknowledges the changes to the session
7) The H(e)NB policy function responds with the outcome of the authorisation
request
8) The remainder of the Handover procedure completes. This occurs
independently of steps 4-7.
#### 5.5.1.7 UE Attach without HeNB GW {#ue-attach-without-henb-gw .list-
paragraph}
Figure 5.5.1.7-1: UE initial attach to a HeNB without HeNB GW
NOTE: This flow does not include all the steps associated with Attach
Procedure or UE triggered Service Request from 23.401.
1) The UE performs either an initial attach or Service Request for idle-to-
active transition.
2) The MME sends an Initial Context Setup Request message towards the HeNB.
3) In parallel to step 2, the MME requests authorisation for the bearer(s)
that form part of the original request including the IP address assigned to
the HeNB and the CSG membership status of the UE.
4) The HeNB policy function decides what action to take and may update the S9*
session as a result of the decision. This reuses the S9* session established
at HeNB power on.
5) The BPCF acknowledges the changes to the session
6) The HeNB policy function responds with the outcome of the authorisation
request
7) The remainder of the attach / service request procedure completes. This
occurs independently of steps 3-6.
#### 5.5.1.8 CS call establishment {#cs-call-establishment .list-paragraph}
Figure 5.5.1.8-1: CS call establishment
NOTE: This flow does not include all the steps associated with CS call setup.
1) The UE initiates call setup using a SETUP message.
2) The MSC sends a RAB Assignment Request message towards the HNB.
3) In parallel to step 2, the HNB GW requests authorisation for the bearer(s)
that form part of the original request including the IP address assigned to
the HNB and the CSG membership status of the UE.
4) The HNB policy function decides what action to take and may update the S9*
session as a result of the decision. This reuses the S9* session established
at HNB power on.
5) The BPCF acknowledges the changes to the session
6) The HNB policy function responds with the outcome of the authorisation
request
7) The remainder of the call setup procedure completes. This occurs
independently of steps 3-6.
#### 5.5.1.9 UE detach and Active-to-Idle transition whilst on H(e)NB
Figure 5.5.1.9-1: UE detach or Active-to-Idle transition on a H(e)NB
NOTE: This flow does not include all the steps associated with Detach
Procedure or Iu/S1 Release from 23.401 and 23.060.
1) The UE performs either a detach or the HNB performs initiates an Iu release
for active-to-idle transition.
2) The MME / SGSN sends a RAB Assignment Request or Initial Context Setup
Request message towards the H(e)NB.
3) On reception of the RAB Assignment Request or Context Release Request
message at the H(e)NB GW, the H(e)NB GW requests authorisation for the
bearer(s) that form part of the original request including the IP address
assigned to the H(e)NB.
4) The H(e)NB policy function decides what action to take and may update the
S9* session as a result of the decision. This reuses the S9* session
established at H(e)NB power on.
5) The BPCF acknowledges the changes to the session
6) The H(e)NB policy function responds with the outcome of the authorisation
request
7) The remainder of the detach / release procedure completes. This occurs
independently of steps 3-6.
## 5.6 H(e)NB interworking architecture alternative 3
### 5.6.1 General
### 5.6.2 Procedures
#### 5.6.2.1 Procedures for the case when H(e)NB is being used and traffic is
routed back to the EPC
##### 5.6.2.1.1 S9* Session Establishment Procedure
The procedure in this clause applies to S9* Session Establishment Procedure,
initiated by the H(e)NB Policy Function during the H(e)NB Registration
Procedure.
Figure 5.6.2.1.1-1: S9* Session Establishment Procedure
  1. When the H(e)NB powers on, it receives a local IP address from the BBF Access Network. How this is done is out of 3GPP scope, but it may involve IP address assignment by an RG or a BNG. The local IP address will be the outer IP address of the IPSec tunnel between the H(e)NB and the SeGW.
  2. The IKEv2 tunnel establishment procedure is started by the H(e)NB. The H(e)NB may indicate in a notification part of the IKEv2 authentication request that it supports MOBIKE. The SeGW IP address to which the H(e)NB needs to form IPSec tunnel is discovered via DNS query as specified in clause 5.1 in TS32.583 and TS32.593. A secure connection is established between the H(e)NB and Security Gateway. The SeGW assigns an IP address to the H(e)NB as the inner IP address of the IPSec tunnel.
  3. The SeGW sends the Notify Request message to the H(e)NB Policy Function, which contains the IPSec Tunnel information (e.g. the outer IP address, the inner IP address, etc. ).
  4. The H(e)NB Policy Function shall store the IPsec Tunnel information and sends a Notify Response message to the SeGW.
  5. Triggered by step3, the H(e)NB Policy Function initiates establishment of an S9*session by sending GW Control Session Establishment(IPSec Tunnel Information) message to BPCF. The BPCF stores the IPsec Tunnel information to identify the access point of the H(e)NB in the BBF Access network.
  6. The BPCF acknowledges the Gateway Control Session Establishment message by sending an GW Control Session Establishment Ack message to the H(e)NB Policy Function.
  7. The H(e)NB initiates the Registration to H(e)MS Procedure as specified in in clause 5.2.1 in TS32.583 and in clause 5.1.3 in TS32.593.
  8. The H(e)NB initiates the Registration to H(e)NB-GW, which is already defined in TS 25.467 section 5.2.2 and in TS36.413 section 8.7.3.
##### 5.6.2.1.2 Bearer Activation [ ]{.underline} Procedure
###### 5.6.2.1.2.1 Bearer Activation when a UE attaches to EUTRAN via HeNB
subsystem
The bearer activation procedure for a UE attaches to EUTRAN via HeNB subsystem
is depicted in figure 5.6.2.1.2-1.
Figure 5.6.2.1.2-1: Bearer activation procedure for a UE attaches to EUTRAN
via HeNB subsystem
NOTE: If a HeNB GW is required in the HeNB subsystem, the messages between the
HeNB and the MME shall traverse the HeNB GW.
  1. If the EPS bearer establishment is required (e.g. default bearer creation, dedicated bearer activation, UE requested bearer resource modification), the Serving GW will send a Create Bearer Request/ Create Session Response message to the MME as defined in TS23.401.
  2. The MME sends to the HeNB the Initial Context Setup Request message during the default bearer creation procedure,or the Bearer Setup Request /Session Management Request message during the dedicated bearer activation procedure and the UE requested bearer resource modification procedure. The messages shall contain the EPS Bearer Identity, the EPS Bearer QoS, as defined in TS23.401.
  3. The HeNB sends the Resource Allocation Request (the EPS Bearer QoS) message to the H(e)NB Policy Function.
  4. The H(e)NB Policy Function requests the BPCF to perform admission control. The H(e)NB Policy Function sends the GW Control and QoS Rule Provision (QoS-Rule with the QoS information) message to BPCF. The BPCF performs admission control in BBF access based on the QoS-Rule with the QoS information, which includes QCI, GBR, MBR, and ARP.
  5. The BPCF finds the HeNB's access point in the BBF access network, and acquires the available resources at this access point. The BPCF takes into account the information contained in the QoS rule and the available resources at the HeNB's access point, but the details for how admission control is performed in the BBF access is out of scope to 3GPP. If the request is accepted the BPCF may provision the BRAS/BNG with information for QoS control of the service data flow.
> The BPCF sends an GW Control and QoS Rule Provision Ack message to the
> H(e)NB Policy Function.
  1. The H(e)NB Policy Function sends Resource Allocation Response to the corresponding HeNB.
  2. The H(e)NB allocates the radio resource, and continue with radio bearer establishment procedure.
  3. As defined in TS23.401, the H(e)NB sends to the MME the Initial Context Setup Response message during the default bearer creation procedure,or the Bearer Setup Response /Session Management Response message during the dedicated bearer activation procedure and the UE requested bearer resource modification procedure.
###### 5.6.2.1.2.2 PDP Context Activation when a UE attaches to UTRAN/GERAN
via HNB subsystem
The PDP Context Activation Procedure for a UE attaches to UTRAN/GERAN via HNB
subsystem is depicted in figure 5.6.2.1.2-2.
Figure 5.6.2.1.2-2: PDP Context Activation Procedure for a UE attaches to
EUTRAN via HeNB subsystem
  1. If the PDP Context creation is required (e.g. PDP Context Activation, secondary PDP Context Activation, Network-Requested PDP Context Activation), the GGSN/Serving GW will send a Create PDP Context Response/Create Bearer Request message to the SGSN as defined in TS23.060.
  2. The SGSN initiates RAB setup by the RAB Assignment procedure sending a RAB Assignment Request message to the HNB via HNB GW to establish one or several RABs. The message shall contain the RAB information to be established as defined in TS23.060.
  3. . The steps are the same as for steps 3-7 in the clause 5.6.2.1.2.1.
  4. The HNB sends to the SGSN the RAB Assignment Response message via HNB GW, as defined in TS23.060.
##### 5.6.2.1.3 Bearer Deactivation Procedure
###### 5.6.2.1.3.1 Bearer deactivation when a UE attaches to EUTRAN via HeNB
subsystem
The bearer deactivation procedure for a UE attaches to EUTRAN via HeNB
subsystem is depicted in figure 5.6.2.1.3‑1.
Figure 5.6.2.1.3‑1: Bearer deactivation procedure for a UE attaches to EUTRAN
via HeNB subsystem
NOTE: If a HeNB GW is required in the HeNB subsystem, the messages between the
HeNB and the MME shall traverse the HeNB GW.
  1. If the EPS bearer deactivation is required (e.g. PDN GW initiated bearer deactivation, MME Initiated Dedicated Bearer Deactivation detach, S1 release), the Serving GW will send a Delete Bearer Request / Release Access Bearers Response message to the MME as defined in TS23.401.
  2. As defined in TS23.401, the MME sends to the HeNB the Delete Bearer Request(the EPS Bearer Identity) message during PDN GW initiated bearer deactivation procedure and MME Initiated Dedicated Bearer Deactivation procedure, or sends to the HeNB the S1 UE Context Release Command(cause) message during the detach procedure and the S1 release procedure.
  3. The HeNB releases the radio resource, and initiates radio bearer release.
  4. The HeNB sends the Resource Release Request (the EPS Bearer QoS) message to the H(e)NB Policy Function.
  5. The H(e)NB Policy Function requests the BPCF to release the resource indicated in the Resource Release Request message. The H(e)NB Policy Function sends the GW Control and QoS Rule Provision (QoS-Rule with the QoS information) message to BPCF. The BPCF releases the corresponding resources in BBF access network based on the QoS-Rule with the QoS information.
> If all the activated bearers are released, the H(e)NB Policy Function should
> send GW Control Session [Termination]{.underline} [to BPCF t]{.underline}o
> terminate the S9* session.
  1. The BPCF takes into account the information contained in the QoS rule and release the corresponding resources, but the details for how to release the resource in the BBF access is out of scope to 3GPP.
> The BPCF acknowledges the GW Control and QoS Rule Provision message by
> sending an GW Control and QoS Rule Provision Ack message to the H(e)NB
> Policy Function.
>
> If the H(e)NB Policy Function indicates the BPCF to terminate the S9*
> session, the BPCF release the S9* session context and sends GW Control
> Session [Termination]{.underline} [Ack to]{.underline} the H(e)NB Policy
> Function.
  1. The H(e)NB Policy Function sends Resource Release Response to the corresponding HeNB.
> If all the activated bearers are released, the H(e)NB Policy Function
> releases the S9* session.
  1. As defined in TS23.401, the HeNB sends to the MME the Delete Bearer Response / S1 UE Context Release Complete message.
###### 5.6.2.1.3.2 PDP Context Deactivation when a UE attaches to UTRAN/GERAN
via HNB subsystem
The PDP Context Deactivation procedure for a UE attaches to UTRAN/GERAN via
HNB subsystem is depicted in figure 5.6.2.1.3-2.
Figure 5.6.2.1.3-2: PDP Context Deactivation procedure for a UE attaches to
UTRAN/GERAN via HNB subsystem
  1. If the PDP Context delete is required (e.g. PDP Context Deactivation, Detach, RAB Release), the SGSN will be triggered to release the resources as defined in TS23.060.
  2. As defined in TS23.060, the SGSN initiates RAB release by the RAB Assignment procedure sending a RAB Assignment Request message to the HNB via HNB GW to release one or several RABs. The message shall contain the RAB information to be released.
  3. The description of these steps are the same as for steps 3-7 in the clause 5.6.2.1.3.1.
  4. The HNB sends to the SGSN the RAB Assignment Response message via HNB GW, as defined in TS23.060.
###### 5.6.2.1.3.3 Iu Release when a UE attaches to UTRAN/GERAN via HNB
subsystem
The Iu Release procedure for a UE attaches to UTRAN/GERAN via HNB subsystem is
depicted in figure 5.6.2.1.3‑3.
Figure 5.6.2.1.3-3: Iu Release procedure for a UE attaches to UTRAN/GERAN via
HNB subsystem
  1. HNB initiates Iu Release Procedure, and sends Iu Release Request message to SGSN via HNB GW as defined in TS23.060.
  2. As defined in TS23.060, the SGSN acknowledges the Iu Release Command message by sending Iu Release Command message.
  3. The HNB may release the radio resource, and initiates radio bearer release as defined in TS23.060.
  4. Procedures are the same as for steps 4-7 in the clause 5.6.2.1.3.1.
  5. The HNB sends to the SGSN the Iu Release complete message via HNB GW, as defined in TS23.060.
##### 5.6.2.1.4 Bearer Modification Procedure
###### 5.6.2.1.4.1 Bearer Modification when a UE attaches to EUTRAN via HeNB
subsystem
The bearer modification procedure for a UE attaches to EUTRAN via HeNB
subsystem is depicted in figure 5.6.2.1.4‑1.
Figure 5.6.2.1.4‑1: Bearer modification procedure for a UE attaches to EUTRAN
via HeNB subsystem
NOTE: If a HeNB GW is required in the HeNB subsystem, the messages between the
HeNB and the MME shall traverse the HeNB GW.
  1. If the EPS bearer modification is required (e.g. PDN GW initiated bearer modification with bearer QoS update, HSS Initiated Subscribed QoS Modification), the PDN GW will send a Update Bearer Request message to the MME through the Serving GW as defined in TS23.401.
  2. As defined in TS23.401, the MME sends the Bearer Modification Request/Session Management Request (the EPS Bearer Identity, EPS Bearer QoS) message to the HeNB.
  3. The HeNB sends the Resource Modification Request (the EPS Bearer QoS) message to the H(e)NB Policy Founction through the SeGW.
  4. The H(e)NB Policy Function requests the BPCF to modify the resource indicated in the Resource Modification Request message. The H(e)NB Policy Function sends the GW Control and QoS Rule Provision (QoS-Rule with the QoS information) message to BPCF. The QoS-Rule with the QoS information indicates the BPCF how to modify the corresponding resources in BBF access network.
  5. The BPCF takes into account the information contained in the QoS rule and modifies the corresponding resources, but the details for how to modify the resource in the BBF access is out of scope to 3GPP.
> The BPCF acknowledges the GW Control and QoS Rule Provision message by
> sending an GW Control and QoS Rule Provision Ack message to the H(e)NB
> Policy Function.
  1. The H(e)NB Policy Function sends Resource Modification Response to the corresponding HeNB according to the Tunnel header information in the S9* Session context.
  2. The HeNB initiates the radio resource reconfiguration.
  3. As defined in TS23.401, the HeNB sends to the MME the Bearer Modification Response/Session Management Response message.
###### 5.6.2.1.4.2 PDP Context Modification when a UE attaches to UTRAN/GERAN
via HNB subsystem
The PDP Context Modification procedure for a UE attaches to UTRAN/GERAN via
HNB subsystem is depicted in figure 5.6.2.1.4-2.
Figure 5.6.2.1.4-2: PDP Context Modification procedure for a UE attaches to
UTRAN/GERAN via HNB subsystem
  1. If the PDP Context modification is required (e.g. SGSN-Initiated PDP Context Modification, GGSN-Initiated PDP Context Modification, MS-Initiated PDP Context Modification, RAN-initiated RAB Modification), the SGSN will be triggered to modify the RAB parameters as defined in TS23.060.
  2. As defined in TS23.060, the SGSN initiates RAB modification by the RAB Assignment procedure. sending a RAB Assignment Request message to the HNB via HNB GW to release one or several RABs. The message shall contain the RAB information to be modified.
  3. The description of these steps are the same as for steps 3-7 in the clause 5..2.1.4.1.
  4. The HNB sends to the SGSN the RAB Assignment Response message via HNB GW, as defined in TS23.060.
## 5.7 Comparison of 3GPP LTE Femto Architecture Options
### 5.7.1 General
The rows in the comparison table include the solutions and the columns the
attributes addressing various aspects of the impact on the network. The table
also identifies the NE/s impacted by a particular solution.
The attributes are meant to answer the questions in the following areas:
**Roaming transparency**
Is the home network aware that the roaming user access the VPLMN via a 3GPP
Femto connected to BBF access?
**BBF QoS Negotiation**
Are Radio Resources allocated to the UE in before it is known whether
resources are available in the BBF access?
**New Interface/Signaling Sequence in 3GPP (besides S9*)**
Does the solution require a 3GPP NE to support a new interface and protocol?
**Correlation of UE PCC & S9* QoS sessions**
Is the S9* session is independent of the UE PCC session?
**Overlay Architecture**
Does the solution enhance the existing PCC architecture to handle the S9*
session or requires an overlay architecture with new reference point/s and a
new policy server (i.e. Femto-PCRF)?
**Additional Signaling Load**
Does the solution generate additional signaling load in the network? (The S9*
signaling is excluded from the comparisons as it is common with all
solutions.)
**Commonality with WLAN PCRF-BBCP IWK**
Is the 3GPP Femto solution compatible with the WLAN solution?
**Impact on 3GPP NEs**
A NE is said to be impacted when the solution requires that the NE supports a
new reference point. For instance, the HeNB GW solution requires that the HeNB
GW supports a new diameter interface to the F-PCRF and therefore the NE is
impacted.
A NE is said not be impacted by the solution when it is required to support
only a new IE in he message set and procedures it already supports. For
instance, the PCRF based solution does not require the MME, S-GW or P-GW to
support a new interface/protocol but a new IE to carry the Tunnel-INFO from
the MME to the PCRF using existing messages and signalling sequences.
Therefore, the PCRF based solution does not impact these NEs
**Interpretation of the arrows:**
The arrows in each cell are meant to indicate relative advantage/or
disadvantage of a particular solution. A plus sign (+) indicates advantage
while a minus sign (-) indicates a disadvantage.
### 5.7.2 Comparison
#### 5.7.2.1 LTE Architecture options
Architecture Alternative | Attribute |  |  |  |  |  |  |  |  |  |  |   
---|---|---|---|---|---|---|---|---|---|---|---|---  
| Roaming Trans-parency? | BBF QoS Negotiation | EPC: New Interface/Signaling Sequence (besides S9*) | Corre-lation of UE PCC & S9* QoS sessions (2) | Over-lay Archi-tecture | Addi-tional Signa-ling Load | Common-ality with WLAN PCRF-BBCP IWK | HeNB | SeGW | HeNB GW | M  
M  
E | P C R F  
PCRF (Alt 2) | No (3) (-) | Yes (+) | No (+) | Yes (+) | No (+) | Low (+) | Yes (+) | No (+) | No (+) | No (+) | No (6) (+) | Yes (7) (-)  
MME (option 1.1) (8) | Yes (+) | No (1) (-) | Yes (-) | No (-) | Yes (-) | High (-) | No (-) | No (+) | Yes (4) (-) | No (+) | Yes (-) | No (+)  
HeNB GW (Option 1.2) (8) | Yes (+) | No (1) (-) | Yes (-) | No (-) | Yes (-) | High (-) | No (-) | No (+) | Yes (4) (-) | Yes (-) | No (+) | No (+)  
HeNB (option 3) (8) | Yes (+) | No (1) (-) | Yes (-) | No (-) | Yes (-) | High (-) | No (-) | Yes (-) | No (+) | No (+) | No (+) | No (+)  
Table 5.2.2.1 -1 LTE Architecture options
Note 1: Backhaul QoS negotiation is possible if the F-PCRF waits for a
response from the BPCF before continuing with the remainder of the EPS
procedures or the variation detailed in slides are used.
Note 2: Correlation refers the 3GPP network. Note that It is not possible to
discriminate individual UE sessions at the BNG due to IPSec tunnelling.
Note 3: The limitation exists for the GTP HR traffic that is a very small
subset of the overall traffic. Note that the roaming subscriber must register
with the 3GPP Femto in the VPLMN. NOTE that this limitation applies also to
the 3GPP-BBF IWK architecture for WLAN.
Note 4: Required at H(e)NB Power up to interface with the F-PCRF/ H(e)NB
Policy Function
Note 5: New Interfaces to the F-PCRF
Note 6: Open issue on how MME retrieves tunnel info
Note 7: S1-AP and S5/S8 need to carry additional IE/s (e.g. IP@ of IPSec
tunnel). Open issue on how MME retrieves tunnel info.
Note 8: Require a new functional entity -- the F-PCRF, that may reside at the
PCRF
#### 5.7.2.2 UMTS Architecture Options
Option | Attribute |  |  |  |  |  |  |  |  |  |  |   
---|---|---|---|---|---|---|---|---|---|---|---|---  
| Roaming Transpa-rency | QoS Nego-tiation | EPC: New Interface/Signaling Sequence (besides S9*) | Correlati-on of UE PCC & S9* QoS sessions (2) | Overlay Architecture | Additio-nal Signaling Load | Commonality with WLAN PCRF-BBCP IWK | H-  
NB | Se-  
GW | H-  
NB  
GW | S  
G  
S  
N | P  
C  
R  
F  
PCRF  
(Alt 2)  
(8) | No (3) (-) | Yes (+) | No (+) | Yes (+) | No (+) | Low (+) | Yes (+) | No (+) | No (+) | No (+) | No (6)  
(+) | Yes (6)  
(-)  
HNB GW (Alt 1)  
(7) (10) | Yes (+) | No (1) (-) | Yes (-) | No (-) | Yes (-) | High (-) | No (-) | No (+) | Yes (4) (+) | Yes (-) | No (+) | No (+)  
HNB  
(Alt 3)  
(7) (9) (10) | Yes (+) | No (1) (-) | Yes (-) | No (-) | Yes (-) | High (-) | No (-) | Yes (-) | No (+) | No (+) | No (+) | No (+)  
Table 5.2.2.2 -1 UMTS Architecture options
Note 1: Backhaul QoS negotiation is possible if the F-PCRF waits for a
response from the BPCF before continuing with the remainder of the EPS
procedures or the variation detailed in slides are used.
Note 2: Correlation refers the 3GPP network. Note that It is not possible to
discriminate individual UE sessions at the BNG due to IPSec tunnelling.
Note 3: The limitation exists for the GTP HR traffic that is a very small
subset of the overall traffic. Note that the roaming subscriber must register
with the 3GPP Femto in the VPLMN. NOTE that this limitation applies also to
the 3GPP-BBF IWK architecture for WLAN.
Note-4: Required at H(e)NB Power up to interface with the F-PCRF/ H(e)NB
Policy Function
Note-5: New Interfaces to the F-PCRF
Note-6: Gn/Gp, S4 and S5/S8 need to carry additional IE/s (e.g. IP@ of IPSec
tunnel). Open issue on how the SGSN obtains the tunnel information.
Note-7: Require a new FE -- the F-PCRF, that may reside at the PCRF
Note-8: Support PS only. It is the same solution as for LTE Femto
Note-9 The signaling interface with the F-PCRF is not based on the Ruh
interface
Note 10: Supports PS and CS
# 6 Building Block II
Editor's Note: This subclause will contain the material related to Building
Block II.
# 7 Building Block III
Editor's Note: This subclause will contain the material related to Building
Block III.
#