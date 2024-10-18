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
The present document is part of a TS-family covering the 3^rd^ Generation
Partnership Project Technical Specification Group Services and System Aspects,
Telecommunication Management; as identified below:
**28.601: Telecommunication management; Core Network (CN) and Wireless Local
Area Network(WLAN) Interworking Network Resource Model (NRM) Integration
Reference Point (IRP); Requirements**
28.602: Telecommunication management; Core Network (CN) and Wireless Local
Area Network(WLAN) Interworking Network Resource Model (NRM) Integration
Reference Point (IRP); Information Service (IS)
> 28.606: Telecommunication management; Core Network (CN) and Wireless Local
> Area Network(WLAN) Interworking Network Resource Model (NRM) Integration
> Reference Point (IRP); Solution Set (SS) definitions
# 1 Scope
The document describes the NRM IRP requirements for IWLAN. According to the
structure of IWLAN defined in TS 23.234[6], this document is focusing the
definition of NRM IRP requirements on 3GPP part (e.g. WAG, PDG, 3GPP AAA,
etc).
# 2 References
The following documents contain provisions which, through reference in this
text, constitute provisions of the present document.
  * References are either specific (identified by date of publication, > edition number, version number, etc.) or non‑specific.
  * For a specific reference, subsequent revisions do not apply.
  * For a non-specific reference, the latest version applies. In the > case of a reference to a 3GPP document (including a GSM document), > a non-specific reference implicitly refers to the latest version > of that document _in the same Release as the present document_.
[1] 3GPP TS 25.905: \"Vocabulary for 3GPP Specifications\".
[2] 3GPP TS 32.101: \"Telecommunication management; Principles and high level
requirements\".
[3] 3GPP TS 32.102: \"Telecommunication management; Architecture\".
[4] 3GPP TS 32.600: \"Telecommunication management; Configuration Management
(CM); Concept and high-level requirements\".
[5] 3GPP TS 32.150: \"Telecommunication management; Integration Reference
Point (IRP) Concept and definitions\".
[6] 3GPP TS 23.234: \"3GPP system to Wireless Local Area Network (WLAN)
interworking; System Description\".
# 3 Definitions, symbols and abbreviations
## 3.1 Definitions
For the purposes of the present document, the following terms and definitions
apply:
**Integration Reference Point (IRP):** See 3GPP TS 32.150 [5].
**Information Service (IS):** See 3GPP TS 32.150 [5].
**Solution Set (SS):** See 3GPP TS 32.150 [5].
**IRP Solution Set:** See 3GPP TS 32.101 [1].
## Abbreviations
For the purposes of the present document, the following abbreviations apply:
AAA Access, Authentication and Authorisation
IRP Integration Reference Point
IOC Information Object Class
NRM Network Resource Model
WAG WLAN Access Gateway
PDG Packet Data Gateway
TTG Tunnel Terminating Gateway
  1. Concepts and background =======================
The architectures of interworking between 3GPP System and WLAN are defined in
TS 23.234[6]. According to the architecture, some new network elements or
functions are introduced to support the interworking:
> \- 3GPP AAA server (proxy/server) which is described in 6.2.2 and 6.2.3 of
> [6].
>
> \- WLAN Access Gateway (WAG) which is described in 6.2.5 of [6].
>
> \- Packet Data Gateway (PDG) which is described in 6.2.6 of [6].
>
> \- Tunnel Terminating Gateway (TTG) which is described in Annex F.5 of [6].
Based on the above characteristics, this specification defines 3GPP/WLAN
interworking NRM IRP requirements.
# 5 Requirements
The following general and high-level requirements apply for the present IRP:
A. IRP-related requirements in 3GPP TS 32.101 [2].
B. IRP-related requirements in 3GPP TS 32.102 [3].
C. IRP-related requirements in 3GPP TS 32.600 [4].
In addition to the above, the following more specific requirements apply:
**REQ-CN_WLAN-CON-001** The Network Resource Model defined by this IRP shall
contain WAG specific IOCs and related definitions.
**REQ-CN_WLAN-CON-002** The Network Resource Model defined by this IRP shall
contain PDG specific IOCs and related definitions.
**REQ-CN_WLAN-CON-003** The Network Resource Model defined by this IRP shall
contain 3GPP AAA specific IOCs and related definitions.
**Editor's note:** The requirements for the new introduced interfaces in CN
and WLAN interworking system are FFS.
#