# Foreword
This Technical Specification has been produced by the 3^rd^ Generation
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
# Introduction
The present document is part of a TS-family covering the 3^rd^ Generation
Partnership Project Technical Specification Group Services and System Aspects,
Telecommunication Management; as identified below:
28.601: Telecommunication management; Core Network (CN) and Wireless Local
Area Network(WLAN) Interworking Network Resource Model (NRM) Integration
Reference Point (IRP); Requirements
**28.602: Telecommunication management; Core Network (CN) and Wireless Local
Area Network (WLAN) Interworking Network Resource Model (NRM) Integration
Reference Point (IRP); Information Service (IS)**
> 28.606: Telecommunication management; Core Network (CN) and Wireless Local
> Area Network(WLAN) Interworking Network Resource Model (NRM) Integration
> Reference Point (IRP); Solution Set (SS) definitions
The present document is part of a set of specifications, which describe the
requirements and information model necessary for the standardised Operation,
Administration and Maintenance (OA&M) of a multi-vendor 3G-system.
Configuration Management (CM), in general, provides the operator with the
ability to assure correct and effective operation of the 3G network as it
evolves. CM actions have the objective to control and monitor the actual
configuration on the Network Elements (NEs) and Network Resources (NRs), and
they may be initiated by the operator or by functions in the Operations
Systems (OSs) or NEs.
CM actions may be requested as part of an implementation programme (e.g.
additions and deletions), as part of an optimization programme (e.g.
modifications), and to maintain the overall Quality of Service (QoS). The CM
actions are initiated either as single actions on single NEs of the 3G
network, or as part of a complex procedure involving actions on many
resources/objects in one or several NEs.
During the lifetime of a 3G network, its logical and physical configuration
will undergo changes of varying degrees and frequencies in order to optimise
the utilisation of the network resources. These changes will be executed
through network configuration management activities and/or network
engineering, see 3GPP TS 32.600 [4].
# 1 Scope
The present document is an Integration Reference Point (IRP) named \" Core
Network (CN) and Wireless Local Area Network (WLAN) Interworking Network
resources IRP \", through which an \'IRPAgent\' (typically an Element Manager
or Network Element) can communicate Configuration Management information to
one or several \'IRPManagers\' (typically Network Managers) concerning
interworking network resources.
According to the structure of IWLAN defined in TS 23.234[5], this document is
focusing the definition of NRM IRP IOC on 3GPP part (e.g. WAG, PDG, 3GPP AAA,
etc).
The present document specifies the protocol neutral interworking Network
Resources IRP: Network Resource Model. It reuses relevant parts of the generic
NRM in 3GPP TS 32.622 [6], either by direct reuse or sub-classing, and in
addition to that defines HNS specific Information Object Classes.
In order to access the information defined by this NRM, an IRP IS is needed,
such as the Basic CM IRP IS (3GPP TS 32.602 [7]) or the Bulk CM IRP IS (3GPP
TS 32.612 [8]). However, which IS that is applicable is outside the scope of
the present document.
The present document (NRM specification) is related to the IS in 3GPP TS
32.672 [9]
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
[1] 3GPP TS 25.905: \"Vocabulary for 3GPP Specifications\".
[2] 3GPP TS 32.101: \"Telecommunication management; Principles and high level
requirements\".
[3] 3GPP TS 32.102: \"Telecommunication management; Architecture\".
[4] 3GPP TS 32.600: \"Telecommunication management; Configuration Management
(CM); Concept and high-level requirements\".
[5] 3GPP TS 23.234: \"3GPP system to Wireless Local Area Network (WLAN)
interworking; System Description\".
[6] 3GPP TS 32.622: \"Telecommunication management; Configuration Management
(CM); Generic network resources Integration Reference Point (IRP): Network
Resource Model (NRM)\".
[7] 3GPP TS 32.602: \"Telecommunication management; Configuration Management
(CM); Basic Configuration Management Integration Reference Point (IRP):
Information Service (IS)\".
[8] 3GPP TS 32.612: \"Telecommunication management; Configuration Management
(CM); Bulk CM Integration Reference Point (IRP): Information Service (IS)\".
[9] 3GPP TS 32.672: \"Telecommunication management; Configuration Management
(CM); State Management Integration Reference Point (IRP): Information Service
(IS)\".
# 3 Definitions, symbols and abbreviations
## 3.1 Definitions
For the purposes of the present document, the following terms and definitions
apply. For terms and definitions not found here, please refer to 3GPP TS
32.101 [2], 3GPP TS 32.102 [3] and 3GPP TS 32.600 [4].
**Association:** In general it is used to model relationships between Managed
Objects. Associations can be implemented in several ways, such as:
(1) name bindings;
(2) reference attributes; and
(3) association objects.
This IRP stipulates that containment associations shall be expressed through
name bindings, but it does not stipulate the implementation for other types of
associations as a general rule. These are specified as separate entities in
the object models (UML diagrams).
**Managed Element (ME):** an instance of the Information Object Class
ManagedElement defined in 3GPP TS 32.622 [6].
**Managed Object (MO):** in the context of the present document, a Managed
Object (MO) is a software object that encapsulates the manageable
characteristics and behaviour of a particular Network Resource. The MO is
instance of a MO class defined in a MIM/NRM. This class, called **Information
Object Class (IOC)** has _attributes_ that provide information used to
characterize the objects that belong to the class (the term \"attribute\" is
taken from TMN and corresponds to a \"property\" according to CIM).
Furthermore, the IOC can have _operations_ that represent the behaviour
relevant for that class (the term \"operation\" is taken from TMN and
corresponds to a \"method\" according to CIM). The IOC may support the
emission of _notifications_ that provide information about an event occurrence
within a network resource.
**Management Information Model (MIM):** also referred to as NRM - see the
definition below.
**Network Resource Model (NRM):** a model representing the actual managed
telecommunications network resources that a System is providing through the
subject IRP\ An NRM identifies and describes IOCs, their associations,
attributes and operations. The NRM is also referred to as \"MIM\" (see above),
which originates from the ITU-T TMN.
## 3.2 Abbreviations
For the purposes of the present document, the following abbreviations apply:
IOCs Information Object Classes
# System Overview
## 4.1 Compliance rules
The following defines the meaning of Mandatory and Optional IOC attributes and
associations between IOCs, in Solution Sets to the IRP defined by the present
document:
  * The IRPManager shall support all mandatory attributes/associations. The IRPManager shall be prepared to receive information related to mandatory as well as optional attributes/associations without failure; however the IRPManager does not have to support handling of the optional attributes/associations.
  * The IRPAgent shall support all mandatory attributes/associations. It may support optional attributes/associations.
An IRPAgent that incorporates vendor-specific extensions shall support normal
communication with a 3GPP SA5‑compliant IRPManager with respect to all
Mandatory and Optional information object classes, attributes and associations
without requiring the IRPManager to have any knowledge of the extensions.
Given that
  * rules for vendor-specific extensions remain to be fully specified, > and
  * many scenarios under which IRPManager and IRPAgent interwork may > exist,
it is recognised that the IRPManager, even though it is not required to have
knowledge of vendor-specific extensions, may be required to be implemented
with an awareness that extensions can exist and behave accordingly.
# 5 Modelling approach
The modelling approach adopted and used in this IRP is described in TS 32.622
[6].
# 6 Information Object Classes
## 6.1 Information entities imported and local labels
## 6.2 Class diagram
### 6.2.1 Attributes and relationships
### 6.2.2 Inheritance
## 6.3 Information object class definitions
## 6.4 Information relationship definitions
## 6.5 Information attribute definitions
## 6.6 Common Notifications
### 6.6.1 Alarm and configuration notifications
### 6.6.2 Configuration notifications
# _Annex A: Change history_
* * *
**Change history**  
**Date** **TSG #** **TSG Doc.** **CR** **Rev** **Subject/Comment** **Old**
**New** Feb 2012 -- -- -- 0.0.1