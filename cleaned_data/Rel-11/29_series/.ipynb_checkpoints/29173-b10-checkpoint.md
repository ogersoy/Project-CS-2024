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
# 1 Scope
The present document describes the Diameter-based SLh interface between the
GMLC and the HSS defined for the Control Plane LCS in EPC.
LCS procedures over the SLh interface are defined in the 3GPP TS 23.271 [2].
This specification defines the Diameter application for the GMLC-HSS, SLh
reference point. The interactions between the HSS and the GMLC are specified,
including the signalling flows. As LCS procedures over the Diameter-based SLh
interface are identical to the MAP-based Lh interface, the descriptions of the
Lh MAP operations defined in the 3GPP TS 29.002 [3] are mapped into the
descriptions of the SLh Diameter commands.
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
> [2] 3GPP TS 23.271: \"Functional stage 2 description of Location Services
> (LCS)\".
>
> [3] 3GPP TS 29.002: \"Mobile Application Part (MAP) specification\".
[4] 3GPP TS 29.228: \"IP multimedia (IM) Subsystem Cx Interface; Signalling
flows and Message Elements\".
[5] IETF RFC 3588: \"Diameter Base Protocol\".
[6] 3GPP TS 33.210: \"3G security; Network Domain Security (NDS); IP network
layer security\".
[7] IETF RFC 4960: \"Stream Control Transport Protocol\".
[8] 3GPP TS 29.229: \"Cx and Dx Interfaces based on the Diameter protocol;
protocol details\".
[9] 3GPP TS 29.329: \"Sh Interface based on the Diameter protocol; protocol
details\".
[10] 3GPP TS 23.003: \"Numbering, addressing and identification \".
[11] 3GPP TS 23.012: \"Location Management Procedures\".
[12] 3GPP TS 29.272: \"Mobility Management Entity (MME) and Serving GPRS
Support Node (SGSN) related interfaces based on Diameter protocol\".
[13] IETF RFC 2234: \"Augmented BNF for syntax specifications\".
[14] 3GPP TS 29.234: \"3GPP system to Wireless Local Area Network (WLAN)
Interworking; Stage 3\".
[15] ITU-T Recommendation E.164: \"The international public telecommunication
numbering plan\".
# 3 Definitions, symbols and abbreviations
## 3.1 Definitions
For the purposes of the present document, the terms and definitions given in
3GPP TR 21.905 [1], 3GPP TS 23.271 [2] and the following apply. A term defined
in the present document takes precedence over the definition of the same term,
if any, in TR 21.905 [1].
## 3.2 Abbreviations
For the purposes of the present document, the abbreviations given in 3GPP TR
21.905 [1] and the following apply. An abbreviation defined in the present
document takes precedence over the definition of the same abbreviation, if
any, in 3GPP TR 21.905 [1].
ABNF Augmented Backus-Naur form
AVP Attribute Value Pair
H-GMLC Home-Gateway Mobile Location Centre
IANA Internet Assigned Numbers Authority
PMD Pseudonym mediation device functionality
PPR Privacy Profile Register
R-GMLC Requesting-Gateway Mobile Location Centre
RFC Request For Comments
V-GMLC Visited-Gateway Mobile Location Centre
# 4 General Description
## 4.1 Introduction
The SLh reference point between the GMLC and the HSS is defined in the 3GPP TS
23.271 [2].
This document describes the Diameter-based SLh interface related procedures,
message parameters and protocol specifications.
## 4.2 Architecture Overview
The architecture for support of Location Services in GSM, UMTS and EPS has
been defined in 3GPP TS 23.271 [2] and the relevant network elements and
interfaces are shown in the figure 4.2-1.
Figure 4.2-1: Overview of the LCS Functional Architecture
In this architecture, the SLh interface is defined between the Gateway Mobile
Location Center (GMLC) and the Home Subscriber Server (HSS) to allow the GMLC
to request routing information from the HLR or HSS.
## 4.3 Functional Requirements of SLh Interface
The requirements for SLh interface are defined in 3GPP TS 23.271 [2].
The SLh interface is used by the GMLC to request routing information from the
HSS i.e. the address of the H-GMLC, and/or the address of the visited MSC/MSC
server, SGSN, 3GPP AAA server or MME for a particular target UE whose location
has been requested.
# 5 Diameter-based SLh Interface
## 5.1 Introduction
This section describes the Diameter-based SLh interface related procedures and
Information elements exchanged between functional entities.
In the tables that describe the Information Elements transported by each
Diameter command, each Information Element is marked as (M) Mandatory, (C)
Conditional or (O) Optional in the \"Cat.\" column. For the correct handling
of the Information Element according to the category type, see the description
detailed in section 6 of the 3GPP TS 29.228 [4].
## 5.2 Procedure Descriptions
### 5.2.1 Send Routing Information for LCS
#### 5.2.1.1 General
This procedure is used between the GMLC and the HSS. The procedure is invoked
by the GMLC and is used:
\- To retrieve routing information for LCS for a specified user from the HSS.
This procedure is mapped to the commands LCS-Routing-Info-Request/Answer in
the Diameter application specified in chapter 6. Tables 5.2.1.1/1 and
5.2.1.1/2 detail the involved information elements.
Table 5.2.1.1/1: Send Routing Information for LCS (SLh-LCS-SRI)
+-------------------+-------------------+------+-------------------+ | Information | Mapping to | Cat. | Description | | element name | Diameter AVP | | | +-------------------+-------------------+------+-------------------+ | IMSI | User-Name | C | This information | | | | | element shall | | | | | contain the IMSI | | | | | of the targeted | | | | | user. This IE | | | | | shall be present | | | | | if the MSISDN is | | | | | absent. | +-------------------+-------------------+------+-------------------+ | MSISDN | MSISDN | C | This information | | | | | element shall | | | | | contain the | | | | | MSISDN of the | | | | | targeted user. | | | | | This IE shall be | | | | | present if the | | | | | IMSI is absent. | +-------------------+-------------------+------+-------------------+ | GMLC Number | GMLC-Number | O | This information | | | | | element shall | | | | | contain the ISDN | | | | | (E.164) number of | | | | | the requesting | | | | | GMLC. | +-------------------+-------------------+------+-------------------+ | Supported | S | O | If present, this | | Features | upported-Features | | information | | | | | element shall | | (See 3GPP TS | | | contain the list | | 29.229 [8]) | | | of features | | | | | supported by the | | | | | origin host. | +-------------------+-------------------+------+-------------------+
Table 5.2.1.1/2: Send Routing Information for LCS (SLh-LCS-SRI) Resp
+-------------------+-------------------+------+-------------------+ | Information | Mapping to | Cat. | Description | | element name | Diameter AVP | | | +-------------------+-------------------+------+-------------------+ | Result | Result-Code / | M | Result of the | | | Ex | | request. | | (See 5.3.5) | perimental-Result | | | | | | | Result-Code AVP | | | | | shall be used for | | | | | errors defined in | | | | | the Diameter Base | | | | | Protocol. | | | | | | | | | | Ex | | | | | perimental-Result | | | | | AVP shall be used | | | | | for SLh errors. | | | | | This is a grouped | | | | | AVP which | | | | | contains the 3GPP | | | | | Vendor ID in the | | | | | Vendor-Id AVP, | | | | | and the error | | | | | code in the | | | | | Experim | | | | | ental-Result-Code | | | | | AVP. | +-------------------+-------------------+------+-------------------+ | IMSI | User-Name | C | This information | | | | | element shall | | | | | contain the IMSI | | | | | of the targeted | | | | | user. This IE | | | | | shall be present | | | | | if the MSISDN is | | | | | absent. | +-------------------+-------------------+------+-------------------+ | MSISDN | MSISDN | C | This information | | | | | element shall | | | | | contain the | | | | | MSISDN of the | | | | | targeted user. | | | | | This IE shall be | | | | | present if the | | | | | IMSI is absent. | +-------------------+-------------------+------+-------------------+ | LMSI | LMSI | C | This information | | | | | element shall | | | | | contain the LMSI | | | | | allocated by the | | | | | VLR. If available | | | | | in the HSS, this | | | | | IE shall be | | | | | present only when | | | | | the Result- Code | | | | | is | | | | | DIAMETER_SUCCESS | | | | | and the serving | | | | | node is a VLR. | +-------------------+-------------------+------+-------------------+ | Serving Node | Serving-Node | C | This information | | | | | element shall | | | | | contain the | | | | | information about | | | | | the network node | | | | | serving the | | | | | targeted user | | | | | i.e. the | | | | | name/number of | | | | | the serving node | | | | | (MME, SGSN, 3GPP | | | | | AAA server or | | | | | MSC/MSC server), | | | | | the LCS | | | | | capabilities sets | | | | | supported by the | | | | | serving node and | | | | | the IP address of | | | | | the visited GMLC | | | | | associated with | | | | | the serving node. | | | | | This IE shall be | | | | | present only when | | | | | the Result- Code | | | | | is | | | | | D | | | | | IAMETER_SUCCESS. | +-------------------+-------------------+------+-------------------+ | Additional | Additi | C | This information | | Serving Node | onal-Serving-Node | | element shall | | | | | contain the | | | | | information about | | | | | another network | | | | | node serving the | | | | | targeted user. | | | | | This IE shall be | | | | | present only when | | | | | the Result- Code | | | | | is | | | | | D | | | | | IAMETER_SUCCESS. | | | | | There may be | | | | | multiple | | | | | instances of this | | | | | IE in the | | | | | response provided | | | | | by the HSS. | +-------------------+-------------------+------+-------------------+ | Home GMLC Address | GMLC-Address | C | This information | | | | | element shall | | | | | contain the IP | | | | | address of the | | | | | H-GMLC. This IE | | | | | shall be present | | | | | only when the | | | | | Result-Code is | | | | | D | | | | | IAMETER_SUCCESS. | +-------------------+-------------------+------+-------------------+ | PPR Address | PPR-Address | C | This information | | | | | element shall | | | | | contain the IP | | | | | address of the | | | | | Privacy Profile | | | | | Register (PPR). | | | | | If available in | | | | | the HSS, this IE | | | | | shall be present | | | | | only when the | | | | | Result-Code is | | | | | D | | | | | IAMETER_SUCCESS. | +-------------------+-------------------+------+-------------------+ | Supported | S | O | If present, this | | Features | upported-Features | | information | | | | | element shall | | (See 3GPP TS | | | contain the list | | 29.229 [8]) | | | of features | | | | | supported by the | | | | | origin host. | +-------------------+-------------------+------+-------------------+
#### 5.2.1.2 Detailed Behaviour of the HSS
Upon reception of the Send Routing Info for LCS request, the HSS shall, in the
following order:
1\. Check whether the requesting GMLC belongs to a network authorized to
request UE location information. If not, Experimental-Result shall be set to
DIAMETER_ERROR_UNAUTHORIZED_REQUESTING_NETWORK in the Send Routing Information
for LCS Response.
2\. Check that the User Identity for whom data is asked exists in HSS. If not,
Experimental-Result shall be set to DIAMETER_ERROR_USER_UNKNOWN in the Send
Routing Information for LCS Response.
3\. Check that there is serving node associated with the targeted user. If
not, Experimental-Result shall be set to DIAMETER_ERROR_ABSENT_USER in the
Send Routing Information for LCS Response.
If there is an error in any of the above steps then the HSS shall stop
processing and shall return the error code specified in the respective step
(see 3GPP TS 29.329 [9] and 3GPP TS 29.229 [8] for an explanation of the error
codes).
If the HSS cannot fulfil the received request for reasons not stated in the
above steps, e.g. due to a database error or empty mandatory data elements, it
shall stop processing the request and set Result-Code to
DIAMETER_UNABLE_TO_COMPLY.
Otherwise, the requested operation shall take place and the HSS shall return
the Result-Code AVP set to DIAMETER_SUCCESS. The HSS returns one or several of
the network addresses of the current MME, SGSN, 3GPP AAA server and/or
VMSC/MSC server, the LCS capabilities of the serving nodes if available, the
V-GMLC address associated with the serving nodes, if available, and whichever
of the IMSI and MSISDN that was not provided in the Send Routing Info for LCS
request. The HSS returns the address of the H-GMLC. The HSS also provides the
address of the PPR, if available.
Regarding the LCS capabilities of the serving nodes, if the HSS registered an
SGSN via the S6d reference point (i.e., the registered serving node is an
S4-SGSN), the HSS shall set the LCS-Capabilities-Set value to indicate support
of Capability Set 5 (i.e., LCS release 7 or later version). If the HSS
registered an MME, the HSS shall not indicate any LCS capability value to the
GMLC (i.e., the LCS-Capabilities-Set AVP shall be absent over SLh when the
serving node is an MME); in this case, the GMLC shall assume that the MME
supports LCS Capability Set 5.
#### 5.2.1.3 Detailed Behaviour of the GLMC
If there are a serving node as well as additional serving nodes in a
successful Send Routing Info for LCS response, the receiving shall use the
serving node in preference to the additional serving nodes.
# 6 Protocol Specification and Implementations
## 6.1 Introduction
### 6.1.1 Use of Diameter Base Protocol
The Diameter Base Protocol as specified in IETF RFC 3588 [5] shall apply
except as modified by the defined support of the methods and the defined
support of the commands and AVPs, result and error codes as specified in this
specification. Unless otherwise specified, the procedures (including error
handling and unrecognised information handling) shall be used unmodified.
### 6.1.2 Securing Diameter Messages
For secure transport of Diameter messages, see 3GPP TS 33.210 [6].
### 6.1.3 Accounting Functionality
Accounting functionality (Accounting Session State Machine, related command
codes and AVPs) shall not be used on the SLh interface.
### 6.1.4 Use of Sessions
Between the GMLC and the HSS, Diameter sessions shall be implicitly
terminated. An implicitly terminated session is one for which the server does
not maintain state information. The client shall not send any re-authorization
or session termination requests to the server.
The Diameter base protocol includes the Auth-Session-State AVP as the
mechanism for the implementation of implicitly terminated sessions.
The client (server) shall include in its requests (responses) the Auth-
Session-State AVP set to the value NO_STATE_MAINTAINED (1), as described in
IETF RFC 3588 [5]. As a consequence, the server shall not maintain any state
information about this session and the client shall not send any session
termination request. Neither the Authorization-Lifetime AVP nor the Session-
Timeout AVP shall be present in requests or responses.
### 6.1.5 Transport Protocol
Diameter messages over the SLh interface shall make use of SCTP IETF RFC 4960
[7] as transport protocol.
### 6.1.6 Routing Considerations
This clause specifies the use of the Diameter routing AVPs Destination-Realm
and Destination-Host.
If GMLC knows the address/name of the HSS for a certain user, both the
Destination-Realm AVP and the Destination-Host AVP shall be present in the
request. Otherwise, only the Destination-Realm AVP shall be present and the
command shall be routed to the next Diameter node. Consequently, the
Destination-Host AVP is declared as optional in the ABNF for all requests
initiated by a GMLC.
Destination-Realm AVP is declared as mandatory in the ABNF for all requests.
### 6.1.7 Advertising Application Support
The HSS and GMLC shall advertise support of the Diameter SLh Application by
including the value of the application identifier in the Auth-Application-Id
AVP within the Vendor-Specific-Application-Id grouped AVP of the Capabilities-
Exchange-Request and Capabilities-Exchange-Answer commands.
The vendor identifier value of 3GPP (10415) shall be included in the
Supported-Vendor-Id AVP of the Capabilities-Exchange-Request and Capabilities-
Exchange-Answer commands, and in the Vendor-Id AVP within the Vendor-Specific-
Application-Id grouped AVP of the Capabilities-Exchange-Request and
Capabilities-Exchange-Answer commands.
The Vendor-Id AVP included in Capabilities-Exchange-Request and Capabilities-
Exchange-Answer commands that is not included in the Vendor-Specific-
Application-Id AVPs as described above shall indicate the manufacturer of the
Diameter node as per RFC 3588 [5].
### 6.1.8 Diameter Application Identifier
The SLh interface protocol shall be defined as an IETF vendor specific
Diameter application, where the vendor is 3GPP. The vendor identifier assigned
by IANA to 3GPP (http://www.iana.org/assignments/enterprise-numbers) is 10415.
The Diameter application identifier assigned to the SLh interface application
is 16777291 (allocated by IANA).
### 6.1.9 User Identity to HSS resolution
The User identity to HSS resolution mechanism enables the GMLC (for non-
roaming case) or Diameter Relay/proxy agents in the home network (for roaming
case) to find the identity of the HSS that holds the LCS subscription data and
routing information for the target user when multiple and separately
addressable HSSs have been deployed in the home network. The resolution
mechanism is not required in networks that utilise a single HSS.
This User identity to HSS resolution mechanism may rely on routing
capabilities provided by Diameter and be implemented in the home operator
network within dedicated Diameter Agents (Redirect Agents or Proxy Agents)
responsible for determining the HSS identity based on the provided user
identity. If this Diameter based implementation is selected by the Home
network operator, the principles described in the 3GPP TS 29.272 [12] shall
apply.
NOTE: Alternatives to the user identity to HSS resolution Diameter based
implementation are outside the scope of this specification.
## 6.2 Commands
### 6.2.1 Introduction
This section defines the Command code values and related ABNF for each command
described in this specification.
### 6.2.2 Command-Code values
This section defines Command-Code values for the SLh interface application as
allocated by IANA.
Every command is defined by means of the ABNF syntax IETF RFC 2234 [13],
according to the rules in IETF RFC 3588 [5]. In the case, the definition and
use of an AVP is not specified in this document, the guidelines in IETF RFC
3588 [5] shall apply.
NOTE: For this release, the Vendor-Specific-Application-Id AVP is included as
an optional AVP in all commands in order to ensure interoperability with
diameter agents following a strict implementation of IETF RFC 3588 [5], by
which messages not including this AVP will be rejected. IETF RFC 3588 [5]
indicates that this AVP shall be present in all proxiable commands, such as
those specified here, despite that the contents of this AVP are redundant
since the application identifier is already present in the command header.
This AVP may be removed in subsequent revisions of this specification, once
the diameter base protocol is updated accordingly.
The following Command Codes are defined in this specification:
Table 6.2.2/1: Command-Code values for SLh
* * *
Command-Name Abbreviation Code Section LCS-Routing-Info-Request RIR 8388622
6.2.3 LCS-Routing-Info-Answer RIA 8388622 6.2.4
* * *
For these commands, the Application-ID field shall be set to 16777291
(application identifier of the SLh interface application, allocated by IANA).
### 6.2.3 LCS-Routing-Info-Request (RIR) Command
The LCS-Routing-Info-Request (RIR) command, indicated by the Command-Code
field set to 8388622 and the \"R\" bit set in the Command Flags field, is sent
from GMLC to HSS.
Message Format
> \ ::= \ 16777291 >
>
> \
>
> [ Vendor-Specific-Application-Id ]
>
> { Auth-Session-State }
>
> { Origin-Host }
>
> { Origin-Realm }
>
> [ Destination-Host ]
>
> { Destination-Realm }
>
> [ User-Name ]
>
> [ MSISDN ]
>
> [ GMLC-Number ]
>
> ***[ Supported-Features ]**
>
> *[ Proxy-Info ]
>
> *[ Route-Record ]
>
> *[ AVP ]
### 6.2.4 LCS-Routing-Info-Answer (RIA) Command
The LCS-Routing-Info-Answer (RIA) command, indicated by the Command-Code field
set to 8388622 and the \'R\' bit cleared in the Command Flags field, is sent
from HSS to GMLC.
Message Format
> \ ::= \
>
> \
>
> [ Vendor-Specific-Application-Id ]
>
> [ Result-Code ]
>
> [ Experimental-Result ]
>
> { Auth-Session-State }
>
> { Origin-Host }
>
> { Origin-Realm }
>
> ***[ Supported-Features ]**
>
> [ User-Name ]
>
> [ MSISDN ]
>
> [ LMSI ]
>
> [ Serving-Node ]
>
> *[ Additional-Serving-Node ]
>
> [ GMLC-Address ]
>
> [ PPR-Address ]
>
> *[ AVP ]
>
> *[ Failed-AVP ]
>
> *[ Proxy-Info ]
>
> *[ Route-Record ]
## 6.3 Result-Code AVP and Experimental-Result AVP Values
### 6.3.1 General
This section defines result code values that shall be supported by all
Diameter implementations that conform to this specification.
### 6.3.2 Success
Result codes that fall within the Success category shall be used to inform a
peer that a request has been successfully completed. The Result-Code AVP
values defined in Diameter Base Protocol RFC 3588 [5] shall be applied.
### 6.3.3 Permanent Failures
Errors that fall within the Permanent Failures category shall be used to
inform the peer that the request has failed, and should not be attempted
again. The Result-Code AVP values defined in Diameter Base Protocol RFC 3588
[5] shall be applied. When one of the result codes defined here is included in
a response, it shall be inside an Experimental-Result AVP and the Result-Code
AVP shall be absent.
#### 6.3.3.1 DIAMETER_ERROR_USER_UNKNOWN (5001)
This result code shall be sent by the HSS to indicate that the user identified
by the IMSI or the MSISDN is unknown. This error code is defined in 3GPP TS
29.229 [8]
#### 6.3.3.2 DIAMETER_ERROR_UNAUTHORIZED_REQUESTING_NETWORK (5490)
This result code shall be sent by the HSS to indicate that the requesting
GMLC\'s network is not authorized to request UE location information.
### 6.3.4 Transient Failures
Errors that fall within the transient failures category are those used to
inform a peer that the request could not be satisfied at the time that it was
received. The request may be able to be satisfied in the future.
#### 6.3.4.1 DIAMETER_ERROR_ABSENT_USER (4201)
This result code shall be sent by the HSS to indicate that the location of the
targeted user is not known at this time to satisfy the requested operation.
## 6.4 AVPs
### 6.4.1 General
The following table specifies the Diameter AVPs defined for the SLh interface
protocol, their AVP Code values, types, possible flag values and whether or
not the AVP may be encrypted. The Vendor-ID header of all AVPs defined in this
specification shall be set to 3GPP (10415).
Table 6.4.1/1: SLh specific Diameter AVPs
* * *
                                                                                                                                                                                                                                                                   AVP Flag rules
Attribute Name AVP Code Section defined Value Type Must May Should not Must
not May Encr. LMSI 2400 6.4.2 OctetString M, V No Serving-Node 2401 6.4.3
Grouped M, V No MME-Name 2402 6.4.4 DiameterIdentity M, V No MSC-Number 2403
6.4.5 OctetString M, V No LCS-Capabilities-Sets 2404 6.4.6 Unsigned32 M, V No
GMLC-Address 2405 6.4.7 Address M, V No Additional-Serving-Node 2406 6.4.8
Grouped M, V No PPR-Address 2407 6.4.9 Address M, V No MME-Realm 2408 6.4.12
DiameterIdentity V M No NOTE 1: The AVP header bit denoted as \"M\", indicates
whether support of the AVP is required. The AVP header bit denoted as \"V\",
indicates whether the optional Vendor-ID field is present in the AVP header.
For further details, see IETF RFC 3588 [5].
* * *
The following table specifies the Diameter AVPs re-used by the SLh interface
protocol from existing Diameter Applications, including a reference to their
respective specifications and when needed, a short description of their use
within SLh.
Any other AVPs from existing Diameter Applications, except for the AVPs from
Diameter Base Protocol, do not need to be supported. The AVPs from Diameter
Base Protocol are not included in table 6.4.1/2, but they may be re-used for
the SLh protocol.
Table 6.4.1/2: SLh re-used Diameter AVPs
* * *
Attribute Name Reference Comments MSISDN 3GPP TS 29.329 [9]  
SGSN-Number 3GPP TS 29.272 [12]  
Supported-Features 3GPP TS 29.229 [8]  
Feature-List-ID 3GPP TS 29.229 [8] See section 6.4.10 Feature-List 3GPP TS
29.229 [8] See section 6.4.11 GMLC-Number 3GPP TS 29.272 [12]  
3GPP-AAA-Server-Name 3GPP TS 29.234 [14]
* * *
### 6.4.2 LMSI
The LMSI AVP is of type OctetString and it shall contain the Local Mobile
Station Identity (LMSI) allocated by the VLR, as defined in 3GPP TS 23.003
[10]. For further details on the encoding of this AVP, see 3GPP TS 23.003[10].
### 6.4.3 Serving-Node
The Serving-Node AVP is of type Grouped. This AVP shall contain the
information about the network node serving the targeted user.
AVP format
> Serving-Node ::= \
>
> [ SGSN-Number ]
>
> [ MME-Name ]
>
> [ MME-Realm ]
>
> [ MSC-Number ]
>
> [ 3GPP-AAA-Server-Name ]
>
> [ LCS-Capabilities-Sets ]
>
> [ GMLC-Address ]
>
> *[AVP]
The GMLC-Address AVP included in the Serving-Node grouped AVP shall contain,
if present, the IPv4 or IPv6 address of the GMLC associated with the serving
node (i.e., either the home GMLC or the visited GMLC, depending on the
location of the serving node).
### 6.4.4 MME-Name
The MME-Name AVP is of type DiameterIdentity and it shall contain the Diameter
identity of the serving MME. For further details on the encoding of this AVP,
see IETF RFC 3588 [5].
### 6.4.5 MSC-Number
The MSC-Number AVP is of type OctetString and it shall contain the ISDN number
of the serving MSC or MSC server in international number format as described
in ITU-T Rec E.164 [15] and shall be encoded as a TBCD-string. See 3GPP TS
29.002 [3] for encoding of TBCD-strings.
### 6.4.6 LCS-Capabilities-Sets
The LCS-Capabilities-Sets AVP is of type Unsigned32 and it shall contain a bit
mask. The meaning of the bits shall be as defined in 3GPP 29.002 [3].
### 6.4.7 GMLC-Address
The GMLC-Address AVP is of type Address and shall contain the IPv4 or IPv6
address of H-GMLC or the V-GMLC associated with the serving node.
### 6.4.8 Additional-Serving-Node
The Additional-Serving-Node AVP is of type Grouped. This AVP shall contain the
information about the network node serving the targeted user.
AVP format
> Additional-Serving-Node ::= \
>
> [ SGSN-Number ]
>
> [ MME-Name ]
>
> [ MME-Realm ]
>
> [ MSC-Number ]
>
> [ 3GPP-AAA-Server-Name ]
>
> [ LCS-Capabilities-Sets ]
>
> [ GMLC-Address ]
>
> *[AVP]
The GMLC-Address AVP included in the Additional-Serving-Node grouped AVP shall
contain, if present, the IPv4 or IPv6 address of the GMLC associated with the
serving node (i.e., either the home GMLC or the visited GMLC, depending on the
location of the serving node).
### 6.4.9 PPR-Address
The PPR-Address AVP is of type Address and contains the IPv4 or IPv6 address
of the Privacy Profile Register for the targeted user.
### 6.4.10 Feature-List-ID AVP
The syntax of this AVP is defined in 3GPP TS 29.229 [8]. For this release, the
Feature-List-ID AVP value shall be set to 1.
### 6.4.11 Feature-List AVP
The syntax of this AVP is defined in 3GPP TS 29.229 [8]. A null value
indicates that there is no feature used by the application.
NOTE: There is no feature defined for this release.
### 6.4.12 MME-Realm
The MME-Realm AVP is of type DiameterIdentity and it shall contain the
Diameter Realm Identity of the serving MME. For further details on the
encoding of this AVP, see IETF RFC 3588 [5].
#