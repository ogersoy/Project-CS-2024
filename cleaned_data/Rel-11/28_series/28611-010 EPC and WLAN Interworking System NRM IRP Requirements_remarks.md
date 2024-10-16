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
**32.611: Telecommunication management; Evolved Packet** **Core** **(EPC) and
Wireless Local Area Network(WLAN) Interworking Network Resource Model (NRM)
Integration Reference Point (IRP); Requirements**
32.612: Telecommunication management; Evolved Packet Core (EPC) and Wireless
Local Area Network(WLAN) Interworking Network Resource Model (NRM) Integration
Reference Point (IRP); Information Service (IS)
32.616: Telecommunication management; Evolved Packet Core (EPC) and Wireless
Local Area Network(WLAN) Interworking Network Resource Model (NRM) Integration
Reference Point (IRP); Solution Set (SS) definitions
# 1 Scope
The document describes the NRM IRP requirements for EPC and WLAN interworking
system according to the structure defined in TS 23.402[8] (e.g. ePDG, 3GPP
AAA, etc).
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
[7] 3GPP TS 23.401: "General Packet Radio Service (GPRS) enhancements for
Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access".
[8] 3GPP TS 23.402: \"Technical Specification Group Services and System
Aspects ; Architecture enhancements for non-3GPP accesses\".
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
IRP Integration Reference Point
IOC Information Object Class
NRM Network Resource Model
> ePDG Evolved Packet Data Gateway
  1. Concepts and background =======================
The architectures of enhancement for non-3GPP access (i.e. WLAN) to 3GPP
system are defined in TS 23.402[8]. In the TS 23.402, three kinds of
architectures are defined, using S2a, S2b and S2c interface separately. The
architectures of S2a and S2c don't introduce new network elements in 3GPP
system, while the architecture S2b introduces a new network element to support
the interworking:
\- Evolved Packet Data Gateway (ePDG) (4.3.4 of [8]).
The above interworking related network element should be managed by 3GPP OAM,
and their corresponding NRM IRP need to be defined.
Based on the above characteristics, this specification defines the evolved
3GPP interworking WLAN NRM IRP requirements.
# 5 Requirements
The following general and high-level requirements apply for the present IRP:
A. IRP-related requirements in 3GPP TS 32.101 [2].
B. IRP-related requirements in 3GPP TS 32.102 [3].
C. IRP-related requirements in 3GPP TS 32.600 [4].
In addition to the above, the following more specific requirements apply:
**REQ-EPC_WLAN-CON-001** The Network Resource Model defined by this IRP shall
contain ePDG specific IOCs and related definitions. This requirement should be
satisfied when the S2b architecture is implemented.
**REQ-EPC_WLAN-CON-002** The Network Resource Model defined by this IRP shall
contain 3GPP AAA specific IOCs and related definitions.
**Editor's note:** The requirements for the new introduced interfaces in EPC
and WLAN Interworking system are FFS.
# Annex A (informative): Change history
* * *
**Change history**  
**Date** **TSG #** **TSG Doc.** **CR** **Rev** **Subject/Comment** **Old**
**New** Oct 2011 SA5-79 -- -- Initial version for TS skeleton --- 0.0.1 Feb
2012 SA5-81 Added NRM IRP requirements 0.0.1 0.1.0