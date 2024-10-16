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
In the present document, modal verbs have the following meanings:
**shall** indicates a mandatory requirement to do something
**shall not** indicates an interdiction (prohibition) to do something
The constructions \"shall\" and \"shall not\" are confined to the context of
normative provisions, and do not appear in Technical Reports.
The constructions \"must\" and \"must not\" are not used as substitutes for
\"shall\" and \"shall not\". Their use is avoided insofar as possible, and
they are not used in a normative context except in a direct citation from an
external, referenced, non-3GPP document, or so as to maintain continuity of
style when extending or modifying the provisions of such a referenced
document.
**should** indicates a recommendation to do something
**should not** indicates a recommendation not to do something
**may** indicates permission to do something
**need not** indicates permission not to do something
The construction \"may not\" is ambiguous and is not used in normative
elements. The unambiguous constructions \"might not\" or \"shall not\" are
used instead, depending upon the meaning intended.
**can** indicates that something is possible
**cannot** indicates that something is impossible
The constructions \"can\" and \"cannot\" are not substitutes for \"may\" and
\"need not\".
**will** indicates that something is certain or expected to happen as a result
of action taken by an agency the behaviour of which is outside the scope of
the present document
**will not** indicates that something is certain or expected not to happen as
a result of action taken by an agency the behaviour of which is outside the
scope of the present document
**might** indicates a likelihood that something will happen as a result of
action taken by some agency the behaviour of which is outside the scope of the
present document
**might not** indicates a likelihood that something will not happen as a
result of action taken by some agency the behaviour of which is outside the
scope of the present document
In addition:
**is** (or any other verb in the indicative mood) indicates a statement of
fact
**is not** (or any other negative verb in the indicative mood) indicates a
statement of fact
The constructions \"is\" and \"is not\" do not indicate requirements.
# Introduction
The present document is part of a TS-family covering the 3rd Generation
Partnership Project Technical Specification Group Services and System Aspects
Management and orchestration of networks, as identified below:
> 3GPP TS 28.540: Management and orchestration of 5G networks; Network
> Resource Model (NRM); Stage 1.
>
> **3GPP TS 28.541: Management and orchestration of 5G networks; Network
> Resource Model (NRM); Stage 2 and stage 3.**
# 1 Scope
The present document specifies the Information Model and Solution Set for the
Network Resource Model (NRM) definitions of NR, NG-RAN, 5G Core Network (5GC)
and network slice, to fulfil the requirements identified in 3GPP TS 28.540
[10].
The Information Model defines the semantics and behaviour of information
object class attributes and relations visible on the management interfaces in
a protocol and technology neutral way. And Solution Set defines one or more
solution set(s) with specific protocol(s) according to the Information Model
definitions.
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
[2] 3GPP TS 23.501: \"System Architecture for the 5G System\".
[3] 3GPP TS 38.300: \"NR; Overall description; Stage-2\".
[4] 3GPP TS 38.401: \"NG-RAN; Architecture description\".
[5] 3GPP TS 38.413: \"NG-RAN; NG Application Protocol (NGAP)\".
[6] 3GPP TS 38.420: \"NG-RAN; Xn general aspects and principles\".
[7] 3GPP TS 38.470: \"NG-RAN; F1 general aspects and principles\".
[8] 3GPP TS 38.473: \"NG-RAN; F1 application protocol (F1AP)\".
[9] 3GPP TS 37.340: \"NR; Multi-connectivity; Overall description; Stage 2\".
[10] 3GPP TS 28.540: \"Management and orchestration; 5G Network Resource Model
(NRM);Stage 1\".
[11] 3GPP TS 28.662: \"Telecommunication management; Generic Radio Access
Network (RAN) Network Resource Model (NRM) Integration Reference Point (IRP);
Information Service (IS) \".
[12] 3GPP TS 38.104: \"NR; Base Station (BS) radio transmission and
reception\".
[13] 3GPP TS 23.003: \"Numbering, Addressing and Identification\".
[14] 3GPP TS 36.410: \"Evolved Universal Terrestrial Radio Access Network
(E-UTRAN); S1 general aspects and principles\".
[15] 3GPP TS 36.423: \"Evolved Universal Terrestrial Radio Access Network
(E-UTRAN); X2 application protocol\".
[16] 3GPP TS 36.425: \"Evolved Universal Terrestrial Radio Access Network
(E-UTRAN); X2 interface user plane protocol\".
[17] 3GPP TS 28.625: \"State Management Data Definition Integration Reference
Point (IRP); Information Service (IS)\".
[18] Recommendation ITU-T X.731: \"Information technology - Open Systems
Interconnection - Systems Management: State management function\".
[19] 3GPP TS 28.658: \"Telecommunications management; Evolved Universal
Terrestrial Radio Access Network (E-UTRAN) Network Resource Model (NRM)
Integration Reference Point (IRP): Information Service (IS)\".
[20] 3GPP TS 28.702: \"Core Network (CN) Network Resource Model (NRM)
Integration Reference Point (IRP); Information Service (IS)\".
[21] 3GPP TS 28.708: \"**Telecommunication management; Evolved Packet Core
(EPC) Network Resource Model (NRM) Integration Reference Point (IRP):
Information Service (IS)\".**
[22] 3GPP TS 23.040: \"Technical realization of the Short Message Service
(SMS)\".
[23] 3GPP TS 29.510: \"5G system; Network Function Repository Services; Stage
3\".
[24] 3GPP TS 29.531: \"5G System; Network Slice Selection Services Stage 3\".
[25] Void.
[26] 3GPP TS 28.531: \"Management and orchestration; Provisioning\".
[27] 3GPP TS 28.554: \"Management and orchestration; 5G End to end Key
Performance Indicators (KPI)\".
[28] 3GPP TS 22.261: \"Service requirements for next generation new services
and markets\".
[29] ETSI GS NFV-IFA 013 (V2.4.1) (2018-02) \"Network Function Virtualisation
(NFV); Management and Orchestration; Os-Ma-nfvo Reference Point - Interface
and Information Model Specification\".
[30] 3GPP TS 28.622: \"Telecommunication management; Generic Network Resource
Model (NRM) Integration Reference Point (IRP); Information Service (IS)\".
[31] Void.
[32] 3GPP TS 38.211: \"NR; Physical channels and modulation\".
[33] 3GPP TS 32.616: \"Telecommunication management; Configuration Management
(CM); Bulk CM Integration Reference Point (IRP); Solution Set (SS)
definitions\".
[34] Void .
[35] 3GPP TS 28.532: \"Management and orchestration; Management services\".
[36] Void.
[37] IETF RFC 791: \"Internet Protocol\".
[38] IETF RFC 2373: \"IP Version 6 Addressing Architecture\".
[39] IEEE 802.1Q^TM^: \"Media Access Control Bridges and Virtual Bridged Local
Area Networks\".
[40] ETSI GR NFV-IFA 015 (V2.4.1): \"Network Function Virtualisation (NFV)
Release 2; Management and Orchestration; Report on NFV Information Model\".
[41] 3GPP TS 38.213: \"NR; Physical layer procedures for control\".
[42] 3GPP TS 38.101-1: \"NR; User Equipment (UE) radio transmission and
reception; Part 1: Range 1 Standalone\".
[43] 3GPP TS 32.156: \"Telecommunication management; Fixed Mobile Convergence
(FMC) model repertoire\".
[44] IETF RFC 4122: \"A Universally Unique IDentifier (UUID) URN Namespace\".
[45] IETF RFC 8528: \"YANG Schema Mount\".
[46] Void
[47] 3GPP TS 32.160: \"Management and orchestration; Management Service
Template\".
[48] 3GPP TS 38.463: \"NG-RAN; E1 application protocol (E1AP)\".
[49] 3GPP TS 38.304: \"NR; User Equipment (UE) procedures in Idle mode and RRC
Inactive state\".
[50] GSMA NG.116 - Generic Network Slice Template Version 2.0 (2019-10-16).
[51] 3GPP TS 22.104: \"Service requirements for cyber-physical control
applications in vertical domains; Stage 1\".
[52] 3GPP TS 33.501: \" Security architecture and procedures for the 5G
System\".
[53] 3GPP TS 38.901: \"Study on channel model for frequencies from 0.5 to 100
GHz \".
[54] 3GPP TS 38.331: \"NR; Radio Resource Control (RRC) protocol
specification\".
[55] 3GPP TS 38.215: \"NR; Physical layer measurements\".
[56] 3GPP TS 29.244: \"Technical Specification Group Core Network and
Terminals; Interface between the Control Plane and the User Plane Nodes; Stage
3\".
[57] 3GPP TS 28.313: \"Self-Organizing Networks (SON) for 5G networks\".
[58] 3GPP TS 38.423: \"NR; Xn application protocol (XnAP)\".
[59] 3GPP TS 23.503: \"Policy and Charging Control Framework for the 5G
System; Stage 2\".
[60] 3GPP TS 29.512: \"5G System; Session Management Policy Control Service;
Stage 3\".
[61] 3GPP TS 29.571: \"5G System; Common Data Types for Service Based
Interfaces; Stage 3\".
[62] 3GPP TS 29.214: \"Policy and Charging Control over Rx reference point\".
[63] IETF RFC 7042: \"IANA Considerations and IETF Protocol and Documentation
Usage for IEEE 802 Parameters\".
[64] IEEE 802.3-2015^TM^: \"IEEE Standard for Ethernet\".
[65] IEEE 802.1Q-2014^TM^: \"Bridges and Bridged Networks\".
[66] IETF RFC 4301: \"Security Architecture for the Internet Protocol\".
[67] 3GPP TS 29.514: \"5G System; Policy Authorization Service; Stage 3\".
[68] 3GPP TS 32.422: \"Telecommunication management; Subscriber and equipment
trace; Trace control and configuration management\"
[69] 3GPP TS 28.530: \"Management and orchestration; Concepts, use cases and
requirements\".
[70] 3GPP TS 28.310: \"Management and orchestration; Energy efficiency of
5G\".
# 3 Definitions and abbreviations
## 3.1 Definitions
For the purposes of the present document, the terms and definitions given in
3GPP TR 21.905 [1], 3GPP TS 28.540 [10] and the following apply. A term
defined in the present document takes precedence over the definition of the
same term, if any, in 3GPP TR 21.905 [1] and 3GPP TS 28.540 [10].
## 3.2 Abbreviations
For the purposes of the present document, the abbreviations given in 3GPP TR
21.905 [1], 3GPP TS 23.501 [2], 3GPP TS 38.401 [4], 3GPP TS 28.540 [10] and
the following apply. An abbreviation defined in the present document takes
precedence over the definition of the same abbreviation, if any, in 3GPP TR
21.905 [1], 3GPP TS 23.501 [2], 3GPP TS 38.401 [4] and TS 28.540 [10].
BWP Bandwidth Part
CM Configuration Management
DN Distinguished Name
IOC Information Object Class
JSON JavaScript Object Notation
NFV Network Functions Virtualisation
NRM Network Resource Model
NS Network Service
NSI Network Slice Instance
NSSAI Network Slice Selection Assistance Information
NSSI Network Slice Subnet Instance
PNF Physical Network Function
RIM Remote Interference Management
RIM-RS Remote Interference Management Reference Signal
SBA Service Based Architecture
SS Solution Set