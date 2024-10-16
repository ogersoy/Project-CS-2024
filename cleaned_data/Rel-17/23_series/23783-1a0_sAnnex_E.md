# Foreword
This Technical Specification has been produced by the 3rd Generation
Partnership Project (3GPP).
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
The objective of this technical specification is to **specify interworking
between MC systems and LMR systems that satisfy the MCPTT requirements in 3GPP
TS 22.179 [3], MCCoRe requirements in 3GPP TS 22.280 [2] and the MCData
requirements (SDS only) in 3GPP TS 22.282 [4].**
The present document refers to an InterWorking Function (IWF). The structure
and functionality of the IWF is out of scope of the present document. The
definition of reference points between the IWF and MC systems and the
interactions between the IWF and MC systems are in scope of the present
document.
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
[2] 3GPP TS 22.280: \"Mission Critical Services Common Requirements (MCCoRe);
Stage 1\".
[3] 3GPP TS 22.179: \"Mission Critical Push to Talk (MCPTT); Stage 1\".
[4] 3GPP TS 22.282: \"Mission Critical Data services\".
[5] 3GPP TS 23.280: \"Common functional architecture to support mission
critical services; Stage 2\".
[6] 3GPP TS 23.282: \"Functional architecture and information flows to support
Mission Critical Data (MCData); Stage 2\".
[7] 3GPP TS 23.379: \"Functional architecture and information flows to support
Mission Critical Push To Talk (MCPTT); Stage 2\".
[8] 3GPP TS 33.180: \"Security of the mission critical service\"
[9] TIA-603-D: \"Land Mobile FM or PM Communications Equipment Measurement and
Performance Standards\".
# 3 Definitions, symbols and abbreviations
## 3.1 Definitions
For the purposes of the present document, the terms and definitions given in
3GPP TR 21.905 [1] and the following apply. A term defined in the present
document takes precedence over the definition of the same term, if any, in
3GPP TR 21.905 [1].
**End‑to‑End Encryption:** encryption that is applied by an originating
terminal or client and is decrypted only by chosen terminating terminals or
clients.
**User homed in the IWF:** is an MC service ID that represents an LMR user in
the MC system.
**Interworking:** a means of communication between mission critical systems
and LMR systems whereby MC users obtaining service from a mission critical
system can communicate with LMR users who are obtaining service from one or
more LMR systems.
**Interworking function:** adapts LMR Systems to mission critical systems via
the IWF interface and supports interworking between LMR systems and mission
critical systems.
**Interworking group:** a group, which is composed of group members from the
MC system and the LMR system and defined in the MC system or the LMR system.
**LMR system:** the collection of applications, services, and enabling
capabilities providing a land mobile radio service offering group and private
communications.
**LMR user:** a user of a device which allows participation in an LMR system.
NOTE: The term LMR user is defined for discussion purposes only and is out of
scope of the present document.
## 3.2 Abbreviations
For the purposes of the present document, the abbreviations given in 3GPP TR
21.905 [1] and the following apply. An abbreviation defined in the present
document takes precedence over the definition of the same abbreviation, if
any, in 3GPP TR 21.905 [1].
E2EE End-to-End Encryption
IWF InterWorking Function
KEK Key Encryption Key (TETRA)
KMS Key Management Service
MC Mission Critical
MCPTT Mission Critical Push To Talk
LMR Land Mobile Radio
OTAK Over-The-Air-Key Management (TETRA)
OTAR Over-The-Air Rekeying (P25)
P25 Project 25
SDS Short Data Service
TETRA TErrestrial Trunked Radio
UE User Equipment
UKEK Unique Key Encryption Key (P25)
URI Uniform Resource Identifier
# 4 Introduction
Mission critical users currently employ a wide range of LMR mission critical
Push To Talk services, and associated data capabilities where available.
The present document describes the architecture to support the interworking
between the MC system and the LMR system to satisfy interworking requirements
specified in 3GPP TS 22.179 [3] and 3GPP TS 22.282 [4]. Other LMR technologies
may interwork as long as they conform to the present document.
The IWF, along with its LMR system, will appear as a peer interconnected MC
system. This is meant as an approach for defining interactions on the IWF
interface but is not intended to specify the functionality of the IWF nor
meant to mandate a deployment model.
# 5 Assumptions and architectural requirements
## 5.1 Key management
Interworking requirements for key management for encrypted interworking
include:
a) a mechanism to securely (i.e. authenticity, integrity, confidentiality)
share an LMR E2EE traffic key for a private call sessions between a party in
an MCPTT system and a party in the LMR system;
b) a mechanism to securely convey to group members, the LMR E2EE key or set of
LMR E2EE keys associated with an MC service group or set of MC service groups,
to be used for encryption of interworking group calls spanning the multiple
systems;
c) a mechanism to securely share with temporary group members in MC systems,
the LMR E2EE key(s) associated with a temporary MC service group to be used in
interworking group calls spanning the multiple systems;
d) key management solutions shall not preclude the ability of an IWF to allow
one or more individual Mission Critical Organizations from having sole control
over and sole access to LMR E2EE traffic keys used for the entity\'s media
traffic and users\' key encryption keys (UKEKs or KEKs);
e) key management solutions shall support the ability of the IWF to
decrypt/reencrypt the media traffic for zero or more groups; and,
f) for deployments where Mission Critical Organizations wish to use LMR E2EE
mechanisms when interworking with LMR users:
i) a mechanism to securely provision an MC service client with the user\'s
UKEK or KEK; and,
ii) a mechanism to convey LMR OTAR or OTAK message contents.
## 5.2 Packet format
Each LMR technology defines its own packet format for voice media
transmission. For interworking sessions, there might be cases where LMR
formatted media is required to be transferred between the IWF and LMR aware
MCPTT clients. An example of such a case is where E2EE is used and thus the
IWF is not able to decrypt the media. In such cases, media that is sent over
the IWF-1 interface needs to be routed within MCPTT systems to/from LMR aware
MCPTT clients using methods described in 3GPP TS 23.379 [7].
Requirements for media transmission across the IWF-1 interface include:
a) media transmission to carry the LMR formatted media between the IWF and LMR
aware MCPTT clients; and
b) the MCPTT system, along with the IWF, may choose to encrypt the LMR
formatted media using 3GPP mechanisms.
NOTE: The contents of the LMR formatted media is out of scope of the present
document.
# 6 Involved business relationships
No business relationships have been identified.
# 7 Functional model
## 7.1 General
## 7.2 Functional model description
Figure 7.2‑1 shows the functional model for the application plane for
interworking between MC systems and LMR systems. Functional entities and
interfaces depicted on the right-hand side of the IWF‑x interfaces are defined
in 3GPP TS 23.280 [5], 3GPP TS 23.379 [7], and 3GPP TS 23.282 [6].
Figure 7.2-1: Functional model for application plane for interworking
## 7.3 Functional entities description
### 7.3.1 IWF
The IWF supports most of the functionality of peer MCPTT and MCData systems,
with some differences, as specified in the present document. The IWF supports
any necessary protocol translation and identity mapping between the MC systems
and the IWF. The internal function of the IWF is out of scope of the present
document.
## 7.4 Reference points
### 7.4.1 Reference point IWF‑1 (between the IWF and the MCPTT server)
The IWF‑1 reference point, which exists between the IWF and the MCPTT server,
provides peer to peer interconnection between an LMR system and the MCPTT
system. IWF‑1 supports a subset of MCPTT‑3 as defined in 3GPP TS 23.379 [7],
with some differences, as specified in the present document. The IWF‑1
interface is supported by the same signalling plane protocol(s) as defined for
MCPTT‑3 except as specified in the present document.
### 7.4.2 Reference point IWF‑2 (between the IWF and the MCData server)
The IWF‑2 reference point, which exists between the IWF and the MCData server,
provides SDS interconnection between an LMR system and the MCData system.
IWF‑2 supports a subset of the functionality of MCData‑SDS‑1 and MCData‑SDS‑2,
as defined in 3GPP TS 23.282 [6] with some differences, as specified in the
present document. The IWF‑2 interface is supported by the same signalling
plane protocol(s) as defined for MCData‑3 except as specified in the present
document.
### 7.4.3 Reference point IWF‑3 (between the IWF and the group management
server)
The IWF‑3 reference point, which exists between the IWF and the group
management server, provides group management interconnection between an LMR
system and the MC service system. IWF‑3 is based upon CSC‑16, as defined in
3GPP TS 23.280 [5] with some differences, as specified in the present
document.
# 8 Identities
## 8.1 Identity mapping
The IWF provides centralised support for interworking between an MCPTT or
MCData system and an LMR system. In MCPTT systems, the identity of an LMR user
is provided as an MCPTT ID, and the identity of an LMR group is provided as an
MCPTT group ID, which can be used by the IWF to derive the corresponding
identities used in an LMR system. Similarly, in MCData systems, the identity
of an LMR user is provided as an MCData ID, and the identity of an LMR group
is provided as an MCData group ID, which can be used by the IWF to derive the
corresponding identities used in an LMR system.
Identities provided on IWF-x reference points are described in clause 8 of
3GPP TS 23.280 [5].
The IWF can perform the identity mapping between an MCPTT system or MCData
system and an LMR system during exchange of signalling and media messages.
The assignment of a functional alias that belongs to the MC system to a user
homed in the IWF enables the mapping to corresponding role-based addressing
schemes applicable in the LMR system.
# 9 Application of functional model to deployments
No applications of functional model to deployments have been identified.
# 10 Procedures and information flows
## 10.1 Affiliation
### 10.1.1 Information flows for affiliation
#### 10.1.1.1 General
The following subclauses define information flows for affiliation on the IWF-1
interface. Affiliation related information flows on reference points other
than IWF-1 are defined in 3GPP TS 23.280 [5].
#### 10.1.1.2 IWF group affiliation request
Table 10.1.1.2-1 describes the information flow IWF group affiliation request
between the IWF and an MC service server and between an MC service server and
the IWF.
Table 10.1.1.2-1: IWF group affiliation request
* * *
Information element Status Description MC service ID M The MC service ID of
the originator (LMR user or MC service user) who triggers the MC service group
affiliation request. (see NOTE) MC service group ID list M A list of one or
more MC service group IDs to which the originator intends to affiliate and is
defined in the destination MC service system. MC service type M The type(s) of
service(s) for which the request is intended (e.g. MCData or MCPTT or both)
NOTE: The IWF is configured with an MC service ID for use when the IWF is
affiliating itself to the group on behalf of the LMR system.
* * *
#### 10.1.1.3 IWF group affiliation response
Table 10.1.1.3-1 describes the information flow IWF group affiliation response
between the IWF and an MC service server and between an MC service server and
the IWF.
Table 10.1.1.3-1: IWF group affiliation response
* * *
Information element Status Description MC service ID M The MC service ID of
the originator (LMR user or MC service user) who triggered the MC service
group affiliation request. MC service group ID list M A list of one or more MC
service group IDs to which the originator intends to affiliate and is defined
in the destination MC service system. Affiliation status per MC service group
ID M Indicates the affiliation result for every MC service group ID in the
list.
* * *
#### 10.1.1.4 IWF group de-affiliation request
Table 10.1.1.4-1 describes the information flow IWF group de-affiliation
request between the IWF and an MC service server and between an MC service
server and the IWF.
Table 10.1.1.4-1: IWF group de-affiliation request
* * *
Information element Status Description MC service ID M The MC service ID of
the originator (LMR user or MC service user) who triggers the MC service group
de-affiliation request. (see NOTE) MC service group ID list M A list of one or
more MC service group IDs to which the originator intends to de-affiliate. MC
service type M The type(s) of service(s) for which the request is intended
(e.g. MCData or MCPTT or both) NOTE: The IWF is configured with an MC service
ID for use when the IWF is de-affiliating from the group on behalf of the LMR
system.
* * *
#### 10.1.1.5 IWF group de-affiliation response
Table 10.1.1.5-1 describes the information flow IWF group de-affiliation
response between the IWF and an MC service server and between an MC service
server and the IWF.
Table 10.1.1.5-1: IWF group de-affiliation response
* * *
Information element Status Description MC service ID M The MC service ID of
the originator (LMR user or MC service user) who triggers the MC service group
de-affiliation request. MC service group ID list M A list of one or more MC
service group IDs to which the originator intends to de-affiliate. De-
affiliation status per MC service group ID M Indicates the de-affiliation
result for every MC service group ID in the list.
* * *
### 10.1.2 Affiliation procedures
#### 10.1.2.1 General
When an interworking group is defined in the MCPTT system, the LMR system (via
the IWF) informs the MCPTT system of group affiliations in one of the
following ways:
\- Every group affiliation in the LMR system results in an affiliation sent to
the MCPTT system, which contains the identity (with appropriate translation by
the IWF) of the affiliating group member; or
\- A group affiliation is sent on behalf of the group\'s LMR users (via the
IWF) to the MCPTT system when the first group member affiliates to the
designated group in the LMR system, and a group de-affiliation is sent on
behalf of the group\'s LMR users (via the IWF) to the MCPTT system when the
last group member de-affiliates, and no other group affiliation signalling is
sent.
The first and second options may be used at the same time, such that some
group members may explicitly affiliate while the IWF may affiliate on behalf
of other group members.
In the second option, when the IWF is configured to affiliate on behalf of the
group\'s LMR members then:
a) the group list in the MCPTT system contains the IWF\'s MCPTT ID. This ID is
recognized (through configuration) as having the ability to affiliate on
behalf of the group\'s LMR users associated with this IWF;
b) the IWF affiliates with its MCPTT ID to the group defined in the MCPTT
system;
c) the MCPTT system recognizes the affiliation as being from an IWF on behalf
of the group\'s LMR users;
d) when the IWF has affiliated to the group, the MCPTT system:
i) considers any LMR user associated with the IWF to be affiliated to the
group on which the IWF has affiliated. The IWF\'s users need not be listed
ahead of time in the group list for this group in the MCPTT system;
ii) allows requests such as call setup or floor request, from MCPTT IDs
representing LMR users associated with the IWF for actions on the group to
which the IWF has affiliated;
iii) does not carry out an additional affiliation on behalf of LMR users when
those users make call requests, and therefore does not send additional
messages to those users (e.g. release messages to both the IWF affiliated
identity and the LMR user identity performing the action), via the IWF, during
call processing;
iv) recognizes which LMR users are associated with the IWF because their MCPTT
IDs belong to the same system as the IWF; and,
v) uses special rules for the IWF for limits such as \"Limitation of number of
affiliations per user (N2)\".
e) requests from LMR users to the MCPTT system are identified with their
individual MCPTT IDs (as translated by the IWF):
i) a user in the LMR system can affiliate on its own (via the IWF) as long as
the user is a group member (i.e. in the group list), even if the IWF has
affiliated to the group.
f) the IWF may make requests on behalf of a group\'s LMR users using the IWF
MCPTT ID like a normal group member including, for example, group join
requests for groups using the chat model;
g) the IWF is not allowed to affiliate to a group that is not configured with
the IWF\'s MCPTT ID in the group member list; and,
h) if the IWF has not affiliated to an MCPTT group, then call requests to this
group from LMR users on the system associated with the IWF, can only be
accepted if the LMR user\'s MCPTT ID is in the group list, and has already
affiliated.
#### 10.1.2.2 Group affiliation to a group defined in the MC system
The LMR system may affiliate its group members to an interworking group
defined in the MC system via the IWF.
For group regroup, the affiliated group members are automatically affiliated
to the temporary group.
The signalling procedure of interworking group affiliation is described in
figure 10.1.2.2-1.
Pre-conditions:
1\. The group to be affiliated to is defined in the MC system.
2\. The IWF is connected to and is authorized to interwork with the MC system.
3\. The interworking group information is available at the IWF.
4\. The mapping relationship of group and user identities between MC system
and the LMR system has been configured at the IWF.
NOTE 1: For all the signalling messages passing through the IWF between the MC
system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.1.2.2-1: Group affiliation to a group defined in the MC system
1\. The IWF sends an IWF group affiliation request to the MC service server on
behalf of the LMR system.
2a. The MC service server checks if the group policy is locally cached. If the
group policy is not locally cached on the MC service server then the MC
service server requests the group policy from the group management server.
2b. The MC service server receives the group policy from the group management
server.
3\. Based on the group policy, the MC service server checks if the MC service
group(s) is not disabled and if the user identified by the MCPTT ID supplied
by the IWF is authorised to affiliate to the requested MC service group(s).
4\. Based on the group policy and user subscription, the MC service server
affiliates the IWF to the group. If a separate affiliation for each LMR user
is expected, the status of the affiliating user is stored by the MC service
server as the status associated with an MC service ID provided by the IWF that
corresponds to the identity of that LMR user. If a separate affiliation for
each LMR user is not expected, an affiliation status for the group using the
MC service ID provided by the IWF is stored.
5\. The MCPTT server sends the group affiliation status update message to the
group management server, the group management server stores and updates the
group affiliation status.
6\. The MC service server returns an IWF group affiliation response to the
IWF.
NOTE 2: How the LMR user(s) affiliates to a group is outside the scope of the
present document.
#### 10.1.2.3 Group de-affiliation from a group defined in the MC system
The signalling procedure of interworking group de-affiliation from a group
defined in the MC system is described in figure 10.1.2.3-1.
The LMR system manages the individual de-affiliation requests from the LMR
users. The LMR system can de-affiliate its group members from the interworking
group via the IWF.
Pre-conditions:
1\. The mapping relationship of group and user identities between the MC
system and the LMR system has been configured at the IWF.
2\. The affiliation procedure described in subclause 10.1.2.2 was previously
performed.
NOTE 1: For all the signalling messages passing through the IWF between the MC
system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.1.2.3-1: Group de-affiliation from group defined in the MC system
1\. The IWF sends an IWF group de-affiliation request to the MC service server
on behalf of the LMR system.
2\. If a separate de-affiliation from each LMR user is expected and based on
the group policy and user subscription, the MC service server may de-affiliate
the LMR group member from the group. Further, the MC service server may store
the affiliation status of the user(s) for the requested MC service group(s).
If a separate de-affiliation from each LMR user is not expected, the de-
affiliation signalling de-affiliates the IWF and therefore the entire LMR
system from the group.
3\. The MC service server sends the group de-affiliation status update message
to the group management server, the group management server stores and updates
the group affiliation status.
4\. The MC service server returns an IWF group de-affiliation response to the
IWF.
NOTE 2: How the LMR user(s) de-affiliate from a group is outside the scope of
the present document.
#### 10.1.2.4 Group affiliation to group defined in the LMR system
The MC service system may affiliate its group members to an interworking group
defined in the LMR system via the IWF.
The signalling procedure of group affiliation via the IWF is described in
figure 10.1.2.4‑1.
Pre-conditions:
1\. The group to be affiliated to is defined in the LMR system.
2\. The IWF is connected to and is authorized to work with the MC system.
3\. The mapping relationship of group and user identities between the MC
system and the LMR system has been configured at the IWF.
NOTE 1: For all signalling messages passing through the IWF between the MC
system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.1.2.4-1: Group affiliation to group defined in the LMR system
> 1\. The MC service client sends a MC service group affiliation request,
> including the MC service group ID(s), to the MC service server.
2\. The MC service server checks if the MC service group ID(s) is an
interworking group defined in the LMR system.
3\. The MC service server sends an IWF group affiliation request to the IWF.
NOTE 2: The IWF can forward the request to the LMR system that could check
whether the MC service client is authorized to affiliate to this interworking
group.
NOTE 3: The IWF can reject the affiliation if the MC service group ID is
either unknown to the IWF or not mapped to an LMR group identity in the IWF
configuration.
4\. The IWF returns an IWF group affiliation response to the MC service
server, informing the successful affiliation to the LMR group.
5\. The MC service server stores the group affiliation status of the MC
service client for the requested interworking group.
6\. The MC service server sends an MC service group affiliation response to
the MC service client.
NOTE 4: How the affiliation is conducted on the LMR system is outside the
scope of the present document.
#### 10.1.2.5 Group de-affiliation from a group defined in the LMR system
The signalling procedure of interworking group de-affiliation from a group
defined in the LMR system is described in figure 10.1.2.5-1.
The MC system manages the individual de-affiliation requests from the MC
service users. The MC service system may de-affiliate its group members from
the interworking group via the IWF.
Pre-conditions:
1\. The mapping relationship of group and user identities between the MC
service system and the LMR system has been configured at the IWF.
2\. The affiliation procedure described in subclause 10.1.2.4 was previously
performed.
NOTE: For all the signalling messages passing through the IWF between the MC
system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.1.2.5-1: Group de-affiliation from a group defined in the LMR system
1\. The MC service client of the MC service user sends an MC service group de-
affiliation request to the MC service server. The MC service client shall
provide the initiating MC service ID and the MC service group ID(s) being de-
affiliated from.
2\. Based on the user subscription and stored group policy, the MC service
server checks if the user of the MC service client is affiliated to the
requested MC service group(s). The MC service server checks if the MC service
group(s) is an interworking group.
3a. If the MC service group(s) is an interworking group, the MC service server
sends an IWF group de-affiliation request to the IWF.
3b. The IWF returns an IWF group de-affiliation response to the MC service
server.
4\. If the user of the MC service client is authorized to de-affiliate from
the requested MC service group(s), the MC service server removes the
affiliation status of the user for the requested MC service group(s).
5\. The MC service server returns an MC service group de-affiliation response
to the MC service client.
## 10.2 Group management
### 10.2.1 Information flows for group management
#### 10.2.1.1 General
The following subclauses define information flows for group management on the
IWF-1 interface. Group management related information flows on reference
points other than IWF-1 are defined in 3GPP TS 23.280 [5].
#### 10.2.1.2 IWF group regroup teardown notification
Table 10.2.1.2-1 describes the information flow IWF group regroup teardown
notification between the group management server and the IWF or between the
IWF and the group management server.
Table 10.2.1.2-1: IWF group regroup teardown notification
* * *
Information element Status Description MC service group ID M MC service group
ID of the temporary group which is torn down
* * *
#### 10.2.1.3 IWF group regroup teardown notification response
Table 10.2.1.3-1 describes the information flow IWF group regroup teardown
notification response between the group management server and the IWF or
between the IWF and the group management server.
Table 10.2.1.3-1: IWF group regroup teardown notification response
* * *
Information element Status Description MC service group ID M MC service group
ID of the temporary group which was torn down Result M Indicates success or
failure of the notification
* * *
#### 10.2.1.4 IWF group regroup request
Table 10.2.1.4-1 describes the information flow IWF group regroup request
between the group management server and the IWF or between the IWF and the
group management server.
Table 10.2.1.4-1: IWF group regroup request
* * *
Information element Status Description MC service group ID list M List of
constituent MC service group IDs
* * *
#### 10.2.1.5 IWF group regroup response
Table 10.2.1.5-1 describes the information flow IWF group regroup response
between the group management server and the IWF or between the IWF and the
group management server.
Table 10.2.1.5-1: IWF group regroup response
* * *
Information element Status Description MC service group ID O (see NOTE) MC
service group ID of the temporary group MC service group ID list M List of
constituent MC service group IDs. Result M Indicates whether the IWF group
regroup was accepted or rejected. NOTE: Shall be present if the Result
information element indicates that the group regroup operation is successful.
Otherwise MC service group ID shall not be present.
* * *
#### 10.2.1.6 IWF group regroup notification
Table 10.2.1.6-1 describes the information flow IWF group regroup notification
between the group management server and the IWF or between the IWF and the
group management server.
Table 10.2.1.6-1: IWF group regroup notification
* * *
Information element Status Description MC service group ID list M List of
constituent MC service group IDs MC service group ID M MC service group ID of
the temporary group Priority level O Required priority level for the temporary
group Security level (see NOTE) O Required security level for the temporary
group NOTE: Security level refers to the configuration of media and floor
control protection parameters as listed in 3GPP TS 23.280 [5]
* * *
#### 10.2.1.7 IWF group regroup notification response
Table 10.2.1.7-1 describes the information flow IWF group regroup notification
response between the group management server and the IWF or between the IWF
and the group management server.
Table 10.2.1.7-1: IWF group regroup notification response
* * *
Information element Status Description MC service group ID list M List of
constituent MC service group IDs MC service group ID M MC service group ID of
the temporary group Priority level M Required priority level for the temporary
group Security level M Required security level for the temporary group
* * *
#### 10.2.1.8 IWF group information request
Table 10.2.1.8-1 describes the IWF group information request from the IWF to
the group management server or from the group management server to the IWF.
Table 10.2.1.8-1: IWF group information request
* * *
Information element Status Description MC service group ID M The identity of
the MC service group.
* * *
#### 10.2.1.9 IWF group information response
Table 10.2.1.9-1 describes the IWF group information response from the group
management server to the IWF or the IWF to the group management server.
Table 10.2.1.9-1: IWF group information response
+-------------------------+----------------+-------------------------+ | Information element | Status | Description | +-------------------------+----------------+-------------------------+ | MC service group ID | M | The identity of the MC | | | | service group. | +-------------------------+----------------+-------------------------+ | MC service group | O (see NOTE 1) | The group information | | provisioning | | retrieved from the | | information | | group management server | | | | or from the IWF in the | | | | case where the IWF is | | | | performing the | | | | provision. | +-------------------------+----------------+-------------------------+ | Result | O (see NOTE 2) | Indicates reason for | | | | failure to provide MC | | | | service group | | | | configuration | | | | information | +-------------------------+----------------+-------------------------+ | NOTE 1: Shall be | | | | present if the request | | | | can be fulfilled. | | | | | | | | NOTE 2: Shall be | | | | present if the request | | | | cannot be fulfilled. | | | +-------------------------+----------------+-------------------------+
#### 10.2.1.10 IWF group information provision request
Table 10.2.1.10-1 describes the IWF group information provision request from
the group management server to the IWF or the IWF to the group management
server.
Table 10.2.1.10-1: IWF group information provision request
* * *
Information element Status Description MC service group ID M The identity of
the MC service group. MCPTT group configuration information M The group
information retrieved from the group management server or from the IWF in the
case where the group is defined in the IWF.
* * *
#### 10.2.1.11 IWF group information provision response
Table 10.2.1.11-1 describes the IWF group information provision response from
the IWF to the group management server or from the group management server to
the IWF.
Table 10.2.1.11-1: IWF group information provision response
* * *
Information element Status Description MC service group ID M The identity of
the MC service group. Result M Indicates success or failure of reception,
modification and storage of MC service group configuration information
* * *
#### 10.2.1.12 IWF group information subscribe request
Table 10.2.1.12-1 describes the information flow IWF group information
subscribe request from the IWF to the group management server in the MC system
for cases where the MC system is the primary system of the group and from the
group management server in the MC system to the IWF for cases there the IWF is
the primary system of the group.
Table 10.2.1.12-1: IWF group information subscribe request
* * *
Information element Status Description MC service group ID M MC service group
ID of the group MC services requested O Service(s) for which group
configuration is requested; one or more of MCPTT, MCData
* * *
#### 10.2.1.13 IWF group information subscribe response
Table 10.2.1.13-1 describes the information flow IWF group information
subscribe response from the group management server in the MC system to the
IWF for cases where the MC system is the primary system of the group and from
the IWF to the group management server in the MC system for cases where the
IWF is the primary system of the group.
Table 10.2.1.13-1: IWF group information subscribe response
* * *
Information element Status Description MC service group ID M MC service group
ID of the group Result M Indicates success or failure of the subscribe request
* * *
#### 10.2.1.14 IWF group information notify request
Table 10.2.1.14-1 describes the information flow IWF group information notify
request from the group management server in the MC system to the IWF for cases
where the MC system is the primary system of the group and from the IWF to the
group management server in the MC system for cases where the IWF is the
primary system of the group.
Table 10.2.1.14-1: IWF group information notify request
* * *
Information element Status Description MC service group ID M MC service group
ID of the group MC service group information reference (see NOTE) O Reference
to information stored relating to the MC service group Group related key
material (see NOTE) O Key material for use with the MC service group NOTE: At
least one of these information elements shall be present.
* * *
#### 10.2.1.15 IWF group information notify response
Table 10.2.1.15-1 describes the information flow IWF group information notify
response from the IWF to the group management server in the MC system for
cases where the MC system is the primary system of the group and from the
group management server in the MC system to the IWF for cases there the IWF is
the primary system of the group.
Table 10.2.1.15-1: IWF group information notify response
* * *
Information element Status Description MC service group ID M MC service group
ID of the group Result M Indicates success or failure of the notification
request
* * *
### 10.2.2 Group regrouping
#### 10.2.2.1 General
The procedures in 3GPP TS 23.280 [5] are followed, but with changes required
for interworking. The IWF will behave on the interface as if it is a peer MC
service server with a peer group management client and peer group management
server.
Exceptions to the 3GPP TS 23.280 [5] procedures are detailed in the subclauses
below.
#### 10.2.2.2 MC system initiates the group regroup
The MC system can initiate a group regroup that includes groups defined at the
IWF. The IWF is informed and may reject the regroup if conditions do not allow
it to support the regroup. This is described in figure 10.2.2.2-1.
Pre-conditions:
1\. The group management client has retrieved the group configurations of the
groups to be regrouped.
2\. At least one MC service group has been defined in the MC system.
3\. At least one MC service group has been defined in the IWF.
Figure 10.2.2.2-1: Group regrouping to an IWF
1\. The group management client of the MC service user (e.g. dispatcher)
requests group regroup operation to the group management server (which is the
group management server of one of the MC service groups to be regrouped). The
identities of the groups being combined shall be included in this message. The
group management client may indicate the security level required for the
temporary group. The group management client may indicate the priority level
required for the temporary group.
2\. The group management server checks whether group regroup operation is
performed by an authorised MC service user, based on group policy. The group
management server checks whether the group is a temporary group. If the group
is a temporary group, then the group regrouping will be rejected, otherwise
the group regrouping can proceed.
3\. The group management server forwards the IWF group regroup request to the
IWF with the information about the IWF\'s groups.
4\. The IWF provides an IWF group regroup response. Due to security aspects
concerning sharing information among different MC systems, the IWF does not
share the users\' information of the groups under its management to the group
management server. The IWF may reject the IWF group regroup response. (e.g. if
one of its constituent groups is in the emergency state or is already in a
regroup, if the IWF does not support temporary groups or the IWF does not
support group regrouping)
5\. The group management server creates and stores the information of the
temporary group, including the temporary MC service group ID, off-network
information, and the MC service IDs of the groups being combined, the priority
level of the temporary group, and the security level of the temporary group.
If the authorised MC service user does not specify the security level and the
priority level, the group management server shall set the lower security level
and the higher priority of the constituent groups.
6\. The group management server notifies the IWF about its group regroup
operation.
NOTE: How the IWF uses the MC service group ID that identifies the temporary
group is outside the scope of the present document.
7\. The IWF acknowledges the group management server.
8\. The group management server notifies the MC service server of the
temporary group creation with the information of the constituent groups.
9\. The MC service server acknowledges the notification from the group
management server.
10\. The group management server notifies the MC service group members of the
constituent MC service groups of the group management server, possibly with an
indication of lower security level.
11\. The group management server provides a group regroup response to the
group management client of the authorised MC service user (e.g. dispatcher).
#### 10.2.2.3 IWF initiates the group regroup
The procedure in 3GPP TS 23.280 [5] is followed, except for steps 1 and 2. The
IWF will behave on the interface as if it is a peer MC service server with a
peer group management server. This is described in figure 10.2.2.3-1.
Pre-conditions:
1\. At least one MC service group has been defined in the MC system.
2\. At least one MC service group has been defined in the IWF.
Figure 10.2.2.3-1: Group regrouping from an IWF
1\. The IWF sends an IWF group regroup request to the group management server.
2\. The group management server checks whether the group can be included in a
temporary group.
3\. The group management server provides an IWF group regroup response.
NOTE: Due to security aspects concerning sharing information among different
systems, the group management server does not share the users\' information of
the groups under its management to the IWF.
4\. The IWF notifies the group management server regarding the temporary group
creation with information of the constituent groups.
5\. The group management server notifies the MC service server regarding the
temporary group creation with the information of the constituent groups.
6\. The MC service server acknowledges the notification from the group
management server. The MC service server may reject the IWF group regroup,
e.g. if one of its constituent groups is already in a regroup.
7\. The group management server acknowledges the notification from the IWF.
8\. The group management server notifies the MC service group members of the
constituent MC service groups of the group management server, possibly with an
indication of a lower security level.
#### 10.2.2.4 Ownership of the group regroup
The group management server that performs the group regroup operation owns the
temporary group created by the regroup, as implied in 3GPP TS 23.280 [5].
#### 10.2.2.5 Simultaneous group regroup requests from each side of the IWF-1
interface
To prevent routing issues and complexity that could result from regrouping the
same users from both sides of the interface, the following rules can be
applied:
\- If group regrouping signalling using temporary groups is used on the MC
system, the IWF must prevent the regroup signalling from propagating to the
LMR system if the LMR system does not support regrouping;
\- the IWF must handle the translation between temporary group identities on
the MC system and the original interworking group identities used on the LMR
system; and
\- the regrouping rules in subclause 10.2.4.4 of 3GPP TS 23.280 [5] also
apply.
#### 10.2.2.6 Resolution of vocoder and encryption mode for the group regroup
If one of the LMR groups to be included in a group regroup requires the use of
LMR E2EE the preferred voice codecs for an MCPTT temporary group should be LMR
codecs. If any of the mission critical users to be included in this MCPTT
temporary group do not support LMR E2EE or the preferred LMR codecs, voice
calls using LMR E2EE will fail for those users.
NOTE 1: How the MC system determines that the temporary group needs to support
LMR E2EE is outside the scope of the present document.
NOTE 2: How the MC system determines that the temporary group needs to support
an LMR codec is outside the scope of the present document.
### 10.2.3 Group configuration for interworking
#### 10.2.3.1 Overview
The procedures in the following subclauses describe the process for sharing
group configuration from an MC system to an IWF where the IWF needs to make
use of the MC service group and from an IWF to an MC system where the MC
system\'s clients need to make use of the group. The procedures in this
subclause are based upon subclause 10.2.7 in 3GPP TS 23.280 [5].
#### 10.2.3.2 MC system provides group configuration to the IWF
Figure 10.2.3.2-1 below illustrates the case where the MC system provides the
group configuration to the IWF, e.g. due to an action by an administrator or
because the primary MC system of some of the MC service group members is the
IWF.
Pre-conditions:
1\. The MC service group is defined in the MC system.
2\. One or more LMR users are members of the group.
3\. The MC system of the MC service group has been configured with addressing
information for the group management function in the IWF.
4\. The MC system of the MC service group is authorized to provide group
configuration information to the IWF.
NOTE: The MC system of the MC service group could be configured with an
address of the IWF which is a proxy address.
Figure 10.2.3.2-1: MC system provides group configuration to the IWF
1\. The group management server in the MC system of the MC service group
provides the configuration information related to the MC service group to the
IWF.
2\. The IWF responds to the group management server of the MC system of the MC
service group that the configuration has been received and stored correctly.
#### 10.2.3.3 IWF requests group configuration from the MC system
Figure 10.2.3.3-1 below illustrates the case where the IWF requests the group
configuration from the MC system, for example because a user on the IWF is a
member of the group.
Pre-conditions:
1\. The MC service group is defined in the MC system.
2\. One or more LMR users are members of the group.
3\. The IWF does not have the configuration for the MC service group stored.
Figure 10.2.3.3-1: Partner MC system requests group configuration from primary
MC system
1\. The IWF requests the group configuration from the group management server
in the primary MC system of the MC service group.
2\. The group management server in the MC system of the MC service group
provides the requested group configuration information.
#### 10.2.3.4 IWF provides group configuration to the MC system
Figure 10.2.3.4-1 below illustrates the case where the IWF provides the group
configuration to the MC system, e.g. due to an action by an administrator or
because some of the IWF\'s MC service group members are homed on the MC
system.
Pre-conditions:
1\. The group is defined in the IWF.
2\. One or more MC service users are members of the group.
NOTE: The group management server within the MC system is responsible for
providing group configuration information to group members for whom the MC
system is their serving MC system.
Figure 10.2.3.4-1: MC system provides group configuration to the IWF
1\. The IWF provides the configuration information related to the group to the
group management server in the MC system.
2\. The group management server in the MC system responds to the IWF that the
configuration has been received and stored correctly.
#### 10.2.3.5 MC system requests group configuration from the IWF
Figure 10.2.3.5-1 below illustrates the case where the MC system requests the
group configuration from the IWF, for example because an MC service user
receiving service in the MC system has the group configured in the user
profile.
Pre-conditions:
1\. The MC service group is defined in the IWF.
2\. One or more MC service users are members of the group.
3\. The group management server in the MC system does not have the
configuration for the MC service group stored.
4\. The MC system has been configured with addressing information for the
group management function in the IWF.
NOTE: The group management server within the MC system is responsible for
providing group configuration information to MC service group members for whom
the MC system is their serving MC system.
Figure 10.2.3.5-1: Partner MC system requests group configuration from primary
MC system
1\. The MC system requests the group configuration from the group management
function in the IWF.
2\. The IWF provides the requested group configuration information.
#### 10.2.3.6 IWF subscribes to group configuration
The procedure for subscription from IWF for group configuration information to
the group management server in the primary MC system of the MC service group
is shown in figure 10.2.3.6-1.
Pre-conditions:
1\. The MC service group is defined in its MC system.
2\. One or more group members are defined in the LMR system.
3\. The IWF has received group information from the GMS in the primary MC
system of the MC service group.
Figure 10.2.3.6-1: Subscription from the IWF to the MC system for MC service
group configuration
1\. The IWF subscribes to the group configuration information stored in the
group management server in the primary MC system of the MC service group.
2\. The group management server in the primary MC system of the MC service
group sends an IWF group information subscribe response to IWF indicating
success or failure of the request.
#### 10.2.3.7 MC system notifies group configuration
The procedure for notification of group configuration information from the
group management server in the primary MC system of the MC service group to
the IWF is shown in figure 10.2.3.7-1.
Pre-conditions:
1\. The IWF has subscribed to the group configuration information for the MC
service group in the group management server in the primary MC system of the
MC service group.
2\. The group management server in the primary MC system of the MC service
group has received and stored new group configuration information for the MC
service group.
Figure 10.2.3.7-1: Notification of group configuration information to the IWF
1\. The group management server in the primary MC system of the MC service
group sends an IWF group information notify request to the IWF.
2\. The IWF sends an IWF group information notify response to the group
management server in the primary MC system of the MC service group indicating
the success or failure of the notification.
#### 10.2.3.8 MC system subscribes to group configuration
The procedure for subscription by the group management server in the MC system
to the IWF for group configuration information is shown in figure 10.2.3.8-1.
Pre-conditions:
1\. The group is defined in the LMR system.
2\. One or more group members are defined in the MC system.
3\. The group management server in the MC system has received group
information from the IWF.
Figure 10.2.3.8-1: Subscription from the MC system to the IWF for MC service
group configuration
1\. The group management server of the MC system subscribes to the group
configuration information stored in the IWF.
2\. The IWF provides an IWF group information subscribe response to group
management server of the MC system indicating success or failure of the
request.
#### 10.2.3.9 IWF notifies group configuration
The procedure for notification of group information from the IWF to the group
management server in the MC system is shown in figure 10.2.3.9-1.
Pre-conditions:
1\. The group management server of the MC system has subscribed to the group
configuration information for the group in the IWF.
2\. The IWF has new information for the group.
Figure 10.2.3.9-1: Notification of group configuration information to partner
MC system of MC service group
1\. The IWF sends an IWF group information notify request to the group
management server in the MC system.
2\. The group management server in the MC system sends an IWF notify group
information notify response to the IWF indicating the success or failure of
the notification.
## 10.3 Group call
### 10.3.1 General
The following subclauses define information flows and signaling procedures for
group calls and broadcast group calls.
Where the group is defined in the MCPTT system and where the IWF has
affiliated to an MCPTT group with a single affiliation on behalf of all LMR
group members, only a single IWF group call request / IWF group call release
request message is sent to the IWF at the commencement / release of a group
call. Where the group is defined in the MCPTT system and where the IWF has
passed through individual affiliations for each group member in the LMR
system, the MCPTT system shall send individual IWF group call request / IWF
group call release request messages to the IWF for all affiliated group
members in the LMR system in accordance with primary and partner MCPTT system
behaviour. In both cases, the distribution of the messages to group members in
the LMR system is out of scope of the present document.
Where the group is defined in the LMR system, the IWF shall send individual
IWF group call request / IWF group call release request messages to the IWF
for all affiliated MCPTT group members in accordance with primary and partner
MCPTT system behaviour.
### 10.3.2 Information flows for group call over interworking group
#### 10.3.2.1 General
The following subclauses define information flows for group calls on the IWF-1
interface. Group call related information flows on reference points other than
IWF-1 are defined in 3GPP TS 23.379 [7].
#### 10.3.2.2 IWF group call request
Table 10.3.2.2-1 describes the information flow IWF group call request from
the IWF to the MCPTT server and from the MCPTT server to the IWF.
Table 10.3.2.2-1: IWF group call request information elements
+-----------------------------+--------+-----------------------------+ | Information Element | Status | Description | +-----------------------------+--------+-----------------------------+ | MCPTT ID | M | The MCPTT ID of the calling | | | | party | | (see NOTE 1) | | | +-----------------------------+--------+-----------------------------+ | MCPTT group ID | M | The MCPTT group ID of the | | | | interworking group on which | | | | the call is initiated | +-----------------------------+--------+-----------------------------+ | SDP offer | M | Media parameters of MCPTT | | | | server | +-----------------------------+--------+-----------------------------+ | Implicit floor request\ | O | Indicates that the | | (see NOTE 2) | | originator requests the | | | | floor. | +-----------------------------+--------+-----------------------------+ | Broadcast indicator | O | Indicates that the group | | | | call request is for a | | | | broadcast group call | +-----------------------------+--------+-----------------------------+ | Location | O | Location of the calling | | | | party | +-----------------------------+--------+-----------------------------+ | NOTE 1: If the LMR system | | | | does not provide the | | | | calling party identity when | | | | the group call is | | | | originated from the LMR | | | | system, then this | | | | information element may be | | | | set to a MCPTT ID reserved | | | | for LMR user at the IWF. | | | | | | | | NOTE 2: This element shall | | | | be included only when the | | | | originating client requests | | | | the floor. | | | +-----------------------------+--------+-----------------------------+
#### 10.3.2.3 IWF group call response (IWF -- MCPTT server)
Table 10.3.2.3-1 describes the information flow IWF group call response from
the MCPTT server to the IWF and from the IWF to MCPTT server.
Table 10.3.2.3-1: IWF group call response information elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the target
MCPTT group member MCPTT group ID M The MCPTT group ID of the group on which
the call is requested SDP answer M Media parameters selected
* * *
#### 10.3.2.4 IWF Group-broadcast group call setup request
Table 10.3.2.4-1 describes the information flow IWF group-broadcast group call
setup request from the MCPTT server to the IWF and from the IWF to the MCPTT
server.
Table 10.3.2.4-1: IWF Group-broadcast group call setup request information
elements
+-----------------------------+--------+-----------------------------+ | Information Element | Status | Description | +-----------------------------+--------+-----------------------------+ | MCPTT ID | M | The MCPTT ID of the calling | | | | party | | (see NOTE 1) | | | +-----------------------------+--------+-----------------------------+ | MCPTT group ID | M | The MCPTT group ID of the | | | | group on which the call is | | | | requested | +-----------------------------+--------+-----------------------------+ | SDP offer | M | Media parameters of MCPTT | | | | clients | +-----------------------------+--------+-----------------------------+ | Implicit floor request | O | Indicates that the | | | | originating client requests | | (see NOTE 2) | | the floor | +-----------------------------+--------+-----------------------------+ | Location | O | Location of the calling | | | | party | +-----------------------------+--------+-----------------------------+ | NOTE 1: If the LMR system | | | | does not provide the | | | | calling party identity when | | | | the group-broadcast group | | | | call setup request is | | | | originated from the LMR | | | | system, then this | | | | information element may be | | | | set to a MCPTT ID reserved | | | | for the LMR user at the | | | | IWF. | | | | | | | | NOTE 2: This element shall | | | | be included only when the | | | | originating client requests | | | | the floor. | | | +-----------------------------+--------+-----------------------------+
#### 10.3.2.5 IWF Group-broadcast group call setup response
Table 10.3.2.5-1 describes the information flow IWF group-broadcast group call
setup response from the IWF to the MCPTT server and from the MCPTT server to
the IWF.
Table 10.3.2.5-1: IWF Group-broadcast group call setup response information
elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the calling
party MCPTT group ID M The MCPTT group ID of the group on which the call is
requested SDP answer M Media parameters selected
* * *
#### 10.3.2.6 IWF Group-broadcast group call release request
Table 10.3.2.6-1 describes the information flow IWF group-broadcast group call
release request from the MCPTT server to the IWF and from the IWF to the MCPTT
server.
Table 10.3.2.6-1: IWF Group-broadcast group call release request information
elements
* * *
Information Element Status Description MCPTT ID M (see NOTE) The MCPTT ID of
the MCPTT group member MCPTT group ID M The MCPTT group ID of the group on
which the call is released NOTE: If the LMR system does not provide the
calling party identity when the group-broadcast group call release request is
originated from the LMR system, then this information element may be set to a
MCPTT ID reserved for the LMR user at the IWF.
* * *
#### 10.3.2.7 IWF group-broadcast group call release response
Table 10.3.2.7-1 describes the information flow IWF group-broadcast group call
release request from the IWF to the MCPTT server and from the MCPTT server to
the IWF.
Table 10.3.2.7-1: IWF Group-broadcast group call release response information
elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the target
MCPTT group member MCPTT group ID M The MCPTT group ID of the group on which
the call is released
* * *
#### 10.3.2.8 IWF group join request
Table 10.3.2.8-1 describes the information flow IWF group join request from
the IWF to the MCPTT server and from the MCPTT server to the IWF.
Table 10.3.2.8-1: IWF group join request information elements
+-----------------------------+--------+-----------------------------+ | Information Element | Status | Description | +-----------------------------+--------+-----------------------------+ | MCPTT ID | M | The MCPTT ID of the | | | | originator of the request.\ | | | | (see NOTE 1) | +-----------------------------+--------+-----------------------------+ | MCPTT group ID | M | The MCPTT group ID of the | | | | group to which the group | | | | communication is requested | +-----------------------------+--------+-----------------------------+ | SDP offer | M | Media parameters of | | | | originator | +-----------------------------+--------+-----------------------------+ | Implicit floor request\ | O | Indicates that the | | (see NOTE 2) | | originating client requests | | | | the floor. | +-----------------------------+--------+-----------------------------+ | NOTE 1: The IWF is | | | | configured with an MCPTT ID | | | | for use when the IWF is | | | | affiliating itself to the | | | | group on behalf of the LMR | | | | system. | | | | | | | | NOTE 2: This element is | | | | included only when the | | | | originating client requests | | | | the floor. | | | +-----------------------------+--------+-----------------------------+
#### 10.3.2.9 IWF group join response
Table 10.3.2.9-1 describes the information flow group join response from the
MCPTT server to the IWF and from the IWF to the MCPTT server.
Table 10.3.2.9-1: IWF group join response information elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the
originator of the request. (see NOTE) MCPTT group ID M The MCPTT group ID of
the group to which the group communication is requested SDP answer M Media
parameters selected NOTE: The IWF is configured with an MCPTT ID for use when
the IWF is affiliating itself to the group on behalf of the LMR system.
* * *
#### 10.3.2.10 IWF group call leave request
Table 10.3.2.10-1 describes the information flow IWF group call leave request
from the MCPTT server to the IWF and from the IWF to the MCPTT server.
Table 10.3.2.10-1: IWF group call leave request information elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the MCPTT
group member MCPTT group ID M The MCPTT group ID of the group from which the
user is leaving
* * *
#### 10.3.2.11 IWF group call leave response
Table 10.3.2.11-1 describes the information flow IWF group call leave response
from the IWF to the MCPTT server and from the MCPTT server to the IWF.
Table 10.3.2.11-1: IWF group call leave response information elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the MCPTT
group member MCPTT group ID M The MCPTT group ID of the group from which the
user is leaving
* * *
#### 10.3.2.12 IWF group call release request
Table 10.3.2.12-1 describes the information flow IWF group call release
request from the IWF to the MCPTT server and from the MCPTT server to the IWF.
Table 10.3.2.12-1: IWF group call release request information elements
* * *
Information element Status Description MCPTT ID (NOTE) O The MCPTT ID of the
initiating MCPTT group member MCPTT group ID M The MCPTT group ID of the group
on which the call is released Release reason O The reason why the call is
released NOTE: This IE is not included if the group call release is initiated
by the server (e.g. due to timeout)
* * *
#### 10.3.2.13 IWF group call release response
Table 10.3.2.13-1 describes the information flow IWF group call release
response from the IWF to the MCPTT server and from the MCPTT server to the
IWF.
Table 10.3.2.13-1: IWF group call release response information elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the target
MCPTT group member MCPTT group ID M The MCPTT group ID of the group on which
the call is released.
* * *
#### 10.3.2.14 IWF pre-configured regroup request
Table 10.3.2.14-1 describes the information flow IWF pre-configured regroup
request from the IWF to the MCPTT server and from the MCPTT server to the IWF.
Table 10.3.2.14-1 IWF pre-configured regroup request information elements
+---------------------------+------------+---------------------------+ | Information Element | Status | Description | +---------------------------+------------+---------------------------+ | MCPTT ID | M | The MCPTT ID of the | | | | requester | +---------------------------+------------+---------------------------+ | MCPTT group ID | M | MCPTT group ID of the | | | | regroup group | +---------------------------+------------+---------------------------+ | MCPTT group ID | M | MCPTT group ID of the | | | | MCPTT group from which | | | | configuration is to be | | | | taken | +---------------------------+------------+---------------------------+ | MCPTT group ID list | O | List of MCPTT groups to | | | | be regrouped into the | | | (see NOTE) | pre-configured regroup | | | | group | +---------------------------+------------+---------------------------+ | MCPTT ID list | O | List of MCPTT IDs to be | | | | regrouped into the | | | (see NOTE) | pre-configured user | | | | regroup group | +---------------------------+------------+---------------------------+ | NOTE: One and only one of | | | | these shall be present. | | | +---------------------------+------------+---------------------------+
#### 10.3.2.15 IWF pre-configured regroup response
Table 10.3.2.15-1 describes the information flow IWF pre-configured regroup
response from IWF to the MCPTT server and from the MCPTT server to the IWF.
Table 10.3.2.15-1 IWF pre-configured regroup response information elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the
requester of the regrouping operation MCPTT group ID M MCPTT group ID of the
regroup group Result M Result of the regrouping operation
* * *
#### 10.3.2.16 IWF pre-configured regroup cancel request
Table 10.3.2.16-1 describes the information flow pre-configured regroup cancel
request from the IWF to the MCPTT server and from the MCPTT server to the IWF.
Table 10.3.2.16-1 IWF pre-configured regroup cancel request information
elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the
requester MCPTT group ID M MCPTT group ID of the regroup group
* * *
#### 10.3.2.17 IWF pre-configured regroup cancel response
Table 10.3.2.17-1 describes the information flow IWF pre-configured regroup
cancel response from the IWF to the MCPTT server and from the MCPTT server to
the IWF.
Table 10.3.2.17-1 IWF pre-configured regroup cancel response information
elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the
requester of the regroup removal MCPTT group ID M MCPTT group ID of the
regroup group Result M Result of the regroup removal operation
* * *
#### 10.3.2.18 IWF pre-configured regroup reject (IWF -- MCPTT server, MCPTT
server - IWF)
Table 10.3.2.18-1 describes the information flow IWF pre-configured regroup
reject from the IWF to the MCPTT server and from the MCPTT server to the IWF.
Table 10.3.2.18-1 IWF pre-configured regroup reject information elements
* * *
Information Element Status Description MCPTT group ID M MCPTT group ID of the
regroup group Reject reason M Reason for rejecting the regrouping operation
* * *
### 10.3.3 Pre-arranged group call
#### 10.3.3.1 General
The subclauses 10.3.3.2 and 10.3.3.3 describe the group call setup between the
MCPTT system and the LMR system on an interworking group defined in the MCPTT
system. The subclauses 10.3.3.4 and 10.3.3.5 describe the group call setup
between the MCPTT system and the LMR system on an interworking group defined
in the LMR system. The subclause 10.3.3.7 describes the late entry procedures
and subclause 10.3.3.8 describes the group call release procedures. Group
calls can use MC media encryption between the IWF and the MCPTT clients as
described in 3GPP TS 33.180 [8]. A call that uses an LMR vocoder may use LMR
E2EE if the calling and called parties have previously been provisioned with
the appropriate LMR E2EE keys.
The procedures in the present subclause are applicable to the following non-
broadcast group call types: pre-configured group regroup calls, pre-configured
user regroup calls and group regroup calls.
NOTE: MC media encryption is independent of LMR E2EE techniques. MC media
encryption can be applied in addition to LMR E2EE.
#### 10.3.3.2 Group call setup initiated by MCPTT user on an interworking
group defined in MCPTT system
In this procedure, an MCPTT user is initiating a group call on an interworking
group defined in the MCPTT system. The signalling procedure is described in
figure 10.3.3.2-1.
This subclause is based upon subclause for pre-arranged group call setup in
3GPP TS 23.379 [7], subclause 10.6.2.3.1.1.2.
Pre-conditions:
1\. The interworking group information is known at the MCPTT server and the
IWF by configuration or group creation. The interworking group has been
defined in the MCPTT system.
2\. MCPTT client 1 and MCPTT client 2 are registered and their respective
users are authenticated and authorized to use the MCPTT service.
3\. The users in this interworking group have been affiliated to the group.
4\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
NOTE 1: For all the signalling messages passing through the IWF between the
MCPTT system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.3.3.2-1: Group call setup initiated by MCPTT user on an interworking
group defined in MCPTT system
1\. MCPTT user at MCPTT client 1 initiates a group call for the selected
interworking group identified by MCPTT group ID.
2\. MCPTT client 1 sends a group call request to the MCPTT server.
3\. MCPTT server checks whether the user of MCPTT client 1 is authorized to
initiate a group call on the selected interworking group.
4\. MCPTT server proceeds group call setup procedures towards the affiliated
MCPTT system users as described in 3GPP TS 23.379 [7].
5\. MCPTT server sends IWF group call request(s) towards the IWF. If the IWF
has affiliated to this group on behalf of the group\'s LMR users, only one IWF
group call request message is sent to the IWF. If the MCPTT server has
received individual affiliations from the group\'s LMR users, an individual
IWF group call request is sent (to the IWF) for each affiliated LMR user.
NOTE 2: How the LMR users are called is outside the scope of the present
document.
NOTE 3: Steps 4 and 5 can occur in any order.
6\. The IWF returns IWF group call response(s) to the MCPTT server. If E2EE is
specified, then the MCPTT users and the LMR users shall use the same codec. If
E2EE is not specified, the MCPTT users and the LMR users can use different
codecs and transcoding is needed at the IWF.
7\. The MCPTT server sends group call response to the MCPTT client 1 about
successful call establishment.
8\. The group call on the interworking group has successfully established
media plane for communication and any user can transmit media. The MCPTT
system where the interworking group is defined is the controlling system of
the group call and manages the floor control.
#### 10.3.3.3 Group call setup initiated by LMR user on an interworking group
defined in MCPTT system.
In this procedure, an LMR user is initiating a group call on an interworking
group defined in the MCPTT system. The signalling procedure is described in
figure 10.3.3.3-1.
This subclause is based upon subclause for pre-arranged group call setup in
3GPP TS 23.379 [7], subclause 10.6.2.3.1.1.2.
Pre-conditions:
1\. The interworking group information is known at the MCPTT server and the
IWF by configuration or group creation. The interworking group has been
defined in MCPTT system.
2\. MCPTT client 1 and MCPTT client 2 are registered and their respective
users are authenticated and authorized to use the MCPTT service.
3\. The users in this interworking group have been affiliated to the
interworking group.
4\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
5\. LMR user initiates a group call.
NOTE 1: For all the signalling messages passing through the IWF between the
MCPTT system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.3.3.3-1: Group call initiated by LMR user on an interworking group
defined in MCPTT system
1\. The IWF sends an IWF group call request to the MCPTT server for call
establishment. If floor control is requested by the calling LMR user, an
indication of implicit floor request is included. If the group call request
contains an implicit floor request it may also include location information.
2\. MCPTT server calls the affiliated users from MCPTT system as described in
3GPP TS 23.379 [7]. If E2EE is specified, then the MCPTT users and the LMR
users shall use the same codec. If E2EE is not specified, the MCPTT users and
the LMR users can use different codecs and transcoding is needed at the IWF.
3\. If the group has other affiliated LMR users than the calling party and the
MCPTT server has received individual affiliations from those LMR users, an
individual IWF group call request is sent to the IWF for each affiliated LMR
user.
NOTE 2: Steps 2 and 3 can occur in any order.
NOTE 3: How the LMR users from the LMR system are being called is outside the
scope of the present document.
4\. The IWF returns IWF group call response(s) to the MCPTT server.
5\. The MCPTT server confirms the successful establishment of the group call
by sending an IWF Group call response to the IWF.
NOTE 4: How the group call response is returned to the initiating LMR user is
outside the scope of the present document.
6\. The interworking group call has successfully established media plane for
communication and any user can transmit media. The MCPTT system where the
interworking group is defined is the controlling system of the group call and
manages the floor control.
NOTE 5: How the floor control is managed in the LMR system is outside the
scope of the present document.
#### 10.3.3.4 Group call setup initiated by MCPTT user on an interworking
group defined in the LMR system
In this procedure, an MCPTT user is initiating a group call on an interworking
group defined in the LMR system. The signalling procedure is described in
figure 10.3.3.4-1.
This subclause is based upon subclause for Pre-arranged group call setup in
3GPP TS 23.379 [7], subclause 10.6.2.3.1.1.2.
Pre-conditions:
1\. The interworking group information is known at the MCPTT Server and the
IWF by configuration or group creation. The interworking group has been
defined in the LMR system.
2\. MCPTT client 1 and MCPTT client 2 are registered and their respective
users are authenticated and authorized to use the MCPTT service.
3\. The users in this interworking group have been affiliated to the group.
4\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
NOTE 1: For all the signalling messages passing through the IWF between the
MCPTT system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.3.3.4-1: Group call initiated by MCPTT user on an interworking group
defined in the LMR system
1\. MCPTT user at MCPTT client 1 initiates a group call on the selected
interworking group identified by MCPTT group ID.
2\. MCPTT client 1 sends a group call request to the MCPTT server.
3\. As the interworking group is defined in the LMR system the MCPTT server
sends an IWF group call request to the IWF.
4\. The IWF sends individual IWF group call request(s) to the MCPTT server for
each affiliated MCPTT user in the group, in this example scenario to the user
in MCPTT client 2.
NOTE 2: How the LMR users are called is outside the scope of the present
document.
5\. The MCPTT server sends a group call request to the MCPTT client 2.
6\. The MCPTT client 2 acknowledges towards the MCPTT server by sending a
group call response.
7\. The MCPTT server acknowledges towards the IWF by sending an IWF group call
response.
8\. The IWF sends an IWF group call response to the MCPTT server to
acknowledge the IWF group call request received in step 3.
9\. The MCPTT server sends a group call response to the initiating MCPTT user.
If E2EE is specified, then the MCPTT users and the LMR users shall use the
same codec. If E2EE is not specified, the MCPTT users and the LMR users can
use different codecs and transcoding is needed at the IWF.
10\. The group call over the interworking group has successfully established
media plane for communication and any user can transmit media. The LMR system
where the interworking group is defined is the controlling system of the group
call and manages the floor control.
#### 10.3.3.5 Group call setup initiated by LMR user on an interworking group
defined in the LMR system.
In this procedure, an LMR user is initiating a group call on an interworking
group defined in the LMR system. The signalling procedure is described in
figure 10.3.3.5-1.
This subclause is based upon subclause for Pre-arranged group call setup in
3GPP TS 23.379 [7], subclause 10.6.2.3.1.1.2.
Pre-conditions:
1\. The interworking group information is known at the MCPTT Server and the
IWF by configuration or group creation. The interworking group has been
defined in the LMR system.
2\. MCPTT client 1 and MCPTT client 2 are registered and their respective
users are authenticated and authorized to use the MCPTT service.
3\. The users in this interworking group have been affiliated to the group.
4\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
5\. LMR user initiates a group call.
NOTE 1: For all the signalling messages passing through the IWF between the
MCPTT system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.3.3.5-1: Group call initiated by LMR user on an interworking group
defined in the LMR system
1\. The IWF sends an IWF group call request(s) to the MCPTT server for call
establishment. An individual IWF group call request is sent to the MCPTT
server for each affiliated MCPTT user in the group, in this example scenario
to the users in MCPTT clients 1 and 2. If floor control is requested by the
calling LMR user, an indication of implicit floor request is included. If the
group call request contains an implicit floor request it may also include
location information.
2\. MCPTT server sends a group call request(s) to the target MCPTT user(s) as
described in 3GPP TS 23.379 [7].
3\. MCPTT client(s) receiving the group call request, acknowledge towards the
MCPTT server by sending a group call response.
4\. The MCPTT server acknowledges the IWF group call request(s) by sending a
IWF group call response(s) to the IWF. If E2EE is specified, then the MCPTT
users and the LMR users shall use the same codec. If E2EE is not specified,
the MCPTT users and the LMR users can use different codecs and transcoding is
needed at the IWF.
NOTE 2: How the IWF group call response(s) is handled in the IWF / LMR system
and how the other LMR users are being called is outside the scope of the
present document.
5\. The interworking group call has successfully established media plane for
communication and any user can transmit media. The LMR system where the
interworking group is defined is the controlling system of the group call and
manages the floor control.
#### 10.3.3.6 Encrypted group call with transcoding
Pre-conditions:
1\. An MCPTT session is established between an MCPTT client, the interworked
LMR system (represented by the IWF), and the MCPTT server.
2\. There is an ongoing media transmission.
3\. An SDP negotiation has occurred between the IWF and MCPTT Server to
establish both the vocoder and the security parameters for the call.
4\. The IWF is configured to perform transcoding of voice media and has
obtained key material from the MCPTT system using the procedures in 3GPP TS
33.180 [8].
Figure 10.3.3.6-1: Encrypted group call with transcoding
1\. The MCPTT client has been given the floor and is transmitting voice media.
2\. The MCPTT client encodes audio using a codec defined for the MCPTT group,
encrypts the encoded voice using procedures in 3GPP TS 33.180 [8], and
forwards the encrypted voice media to the MCPTT server.
3\. The MCPTT server forwards the encrypted voice media to other participants
in the group call including the IWF.
4\. The IWF decrypts the voice media from the MCPTT client using the
procedures in 3GPP TS 33.180 [8]. The IWF transcodes the voice to a LMR codec.
If needed, the IWF re-encrypts the transcoded voice media using LMR security
procedures (these are out-of-scope of this specification), and forwards the
voice media to the LMR system.
NOTE: Where transcoding occurs is outside the scope of this specification. In
this procedure, it is assumed to take place internal to the IWF.
5\. Sometime later the floor becomes idle.
6\. The LMR system (represented by the IWF in figure 10.3.3.6‑1) requests and
is granted the floor.
7\. The IWF has been given the floor and is transmitting voice media.
8\. The IWF receives voice media from the LMR system. If the voice media is
encrypted, the IWF decrypts the voice media using LMR security procedures
(these are out-of-scope of this specification). The IWF transcodes the voice
to the group\'s MCPTT codec. The IWF re-encrypts the transcoded voice using
the procedures in 3GPP TS 33.180 [8].
9\. The IWF forwards the voice media to the MCPTT server.
10\. The MCPTT server forwards the voice media to other participants in the
group call.
#### 10.3.3.7 Late Entry
##### 10.3.3.7.1 General
Late Entry for an ongoing interworking group call is triggered by a successful
group affiliation procedure from the participating system.
NOTE: These procedures apply to all types of group calls, including, for
example, emergency call, imminent peril call and broadcast call.
##### 10.3.3.7.2 Group call late entry on an interworking group defined in the
MCPTT system
In this procedure, the group affiliation from IWF triggers a late entry
procedure in the MCPTT system. The signalling procedure is described in figure
10.3.3.7.2-1.
For the first affiliating LMR user, this procedure is applicable for both IWF
affiliation options (see subclauses 10.1.2.1 and 10.3.1). For the following
LMR users affiliating to the same group, this procedure is triggered only if
the IWF passes through individual affiliations for each group member.
This subclause is based upon subclauses in 3GPP TS 23.379 [7] for:
\- Late entry for pre-arranged group call, subclause 10.6.2.3.1.1.4, and
\- Group call for an MCPTT group defined in partner MCPTT system, subclause
10.6.2.4.3.1.
Pre-conditions:
1\. The interworking group information is known at the MCPTT server and the
IWF by configuration or group creation. The interworking group has been
defined in the MCPTT system.
2\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
3\. There is an on-going group call in the interworking group involving MCPTT
clients 1 and 2.
4\. First LMR user affiliates to the interworking group.
NOTE 1: For all the signalling messages passing through the IWF between the
MCPTT system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.3.3.7.2-1: Group call late entry on an interworking group defined in
the MCPTT system
1\. The IWF triggers a group affiliation towards the MCPTT server (see
subclause 10.1.2.2).
2\. The MCPTT server initiates a group call late entry for an interworking
group.
3\. The MCPTT server sends an IWF group call request to the IWF.
NOTE 2: How the IWF delivers the group call request to the LMR system is out
of the scope of the present document.
4\. The IWF confirms the group call request by sending IWF group call response
to the MCPTT server.
5\. The IWF (and the LMR user) is successfully added to the ongoing group call
and MCPTT users at MCPTT client 1 and MCPTT client 2 may be notified about the
LMR user joining the group call.
6\. If the floor has been granted to another user, the MCPTT server sends a
IWF floor taken (6a) to the IWF. If the floor is not granted to any party, an
IWF floor idle (6b) is sent to the IWF.
##### 10.3.3.7.3 Group call late entry on an interworking group defined in the
LMR system
In this procedure, the group affiliation from MCPTT system triggers a late
entry procedure in the LMR system. The signalling procedure is described in
figure 10.3.3.7.3-1.
This procedure describes the affiliation and late entry of the first MCPTT
user into the interworking group, but it is applicable also for all subsequent
MCPTT users\' affiliations to the same group.
This subclause is based upon subclauses in 3GPP TS 23.379 [7] for:
\- Late entry pre-arranged group call, subclause 10.6.2.3.1.1.4, and
\- Group call setup involving groups from multiple MCPTT systems, subclause
10.6.2.4.1.1.
Pre-conditions:
1\. The interworking group information is known at the MCPTT server and the
IWF by configuration or group creation. The interworking group has been
defined in the LMR system.
2\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
3\. There is an on-going group call in the interworking group, involving only
LMR users.
NOTE 1: For all the signalling messages passing through the IWF between the
MCPTT system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.3.3.7.3-1: Group call late entry on an interworking group defined in
the LMR system
1\. MCPTT user (client 1) affiliates to the group (see subclause 10.1.2.4).
NOTE 2: How the IWF delivers the affiliation to LMR system and how the LMR
system handles the late entry is out of scope of the present document.
2\. The IWF sends an IWF group call request to the MCPTT server.
3\. The MCPTT server triggers a group call setup procedure for the newly
affiliated user in MCPTT client 1, as described in 3GPP TS 23.379 [7].
4\. The MCPTT server confirms the successful establishment of the group call
by sending IWF group call response to the IWF. If E2EE is specified, then the
MCPTT users and the LMR users shall use the same codec. If E2EE is not
specified, the MCPTT users and the LMR users can use different codecs and
transcoding is needed at the IWF.
5\. MCPTT client 1 is successfully added to the ongoing group call.
6\. If the floor has been granted to another user, the IWF sends an IWF floor
taken (6a) to the MCPTT server. If the floor is not granted to any party, an
IWF floor idle (6b) is sent.
7\. The MCPTT server sends Floor taken (7a) or Floor idle (7b) to the newly
affiliated user in MCPTT client 1, as described in 3GPP TS 23.379 [7].
#### 10.3.3.8 Interworking group call release
##### 10.3.3.8.1 General
The procedures in this subclause define the cases where the group host server
releases an ongoing interworking group call for all the participants of that
group.
If the group host server is an MCPTT server, the release conditions are
described in 3GPP TS 23.379 [7], subclause 10.6.2.4.1.2.
If the group host server is an LMR system, represented by an IWF, the release
conditions are outside the scope of the present document.
##### 10.3.3.8.2 Group call release on an interworking group defined in the
MCPTT system
In this procedure, the MCPTT system is releasing a group call on an
interworking group defined in the MCPTT system. The signalling procedure is
described in figure 10.3.3.8.2-1.
This subclause is based upon subclause 10.6.2.4.1.2 Group call release in 3GPP
TS 23.379 [7].
Pre-conditions:
1\. The interworking group information is known at the MCPTT server and the
IWF by configuration or group creation. The interworking group has been
defined in the MCPTT system.
2\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
3\. There is an on-going group call involving the IWF and MCPTT clients 1 and
2.
NOTE 1: For all the signalling messages passing through the IWF between the
MCPTT system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.3.3.8.2-1: Group call release initiated by MCPTT system on an
interworking group
1\. The MCPTT server initiates a group call release on an interworking group.
NOTE 2: The MCPTT server may decide to release the group call for different
reasons, see subclause 10.6.2.4.1.2 in 3GPP TS 23.379 [7].
2\. The MCPTT server identifies the participants of the ongoing group call, at
least one of them being an LMR user, represented by an IWF.
3\. The MCPTT server sends IWF group call release request(s) to the IWF. If
the IWF has affiliated to this group on behalf of the group\'s LMR users, only
one IWF group call release request message is sent to the IWF. If the MCPTT
server has received individual affiliations from the group\'s LMR users, an
individual IWF group call release request is sent (to the IWF) for each
affiliated LMR user.
NOTE 3: How the group call release request(s) is(are) forwarded to the LMR
system is out of scope of the present document.
4\. The MCPTT server sends the (MCPTT) group call release request(s) to the
group\'s MCPTT users, as described in 3GPP TS 23.379 [7].
NOTE 4: Steps 3 and 4 can occur in any order.
5\. The IWF confirms the IWF group call release request(s) received in step 3
by IWF group call release response(s) to the MCPTT server.
6\. The MCPTT client 1, client 2 and the IWF have successfully released the
floor control and media plane resources associated with the group call that is
released.
##### 10.3.3.8.3 Group call release on an interworking group defined in the
LMR system
In this procedure, the LMR system is releasing a group call on an interworking
group defined in the LMR system. The signalling procedure is described in
figure 10.3.3.8.3-1.
This subclause is based upon subclause 10.6.2.4.1.2 Group call release in 3GPP
TS 23.379 [7].
Pre-conditions:
1\. The interworking group information is known at the MCPTT server and the
IWF by configuration or group creation. The interworking group has been
defined in the LMR system.
2\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
3\. There is an on-going group call involving the IWF and MCPTT clients 1 and
2.
4\. The LMR system initiates release of the group call.
NOTE 1: The reasons for the LMR system\'s decision to release the group call
are out of scope of the present document.
NOTE 2: For all the signalling messages passing through the IWF between the
MCPTT system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.3.3.8.3-1: Group call release initiated by LMR system on an
interworking group defined in the LMR system
1\. The IWF sends IWF group call release requests to the MCPTT server. An
individual IWF group call release request is sent for each MCPTT user in the
call.
2\. The MCPTT server forwards the release requests to the group\'s MCPTT users
(in this example to users in MCPTT clients 1 and 2), as described in 3GPP TS
23.379 [7].
3\. The MCPTT clients respond with group call release response(s).
4\. The MCPTT server confirms the IWF group call release requests received in
step 1 by IWF group call release responses to the IWF.
5\. The MCPTT client 1, client 2 and the IWF have successfully released the
floor control and media plane resources associated with the group call that is
released.
### 10.3.4 Group broadcast
#### 10.3.4.1 General
A broadcast group call is a special group call where the initiating user
expects no response from the receiving users so that when the transmission is
complete, so is the call. The initiating user can be an MCPTT user or can be
an LMR user.
The group-broadcast group is defined as a set of groups, not a set of users.
The user that originates the group-broadcast group call is the only one
transmitting media during this call.
The group-broadcast group is defined with a hierarchy. For example, groups A
and B may be subordinate to a group-broadcast group. All subordinate groups
belonging to a group-broadcast group are defined either in the MCPTT system or
the LMR system.
#### 10.3.4.2 Group-broadcast group call procedure with an interworking group
where the group-broadcast group is defined in the MCPTT system
3GPP TS 23.379 [7], subclause 10.6.2.5.2.1 describes the procedure for a
group-broadcast group call within a single MCPTT system. The present procedure
describes a group-broadcast group call that includes the IWF.
In this procedure, the MCPTT server is initiating the broadcast and is the
owner of the group-broadcast group.
The procedure shows the case where the call is initiated by a MCPTT user.
However, if the override feature is enabled, then the call originator may be
overridden.
Figure 10.3.4.2-1 illustrates the procedure for group-broadcast group call
establishment (the group-broadcast group is defined in the MCPTT system).
Pre-conditions:
1\. The group (e.g. A) to which MCPTT client 2 and the IWF are members is a
subordinate group of the group-broadcast group (i.e., the group-broadcast
group was defined with group A as a subordinate group).
2\. The group (e.g. A) currently has an on-going MCPTT group call that is not
an MCPTT emergency group call.
3\. The call initiator of the group-broadcast group is a member of another
group (e.g., X, not group A) which is also a subordinate group of the group-
broadcast group (i.e., the group-broadcast group was defined with group X as a
subordinate group).
4\. The group-broadcast group and its subordinate groups are defined in the
same group management server and served by the same MCPTT server.
{width="6.08125in" height="7.009722222222222in"}
Figure 10.3.4.2-1: Group-broadcast group call involving IWF (group-broadcast
group is defined in the MCPTT system)
1\. MCPTT user at MCPTT client 1 initiates the group-broadcast group call
setup procedure.
2\. The MCPTT client 1 sends a group-broadcast group call request to the MCPTT
server.
3\. The MCPTT server needs to resolve the group-broadcast group ID into its
subordinate groups in order to contact the affiliated MCPTT users of those
subordinate groups.
4\. The MCPTT server then needs to consider any on-going group calls on those
subordinate groups because this may affect the behaviour for what happens
next. In this case a group call exists on a subordinate group. Thus, the MCPTT
users involved in the group call on this subordinate group.
5\. The MCPTT server performs group call release procedures of groups defined
in the MCPTT system as described in subclause 10.3.3.8.2.
6\. A group-broadcast group call request is sent to MCPTT client 2 and an IWF
group-broadcast group call request to the IWF. If the IWF has affiliated to
this group on behalf of the group\'s LMR users, only one IWF group-broadcast
group call request is sent to the IWF. If the MCPTT server has received
individual affiliations from the group\'s LMR users, an individual IWF group-
broadcast group call request is sent (to the IWF) for each affiliated LMR
user.
NOTE 1: How the group-broadcast group call request(s) is(are) forwarded to the
LMR system is out of scope of the present document.
7\. MCPTT client 2 is notified of the incoming group-broadcast group call.
NOTE 2: How LMR user(s) is(are) notified of the incoming group-broadcast group
call is outside the scope of the present document.
8\. MCPTT client 2 and the IWF respond to the IWF group-broadcast group call
request by sending an IWF group-broadcast group call response. If the IWF has
affiliated to this group on behalf of the group\'s LMR users, only one IWF
group-broadcast group call response is sent to the MCPTT server. If the MCPTT
server has received individual affiliations from the group\'s LMR users, an
individual IWF group-broadcast group call response is sent (to the MCPTT
server) for each affiliated LMR user.
9\. The MCPTT server responds to MCPTT client 1 (the call initiator) that the
group-broadcast group call has been established by sending a group-broadcast
group call response.
10\. The MCPTT client 1 notifies its user that the user can begin transmitting
using the group-broadcast group call resources.
Once the user of MCPTT cleint 1 completes transmitting, the group-broadcast
group call is released.
#### 10.3.4.3 Group-broadcast group call procedure with an interworking group
where the group-broadcast group is defined in the LMR system
3GPP TS 23.379 [7], subclause 10.6.2.5.2.1 describes the procedure for a
group-broadcast group call within a single MCPTT system. The present procedure
describes a group-broadcast group call that includes the IWF.
In this procedure, the IWF is the owner of the group-broadcast group and is
initiating the group-broadcast group call.
The procedure only shows the case where the call is initiated by a MCPTT user.
However, if the override feature is enabled, then the call originator may be
overridden.
Figure 10.3.4.3-1 illustrates the procedure for group-broadcast group call
establishment (the group-broadcast group is defined in the LMR system).
Pre-conditions:
1\. The group (e.g. A) to which MCPTT client 2 is a member is a subordinate
group of the group-broadcast group (i.e., the group-broadcast group was
defined with group A as a subordinate group).
2\. The group (e.g. A) currently has an on-going MCPTT group call that is not
an MCPTT emergency group call.
3\. The call initiator, MCPTT client 1, of the group-broadcast group is a
member of another group (e.g., X, not group A) which is also a subordinate
group of the group-broadcast group (i.e., the group-broadcast group was
defined with group X as a subordinate group).
4\. The group-broadcast group and its subordinate groups are defined in the
IWF.
Figure 10.3.4.3-1: Group-broadcast group call involving IWF (group-broadcast
group defined in the LMR system)
1\. MCPTT user at MCPTT client 1 initiates the group-broadcast group call
setup procedure.
2\. The MCPTT client 1 sends a group-broadcast group call request to the MCPTT
server.
3\. As the group-broadcast group is defined in the LMR system the MCPTT server
sends an IWF group-broadcast group call setup request to the IWF.
4\. The IWF performs group call release procedures of groups defined in the
LMR system as described in subclause 10.3.3.8.3.
5\. The IWF issues a group-broadcast group call setup request to establish the
group-broadcast call.
6\. The MCPTT user of MCPTT client 2 is notified.
NOTE: How LMR user(s) is(are) notified of the incoming group-broadcast group
call is outside the scope of the present document.
7\. Optionally, MCPTT client 2 respond with a group-broadcast group call
response to the MCPTT server and then to the IWF.
8\. The MCPTT server responds to MCPTT client 1 (the call initiator) that the
group-broadcast group call has been established by sending a group-broadcast
group call response.
9\. The MCPTT client 1 notifies its user that the user can begin transmitting
using the group-broadcast group call resources.
Once the user of MCPTT client 1 completes transmitting, the group-broadcast
group call is released.
#### 10.3.4.4 Group-broadcast group call release with an interworking group
procedure where the group-broadcast group is defined in the MCPTT system
When the call originator has completed transmitting, the group-broadcast group
call is ended and the resources are released.
Figure 10.3.4.4-1 illustrates the procedure for group-broadcast group call
release (the group-broadcast group is defined in the MCPTT system).
Pre-conditions:
1\. An on-going group-broadcast group call involving MCPTT client 1, the MCPTT
client 2 and the IWF exists.
Figure 10.3.4.4-1: Group-broadcast group call transmission ended (group-
broadcast group is defined in the MCPTT system)
1\. MCPTT user on MCPTT client 1 finished transmitting.
2\. A group-broadcast group call release request is sent to the MCPTT server
of the group-broadcast group.
3\. The MCPTT users of MCPTT client 2 and the IWF of the group-broadcast
group\'s subordinate groups are sent a group-broadcast group call release
request. If the IWF has affiliated to this group on behalf of the group\'s LMR
users, only one IWF group-broadcast group call release request is sent to the
IWF. If the MCPTT server has received individual affiliations from the
group\'s LMR users, an individual IWF group-broadcast group call request is
sent (to the IWF) for each affiliated LMR user.
4\. MCPTT client 2 and the IWF notify their users that the group-broadcast
group call has ended.
NOTE: How LMR user(s) is(are) notified that the group-broadcast group call has
ended is outside the scope of the present document.
5\. MCPTT client 2 and the IWF respond to confirm the release of the group-
broadcast group call by sending a group-broadcast group call release response.
If the IWF has affiliated to this group on behalf of the group\'s LMR users,
only one IWF group-broadcast group call release response is sent to the MCPTT
server. If the MCPTT server has received individual affiliations from the
group\'s LMR users, an individual IWF group-broadcast group call response is
sent (to the MCPTT server) for each affiliated LMR user.
6\. The MCPTT server sends a group-broadcast group call release response
indicating to the initiator that the call is now ended.
#### 10.3.4.5 Group-broadcast group call release with an interworking group
procedure where the group-broadcast group is defined in the LMR system
When the call originator has completed transmitting, the group-broadcast group
call is ended and the resources are released.
Figure 10.3.4.5-1 illustrates the procedure for group-broadcast group call
release (the group-broadcast group defined in the LMR system).
Pre-conditions:
1\. An on-going group-broadcast group call involving MCPTT client 1, the MCPTT
client 2 and the IWF exists.
Figure 10.3.4.5-1: Group-broadcast group call transmission ended (group-
broadcast group defined in the LMR system)
1\. The MCPTT user on MCPTT client 1 finished transmitting.
2\. A group-broadcast group call release request is sent to the MCPTT server.
3\. As the group-broadcast group is defined in the LMR system the MCPTT server
sends an IWF group-broadcast group call release request to the IWF.
4\. The IWF sends an IWF group-broadcast group call release request to the
MCPTT server hosting client 2. The MCPTT server sends the group-broadcast
group call release request to MCPTT client 2.
5\. MCPTT client 2 is notified that the group-broadcast group call has ended.
NOTE: How LMR user(s) is(are) notified that the group-broadcast group call has
ended is outside the scope of the present document.
6\. MCPTT client 2 responds to confirm the release of the group-broadcast
group call by sending a group-broadcast group call release response.
7\. The MCPTT server sends an IWF group-broadcast group call release response
to the IWF. The IWF becomes aware that MCPTT client 2 has confirmed the group-
broadcast group call release and replies with another IWF group-broadcast
group call release response back to the MCPTT server to trigger step 8.
8\. The MCPTT server sends a group-broadcast group call release response
indicating to the initiator that the group-broadcast group call is now ended.
#### 10.3.4.6 Broadcast group regroup call using pre-configured group
##### 10.3.4.6.1 General
The temporary group created using a pre-configured group can be a broadcast
group or a non-broadcast group.
A broadcast group regroup call using pre-configured groups can be achieved by
first regrouping users into a pre-configured group regroup, making the
broadcast group call on the pre-configured group, and then cancelling the pre-
configured group regroup.
##### 10.3.4.6.2 Broadcast group regroup call using pre-configured group the
MCPTT system
The broadcast group regroup call procedure using pre-configured group allows
an authorized MCPTT user to initiate a broadcast call to a set of MCPTT
groups, which are regrouped only for the duration of the broadcast call. The
regroup is cancelled at the end of the broadcast call to prevent users from
talking back on the pre-configured group regroup. This procedure requires that
the authorized MCPTT user is a group member of at least one of the MCPTT
groups included in the regroup operation.
Figure 10.3.4.6.2‑1 illustrates the procedure to initiate a broadcast group
regroup call using a pre-configured MCPTT regroup group owned by the MCPTT
system. For simplicity, no receiving clients are shown.
Pre-conditions:
\- The MCPTT client is registered with the MCPTT service.
\- The MCPTT group identity and group configuration for the pre-configured
group regroup have been pre-configured in the MCPTT client and the IWF. The
MCPTT client and the IWF have received the relevant security related
information to allow them to communicate in the pre-configured group regroup.
\- The MCPTT client is authorized to initiate a pre-configured group regroup
using the pre-configured group regroup procedure.
\- The MCPTT client is aware of a suitable pre-configured group whose
configuration has been pre-configured in the IWF and the MC service UEs of the
MCPTT users who will be regrouped.
\- The MCPTT client is affiliated to group 1.
\- The IWF is affiliated to one or more of MCPTT group 1, 2 or 3.
\- The pre-configured group regroup is homed in the MCPTT server.
\- The IWF is home to at least one group that\'s a constituent group of the
pre-configured group regroup.
Figure 10.3.4.6.2-1: Broadcast group regroup call using pre-configured group
in the MCPTT system
1\. The authorized user of the MCPTT client initiates the pre-configured group
regroup formation procedure using pre-configured groups as specified in
subclause 10.3.7.1. MCPTT groups 1, 2, and 3 are regrouped into group 4.
2\. The MCPTT user at the MCPTT client performs the broadcast group call
procedure as specified in subclause 10.3.4.
3\. The MCPTT client initiates the pre-configured group regroup cancellation
procedure using pre-configured groups as specified in subclause 10.3.7.1.
##### 10.3.4.6.3 Broadcast group regroup call using pre-configured group in
the IWF
The broadcast group regroup call procedure using a pre-configured group allows
an IWF user to initiate a broadcast call to a set of MCPTT groups, which are
regrouped only for the duration of the broadcast call.
Figure 10.3.4.6.3-1 illustrates the procedure to initiate a broadcast group
regroup call using a pre-configured group owned by the IWF.
Pre-conditions:
\- MCPTT clients 1 and 2 are registered with the MCPTT service.
\- The MCPTT group identity and group configuration for the pre-configured
group regroup have been pre-configured in MCPTT clients 1 and 2, and MCPTT
clients 1 and 2 have received the relevant security related information to
allow them to communicate in the pre-configured group regroup.
\- MCPTT client 1 is affiliated to group 1, MCPTT client 2 is affiliated to
group 2. Group 3 is used as the pre-configured group regroup.
\- The pre-configured group regroup is homed in the IWF.
\- The MCPTT server is home to at least one group that\'s a constituent group
of the pre-configured group regroup.
Figure 10.3.4.6.3-1: Broadcast group regroup call using pre-configured group
in the IWF
1\. The IWF initiates the group regroup formation procedure using pre-
configured groups as specified in subclause 10.3.7.1. MCPTT groups 1 and 2 are
regrouped into group 3.
2\. The IWF performs the broadcast group call procedure as specified in
subclause 10.3.4.
3\. The IWF initiates the pre-configured group regroup cancellation procedure
using pre-configured groups as specified in subclause 10.3.7.1.
### 10.3.5 Chat group call
#### 10.3.5.1 General
This subclause is based upon subclause for chat group call in 3GPP TS 23.379
[7], subclause 10.6.2.3.1.2. For LMR systems that do not support the concept
of chat groups, the IWF might still adapt its calls to the MCPTT chat model.
#### 10.3.5.2 MCPTT user initiated chat group call in an interworking group
defined in LMR system
In this procedure, an MCPTT user initiates a chat group call in an
interworking group defined in the LMR system. The signalling procedure is
described in figure 10.3.5.2-1.
Pre-conditions:
1\. The interworking group information is known at the MCPTT server and the
IWF by configuration or group creation. The interworking group has been
defined in the LMR system.
2\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
NOTE: For all the signalling messages passing through the IWF between the
MCPTT system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.3.5.2-1: MCPTT user initiated chat group call in an interworking
group defined in the LMR system
1\. MCPTT user of the MCPTT client indicates to join the group communication
for the group. The MCPTT client joins the group by sending a group join
request to the MCPTT server. If there is a request to transmit, then the group
join request contains an indication of an implicit floor request and the
location of the joining party if required.
2\. The MCPTT server inspects the Group join request for presence of location
information of the calling party. If location information is included in the
join request, the MCPTT server checks the privacy policy (authorisation to
provide location information to other MCPTT users on a call when talking, as
defined in 3GPP TS 23.379 [7] Annex A.3) of the requesting MCPTT user to
decide if the user\'s location information may be provided to other MCPTT
users on the call and the IWF.
3\. The MCPTT server notices that the interworking group is defined in the LMR
system and forwards the group join request with or without location depending
on the outcome of the privacy check as an IWF group join request to the IWF.
4\. The IWF replies with an IWF group join response indicating the acceptance
of the group join request and also returns the IWF selected media parameters
for the chat group call in the IWF group join response.
5\. The MCPTT server forwards the IWF group join response to the MCPTT client
as a group join response.
6\. If the MCPTT client requests to transmit, the MCPTT server establishes the
media plane (if not already established) for the call.
7\. Floor control will continue to be used by the floor participants
associated with the MCPTT client and the IWF for the duration of the call.
Media plane signalling using floor control will be used for subsequent calls
for the group as long as one or more users are affiliated.
#### 10.3.5.3 LMR user initiated chat group call in an interworking group
defined in MCPTT system
In this procedure, an LMR user initiates a chat group call in an interworking
group defined in the MCPTT system. The signalling procedure is described in
figure 10.3.5.3-1.
Pre-conditions:
1\. The interworking group information is known at the IWF by configuration.
The interworking group has been defined in the MCPTT system.
2\. MCPTT user 1 and MCPTT user 2 have previously joined (affiliated) to the
group.
3\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
4\. LMR user initiates a join to the group.
NOTE: For all the signalling messages passing through the IWF between the
MCPTT system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.3.5.3-1: LMR user initiated chat group call in an interworking group
defined in the MCPTT system
1\. The IWF sends an IWF group join request to the MCPTT server. The request
to join may contain location information of the transmitting party. If there
is a request to transmit, then the IWF group join request contains an
indication of an implicit floor request and the location of the joining party
if required.
2\. The MCPTT server checks whether the MCPTT ID is authorized to affiliate to
the group. MCPTT server generates an implicit affiliation if the MCPTT ID is
not already affiliated to the group.
3\. The MCPTT server replies with a group join response indicating the
acceptance of the group join request and also returns the MCPTT server
selected media parameters for the chat group call in the IWF group join
response.
4\. If the IWF requests to transmit, the MCPTT server establishes the media
plane (if not already established) for the call.
5\. Floor control will continue to be used by the floor participants
associated with MCPTT client 1, MCPTT client 2 and the IWF for the duration of
the call. Media plane signalling using floor control will be used for
subsequent calls for the group as long as one or more users are affiliated.
#### 10.3.5.4 Release chat group call on an interworking group defined in the
LMR system
This procedure describes the case where the LMR system releases an ongoing
MCPTT chat group call on an interworking group defined in the LMR system, for
all the participants of that group call. The signalling procedure is described
in figure 10.3.5.4-1.
Pre-conditions:
1\. A chat group call is ongoing involving an MCPTT client and the IWF.
2\. The LMR system initiates release of the chat group call.
Figure 10.3.5.4-1: Release chat group call on an interworking group defined in
the LMR system
1\. The IWF sends an IWF group call release request to the MCPTT server. An
individual IWF group call release request is sent for each MCPTT user in the
call.
2\. MCPTT server forwards the release request(s) to the group\'s MCPTT users,
as described in 3GPP TS 23.379 [7].
3\. MCPTT users are notified about the release of the group call.
4\. Optionally, the MCPTT client confirms the group call release request
received in step 2 with a group call release response to the MCPTT server.
5\. The MCPTT server forwards the group call release response to the IWF as an
IWF group call release response.
6\. The MCPTT client and the IWF release the floor control and media plane
resources associated with the chat group call that is released. Successful
release of the chat group call does not affect the status of affiliation of
any of the clients.
#### 10.3.5.5 Release chat group call on an interworking group defined in the
MCPTT system
This procedure describes the case where the MCPTT server releases an ongoing
MCPTT chat group call, on an interworking group defined in the MCPTT system,
for all the participants of that group call, since at least one of the
conditions for release are met e.g. due to hang time expiry, last participant
leaving, second last participant leaving, initiator leaving, or the number of
affiliated MCPTT group members is below the minimum number permitted.
The signalling procedure is described in figure 10.3.5.5-1.
Pre-conditions:
1\. A chat group call is ongoing involving MCPTT clients 1, 2 and the IWF.
Figure 10.3.5.5-1: Release chat group call on an interworking group defined in
the MCPTT system
1\. The MCPTT server decides to release the MCPTT chat group call which is
ongoing e.g., due to hang time expiry, last participant leaving, second last
participant leaving, initiator leaving, or minimum number of affiliated MCPTT
group members are not present.
2\. The MCPTT server sends an IWF group call release request to the IWF to
release the ongoing session. If the IWF has joined itself to this group on
behalf of all the group\'s LMR users, only one IWF group call release request
message is sent to the IWF. If the MCPTT server has received individual joins
from the group\'s LMR users, an individual IWF group call release request is
sent to the IWF for each joined LMR user.
3\. The MCPTT server sends a group call release request towards each MCPTT
participant of the ongoing group call.
4\. The MCPTT users are notified about the release of the group call.
5\. The IWF confirms the IWF group call release request(s) received in step 2
by IWF group call release response(s) to the MCPTT server.
6\. Optionally, the MCPTT client(s) receiving a group call release request may
send a group call release response to the MCPTT server.
7\. MCPTT client 1, client 2 and the IWF release the floor control and media
plane resources associated with the chat group call that is released.
Successful release of the chat group call does not affect the status of
affiliation of any of the clients.
#### 10.3.5.6 void
#### 10.3.5.7 void
#### 10.3.5.8 Newly joined MCPTT group member of a group defined in the LMR
system
Procedures in figure 10.3.5.8-1 are those for a group member entering an
ongoing MCPTT group call, i.e. performing a late entry.
Pre-conditions:
1\. The MCPTT client is registered and the MCPTT user has been authenticated
and authorized to use the MCPTT service.
2\. There is an ongoing group call on the group homed on the LMR system.
3\. The MCPTT client has not yet joined the group call.
4\. The MCPTT user indicates to join the group call.
Figure 10.3.5.8-1: Late entry of a newly joined MCPTT group member
1\. The MCPTT client sends a group join request with the MCPTT group ID of the
desired group to the MCPTT server. If there is a request to transmit, then the
group joint request contains an indication of an implicit floor request.
2\. The MCPTT server forwards the request to the IWF.
3\. The IWF replies with a group join response indicating the acceptance of
the group join request.
4\. The MCPTT server forwards the response to the MCPTT client.
5\. The IWF establishes the media plane with the MCPTT client.
6\. The IWF may notify its users that an MCPTT user has joined the group.
7 a. The IWF sends an IWF floor taken (for the current talker) to the MCPTT
server if the floor has been taken.
7b. The MCPTT responds to any incoming IWF floor taken message by forwarding a
floor taken message to the MCPTT client.
8\. Floor control will continue to be used by the floor participants.
#### 10.3.5.9 Newly joined LMR group member of a group defined in the MCPTT
system
Procedures in figure 10.3.5.9-1 are those for the IWF entering an ongoing
MCPTT group call, i.e. performing a late entry.
Pre-conditions:
1\. MCPTT user 1 and MCPTT user 2 have previously joined to the group.
2\. MCPTT users using MCPTT client 1 and MCPTT client 2 are in an ongoing
group call.
3\. The IWF has not yet joined the group call.
Figure 10.3.5.9-1: Late entry of a newly joined LMR group member
1\. The IWF sends a group join request with the MCPTT group ID of the desired
group and either using the MCPTT ID corresponding to the LMR group member or
using the pre-configured MCPTT ID for use when the IWF is affiliating itself
on behalf of the group\'s LMR users. If there is a request to transmit, then
the group join request contains an indication of an implicit floor request. If
the group join request includes an implicit floor request it may also include
location information.
2\. The MCPTT server receives the group join request. MCPTT server generates
an implicit affiliation using the MCPTT ID used by the IWF (if the IWF or the
LMR user is not already affiliated to the group) and verifies that IWF is
authorized to affiliate to the group.
3\. The MCPTT server replies with a group join response indicating the
acceptance of the group join request.
4\. The MCPTT server establishes the media plane between the IWF and the MCPTT
server.
> 5\. MCPTT users at MCPTT client 1 and MCPTT client 2 may be notified about
> the IWF joining the group call.
6\. The MCPTT server sends a floor taken (for the current talker) to the IWF.
7\. Floor control will continue to be used by the floor participants
associated with MCPTT client 1, MCPTT client 2 and the IWF.
#### 10.3.5.10 MCPTT client returning to coverage on a group homed in the LMR
system
Procedures in figure 10.3.5.10-1 are those for an MCPTT client returning to
coverage during an ongoing MCPTT chat group call.
Pre-conditions:
1\. The MCPTT user using an MCPTT client is in an ongoing chat group call when
the MCPTT client goes out of radio coverage.
Figure 10.3.5.10-1: Late entry of a MCPTT client returning from out of
coverage
1\. The MCPTT client or MCPTT server detects that MCPTT client has returned to
coverage.
NOTE: How the MCPTT client or MCPTT server detects that the client has
returned to coverage is out of scope of the present document.
2\. The media plane between the MCPTT client and the IWF are re-established
using media plane control signalling
3a. The IWF sends an IWF floor taken to the MCPTT server if anyone currently
has the floor.
3b. The MCPTT server forwards a floor taken message to the MC Client if anyone
currently has the floor.
4\. Floor control will continue to be used by the floor participants.
### 10.3.6 Exiting group call due to de-affiliation
#### 10.3.6.1 General
The following procedures are applicable both for the pre-arranged and chat
group calls.
#### 10.3.6.2 Exiting group call defined in the LMR system due to de-
affiliation
Procedures in figure 10.3.6.2-1 are the signalling control plane procedures
for the IWF requesting a newly de-affiliated MCPTT user to leave an ongoing
MCPTT group call.
Pre-conditions:
1\. The MCPTT group is previously defined on the IWF with MCPTT users
affiliated to that group. At least one user is an LMR user represented by an
MCPTT ID.
2\. An MCPTT user on the MCPTT client and an LMR user via the IWF, are on an
ongoing call.
Figure 10.3.6.2-1: Exiting MCPTT group call due to de-affiliation
1\. The MCPTT client is de-affiliated.
2\. The IWF sends an IWF group call leave request to the MCPTT client via the
MCPTT server.
3\. The MCPTT server forwards the IWF group call leave request as a group call
leave request to the MCPTT client.
4\. The MCPTT user at the MCPTT client is notified about leaving the group
call.
5\. The MCPTT client sends the group call leave response to the MCPTT server
and leaves the group call.
6\. The MCPTT server forwards the group call leave response to the IWF as an
IWF group call leave response.
7\. The MCPTT client is now removed from the ongoing group call.
#### 10.3.6.3 Exiting group call defined in the MCPTT system due to de-
affiliation
Procedures in figure 10.3.6.3-1 are the signalling control plane procedures
for the MCPTT server requesting a newly de-affiliated LMR user to leave an
ongoing MCPTT group call.
Pre-conditions:
1\. The MCPTT group is previously defined on the group management server with
MCPTT users affiliated to that group. At least one user is an LMR user
represented by an MCPTT ID.
2\. An MCPTT user on the MCPTT client and an LMR user via the IWF, are on an
ongoing call.
Figure 10.3.6.3-1: Exiting MCPTT group call due to de-affiliation
1\. The LMR user represented by the IWF has been de-affiliated.
2\. The MCPTT server sends an IWF group call leave request to the LMR user via
the IWF.
3\. The IWF sends an IWF group call leave response to the MCPTT server and
leaves the group call.
4\. The LMR user represented by the IWF is now removed from the ongoing group
call.
### 10.3.7 Group regroup with pre-configured group
#### 10.3.7.1 General
A group regroup may be achieved by regrouping MCPTT groups into a new regroup
group which uses the configuration of a separate pre-configured MCPTT group.
The MCPTT group configuration needs to be provided to the relevant MCPTT group
members of the MCPTT groups that will be regrouped in advance of the
regrouping operation.
NOTE 1: A pre-configured group which is intended only to provide configuration
for the pre-configured group regroup process is identified by a parameter in
group configuration described in 3GPP TS 23.280 [5].
NOTE 2: The configuration may alternatively be taken from any MCPTT group that
has been configured in the IWF and the user profile of all the relevant MCPTT
users who will be regrouped.
NOTE 3: Pre-configured group regroups may be defined according to the
organizational structure of a mission critical organization, or by some other
means which allows the MCPTT client of an authorized user and the IWF to be
aware of an appropriate pre-configured group regroup for sets of MCPTT groups
that will be regrouped together.
The pre-configured MCPTT group that provides the configuration is not used as
the pre-configured group regroup itself, it only provides configuration for
one or more pre-configured group or user regroup. The MCPTT group ID of the
pre-configured group regroup is provided by the authorized user or the IWF
(for the case where the IWF owns the pre-configured group regroup) when the
pre-configured group regrouping is carried out.
The pre-configured group regroup can be specified to be a broadcast or non-
broadcast type according to the configuration of the MCPTT group whose
configuration is specified by the pre-configured group regroup request. The
broadcast type of pre-configured group regroup is used for one-way
communication where only an authorized user or the IWF (for the case where the
IWF owns the pre-configured group regroup) is allowed to transmit and all
other regroup members are only allowed to receive the communication (e.g. a
call from a dispatcher to all regroup members). The non-broadcast type is used
for two-way communication where all regroup members can transmit and receive
(i.e, the pre-configured group regroup call behaves like a normal non-
broadcast group call).
These procedures provide a regrouping service for MCPTT only and are
independent of group regrouping procedures specified in subclause 10.2.2. If
one of the MCPTT groups that has been requested for regrouping by means of
this procedure has already been regrouped by the group regrouping procedure
specified in 3GPP TS 23.280 [5] or subclause 10.2.2, the request for
regrouping shall be rejected. The rules for regrouping set forth in subclause
10.2.2.5 apply.
#### 10.3.7.2 Regroup formation using pre-configured group
##### 10.3.7.2.1 Regroup formation using pre-configured group initiated in the
MCPTT system
Figure 10.3.7.2.1-1 illustrates the procedure to initiate a regroup procedure
using a pre-configured MCPTT regroup group, where at least one of the groups
to be regrouped is configured in the IWF. The group management server in the
MCPTT system of the regroup group shares the necessary security related
parameters together with the group configuration of the pre-configured group
regroup with the group management server in the IWF; the MCPTT system does not
need to be aware of the group members of the pre-configured group regroup that
are receiving service in the IWF.
The procedure takes place prior to the establishment of a group call to the
pre-configured group regroup.
In this procedure, any gateway MC servers between the IWF and the MCPTT system
are not shown.
Pre-conditions:
\- The MCPTT client is authorized to initiated a pre-configured group regroup
procedure, and is receiving MCPTT service in the MCPTT system.
\- The MCPTT group identity and group configuration for the pre-configured
group regroup have been pre-configured in the IWF, and the IWF has received
the relevant security related information to allow communication in the pre-
configured group regroup.
\- In order to be aware whether the group is regrouped, the MCPTT server is
subscribed to the group configuration in GMS.
\- The GMS has subscribed group dynamic data as specified in subclause
10.1.5.5.1 from the MCPTT server within the same MCPTT system using the
procedures defined in subclause 10.1.5.6 in 3GPP TS 23.280 [5].
\- The IWF is affiliated to one or more of the MCPTT groups that will be
regrouped; and/or, the IWF may own one or more of MCPTT groups to be
regrouped.
\- The pre-configured group regroup is homed in the MCPTT server.
\- The IWF is home to at least one group that\'s a constituent group of the
pre-configured group regroup.
NOTE 1: The IWF has the configuratiton information contained in the pre-
configured group regroup, which is normally because at least one member of the
pre-configured group regroup is homed on the IWF.
Figure 10.3.7.2.1-1: Regroup procedure using pre-configured group initiated in
the MCPTT system
1\. The authorized user of the MCPTT client initiates the pre-configured group
regroup procedure, specifying the list of MCPTT groups to be regrouped
including MCPTT group 1, the MCPTT group ID of the pre-configured group
regroup and the MCPTT group ID of the group from which configuration
information for the pre-configured group regroup is to be taken.
2\. The MCPTT client sends the pre-configured regroup request to the MCPTT
server.
3\. The MCPTT server checks that the MCPTT client is authorized to initiate a
pre-configured group regroup procedure, and resolves the group identities of
the MCPTT groups requested in step 1. The MCPTT server also checks which group
members are affiliated to the requested MCPTT groups that are homed in the
MCPTT system. The MCPTT server identifies any partner systems or IWFs which
are the group home systems for MCPTT groups identified in the list of groups
to be regrouped. The MCPTT server may retrieve the configuration for the
regroup group from the GMS if that configuration information is not already
known to the MCPTT server.
NOTE 2: This procedure does not require that that the authorized user of the
MCPTT client is a group member of the MCPTT groups listed in the pre-
configured group regroup request, or that the authorized user of the MCPTT
client is an affiliated group member of any of the listed MCPTT groups.
4\. The MCPTT server sends an IWF pre-configured regroup requests to the IWF.
NOTE 3: Only group members that are affiliated to the MCPTT groups that are to
be regrouped are sent a pre-configured regroup request.
5\. The IWF sends an IWF pre-configured regroup response to the MCPTT server.
The IWF may reject the IWF group regroup response. (e.g. if one of its
constituent groups is in the emergency state or is already in a regroup, if
the IWF does not support temporary groups or the IWF does not support group
regrouping)
6\. The MCPTT server sends the pre-configured regroup response to the MCPTT
client.
After the pre-configured group regrouping procedure, the regrouping remains in
effect until explicitly cancelled by the procedure in subclause 10.3.7.3.
Participation by the IWF in the ongoing pre-configured group regroup persists
until the IWF is no longer affiliated to any of the regrouped groups.
##### 10.3.7.2.2 Regroup formation using pre-configured group initiated in the
IWF
Figure 10.3.7.2.2-1 illustrates the procedure to initiate a pre-configured
group regroup procedure using a pre-configured MCPTT group, where at least one
of the groups to be regrouped is configured in an MCPTT system. The group
management server in the IWF shares the necessary security related parameters
together with the group configuration of the MCPTT regroup group with the
group management server in the MCPTT system and the group management server in
the MCPTT system distributes this configuration including those security
parameters to its served MCPTT users according to the procedures in 3GPP TS
23.280 [5] subclause 10.2.7; the IWF does not need to be aware of the list of
group members of the pre-configured group regroup that are receiving service
in the MCPTT system. The group can have multiple MCPTT clients, but only one
MCPTT client involved in the session is shown for simplicity.
The procedure takes place prior to the establishment of a group call to the
pre-configured group regroup.
In this procedure, any gateway MC servers between the IWF and the MCPTT system
are not shown.
Pre-conditions:
\- The MCPTT client is an affiliated member of MCPTT group 1 where MCPTT group
1 is defined in the MCPTT system.
\- The MCPTT group identity and group configuration for the pre-configured
group regroup have been pre-configured in the MCPTT client, and the MCPTT
client has received the relevant security related information to allow
communication in the pre-configured group regroup.
\- The pre-configured group regroup is homed in the IWF.
\- The MCPTT system is home to at least one group that\'s a constituent group
of the pre-configured group regroup.
NOTE 1: The MCPTT system has the configuratiton information contained in the
pre-configured group, which is normally because at least one member of the
preconfigured group is homed on the MCPTT system.
Figure 10.3.7.2.2-1: Regroup procedure using pre-configured group initiated in
the IWF
1\. The IWF initiates the pre-configured group regroup procedure, specifying
the list of MCPTT groups to be regrouped including MCPTT group 1, the MCPTT
group ID of the pre-configured group regroup and the MCPTT group ID of the
group from which configuration information for the pre-configured group
regroup is to be taken. The IWF sends the IWF pre-configured regroup request
to the MCPTT server in the partner MCPTT system.
2\. The MCPTT server checks the status of any MCPTT groups hosted by itself,
and identifies affiliated group members of any of the identified MCPTT groups
(both MCPTT groups that are hosted in the MCPTT system and MCPTT groups that
are hosted in the IWF) that are receiving MCPTT service in the MCPTT system,
which includes the MCPTT client.
3\. The MCPTT server sends a pre-configured regroup request to the MCPTT
client.
NOTE 2: Only group members that are affiliated to the MCPTT groups that are to
be regrouped are sent a pre-configured regroup request.
4\. The MCPTT client notifies the user of the regrouping.
5\. The MCPTT client 2 may send the pre-configured regroup response to the
MCPTT server to acknowledge the regrouping action. This acknowledgement is not
sent in response to a multicast transmission of the pre-configured regroup
request.
6\. The MCPTT server affiliates the regrouped MCPTT client to the pre-
configured group regroup.
7\. The MCPTT server sends an IWF pre-configured regroup response to the IWF.
After the pre-configured group regrouping procedure, the regrouping remains in
effect until explicitly cancelled by the procedure in subclause 10.3.7.3.
MCPTT client participation in the ongoing pre-configured group regroup
persists until the MCPTT client is no longer affiliated to any of the
regrouped groups.
MCPTT client affiliation to the pre-configured group regroup may cease when
the clients MCPTT service ceases, e.g. when the UE is powered down, or by the
client performing a log-off operation.
#### 10.3.7.3 Regroup cancellation using pre-configured group regroup
##### 10.3.7.3.1 Regroup cancellation using pre-configured group initiated in
the MCPTT system
Figure 10.3.7.3.1-1 illustrates the procedure to cancel a regrouping that uses
a pre-configured MCPTT regroup group where there the regroup had been
initiated in the MCPTT system.
Pre-conditions:
\- The IWF has been regrouped into the pre-configured group regroup.
\- The MCPTT client is authorized to cancel a pre-configured group regroup.
\- The GMS has subscribed to the group dynamic data specified in 3GPP TS
23.280 [5] subclause 10.1.5.5.1 from the MCPTT server as specified in 3GPP TS
23.280 [5] subclause 10.1.5.6.
Figure 10.3.7.3.1-1: Regroup cancellation using pre-configured group initiated
in the MCPTT system
1\. The authorized user of the MCPTT client initiates the cancellation of the
pre-configured group regroup.
2\. The MCPTT client sends the pre-configured regroup cancel request to the
MCPTT server, specifying the MCPTT group ID of the regroup group.
3\. The MCPTT server checks that the MCPTT client is authorized to cancel a
pre-configured group regroup.
4\. The MCPTT server sends the IWF pre-configured regroup cancel request to
the IWF.
5\. The IWF sends the IWF pre-configured regroup cancel response to the MCPTT
server. The IWF may reject the IWF group regroup response. (e.g. if one of its
constituent groups is in the emergency state or is already in a regroup, if
the IWF does not support temporary groups or the IWF does not support group
regrouping)
6\. The MCPTT server sends a pre-configured regroup cancel response to the
MCPTT client.
##### 10.3.7.3.2 Regroup cancellation using pre-configured group initiated in
the IWF
Figure 10.3.7.3.2-1 illustrates the procedure to cancel a regrouping that uses
a pre-configured MCPTT group where the regroup is initiated in the IWF. Only
one MCPTT group member is shown for simplicity.
Pre-conditions:
\- The MCPTT client has been regrouped into a pre-configured group regroup,
and is receiving MCPTT service in the MCPTT system.
Figure 10.3.7.3.2-1: Cancel pre-configured group regroup procedure using pre-
configured group in the MCPTT system
1\. The IWF initiates the cancellation of the regrouping that uses a pre-
configured MCPTT group. The IWF sends the IWF pre-configured regroup cancel
request to the MCPTT server, specifying the MCPTT group ID of the regroup
group.
2\. The MCPTT server sends the pre-configured regroup cancel request to the
MCPTT client.
3\. The MCPTT client notifies the user of the cancellation of the pre-
configured group regrouping.
4\. The MCPTT client may send the pre-configured regroup remove response to
the MCPTT server to acknowledge the cancellation of the pre-configured group
regrouping. This acknowledgement is not sent in response to a multi-cast
transmission of the pre-configured regroup cancel request.
5\. The MCPTT server de-affiliates the MCPTT client from the pre-configured
group regroup.
6\. The MCPTT server sends the IWF pre-configured regroup cancel response to
the IWF.
#### 10.3.7.4 Regroup rejection using pre-configured group
##### 10.3.7.4.1 Regroup rejection using pre-configured group for regroup
initiated in the MCPTT system
Figure 10.3.7.4.1‑1 illustrates the case where the procedure to initiate a
pre-configured group regroup procedure with an MCPTT system and an IWF using a
pre-configured MCPTT group described in subclause 10.3.7.3.1 commences, but
where the request for the regroup is rejected by the IWF, for example because
one of the groups hosted by the IWF is already regrouped by other group
regrouping procedures.
In this procedure, any gateway MC servers between the IWF and the MCPTT system
are not shown.
Pre-conditions:
\- The MCPTT client is authorized to initiate a pre-configured group regroup
procedure.
\- The MCPTT group identity and group configuration for the pre-configured
group regroup have been pre-configured in the IWF, and the IWF has received
the relevant security related information to allow communication in the pre-
configured group regroup.
\- In order to be aware whether the group is regrouped, the MCPTT server is
subscribed to the group configuration in GMS.
\- The GMS has subscribed group dynamic data as specified in subclause
10.1.5.5.1 from the MCPTT server within the same MCPTT system using the
procedures defined in subclause 10.1.5.6 in 3GPP TS 23.280 [5].
\- The IWF is affiliated to one or more of the MCPTT groups that will be
regrouped; and/or, the IWF may own one or more of MCPTT groups to be
regrouped.
Figure 10.3.7.4.1-1: Regroup rejection using pre-configured group for group
initiated in the MCPTT system
1\. The authorized user of the MCPTT client initiates the pre-configured group
regroup procedure, specifying the list of MCPTT groups to be regrouped
including MCPTT group 1, the MCPTT group ID of the pre-configured group
regroup and the MCPTT group ID of the group from which configuration
information for the pre-configured group regroup is to be taken.
2\. The MCPTT client sends the pre-configured regroup request to the MCPTT
server.
3\. The MCPTT server checks that the MCPTT client is authorized to initiate a
pre-configured group regroup procedure, and resolves the group identities of
the MCPTT groups requested in step 1. The MCPTT server also checks which group
members are affiliated to the requested MCPTT groups that are homed in the
MCPTT system. The MCPTT server identifies any partner systems or IWFs which
are the group home systems for MCPTT groups identified in the list of groups
to be regrouped. The MCPTT server may retrieve the configuration for the pre-
configured group regroup from the GMS if that configuration information is not
already known to the MCPTT server.
NOTE: This procedure does not require that that the authorized user of the
MCPTT client is a group member of the MCPTT groups listed in the regroup
request, or that the authorized user of the MCPTT client is an affiliated
group member of any of the listed MCPTT groups.
4\. The MCPTT server sends the IWF pre-configured regroup requests to the IWF.
5\. The IWF sends a pre-configured regroup reject to the MCPTT server,
indicating the reason for rejection, for example because one or more of the
MCPTT groups has already been regrouped by another group regrouping procedure,
either internal to the IWF or in an MCPTT system.
6\. The MCPTT server sends a pre-configured regroup reject to the MCPTT
client, indicating the reason for the rejection.
##### 10.3.7.4.2 Regroup rejection using pre-configured group for regroup
initiated in the IWF
Figure 10.3.7.4.2 1 illustrates the case where the procedure to initiate a
regroup procedure with an MCPTT system and an IWF using a pre-configured MCPTT
group described in subclause 10.3.7.3.2 commences, but where the request for
the pre-configured group regroup is rejected by the MCPTT system, for example
because one of the groups hosted by the MCPTT system is already regrouped by
other group regrouping procedures.
In this procedure, any gateway MC servers between the IWF and the MCPTT system
are not shown.
Pre-conditions:
\- The MCPTT client is an affiliated member of MCPTT group 1 where MCPTT group
1 is defined in the MCPTT system.
\- The MCPTT group identity and group configuration for the pre-configured
group regroup have been pre-configured in the MCPTT client, and the MCPTT
client has received the relevant security related information to allow
communication in the pre-configured group regroup.
Figure 10.3.7.4.2-1: Regroup rejection using pre-configured group for group
initiated in the IWF
1\. The IWF initiates the pre-configured group regroup procedure, specifying
the list of MCPTT groups to be regrouped including MCPTT group 1, the MCPTT
group ID of the pre-configured group regroup and the MCPTT group ID of the
group from which configuration information for the pre-configured group
regroup is to be taken. The IWF sends the IWF pre-configured regroup request
to the MCPTT server.
2\. The MCPTT server checks the status of any MCPTT groups hosted by that
MCPTT server, and determines that one or more requested MCPTT groups has
already been regrouped by another group regrouping procedure.
3\. The partner MCPTT server sends an IWF pre-configured regroup reject to the
IWF, indicating the reason for rejection.
#### 10.3.7.5 Pre-configured regroup update procedures
##### 10.3.7.5.1 MCPTT client PTTs on MCPTT group during an in-progress pre-
configured group regroup
Figure 10.3.7.5.1‑1 illustrates the procedure when a user attempts to set up a
MCPTT group call on a group involved in an in-progress pre-configured group
regroup, homed in the IWF.
Pre-conditions:
\- The MCPTT client is an affiliated member of MCPTT group A that is part of
an in-progress pre-configured group regroup with MCPTT groups B and C. MCPTT
groups A, B and C can be homed in either the IWF or the MCPTT system.
\- MCPTT group D is being used as the pre-configured group regroup. MCPTT
group D is homed in the IWF.
\- The MCPTT client has missed the pre-configured regroup request message
(e.g. poor signalling conditions, race condition).
Figure 10.3.7.5.1-1: Procedure for MCPTT client PTTs on MCPTT group during an
in-progress pre-configured group regroup
1\. The MCPTT client attempts to start a call on MCPTT group A. The MCPTT
client sends a group call request message to the MCPTT server containing MCPTT
group A as the target group.
2\. The MCPTT server forwards the request to the IWF as an IWF group call
request.
3\. The IWF sends an IWF group call response to the MCPTT server indicating
that the call set up is denied because the group is part of an in-progress
pre-configured group regroup.
4\. The MCPTT server forwards the response to the MCPTT client as a group call
response.
5\. The IWF sends an IWF pre-configured regroup request to the MCPTT server
containing MCPTT group D, the group ID of the pre-configured group regroup.
6\. The MCPTT server forwards the request to the MCPTT client as a pre-
configured regroup request.
7\. The MCPTT client notifies the user of the group call set up failure and of
the regrouping procedure.
NOTE 1: Step 5 can occur prior to step 4 and step 7 can occur after step 4.
8\. The MCPTT client sends the pre-configured regroup response to the MCPTT
server to acknowledge the regrouping action.
9\. The MCPTT server forwards the response to the IWF as an IWF pre-configured
regroup response. The IWF affiliates the regrouped MCPTT client to the pre-
configured group regroup.
NOTE 2: If there is a call currently in progress on the pre-configured group
regroup then this MCPTT client can be added to the call using the late entry
procedure. If there is no call currently in progress, then the MCPTT user can
retry the group call set up.
#### 10.3.7.6 Call request on pre-configured regroup group after group regroup
has been cancelled
##### 10.3.7.6.1 MCPTT client PTTs on pre-configured regroup group after group
regroup has been cancelled
Figure 10.3.7.6.1‑1 illustrates the procedure when an MCPTT user attempts to
set up a MCPTT group call on a pre-configured regroup group after the pre-
configured MCPTT group regroup has been cancelled.
Pre-conditions:
\- The MCPTT client is a member of MCPTT group A that was part of an in-
progress pre-configured group regroup with MCPTT groups B and C that has been
cancelled. MCPTT group D was used as the pre-configured regroup group. MCPTT
group D is homed in the IWF.
\- The MCPTT client has missed the pre-configured regroup cancel request
message (e.g. poor signalling conditions, race condition).
Figure 10.3.7.6.1-1: Procedure for MCPTT client PTTs on pre-configured regroup
group after the group regroup is cancelled
1\. The MCPTT client attempts to start a call on MCPTT group D, the pre-
configured regroup group. The MCPTT client sends a group call request message
to the MCPTT server containing MCPTT group D as the target group.
2\. The MCPTT server forwards the request to the IWF as an IWF group call
request.
NOTE 1: The pre-configured regroup group D can be a group in the MCPTT
client\'s profile, and the MCPTT client can be a member of group D.
3\. The IWF sends an IWF group call response to the MCPTT server indicating
that the call set up is denied because the group regroup is no longer active.
4\. The MCPTT server forwards the response to the MCPTT client as a group call
response
NOTE 2: In the following, steps 5, 6, 8 and 9 are optional.
5\. The IWF sends an IWF pre-configured regroup cancel request to the MCPTT
server.
6\. The MCPTT server forwards the request as a pre-configured regroup cancel
request to the MCPTT client.
NOTE 3: This message should be sent over unicast.
7\. The MCPTT client notifies the user of the group call set up failure and of
the regrouping cancellation.
8\. The MCPTT client sends a pre-configured regroup cancel response to the
MCPTT server to acknowledge the regrouping cancellation.
9\. The MCPTT server forwards the response to the IWF as an IWF pre-configured
regroup cancel response.
#### 10.3.7.7 Adding newly affiliated user to a pre-configured group regroup
##### 10.3.7.7.1 Adding newly affiliated MCPTT user to a pre-configured group
regroup
Figure 10.3.7.7.1‑1 illustrates the procedure to add a newly affiliated MCPTT
user to an in-progress pre-configured group regroup operation.
Pre-conditions:
\- The MCPTT client is a member of, but not yet affiliated with, a MCPTT group
that is part of an in-progress pre-configured group regroup operation.
\- The MCPTT group identity and group configuration for the regroup MCPTT
group has been pre-configured in the MCPTT client, and the MCPTT client has
received the relevant security related information to allow it to communicate
in the pre-configured group regroup.
Figure 10.3.7.7.1-1: Procedure to add a newly affiliated user to a pre-
configured group regroup
1\. The MCPTT client affiliates to an MCPTT group that is currently part of an
in-progress pre-configured group regroup. The affiliation follows the
procedure in subclause 10.1.2.4.
2\. The IWF sends an IWF pre-configured regroup request to the MCPTT server.
3\. The MCPTT server sends a pre-configured regroup request to the MCPTT
client.
4\. The MCPTT client notifies the user of the regrouping.
5\. The MCPTT client may send the pre-configured regroup response to the MCPTT
server to acknowledge the regrouping action. These acknowledgements are not
sent in response to a multicast transmission of the pre-configured regroup
request.
6\. The MCPTT server sends an IWF pre-configured regroup response to the IWF.
The IWF affiliates the MCPTT client to the group regroup.
##### 10.3.7.7.2 Adding newly affiliated user homed in the IWF to a pre-
configured group regroup
Figure 10.3.7.7.2‑1 illustrates the procedure to add a newly affiliated user
homed in the IWF to an in-progress pre-configured group regroup operation.
Pre-conditions:
\- The LMR user is a member of, but not yet affiliated to, an MCPTT group that
is part of an in-progress pre-configured group regroup operation.
\- The MCPTT group identity and group configuration for the pre-configured
group regroup has been pre-configured in the IWF, and the IWF has received the
relevant security related information to allow it to communicate in the pre-
configured group regroup.
Figure 10.3.7.7.2-1: Procedure to add a newly affiliated user to a pre-
configured regroup
1\. The IWF affiliates to an MCPTT group that is currently part of an in-
progress pre-configured group regroup. The affiliation follows the procedure
in subclause 10.1.2.2.
2\. The MCPTT server retrieves the MCPTT group ID of the pre-configured group
regroup and the MCPTT group ID of the group from which configuration
information for the pre-configured group regroup is to be taken.
3\. The MCPTT server sends an IWF pre-configured regroup request to the IWF.
4\. The IWF sends an IWF pre-configured regroup response to the MCPTT server
to acknowledge the regrouping action.
5\. The MCPTT server affiliates the IWF to the group regroup.
### 10.3.8 User regroup with pre-configured group
#### 10.3.8.1 General
A user regroup may be achieved by regrouping MCPTT users into a new regroup
group which uses the configuration of a separate pre-configured MCPTT group.
The MCPTT regroup group configuration needs to be provided to the relevant
MCPTT users who will be regrouped in advance of the regrouping operation. A
pre-configured user regroup may contain users homed in the IWF and the IWF may
host pre-configured user regroups which may contain members homed in an MCPTT
system.
NOTE 1: A pre-configured group which is intended only to provide configuration
for the pre-configured user regroup process is identified by a parameter in
group configuration described in 3GPP TS 23.280 [5].
NOTE 2: The configuration may alternatively be taken from any MCPTT group that
has been configured in the user profile of all of the relevant MCPTT users who
will be regrouped and that has also been configured to the IWF for the case
where the pre-configured user regroup contains members homed in the IWF.
The pre-configured user regroup that provides the configuration is not used as
the pre-configured user regroup itself, it only provides configuration for one
or more pre-configured user regroups. The MCPTT group ID of the pre-configured
user regroup is provided by the originating authorized user or the originating
IWF when the pre-configured user regrouping is carried out.
#### 10.3.8.2 Pre-configured user regroup formation
##### 10.3.8.2.1 Pre-configured user regroup formation by the MCPTT system
Figure 10.3.8.2.1‑1 illustrates the procedure to initiate a pre-configured
user regroup procedure using a pre-configured user regroup. The procedure
takes place prior to the establishment of a group call to the pre-configured
user regroup.
Pre-conditions:
\- MCPTT clients 2 and 3 are registered with the MCPTT service.
\- An MCPTT group that will be used for configuration of the pre-configured
user regroup has been pre-configured in MCPTT clients 2 and 3 and the IWF, and
MCPTT clients 2 and 3 and the IWF have received the relevant security related
information to allow them to communicate in the pre-configured user regroup.
\- MCPTT client 1 is authorized to initiated a pre-configured user regroup
using the pre-configured user regroup procedure.
\- MCPTT client 1 is aware of a suitable pre-configured group whose
configuration has been pre-configured in the MC service clients of the MCPTT
users who will be regrouped.
\- The pre-configured user regroup is homed in the MCPTT server.
{width="6.182638888888889in" height="4.829166666666667in"}
Figure 10.3.8.2.1-1: User regroup procedure using pre-configured group by the
MCPTT system
1\. The authorized user of MCPTT client 1 initiates the pre-configured user
regroup procedure, specifying the list of MCPTT users to be regrouped (MCPTT
clients 2, 3 and one or more IWF users), the MCPTT group ID of the pre-
configured user regroup, and the MCPTT group ID of the group from which
configuration information for the pre-configured user regroup is to be taken.
2\. MCPTT client 1 sends the pre-configured regroup request to the MCPTT
server. The request indicates the list of users to be included in the regroup
operation.
3\. The MCPTT server checks that MCPTT client 1 is authorized to initiate a
pre-configured user regroup procedure.
NOTE 1: MCPTT clients and users homed in the IWF can be involved in multiple
user and group regroups simultaneously.
4\. The MCPTT server sends the pre-configured regroup requests to MCPTT
clients 2 and 3 in steps 4a and 4b respectively.
5\. MCPTT clients 2 and 3 notify their users of the regrouping in steps 4a and
4b respectively.
6\. MCPTT clients 2 and 3 may send the pre-configured regroup response to the
MCPTT server to acknowledge the regrouping action. These acknowledgements are
not sent in response to a multicast transmission of the pre-configured regroup
request.
7\. The MCPTT server sends the IWF an IWF pre-configured regroup request.
8\. The IWF sends the MCPTT server and IWF pre-configured regroup response.
9\. The MCPTT server affiliates the regrouped MCPTT clients and the IWF to the
pre-configured user regroup.
10\. The MCPTT server sends a pre-configured user regroup response to MCPTT
client 1.
NOTE 2: After the pre-configured user regrouping procedure, the regrouping
remains in effect until explicitly cancelled by the procedure in subclause
10.3.8.3.1.
##### 10.3.8.2.2 Pre-configured user grop regroup formation by the IWF
Figure 10.3.8.2.2-1 illustrates the procedure for the IWF to initiate a pre-
configured user regroup procedure using a pre-configured MCPTT group. The
procedure takes place prior to the establishment of a pre-configured user
regroup call to the pre-configured user regroup. For simplicity, only one
receiving MCPTT client is shown.
Pre-conditions:
\- The MCPTT client is registered with the MCPTT service.
\- An MCPTT group that will be used for configuration of the pre-configured
user regroup has been pre-configured in the MCPTT client and the IWF, and the
MCPTT client has received the relevant security related information to allow
it to communicate in the pre-configured user regroup.
\- The pre-configured user regroup is homed in the IWF.
Figure 10.3.8.2.2-1: User regroup procedure using pre-configured group by the
IWF
1\. The IWF initiates the pre-configured user regroup, the IWF sends an IWF
pre-configured regroup request to the MCPTT server. The request indicates the
list of users to be included in the regroup operation, that are homed in the
MCPTT system.
NOTE 1: MCPTT clients and users homed in the IWF can be involved in multiple
user and group regroups simultaneously.
2\. The MCPTT server sends the pre-configured regroup request to the MCPTT
client.
3\. The MCPTT client notifies the MCPTT users of the regrouping.
4\. The MCPTT client may send the pre-configured regroup response to the MCPTT
server to acknowledge the regrouping action. These acknowledgement is not sent
in response to a multicast transmission of the pre-configured regroup request.
5\. The MCPTT server sends an IWF pre-configured regroup response to the IWF.
NOTE 2: After the pre-configured user regroup procedure, the regrouping
remains in effect until explicitly cancelled by the procedure in subclause
10.3.8.3.2.
#### 10.3.8.3 Pre-configured user regroup cancellation
##### 10.3.8.3.1 Pre-configured user regroup cancellation by the MCPTT system
Figure 10.3.8.3.1-1 illustrates the procedure to cancel a pre-configured user
regroup that uses a pre-configured MCPTT group. For simplicity, only one
receiving MCPTT client is shown.
Pre-conditions:
\- MCPTT client 2 and at least one user homed in the IWF have been regrouped
into the pre-configured user regroup.
\- MCPTT client 1 is authorized to cancel a pre-configured user regroup that
uses a pre-configured MCPTT group.
Figure 10.3.8.3.1-1: Cancel pre-configured user regroup procedure by the MCPTT
system
1\. The authorized user of MCPTT client 1 initiates the cancellation of the
pre-configured user regroup that uses a pre-configured MCPTT group.
2\. MCPTT client 1 sends the pre-configured regroup cancel request to the
MCPTT server, specifying the MCPTT group ID of the pre-configured user
regroup.
3\. The MCPTT server checks that MCPTT client 1 is authorized to cancel a pre-
configured user regroup.
4\. The MCPTT server sends the pre-configured regroup cancel requests to MCPTT
client 2.
5\. MCPTT clients 2 notifies the MCPTT user of the cancellation of the pre-
configured user regroup.
6\. MCPTT client 2 may send the MCPTT server a pre-configured regroup cancel
response. This acknowledgement is not sent in response to a multicast
transmission of the pre-configured regroup cancel request.
7\. The MCPTT server sends the IWF an IWF pre-configured regroup cancel
request.
8\. The IWF sends the MCPTT server an IWF pre-configured regroup cancel
response.
9\. The MCPTT server de-affiliates MCPTT clients 2 and 3 from the pre-
configured user regroup.
10\. The MCPTT server sends a pre-configured regroup cancel response to MCPTT
client 1.
##### 10.3.8.3.2 Pre-configured user regroup cancellation by the IWF
Figure 10.3.8.3.2-1 illustrates the procedure to cancel a pre-configured user
regroup that uses a pre-configured MCPTT group. For simplicity, only one
receiving MCPTT client is shown.
Pre-conditions:
\- An MCPTT client and at least one user homed in the IWF have been regrouped
into the pre-configured user regroup.
Figure 10.3.8.3.2-1: Cancel pre-configured pre-configured user regroup
procedure by the IWF
1\. The IWF initiates the cancellation of the pre-configured user regroup. The
IWF sends the pre-configured regroup cancel request to the MCPTT server,
specifying the MCPTT group ID of the pre-configured user regroup.
2\. The MCPTT server sends the pre-configured regroup cancel requests to the
MCPTT client.
3\. The MCPTT client notifies the MCPTT user of the cancellation of the pre-
configured user regroup.
4\. The MCPTT client may send the MCPTT server a pre-configured regroup cancel
response. This acknowledgement is not sent in response to a multicast
transmission of the pre-configured regroup cancel request.
5\. The MCPTT server sends an IWF pre-configured regroup cancel response to
the IWF.
## 10.4 Private call
### 10.4.1 Information flows for private calls
#### 10.4.1.1 General
The following subclauses define information flows for private calls on the
IWF-1 interface. Private call related information flows on reference points
other than IWF-1 are defined in 3GPP TS 23.379 [7].
#### 10.4.1.2 IWF private call request
Table 10.4.1.2-1 describes the information flow IWF private call request from
the MCPTT server to the IWF and from the IWF to the MCPTT server.
Table 10.4.1.2-1: IWF private call request information elements
+-----------------------------+--------+-----------------------------+ | Information Element | Status | Description | +-----------------------------+--------+-----------------------------+ | MCPTT ID | M | The MCPTT ID of the calling | | | | party | +-----------------------------+--------+-----------------------------+ | Functional alias | O | The functional alias | | | | associated with the MCPTT | | | | ID of the calling party. | +-----------------------------+--------+-----------------------------+ | MCPTT ID | M | The MCPTT ID of the called | | | | party | +-----------------------------+--------+-----------------------------+ | Use floor control | M | This element indicates | | indication | | whether floor control will | | | | be used for the private | | | | call. | +-----------------------------+--------+-----------------------------+ | SDP offer | M | Media parameters of MCPTT | | | | client. | +-----------------------------+--------+-----------------------------+ | Encryption Algorithm | O | Encryption algorithm to use | | | | for the call. The field can | | | | also indicate whether the | | | | encryption algorithm choice | | | | is determined from | | | | information in the media | | | | stream. | +-----------------------------+--------+-----------------------------+ | Encryption mode | M | Whether E2EE will be used. | +-----------------------------+--------+-----------------------------+ | Requested commencement mode | O | An indication of the | | | | commencement mode to be | | | | used. | +-----------------------------+--------+-----------------------------+ | Implicit floor request | O | An indication that the user | | | | is also requesting the | | (see NOTE) | | floor. | +-----------------------------+--------+-----------------------------+ | Location | O | Location of the calling | | | | party | +-----------------------------+--------+-----------------------------+ | NOTE: This element shall be | | | | included only when the | | | | originating client requests | | | | the floor. | | | +-----------------------------+--------+-----------------------------+
#### 10.4.1.3 IWF private call response
Table 10.4.1.3-1 describes the information flow IWF private call response from
the MCPTT server to the IWF and from the IWF to the MCPTT server.
Table 10.4.1.3-1: IWF private call response information elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the calling
party MCPTT ID O The MCPTT ID of the called party Acceptance confirmation O An
indication whether the user has positively accepted the call. SDP answer M
Media parameters selected Result M Result of the IWF private call request:
success or failure Encryption Algorithm(s) response O A list of one or more
alternative encryption algorithm(s) to use for the call. Use floor control
indication response O This element indicates whether the floor control
indication in the request is acceptable. Implicit floor request response O
This element indicates whether the indication that the user is also requesting
the floor in the request is acceptable.
* * *
#### 10.4.1.4 IWF ringing
Table 10.4.1.4-1 describes the information flow IWF ringing from the MCPTT
server to the IWF and from the IWF to the MCPTT server.
Table 10.4.1.4-1: IWF ringing information elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the calling
party MCPTT ID M The MCPTT ID of the called party Ringing indication O
Indication to the caller.
* * *
#### 10.4.1.5 IWF call end request
Table 10.4.1.5-1 describes the information flow IWF call end request from the
MCPTT server to the IWF and from the IWF to the MCPTT server.
Table 10.4.1.5-1: IWF call end request information elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the calling
party MCPTT ID M The MCPTT ID of the called party
* * *
#### 10.4.1.6 IWF call end response
Table 10.4.1.6-1 describes the information flow IWF call end response from the
IWF to the MCPTT server.
Table 10.4.1.6-1: IWF call end response information elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the
responding party
* * *
### 10.4.2 Private call setup in automatic commencement mode
#### 10.4.2.1 MCPTT user initiating an MCPTT private call
In this procedure, an MCPTT user is initiating an MCPTT private call
(automatic commencement mode) for communicating with a user in an LMR system,
with or without floor control enabled.
This subclause is based on the procedure for private call setup in automatic
commencement mode -- MCPTT users in multiple MCPTT systems described in 3GPP
TS 23.379 [7], subclause 10.7.2.3.1.
In figure 10.4.2.1-1, an MCPTT client initiates establishment of an MCPTT
private call with an LMR user.
Pre-conditions:
1\. The calling MCPTT user has selected automatic commencement mode for the
call;
2\. The MCPTT client is registered to the MCPTT service, as per procedure in
subclause 10.2 in 3GPP TS 23.379 [7].
3\. Optionally, MCPTT client may use an activated functional alias for the
call.
4\. The MCPTT server has subscribed to the MCPTT functional alias controlling
server within the MC system for functional alias activation/de-activation
updates.
Figure 10.4.2.1-1: Private call setup in automatic commencement mode,
initiated by an MCPTT user
1\. The MCPTT user at the MCPTT client initiates an MCPTT private call. The
MCPTT client sends an MCPTT private call request towards the MCPTT server. The
MCPTT private call request contains the MCPTT IDs corresponding to the calling
MCPTT party and called LMR party and an SDP offer containing one or more media
types. If available, the MCPTT user at the MCPTT client may also include a
functional alias. The following parameters are also included that describe the
MCPTT client\'s choices:
\- the encryption algorithm;
\- the encryption mode (encrypted or not);
\- an indication of whether the MCPTT client is requesting the floor, and if
the MCPTT client is requesting the floor, location information of the calling
MCPTT client may be provided;
\- requested commencement mode (automatic in this case); and
\- an indication of whether the call is to be full or half duplex (whether to
establish floor control).
2\. The MCPTT server checks whether the MCPTT user at the MCPTT client is
authorized to initiate the private call and whether the provided functional
alias, if present, can be used and has been activated for the user. Because
the IWF private call request is requesting automatic commencement mode, the
MCPTT server also checks whether the MCPTT user at the MCPTT client is
authorized to initiate a call in automatic commencement mode. If location
information was included in the MCPTT private call request, the MCPTT server
also checks the privacy policy (authorisation to provide location information
to other MCPTT users on a call when talking, as defined in 3GPP TS 23.379 [7]
Annex A.3) of the requesting MCPTT user to decide if the user\'s location
information may be provided to other MCPTT users on the call and the IWF.
3\. If authorized, the MCPTT server sends the IWF private call request that
may or may not include location of the requestor, depending on the outcome of
the privacy check towards the IWF, including the original parameters and
offering the same media types or a subset of the media types contained in the
initial received request as per 3GPP TS 23.379 [7].
NOTE: How the IWF private call request is forwarded to the LMR system is out
of scope of the present document.
4\. The IWF sends an IWF private call response to the MCPTT server, indicating
that the IWF does support one of the requested media types. The response
indicates success or failure. If the indication is failure, the response may
include one or more alternatives to the parameter values contained in step 3.
5\. The MCPTT server forwards the MCPTT private call response to the MCPTT
client. If the result parameter indicates success, then the MCPTT client
proceeds to step 6. Otherwise, if the parameters returned in the MCPTT private
call response are acceptable to the MCPTT client, then the MCPTT client can
send a new MCPTT private call request with the new parameters and behaves
according to those parameters. The calling MCPTT user may be notified of the
change in parameters, for example, that the call is to be without floor
control. The MCPTT user can choose to end the call rather than continue with
the new parameters. If the parameters returned are not acceptable to the MCPTT
client, then the call fails.
6\. The MCPTT client has successfully established media plane for
communication to the IWF and either end can transmit media. The MCPTT system
initiating the call is responsible of granting the floor, solving competing
floor requests and issuing floor revoked indications.
#### 10.4.2.2 LMR user initiating a private call with MCPTT user
In this procedure, an LMR user is initiating a private call (in automatic
commencement mode) for communicating with a user in MCPTT system, with or
without floor control enabled.
This subclause is based on the procedure for private call setup in automatic
commencement mode -- MCPTT users in multiple MCPTT systems described in 3GPP
TS 23.379 [7], subclause 10.7.2.3.1.
In figure 10.4.2.2-1, an LMR user initiates establishment of a private call
with an MCPTT user.
Pre-conditions:
1\. The calling LMR user has selected automatic commencement mode for the
call;
2\. The MCPTT client is registered to the MCPTT service, as per procedure in
subclause 10.2 in 3GPP TS 23.379 [7].
3\. The LMR user at the LMR system has initiated a private call towards an
MCPTT user.
4\. Optionally, LMR user may use an activated functional alias (homed in the
MCPTT system) for the call.
5\. The MCPTT server has subscribed to the MCPTT functional alias controlling
server within the MC system for functional alias activation/de-activation
updates.
NOTE 1: Private call operation between the LMR user and the IWF are out of
scope of the present document.
NOTE 2: The mapping between alternative addressing schemes of the LMR user and
the corresponding functional alias is out of scope of the present document.
Figure 10.4.2.2-1: Private call setup in automatic commencement mode,
initiated by an LMR user
1\. The IWF sends an IWF private call request towards the MCPTT server. The
IWF private call request contains the MCPTT IDs corresponding to the calling
LMR party and the called MCPTT party and an SDP offer containing one or more
media types. If available, the LMR party homed in the IWF may also include a
functional alias. The following parameters are also included that describe the
MCPTT client\'s choices:
\- the encryption algorithm;
\- the encryption mode (encrypted or not);
\- an indication of whether the LMR user is requesting the floor, and if the
MCPTT client is requesting the floor, location information of the calling
MCPTT client may be provided;
\- requested commencement mode (automatic in this case); and
\- an indication of whether the call is to be full or half duplex (whether to
establish floor control).
2\. The MCPTT server checks whether the MCPTT user at the MCPTT client is
authorized and able to receive the private call. Because the IWF private call
request is requesting automatic commencement mode, the MCPTT server also
checks whether the MCPTT user at the MCPTT client is authorized to receive a
call in automatic commencement mode. The MCPTT server also checks whether the
provided functional alias, if present, can be used and has been activated for
the LMR user homed in the IWF.
3\. If authorized, the MCPTT server sends the MCPTT private call request
towards the MCPTT client, including the original parameters with or without
the location of the calling party and offering the same media types or a
subset of the media types contained in the initial received request as per
3GPP TS 23.379 [7].
4\. The MCPTT client sends an MCPTT private call response to the MCPTT server
indicating that the MCPTT client does support one of the requested media
types. The response indicates success or failure. If the indication is
failure, the response may also include one or more alternatives to the
parameter values contained in step 3.
5\. The MCPTT server sends the IWF private call response to the IWF offering
the same media type as that sent in step 4. If the parameters returned are not
acceptable to the IWF, then the call fails. If the parameters returned in the
IWF private call response are different but acceptable to the IWF, then the
IWF can send a new IWF private call request with the new parameters starting
with step 1, which is to essentially restart the call. If there is no change
of parameter, then the call proceeds to step 6.
NOTE 2: The calling LMR user may be notified of the change in parameters, for
example, that the call is to be without floor control.
6\. The MCPTT client has successfully established media plane for
communication to the IWF and either end can transmit media. The LMR system
initiating the call is responsible of granting the floor, solving competing
floor requests and issuing floor revoked indications.
### 10.4.3 Private call setup in manual commencement mode
#### 10.4.3.1 MCPTT user is initiating an MCPTT private call
In this procedure, an MCPTT user is initiating an MCPTT private call (manual
commencement mode) for communicating with an LMR user via an IWF, with or
without floor control enabled.
This subclause is based on the procedure for private call setup in manual
commencement mode -- MCPTT users in multiple MCPTT systems described in 3GPP
TS 23.379 [7], subclause 10.7.2.3.2.
In figure 10.4.3.1-1, an MCPTT client initiates establishment of an MCPTT
private call with an LMR user.
Pre-conditions:
1\. The calling MCPTT user has selected manual commencement mode for the call.
2\. The MCPTT client is registered to the MCPTT service, as per procedure in
subclause 10.2 in 3GPP TS 23.379 [7].
3\. Optionally, MCPTT client may use an activated functional alias (homed in
the MCPTT system) for the call.
4\. The MCPTT server has subscribed to the MCPTT functional alias controlling
server within the MC system for functional alias activation/de-activation
updates.
Figure 10.4.3.1-1: Private call setup in manual commencement mode -- initiated
by an MCPTT user
1\. The MCPTT user at the MCPTT client would like to initiate an MCPTT private
call. The MCPTT client sends an MCPTT private call request towards the MCPTT
server. The MCPTT private call request contains the MCPTT IDs corresponding to
the calling MCPTT party and called LMR party and an SDP offer containing one
or more media types. If available, the MCPTT user at the MCPTT client may also
include a functional alias. The following parameters are also included that
describe the MCPTT client\'s choices:
\- the encryption algorithm;
\- the encryption mode (encrypted or not)
\- an indication of whether the MCPTT client is requesting the floor;
\- requested commencement mode (manual in this case), and if the MCPTT client
is requesting the floor, location information of the calling MCPTT client may
be provided; and
\- an indication of whether the call is to be full or half duplex (whether to
establish floor control).
2\. The MCPTT server checks whether the MCPTT user at the MCPTT client is
authorized to initiate the private call and whether the provided functional
alias, if present, can be used and has been activated for the user. Because
the IWF private call request is requesting manual commencement mode, the MCPTT
server also checks whether the MCPTT user at the MCPTT client is authorized to
initiate a call in manual commencement mode. If location information was
included in the MCPTT private call request, the MCPTT server also checks the
privacy policy (authorisation to provide location information to other MCPTT
users on a call when talking, as defined in 3GPP TS 23.379 [7] Annex A.3) of
the requesting MCPTT user to decide if the user\'s location information may be
provided to other MCPTT users on the call and the IWF.
3\. If authorized, the MCPTT server sends the IWF private call request towards
the IWF, including the original parameters that may or may not include
location of the requestor, depending on the outcome of the privacy check, and
offering the same media types or a subset of the media types contained in the
initial received request as per 3GPP TS 23.379 [7].
NOTE: How the IWF private call request is forwarded to the LMR system is out
of scope of the present document.
4\. The IWF may report failure with an IWF private call response to the MCPTT
server. The response may include one or more alternatives to the parameter
values contained in step 3. If the IWF does not report failure, the process
proceeds with step 6.
5\. The MCPTT server forwards the MCPTT private call response to the MCPTT
client. If the result parameter indicates failure, the MCPTT client may
abandon the call. If the parameters in the MCPTT private call response are
acceptable to the MCPTT client, then the MCPTT client can send a new MCPTT
private call request with the new parameters to the MCPTT server and behaves
according to those parameters. The calling user may be notified of the change
in parameters, for example, that the call is to be without floor control. The
calling user may choose to end the call rather than continue with the new
parameters.
6\. The receiving IWF sends an IWF ringing to the MCPTT server while waiting
for the call to be accepted.
7\. The MCPTT server forwards the MCPTT ringing to the MCPTT client. The MCPTT
client may indicate to the MCPTT user that the LMR user has been notified,
e.g. by producing ringback audio.
8\. Once the call has been accepted by the called user, the IWF sends an IWF
private call response to the MCPTT server. The IWF private call response
indicates that the IWF does support one of the requested media types.
9\. The MCPTT server forwards the MCPTT private call response to the MCPTT
client. The MCPTT client may indicate to the MCPTT user that the call is
connected, e.g. by stopping the ringback audio.
10\. The MCPTT client has successfully established media plane for
communication to the IWF. The MCPTT system initiating the call is responsible
of granting the floor and solving the competing floor requests, and floor
revoked indications.
#### 10.4.3.2 LMR user initiating a private call with MCPTT user
In this procedure, an LMR user is initiating a private call (in manual
commencement mode) for communicating with an MCPTT user via an IWF, with or
without floor control enabled.
This subclause is based on the procedure for private call setup in manual
commencement mode -- MCPTT users in multiple MCPTT systems described in 3GPP
TS 23.379 [7], subclause 10.7.2.3.2.
In figure 10.4.3.2-1, an LMR user initiates establishment of a private call
with an MCPTT user.
Pre-conditions:
1\. The calling LMR user has selected manual commencement mode for the call.
2\. The MCPTT client is registered to the MCPTT service, as per procedure in
subclause 10.2 in 3GPP TS 23.379 [7].
3\. The LMR user at the LMR system has initiated a private call towards an
MCPTT user.
4\. Optionally, LMR user may use an activated functional alias (homed in the
MCPTT system) for the call.
5\. The MCPTT server has subscribed to the MCPTT functional alias controlling
server within the MC system for functional alias activation/de-activation
updates.
NOTE 1: Private call operation between the LMR user and the IWF are out of
scope of the present document.
NOTE 2: The mapping between alternative addressing schemes of the LMR user and
the corresponding functional alias is out of scope of the present document
Figure 10.4.3.2-1: Private call setup in manual commencement mode, initiated
by an LMR user
1\. The IWF sends an IWF private call request towards the MCPTT server. The
IWF private call request contains the MCPTT IDs corresponding to the calling
LMR party and called MCPTT party and an SDP offer containing one or more media
types. If available, the LMR party homed in the IWF may also include a
functional alias. The following parameters are also included that describe the
IWF\'s choices:
\- the encryption algorithm;
\- the encryption mode (encrypted or not)
\- an indication of whether the LMR user is requesting the floor, and if the
MCPTT client is requesting the floor, location information of the calling
MCPTT client may be provided;
\- requested commencement mode (manual in this case); and
\- an indication of whether the call is to be full or half duplex (whether to
establish floor control).
2\. The MCPTT server checks whether the MCPTT user at the MCPTT client is
authorized and able to receive the private call. Because the IWF private call
request is requesting manual commencement mode, the MCPTT server also checks
whether the MCPTT user at the MCPTT client is authorized to receive a call in
manual commencement mode. The MCPTT server also checks whether the provided
functional alias, if present, can be used and has been activated for the LMR
user homed in the IWF.
3\. If authorized, the MCPTT server sends the MCPTT private call request
towards the MCPTT client, including the original parameters with or without
the location of the calling party and offering the same media types or a
subset of the media types contained in the initial received request as per
3GPP TS 23.379 [7].
NOTE 2: How the IWF private call request is forwarded to the LMR system is out
of scope of the present document.
4\. The MCPTT client may report failure with an MCPTT private call response to
the MCPTT server. The response may include one or more alternatives to the
parameter values contained in step 3. If the MCPTT client does not report
failure, the process proceeds with step 6.
5\. The MCPTT server forwards the MCPTT private call response to the IWF. If
the result parameter indicates failure, the IWF may abandon the call. If the
parameters in the IWF private call response are acceptable to the IWF, then
the IWF can send a new IWF private call request with the new parameters to the
MCPTT server and behaves according to those parameters. The IWF may choose to
end the call rather than continue with the new parameters.
6\. The MCPTT client sends an MCPTT ringing to the MCPTT server while waiting
for the call to be accepted by the MCPTT user.
7\. The MCPTT server sends an IWF ringing to IWF the while waiting for the
call to be accepted.
8\. Once the call has been accepted by the called user, the MCPTT client sends
an MCPTT private call response to the MCPTT server. The IWF private call
response indicates that the IWF does support one of the requested media types.
9\. The MCPTT sends the IWF private call response to the IWF.
10\. The MCPTT client has successfully established media plane for
communication to the IWF. The LMR system initiating the call is responsible of
granting the floor, solving competing floor requests and issuing floor revoked
indications.
### 10.4.4 Private call release
#### 10.4.4.1 MCPTT client initiated
The procedure describes the case where an MCPTT client requests release of an
ongoing MCPTT private call (with or without floor control) that was
established in either of the two commencement modes (manual or automatic).
This subclause is based upon the subclauses for MCPTT private call release in
3GPP TS 23.379 [7], subclauses 10.7.2.2.3.1 and 10.7.2.3.3.
Procedures in figure 10.4.4.1-1 are the basic signalling control plane
procedures for the MCPTT client initiating the release of an ongoing
interworked private call.
Pre-conditions:
1\. The MCPTT user on the MCPTT client is already registered for receiving
MCPTT service and is involved in a private call with an LMR user via the IWF
with or without floor control and established either in manual or automatic
commencement mode, as described in subclause 10.4.2 and subclause 10.4.3.
Figure 10.4.4.1-1: Private call release -- client initiated
1\. The user at the MCPTT client would like to release an ongoing interworked
private call with the LMR user.
2\. The MCPTT client sends an MCPTT private call end request towards the MCPTT
server (via SIP core) for tearing down the private call with the other client.
3\. The MCPTT server sends the corresponding IWF call end request towards the
IWF, addressed to the MCPTT client ID specified in the original MCPTT private
call end request.
NOTE: The LMR user is also notified about the release of the private call. How
the LMR user is notified is outside the scope of the present document.
4\. The IWF acknowledges the IWF call end request with an IWF call end
response sent towards the MCPTT server.
5\. After receiving the MCPTT private call end request acknowledgement from
the IWF, the MCPTT server generates an acknowledgement for the MCPTT client\'s
MCPTT private call end request.
6\. The MCPTT client and the IWF release all the media plane resources used
for the private call. Further, if the private call was established with floor
control, floor control resources are released and the MCPTT client cannot make
further requests for floor control or send media.
#### 10.4.4.2 MCPTT server initiated
The procedure describes the case where an MCPTT server terminates an ongoing
interworked private call (with or without floor control) that was established
in either of the two commencement modes (manual or automatic). The conditions
causing the MCPTT server to terminate the call could include expiry of the
MCPTT administrator configured maximum duration for MCPTT private calls or
expiry of the maximum time permitted for an MCPTT private call without
transmission/reception. This subclause is based upon the subclauses for MCPTT
private call release in 3GPP TS 23.379 [7], subclauses 10.7.2.2.3.2 and
10.7.2.3.3.
Procedures in figure 10.4.4.2-1 are the basic signalling control plane
procedures for the MCPTT server initiating termination of an ongoing
interworked private call.
Pre-conditions:
1\. The MCPTT user on the MCPTT client is already registered for receiving
MCPTT service and is involved in a private call with an LMR user via the IWF
with or without floor control and established either in manual or automatic
commencement mode, as described in subclause 10.4.2 and subclause 10.4.3.
Figure 10.4.4.2-1: End private call -- server initiated
1\. Upon conditions to terminate call e.g., MCPTT administrator configured
maximum duration for MCPTT private calls expiry or time out due to MCPTT
private call without transmission/reception, the MCPTT server decides to
initiate termination of an ongoing interworking private call between the MCPTT
client and the LMR user.
2a. The MCPTT server sends an MCPTT private call end request towards the MCPTT
client (via SIP core) for tearing down the private call.
2b. The MCPTT server sends a corresponding IWF call end request towards the
MCPTT client identity associated with the LMR user
3\. The MCPTT user at the MCPTT client is notified about the termination of
the private call.
NOTE: The LMR user is also notified about the termination of the private call.
How the LMR user is notified is outside the scope of the present document.
4\. The MCPTT client and the IWF acknowledge the request.
5\. The MCPTT client and the IWF release all the media plane resources used
for the private call. Further, if the private call was established with floor
control, floor control resources are released and the MCPTT client cannot make
further requests for floor control or send media.
#### 10.4.4.3 LMR user initiated
The procedure describes the case where either an LMR user or the LMR system is
requesting to release an ongoing interworked private call (with or without
floor control) and the call established in either of the two commencement
modes (manual or automatic). This subclause is based upon the subclauses for
MCPTT private call release in 3GPP TS 23.379 [7], subclauses 10.7.2.2.3.1 and
10.7.2.3.3.
Procedures in figure 10.4.4.3-1 are the basic signalling control plane
procedures for the LMR user, via the IWF, initiating the release of an ongoing
interworked private call.
Pre-conditions:
1\. The MCPTT user on the MCPTT client is already registered for receiving
MCPTT service and is involved in a private call with an LMR user via the IWF
with or without floor control and established either in manual or automatic
commencement mode, as described in subclause 10.4.2 and subclause 10.4.3.
Figure 10.4.4.3-1: Private call release -- IWF initiated
1\. The LMR system would like to release an ongoing interworked private call
with the MCPTT user.
2\. The IWF sends an IWF call end request towards the MCPTT server for tearing
down the private call with the MCPTT client.
3\. The MCPTT server sends the corresponding MCPTT private call end request
towards the MCPTT client specified in the original IWF call end request.
4\. The MCPTT user is notified about the release of the private call.
5\. The MCPTT client acknowledges the MCPTT private call end request.
6\. After receiving the MCPTT private call end request acknowledgement from
the MCPTT client, the MCPTT server generates an acknowledgement for the IWF\'s
IWF call end request.
7\. The MCPTT client and the IWF release all the media plane resources used
for the private call. Further, if the private call was established with floor
control, floor control resources are released and the MCPTT client cannot make
further requests for floor control or send media.
### 10.4.5 Encryption of private calls
Private calls can use MC media encryption (see 3GPP TS 33.180 [8]) between the
IWF and the MCPTT client. A private call that uses an LMR vocoder may use LMR
E2EE if the calling and called parties have previously been provisioned with
the appropriate LMR E2EE keys.
NOTE: MC media encryption is independent of LMR E2EE techniques. MC media
encryption can be applied in addition to LMR E2EE.
## 10.5 Floor control
### 10.5.1 General
Floor control involving a single MCPTT server is described in 3GPP TS 23.379
[7]. Floor control involving multiple MCPTT servers is also described in 3GPP
TS 23.379 [7] in that a primary MCPTT server is interconnected to a partner
MCPTT server. Subclause 10.5.2 describes how the floor control procedures for
interconnection also apply to interworking. Subclause 10.5.3 describes a
special case of floor control that can occur on an interworking group.
Subclauses 10.5.4/10.5.6 and 10.5.5/10.5.7 describe general cases of floor
control on an interworking group defined in the LMR system and in the MCPTT
system respectively, where the partner system has been configured to apply/not
apply local filtering of floor control requests before communicating with the
primary system.
### 10.5.2 Information flows for floor control
#### 10.5.2.1 General
The following sections describe information flows for interworking floor
control.
In the following information flows the MCPTT ID and its associated functional
alias represents the LMR user, the IWF, or the MCPTT user depending on the
interworking methods being used and the message source/destination.
#### 10.5.2.2 IWF floor request
Table 10.5.2.2-1 describes the information flow IWF floor request, from the
IWF to the MCPTT floor control server and from the MCPTT floor control server
to the IWF, which is used to request the floor for media transfer.
Table 10.5.2.2-1: IWF floor request
* * *
Information element Status Description MCPTT ID M Requester identity
Functional alias O Functional alias of the requester Floor priority M Priority
of the request Source identifier O Identifies the communication, e.g. by
identifying the media flow within a media multiplex, present only if media
multiplexing Location O Location information of requester
* * *
#### 10.5.2.3 IWF floor granted
Table 10.5.2.3-1 describes the information flow IWF floor granted, from the
IWF to the MCPTT floor control server and from the MCPTT floor control server
to the IWF, which is used to indicate that a request for floor is granted and
media transfer is possible.
Table 10.5.2.3-1: IWF floor granted
* * *
Information element Status Description MCPTT ID M Granted party identity
Functional alias O Functional alias of the granted party identity Duration M
The time for which the granted party is allowed to transmit Source identifier
O Identifies the communication, e.g. by identifying the media flow within a
media multiplex, present only if media multiplexing Acknowledgement required O
Indicates if acknowledgement from the floor participant is required
* * *
#### 10.5.2.4 IWF floor rejected
Table 10.5.2.4-1 describes the information flow IWF floor rejected, from the
IWF to the MCPTT floor control server and from the MCPTT floor control server
to the IWF, which is used to indicate that a request for the floor is
rejected.
Table 10.5.2.4-1: IWF floor rejected
* * *
Information element Status Description MCPTT ID M Rejected party identity
Functional alias O Functional alias of the rejected party Source identifier O
Identifies the communication, e.g. by identifying the media flow within a
media multiplex, present only if media multiplexing Rejection cause O
Indicates the cause for floor rejection Acknowledgement required O Indicates
if acknowledgement from the floor participant is required
* * *
#### 10.5.2.5 IWF floor request cancel
Table 10.5.2.5-1 describes the information flow IWF floor request cancel, from
the IWF to the MCPTT floor control server and from the MCPTT floor control
server to the IWF, which is used to request cancelling the floor request from
the floor request queue.
Table 10.5.2.5-1: IWF floor request cancel
* * *
Information element Status Description MCPTT ID M Identity for the requester
Functional alias O Functional alias of the requester List of MCPTT IDs M
Target identity (Identities) whose floor request is to be cancelled Source
identifier O Identifies the communication, e.g. by identifying the media flow
within a media multiplex, present only if media multiplexing
* * *
#### 10.5.2.6 IWF floor request cancel response
Table 10.5.2.6-1 describes the information flow IWF floor request cancel
response, from the IWF to the MCPTT floor control server and from the MCPTT
floor control server to the IWF, which is used to indicate the response for
the floor request cancellation.
Table 10.5.2.6-1: IWF floor request cancel response
* * *
Information element Status Description MCPTT ID M Identity of party that
initiated the cancellation request Functional alias O Functional alias of the
requester Source identifier O Identifies the communication, e.g. by
identifying the media flow within a media multiplex, present only if media
multiplexing Acknowledgement required O Indicates if acknowledgement from the
floor participant is required
* * *
#### 10.5.2.7 IWF floor request cancel notify
Table 10.5.2.7-1 describes the information flow IWF floor request cancel
notify, from the IWF to the MCPTT floor control server and from the MCPTT
floor control server to the IWF, which is used to indicate the floor request
is cancelled by the administrator/floor control server.
Table 10.5.2.7-1: IWF floor request cancel notify
* * *
Information element Status Description MCPTT ID M Identity of the
administrator Functional alias O Functional alias of the administrator Source
identifier O Identifies the communication, e.g. by identifying the media flow
within a media multiplex, present only if media multiplexing Acknowledgement
required O Indicates if acknowledgement from the floor participant is required
* * *
#### 10.5.2.8 IWF floor idle
Table 10.5.2.8-1 describes the information flow IWF floor idle, from the IWF
to the MCPTT floor control server and from the MCPTT floor control server to
the IWF, which is used to indicate that a session is in idle status, i.e. the
floor is not granted to any party.
Table 10.5.2.8-1: IWF floor idle
* * *
Information element Status Description Source identifier O Identifies the
communication, e.g. by identifying the media flow within a media multiplex,
present only if media multiplexing Acknowledgement required O Indicates if
acknowledgement from the floor participant is required
* * *
#### 10.5.2.9 IWF floor release
Table 10.5.2.9-1 describes the information flow IWF floor release, from the
IWF to the MCPTT floor control server and from the MCPTT floor control server
to the IWF, which is used to indicate the media transfer is completed and the
floor is released.
Table 10.5.2.9-1: IWF floor release
* * *
Information element Status Description MCPTT ID M Identity of party that
released the floor Functional alias O Functional alias of the party that
released the floor Source identifier O Identifies the communication, e.g. by
identifying the media flow within a media multiplex, present only if media
multiplexing
* * *
#### 10.5.2.10 IWF floor taken
Table 10.5.2.10-1 describes the information flow IWF floor taken, from the IWF
to the MCPTT floor control server and from the MCPTT floor control server to
the IWF, which is used to indicate the floor is granted to another MCPTT user.
Table 10.5.2.10-1: IWF floor taken
* * *
Information element Status Description MCPTT ID M Identity for the granted
party Functional alias O Functional alias for the granted party Source
identifier O Identifies the communication, e.g. by identifying the media flow
within a media multiplex, present only if media multiplexing Permission to
request the floor O Indicates whether receiving parties are allowed to request
the floor or not (e.g. broadcast call). Acknowledgement required O Indicates
if acknowledgement from the floor participant is required Location O Location
information of the granted party
* * *
#### 10.5.2.11 IWF floor revoked
Table 10.5.2.11-1 describes the information flow IWF floor revoked, from the
IWF to the MCPTT floor control server and from the MCPTT floor control server
to the IWF, which is used to indicate the floor is revoked from its current
holder (the floor participant who was granted the floor).
Table 10.5.2.11-1: IWF floor revoked
* * *
Information element Status Description MCPTT ID M Revoked party identity
Functional alias O Functional alias of the revoked party Source identifier O
Identifies the communication, e.g. by identifying the media flow within a
media multiplex, present only if media multiplexing Acknowledgement required O
Indicates if acknowledgement from the floor participant is required
* * *
#### 10.5.2.12 IWF floor acknowledgement
Table 10.5.2.12-1 describes the information flow IWF floor acknowledgement,
from the IWF to the MCPTT floor control server and from the MCPTT floor
control server to the IWF, which is used to provide an acknowledgement if the
acknowledgement is required in the received floor control message.
NOTE: The floor acknowledgement flow can be sent by the floor control server
after each floor control information flow that includes an indication that an
acknowledgement is required.
Table 10.5.2.12-1: IWF floor acknowledgement
* * *
Information element Status Description MCPTT ID M Identity of the sender.
Functional alias O Functional alias of the sender
* * *
#### 10.5.2.13 IWF queue position request
Table 10.5.2.13-1 describes the information flow IWF queue position request,
from the IWF to the MCPTT floor control server and from the MCPTT floor
control server to the IWF, which is used to request the position in the floor
request queue. The MCPTT server and the MCPTT client that support queuing of
the floor control requests shall support this information flow.
Table 10.5.2.13-1: IWF queue position request
* * *
Information element Status Description MCPTT ID M Identity of party whose
floor position is requested Functional alias O Functional alias of the party
whose floor position is requested Source identifier O Identifies the
communication, e.g. by identifying the media flow within a media multiplex,
present only if media multiplexing
* * *
#### 10.5.2.14 IWF queue position info
Table 10.5.2.14-1 describes the information flow IWF queue position info, from
the IWF to the MCPTT floor control server and from the MCPTT floor control
server to the IWF, which is used to indicate the floor request is queued and
the queue position to the floor requesting UE.
Table 10.5.2.14-1: IWF queue position info
* * *
Information element Status Description MCPTT ID M Identity of party whose
floor position is provided Functional alias O Functional alias of the party
whose floor position is provided Queue position info M Position of the queued
floor request in the queue Source identifier O Identifies the communication,
e.g. by identifying the media flow within a media multiplex, present only if
media multiplexing Acknowledgement required O Indicates if acknowledgement
from the floor participant is required
* * *
#### 10.5.2.15 IWF unicast media stop request
Table 10.5.2.15-1 describes the information flow IWF unicast media stop
request, from the IWF to the MCPTT floor control server and from the MCPTT
floor control server to the IWF, which is used to indicate that the unicast
media flow of the designated communication does not need to be sent to the
client indicated by the MCPTT ID.
Table 10.5.2.15-1: IWF unicast media stop request
* * *
Information element Status Description MCPTT ID M Identity of the requester
Functional alias O Functional alias of the requester Source identifier O
Identifies the communication whose media flow is to be stopped, e.g. by
identifying the media flow within a media multiplex, present only if media
multiplexing
* * *
#### 10.5.2.16 IWF unicast media resume request
Table 10.5.2.16-1 describes the information flow IWF unicast media resume
request, from the IWF to the MCPTT floor control server and from the MCPTT
floor control server to the IWF, which is used by the floor control server to
request that the unicast media flow of the designated communication is to be
sent to the client indicated by the MCPTT ID.
Table 10.5.2.16-1: IWF unicast media resume request
* * *
Information element Status Description MCPTT ID M Identity of the requester
Functional alias O Functional alias of the requester Source identifier O
Identifies the communication whose media flow is to be resumed, e.g. by
identifying the media flow within a media multiplex, present only if media
multiplexing
* * *
#### 10.5.2.17 IWF floor talker ID update
Table 10.5.2.17-1 describes the information flow IWF floor talker ID update,
from the IWF to the MCPTT floor control server and from the MCPTT floor
control server to the IWF, which is used to indicate that the talker ID has
changed for the current MCPTT user granted the floor.
Table 10.5.2.17-1: IWF floor talker ID update
* * *
Information element Status Description MCPTT ID M Identity for the party using
the floor Functional alias O Functional alias associated with the MCPTT ID
using the floor Source identifier O Identifies the communication, e.g. by
identifying the media flow within a media multiplex, present only if media
multiplexing
* * *
### 10.5.3 Interworking floor control
3GPP TS 23.379 [7], subclause 10.9.1.4.1 describes floor control involving
groups in multiple MCPTT systems where floor control arbitration resides with
the primary MCPTT server and all floor control messages are routed to that
primary MCPTT server. The group is homed on the primary MCPTT server.
An interworking group can be homed on the MCPTT server or on the LMR system.
When the group is homed on the MCPTT server the floor control server is on
this MCPTT server. When the group is homed on the LMR system the floor control
server is represented by the IWF.
The primary MCPTT system of an MCPTT group is defined by configuration and
identified by the MC service group ID.
3GPP TS 23.379 [7], subclause 10.9.1.4.2 describes floor control involving
groups in multiple MCPTT systems where the partner MCPTT system filters its
MCPTT users\' floor requests before communicating with the floor control
server of the primary MCPTT system. When an MCPTT system is interworking with
an IWF, depending on where the group is homed the MCPTT server, or the IWF can
filter floor control requests in the same way as an interconnected MCPTT
system.
### 10.5.4 Floor override without using floor revoked on an interworking group
This procedure describes the case where a transmitting radio cannot be
signalled that the floor has been taken or revoked. Within the context of
interworking between MCPTT and LMR systems, this condition can occur due to
both MCPTT and LMR users obtaining the floor simultaneously, or the floor
granted to an LMR user is taken by an MCPTT user.
Figure 10.5.4‑1 shows the high-level procedure where an MCPTT session is
already established between the floor participants (with floor granted to an
LMR user represented by the IWF) and the floor control server (with an
override based on priority and configured to permit the transmission of
overridden floor participant from the IWF). The group is defined in the MCPTT
system and the MCPTT Server is the floor control server. Only two UEs involved
in the session are shown for simplicity.
Pre-conditions:
1\. The MCPTT floor control server has been configured to support override.
2\. The override supported in this case permits both the overridden floor
participant and the overriding floor participant to be transmitting.
3\. An MCPTT session is established between an MCPTT client, the interworked
system, and MCPTT server.
4\. Session is ongoing.
Figure 10.5.4‑1: Floor override (overridden continues to transmit) during an
interworking session
1\. It is assumed that the floor participant B (represented by the IWF in
figure 10.5.4‑1) has been given the floor and is transmitting voice media.
2\. Floor participant A, having a floor priority which is relatively higher
than that of floor participant B, wants to send voice media over the session.
3\. Floor participant A sends a floor request message to the floor control
server.
4\. The floor control server determines to accept the floor request from floor
participant A based on arbitration result e.g., according to the floor
priority information that is received in the floor request message.
5a. Floor control server responds with a floor granted message to floor
participant A.
5b. Floor control server sends a floor taken message to the other floor
participants (via the IWF). Floor participant B continues transmitting the
(overridden) voice media transmission.
NOTE 1: All other floor participants (not shown) that are part of this group
call receive a floor taken message, so that the other floor participants learn
who the newly granted talker (overriding) is.
6a. The floor granted causes the user of floor participant A to be notified.
6b. Floor participant B cannot be notified of the status because it is unable
to receive the message and continues transmitting.
7\. Floor participant A (overriding) starts sending voice media over the
session established beforehand.
NOTE 2: Floor participant B is still sending voice (overridden). The list of
floor participants that receive the overriding, overridden, or both
transmissions is based on configuration.
NOTE 3: When floor participant A stops transmitting, if floor participant B is
still sending voice, then the floor is granted back to floor participant B and
audio is routed to all current floor participants.
### 10.5.5 Floor control on an interworking group homed in the LMR system
Figure 10.5.5‑1 shows the procedure for floor control on an interworking group
homed in the LMR system. Simultaneous floor requests are included to show
various aspects of interworking floor control.
Pre-conditions:
1\. The interworking group is homed in the LMR system.
2\. The MCPTT server is configured to locally filter competing floor control
requests before communicating with the IWF.
3\. MCPTT client 1, MCPTT client 2, and LMR users (represented by the IWF) are
affiliated to that group.
4\. An interworking group call is ongoing involving MCPTT users and LMR users
(represented by the IWF). The floor is currently idle.
Figure 10.5.5-1: Floor control on a group homed in the LMR system
1\. The users of MCPTT Client 1 and MCPTT Client 2 both want to send voice
media over the session.
2\. MCPTT Clients 1 and 2 send floor request messages to the floor control
server.
3\. The MCPTT floor control server determines to accept the floor request from
MCPTT Client 1 based on local arbitration results (e.g., according to priority
information versus the competing request from MCPTT client 2).
4\. The user of MCPTT client 2 is notified that their floor request was
rejected.
5\. Since the group is homed in the LMR system the MCPTT floor control server
forwards the floor request to the IWF for final floor control determination.
The IWF performs floor arbitration in conjunction with the LMR system (not
shown). The IWF determines that the floor can be granted to the MCPTT user.
6\. The IWF sends a floor granted message to the MCPTT floor control server.
7\. The MCPTT floor control server sends a floor granted message to MCPTT
client 1.
8\. The MCPTT floor control server sends a floor taken message to MCPTT client
2 to notify the user of who is granted the floor.
9\. MCPTT Client 1 notifies the user that he/she has been granted the floor
and may begin speaking.
10\. MCPTT Client 1 begins sending voice media over the established session.
The media is distributed to affiliated group members including the IWF.
### 10.5.6 Floor control on an interworking group homed in the MCPTT system
Figure 10.5.6‑1 shows the procedure for floor control on an interworking group
homed in the MCPTT system, and the LMR system is configured for local floor
control request filtering. Simultaneous floor requests are included to show
various aspects of interworking floor control.
Pre-conditions:
1\. The interworking group is homed in the MCPTT system.
2\. The interworking group is previously defined on the group management
server.
3\. MCPTT client 1, MCPTT client 2, and LMR users (represented by the IWF) are
affiliated to that group.
4\. An interworking group call is ongoing involving MCPTT users and LMR users
(represented by the IWF). The floor is currently idle.
Figure 10.5.6-1: Floor control on a group homed in the MCPTT system
1\. The user of MCPTT Client 1 wants to send voice media over the session. At
the same time a user in the LMR system (represented by the IWF) wants to also
send voice media over the session.
2\. MCPTT Client 1 sends a floor request message to the MCPTT floor control
server.
3\. The IWF sends a floor request message to the MCPTT floor control server.
NOTE: If multiple LMR users want to speak, it is assumed that the LMR system
has arbitrated these requests based on local policies and only presents one
floor request to the MCPTT system.
4\. Since the group is homed in the MCPTT system the MCPTT floor control
server performs final floor control determination. In this case the MCPTT
floor control server determines to accept the floor request from MCPTT Client
1 based on local policy and arbitration results (e.g., according to time of
arrival of the request versus the competing request from the IWF).
5\. The IWF is notified that its floor request was rejected.
6\. The MCPTT floor control server sends a floor granted message to MCPTT
client 1.
7\. The MCPTT floor control server sends a floor taken message to both MCPTT
client 2 and the IWF to inform them of who is granted the floor.
8\. MCPTT Client 1 notifies the user that he/she has been granted the floor
and may begin speaking.
9\. MCPTT Client 1 begins sending voice media over the established session.
The media is distributed to affiliated group members including the IWF.
### 10.5.7 Floor control without local filtering on an interworking group
defined in the LMR system
Figure 10.5.7‑1 shows the procedure for floor control on an interworking group
defined in the LMR system where local filtering is not performed by the MCPTT
server. Simultaneous floor requests are included to show various aspects of
interworking floor control.
Pre-conditions:
1\. The interworking group is defined in the LMR system.
2\. The MCPTT system is configured to send competing floor control requests to
the LMR system (represented by the IWF) for floor control arbitration.
3\. MCPTT client 1, MCPTT client 2, and LMR users are affiliated to that
group.
4\. An interworking group call is ongoing involving MCPTT users and LMR users.
The floor is currently idle.
Figure 10.5.7-1: Floor control without local filtering on a group defined in
the LMR system
1\. The users of MCPTT client 1 and MCPTT client 2 both want to send voice
media over the session.
2\. MCPTT clients 1 and 2 send floor request messages to the MCPTT floor
control server.
3\. Since the group is defined in the LMR system the MCPTT floor control
server forwards these floor requests to the IWF for final floor control
determination. The IWF performs floor arbitration in conjunction with the LMR
system (not shown). The IWF determines that the floor can be granted to MCPTT
client 1.
4\. The IWF sends an IWF floor granted message for MCPTT client 1, an IWF
floor rejected message for MCPTT client 2, and an IWF floor taken message for
MCPTT client 2 to the MCPTT floor control server.
NOTE: If other MCPTT clients are affiliated to this group, the IWF sends an
IWF floor taken message to the MCPTT floor control server for each one of
them.
5\. The MCPTT floor control server sends a Floor rejected message to MCPTT
client 2 to notify the user that his/her floor request was rejected.
6\. The MCPTT floor control server sends a Floor granted message to MCPTT
client 1.
7\. The MCPTT floor control server sends a Floor taken message to MCPTT client
2 to notify the user of who is granted the floor.
8\. MCPTT client 1 notifies the user that he/she has been granted the floor
and may begin speaking.
9\. MCPTT client 1 begins sending voice media over the established session.
The media is distributed to affiliated group members including the IWF.
### 10.5.8 Floor control without local filtering on an interworking group
defined in the MCPTT system
Figure 10.5.8‑1 shows the procedure for floor control on an interworking group
defined in the MCPTT system where local filtering is not performed by the LMR
system. Simultaneous floor requests are included to show various aspects of
interworking floor control.
Pre-conditions:
1\. The interworking group is defined in the MCPTT system.
2\. MCPTT client 1, MCPTT client 2, and LMR users are affiliated to that
group.
3\. The LMR system (represented by the IWF) is configured to send all
competing floor control requests to the MCPTT system for floor control
arbitration.
4\. The IWF is not affiliating on behalf of LMR users. All LMR group
affiliations are passed through the IWF to the MCPTT server.
5\. An interworking group call is ongoing involving MCPTT users and LMR users.
The floor is currently idle.
Figure 10.5.8-1: Floor control without local filtering on a group defined in
the MCPTT system
1\. The user of MCPTT client 1 wants to send voice media over the session. At
the same time multiple users in the LMR system (represented by the IWF) want
to also send voice media over the session.
2\. MCPTT client 1 sends a floor request message to the MCPTT floor control
server.
3\. The IWF sends floor request messages to the MCPTT floor control server for
each LMR user requesting the floor. In this case two LMR users are requesting
the floor. These floor requests contain the MCPTT ID of the LMR user
(converted by the IWF).
4\. Since the group is defined in the MCPTT system the MCPTT floor control
server performs final floor control determination. In this case the MCPTT
floor control server determines to accept the floor request from MCPTT client
1 based on local policy and arbitration results (e.g., according to priority
of the request versus the competing requests from the IWF).
5\. The IWF is notified that its floor requests were rejected. The MCPTT floor
control server sends an IWF floor rejected message to the IWF for each floor
request.
6\. The MCPTT floor control server sends a floor granted message to MCPTT
client 1.
7\. The MCPTT floor control server sends floor taken messages to MCPTT client
2 and the IWF to inform them of who is granted the floor. In this case a floor
taken message is sent to the IWF corresponding to each affiliated LMR user.
NOTE: If the IWF has affiliated to this group on behalf of the group\'s LMR
users, only one IWF floor taken message is sent to the IWF.
8\. MCPTT client 1 notifies the user that he/she has been granted the floor
and may begin speaking.
9\. MCPTT client 1 begins sending voice media over the established session.
The media is distributed to affiliated group members including the LMR users.
## 10.6 Emergency and imminent peril
### 10.6.1 Information flows for emergency and imminent peril
#### 10.6.1.1 IWF emergency group call request
Table 10.6.1.1-1 describes the information flow IWF emergency group call
request from the IWF to the MCPTT server and from the MCPTT server to the IWF.
Table 10.6.1.1-1: IWF emergency group call request information elements
* * *
Information Element Status Description MCPTT ID M The identity of the calling
party MCPTT group ID M The MCPTT group ID on which the call is to be conducted
Emergency indicator M Indicates that the group call request is an MCPTT
emergency call Alert indicator O May be used to indicate that an emergency
alert is to be sent Location O Location, if available Implicit floor request
(see NOTE) O Indicates that the originating client requests the floor NOTE:
This element shall be included only when the originating client requests the
floor.
* * *
#### 10.6.1.2 IWF emergency group call response
Table 10.6.1.2-1 describes the information flow IWF emergency group call
response from the MCPTT server to the IWF and from the IWF to the MCPTT
server.
Table 10.6.1.2-1: IWF emergency group call response information elements
* * *
Information Element Status Description MCPTT ID M The identity of the calling
party MCPTT group ID M The MCPTT group ID on which the call is to be conducted
Result M The IWF emergency group call request may be rejected.
* * *
#### 10.6.1.3 IWF imminent peril group call request
Table 10.6.1.3-1 describes the information flow IWF imminent peril group call
request from the IWF to the MCPTT server and from the MCPTT server to the IWF.
Table 10.6.1.3-1: IWF imminent peril group call request information elements
* * *
Information Element Status Description
MCPTT ID M The identity of the calling party
MCPTT group ID M The MCPTT group ID on which the call is to be conducted
Imminent peril indicator M Indicates that the group call request is an
imminent peril call
Location O Location, if available
Implicit floor request\ O Indicates that the originating client requests the
floor (see NOTE)
NOTE: This element shall be included only when this information flow is from
the client to the server and the originator requests the floor.
* * *
#### 10.6.1.4 IWF imminent peril group call response
Table 10.6.1.4-1 describes the information flow IWF imminent peril group call
response from the IWF to the MCPTT server and from the MCPTT server to the
IWF.
Table 10.6.1.4-1: IWF imminent peril group call response information elements
* * *
Information Element Status Description MCPTT ID M The identity of the calling
party MCPTT group ID M The MCPTT group ID on which the call is to be conducted
Result M The IWF imminent peril group call request may be rejected.
* * *
#### 10.6.1.5 IWF in-progress imminent peril group state cancel request
Table 10.6.1.5-1 describes the information flow IWF in-progress imminent peril
group state cancel request from the MCPTT server to the IWF.
Table 10.6.1.5-1: IWF in-progress imminent peril group state cancel request
information elements
* * *
Information Element Status Description MCPTT ID M The identity of the
cancelling party MCPTT group ID M The MCPTT group ID on which the in-progress
imminent peril state is to be cancelled
* * *
#### 10.6.1.6 IWF in-progress imminent peril group state cancel response
Table 10.6.1.6-1 describes the information flow IWF in-progress imminent peril
group state cancel response from the IWF to the MCPTT server.
Table 10.6.1.6-1: IWF in-progress imminent peril group state cancel response
information elements
* * *
Information Element Status Description MCPTT ID M The identity of the
cancelling party MCPTT group ID M The MCPTT group ID on which the in-progress
imminent peril state is to be cancelled
* * *
#### 10.6.1.7 IWF emergency alert request
Table 10.6.1.7-1 describes the information flow IWF emergency alert request
from the IWF to the MCPTT server and from the MCPTT server to the IWF.
Table 10.6.1.7-1: IWF emergency alert request information elements
* * *
Information Element Status Description MCPTT ID M The identity of the alerting
party MCPTT group ID M The MCPTT group ID with which the alert is associated
Organization name O The alerting MCPTT user\'s mission critical organization
name. Location O The alerting MCPTT client\'s location
* * *
#### 10.6.1.8 IWF emergency alert response
Table 10.6.1.8-1 describes the information flow IWF emergency alert response
from the IWF to the MCPTT server and from the MCPTT server to the IWF.
Table 10.6.1.8-1: IWF emergency alert response information elements
* * *
Information Element Status Description MCPTT ID M The identity of the alerting
party MCPTT group ID M The MCPTT group ID with which the alert is associated
* * *
#### 10.6.1.9 IWF emergency alert cancel request
Table 10.6.1.9-1 describes the information flow IWF emergency alert cancel
request from the IWF to the MCPTT server and from the MCPTT server to the IWF.
Table 10.6.1.9-1: IWF emergency alert cancel request information elements
* * *
Information Element Status Description MCPTT ID M MCPTT user identity of the
cancelling party MCPTT ID (see NOTE) O MCPTT user identity whose emergency
alert is to be cancelled MCPTT group ID M The MCPTT group ID with which the
alert is associated Group\'s in-progress emergency alert cancel request O
Requests cancellation of the in-progress emergency alert of the group NOTE:
This information shall be present if the message is requesting cancellation of
another MCPTT user\'s alert. If not present, then the alert of the MCPTT ID of
the cancelling party is being cancelled
* * *
#### 10.6.1.10 IWF emergency alert cancel response
Table 10.6.1.10-1 describes the information flow IWF emergency alert cancel
response from the IWF to the MCPTT server and from the MCPTT server to the
IWF.
Table 10.6.1.10-1: IWF emergency alert cancel response information elements
* * *
Information Element Status Description MCPTT ID M The identity of the
cancelling party MCPTT group ID M The MCPTT group ID with which the alert is
associated
* * *
#### 10.6.1.11 IWF in-progress emergency group state cancel request
Table 10.6.1.11-1 describes the information flow IWF in-progress emergency
group state cancel request from the IWF to the MCPTT server and from the MCPTT
server to the IWF.
Table 10.6.1.11-1: IWF in-progress emergency group state cancel request
information elements
* * *
Information Element Status Description MCPTT ID M The identity of the
cancelling party MCPTT group ID M The MCPTT group ID on which the MCPTT in-
progress emergency state is to be cancelled. Alert indicator O Indicates
whether the emergency alert of the cancelling party is to be cancelled
* * *
#### 10.6.1.12 IWF in-progress emergency group state cancel response
Table 10.6.1.12-1 describes the information flow IWF in-progress emergency
group state cancel response from the MCPTT server to the IWF and from IWF to
MCPTT server.
Table 10.6.1.12-1: IWF in-progress emergency group state cancel response
information elements
* * *
Information Element Status Description MCPTT ID M The identity of the
cancelling party MCPTT group ID M The MCPTT group ID on which the MCPTT in-
progress emergency in-progress is to be cancelled.
* * *
### 10.6.2 Emergency calls
#### 10.6.2.1 General
This subclause addresses various aspects of emergency call interworking.
Where the group is defined in the MCPTT system and where the IWF has
affiliated to an MCPTT group with a single affiliation on behalf of all LMR
group members, only a single IWF emergency group call request / IWF in-
progress emergency group state cancel request message is sent to the IWF at
the commencement / release of an emergency group call. Where the group is
defined in the MCPTT system and where the IWF has passed through individual
affiliations for each group member in the LMR system, the MCPTT system shall
send individual IWF emergency group call request / IWF in-progress emergency
group state cancel request messages to the IWF for all affiliated group
members in the LMR system in accordance with primary and partner MCPTT system
behaviour. In both cases, the distribution of the messages to group members in
the LMR system is out of scope of the present document.
Where the group is defined in the LMR system, the IWF shall send individual
IWF emergency group call request / IWF in-progress emergency group state
cancel request messages to the IWF for all affiliated MCPTT group members in
accordance with primary and partner MCPTT system behaviour.
#### 10.6.2.2 Emergency group call
##### 10.6.2.2.1 Emergency group call setup initiated by a user in the LMR
system on an interworking group defined in the MCPTT system
Figure 10.6.2.2.1‑1 shows the procedure for an emergency group call setup
initiated by a user in the LMR system. The figure is based upon the figure for
emergency calls in 3GPP TS 23.379 [7], subclause 10.6.2.6.1.1. This scenario
assumes that the group is an interworking group defined in the MCPTT system.
NOTE 1: For simplicity, a single MCPTT server is shown in place of a user home
MCPTT server and a group hosting MCPTT server.
NOTE 2: The emergency interworking call procedures reuse the information flows
defined 3GPP TS 23.379 [7].
Pre-conditions:
1\. The MCPTT group is an interworking group defined in the MCPTT system
2\. MCPTT client 1 and MCPTT client 2 are affiliated to that MCPTT group.
3\. The IWF is connected to and is authorized to interwork with the MCPTT
system.
4\. The mapping relationship of group and user identities between MCPTT system
and LMR system has been configured at the IWF.
5\. LMR user initiates an emergency group call.
Figure 10.6.2.2.1-1: Emergency group call setup, initiated by LMR user on an
interworking group defined in the MCPTT system
1\. The IWF sends an IWF emergency group call request including a MCPTT group
ID to the MCPTT server. The request contains an indication of the MCPTT
emergency. The IWF may indicate in its request that an MCPTT emergency alert
is to be sent when initiating an MCPTT emergency group call. The request may
contain an indication of an implicit floor request.
2\. The MCPTT server implicitly affiliates the MCPTT ID of the LMR user to the
MCPTT emergency group if the user is not already affiliated. If the IWF is
configured to affiliate on behalf of all of its group members in a single
affiliation step, the MC service server affiliates the IWF instead of an
individual MC service ID.
3\. The MCPTT server checks whether the MCPTT ID of the LMR user is authorized
for initiation of MCPTT emergency calls on the indicated MCPTT group. If
authorized, it resolves the MCPTT group ID to determine the members of that
MCPTT group and their affiliation status.
4\. The MCPTT server configures the priority of the underlying bearers for all
MCPTT participants in the MCPTT group. All successive calls during the MCPTT
group\'s in-progress emergency state will receive the adjusted bearer
priority.
5\. The MCPTT server records the emergency state of the group. Once an MCPTT
emergency call has been initiated, the MCPTT group is in an in-progress
emergency state until that state is cancelled.
NOTE 3: The IWF actions for priority are out of scope of the present document.
6\. MCPTT server sends the MCPTT emergency group call request towards the
MCPTT clients of each of those affiliated MCPTT group members as defined in
3GPP TS 23.379 [7].
7\. If the group has other affiliated LMR users than the calling party and the
MCPTT server has received individual affiliations from those LMR users, an
individual IWF emergency group call request is sent (to the IWF) for each
affiliated LMR user.
8\. The IWF returns IWF emergency group call response(s) to the MCPTT server.
9\. The MCPTT server sends the IWF emergency group call response to the IWF
(as a response to the request received in step 1) to inform of the successful
MCPTT emergency group call establishment.
NOTE 4: How the LMR group members are called within the LMR system is out
scope of the present document.
NOTE 5: Step 9 can occur at any time following step 5, but at the latest
following step 8 depending on the conditions to proceed with the call.
10\. The LMR users via the IWF and the affiliated MCPTTs have successfully
established media plane for communication. The MCPTT system where the
interworking group is defined is the controlling system of the group call.
##### 10.6.2.2.2 Emergency group call setup initiated by a user in the MCPTT
system on an interworking group defined in MCPTT system
Figure 10.6.2.2.2‑1 shows the procedure for an emergency group call setup
initiated by a user in the MCPTT system. The figure is based upon the figure
for emergency group call in 3GPP TS 23.379 [7], subclause 10.6.2.6.1.1. This
scenario assumes that the MCPTT group is an interworking group defined in the
MCPTT system.
NOTE 1: For simplicity, a single MCPTT server is shown in place of a user home
MCPTT server and a group hosting MCPTT server.
NOTE 2: The emergency interworking group call procedures reuse the information
flows defined 3GPP TS 23.379 [7].
Pre-conditions:
1\. The MCPTT group is an interworking group defined in the MCPTT system.
2\. MCPTT client 2 is affiliated to the MCPTT group.
3\. The IWF is connected to and is authorized to interwork with the MCPTT
system.
4\. The mapping relationship of group and user identities between MCPTT system
and LMR system has been configured at the IWF.
5\. The initiating MCPTT client 1 has been provisioned with the MCPTT group
that has been designated via provisioning as the MCPTT emergency group.
NOTE 3: Alternatively, the client could have been provisioned for emergency
behaviour on the selected group.
Figure 10.6.2.2.2-1: Emergency group call setup, initiated by MCPTT user on an
interworking group defined in the MCPTT system
1\. An MCPTT user initiates an emergency group call. MCPTT client 1 sets its
MCPTT emergency state. The MCPTT emergency state is retained until explicitly
cancelled.
2\. The MCPTT client sends an MCPTT emergency group call request to the MCPTT
server. The request contains an indication of the MCPTT emergency. The MCPTT
client may indicate in its request that an MCPTT emergency alert is to be sent
when initiating an MCPTT emergency group call. The request may contain an
indication of an implicit floor request.
3\. The MCPTT server implicitly affiliates MCPTT client 1 to the emergency
group if the client is not already affiliated.
4\. The MCPTT server checks whether the MCPTT user of the MCPTT client 1 is
authorized for initiation of MCPTT emergency calls on the indicated
interworking group. If authorized, it resolves the MCPTT group ID to determine
the members of that MCPTT group and their affiliation status.
5\. The MCPTT server configures the priority of the underlying bearers for all
participants in the MCPTT group.
NOTE 4: Successive calls during the group\'s in-progress emergency state will
all receive the adjusted bearer priority.
6\. The MCPTT server records the in-progress emergency state of the group. The
MCPTT server also records the identity of the MCPTT user that initiated the
MCPTT emergency group call until the MCPTT emergency is cancelled. Once an
MCPTT emergency group call has been initiated, the MCPTT group is considered
to be in an in-progress emergency state until that state is cancelled.
7\. The MCPTT server sends an IWF emergency group call request to IWF. If the
IWF has affiliated to this group on behalf of the group\'s LMR users, only one
IWF emergency group call request message is sent to the IWF. If the MCPTT
server has received individual affiliations from the group\'s LMR users, an
individual IWF emergency group call request is sent (to the IWF) for each
affiliated LMR user.
8\. IWF responds with the IWF emergency group call response(s) to MCPTT server
to inform of the successful MCPTT emergency call establishment.
NOTE 5: How the LMR group members are called within the LMR system is out of
scope of the present document.
NOTE 6: Steps 7 to 8 can occur at any time between steps 5 and 10.
NOTE 7: IWF actions for priority are out of scope of the present document.
9\. The MCPTT server sends the MCPTT emergency group call request towards the
MCPTT clients of each of those affiliated MCPTT group members as defined in
3GPP TS 23.379 [7].
10\. The MCPTT server sends an MCPTT emergency group call response to the
MCPTT client to inform of the successful MCPTT emergency call establishment.
NOTE 8: Step 10 can occur at any time following step 8, but at the latest
following step 9, depending on the conditions to proceed with the call.
11\. The LMR users via the IWF and the affiliated MCPTT clients have
successfully established media plane for communication. The MCPTT system where
the interworking group is defined is the controlling system of the group call.
##### 10.6.2.2.3 Emergency group call setup initiated by a user in the LMR
system on an interworking group defined in the LMR system
Figure 10.6.2.2.3‑1 shows the procedure for an emergency group call setup
initiated by a user in the LMR system. The figure is based upon the figure for
emergency group call in 3GPP TS 23.379 [7], subclause 10.6.2.6.1.1. This
scenario assumes that the MCPTT group is an interworking group defined in the
LMR system.
NOTE 1: The emergency interworking group call procedures reuse the information
flows defined 3GPP TS 23.379 [7].
Pre-conditions:
1\. The MCPTT group is an interworking group defined in the LMR system.
2\. MCPTT client 1 and MCPTT client 2 are affiliated to that group.
3\. The IWF is connected to and is authorized to interwork with the MCPTT
system.
4\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
5\. LMR user initiates an emergency group call.
Figure 10.6.2.2.3-1: Emergency group call setup, initiated by LMR user on an
interworking group defined in the LMR system
1\. The IWF sends an IWF emergency group call request(s) to the MCPTT server.
An emergency group call request is sent individually for each affiliated MCPTT
user in the group. The request contains an indication of the MCPTT emergency.
NOTE 2: IWF actions for priority are out of scope of the present document.
2\. The MCPTT server configures the priority of the underlying bearers and
sends the MCPTT emergency group call request(s) as defined in 3GPP TS 23.379
[7].
NOTE 3: Successive calls during the MCPTT group\'s in-progress emergency state
will all receive the adjusted bearer priority.
3\. The MCPTT clients respond with MCPTT emergency group call response to the
MCPTT server.
4\. The MCPTT server sends the IWF emergency group call response(s) to the IWF
to inform of the successful MCPTT emergency call establishment.
NOTE 4: How the LMR group members are called within the LMR system is out of
scope of the present document.
5\. The LMR users via the IWF and the affiliated MCPTT clients have
successfully established media plane for communication. The LMR system where
the interworking group is defined is the controlling system of the group call.
##### 10.6.2.2.4 Emergency group call setup initiated by a user in the MCPTT
system to an interworking group defined in the LMR system
Figure 10.6.2.2.4‑1 shows the procedure for an emergency group call initiated
by a user in the MCPTT system. The figure is based upon the figure for MCPTT
emergency group call in 3GPP TS 23.379 [7], subclause 10.6.2.6.1.1. This
scenario assumes that the MCPTT group is an interworking group defined in the
LMR system.
NOTE 1: The emergency interworking group call procedures reuse the information
flows defined 3GPP TS 23.379 [7].
Pre-conditions:
1\. The MCPTT group is an interworking group defined in the LMR system.
2\. MCPTT client 2 is affiliated to the MCPTT group.
3\. The IWF is connected to and is authorized to interwork with the MCPTT
system.
4\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
Figure 10.6.2.2.4-1: Emergency group call setup, initiated by MCPTT user to an
interworking group defined in the LMR system
1\. An MCPTT user initiates an emergency group call.
2\. The MCPTT client sends an MCPTT emergency group call request to the MCPTT
server. The request contains an indication of the MCPTT emergency. The MCPTT
client may indicate in its request that an MCPTT emergency alert is to be sent
when initiating an MCPTT emergency group call. The request may contain an
indication of an implicit floor request.
3\. The MCPTT server configures the priority of the underlying bearer and
sends an IWF emergency group call request to the IWF.
4\. The IWF sends an individual IWF emergency group call request to the MCPTT
server for each affiliated MCPTT group member, in this example to a user in
MCPTT client 2.
NOTE 2: How the LMR group members are called within the LMR system is outside
the scope of the present document.
NOTE 3: All successive calls during the MCPTT group\'s in-progress emergency
state will receive the adjusted bearer priority.
NOTE 4: IWF actions for priority are out of scope of the present document.
5\. The MCPTT server configures the priority of the underlying bearer and
sends an MCPTT emergency group call request towards the MCPTT clients as
defined in 3GPP TS 23.379 [7].
6\. The MCPTT client responds with MCPTT emergency group call response, as
defined in 3GPP TS 23.379 [7].
7\. The MCPTT server responds to the IWF emergency group call request(s),
received in step 4, with IWF emergency group call response(s).
8\. The IWF sends an IWF emergency group call response to the MCPTT server, as
a response to the request received in step 3, to inform of the successful
MCPTT emergency group call establishment.
9\. The MCPTT server sends MCPTT emergency group call response to the
initiating user in MCPTT client 1.
NOTE 5: Step 8 can occur at any time following step 3, but at the latest
following step 7.
10\. The LMR users (via the IWF) and the affiliated MCPTT clients have
successfully established media plane for communication. The LMR system where
the interworking group is defined is the controlling system of the group call.
#### 10.6.2.3 In-progress emergency group state cancel of an interworking
group
##### 10.6.2.3.1 LMR user initiated in-progress emergency group state cancel
of an interworking group defined in the MCPTT system
Figure 10.6.2.3.1‑1 shows the procedure for an in-progress emergency group
state cancel initiated by an LMR user. The figure is based upon the figure for
MCPTT in-progress emergency group state cancel in 3GPP TS 23.379 [7],
subclause 10.6.2.6.1.3.
NOTE 1: For simplicity, a single MCPTT server is shown in place of a user home
MCPTT server and a group hosting MCPTT server.
NOTE 2: The information flows between MCPTT client and MCPTT server are
defined 3GPP TS 23.379 [7].
NOTE 3: The end of an MCPTT emergency group call does not cancel the MCPTT
group\'s in-progress emergency group state. It is explicitly cancelled by an
authorized user by this procedure.
Pre-conditions:
1\. The MCPTT group is in an in-progress emergency group state.
2\. The MCPTT group is an interworking group defined in the MCPTT system.
3\. The MCPTT client is affiliated to the MCPTT group.
4\. The IWF is connected to and is authorized to interwork with the MCPTT
system.
5\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
6\. An LMR user initiates in-progress emergency group state cancel of an
interworking group.
Figure 10.6.2.3.1-1: LMR user initiated in-progress emergency group state
cancel of an interworking group defined in the MCPTT system
1\. The IWF sends an IWF in-progress emergency group state cancel request to
the MCPTT server. The IWF in-progress emergency group state cancel request may
carry an indication that the emergency alert of the user is also being
cancelled.
2\. The MCPTT server checks that the initiator of the request is authorized to
cancel the in-progress emergency group state of the group.
3\. The MCPTT server cancels the in-progress emergency group state of the
MCPTT group. If the emergency alert of the user is also requested to be
cancelled, the MCPTT server cancels the emergency alert of the user.
4\. The MCPTT server adjusts the priority of the underlying bearer; priority
treatment is no longer required.
5\. The MCPTT server handles the MCPTT in-progress emergency group state
cancel request towards the affiliated MCPTT clients as defined in 3GPP TS
23.379 [7], subclause 10.6.2.6.1.3.
6\. The MCPTT server sends an IWF in-progress emergency group state cancel
response to the IWF to confirm the IWF in-progress emergency group state
cancel request.
NOTE 4: Step 6 can occur at any time following step 3.
##### 10.6.2.3.2 MCPTT user initiated in-progress emergency group state cancel
of an interworking group defined in the MCPTT system
Figure 10.6.2.3.2‑1 shows the procedure for an in-progress emergency group
state cancel initiated by an MCPTT user. The figure is based upon the figure
for MCPTT in-progress emergency group state cancel in 3GPP TS 23.379 [7],
subclause 10.6.2.6.1.3.
NOTE 1: For simplicity, a single MCPTT server is shown in place of a user home
MCPTT server and a group hosting MCPTT server.
NOTE 2: The information flows between an MCPTT client and an MCPTT server are
defined 3GPP TS 23.379 [7].
NOTE 3: The end of the MCPTT emergency group call does not cancel the MCPTT
group\'s in-progress emergency group state. It is explicitly cancelled by an
authorized user by this procedure.
Pre-conditions:
1\. MCPTT group is in an in-progress emergency group state.
2\. The MCPTT group is an interworking group defined in the MCPTT system.
3\. MCPTT client 2 is affiliated to that MCPTT group.
4\. The IWF is connected to and is authorized to interwork with the MCPTT
system.
5\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
Figure 10.6.2.3.2-1: MCPTT user initiated in-progress emergency group state
cancel of an interworking group defined in MCPTT system
1\. The MC user of MCPTT client 1 initiates in-progress emergency group state
cancel of an interworking group.
2\. The MCPTT client sends an MCPTT in-progress emergency group state cancel
request to the MCPTT server. The request may carry an indication that the
emergency alert of the user is also being cancelled.
3\. The MCPTT server checks that the initiator of the request is authorised to
cancel the in-progress emergency group state of the group.
4\. The MCPTT server cancels the in-progress emergency group state of the
MCPTT group. If the emergency alert of the user is also requested to be
cancelled, the MCPTT server cancels the emergency alert of the user.
5\. The MCPTT server adjusts the priority of the underlying bearer; priority
treatment is no longer required.
6\. The MCPTT server sends the IWF in-progress emergency group state cancel
request to the IWF.
NOTE 4: IWF actions for cancelling in-progress emergency group state are out
of scope of the present document.
7\. The IWF sends the IWF in-progress emergency group state cancel response to
the MCPTT server to confirm the IWF in-progress emergency group state cancel
request.
8\. The MCPTT server handles the MCPTT in-progress emergency group state
cancel request towards the affiliated MCPTT clients as defined in 3GPP TS
23.379 [7], subclause 10.6.2.6.1.3.
9\. The MCPTT server sends the MCPTT in-progress emergency group state cancel
response to the MCPTT client 1 to confirm the MCPTT in-progress emergency
group state cancel request.
NOTE 5: Step 9 can occur at any time following step 4, depending on the
conditions to proceed with the call.
##### 10.6.2.3.3 LMR user initiated in-progress emergency group state cancel
of an interworking group defined in an LMR system
Figure 10.6.2.3.3‑1 shows the procedure for an in-progress emergency group
state cancel initiated by an LMR user.
NOTE 1: The information flows between MCPTT client and MCPTT server are
defined 3GPP TS 23.379 [7].
NOTE 2: The end of an MCPTT emergency group call does not cancel the MCPTT
group\'s in-progress emergency group state. It is explicitly cancelled by an
authorized user by this procedure.
Pre-conditions:
1\. MCPTT group is in an in-progress emergency group state.
2\. The MCPTT group is an interworking group defined in the LMR system.
3\. The MCPTT client is affiliated to the MCPTT group.
4\. The IWF is connected to and is authorized to interwork with the MCPTT
system.
5\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
6\. An LMR user initiates in-progress emergency group state cancel of an
interworking group.
Figure 10.6.2.3.3-1: LMR user initiated in-progress emergency group state
cancel of an interworking group defined in the LMR system
1\. The IWF sends an IWF in-progress emergency group state cancel request to
the MCPTT server.
2\. The MCPTT server adjusts the priority of the underlying bearer; priority
treatment is no longer required.
3\. The MCPTT server handles the MCPTT in-progress emergency group state
cancel request towards the affiliated MCPTT clients as defined in 3GPP TS
23.379 [7], subclause 10.6.2.6.1.3.
4\. The MCPTT server sends an IWF in-progress emergency group state cancel
response to the IWF to confirm the IWF in-progress emergency group state
cancel request.
NOTE 3: Step 4 can occur at any time following step 1, depending on the
conditions to proceed with the call.
##### 10.6.2.3.4 MCPTT user initiated in-progress emergency group state cancel
of an interworking group defined in an LMR system
Figure 10.6.2.3.4‑1 shows the procedure for an in-progress emergency group
state cancel initiated by an MCPTT user. The figure is based upon the figure
for MCPTT in-progress emergency group state cancel in 3GPP TS 23.379 [7],
subclause 10.6.2.6.1.3.
NOTE 1: The information flows between an MCPTT client and an MCPTT server are
defined 3GPP TS 23.379 [7].
NOTE 2: The end of the MCPTT emergency group call does not cancel the MCPTT
group\'s in-progress emergency group state. It is explicitly cancelled by an
authorized user by this procedure.
Pre-conditions:
1\. MCPTT group is in an in-progress emergency group state.
2\. The MCPTT group is an interworking group defined in the LMR system.
3\. MCPTT client 2 is affiliated to that MCPTT group.
4\. The IWF is connected to and is authorized to interwork with the MCPTT
system.
5\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
Figure 10.6.2.3.4-1: MCPTT user initiated in-progress emergency group state
cancel of an interworking group defined in the LMR system
1\. The MC user of MCPTT client 1 initiates in-progress emergency group state
cancel of an interworking group.
2\. An MCPTT client sends an MCPTT in-progress emergency group state cancel
request to the MCPTT server. The request may carry an indication that the
emergency alert of the user is also being cancelled.
3\. The MCPTT server sends the IWF in-progress emergency group state cancel
request to the IWF.
NOTE 3: IWF actions for checking authorization and cancelling in-progress
emergency group state are out of scope of the present document.
NOTE 4: The LMR system can also reject the request.
4\. The IWF sends the IWF in-progress emergency group state cancel response to
the MCPTT server to confirm the IWF in-progress emergency group state cancel
request.
5\. The MCPTT server adjusts the priority of the underlying bearer; priority
treatment is no longer required.
6\. The MCPTT server handles the MCPTT in-progress emergency group state
cancel request towards the affiliated MCPTT clients as defined in 3GPP TS
23.379 [7], subclause 10.6.2.6.1.3.
7\. The MCPTT server sends the MCPTT in-progress emergency group state cancel
response to the MCPTT client 1 to confirm the MCPTT in-progress emergency
group state cancel request.
NOTE 5: Step 7 can occur at any time following step 4, depending on the
conditions to proceed with the call.
#### 10.6.2.4 Losing audio
For LMR systems where a user cannot be pre-empted, the IWF identifies the
audio as losing audio to the system. Subclause 10.5 is applicable to losing
audio during emergency calls as well as non-emergency calls.
#### 10.6.2.5 Default emergency group
In MCPTT, the user\'s profile determines whether an emergency is raised on the
user\'s currently selected group or on a configured default emergency group.
It\'s up to the IWF and the LMR system to which it is connected to determine
what group the emergency is raised on and whether an alert is also sent when
the emergency is raised. From the perspective of the MCPTT system, all
emergency behavior by the IWF on behalf of its users mapped to MCPTT shall
comply with behaviors defined in 3GPP TS 23.379 [7]. The implementation shall
ensure that emergency related parameters of a group or private call are
adhered to. For example, an MC service group must be configured in the MC
sevice group managment system for emergency alerts in order for an emergency
alert to be sent on it. This can be enforced through proper configuration of
both LMR and MCPTT systems or can be enforced at run time by the IWF.
#### 10.6.2.6 Emergency private call
An emergency private call to an LMR user will have emergency priority for the
portion of the call transported in the MCPTT system and the LTE EPS but will
not receive priority on the LMR system in LMR systems that do not support
emergency treatment for private calls.
#### 10.6.2.7 LMR systems that do not track group emergencies
The MCPTT system tracks the emergency state of every group. In interworked LMR
systems that do not track the emergency state of groups, only a UE in
emergency state will be given emergency priority on the LMR system when
talking. For any user talking on an emergency group, the portion of the call
transported by the MCPTT system will receive emergency priority.
### 10.6.3 Imminent peril calls
#### 10.6.3.1 General
This subclause addresses various aspects of imminent peril call interworking.
LMR systems do not support imminent peril. Imminent peril calls can be
propagated into the LMR system by the IWF as normal group calls or emergency
group calls. The decision of the LMR group call type is outside the scope of
the present document.
Where the group is defined in the MCPTT system and where the IWF has
affiliated to an MCPTT group with a single affiliation on behalf of all LMR
group members, only a single IWF imminent peril group call request / IWF
imminent peril cancel request message is sent to the IWF at the commencement /
cancel of an imminent peril group call. Where the group is defined in the
MCPTT system and where the IWF has passed through individual affiliations for
each group member in the LMR system, the MCPTT system shall send individual
IWF imminent peril group call request / IWF imminent peril cancel request
messages to the IWF for all affiliated group members in the LMR system in
accordance with primary and partner MCPTT system behaviour. In both cases, the
distribution of the messages to group members in the LMR system is out of
scope of the present document.
Where the group is defined in the LMR system, the IWF shall send individual
IWF imminent peril group call request / IWF imminent peril cancel request
messages to the MCPTT server for all affiliated MCPTT group members in
accordance with primary and partner MCPTT system behaviour.
#### 10.6.3.2 Imminent peril group call initiated by an MCPTT user on an
interworking group
Figure 10.6.3.2‑1 shows the procedure for an imminent peril group call
initiated by a user in the MCPTT system. The figure is based upon the figure
for imminent peril group call in 3GPP TS 23.379 [7], subclause 10.6.2.6.2.1.
NOTE 1: For simplicity, a single MCPTT server is shown in place of a user home
MCPTT server and a group hosting MCPTT server.
NOTE 2: The imminent peril interworking group call procedures reuse the
information flows defined in 3GPP TS 23.379 [7].
Pre-conditions:
1\. The initiating MCPTT client 1 has been provisioned with an MCPTT group
that has been designated in the provisioning to be used for imminent peril
communications
2\. The MCPTT group is an interworking group defined in the MCPTT system.
3\. MCPTT client 2 is affiliated to the MCPTT group.
4\. The IWF is connected to, and is authorized to, interwork with the MCPTT
system.
5\. At least one LMR user has affiliated to the MCPTT group.
6\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
NOTE 3: For all the signalling messages passing through the IWF between the
MCPTT system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.6.3.2-1: Imminent peril group call initiated by a MCPTT user to an
interworking group defined in the MCPTT system
1\. An MCPTT user initiates an imminent peril group call.
2\. The MCPTT client sends an MCPTT imminent peril group call request to the
MCPTT server. The request contains an indication of the in-progress imminent
peril. The request may also contain an indication of an implicit floor request
and may also contain the location of the calling party.
3\. The MCPTT server implicitly affiliates MCPTT client 1 to the imminent
peril group if the client is not already affiliated.
4\. The MCPTT server checks whether the MCPTT user of MCPTT client 1 is
authorized for initiation of imminent peril group calls on the indicated
interworking group defined in the MCPTT system. If authorized, it resolves the
MCPTT group ID to determine the members of that MCPTT group and their
affiliation status. The MCPTT server also checks the privacy policy
(authorisation to provide location information to other MCPTT users on a call
when talking, as defined in 3GPP TS 23.379 [7] Annex A.3) of the requesting
MCPTT user to decide if the user\'s location information may be provided to
other MCPTT users on the call and the IWF.
5\. The MCPTT server configures the priority of the underlying bearers for all
participants in the MCPTT group.
NOTE 4: Successive calls during the in-progress imminent peril state will all
receive the adjusted bearer priority.
6\. The MCPTT server records the imminent peril state of the group. The MCPTT
server also records the identity of the MCPTT user that initiated the imminent
peril group call until the in-progress imminent peril state is cancelled. Once
an imminent peril group call has been initiated, the MCPTT group is considered
to be in an in-progress imminent peril state until that state is cancelled.
7\. The MCPTT server sends the IWF imminent peril group call request(s) to the
IWF. If the IWF has affiliated to this group on behalf of the group\'s LMR
users, only one IWF imminent peril group call request message is sent to the
IWF. If the MCPTT server has received individual affiliations from the
group\'s LMR users, an individual IWF imminent peril group call request is
sent to the IWF for each affiliated LMR user.
8\. The IWF responds with the IWF imminent peril group call response(s) to
MCPTT server to inform of the successful MCPTT imminent peril call
establishment.
NOTE 5: The IWF can reject the request if it does not support imminent peril
group calls. IWF actions for priority are out of scope of the present
document.
NOTE 6: How the LMR group members are called within the LMR system is out of
scope of the present document.
9\. The MCPTT server sends the imminent peril group call request towards the
MCPTT clients of each of those affiliated MCPTT group members. The request
contains an indication of the in-progress imminent peril. MCPTT users are
notified of the incoming imminent peril call. The MCPTT clients acknowledge
the imminent peril call request as specified in 3GPP TS 23.379 [7].
10\. The MCPTT server sends the MCPTT imminent peril group call response to
the MCPTT user 1 to inform the successful imminent peril call establishment.
NOTE 7: Step 10 can occur at any time following step 5, and prior to step 11
depending on the conditions to proceed with the imminent peril call.
11\. The LMR users via the IWF and the affiliated MCPTT clients have
successfully established the media plane for communication. The MCPTT system,
where the interworking group is defined, is the controlling system of the
group call.
#### 10.6.3.3 Group call initiated by a user in the LMR system on an
interworking group in imminent peril state
Figure 10.6.3.3‑1 shows the procedure for a group call initiated by an LMR
user (represented by the IWF) on an interworking group where the group is
currently in imminent peril state within the MCPTT system.
NOTE 1: For simplicity, a single MCPTT server is shown in place of a user home
MCPTT server and a group hosting MCPTT server.
NOTE 2: The imminent peril interworking group call procedures reuse the
information flows defined in 3GPP TS 23.379 [7].
Pre-conditions:
1\. The MCPTT group is previously defined on the group management server with
MCPTT client 1, MCPTT client 2, and LMR users (represented by the IWF)
affiliated to that MCPTT group.
2\. The IWF is connected to, and is authorized to interwork with, the MCPTT
system.
3\. The interworking group information is available at the IWF.
4\. The interworking group is currently in imminent peril state within the
MCPTT system.
5\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
6\. LMR user initiates a group call.
NOTE 3: For all the signalling messages passing through the IWF between the
MCPTT system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.6.3.3-1: Group call initiated by a user in the LMR system on an
interworking group in imminent peril state
1\. The IWF does not track the imminent peril state of the group and sends an
IWF group call request including an MCPTT group ID to the MCPTT server for
call establishment. If floor control is requested by the calling LMR user, an
indication of implicit floor request is included and the location information
of the requestor if required.
2\. The MCPTT server determines that the MCPTT group is currently in imminent
peril state.
3\. The MCPTT server converts the request and sends an MCPTT imminent peril
group call request to all of the affiliated MCPTT clients.
3a. If the group has other affiliated LMR users than the calling party and the
MCPTT server has received individual affiliations from those LMR users, an
individual IWF imminent peril group call request is sent to the IWF for each
affiliated LMR user.
4\. The receiving MCPTT clients send the MCPTT imminent peril group call
response to the MCPTT server to acknowledge the MCPTT imminent peril group
call request. For a multicast call, these acknowledgements are not sent.
4a. The IWF returns IWF imminent peril group call response(s) to the MCPTT
server.
5\. The MCPTT server sends the IWF imminent peril group call response message
to the IWF.
6\. The LMR users (via the IWF) and the affiliated MCPTT clients have
successfully established the media plane for communication. The MCPTT system
where the interworking group is defined is the controlling system of the group
call.
The IWF, MCPTT client 1, and MCPTT client 2 continue with the MCPTT group
call, which receives adjusted bearer priority within the MCPTT system due to
the MCPTT group being in imminent peril state.
NOTE 4: IWF actions for priority are out of scope of the present document.
#### 10.6.3.4 In-progress imminent peril state cancel on an interworking group
This procedure describes the case where an authorized MCPTT user cancels an
interworking group\'s in-progress imminent peril state.
Figure 10.6.3.4‑1 shows the procedures for the MCPTT client cancelling an
interworking group\'s in-progress imminent peril state.
NOTE 1: The end of an imminent peril call does not cancel the MCPTT group\'s
in-progress imminent peril state. It is explicitly cancelled by an authorized
user.
NOTE 2: For simplicity, a single MCPTT server is shown in place of a user home
MCPTT server and a group hosting MCPTT server.
NOTE 3: The in-progress imminent peril interworking group state cancel
procedures reuse the information flows defined 3GPP TS 23.379 [7].
Pre-conditions:
1\. The MCPTT group is previously defined on the group management server with
MCPTT client 1, MCPTT client 2, and LMR users (represented by the IWF)
affiliated to that MCPTT group.
2\. The IWF is connected to, and is authorized to interwork with, the MCPTT
system.
3\. The interworking group information is available at the IWF.
4\. The interworking group is currently in in-progress imminent peril state
within the MCPTT system and has prioritized bearer support.
5\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
NOTE 4: For all the signalling messages passing through the IWF between the
MCPTT system and the LMR system, the IWF performs the identity conversion and
protocol translation.
6\. MCPTT client 1 previously initiated the imminent peril group call.
Figure 10.6.3.4-1: In-progress imminent peril group state cancel on an
interworking group
1\. The user at the MCPTT client 1 initiates an in-progress imminent peril
state cancel.
2\. MCPTT client 1 sends an MCPTT in-progress imminent peril group state
cancel request to the MCPTT server.
3\. The MCPTT server checks whether the MCPTT user 1 at MCPTT client 1 is
authorized to cancel the in-progress imminent peril group state.
4\. The MCPTT server cancels/resets the in-progress imminent peril group
state.
5\. The MCPTT server adjusts the priority of the underlying bearer; priority
treatment is no longer required.
6\. The MCPTT server sends an IWF in-progress imminent peril group state
cancel request(s) to the IWF. If the IWF has affiliated to this group on
behalf of the group\'s LMR users, only one IWF in-progress imminent peril
group state cancel request is sent to the IWF. If the MCPTT server has
received individual affiliations from the group\'s LMR users, an individual
IWF in-progress imminent peril group state cancel request is sent (to the IWF)
for each affiliated LMR user.
7\. The IWF sends the IWF in-progress imminent peril group state cancel
response(s) to the MCPTT server.
NOTE 5: The IWF responds even if it does not support imminent peril group
calls. IWF actions for priority are out of scope of the present document.
8\. The MCPTT server sends an MCPTT in-progress imminent peril group state
cancel request to the MCPTT group members.
NOTE 6: Steps 6 and 8 can occur in any order following step 5.
9\. MCPTT group members are notified of the in-progress imminent peril group
state cancel.
10\. MCPTT client 2 sends the MCPTT in-progress imminent peril group state
cancel response to the MCPTT server to acknowledge the in-progress MCPTT in-
progress imminent peril group state cancel request. For a multicast scenario,
this acknowledgement is not sent.
11\. The MCPTT server sends the MCPTT in-progress imminent peril group state
cancel response to the MCPTT client 1 to confirm the MCPTT in-progress
imminent peril group state cancel request.
NOTE 7: Step 11 can occur at any time following step 5.
### 10.6.4 Emergency alerts
#### 10.6.4.1 Emergency alert initiated by LMR user
In this procedure, an LMR user is initiating an emergency alert via the IWF.
Figure 10.6.4.1-1 shows the procedure for an emergency alert initiated by a
user in the LMR system. This subclause is based upon subclause for MCPTT
emergency alerts in 3GPP TS 23.379 [7], subclause 10.6.2.6.3.1.
Pre-conditions:
1\. The MC service group is previously defined on the group management server
with MC service client 1 and MC service client 2 affiliated to that MC service
group.
2\. The IWF is connected to and is authorized to interwork with the MC service
system.
3\. The MC service group information is available at the IWF, including
information that the MC service group is an interworking group (defined in the
LMR system or MC the system).
4\. The mapping relationship of group and user identities between the MC
service system and the LMR system has been configured at the IWF.
5\. The IWF may or may not have carried out an explicit affiliation procedure
with the MC service group.
6\. An emergency alert is requested on the LMR system.
NOTE 1: For all signalling messages passing through the IWF between the MC
service system and the LMR system, the IWF performs identity conversion and
protocol translation.
Figure 10.6.4.1-1 MC service emergency alert initiated by LMR user
1\. The LMR user initiates an emergency alert.
NOTE 2: How the IWF determines the emergency condition from the LMR system is
out of scope of the present document.
2\. The IWF sends an IWF emergency alert request to the designated MC service
server. If the location of the LMR user is not available to the IWF, the IWF
emergency alert request shall contain an indication that location is not
available.
3\. MC service server checks whether the MC service user ID that represents
the LMR user is authorized for initiation of MC service emergency alerts for
the indicated MC service group. The MC service server determines the
affiliation status of the group members.
4\. The MC service server sends an IWF emergency alert response to the IWF to
confirm the IWF emergency alert request.
NOTE 3: Sending the IWF emergency alert request without making a request to
also start an emergency call does not put the group into an ongoing emergency
condition.
5\. The MC service server sends an MC service emergency alert request towards
the MC service clients of each of those affiliated MC service group members.
The MC service emergency alert request message shall contain the following
information: Location, MC service ID and MC service group ID (i.e., MC service
user\'s selected MC service group or dedicated MC service emergency group, as
per MC service group configuration) and the MC service user\'s mission
critical organization name.
6\. MC service users are notified of the MC service emergency.
7\. The receiving MC service clients send an MC service emergency alert
response to the MC service server to acknowledge the MC service emergency
alert request.
8\. If the group is an interworking group defined in the MC system, the MC
service server implicitly affiliates the individual MC service ID of the LMR
user to the emergency group if not already affiliated. If the IWF is
configured to affiliate on behalf of all of its group members in a single
affiliation step, the MC service server affiliates the IWF ID instead of an
individual MC service ID.
NOTE 4: Step 8 can be performed any time after step 3 but at the latest
immediately after step 7.
NOTE 5: MC service group calls made to this MC service group will be
established as emergency calls if this MC service group has an ongoing
emergency condition.
NOTE 6: Sending the emergency alert does not put the other UEs in the group
into an emergency state.
#### 10.6.4.2 Emergency alert initiated by MC service user
In this procedure, an MC service user is initiating an emergency alert that is
delivered to the LMR system via the IWF. Figure 10.6.4.2-1 shows the procedure
for an emergency alert initiated by a user in the MC service system. This
subclause is based upon subclause for MCPTT emergency alerts in 3GPP TS 23.379
[7], subclause 10.6.2.6.3.1.
Pre-conditions:
1\. The MC service group is previously defined on the group management server
with MC service client 1 and MC service client 2 affiliated to that MC service
group.
2\. The IWF is connected to and is authorized to interwork with the MC service
system.
3\. The MC service group information is available at the IWF, including
information that the MC service group is an interworking group (defined in the
LMR system or the MC system).
4\. The mapping relationship of group and user identities between the MC
system and the LMR system has been configured at the IWF.
NOTE 1: For all signalling messages passing through the IWF between the MC
system and the LMR system, the IWF performs identity conversion and protocol
translation.
Figure 10.6.4.2-1 MC service emergency alert initiated by MC service user
1\. The MC service user 1 initiates an emergency alert.
2\. MC service client 1 sends an MC service emergency alert request to the MC
service server.
3\. The MC service server resolves the group ID, determines the affiliation
status of the group members and checks whether the IWF should be informed. In
this scenario, the group has affiliated members that are homed on the IWF,
thus the IWF shall be involved. MC service server also checks whether the MC
service user ID is authorized to initiate MC service emergency alerts for the
indicated MC service group.
4\. The MC service server sends an MC service emergency alert response to the
MC service client 1 to confirm the MC service emergency alert request.
NOTE 2: Sending the emergency alert without making a request to also start an
emergency call does not put the group into an ongoing emergency condition.
5\. MC service server sends an IWF emergency alert request to the IWF. If the
location of the MC service client 1 is not available, the IWF emergency alert
request shall contain an indication that location is not available. If the IWF
has affiliated to this group on behalf of the group\'s LMR users, only one IWF
emergency alert request is sent to the IWF. If the IWF has sent individual
affiliations for each of its LMR users, the MC service server sends an IWF
emergency alert request via the IWF to each affiliated LMR group member.
6\. The IWF sends an IWF service emergency alert response to the MC service
server to confirm the IWF emergency alert request(s).
7\. The MC service server sends an MC service emergency alert request towards
the MC service clients of each of those affiliated MC service group members.
The MC service emergency alert request message shall contain the following
information: Location, MC service ID and MC service group ID (i.e., MC service
user\'s selected MC service group or dedicated MC service emergency group, as
per MC service group configuration) and the MC service user\'s mission
critical organization name.
8\. MC service users are notified of the MC service emergency.
9\. The receiving MC service clients send an MC service emergency alert
response to the MC service server to acknowledge the MC service emergency
alert.
10\. The MC service server implicitly affiliates the MC service client 1 to
the emergency group if it is not already affiliated.
NOTE 3: Step 10 can be performed any time after step 3. Steps 5 and 7 can be
performed in which ever order.
NOTE 4: MC service group calls made to this MC service group will be
established as emergency calls if the MC service group has an ongoing
emergency condition.
NOTE 5: Sending an emergency alert does not put the other UEs in the group
into an emergency state.
### 10.6.5 Emergency alert cancellation
#### 10.6.5.1 Emergency alert cancellation of an LMR user
In this procedure, an LMR user is cancelling the emergency alert. Figure
10.6.5.1-1 shows the procedure for emergency alert cancellation of a user in
the LMR system. This subclause is based upon subclause for MCPTT emergency
alert cancel in 3GPP TS 23.379 [7], subclause 10.6.2.6.3.2.
Pre-conditions:
1\. The MC service group information is available at the IWF, including
information that the MC service group is an interworking group (defined in the
LMR system or the MC system).
2\. The LMR user had previously successfully initiated an emergency alert via
the IWF.
3\. The MC service client 1 and MC service client 2 are affiliated to the MC
service group.
4\. The MC service server may have carried out an explicit or implicit
affiliation procedure of the LMR user to the MC service group.
5\. The mapping relationship of group and user identities between the MC
service system and the LMR system has been configured at the IWF.
6\. The LMR user initiates an emergency alert cancel.
NOTE 1: For all the signalling messages passing through the IWF between the MC
service system and the LMR system, the IWF performs the identity conversion
and protocol translation.
Figure 10.6.5.1-1 MC service emergency alert cancellation of an LMR user
1\. The IWF sends an IWF emergency alert cancel request to the MC service
group to which the IWF had previously successfully sent the IWF emergency
alert request on behalf of the LMR user.
NOTE 2: The IWF emergency alert cancel request may carry an indication to also
request that the in-progress emergency state on the group is to be cancelled.
2\. The MC service server sends the IWF emergency alert cancel response to the
IWF to confirm the IWF emergency alert cancellation.
3\. The MC service server sends an MC service emergency alert cancel request
to the MC service clients of the affiliated MC service group members.
4\. MC service users are notified of the MC service emergency alert
cancellation of the LMR user.
5\. The receiving MC service clients send the MC service emergency alert
cancel response to the MC service server to acknowledge the MC service
emergency alert cancel request. For a multicast call scenario, these
acknowledgements are not sent.
NOTE 3: Steps 2 and 3 can be performed in which ever order.
#### 10.6.5.2 Emergency alert cancellation of an MC service user
In this procedure, an MC service user is cancelling the emergency alert.
Figure 10.6.5.2-1 shows the procedure for emergency alert cancellation from a
user in the MC service system. This subclause is based upon subclause for
MCPTT emergency alerts in 3GPP TS 23.379 [7], subclause 10.6.2.6.3.2.
Pre-conditions:
1\. The MC service group information is available at the IWF, including
information that the MC service group is an interworking group (defined in the
LMR system or the MC system).
2\. The MC service client 1 had previously successfully initiated an MC
service emergency alert request.
3\. The MC service client 1 is still in the emergency state.
4\. The MC service client 2 is affiliated to the MC service group.
5\. The MC service server may have carried out an explicit or implicit
affiliation procedure of the LMR user with the MC service group.
6\. The mapping relationship of group and user identities between the MC
service system and the LMR system has been configured at the IWF.
NOTE 1: For all the signalling messages passing through the IWF between the MC
service system and the LMR system, the IWF performs the identity conversion
and protocol translation.
Figure 10.6.5.2-1 MC service emergency alert cancellation of an MC service
user
1\. The user at the MC service client 1 initiates an emergency alert cancel.
NOTE 2: The MC service emergency alert cancel request may carry an indication
that the in-progress emergency state on the group is to be cancelled.
2\. MC service client 1 requests the MC service server to send an MC service
emergency alert cancel to the MC service group to which MC service client 1
had previously sent the emergency alert request. The MC service server
resolves the group ID, determines the affiliation status of the group members
and checks whether the IWF should be informed. In this scenario, the group has
affiliated members that are homed on the IWF, thus the IWF shall be involved.
3\. The MC service server sends the MC service emergency alert cancel response
to the MC service client 1 to confirm the MC service emergency alert cancel
request. MC service client 1 resets its emergency state.
4\. The MC service server sends an IWF emergency alert cancel request(s) to
the IWF. If the IWF has affiliated to this group on behalf of the group\'s LMR
users, only one IWF emergency alert cancel request message is sent to the IWF.
If the MCPTT server has received individual affiliations from the group\'s LMR
users, an individual IWF emergency alert cancel request message is sent to the
IWF for each affiliated LMR user.
5\. The IWF sends an IWF emergency alert cancel response(s) to the MC service
server to acknowledge the IWF emergency alert cancel request(s).
6\. The MC service server sends an MC service emergency alert cancel request
towards the MC service clients of the affiliated MC service group members.
7\. MC service users are notified of the MC service emergency alert
cancellation of MC service client 1.
8\. The receiving MC service clients send the MC service emergency alert
cancel response to the MC service server to acknowledge the MC service
emergency alert cancel request. For a multicast call scenario, these
acknowledgements are not sent.
NOTE 3: Steps 3 and 4 can be performed in which ever order.
## 10.7 Codec
### 10.7.1 Information flows for codec
#### 10.7.1.1 IWF codec reconciliation request
Table 10.7.1.1-1 describes the information flow IWF codec reconciliation
request from the IWF to the MCPTT server.
Table 10.7.1.1-1: IWF codec reconciliation request
* * *
Information element Status Description MCPTT group ID M The MCPTT group ID for
which a codec change is requested. Codec type M Type of the requested codec
* * *
#### 10.7.1.2 IWF codec reconciliation response
Table 10.7.1.2-1 describes the information flow IWF codec reconciliation
response from the MCPTT server to the IWF.
Table 10.7.1.2-1: IWF codec reconciliation response
* * *
Information element Status Description MCPTT group ID M The MCPTT group ID for
which a codec change was requested. Result M Result indicates success or
failure of the requested codec change.
* * *
### 10.7.2 IWF transcoding
The IWF can be used to transcode voice packets in transit between the LMR and
MCPTT systems. In this scenario, the MCPTT system can operate its own vocoder
type and the LMR system can operate its own vocoder type. The type of vocoder
used on the LMR side is outside the scope of the present document.
When operating in this mode, the IWF converts voice media formats between the
two sides. Vocoder negotiation is according to procedures in the present
document.
### 10.7.3 Codec negotiation by the LMR system
#### 10.7.3.1 Description
An MCPTT group may be configured to use an LMR speech codec, such that speech
can be carried end to end between all group members in both LMR and MCPTT
system without transcoding.
An LMR system can support more than one speech codec; for example P25 supports
both a full rate and a half rate speech codec. Circumstances within the LMR
system might require that the codec in use within a group is changed according
to the needs of the LMR system.
Figure 10.7.3.1-1 below illustrates a procedure which allows the LMR system to
change the speech codec within an MCPTT group that is connected to the LMR
system via the IWF.
Pre-conditions:
1\. Group members have affiliated to the MCPTT group in both the LMR system
and in the MCPTT system
2\. A permitted LMR codec has been negotiated for use by MCPTT group members
3\. MCPTT group members support the requested second LMR speech codec
NOTE 1: The exception condition created if the IWF does not support trancoding
and the MCPTT client does not support the requested LMR codec is outside the
scope of the present document.
4\. The LMR system requires a change to an alternative speech codec.
Figure 10.7.3.1-1: Codec reconciliation procedure
1\. The IWF sends a codec reconciliation request to the MCPTT server on behalf
of the LMR system.
2\. The MCPTT server checks that the requested codec is permitted for the
MCPTT group.
3\. The MCPTT server sends a codec reconciliation request to all of the
affilliated MCPTT client(s) to negotiate the use of the speech codec requested
by the LMR system.
4\. The MCPTT client replies with a codec reconciliation response to the MCPTT
server, indicating acceptance of the new speech codec.
5\. The MCPTT server sends a codec reconciliation response to the IWF.
6\. Further transmissions in the MCPTT group use the new codec in the media
plane.
NOTE 2: The time at which the new codec is first used by a transmitting party
is outside the scope of the present document.
## 10.8 MCData short data service
### 10.8.1 General
The present document specifies short data service (SDS) interworking between
LMR users and MCData clients using one-to-one standalone SDS messages and
group standalone SDS messages. The IWF behaves as a peer MCData server to
other MCData servers.
When an LMR user attempts to send an LMR message to the MCData service, the
IWF converts the LMR message into a request to send an MCData SDS. The method
by which the IWF converts the LMR message into a request to send an MCData SDS
is outside the scope of the present document.
When the IWF receives a request to send an MCData SDS to an LMR user or a
group of LMR users, the IWF converts the request into one or more LMR
messages. The method by which the IWF converts the MCData SDS request into an
LMR messages is outside the scope of the present document.
### 10.8.2 Information flows for the short data service
#### 10.8.2.1 General
The following subclauses define information flows for MCData SDS on the IWF-2
interface. MCData SDS related information flows on reference points other than
IWF-2 are defined in 3GPP TS 23.282 [6], subclause 7.4.2.1. In each case, the
LMR users behind the IWF are represented by MCData IDs or a MCData group ID as
appropriate and so the MCData server shall be capable of routing messages
towards identities located behind the IWF.
#### 10.8.2.2 IWF MCData standalone data request
Table 10.8.2.2-1 describes the information flow for the MCData standalone data
request (in 3GPP TS 23.282 [6] subclauses 7.4.2.2.2 and 7.4.2.3.2) sent from
the MCData server to the IWF and from the IWF to a MCData server.
Table 10.8.2.2-1: IWF MCData standalone data request
+-----------------------------+--------+-----------------------------+ | Information element | Status | Description | +-----------------------------+--------+-----------------------------+ | MCData ID | M | The identity of the MCData | | | | user sending data | +-----------------------------+--------+-----------------------------+ | Functional alias | O | The associated functional | | | | alias of the MCData user | | | | sending data. | +-----------------------------+--------+-----------------------------+ | MCData ID | M | The identity of the MCData | | | | user towards which the data | | | | is sent | +-----------------------------+--------+-----------------------------+ | Conversation Identifier | M | Identifies the conversation | | (see NOTE 1) | | | +-----------------------------+--------+-----------------------------+ | Transaction Identifier (see | M | Identifies the MCData | | NOTE 1) | | transaction | +-----------------------------+--------+-----------------------------+ | Reply Identifier | O | Identifies the original | | | | MCData transaction to which | | | | the current transaction is | | | | a reply to | +-----------------------------+--------+-----------------------------+ | Disposition Type | O | Indicates the disposition | | | | type expected from the | | | | receiver (i.e., delivered | | | | or read or both) | +-----------------------------+--------+-----------------------------+ | Payload Destination Type | M | Indicates whether the | | | | payload is for application | | | | consumption or MCData | | | | client consumption | +-----------------------------+--------+-----------------------------+ | Application identifier (see | O | Identifies the application | | NOTE 2) | | for which the payload is | | | | intended (e.g. text string, | | | | port address, URI) | +-----------------------------+--------+-----------------------------+ | Payload | M | SDS content | +-----------------------------+--------+-----------------------------+ | NOTE 1: A reserved value of | | | | the Information Element | | | | shall be defined which | | | | indicates that the sender | | | | does not support this | | | | Information Element. | | | | | | | | NOTE 2: The application | | | | identifier shall be | | | | included only if the | | | | payload destination type | | | | indicates that the payload | | | | is for application | | | | consumption. | | | +-----------------------------+--------+-----------------------------+
#### 10.8.2.3 IWF MCData data disposition notification
Table 10.8.2.3-1 describes the information flow for the MCData data
disposition notification sent from the IWF to the MCData server and from the
MCData server to the IWF.
Table 10.8.2.3-1: IWF MCData data disposition notification
* * *
Information element Status Description MCData ID M The identity of the MCData
user towards which the notification is sent MCData ID M The identity of the
MCData user sending notification Conversation Identifier (see NOTE) M
Identifies the conversation Disposition association M Identity of the original
MCData transaction Disposition M Disposition which is delivered or read or
both NOTE: A reserved value of the Information Element shall be defined which
indicates that the sender does not support this Information Element.
* * *
#### 10.8.2.4 IWF MCData group standalone data request (IWF -- MCData server)
Table 10.8.2.4-1 describes the information flow for the MCData group
standalone data request (in 3GPP TS 23.282 [6] subclause 7.4.2.5.2) sent from
the IWF to the MCData server when the IWF is acting as the initiating MCData
client.
Table 10.8.2.4-1: IWF MCData group standalone data request (IWF -- MCData
server)
+-----------------------------+--------+-----------------------------+ | Information element | Status | Description | +-----------------------------+--------+-----------------------------+ | MCData ID | M | The identity of the MCData | | | | user sending data | +-----------------------------+--------+-----------------------------+ | MCData group ID | M | The MCData group ID to | | | | which the data is to be | | | | sent | +-----------------------------+--------+-----------------------------+ | Conversation Identifier | M | Identifies the conversation | | (see NOTE 1) | | | +-----------------------------+--------+-----------------------------+ | Transaction Identifier (see | M | Identifies the MCData | | NOTE 1) | | transaction | +-----------------------------+--------+-----------------------------+ | Reply Identifier | O | Identifies the original | | | | MCData transaction to which | | | | the current transaction is | | | | a reply to | +-----------------------------+--------+-----------------------------+ | Disposition Type | O | Indicates the disposition | | | | type expected from the | | | | receiver (i.e., delivered | | | | or read or both) | +-----------------------------+--------+-----------------------------+ | Payload Destination Type | M | Indicates whether the | | | | payload is for application | | | | consumption or MCData | | | | client consumption | +-----------------------------+--------+-----------------------------+ | Application identifier (see | O | Identifies the application | | NOTE 2) | | for which the payload is | | | | intended (e.g. text string, | | | | port address, URI) | +-----------------------------+--------+-----------------------------+ | Payload | M | SDS content | +-----------------------------+--------+-----------------------------+ | NOTE 1: A reserved value of | | | | the Information Element | | | | shall be defined which | | | | indicates that the sender | | | | does not support this | | | | Information Element. | | | | | | | | NOTE 2: The application | | | | identifier shall be | | | | included only if the | | | | payload destination type | | | | indicates that the SDS | | | | message is for application | | | | consumption. | | | +-----------------------------+--------+-----------------------------+
#### 10.8.2.5 IWF MCData group standalone data request (MCData server - IWF)
Table 10.8.2.5‑1 describes the information flow for the MCData group
standalone data request (in 3GPP TS 23.282 [6] subclause 7.4.2.5.2) sent from
the MCData server to the IWF when the IWF is acting as proxy for MCData
clients.
Table 10.8.2.5‑1: IWF MCData group standalone data request (MCData server --
IWF)
* * *
Information element Status Description MCData ID M The identity of the MCData
user sending data MCData group ID M The MCData group ID to which the data is
to be sent MCData ID M The identity of the MCData user towards which the data
is sent Conversation Identifier M Identifies the conversation Transaction
Identifier M Identifies the MCData transaction Reply Identifier O Identifies
the original MCData transaction to which the current transaction is a reply to
Disposition Type O Indicates the disposition type expected from the receiver
(i.e., delivered or read or both) Payload Destination Type M Indicates whether
the payload is for application consumption or MCData client consumption
Application identifier (see NOTE) O Identifies the application for which the
payload is intended (e.g. text string, port address, URI) Payload M SDS
content NOTE: The application identifier shall be included only if the payload
destination type indicates that the payload is for application consumption.
* * *
#### 10.8.2.6 IWF MCData data disposition notification(s) (MCData server to
IWF)
Table 10.8.2.6‑1 describes the information flow for the MCData data
disposition notification(s) sent from the MCData server to the IWF when the
IWF is acting as proxy for MCData client(s).
Table 10.8.2.6-1: IWF MCData data disposition notification(s) (MCData server
-- IWF)
* * *
Information element Status Description MCData ID M The identity of the MCData
user towards which the notification is sent MCData ID M The identity of the
MCData user sending notification Conversation Identifier M Identifies the
conversation Disposition association M Identity of the original MCData
transaction Disposition M Disposition which is delivered or read or both
* * *
#### 10.8.2.7 IWF MCData group standalone data request (IWF -- MCData server)
Table 10.8.2.7‑1 describes the information flow for the MCData group
standalone data request (in 3GPP TS 23.282 [6] subclause 7.4.2.6.2) sent from
the IWF representing the MCData client to the MCData server.
Table 10.8.2.7‑1: IWF MCData group standalone data request (IWF -- MCData
server)
+-----------------------------+--------+-----------------------------+ | Information element | Status | Description | +-----------------------------+--------+-----------------------------+ | MCData ID | M | The identity of the MCData | | | | user sending data | +-----------------------------+--------+-----------------------------+ | MCData group ID | M | The MCData group ID to | | | | which the data is to be | | | | sent | +-----------------------------+--------+-----------------------------+ | Conversation Identifier | M | Identifies the conversation | | (see NOTE 1) | | | +-----------------------------+--------+-----------------------------+ | Transaction Identifier (see | M | Identifies the MCData | | NOTE 1) | | transaction | +-----------------------------+--------+-----------------------------+ | Reply Identifier | O | Identifies the original | | | | MCData transaction to which | | | | the current transaction is | | | | a reply to | +-----------------------------+--------+-----------------------------+ | Transaction type | M | Standalone transaction | +-----------------------------+--------+-----------------------------+ | Disposition Type | O | Indicates the disposition | | | | type expected from the | | | | receiver (i.e., delivered | | | | or read or both) | +-----------------------------+--------+-----------------------------+ | Payload Destination Type | M | Indicates whether the SDS | | | | payload is for application | | | | consumption or MCData user | | | | consumption | +-----------------------------+--------+-----------------------------+ | Application identifier | O | Identifies the application | | (see NOTE 2) | | for which the payload is | | | | intended (e.g. text string, | | | | port address, URI) | +-----------------------------+--------+-----------------------------+ | SDP offer | M | Media parameters offered | +-----------------------------+--------+-----------------------------+ | NOTE 1: A reserved value of | | | | the Information Element | | | | shall be defined which | | | | indicates that the sender | | | | does not support this | | | | Information Element. | | | | | | | | NOTE 2: The application | | | | identifier shall be | | | | included only if the | | | | payload destination type | | | | indicates that the SDS | | | | message is for application | | | | consumption. | | | +-----------------------------+--------+-----------------------------+
#### 10.8.2.8 IWF MCData group standalone data request (MCData server -- IWF)
Table 10.8.2.8-1 describes the information flow for the MCData group
standalone data request (in 3GPP TS 23.282 [6] subclause 7.4.2.6.2) sent from
the MCData server to the IWF acting as proxy for MCData client(s).
Table 10.8.2.8-1: IWF MCData group standalone data request (MCData server --
IWF)
* * *
Information element Status Description MCData ID M The identity of the MCData
user sending data MCData group ID M The MCData group ID to which the data is
to be sent MCData ID M The identity of the MCData user towards which the data
is sent Conversation Identifier M Identifies the conversation Transaction
Identifier M Identifies the MCData transaction Reply Identifier O Identifies
the original MCData transaction to which the current transaction is a reply to
Transaction type M Standalone transaction Disposition Type O Indicates the
disposition type expected from the receiver (i.e., delivered or read or both)
Payload Destination Type M Indicates whether the SDS payload is for
application consumption or MCData user consumption Application identifier (see
NOTE) O Identifies the application for which the payload is intended (e.g.
text string, port address, URI) SDP offer M Media parameters offered NOTE: The
application identifier shall be included only if the payload destination type
indicates that the payload is for application consumption.
* * *
#### 10.8.2.9 IWF MCData group standalone data response
Table 10.8.2.9-1 describes the information flow for the MCData group
standalone data response (in 3GPP TS 23.282 [6] subclause 7.4.2.6.2) sent from
the IWF to the MCData server and from the MCData server to the IWF acting as
proxy for other MCData clients.
Table 10.8.2.9-1: IWF MCData group standalone data response
* * *
Information element Status Description MCData ID M The identity of the MCData
user receiving data MCData group ID M The MCData group ID to which the data is
to be sent MCData ID M The identity of the MCData user sent data Conversation
Identifier (see NOTE) M Identifies the conversation SDP answer M Media
parameters selected NOTE: A reserved value of the Information Element shall be
defined which indicates that the sender does not support this Information
Element.
* * *
### 10.8.3 Behaviour at the MCData Client
The MCData client interfaces with the MCData server as specified in 3GPP TS
23.282 [6].
### 10.8.4 Behaviour at the IWF
The IWF interfaces with the MCData server via the reference points defined in
subclause 7.4 of the present document.
### 10.8.5 Behaviour at the MCData server
The MCData server behaves as specified in 3GPP TS 23.282 [6], with the
addition that the MCData server shall route SDS messages addressed to MCData
IDs and MCData group IDs that lie behind IWFs to the appropriate IWFs.
### 10.8.6 MCData user one-to-one SDS request to an LMR user
#### 10.8.6.1 Signalling control plane
The procedure for an MCData user requesting to send a signalling control plane
SDS to a single LMR user is as specified in 3GPP TS 23.282 [6] subclause
7.4.2.2 for the one‑to‑one standalone short data service using the signalling
control plane, with the exception that MCData client 2 is located behind the
IWF. The SDS is addressed to the MCData ID that has been allocated to the LMR
user. The IWF behaves as a peer MCData server.
#### 10.8.6.2 Media plane
The procedure for an MCData user requesting to send a media plane SDS to a
single LMR user is as specified in 3GPP TS 23.282 [6] subclause 7.4.2.3 for
the one‑to‑one standalone short data service using the media plane, with the
exception that MCData client 2 is located behind the IWF. The SDS is addressed
to the MCData ID that has been allocated to the LMR user. The IWF behaves as a
peer MCData server.
### 10.8.7 LMR user one-to-one SDS request to an MCData user
#### 10.8.7.1 Signalling control plane
The procedure for an IWF requesting, on behalf of an LMR user, to send a
signalling control plane SDS to a single MCData user is as specified in 3GPP
TS 23.282 [6] subclause 7.4.2.2 for the one‑to‑one standalone short data
service using the signalling control plane, with the exception that MCData
client 1 is located behind the IWF. The source address of the SDS is the
MCData ID that has been allocated to the LMR user. The IWF behaves as a peer
MCData server.
#### 10.8.7.2 Media plane
The procedure for an IWF requesting, on behalf of an LMR user, to send a media
plane SDS to a single MCData user is as specified in 3GPP TS 23.282 [6]
subclause 7.4.2.3 for the one‑to‑one standalone short data service using the
media plane, with the exception that MCData client 1 is located behind the
IWF. The source address of the SDS is the MCData ID that has been allocated to
the LMR user. The IWF behaves as a peer MCData server.
### 10.8.8 MCData user group SDS request to an MCData group including LMR
users
#### 10.8.8.1 Signalling control plane
The procedure for an MCData user requesting to send a signalling control plane
SDS to an MCData group that includes one or more LMR users is as specified in
3GPP TS 23.282 [6] subclause 7.4.2.5 for the group standalone short data
service using the signalling control plane. In the case of implementation
involving an IWF the difference is that one or more of the MCData clients 2 to
n are located behind IWFs that have affiliated to the MCData group (see
subclause 10.1.2 of the present document). The SDS is addressed to the MCData
group ID. The IWF behaves as a peer MCData server.
#### 10.8.8.2 Media plane
The procedure for an MCData user requesting to send a media plane SDS to an
MCData group that includes one or more LMR users is as specified in 3GPP TS
23.282 [6] subclause 7.4.2.6 for the group standalone short data service using
the media plane. In the case of implementation involving an IWF the difference
is that one or more of the MCData clients 2 to n can be located behind IWFs
that have affilated to the MCData group (see subclause 10.1.2 of the present
document). The SDS is addressed to the MCData group ID. The IWF behaves as a
peer MCData server.
### 10.8.9 LMR user group SDS request to an MCData group
#### 10.8.9.1 Signalling control plane
The procedure for an IWF requesting, on behalf of an LMR user, to send a
signalling control plane SDS to an MCData group is as specified in 3GPP TS
23.282 [6] subclause 7.4.2.5 for the group standalone short data service using
the signalling control plane, with the exception that MCData client 1 is
located behind an IWF and one or more of the MCData clients 2 to n can be
behind IWFs that have affiliated to the MCData group (see subclause 10.1.2 of
the present document). The SDS is addressed to the MCData group ID. The IWF
behaves as a peer MCData server to other MCData servers.
#### 10.8.9.2 Media plane
The procedure for an IWF requesting, on behalf of an LMR user, to send a media
plane SDS to an MCData group is as specified in 3GPP TS 23.282 [6] subclause
7.4.2.6 for the group standalone short data service using the media plane,
with the exception that MCData client 1 is located behind an IWF and one or
more of the MCData clients 2 to n can be behind IWFs that have affiliated to
the MCData group (see subclause 10.1.2 of the present document). The SDS is
addressed to the MCData group ID. The IWF behaves as a peer MCData server to
other MCData servers.
## 10.9 IWF as a security gateway
### 10.9.1 Support for transcoding with encrypted speech
In some cases when encryption of voice media is required in the MC system, the
MCPTT user(s) and the LMR user(s) can use different codecs. In these cases,
transcoding is needed and before transcoding can occur, encryption applied to
the voice media by the MC system needs to be removed. After transcoding, LMR
encryption can be applied (out-of-scope of the present document). An IWF can
perform these functions and be deployed as a security gateway between the
MCPTT system and the LMR system. When the IWF removes the encryption applied
by the MC system, the IWF must perform key management procedures defined in
3GPP TS 33.180 [8] to obtain the key material for the group.
## 10.10 Simultaneous interworked calls (on-network)
### 10.10.1 General
An IWF representing an LMR user may support simultaneous interworked calls for
the same LMR user. The LMR user can become involved in simultaneous
interworked calls when the IWF invites, joins or accepts more than one
interworked call on behalf of the LMR user, or when the IWF affilates the LMR
user to multiple groups. This subclause is based on the subclause for
simultaneous session for MCPTT calls in 3GPP TS 23.379 [7], subclause 10.8.
NOTE: An LMR user affiliating to multiple interworked groups with active calls
via the IWF can result in the LMR user being invited simultaneously to
multiple interworked calls.
How the IWF accomodates simultaneous interworked calls to a single LMR user is
outside the scope of the present document.
## 10.11 Location
### 10.11.1 Location of current talker
3GPP TS 23.379 [7], subclause 10.6.2.7 describes a high-level procedure to
provide the location of the current talker to all the receiving MCPTT users.
### 10.11.2 Location of current talker (MCPTT server to IWF)
Figure 10.11.2-1 shows the high-level procedure to for MCPTT service to
provide the location information about the current talking user to all the
receiving MCPTT users and the IWF.
Pre-conditions:
1\. There is on-going group call involving MCPTT client 1 and MCPTT client 2
and the IWF.
2\. MCPTT client 1 is the current talking user.
3\. MCPTT server has obtained the location information of MCPTT client 1.
Figure 10.11.2-1: Providing location information of the current talker
1\. MCPTT client 1 gets the floor to transmit voice media.
2\. The MCPTT server checks the privacy policy (authorisation to provide
location information to other MCPTT users on a call when talking, as defined
in 3GPP TS 23.379 [7] Annex A.3) of the current talking MCPTT user to decide
if the location information of MCPTT client 1 can be provided to other MCPTT
users on the call.
3\. If the privacy policy permits, the MCPTT server provides the location
information of MCPTT client 1 to MCPTT client 2 and the IWF. The procedures
for this are described in 3GPP TS 23.280 [5] subclause 10.9.3.6. Optionally,
the location information may be provided in the floor taken message sent to
MCPTT client 2 and the IWF according to 3GPP TS 23.379 [7] subclause
10.9.1.3.1, if the privacy policy permits.
### 10.11.3 Location of current talker (IWF to MCPTT server)
Figure 10.11.3‑1 shows the high-level procedure to for the IWF to provide the
location information about the current LMR talking user to all the receiving
MCPTT users.
Pre-conditions:
1\. There is on-going group call involving MCPTT client 1 and MCPTT client 2
and the IWF.
2\. An LMR user is the current talking user through the IWF.
NOTE: How the MCPTT server acquires the location of the LMR user is outside
the scope of the present document.
Figure 10.11.3-1: Providing location information of the current talker
1\. The IWF gets the floor to transmit voice media.
2\. The MCPTT server checks the privacy policy (authorisation to provide
location information to other MCPTT users on a call when talking, as defined
in 3GPP TS 23.379 [7] Annex A.3) of the current talking IWF user to decide if
the location information of the user on the IWF can be provided to other MCPTT
users on the call.
3\. The MCPTT server provides the location information of the IWF user to
MCPTT client 1 and MCPTT client 2. The procedures for this are described in
3GPP TS 23.280 [5] subclause 10.9.3.6. Optionally, the location information
may be provided in the floor taken message sent to MCPTT client 2 and the IWF
according to 3GPP TS 23.379 [7] subclause 10.9.1.3.1.
## 10.12 LMR security transport
### 10.12.1 Information flows for LMR security transport
#### 10.12.1.1 Non-3GPP security message request
Table 10.12.1.1-1 describes the information flow non-3GPP security message
request from the MC service server to the IWF, from the IWF to the MC service
server, from the MC service server to the MC service client and from the MC
service client to the MC service server.
Table 10.12.1.1-1: Non-3GPP security message request
* * *
Information Element Status Description MC service ID M The identity of the MC
service user URI of LMR security functional entity M URI of LMR key management
functional entity user profile parameter defined in 3GPP TS 23.379 [7] LMR
type O The LMR technology, e.g. TETRA, P25. Required when sent toward the MC
service client. Payload M Opaque payload. Contents and format are out of 3GPP
scope.
* * *
#### 10.12.1.2 Non-3GPP security message response
Table 10.12.1.2-1 describes the information flow non-3GPP security message
response from the MC service server to the IWF, from the IWF to the MC service
server, from the MC service server to the MC service client and from the MC
service client to the MC service server.
Table 10.12.1.2-1: Non-3GPP security message response
* * *
Information Element Status Description MC service ID M The identity of the MC
service user URI of LMR security functional entity M URI of LMR key management
functional entity user profile parameter defined in 3GPP TS 23.379 [7]
* * *
### 10.12.2 LMR key management messages
#### 10.12.2.1 General
This subclause defines end to end messaging to convey the non-3GPP, LMR
security information opaquely (message contents are out of 3GPP\'s scope)
across the MC system, between the IWF and the LMR aware MC service client. The
end to end messasges are service independent, any MC service may support them.
#### 10.12.2.2 MC service client initiated
Figure 10.12.2.2-1 describes the case where an MC service client sends LMR
security information to the IWF.
Pre-conditions:
1\. The MC service client is registered and the user is authenticated and
authorized to use the MC service server.
Figure 10.12.2.2-1: Non-3GPP security messaging, MC service client to the IWF
1\. The MC service client sends s a non-3GPP security message request to the
MC service server. The contents of the message are opaque to the MC service
and are out of scope of 3GPP.
2\. The MC service server forwards the contents of the non-3GPP security
message request to the IWF.
3\. The IWF acknowledges with a non-3GPP security message response to the MC
service server.
4\. The MC service server acknowledges with a non-3GPP security message
response to the MC service client.
#### 10.12.2.3 IWF initiated
Figure 10.12.2.3-1 describes the case where the IWF sends LMR security
information to an MC service client.
Pre-conditions:
1\. The MC service client is registered and the user is authenticated and
authorized to use the MC service server.
Figure 10.12.2.3-1: Non-3GPP security, from the IWF to MC service client
1\. The IWF sends a non-3GPP security message request to the MC service
server. The contents of the message are opaque to the MC service and are out
of scope of 3GPP.
2\. The MC service server forwards the contents of non-3GPP security message
request to the MC service client.
3\. The MC service client acknowledges with a non-3GPP security message
response to the MC service server.
4\. The MC service server forwards the non-3GPP security message response to
the IWF.
## 10.13 Analogue FM/TIA-603-D and other legacy LMR interworking
### 10.13.1 General
An IWF representing an LMR user can support interworking with legacy analogue
FM radio systems that are compliant with the TIA-603-D [9] Standard. This type
of legacy LMR system is sometimes referred to as conventional FM radio.
Characteristics of legacy conventional FM radio include:
\- Voice media is conveyed without the use of a voice codec.
\- There is no possibility of end-to-end encryption between an LMR user and a
MC user.
\- Group communication is possible using various means to identify a group
such as a single channel / FM frequency, or sub-audible data as defined in
[3]. The means for identifying groups within the legacy conventional FM system
is outside the scope of the present document.
\- The ID of the talking party is generally not available. Various means to
identify a talker are available in legacy conventional FM systems, but this is
outside the scope of the present document.
\- Indication of call priority (e.g. emergency) is generally not available.
Various means to identify priority are available in legacy conventional FM
systems, but this is outside the scope of the present document.
Other legacy LMR systems such as digital conventional (e.g. P25 conventional),
trunked analogue FM systems, non-standard legacy LMR systems, both
conventional and trunked, can also be supported as long as they conform to the
present document.
### 10.13.2 Interworking Concepts
Procedures defined in the present document are applicable to interworking with
legacy analogue FM radio systems.
Architecture concepts for interworking are summarized below, including general
information for other legacy conventional radio systems.
\- The IWF is configured with knowledge of groups and users from legacy
conventional LMR radio systems. Translations to MCPTT Group and MCPTT User IDs
is performed by the IWF as specified in the present document. How the legacy
LMR conventional system supports groups, such as mapping a group to a
channel/frequency, or using a Group ID (i.e. P25 conventional), or mapping
some other protocol element or tone signalling to a group is outside the scope
of the present document.
\- Interworking to a legacy conventional LMR system can make use of the
following procedures as defined in the present document:
\- affiliation;
\- group management including group regrouping
\- group calls including pre-arranged, chat, and broadcast;
\- priority calls including emergency and imminent peril; and
\- private calls.
NOTE 1: Some analogue FM conventional LMR systems and digital conventional LMR
systems support various schemes for private call. These can be supported as
long as they conform to the present document.
\- Interworking to a legacy conventional LMR system can make use of the
following functions of the MCPTT system, as defined in the present document:
\- transcoding.
\- Interworking to a legacy conventional LMR system can make use of the
following functions of the MCPTT system, as defined in the present document,
with some limitations:
\- caller ID / talker ID;
\- priority indication (e.g. emergency);
\- end-to-end encryption;
\- location; and
\- short data service.
NOTE 2: Some digital conventional LMR systems, such as P25 Conventional,
natively support group IDs, user IDs, short data, and priority indication. In
some cases, the talker ID becomes available sometime after the call starts.
NOTE 3: Some analogue FM conventional LMR systems support various schemes for
caller ID, emergency, and other features (e.g. Multi-tone, Type 99). These can
be supported as long as they conform to the present document. In some cases,
the talker ID becomes available sometime after the call starts.
NOTE 4: Some digital conventional LMR systems, such as P25 Conventional, can
support end-to-end encryption between the LMR user and a MC user. There is no
possibility of end-to-end encryption between an analogue FM LMR user and a MC
user.
### 10.13.3 Procedures
As described above, existing procedures in this document can be used for
interworking with legacy conventional LMR radio systems.
The following procedures describe special cases where the MCPTT ID (i.e.
talker ID) is updated during a media transmission within a call. This
mechanism of updating the MCPTT ID part way through an MCPTT media
transmission may be used for any MCPTT media transmission described elsewhere
in the present document.
#### 10.13.3.1 Group call with talker ID update initiated by an LMR user on an
interworking group defined in the MCPTT system
In this procedure, an LMR user in a legacy conventional FM radio system
initiates a group call on an interworking group defined in the MCPTT system.
The talker ID is not known at the start of the call and is updated after media
transmission begins. The signalling procedure is described in figure
10.13.3.1-1.
This subclause is based upon subclause for pre-arranged group call setup in
3GPP TS 23.379 [7], subclause 10.6.2.3.1.1.2.
Pre-conditions:
1\. The interworking group information is known at the MCPTT server and the
IWF by configuration or group creation. The interworking group has been
defined in the MCPTT system.
2\. MCPTT client 1 and MCPTT client 2 are registered and their respective
users are authenticated and authorized to use the MCPTT service.
3\. The users in this interworking group have been affiliated to the
interworking group.
4\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
5\. The LMR user in a legacy conventional FM radio system initiates a group
call.
NOTE 1: For all the signalling messages passing through the IWF between the
MCPTT system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.13.3.1-1: Group call with talker ID update initiated by an LMR user
on an interworking group defined in the MCPTT system
1\. The IWF sends an IWF group call request to the MCPTT server for call
establishment. In this case floor control is also requested and an indication
of implicit floor request is included. The IWF uses its pre-configured MCPTT
ID in the group call request.
2\. The MCPTT server calls the affiliated users from the MCPTT system as
described in 3GPP TS 23.379 [7]. The LMR user is in a legacy conventional FM
radio system so E2EE is not specified, and transcoding is needed at the IWF.
3\. If the group has other affiliated LMR users than the calling party and the
MCPTT server has received individual affiliations from those LMR users, an
individual IWF group call request is sent to the IWF for each affiliated LMR
user.
NOTE 2: Steps 2 and 3 can occur in any order.
NOTE 3: How the LMR users from the LMR system are being called is outside the
scope of the present document.
4\. The IWF returns IWF group call response(s) to the MCPTT server.
5\. The MCPTT server confirms the successful establishment of the group call
by sending an IWF Group call response to the IWF.
NOTE 4: How the group call response is returned to the initiating LMR user is
outside the scope of the present document.
6\. The interworking group call has successfully established media plane for
communication and any user can transmit media. The MCPTT system where the
interworking group is defined is the controlling system of the group call and
manages the floor control.
NOTE 5: How the floor control is managed in the LMR system is outside the
scope of the present document.
7\. Because the group call request contained an imlicit floor request, and no
other users are requesting the floor, the MCPTT server sends an IWF floor
granted message to the IWF confirming that the IWF has the floor. The MCPTT
server also sends Floor taken messages to the affiliated users in the MCPTT
system. The MCPTT ID in the floor taken messages is the pre-configured IWF
MCPTT ID.
8\. If the group has other affiliated LMR users than the calling party, and
the MCPTT server has received individual affiliations from those LMR users, an
individual IWF floor taken message is sent to the IWF for each affiliated LMR
user.
9\. At some time after media transfer begins, the IWF receives knowledge of
the LMR user\'s talker ID.
NOTE 6: How the IWF learns the LMR user\'s talker ID is outside the scope of
the present document. In some LMR conventional systems, the talker ID becomes
available shortly after the start of the call; in other systems, it is not
available until the end of the call.
10\. The IWF sends an IWF talker ID update to the MCPTT server informing the
server that a new talker is using the floor, but the floor should not be
released.
11\. The MCPTT server sends Floor taken messages to the affiliated users in
the MCPTT system. The MCPTT ID in the floor taken messages is the new talker
ID contained in the IWF talker ID update.
NOTE 7: All other floor participants (not shown) that are part of this group
call receive a floor taken message, so that the other floor participants learn
the identity of the newly granted talker.
12\. If the group has other affiliated LMR users than the calling party, and
the MCPTT server has received individual affiliations from those LMR users, an
individual IWF floor taken message is sent to the IWF for each affiliated LMR
user.
#### 10.13.3.2 Group call with talker ID update initiated by an LMR user on an
interworking group defined in the LMR system
In this procedure, an LMR user in a legacy conventional FM radio system
initiates a group call on an interworking group defined in the LMR system. The
talker ID is not known at the start of the call and is updated after media
transmission begins. The signalling procedure is described in figure
10.13.3.2-1.
This subclause is based upon subclause for pre-arranged group call setup in
3GPP TS 23.379 [7], subclause 10.6.2.3.1.1.2.
Pre-conditions:
1\. The interworking group information is known at the MCPTT server and the
IWF by configuration or group creation. The interworking group has been
defined in the LMR system.
2\. MCPTT client 1 and MCPTT client 2 are registered and their respective
users are authenticated and authorized to use the MCPTT service.
3\. The users in this interworking group have been affiliated to the
interworking group.
4\. The mapping relationship of group and user identities between the MCPTT
system and the LMR system has been configured at the IWF.
5\. The LMR user in a legacy conventional FM radio system initiates a group
call.
NOTE 1: For all the signalling messages passing through the IWF between the
MCPTT system and the LMR system, the IWF performs the identity conversion and
protocol translation.
Figure 10.13.3.2-1: Group call with talker ID update initiated by an LMR user
on an interworking group defined in the LMR system
1\. The IWF sends an IWF group call request(s) to the MCPTT server for call
establishment. An individual IWF group call request is sent to the MCPTT
server for each affiliated MCPTT user in the group, in this example scenario
to the users in MCPTT clients 1 and 2. In this case floor control is also
requested and an indication of implicit floor request is included. The IWF
uses its pre-configured MCPTT ID in the group call request.
2\. The MCPTT server sends a group call request(s) to the target MCPTT user(s)
as described in 3GPP TS 23.379 [7]. The LMR user is in a legacy conventional
FM radio system so E2EE is not specified, and transcoding is needed at the
IWF.
3\. MCPTT client(s) receiving the group call request, acknowledge towards the
MCPTT server by sending a group call response.
4\. The MCPTT server acknowledges the IWF group call request(s) by sending an
IWF group call response(s) to the IWF.
NOTE 2: How the IWF group call response(s) is handled in the IWF / LMR system
and how the other LMR users are being called is outside the scope of the
present document.
5\. The interworking group call has successfully established media plane for
communication and any user can transmit media. The LMR system where the
interworking group is defined is the controlling system of the group call and
manages the floor control.
NOTE 3: How the floor control is managed in the LMR system is outside the
scope of the present document.
6\. Because the group call request contained an implicit floor request, and no
other users are requesting the floor, the IWF sends an IWF floor taken message
to the MCPTT server confirming that the IWF has the floor. An individual IWF
floor taken message is sent to the MCPTT server for each affiliated MCPTT user
in the group, in this example scenario to the users in MCPTT clients 1 and 2.
7\. The MCPTT server sends Floor taken to the target MCPTT user(s) in the
MCPTT system. The MCPTT ID in the floor taken messages is the pre-configured
IWF MCPTT ID.
8\. At some time after media transfer begins, the IWF receives knowledge of
the LMR user\'s talker ID.
NOTE 4: How the IWF learns the LMR user\'s talker ID is outside the scope of
the present document. In some LMR conventional systems, the talker ID becomes
available shortly after the start of the call; in other systems, it is not
available until the end of the call.
9\. The IWF sends an IWF floor taken to the MCPTT server informing the server
that a new talker is using the floor, but the floor should not be released. An
individual IWF floor taken message is sent to the MCPTT server for each
affiliated MCPTT user in the group, in this example scenario to the users in
MCPTT clients 1 and 2
10\. The MCPTT server sends Floor taken messages to the target MCPTT user(s)
in the MCPTT system. The MCPTT ID in the floor taken messages is the new
talker ID contained in the IWF talker ID update.
NOTE 5: All other floor participants (not shown) that are part of this group
call receive a floor taken message, so that the other floor participants learn
the identity of the newly granted talker.
## 10.14 IWF functional alias management
### 10.14.1 General
LMR users homed in the IWF shall have the ability to enable, apply, or disable
a functional alias in the MC system for the use in communication with MC
service users. At least the IWF provide the functional alias management to
activate, deactivate etc. functional alias(es).
Editor\'s Note: The corresponding service profiles in the MC system for LMR
user homed to IWF are FFS.
Editor\'s Note: How the MC service server checks the authorization of the IWF
to perform functional alias related actions in the procedures in this
subclause is FFS.
### 10.14.2 IWF information flows for functional alias management
#### 10.14.2.1 IWF functional alias information query request
Table 10.14.2.1-1 describes the information flow of the functional alias
information query request from the user homed in the IWF to the MC service
server.
Table 10.14.2.1-1: IWF functional alias information query request
* * *
Information element Status Description MC service ID M The identity of the
user homed in the IWF who performs the query. MC service ID O The identity of
the MC service user to be queried. Functional alias O The functional alias to
be queried.
* * *
#### 10.14.2.2 IWF functional alias information query response
Table 10.14.2.2-1 describes the information flow of the functional alias
information query response from the MC service server to the user homed in the
IWF. This information flow is sent individually addressed on unicast.
Table 10.14.2.2-1: IWF functional alias information query response.
* * *
Information element Status Description MC service ID M The identity of the
user homed in the IWF who performed the query. MC service ID O The identity of
the MC service user that was queried. Functional alias O The functional alias
that was queried. Query result M The functional alias or MC service ID
information retrieved from the functional alias management server, i.e. the
list of activated functional alias identities of the MC service user or the
associated MC service IDs and status which correspond to the queried
functional alias.
* * *
#### 10.14.2.3 IWF functional alias activation request
Table 10.14.2.3-1 describes the information flow of the functional alias
activation request from the user homed in the IWF to the MC service server.
Table 10.14.2.3-1: IWF functional alias activation request
* * *
Information element Status Description MC service ID M The MC service ID of
the user homed in the IWF who triggers the functional alias activation
request. Functional alias list M A list of one or more functional aliases
which the originator intends to activate.
* * *
#### 10.14.2.4 IWF functional alias activation response
Table 10.14.2.4-1 describes the information flow of the functional alias
activation response from the MC service server to the user homed in the IWF.
This information flow is sent individually addressed on unicast.
Table 10.14.2.4-1: IWF functional alias activation response
* * *
Information element Status Description MC service ID M The MC service ID of
the user homed in the IWF who triggers the functional alias activation
request. Functional alias list M A list of one or more functional aliases
which the originator intended to activate. Activation status per functional
alias M Indicates the activation result for each functional alias in the list
(activated, rejected, can be taken over).
* * *
#### 10.14.2.5 IWF functional alias de-activation request
Table 10.14.2.5-1 describes the information flow functional alias de-
activation request from the user homed in the IWF to the MC service server.
Table 10.14.2.5-1: IWF functional alias de-activation request
* * *
Information element Status Description MC service ID M The MC service ID of
the user homed in the IWF who triggers the functional alias de-activation
request. Functional alias list M A list of one or more functional aliases
which the originator intends to de-activate.
* * *
#### 10.14.2.6 IWF functional alias de-activation response
Table 10.14.2.6-1 describes the information flow of the functional alias de-
activation response from the MC service server to the user homed in the IWF.
This information flow is sent individually addressed on unicast.
Table 10.14.2.6-1: IWF functional alias de-activation response
* * *
Information element Status Description MC service ID M The MC service ID of
the user homed in the IWF who triggers the functional alias de-activation
request. Functional alias list M A list of one or more functional aliases
which the originator intends to de-activate. De-activation status per
functional alias M Indicates the de-activation result for every functional
alias in the list.
* * *
#### 10.14.2.7 IWF functional alias status notification
Table 10.14.2.7-1 describes the information flow of the functional alias
notification from the MC service server to the user homed in the IWF. This
information flow may be sent individually addressed or group addressed on
unicast.
Table 10.14.2.7-1: IWF functional alias status notification
* * *
Information element Status Description MC service ID M The MC service ID of
the user homed in the IWF who triggers the functional alias activation, de-
activation or take over request. Functional alias list M A list of one or more
functional aliases. Operational status M Activation, de-activation or take
over status per functional alias.
* * *
#### 10.14.2.8 IWF Functional alias take over request
Table 10.14.2.8-1 describes the information flow of the functional alias take
over request from the user homed in the IWF to the MC service server.
Table 10.14.2.8-1: IWF functional alias take over request
* * *
Information element Status Description MC service ID M The MC service ID of
the user homed in the IWF of the originator who triggers the functional alias
take over request. Functional alias M A functional alias which the originator
intends to take over.
* * *
#### 10.14.2.9 IWF Functional alias take over response
Table 10.14.2.9-1 describes the information flow of the functional alias take
over response from the MC service server to the user homed in the IWF. This
information flow is sent individually addressed on unicast.
Table 10.14.2.9-1: IWF functional alias take over response
* * *
Information element Status Description MC service ID M The MC service ID of
the user homed in the IWF who triggers the functional alias activation
request. Functional alias M A functional alias which the requestor intends to
take over. Activation status per functional alias M Indicates the take over
request result (accepted, rejected).
* * *
#### 10.14.2.10 IWF Functional alias revoke notification
Table 10.14.2.10-1 describes the information flow of the functional revoke
notification from the MC service server to the user homed in the IWF. This
information flow is sent individually addressed on unicast.
Table 10.14.2.10-1: IWF functional alias revoke notification
* * *
Information element Status Description MC service ID M The MC service ID of
the user homed in the IWF of the originator who triggers the functional alias
take over request. Functional alias M The functional alias which is revoked.
* * *
### 10.14.3 IWF Functional alias management procedures
#### 10.14.3.1 General
The following subclauses describe the relevant functional alias management
procedures between the MC service system and the LMR system to enable role
based addressing of LMR users.
#### 10.14.3.2 User homed in the IWF retrieves active functional alias(es) for
a certain MC service user
An user homed in the IWF can request the active functional alias(es) for a
certain MC service user.
Figure 10.14.3.2-1 below illustrates the active functional alias list query
for a certain MC service user.
Figure 10.14.3.2-1: IWF active functional alias list query
1\. The user homed in the IWF requests a list of active functional aliases for
a certain MC service user from the MC service server by sending an IWF
functional alias information query request encompassing the MC service ID or
the functional alias of the queried user.
2\. The MC service server checks whether the querying MC service user is
authorized to perform the query. If authorized, then the MC service server
retrieves the requested functional alias information based on the
corresponding MC service ID or the MC service IDs based on the functional
alias.
3\. The MC service server sends an IWF functional alias information query
response including the active functional alias or MC service ID information to
the user homed in the IWF.
#### 10.14.3.3 User homed in the IWF activates functional alias(es) within an
MC system
The procedure for the user homed in the IWF activates functional alias(es)
within an MC system is illustrated in figure 10.14.3.3-1.
Pre-conditions:
1\. The user homed in the IWF has already been provisioned (statically or
dynamically) with the functional alias(es) information that the user homed in
the IWF is allowed to activate.
2\. MC service server may have retrieved the user subscription and functional
alias policy e.g. which user(s) are authorized to activate to what functional
alias, priority, and other configuration data.
3\. The user homed in the IWF may have indicated to the functional alias
management server that it wishes to receive updates of functional alias data
for the functional aliases for which it is authorized.
4\. The user homed in the IWF triggers the functional alias activation
procedure. This is an explicit activation caused either by the MC service user
or determined by a trigger event such as the MC service user coming within a
permitted geographic operational area of a functional alias.
Figure 10.14.3.3-1: IWF functional alias activation procedure within an MC
system
1\. The user homed in the IWF requests the MC service server to activate a
functional alias or a set of functional aliases.
2\. The MC service server checks if there are any conflicts with active
functional alias(es).
3\. If the user homed in the IWF is authorised to activate the requested
functional alias(es) then the MC service server stores the functional
alias(es) status of the requested functional alias(es).
If a certain functional alias(es) can be simultaneously active for multiple MC
service users and the upper limit of number of simultaneous MC service users
is not reached, the MC service shall activate the functional alias(es) for the
MC service user and inform all other MC service user(s) with sharing the same
functional alias(es) (step 5). If the limit of number of simultaneous MC
service users is reached or the functional alias is not allowed to be shared,
the request is rejected, and the MC service user is notified (step 4).
If the functional alias(es) is (are) already used by another MC service
user(s), an authorized MC service user gets an offer to take over the
functional alias from the MC service user currently using the functional
alias(es).
4\. MC service server sends an IWF functional alias(es) activation response to
the user homed in the IWF.
5\. The MC service server informs all other MC service user(s) and/or IWF
sharing the same functional alias(es).
#### 10.14.3.4 User homed in the IWF de-activates functional alias(es) within
an MC system
The procedure for the user homed in the IWF de-activates functional alias(es)
within an MC system is illustrated in figure 10.14.3.4-1.
When an user homed in the IWF does not want to use a functional alias(es)
anymore, then the user homed in the IWF can de-activate functional alias(es).
Pre-conditions:
1\. MC service server has already subscribed to the functional alias(es)
information from the functional alias management server and has stored the
data of the functional alias(es) a user homed in the IWF has activated.
2\. The user homed in the IWF triggers the functional alias(es) de-activation
procedure. This is an explicit de-activation request either by the user homed
in the IWF or determined by a trigger event such as the user moving outside a
permitted geographic operational area of a functional alias.
Figure 10.14.3.4-1: IWF functional alias de-activation procedure within an MC
system
1\. The user homed in the IWF requests the MC service server to de-activate a
functional alias or a set of functional aliases.
2\. Based on the MC service user subscription and stored functional alias
policy, the MC service server checks if the user homed in the IWF is
authorized to de-activate from the requested functional alias(es) and if the
user homed in the IWF has activated to the requested functional alias(es).
3\. If the user homed in the IWF is authorized to de-activate from the
requested functional alias(es) then the MC service server updates the
functional alias activation status of the MC service user.
4\. MC service server provides to the user homed in the IWF the functional
alias de-activation response.
5\. The MC service server informs all other MC service user(s) and/or users
homed in the IWF sharing the same functional alias(es).
#### 10.14.3.5 User homed in the IWF takes over functional alias(es) within an
MC system
The procedure for the user homed to IWF takes over functional alias(es) within
an MC system is illustrated in figure 10.14.3.5-1.
During functional alias(es) activation, if the functional alias(es) is (are)
already used by another MC service user(s), an authorized user homed in the
IWF may get an offer to take over the functional alias(es) from the MC service
user currently using the functional alias(es).
Pre-conditions:
1\. MC service client 1 has performed the functional alias(es) activation
procedure.
2\. As result of the functional alias(es) activation procedure, the user homed
in the IWF is aware which functional alias(es) are already used but can be
taken over.
3\. The user homed in the IWF decides to take over a functional alias.
Figure 10.14.3.5-1: IWF functional alias taking over procedure within an MC
system
1\. The user homed in the IWF requests the MC service server to take over a
functional alias by sending an IWF functional alias take over request.
2\. The MC service server checks if there are any conflicts taking over the
functional alias.
3\. If the user homed in the IWF is authorised to take over the requested
functional alias then the MC service server sends a functional alias revoke
notification to inform MC service client 2 that the functional alias has been
revoked and is not any longer active for the user of MC service client 2.
4\. The MC service server stores the functional alias status of the requested
functional alias.
5\. MC service server sends an IWF functional alias take over response to the
user homed in the IWF.
6\. The MC service server informs all other MC service user(s) including the
user homed in the IWF sharing the same functional alias.
## 10.15 First-to-answer call setup
### 10.15.1 Description
The present document specifies the interworking between LMR users and MCPTT
clients for first-to-answer calls. It can be used based on MCPTT IDs, or based
on functional alias for interworking with alternative addressing scheme used
by the LMR system.
### 10.15.2 Information flows for first-to-answer call
#### 10.15.2.1 IWF first-to-answer call request
Table 10.15.2.1-1 describes the information flow IWF first-to-answer call
request from the MCPTT server to the IWF and from the IWF to the MCPTT server.
Table 10.15.2.1-1: IWF first-to-answer call request information elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the calling
party Functional alias O The functional alias of the calling party MCPTT ID
(see NOTE) O The MCPTT ID of the called party Functional alias (see NOTE) O
The functional alias of the called party Use floor control indication M This
element indicates whether floor control will be used for the private call. SDP
offer O Media parameters of MCPTT client. Implicit floor request O An
indication that the user is also requesting the floor. Location information O
Location of the calling party NOTE: One of these information elements must be
present. If the information element MCPTT ID is present, it may consist of a
set of MCPTT IDs. If the information element functional alias is present it
must consist of a single functional alias.
* * *
#### 10.15.2.2 IWF first-to-answer call response
Table 10.15.2.2-1 describes the information flow IWF first-to-answer call
response from the MCPTT server to the IWF and from the IWF to the MCPTT
server.
Table 10.15.2.2-1: IWF first-to-answer call response information elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the calling
party Functional alias O The functional alias of the calling party MCPTT ID M
The MCPTT ID of the called party Functional alias O The functional alias of
the called party SDP answer M Media parameters selected
* * *
#### 10.15.2.3 IWF first-to-answer call cancel request
Table 10.15.2.3-1 describes the information flow IWF first-to-answer call
cancel request from the MCPTT server to the IWF and from the IWF to the MCPTT
server.
Table 10.15.2.3-1: IWF first-to-answer call cancel request information
elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the calling
party MCPTT ID M The MCPTT ID of the called party
* * *
#### 10.15.2.4 IWF first-to-answer call cancel response
Table 10.15.2.4-1 describes the information flow IWF first-to-answer call
cancel response from the MCPTT server to the IWF and from the IWF to the MCPTT
server.
Table 10.15.2.4-1: MCPTT first-to-answer call cancel response information
elements
* * *
Information Element Status Description MCPTT ID M The MCPTT ID of the called
party
* * *
### 10.15.3 Procedures
#### 10.15.3.1 MCPTT user initiating a first-to-answer call
In this procedure, an MCPTT user is initiating an MCPTT first-to-answer call
for communicating with an LMR user via an IWF.
Pre-conditions:
1\. The calling MCPTT user has selected first-to-answer call.
2\. The MCPTT client is registered to the MCPTT service, as per procedure in
subclause 10.2 in 3GPP TS 23.379 [7].
3\. The MCPTT server has subscribed to the MCPTT functional alias controlling
server within the MC system for functional alias activation/de-activation
updates.
Figure 10.15.3.1-1: MCPTT first-to-answer call initiated by MCPTT user
**1**. The MCPTT user at the MCPTT client initiates an MCPTT **first-to-
answer** call. The MCPTT client sends an MCPTT **first-to-answer** call
request towards the MCPTT server. The MCPTT **first-to-answer** call request
contains the MCPTT ID corresponding to the calling MCPTT party and called LMR
party, and an SDP offer containing one or more media types. The called LMR
party can consist of a set of potential target recipients represented by their
MCPTT IDs, or a functional alias. The following parameters are also included
that describe the MCPTT client\'s choices:
\- the encryption algorithm;
\- the encryption mode (encrypted or not);
\- an indication of whether the MCPTT client is requesting the floor, and if
the MCPTT client is requesting the floor, and
\- an indication of whether the call is to be full or half duplex (whether to
establish floor control).
2\. The MCPTT server checks whether the MCPTT user at the MCPTT client is
authorized to initiate the **first-to-answer** call. The MCPTT server checks
whether the provided functional alias of the calling user, if present, can be
used and has been activated for the MCPTT user.
3\. If authorized, the MCPTT server sends the IWF **first-to-answer** call
request that may or may not include location of the requestor, depending on
the outcome of the privacy check towards the IWF, including the original
parameters and offering the same media types or a subset of the media types
contained in the initial received request as per 3GPP TS 23.379 [7].
NOTE: How the IWF **first-to-answer** call request is forwarded to the LMR
system is out of scope of the present document.
4\. The IWF sends an IWF **first-to-answer** call response to the MCPTT
server, indicating that the IWF does support one of the requested media types.
The response indicates success or failure. If the indication is failure, the
response may include one or more alternatives to the parameter values
contained in step 3.
5\. The MCPTT server forwards the MCPTT **first-to-answer** call response to
the MCPTT client. If the result parameter indicates success, then the MCPTT
client proceeds to step 6. Otherwise, if the parameters returned in the MCPTT
**first-to-answer** call response are acceptable to the MCPTT client, then the
MCPTT client can send a new MCPTT **first-to-answer** call request with the
new parameters and behaves according to those parameters. The calling MCPTT
user may be notified of the change in parameters, for example, that the call
is to be without floor control. The MCPTT user can choose to end the call
rather than continue with the new parameters. If the parameters returned are
not acceptable to the MCPTT client, then the call fails.
6\. The MCPTT client has successfully established media plane for
communication to the IWF and either end can transmit media. The MCPTT system
initiating the call is responsible of granting the floor, solving competing
floor requests and issuing floor revoked indications.
#### 10.15.3.2 LMR user initiating a first-to-answer call
In this procedure, an MCPTT user is initiating an MCPTT first-to-answer call
for communicating with an LMR user via an IWF.
Pre-conditions:
1\. The calling LMR user has selected first-to-answer call
2\. The MCPTT client is registered to the MCPTT service, as per procedure in
subclause 10.2 in 3GPP TS 23.379 [7].
3\. The MCPTT server has subscribed to the MCPTT functional alias controlling
server within the MC system for functional alias activation/de-activation
updates.
Figure 10.15.3.2-1: MCPTT first-to-answer call initiated by MCPTT user
**1**. The IWF sends an IWF **first-to-answer** call request towards the MCPTT
server. The IWF **first-to-answer** call request contains the MCPTT ID
corresponding to the calling LMR party and called MCPTT party, and an SDP
offer containing one or more media types. The called MCPTT party can consist
of a set of potential target recipients represented by their MCPTT IDs, or a
functional alias. The following parameters are also included that describe the
LMR party\'s choices:
\- the encryption algorithm;
\- the encryption mode (encrypted or not);
\- an indication of whether the LMR user is requesting the floor, and if the
LMR user is requesting the floor, and
\- an indication of whether the call is to be full or half duplex (whether to
establish floor control).
2\. The MCPTT server checks whether the MCPTT user at the MCPTT client is
authorized to receive the **first-to-answer** call. The MCPTT server checks
whether the provided functional alias of the calling user, if present, can be
used and has been activated for the LMR user.
3\. If authorized, the MCPTT server sends the MCPTT **first-to-answer** call
request towards the MCPTT client, including the original parameters and
offering the same media types or a subset of the media types contained in the
initial received request as per 3GPP TS 23.379 [7].
4\. The MCPTT client sends an MCPTT **first-to-answer** call response to the
MCPTT server, indicating that the MCPTT client does support one of the
requested media types. The response indicates success or failure. If the
indication is failure, the response may include one or more alternatives to
the parameter values contained in step 3.
5\. The MCPTT server sends the IWF **first-to-answer** call response to the
IWF offering the same media type as that sent in step 4. If the parameters
returned are not acceptable to the IWF, then the call fails. If the parameters
returned in the IWF private call response are different but acceptable to the
IWF, then the IWF can send a new IWF private call request with the new
parameters starting with step 1, which is to essentially restart the call. If
there is no change of parameter, then the call proceeds to step 6.
6\. The MCPTT client has successfully established media plane for
communication to the IWF and either end can transmit media. The MCPTT system
initiating the call is responsible of granting the floor, solving competing
floor requests and issuing floor revoked indications.
#