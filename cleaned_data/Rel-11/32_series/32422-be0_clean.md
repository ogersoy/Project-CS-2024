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
The present document is part of a TS-family covering the 3rd Generation
Partnership Project; Technical Specification Group Services and System
Aspects; Telecommunication management, as identified below:
TS 32.421: \"Subscriber and equipment trace: Trace concepts and
requirements\";
**TS 32.422: \"Subscriber and equipment trace: Trace control and configuration
management\";**
TS 32.423: \"Subscriber and equipment trace: Trace data definition and
management\";
Additionally, there is a GSM only Subscriber and Equipment Trace
specification: 3GPP TS 52.008 [5].
Subscriber and Equipment Trace provide very detailed information at call level
on one or more specific mobile(s). This data is an additional source of
information to Performance Measurements and allows going further in monitoring
and optimisation operations.
Contrary to Performance Measurements, which are a permanent source of
information, Trace is activated on user demand for a limited period of time
for specific analysis purposes.
Trace plays a major role in activities such as determination of the root cause
of a malfunctioning mobile, advanced troubleshooting, optimisation of resource
usage and quality, RF coverage control and capacity improvement, dropped call
analysis, Core Network, UTRAN, EPC and E-UTRAN UMTS procedure validation.
The capability to log data on any interface at call level for a specific user
(e.g. IMSI) or mobile type (e.g. IMEI or IMEISV) allows getting information
which cannot be deduced from Performance Measurements such as perception of
end-user QoS during his call (e.g. requested QoS vs. provided QoS),
correlation between protocol messages and RF measurements, or interoperability
with specific mobile vendors.
Moreover, Performance Measurements provide values aggregated on an observation
period, Subscriber and Equipment Trace give instantaneous values for a
specific event (e.g., call, location update, etc.).
If Performance Measurements are mandatory for daily operations, future network
planning and primary trouble shooting, Subscriber and Equipment Trace is the
easy way to go deeper into investigation and network optimisation.
In order to produce this data, Subscriber and Equipment Trace are carried out
in the NEs, which comprise the network. The data can then be transferred to an
external system (e.g. an Operations System (OS) in TMN terminology, for
further evaluation).
# 1 Scope
The present document describes the mechanisms used for the control and
configuration of the Trace, Minimization of Drive Test (MDT) and Radio Link
Failure (RLF) reporting functionality at the EMs, NEs and UEs. For Trace
functionality, it covers the triggering events for starting/stopping of
subscriber/UE activity traced over 3GPP standardized signalling interfaces,
the types of trace mechanisms, configuration of a trace, level of detail
available in the trace data, the generation of Trace results in the Network
Elements (NEs) and User Equipment (UE) and the transfer of these results to
one or more EM(s) and/or Network Manager(s) (NM(s)). For MDT, it also covers
logged MDT and immediate MDT mechanims in both area based and signalling based
scenarios. GSM is excluded from the RAT systems which the present document can
be applied to.
The mechanisms for Trace, MDT and RLF reporting activation/deactivation are
detailed in clause 4; clause 5 details the various Trace, MDT and RLF
reporting control and configuration parameters and the triggering events that
can be set in a network. Trace, MDT and RLF reporting concepts and
requirements are covered in 3GPP TS 32.421 [2] while Trace and MDT data
definition and management is covered in 3GPP TS 32.423 [3].
The conditions for supporting Network Sharing are stated in 3GPP TS 32.421
[2].
# 2 References
The following documents contain provisions, which, through reference in this
text, constitute provisions of the present document.
  * References are either specific (identified by date of publication, > edition number, version number, etc.) or non‑specific.
  * For a specific reference, subsequent revisions do not apply.
  * For a non-specific reference, the latest version applies. In the > case of a reference to a 3GPP document (including a GSM document), > a non-specific reference implicitly refers to the latest version > of that document _in the same Release as the present document_.
NOTE: Overall management principles are defined in 3GPP TS 32.101 [1].
[1] 3GPP TS 32.101: \"Telecommunication management; Principles and high level
requirements\".
[2] 3GPP TS 32.421: \"Telecommunication management; Subscriber and equipment
trace: Trace concepts and requirements\".
[3] 3GPP TS 32.423: \"Telecommunication management; Subscriber and equipment
trace: Trace data definition and management\".
[4] 3GPP TR 21.905: \"Vocabulary for 3GPP Specifications\".
[5] 3GPP TS 52.008: \"Telecommunication management; GSM subscriber and
equipment trace\".
[6] 3GPP TS 23.060: \"General Packet Radio Service (GPRS) Service description;
Stage 2\".
[7] 3GPP TS 23.205: \"Bearer-independent circuit-switched core network; Stage
2\".
[8] 3GPP TS 23.108: \"Mobile radio interface layer 3 specification, core
network protocols; Stage 2 (structured procedures)\".
[9] 3GPP TS 23.246: \"Multimedia Broadcast/Multicast Service (MBMS);
Architecture and functional description\".
[10] 3GPP TS 29.232: \"Media Gateway Controller (MGC) - Media Gateway (MGW);
interface; Stage 3\".
[11] 3GPP TS 29.002: \"Mobile Application Part (MAP) specification\".
[12] 3GPP TS 29.060: \"General Packet Radio Service (GPRS); GPRS Tunnelling
Protocol (GTP) across the Gn and Gp interface\".
[13] 3GPP TS 25.413: \"UTRAN Iu interface Radio Access Network Application
Part (RANAP) signalling\".
[14] 3GPP TS 23.218: \"IP Multimedia (IM) session handling; IM call model;
Stage 2\".
[15] 3GPP TS 23.228: \"IP Multimedia Subsystem (IMS); Stage 2\".
[16] 3GPP TS 29.228: \"IP Multimedia (IM) Subsystem Cx and Dx Interfaces;
Signalling flows and message contents\".
[17] 3GPP TS 29.328: \"IP Multimedia Subsystem (IMS) Sh interface; Signalling
flows and message contents\".
[18] Void.
[19] Void.
[20] Void.
[21] 3GPP TS 23.401: \"General Packet Radio Service (GPRS) enhancements for
Evolved Universal Terrestrial Radio Access Network (E-UTRAN) access\".
[22] 3GPP TS 23.402: \"Architecture enhancements for non-3GPP accesses\".
[23] 3GPP TS 36.401: \"Evolved Universal Terrestrial Radio Access Network
(E-UTRAN); Architecture description\".
[24] 3GPP TS 32.442: \"Telecommunication management; Trace management
Integration Reference Point (IRP); Information Service (IS)\".
[25] 3GPP TS 29.273: \"Evolved Packet System (EPS); 3GPP EPS AAA interfaces\".
[26] 3GPP TS 29.272: \"Evolved Packet System (EPS); Mobility Management Entity
(MME) and Serving GPRS Support Node (SGSN) related interfaces based on
Diameter protocol\".
[27] 3GPP TS 32.615: \"Telecommunication management; Configuration Management
(CM); Bulk CM Integration Reference Point (IRP): eXtensible Markup Language
(XML) definitions\".
[28] 3GPP TS 32.342: \"Telecommunication management; File Transfer (FT)
Integration Reference Point (IRP): Information Service (IS)\".
[29] 3GPP TS 29.212: \" **Policy and Charging Control (PCC);Reference points**
\".
[30] 3GPP TS 37.320: \"Universal Terrestrial Radio Access (UTRA) and Evolved
Universal Terrestrial Radio Access (E-UTRA); Radio measurement collection for
Minimization of Drive Tests (MDT);Overall description; Stage 2\".
[31] 3GPP TS 25.331: \"Radio Resource Control (RRC); Protocol specification\"
[32] 3GPP TS 36.331: \"Evolved Universal Terrestrial Radio Access (E-UTRA);
Radio Resource Control (RRC); Protocol specification\".
[33] 3GPP TS 24.301: \"Non-Access-Stratum (NAS) protocol for Evolved Packet
System (EPS); Stage 3\".
[34] 3GPP TS 29.274: \"3GPP Evolved Packet System (EPS); Evolved General
Packet Radio Service (GPRS) Tunnelling Protocol for Control plane (GTPv2-C);
Stage 3\".
[35] 3GPP TS 32.622: \"Telecommunication management; Configuration Management
(CM); Generic network resources Integration Reference Point (IRP): Network
Resource Model (NRM)\".
[36] 3GPP TS 36.413: \"Evolved Universal Terrestrial Radio Access Network
(E-UTRAN); S1 Application Protocol\".
[37] 3GPP TS 36.300: \"Evolved Universal Terrestrial Radio Access (E-UTRA) and
Evolved Universal Terrestrial Radio Access Network (E-UTRAN): Overall
description stage 2\".
[38] 3GPP TS 36.214:\"Evolved Universal Terrestrial Radio Access (E-UTRA);
Physical layer - Measurements\".
# 3 Definitions and abbreviations
## 3.1 Definitions
For the purposes of the present document, the terms and definitions given in
TR 21.905 [4] and the following apply. A term defined in the present document
takes precedence over the definition of the same term, if any, in TR 21.905
[4].
**Area based MDT:** MDT data is collected from UEs in a specified area. The
area is defined as a list of cells (UTRAN or E-UTRAN) or as a list of
tracking/routing/location areas. The area based MDT is an enhancement of the
management based trace functionality. Area based MDT can be either a logged
MDT or Immediate MDT.
**Immediate MDT:** Collection of UE measurements in connected mode.
**Logged MDT:** Collection of UE measurements in idle mode.
**Signalling based MDT:** MDT data is collected from one specific UE. The UE
that is participating in the MDT data collection is specified as IMEI(SV) or
as IMSI. The signalling based MDT is an enhancement of the signalling based
subscriber and equipment trace. A signalling based MDT can be either a logged
MDT or Immediate MDT.
## 3.2 Abbreviations
For the purposes of the present document, the abbreviations given in TR 21.905
[4], 3GPP TS 32.101 [1] and the following apply. An abbreviation defined in
the present document takes precedence over the definition of the same
abbreviation, if any, in TR 21.905 [4].
AS Application Server
BGCF Breakout Gateway Control Function
CSCF Call Session Control Function
I-CSCF Interrogating-CSCF
IM CN SS IP Multimedia Core Network Subsystem
IMEI-TAC IMEI Type Allocation Code
MRFC Multimedia Resource Function Controller
MDT Minimization of Drive Tests
P-CSCF Proxy - CSCF
RCEF RRC Connection Establishment Failure
RLF Radio Link Failure
S-CSCF Serving-CSCF
TAU Tracking Area Update
# 4 Trace/UE measurements activation and deactivation
## 4.1 Trace Session activation / deactivation for Trace and MDT
### 4.1.1 Management activation
#### 4.1.1.1 General
In Management activation, the Trace Control and Configuration parameters are
sent directly to the concerned NE (by its EM). This NE shall not propagate the
received data to any other NE\'s - whether or not it is involved in the actual
recording of the call.
Once the parameters have been provided, the NE looks for the IMSI or IMEI
(IMEISV) passing through it. If it does not have them, these shall be provided
to the NE (that performs the trace recording) as part of traffic signalling by
the CN.
The following figure represents the management based trace functionality
within a PLMN. The figure represents a typical PLMN network. A dotted arrow
with \"Trace Parameter Configuration\" represents the availability of the
management based trace functionality at the EM for that domain.
NOTE: There is no propagation of trace parameters in management based trace
activation.
Figure 4.1.1.1.1: Overview of management activation for an UMTS system
If the NE failed to activate the Trace Session, a Trace failure notification
shall be sent to the TCE, and the Trace failure notification has the the same
parameters as the notification notifyTraceRecordingSessionFailure defined in
3GPP TS 32.442 [24], the Trace failure notification file XML schema is defined
in Annex A.
#### 4.1.1.2 UTRAN activation mechanisms
When an RNC receives Trace Session activation from the EM it shall start a
Trace Session. The trace control and configuration parameters of the Trace
Session are received in Trace Session activation from the EM. The RNC shall
not forward these trace control and configuration parameters to other nodes.
The received trace control and configuration parameters shall be saved and
used to determine when and how to start a Trace Recording Session. (Starting a
Trace Recording Session is described in subclause 4.2.2.1). A Trace Session
may be requested for a limited geographical area.
Since a RNC has visibility of an IMSI, it can start an IMSI Trace all by
itself when a Trace session is requested for an IMSI or a list of IMSI's.
However, a RNC does not have visibility of the IMEI(SV). Hence, when a Trace
session is requested for an IMEI(SV) or a list of IMEI(SV), the RNC shall send
the requested IMEI(SV) / list of IMEI(SV)s in an \'Uplink Information Exchange
Request\' message to the interacting MSC Server(s) and SGSN(s). The MSC
Servers and SGSNs shall store the requested IMEI(SV)s per RNC. For each
subscriber/UE activity the MSC Servers and SGSNs shall request IMEI(SV), if it
is not already provided. For each subscriber/UE activity the MSC server/SGSN
shall check whether a trace request is active in an RNC for the IMEI(SV). If a
match is found, the MSC Server/SGSN shall inform the RNC about the IMEI(SV) in
CN Invoke Trace, so that the RNC can trace the control signalling according to
the trace control and configuration parameters that are received from its EM.
If an Inter-MSC SRNS Relocation or an Inter-SGSN SRNS relocation occurs, the
anchor MSC Server or source SGSN shall transfer the IMSI and IMEI(SV) for the
subscriber/UE activity to the non anchor MSC Server or target SGSN. The non
anchor MSC Server/target SGSN shall check whether it has received a trace
request from the target RNC for the transferred IMEI(SV). If a match is found
on the IMEI(SV) in the non anchor MSC Server/target SGSN, the MSC Server/SGSN
shall inform the RNC about the IMEI(SV) in the CN Invoke Trace. The IMSI shall
be transferred from the non anchor MSC Server/target SGSN to the target RNC in
Relocation Request. The RNC can then trace the subscriber/UE activity
according to the trace control and configuration parameters that are received
from its EM.
#### 4.1.1.2a UTRAN activation mechanisms for area based MDT data collections
without IMSI/IMEI(SV) selection
In case of area based MDT data collection, the UE selection should be done in
the radio network at RNC based on the input information received from OAM,
like device capability information and area scope. In this case there is no
IMSI, IMEI(SV) selection.
The following figure shows an example scenario how the MDT configuration is
done utilising the cell traffic trace functionality:
Figure 4.1.1.2a.1: Example for area based MDT activation in UTRAN
1) The EM sends a Trace Session activation request to the RNC. This request
includes the parameters for configuring MDT data collection:
> \- The area where the MDT data should be collected: list of UTRAN cells.
> Routing Area or Location Area should be converted to UTRAN cells.
>
> \- Job type
>
> \- List of measurements
>
> \- Reporting Trigger (only in case of Immediate MDT)
>
> \- Report Interval (only in case of Immediate MDT)
>
> \- Report Amount (only in case of Immediate MDT)
>
> \- Event Threshold (Only in case of Immediate MDT)
>
> \- Logging Interval (Only in case of Logged MDT)
>
> \- Logging Duration (Only in case of Logged MDT)
>
> \- Trace Reference
>
> \- IP address of TCE
>
> \- Anonymization of MDT data.
>
> \- Measurement quantity
>
> \- Measurement Period UMTS (Only in case of Immediate MDT and if either of
> the measurements M6, M7 is requested in the list of measurement parameter).
>
> \- Collection period for RRM measurements UMTS (present only if any of M3,
> M4 or M5 measurements are requested).
>
> \- Positioning method
2) When RNC receives the Trace Session activation request from its EM, it
shall start a Trace Session and should save the parameters associated to the
Trace Session.
3) Void.
4) RNC shall select the suitable UEs for MDT data collection. The selection is
based on the area received from the EM and the area where UE is roaming, user
consent information received from the core network (As described in clause
4.6.2 of the present document).If the user is not in the specified area or if
the **_Management Based MDT Allowed_ IE is not received from the Core Network
(which indicates lacking user consent)**the UE shall not be selected by the
RNC for MDT data collection. During UE selection , the RNC shall take into
account also the UE capability (MDT capability) when it selects UE for logged
MDT configuration. If the UE does not support logged MDT the UE shall not be
selected. The RNC should also start the Data Volume measurement if it is
requested in the MDT configuration.
5) RNC shall activate the MDT functionality to the selected UEs. As part of
this operation the RNC shall allocate a Trace Recording Session Reference and
send at least the following configuration information to the UE in case of
Logged MDT:
> \- Trace Reference
>
> \- Trace Recording Session Reference
>
> \- TCE Id (The value signalled as IP address of TCE from the EM is mapped to
> a TCE Id, using a configured mapping in the RNC)
>
> \- Logging Interval
>
> \- Logging duration
>
> \- Absolute time reference
>
> \- The area where the MDT data should be collected: list of UTRAN
> cells/RA/LA
>
> In case of Immediate MDT only the measurements and their parameters needs to
> be sent to the UE:
\- List of measurements
\- Reporting trigger
\- Report Interval
\- Report Amount
\- Event threshold (only if event based reporting is configured in reporting
trigger)
6) When UE receives the MDT activation it shall start the MDT functionality
based on the received configuration parameters. The MDT related measurements
are reported to the RNC via RRC signalling. In case of Logged MDT the MDT
reporting is done when the network requests the log The MDT log is requested
if UE's rPLMN matches the PLMN where TCE used to collect MDT data resides
(e.g. RNC's primary PLMN) by sending the UEInformationRequest message. The MDT
log is sent by the UE in the UEInformationResponse message. If the MDT
anonymization requires the IMEI-TAC in the MDT record, RNC shall send the
Trace Recording Session Reference, Trace Reference, serving Cell Identifier
(containing serving cell PLMN and Cell ID, for immediate MDT only), TCE IP
address and IMSI in the UPLINK INFORMATION EXCHANGE REQUEST message to the
SGSN/MSC Server via Iu connection. When SGSN/MSC Server receives this Iu
signalling message containing the Trace Recording Session Reference, Trace
Reference, TCE IP address, IMSI, the SGSN/MSC Server shall look up the
corresponding equipment identities (IMEI (SV)) of the given IMSI from its
database, and send the IMEI-TAC together with the Trace Recording Session
Reference and Trace Reference to the TCE, as described in section 4.7 of the
present document. For logged MDT, SGSN/MSC Server shall send the IMEI-TAC
together with the Trace Recording Session Reference, Trace Reference to the
TCE.
> For immediate MDT, RNC shall include the serving cell identifier in the
> UPLINK INFORMATION EXCHANGE REQUEST message.
The UE should report the Trace Reference, Trace Recording Session Reference
and TCE Id together with the MDT reports to the network in case of Logged MDT.
7) When RNC receives the MDT report from the UE the RNC shall compare the
Trace PLMN (PLMN portion of Trace Reference) with the PLMN where TCE used to
collect MDT data resides (e.g. its primary PLMN). In case of a match, for
immediate MDT, it shall capture it and put the UE's serving cell CGI together
with the MDT report from the UE to the trace record. In case of a match, for
logged MDT, the RNC shall capture it and put it to the trace record. Otherwise
it shall discard the MDT report.
NOTE: For area based Immediate MDT, TRSR may be duplicated among different
RNCs when multiple cells are selected as the area scope for the same MDT job.
In this case, the combination of TRSR and the UE's serving cell CGI in the MDT
report can uniquely identify one trace recording session.
8) The Trace Records shall be forwarded to the Trace Collection Entity
indicated in the MDT report received from the UE in case of Logged MDT. The
RNC translates the TCE Id received from the UE to the TCE IP address before it
forwards the measurement records to the TCE. (The address translation is done
by using configured mapping in the RNC.) The RNC shall not provide the IMSI in
the MDT.
The Immediate MDT measurement configuration is deleted in the UE together with
the RRC context when entering idle mode.
**The Logged MDT trace session is preserved in the UE until the duration time
of the trace session expires, including also multiple idle periods interrupted
by idle-connected-idle state transitions.**
**The Logged MDT trace session context of the UE is stored in the network as
long as the trace session is active, including also the periods when the UE is
in connected state.**
EM shall validate that the MCC and MNC in the Trace reference is the same as
the PLMN supported by all the RNCs specified in the area scope. If the RNC
receives a request with a PLMN in the TraceReference that does not match any
PLMN in its list, it shall ignore the request.
#### 4.1.1.3 PS Domain activation mechanisms
When a SGSN, GGSN or BM-SC receives Trace Session activation from the EM it
shall start a Trace Session. The trace control and configuration parameters of
the Trace Session are received in the Trace Session activation from the EM.
The SGSN/GGSN/BM-SC shall not forward these trace control and configuration
parameters to other nodes. The received trace control and configuration
parameters shall be saved and used to determine when and how to start a Trace
Recording Session. (Starting a Trace Recording Session is described in
subclause 4.2.2.2).
#### 4.1.1.4 CS Domain activation mechanisms
When a MSC Server receives Trace Session activation from the EM it shall start
a Trace Session. The trace control and configuration parameters of the Trace
Session are received in the Trace Session activation from the EM. The MSC
Server shall not forward these trace control and configuration parameters to
other nodes. The received trace control and configuration parameters shall be
saved and used to determine when and how to start a Trace Recording Session.
(Starting a Trace Recording Session is described in subclause 4.2.2.3).
#### 4.1.1.5 IP Multimedia Subsystem activation mechanisms
When a S-CSCF/P-CSCF receives Trace Session activation from EM, the
S-CSCF/P-CSCF shall start a Trace Session. The Trace control and configuration
parameters of the Trace Session, received from EM in the Trace Session
activation, shall be saved. The Trace control and configuration parameters
define when the S-CSCF and P-CSCF shall start and stop a Trace Recording
Session. For detailed information on starting and stopping Trace Recording
Session in IMS see sub clauses 4.2.2.4 and 4.2.4.4.
The following figure illustrates the Trace Session activation in S-CSCF and in
P-CSCF in case of Management based activation.
Figure 4.1.1.5.1: Trace Session activation in IMS
#### 4.1.1.6 E-UTRAN activation mechanisms
In E-UTRAN the Management Based Trace Activation can be fulfilled with the
E-UTRAN Cell Traffic trace functionality. In this case the Trace Session
Activation is done to one or a list E-UTRAN cells within one eNodeB, where
Trace Session is activated.
The following trace control and configuration parameters of the Trace Session
are received by eNodeB in the Trace Session activation message from the EM:
  * Trace Reference
  * Trace Depth
  * E-UTRAN cells list
  * List of interfaces for eNB
  * IP address of Trace Collection Entity
When eNodeB receives the Trace Session Activation message from the EM for a
given or a list of E-UTRAN cell(s) the eNodeB shall start a Trace Session for
the given or list of E-UTRAN cell(s).
#### 4.1.1.6a E-UTRAN activation mechanisms for area based MDT data
collections without IMSI/IMEI(SV) selection
For area based MDT data collection with no IMSI/IMEI(SV) criteria, the UE
selection can be done in the radio network at eNB based on the input
information received from EM and the user consent information stored in the
eNB. This mechanism works for the following OAM input parameters:
  * Area information only
The following figure summarizes the flow how the MDT configuration is done
utilising the cell traffic trace functionality for this scenario:
Figure 4.1.1.6a.1: Example for area based logged MDT activation in E-UTRAN
> 0\. Whenever the eNB receives the Management based MDT allowed IE in Initial
> Context Setup Request or in Handover Request message, it shall save it for
> possible later usage.
  1. The EM sends a Trace Session activation request to the eNB. This request includes the parameters for configuring UE measurements:
\- Job type
\- Area scope where the UE measurements should be collected: list of E-UTRAN
cells. Tracking Area should be converted to E-UTRAN cell.
\- List of measurements
\- Reporting Trigger
\- Report Interval
\- Report Amount
\- Event Threshold
\- Logging Interval
\- Logging Duration
\- Trace Reference
\- IP address of TCE
\- Anonymization of MDT data.
\- Measurement period LTE (if either of the measurements M4, M5 is requested)
\- Collection period for RRM measurements LTE (present only if any of M2 or M3
measurements are requested).
\- Positioning method
\- MDT PLMN List
Note that at the same time not all the parameters can be present. The criteria
for which parameters are present are described in clause 5 of the present
document.
  1. When eNB receives the Trace Session activation request from its EM, it shall start a Trace Session and should save the parameters associated to the Trace Session.
  2. eNB shall select the suitable UEs for MDT data collection. The selection is based on the area received from the EM and the area where UE islocated, user consent information received from the core network as part of the Management Based MDT Allowed IE (As described in section in 4.6. of this document).If the user is not in the specified area or if the Management Based MDT Allowed IE is not present in the UE context the UE shall not be selected by the eNB for MDT data collection. During UE selection, the eNB shall take into account also the UE capability (MDT capability) when it selects UE for logged MDT configuration. If the UE does not support logged MDT the UE shall not be selected.\ If M4 or M5 measurements are requested in the MDT configuration, eNB should start the measurement according to the received configuration. Details of the measurements are defined in TS 36.314 [35].
  3. eNB shall activate the MDT functionality to the selected UEs. When eNB selects a UE it shall take into account the availability of Management Based MDT Allowed IE in the user context and the area scope parameter received in MDT configuration (Trace Session activation). Detailed description about user consent handling and how it is provided to the eNB is described in section 4.6.2. If there is no Management Based MDT Allowed IE in the user context or the user is outside the area scope defined in the MDT configuration, the UE shall not be selected for MDT data collection. The eNB shall assign Trace Recording Session Reference corresponding to the selected UE. The eNB shall send at least the following configuration information to the UE in case of Logged MDT:
\- Trace Reference
\- Trace Recording Session Reference
\- TCE Id (The value signalled as IP address of TCE from the EM is mapped to a
TCE Id, using a configured mapping in the eNB)
\- Logging Interval
\- Logging Duration
\- Absolute time reference
\- Area scope where the UE measurements should be collected: list of E-UTRAN
cells/TA.
\- MDT PLMN List
NOTE: For UEs currently being in idle mode and camping in the cell the logged
MDT configuration cannot be sent. These UEs may be configured when they
initiate some activity (e.g., Service Request or Tracking Area Update) at next
time.
> In case of Immediate MDT the following parameters shall be sent to the UE:
\- List of measurements
\- Reporting trigger
\- Report Interval
\- Report Amount
\- Event Threshold
Note that at the same time not all the parameters can be present. Conditions
of the parameters are described in clause 5 of the present document.
If positioning method indicates GNSS positioning, eNB should activate the GNSS
module of the UE via RRC as specified in TS 36.331 [32]. If positioning method
indicates E-Cell ID positioning, the eNB should collect the UE reported UE Rx-
Tx time difference measurements as specified in TS 36.331[32] measurement
procedures, as well as, any available eNB measured eNB Rx-Tx time difference,
Angle of Arrival measurements as specified in TS 36.214[38] and capture it in
MDT trace record.
If Reporting Trigger parameter indicates that all configured RRM measurement
trigger should be reported in MDT, then eNB should ask the UE to provide the
"best effort" location information together with the measurement reporting by
setting the _includeLocationInfo_ IE in all RRC measurement reporting
configurations.
  1. When UE receives the MDT activation it shall start the MDT functionality based on the received configuration parameters.
  2. The eNodeB shall not retrieve MDT report from the UE if UE's rPLMN does not match the PLMN where TCE used to collect MDT data resides (e.g. eNodeB's primary PLMN). When the eNodeB receives the MDT report from UE, the eNodeB shall get the Trace Recording Session Reference, Trace Reference and TCE Id from the report, and compare the Trace PLMN (PLMN portion of Trace Reference) with the PLMN where TCE used to collect MDT data resides (e.g. its primary PLMN) and discard MDT report in case of a mismatch. Otherwise if the MDT anonymization requires the IMEI-TAC in the MDT record eNodeB shall send the Trace Recording Session Reference, Trace Reference, serving cell CGI, and TCE IP address in the CELL TRAFFIC TRACE message to the MME via the S1 connection. When MME receives this S1 signalling message containing the Trace Recording Session Reference , Trace Reference, serving cell CGI, and the Privacy Indicator (that shall be set to _Logged MDT_ or _Immediate MDT_ depending on the configured job type) if so indicated in the privacy indicator, the MME shall look up the subscriber identities (IMEI (SV)) of the given call from its database, and send the IMEI-TAC together with the Trace Recording Session Reference and Trace Reference and for immediate MDT also the serving cell CGI to the TCE, as described in section 4.7 of the present document. For logged MDT, MME will send the IMEI-TAC together with the Trace Recording Session Reference, Trace Reference to the TCE.
> NOTE: For area based Immediate MDT, TRSR may be duplicated among different
> eNodeBs when multiple cells are selected as the area scope for the same MDT
> job. In this case, the combination of TRSR and the UE's serving cell CGI in
> the MDT report can uniquely identify one trace recording session.
  1. For Immediate MDT when the eNB receives the MDT report from the UE in the RRC message the eNB shall capture it and put the UE's serving cell CGI together with the MDT report from the UE to the trace record. A UE configured to perform Logged MDT measurements in IDLE indicates the availability of MDT measurements, by means of a one bit indicator, in _RRCConnectionSetupComplete_ message during connection establishment as specified in [2]. The eNB can decide to retrieve the logged measurements based on this indication by sending the UEInformationRequest message to the UE. The UE can answer with the collected MDT logs in UEInformationResponse message.
  2. The eNB shall forward the Trace Records to the Trace Collection Entity (TCE). In case of logged MDT, the TCE Id is indicated in the MDT report is translated to the actual IP address of the TCE by the eNB before it forwards the measurement records. (The address translation is using configured mapping in the eNB.) In case of immediate MDT, the IP address of the TCE is indicated for the eNB in the trace configuration.
The Immediate MDT measurement configuration is deleted in the UE together with
the RRC context when entering idle mode.
**The Logged MDT trace session is preserved in the UE until the duration time
of the trace session expires, including also multiple idle periods interrupted
by idle-connected-idle state transitions.**
**The Logged MDT trace session context of the UE is stored in the network as
long as the trace session is active, including also the periods when the UE is
in connected state.**
EM shall validate that the MCC and MNC specified in the Trace reference is the
same as the PLMN supported by all the cells specified in the area scope. If
the eNodeB receives a request with a PLMN in the TraceReference that does not
match any PLMN in its list, it shall ignore the request.
#### 4.1.1.7 EPC Domain activation mechanisms
When a MME, SGW or PGW receives Trace Session activation from the EM, it shall
start a Trace Session. The following trace control and configuration
parameters of the Trace Session are received in the Trace Session activation
from the EM:
  * IMSI or IMEISV
  * Trace Reference
  * Triggering events for this network element
  * Trace Depth
  * List of Interfaces for this network element
  * IP address of Trace Collection Entity
The MME, SGW or PGW shall not forward these trace control and configuration
parameters to other nodes. The received trace control and configuration
parameters shall be saved and used to determine when and how to start a Trace
Recording Session. (Starting a Trace Recording Session is described in
subclause 4.2.2.6).
### 4.1.2 Signalling activation
#### 4.1.2.1 General
In Signalling activation, the Trace Activation shall be carried out from the
Core Network EM only [EM (PS), EM (CS), EM (HSS) and EM(EPC) are generally
considered to be in the Core Network. A Core Network EM can be any of these or
their combinations].
In case of home subscriber trace (i.e. in the HPLMN) the Trace Session
activation shall go to the HSS / MSC Server / SGSN / MME. Instances where the
home subscriber is roaming in a VPLMN, the HSS may initiate a trace in that
VPLMN. The VPLMN may reject such requests.
In case of foreign subscriber trace (i.e. the HPLMN operator wishes to trace
foreign subscribers roaming in his PLMN) the Trace Session activation shall go
the MSC Server/VLR, SGSN / MME. Depending on the Trace Control and
Configuration parameters received, the Core Network shall propagate the
activation to selected NE\'s in the entire network \-- RAN and Core Network.
If the NE failed to activate the Trace Session, a Trace failure notification
shall be sent to the TCE, and the Trace failure notification has the the same
parameters as the notification notifyTraceRecordingSessionFailure defined in
3GPP TS 32.442 [24], the Trace failure notification file XML schema is defined
in Annex A.
#### 4.1.2.2 Intra PLMN signalling activation
The following figure represents the signalling based trace functionality
within a PLMN. The figure represents a typical PLMN network. A dotted arrow
with \"Trace Parameter Configuration\" represents the availability of the
trace functionality at the EM for that domain. You can however do it from the
EM (CS Domain). Similarly \"Trace Parameter Propagation\" is allowed only for
the interfaces indicated in the figure. E.g. there is no parameter propagation
over Iu-B.
The trace propagation across multiple PLMNs of the same operator (e.g.
deployment scenario where UMTS part of the network has one PLMN and LTE part
of the network as another PLMN) follows the rules of the Intra-PLMN signalling
activation.
NOTE: For tracing on the basis of IMEI(SV), the signalling based activation
can be only initiated from the MSC/VLR or SGSN.
Figure 4.1.2.2.1: Overview of Intra-PLMN Signalling Activation
#### 4.1.2.3 Inter PLMN Signalling Activation
The following figure represents the signalling based trace functionality
between PLMNs. This is particularly useful when a roaming subscriber needs to
be traced in a network. The figure represents a typical PLMN network and its
connections with another PLMN's HSS. A dotted arrow with \"Trace Parameter
Configuration\" represents the availability of the trace functionality at the
EM for that domain. E.g. you cannot invoke a Signalling Trace at the EM
(UTRAN) because there is no such arrow shown in the figure. You can however do
it from the EM (CS Domain). Similarly \"Trace Parameter Propagation\" is
allowed only for the interfaces indicated in the figure. E.g. there is no
parameter propagation over Iu-B.
NOTE: There is no intention to allow tracing of a home subscriber roaming in a
foreign network i.e. the trace function is limited to PLMNs of a single
operator.
Figure 4.1.2.3.1: Overview of Inter-PLMN Signalling Activation
#### 4.1.2.4 UTRAN activation mechanisms
See subclause 4.2.3.1.
#### 4.1.2.5 PS Domain activation mechanisms
The following figure shows the Trace Session activation in the PS domain. The
figure is an example of tracing PDP context.
Figure 4.1.2.5.1: Trace session activation in PS domain for PDP Context
When a UE registers with the network by sending an ATTACH_REQUEST message to
the SGSN, it updates the location information in the HSS by sending the
UPDATE_GPRS_LOCATION message to the HSS. The HSS checks if the UE is being
traced. If it is being traced, the HSS shall propagate the trace control and
configuration parameters to the SGSN by sending a MAP-ACTIVATE_TRACE_MODE -
see 3GPP TS 29.002 [11] message to the SGSN. When an inter-SGSN routing area
update occurs, HSS shall send the MAP-ACTIVATE_TRACE_MODE message to the new
SGSN.
When SGSN receives the MAP-ACTIVATE_TRACE_MODE message it shall store the
trace control and configuration parameters and shall start a Trace Session.
When any of the triggering events defined in the trace control and
configuration parameters occur, (e.g. PS session is started (i.e. a ACTIVATE
PDP CONTEXT REQUEST message is received from the UE)) the SGSN shall propagate
the trace control and configuration parameters to the GGSN (by sending a GTP-
CREATE_PDP_CONTEXT_REQUEST message) and to the radio network (by sending a
RANAP-CN_INVOKE_TRACE message), if it is defined in the trace control and
configuration parameters (NE types to trace). The Trace Session activation to
UTRAN is described in clauses 4.1.2.4.
When HSS sends the MAP-ACTIVATE_TRACE_MODE message to SGSN it shall include
the following parameters to the message (The values related to the EPS domain
shall be used for the Trace Session activation through the S3 interface in
case of an Inter-RAT handover event.):
  * IMSI (M).
  * Trace reference (M).
  * Triggering events for SGSN (M) , GGSN (M) , MME (M), Serving GW(M) and PDN GW(M).
  * Trace Depth (M).
  * List of NE types to trace (M).
  * List of interfaces for SGSN (O), GGSN (O) and/or RNC (O) , MME (O), Serving GW (O), PDN GW(O), eNB(O).
  * IP address of Trace Collection Entity (O).
When the SGSN sends the GTP-CREATE_PDP_CONTEXT_REQUEST message to GGSN it
shall include the following parameters to the message:
  * IMSI or IMEI (SV) (M).
  * Trace reference (M).
  * Trace Recording Session Reference (M).
  * Triggering events for GGSN (M).
  * Trace Depth (M).
  * List of interfaces for GGSN (O).
  * IP address of Trace Collection Entity (O).
Figure 4.1.2.5.2 is an example of tracing for MBMS Context.
Figure 4.1.2.5.2: Trace session activation in PS domain for MBMSContext
When HSS receives a Trace Session activation from its EMS, it shall store the
received trace control and configuration parameters. At this point a Trace
Session shall be started in the HSS.
When a UE registers with the network by sending an ATTACH_REQUEST message to
the SGSN, it updates the location information in the HSS by sending the
UPDATE_GPRS_LOCATION message to the HSS. The HSS checks if the UE is being
traced. If it is being traced, the HSS shall propagate the trace control and
configuration parameters to the SGSN by sending a MAP-ACTIVATE_TRACE_MODE
message to the SGSN. When an inter-SGSN routing area update occurs, HSS shall
send the MAP-ACTIVATE_TRACE_MODE message to the new SGSN.
When SGSN receives the MAP-ACTIVATE_TRACE_MODE message it shall store the
trace control and configuration parameters and shall start a Trace Session.
In case of an inter-SGSN handover the trace control and configuration
parameters (both PS domain specific and EPS domain specific parameters) shall
be propagated to the target SGSN.
In case of an inter-RAT handover the SGSN shall send the PS and EPS specific
Trace control and configuration parameters to the target MME via the S3
interface.
When any of the triggering events defined in the trace control and
configuration parameters occur, (i.e. an ACTIVATE MBMS CONTEXT REQUEST message
is sent to the UE)) the SGSN shall propagate the trace control and
configuration parameters to the GGSN (by sending a GTP-
CREATE_MBMS_CONTEXT_REQUEST message) and to the radio network (by sending a
RANAP-CN_INVOKE_TRACE message), if it is defined in the trace control and
configuration parameters (NE types to trace). The Trace Session activation to
UTRAN is described in clauses 4.1.2.4.
The GGSN shall propagate the trace control and configuration parameters to the
BM-SC (by sending a Diameter Gmb AAR message) if the BM-SC is defined in the
trace control and configuration parameters (NE types to trace).
When HSS sends the MAP-ACTIVATE_TRACE_MODE message to SGSN it shall include
the following parameters in the message:
  * IMSI (M).
  * Trace reference (M).
  * Triggering events for SGSN (M), GGSN (M) and BM-SC (M).
  * Trace Depth (M).
  * List of NE types to trace (M).
  * List of interfaces for SGSN (O), GGSN (O), BM-SC (O) and/or RNC (O).
  * IP address of Trace Collection Entity (O).
When the SGSN sends the GTP-CREATE_MBMS_CONTEXT_REQUEST message to GGSN it
shall include the following parameters in the message:
  * IMSI or IMEI (SV) (M).
  * Trace reference (M).
  * Trace Recording Session Reference (M).
  * Triggering events for GGSN (M) and BM-SC (M).
  * Trace Depth (M).
  * List of interfaces for GGSN (O) and BM-SC (O).
  * IP address of Trace Collection Entity (O).
When the GGSN sends the Diameter Gmb AAR message to the BM-SC it shall include
the following parameters in the message:
  * IMSI or IMEI (SV) (M).
  * Trace reference (M).
  * Trace Recording Session Reference (M).
  * Triggering events for BM-SC (M).
  * Trace Depth (M).
  * List of interfaces for BM-SC (O).
  * IP address of Trace Collection Entity (O).
#### 4.1.2.6 CS Domain activation mechanisms
Figure 4.1.2.6.1 shows the Trace Session activation in the CS domain. The
figure is an example of tracing Mobile Originating Call.
Figure 4.1.2.6.1: Trace Session Activation in CS domain
When HSS receives Trace Session activation from the EMS it should store the
trace control and configuration parameters associated to the Trace Session.
If the UE registers to the network, by sending a LOCATION UPDATING REQUEST
message to the MSC/VLR, the MSC Server/VLR updates the location information in
the HSS by sending the MAP-UPDATE_LOCATION message to the HSS. After receiving
the UPDATE_LOCATION message HSS shall propagate the trace control and
configuration parameters by sending a MAP-ACTIVATE_TRACE_MODE message to the
MSC Server/VLR.
When the MSC Server/VLR receives the MAP-ACTIVATE_TRACE_MODE message from the
HSS, it shall store the trace control and configuration parameters.
When any of the triggering event, defined in the trace control and
configuration parameters, occurs (e.g. in case of Mobile Originating Call is
started (i.e. the MSC Server receives the CM_SERVICE_REQUEST message with
service type set to originating call establishment)) the MSC Server should
propagate the trace control and configuration parameters to the MGW (by
sending an ADD command with a trace package - see 3GPP TS 29.232 [10]) and to
the radio network if it is defined in the trace control and configuration
parameters (NE types to trace). Trace Session activation for UTRAN is
described in clauses 4.1.2.4. In case of inter-MSC Server handover the MSC
Server-A should propagate the trace control and configuration parameters to
the MSC Server-B.
When HSS sends the MAP-ACTIVATE_TRACE_MODE message to MSC Server it shall
include the following parameters to the message:
  * IMSI (M).
  * Trace reference (M).
  * Triggering events for MSC Server (M) and MGW (M).
  * Trace Depth (M).
  * List of NE types to trace (M).
  * List of interfaces for MSC Server (O), MGW (O) and/or RNC (O).
  * IP address of Trace Collection Entity (O).
When the MSC Server sends the ADD command with trace package to MGW it shall
include the following parameters to the message:
  * IMSI or IMEI (SV) (M).
  * Trace reference (M).
  * Trace Recording Session Reference (M).
  * Triggering events for MGW (M).
  * Trace Depth (M).
  * List of interfaces for MGW (O).
  * IP address of Trace Collection Entity (O).
#### 4.1.2.7 Void
#### 4.1.2.8 Tracing roaming subscribers
If a HPLMN operator activates a Trace Session for a home subscriber, while it
(MS) is roaming in a VPLMN, it (HSS) may restrict the propagation of the Trace
Session activation message to a MSC Server/VLR or to a SGSN located in the
VPLMN.
Also, a MSC Server/VLR or a SGSN located in a VPLMN may accept any Trace
Session activation message(s) coming from an HSS located in another PLMN.
However, there shall be a capability to reject activations from another PLMN.
#### 4.1.2.9 void
##### 4.1.2.9.1 void
##### 4.1.2.9.2 Void
##### 4.1.2.9.3 Void
##### 4.1.2.9.4 Void
#### 4.1.2.10 EPC activation mechanism
##### 4.1.2.10.1 UE attached to EPC via E-UTRAN
Figure 4.1.2.10.1 summarizes the Trace Session activation procedure in EPC:
Figure 4.1.2.10.1: Trace Session activation procedure in EPC with GTP based S5
interface:
The Trace Session activation in MME can come for a home subscriber trace from
HSS via the S6a interface or for a foreign subscriber from the EM of MME.
When the UE makes an attach request to the MME, it updates the location
information in the HSS. The HSS checks if the UE is being traced. If it is
being traced, the HSS shall propagate the trace control and configuration data
to the MME by including the trace control and configuration parameters into
the S6a-Insert subscriber data message or the S6a-Update Location Answer
message. If the traced UE has already attached before receiving the Trace
Session Activation from the EM/NM, the HSS shall also propagate the trace
control and configuration data to the MME by either S6a-Insert subscriber data
message or the S6a-Update Location Answer message. When MME receives the trace
control and configuration data from the HSS it shall store the information and
shall start a Trace Session.
During inter-MME TAU, the MME shall propagate the trace control and
configuration parameters to the target MME within an S10- Context Response as
part of inter-MME TAU procedures. During attach procedures where the context
information is requested from the target MME, the MME shall propagate the
trace control and configuration parameters within an S10-Identification
Response message. During inter-MME handover, the MME shall propagate the trace
control and configuration parameters to the target MME within an S10- Forward
Relocation Request message as part of inter-MME handover procedures. During
inter-RAT handover procedure, the MME shall propagate the trace control and
configuration parameters to the target SGSN via the S3 interface as part of
the inter-RAT handover procedure.
If the List of NE Types parameter specifies tracing in the SGW and/or Tracing
in the PGW, MME shall propagate the trace control and configuration parameters
via the S11 interface to the SGW per one of the following messages:
1) if a default bearer connection has not been established, via the S11:
Create Session Request message;
2) otherwise via the S11-Trace Session Activation message.
The SGW upon receiving the trace control and configuration parameters shall
start a trace session.
If the List of NE Types parameter specifies Tracing in the PGW, SGW shall
propagate the trace control and configuration parameters via the S5 interface
to the PGW per one of the following messages:
1) if a default bearer connection has not been established, via the S5: Create
Session Request message;
```{=html}
``` 3) otherwise via the S5-Trace Session Activation message.
The PGW upon receiving the trace control and configuration parameters shall
start a trace session.
When a triggering events, defined in the trace control and configuration data
occur (i.e. a session is started) a Trace Recording Session should be started
and the trace control and configuration data should be propagated to the radio
network to the eNB if the List of NE Types parameter specifies eNB tracing.
However if the triggering events parameter at MME indicates that all events
should be traced, Trace Recording Session shall be started only when the user
specific S1 association is setup to the eNB and the Trace Recording Session is
kept as long as the user specific S1 association is released or the Trace
Session is deactivated. See section 4.2.3.6.
When HSS activates the trace to the MME the following trace control and
configuration parameters shall be included in the message (the values related
to the PS domain shall be used for Trace Session Activation during inter-RAT
handover procedure):
  * IMSI or IMEISV
  * Trace Reference
  * Triggering events for MME, Serving GW, PDN GW, SGSN, GGSN
  * Trace Depth
  * List of NE types to trace
  * List of Interfaces for MME, Serving GW, PDN GW, eNB, SGSN, GGSN, RNC
  * IP address of Trace Collection Entity
When MME activates the trace to the SGW the following trace control and
configuration parameters shall be included in the message:
  * IMSI or IMEISV
  * Trace Reference
  * Triggering events for Serving GW, PDN GW
  * Trace Depth
  * List of NE types to trace
  * List of Interfaces for Serving GW, PDN GW
  * IP address of Trace Collection Entity
When SGW activates the trace to the PGW the following trace control and
configuration parameters shall be included in the message:
  * IMSI or IMEISV
  * Trace Reference
  * Triggering events for PDN GW
  * Trace Depth
  * List of Interfaces for PDN GW
  * IP address of Trace Collection Entity
When MME sends the trace control and configuration parameters to the eNB the
following information shall be included in the message:
  * Trace Reference
  * Trace Recording Session Reference
  * Trace Depth
  * IP Address of Trace Collection Entity
and the following information may be included in the message:
  * List of Interfaces for eNB
Figure 4.1.2.10.1.A illustrates the Trace Session activation in case of PMIP
based S5 interface. The figure contains only the difference compare to the GTP
based S5 interface.
Figure 4.1.2.10.1.A: Trace Session Activation from SWG to PGW in case of PMIP
based S5 interface
When the SGW receives the Trace Session activation message and the List of NE
Type to trace parameter specifies Tracing in the PDN GW , SGW shall send Trace
Session Activation to PDN GW via the PCRF. The Trace Session activation can be
done as part of the IP CAN session establishment or as a standalone procedure
[29].
The Trace Session Activation shall include the following information:
  * IMSI or IMEISV
  * Trace reference
  * Trace Recording Session Reference
  * Trace Depth
  * Triggering events for PDN GW
  * List of Interfaces for PDN GW
  * IP address of Trace Collection Entity
When the PCRF receives the Trace Session Activation it shall forward the same
trace control and configuration parameters to the PDN GW [29].
##### 4.1.2.10.2 UE attached to EPC via _non-3GPP_ accesses with DSMIPv6 on
S2c or PMIP on S2a/S2b
Figure 4.1.2.10.2 illustrates the Trace Session activation when the UE is
attached from a non-3GPP access network with DSMIPv6 on S2c or PMIP on S2a or
S2b interface.
{width="5.519444444444445in" height="4.508333333333334in"}
Figure 4.1.2.10.2: Trace Session activation procedure to PGW in case of UE
attaches from non-3GPP access network via DSMIPv6 on S2c or PMIP on S2a/S2b
When the UE attaches to the EPC network via a non-3GPP access network the
Trace Session activation to the PGW can be done via HSS and AAA server.
Therefore when the UE attach is signalled to the HSS via non-3GPP access
network, the HSS shall send the Trace control and configuration parameters to
the AAA server as part of the user profile download [25]. The following
information shall be included in the downloaded user data:
  * IMSI, or IMEI(SV)
  * Trace Reference
  * Triggering event for PGW
  * Trace Depth
  * List of interface for PGW
  * IP address of Trace Collection Entity
When the AAA server receives the user profile, which contains also the trace
control and configuration parameters, it shall store the received trace
control and configuration parameters. The AAA server shall forward the
received trace control and configuration parameters in the authorization when
it receives the authorization request from the PGW during the PDN
connectivity.
The event, which triggers the authorization in the PDN GW depend on the used
IP mobility protocol:
In case of DSMIP (option A), it is a binding update received from the UE,
In case of PMIP (Option B), it is a proxy binding update request received from
the Trusted Non-3GPP GW or ePDG playing the role of the Mobile Access Gateway
(MAG)
If the UE is already registered to the HSS by a AAA server via the SWx
interface, Trace Session activation shall also be possible from the HSS to the
PDN GW via the AAA server. In that case the HSS sends the Trace Session
activation message with a push profile request.
The AAA server shall examine the received user profile and if Trace Session
activation is needed in the PDN GW, it shall initiate a re-authorization
procedure towards the PDN GW. The Trace Session is activated to te PDN GW
using this re-authorization procedure. When PDN GW receives the Trace Session
activation message, it shall save the received trace control and configuration
parameters.
##### 4.1.2.10.3 UE attached to EPC via non-3GPP accesses with GTP on S2b
interface
Figure 4.1.2.10.3 illustrates the Trace Session activation when the UE is
attached from a non-3GPP access with GTP on the S2b interface.
Figure 4.1.2.10.3: Trace Session activation procedure to PGW when the UE is
attaches to EPC from a non-3GPP access with GTP based S2b
When the UE attaches to the EPC network via a non-3GPP access network the
Trace Session activation to the PGW can be done via HSS, AAA server and ePDG.
Therefore when the UE attach is signalled to the HSS via non-3GPP access
network, the HSS shall send the Trace control and configuration parameters to
the AAA server as part of the user profile download (see [22] , [25] and
[34]).\ The following information shall be included in the downloaded user
data:
  * IMSI, or IMEI(SV)
  * Trace Reference
  * Triggering event for PGW
  * Trace Depth
  * List of interface for PGW
  * IP address of Trace Collection Entity
The ePDG sends a GTPv2 Create Session Request which contains trace information
message to the PGW. The RAT type indicates the non-3GPP IP access technology
type.
Figure 4.1.2.10.4 illustrates the Trace Session activation when the UE is
already attached from a non-3GPP access with GTP based S2b, i.e. trace session
activation after a session has been created.
If the UE is already registered to the HSS by a AAA server via the SWx
interface, Trace Session activation shall also be possible from the ePDG to
the PDN GW. In that case the HSS sends the Trace activation message with a
push profile request.
Figure 4.1.2.10.4: Trace Session activation procedure to PGW when the UE is
already attached to EPC from a non-3GPP access with GTP based S2b
The AAA shall examine the received information and if Trace Session activation
is needed in the PDN GW, it shall initiate a reauthorization request towards
the ePDG. ePDG sends a GTPv2 Trace Session Activation message to the PGW when
determining from the updated profile that a trace activation is needed. When
PDN GW receives the Trace Session activation message, it shall save the
received trace control and configuration parameters.
##### 4.1.2.10.4 Inter-RAT handover from E-UTRAN to UTRAN
The following figure illustrates an example scenario when the UE attaches to
the EPC domain, then makes an inter-RAT handover to the UMTS and makes another
handover back from UMTS to E-UTRAN.
Figure 4.1.2.10.4.1 Example scenario for Trace Session activation in case of
inter-RAT handover
In order to support the inter-RAT trace between EPS and PS domain when the HSS
sends the Trace Session Activation message to the SGSN/MME respectively it
shall send the trace control and configuration parameters that are applicable
for both PS and EPC domains. These parameters shall be transferred in the
Trace Session Activation message in the S6a/S6d interface respectively. When
MME/SGSN receives the Trace Session Activation message from the HSS or from
MME/SGSN the trace control and configuration parameters shall be stored and a
Trace Session shall be started.
When the MME sends the Forward Relocation Request messager to the S4-SGSN the
MME shall sends the following trace control and configuration parameters for
Trace Session activation to the SGSN:
\- IMSI or IMEI(SV)
\- Trace Reference
\- Trace Recording Session Reference
\- Trace Depth
\- Triggering events for SGSN, GGSN, RNC, MME, Serving GW, PDN GW and eNB
\- List of Interfaces for SGSN, GGSN, RNC, MME, Serving GW, PDN GW and eNB
\- IP address of Trace Collection Entity
The Trace Control and Configuration parameters shall be propagated during an
inter-RAT handover procedure from the source node to the target node. The
propagated Trace Control and Configuration parameters shall include values
that are applicable for both EPS and PS domain during the inter-RAT handover
procedure.
Similarly, in case of Gn SGSN those parameters shall be transferred through
S6a/Gn interface from the HSS to the MME/Gn SGSN. The Trace Control and
Configuration parameter of both domain shall be stored in the Trace Session in
MME/Gn SGSN respectively.
#### 4.1.2.11 E-UTRAN activation mechanisms
The Trace Session should be activated in in an eNB when the eNB receives the
TRACE START, INITIAL CONTEXT SETUP REQUEST or HANDOVER REQUEST message with
the IE _Trace Activation_ from the MME and if some activities have been
started on the interfaces that have been requested to be traced.
If the subscriber or equipment which is traced makes a handover to a target
eNB using the X2 interface, the source eNB should propagate the trace control
and configuration parameters further to the target eNB by using the HANDOVER
REQUEST message. When the target eNB receives the HANDOVER REQUEST message it
should immediately start a Trace Session according to the trace control and
configuration parameters received in the HANDOVER REQUEST message.
If the subscriber or equipment which is traced makes a handover to a target
eNB using the S1 interface, it is the MME\'s responsibility to propagate the
trace control and configuration parameters to the target eNB.
##### Interaction with Relocation {#interaction-with-relocation .H6}
If the tracing shall continue also after the relocation has been performed,
the CN Invoke Trace procedure shall be re-initiated from the CN towards the
future eNB after the Relocation Resource Allocation procedure has been
executed successfully.
The TRACE START, INITIAL CONTEXT SETUP REQUEST or HANDOVER REQUEST message
that is received from the MME contains the following information:
  * Trace Reference
  * including Trace Recording Session Reference
  * Trace Depth
  * List of interfaces for eNB
  * IP address of Trace Collection Entity
If the Trace Reference is the same as an existing Trace Session for the same
subscriber or equipment, the eNB shall not activate a new Trace Session and
the existing Trace Session will not be impacted. See clause 4.2.3.6 for the
conditions on whether or not the Trace Recording Session should be started.
If the Trace Reference is the same as an existing Trace Session for different
subscriber(s) or equipment(s), the eNB shall not activate a new Trace Session,
and the eNB shall not start a new Trace Recording Session.
#### 4.1.2.12 EPC and E-UTRAN Activation mechanism for MDT
##### 4.1.2.12.1 General
UE measurements activation extends the EPC trace activation procedure, as
described in 4.1.2.10. When a Trace Session is activated, configuration
parameters of MDT are added into the message.
For IMSI/IMEI(SV)/IMEI-TAC based UE selection, or IMSI/IMEI(SV)/IMEI-TAC
combined with geographical area based UE selection, UE performance
measurements activation request is propagated to UE finally.
This mechanism works for the following input parameters:
  * IMSI only or
  * IMSI and area information or
  * IMEI(SV) only or
  * IMEI(SV) and area information or
  * IMEI-TAC only or
  * IMEI-TAC and area information
After the IMSI, IMEISV or IMEI-TAC type user attached to the network, the MME
shall forward the MDT configurations to the corresponding eNB which serves the
IMSI, IMEISV or IMEI-TAC type user. If the area criterion is specified and is
not satisfied, the MME shall keep the MDT configuration first and then forward
it to the serving eNB only when the area criterion is satisfied.
**MDT criteria checking on eNB:**
  * For immediate MDT, after eNB got the MDT configuration, the eNB can detect the area information and decide whether the selected IMSI/IMEISV can fit into the criteria for initiating MDT data collection. If the area information criterion is not met, the eNB keeps the MDT configuration and propagates it during handover as specified in section 4. 4.
  * For logged MDT, the eNB will forward the MDT configuration criteria to the selected IMSI/IMEISV. The area criteria checking will be done at UE side after UE received the MDT configuration criteria.
**MDT criteria checking on UE:**
  * For immediate MDT, there is no need to do MDT criteria checking on UE.
  * For logged MDT, The area criteria checking will be done at UE side after UE received the MDT configuration criteria.
**_In case of logged MDT, after UE receives from eNodeB the configuration
parameters via the message RRC Connection Reconfiguration, it detects whether
it stays within the specified area. If yes the UE will execute measurement
job. Otherwise UE will do nothing but waiting._**
**In case of Immediate MDT trace (e.g., IMSI/IMEI based selection), the
Immediate MDT trace session context of the UE shall be preserved in the
network when the UE enters idle mode.**
**The Logged MDT trace session is preserved in the UE until the duration time
of the trace session expires, including also multiple idle periods interrupted
by idle-connected-idle state transitions.**
**The Logged MDT trace session context of the UE is stored in the network as
long as the trace session is active, including also the periods when the UE is
in connected state.**
Two scenarios shall be considered according to UE status when EMS activates
MDT job: before UE attachment, after UE attachment, different procedures are
described in 4.1.2.12.2, 4.1.2.12.3.
##### 4.1.2.12.2 Activation of MDT task before UE attaches to the network
As shown in figure 4.1.2.12.1, by adding configurations of MDT EMS activate
the Trace Session for MDT job.
Figure 4.1.2.12.1: MDT activation procedure in EPC
> When HSS activates the trace, for MDT job, to the MME the following
> configuration parameters shall be included in the message:
\- jobType
\- IMSI or IMEISV or IMEI-TAC
\- Area scope (e.g. TA, Cell)
\- Trace Reference
\- List of measurements
\- Reporting Trigger
\- Report Interval
\- Report Amount
\- Event Threshold
\- Logging Interval
\- Logging duration
\- Measurement period LTE (if either of the measurements M4, M5 is requested)
\- Collection period for RRM measurements LTE (present only if any of M2 or M3
measurements are requested).
\- Positioning method
\- MDT PLMN List
Note that at the same time not all the parameters can be present. The
conditions are described in clause 5.10 of the present document.
\- IP address of Trace Collection Entity
> The Specified geographical area field is available when IMSI/IMEI(SV)/IMEI-
> TAC combined with geographical area are needed for UE selection.
>
> When MME activate MDT activation to eNodeB, the MDT configuration parameters
> can be included in the message in the Initial Context Setup:
\- Area scope (TA, Cell)
\- Trace Reference
\- Trace Recording Session Reference
\- List of measurements
\- Reporting Trigger
\- Report Amount
\- Report Interval
\- Event Threshold
\- Logging Interval
\- Logging Duration
\- IP address of Trace Collection Entity
\- Collection period for RRM measurements LTE (present only if any of M2 or M3
measurements are requested).
\- Measurement period LTE (if either of the measurements M4, M5 is requested)
\- Positioning method
\- MDT PLMN List
Note that at the same time not all the parameters can be present. The
conditions are described in clause 5.10 of the present document.
The MME receives and stores MDT user consent indication from HSS as part of
subscriber information when user context is established in MME at UE
attachment. The MME shall consider the MDT user consent information when
activating an MDT trace session for the UE. Details on the user consent
handling are described in section 4.6.
If positioning method indicates GNSS positioning, eNB should activate the GNSS
module of the UE via RRC as specified in TS 36.331 [32]. If positioning method
indicates E-Cell ID positioning, the eNB should collect the UE reported UE Rx-
Tx time difference measurements as specified in TS 36.331[32] measurement
procedures, as well as, any available eNB measured eNB Rx-Tx time difference,
Angle of Arrival measurements as specified in TS 36.214 [38]and capture it in
MDT trace record.
If Reporting Trigger parameter indicates that all configured RRM measurement
trigger should be reported in MDT, then eNodeB should ask the UE to provide
the "best effort" location information together with the measurement reporting
by setting the _includeLocationInfo_ IE in all RRC measurement reporting
configurations.
##### 4.1.2.12.3 Activation of MDT task after UE attachment
Figure 4.1.2.12.2: MDT activation in EPC after UE attachment
The messages propagated to HSS, MME and eNodeB are the same as described in
clause 4.1.2.12.2.
When MME can send Trace Start to eNodeB, the following configuration
parameters shall be included in the message:
\- Area scope (TA, Cell)
\- Trace Reference
\- Trace Recording Session Reference
\- List of measurements
\- Reporting Trigger
\- Report Amount
\- Report Interval
\- Event Threshold
\- Logging Interval
\- Logging Duration
\- IP address of Trace Collection Entity
\- Measurement period LTE (if either of the measurements M4, M5 is requested)
\- Positioning method
\- Collection period for RRM measurements LTE (present only if any of M2 or M3
measurements are requested).
\- MDT PLMN List
Note that at the same time not all the parameters can be present. The
conditions are described in clause 5.10 of the present document.
The MME shall consider the MDT user consent information when activating an MDT
trace session for the UE. Detailed procedures about user consent is described
in Section 4. 6.1.
In case of logged MDT and the UE is currently being in idle mode, the MME is
not required to initiate paging of the UE in order to send the configuration.
Then eNodeB initiates RRC Connection Reconfiguration Request in case of
immediate MDT or the IdleMDTConfiguration RRC message in case of logged MDT
toward the UE and sends the MDT measurement configuration parameters as
received from the MME.
Immediate/Logged signalling based MDT criteria may consist of a cell list. MME
shall validate whether the serving cell is controlled by the same eNodeB as
any other cell in the cell list. If yes, the MDT activation shall be sent to
the serving eNodeB.
If positioning method indicates GNSS positioning, eNB should activate the GNSS
module of the UE via RRC as specified in TS 36.331 [32]. If positioning method
indicates E-Cell ID positioning, the eNB should collect the UE reported UE Rx-
Tx time difference measurements as specified in TS 36.331[32] measurement
procedures, as well as, any available eNB measured eNB Rx-Tx time difference,
Angle of Arrival measurements as specified in TS 36.214 [38] and capture it in
MDT trace record.
##### 4.1.2.12.4 Handling of various scenarios during MDT activation
Handling of various scenarios for Signalling based Logged/Immediate MDT are
addressed below:
1) EM initiating MDT activation shall validate that PLMNs specified in the MDT
PLMN List are supported by all the cells specified in the area scope. If the
eNodeB receives a request where none of the PLMNs in the MDT PLMN List match
any PLMN in its list, it shall ignore the request
2) Void.
3) MME shall be informed with a TRACE FAILURE INDICATION message if the eNodeB
could not configure the UE because it was in the middle of a handover (refer
to TS 36.413[36]). MME shall try to reactivate MDT in the target cell if the
target cell scope meets the MDT criteria.
4) Void.
5) When the UE re-enters PLMN (specified in the MDT PLMN List) then the MME
shall be responsible for restarting the Immediate MDT activation (if it is as
a result of an X2 handover then one option is MME could use the path switch
request as trigger). However this is best effort. There can be cases where MME
may not be able to restart the MDT when the UE re-enters the PLMN (specified
in the MDT PLMN List): for example: If the UE performs intra eNB handover
where path switch is not necessarily sent, the MME may not be able to restart
MDT
#### 4.1.2.13 PS domain activation mechanism for MDT
##### 4.1.2.13.1 General
MDT activation in PS domain extends the trace activation procedure, as
described in 4.1.2.5. When a Trace Session is activated, configuration
parameters of MDT are added into the Trace Session Activation message(s).
For IMSI/IMEI(SV) based UE selection, or IMSI/IMEI(SV) combined with
geographical area based UE selection, UE performance measurements activation
request is propagated to UE finally.
**_Detailed behaviour of the UE when it receives the configuration parameters
is described in 3GPP TS 37.320 [30]._**
**In case of Immediate MDT trace (e.g., IMSI/IMEI based selection), the
Immediate MDT trace session context of the UE shall be preserved in the
network when the UE enters idle mode.**
**The Logged MDT trace session is preserved in the UE until the duration time
of the trace session expires, including also multiple idle periods interrupted
by idle-connected-idle state transitions.**
**The Logged MDT trace session context of the UE is stored in the network as
long as the trace session is active, including also the periods when the UE is
in connected state.**
Two scenarios shall be considered according to UE status when the network
activates MDT job: before UE attachment, after UE attachment, different
procedures are described in 4.1.2.13.2 and 4.1.2.13.2a.
##### 4.1.2.13.2 Activation of MDT task before UE attaches to the network
The MDT activation procedure is shown in figure 4.1.2.13.2.1.
Figure 4.1.2.13.2.1: MDT activation procedure in PS domain during attach
procedure
The Trace Session activation is started from the EMS, when it activates the
Trace Session to the HSS. The HSS stores the trace control and configuration
parameters in its database.
When a UE registers with the network by sending an ATTACH_REQUEST message to
the SGSN, it updates the location information in the HSS by sending the
UPDATE_GPRS_LOCATION message to the HSS. The HSS checks if the UE is being
traced. If it is being traced, the HSS shall propagate the trace control and
configuration parameters to the SGSN by sending a MAP-ACTIVATE_TRACE_MODE -
see 3GPP TS 29.002 [11] message to the SGSN (This message can be embedded also
in the MAP INSERT SUBSCRIBER DATA message). The SGSN receives and stores MDT
user consent indication from HSS as part of subscriber information when user
context is established in SGSN at UE attachment (details are available in
clause 4. 6.1). When an inter-SGSN routing area update occurs, HSS shall send
the MAP-ACTIVATE_TRACE_MODE message to the new SGSN. The Trace Session
Activation from HSS to SGSN shall contain the following MDT specific
parameters in addition to the existing trace parameters:
\- Job type
\- Area Scope
\- List of measurements
\- Reporting Trigger
\- Report Interval
\- Report Amount
\- Event Threshold
\- Logging Interval
\- Logging Duration
\- IP address of Trace Collection Entity
\- Measurement quantity
\- Measurement period UMTS (if either of the measurements M6, M7 is requested)
\- Collection period for RRM measurements UMTS (present only if any of M3, M4
or M5 measurements are requested).
\- Positioning Method
\- MDT PLMN List
> Note that at the same time not all of the parameters can be present. The
> condition which parameters shall be present is described in clause 5 of the
> present document.
When SGSN receives the MAP-ACTIVATE_TRACE_MODE message it shall store the
trace control and configuration parameters and shall start a Trace Session and
shall send the CN_INVOKE_TRACE message to the RNC. The SGSN shall consider the
MDT user consent information when activating an MDT trace session for the UE.
The SGSN shall send the following parameters to the RNC beside the existing
trace parameters:
\- Job type
\- Area Scope
\- List of measurements
\- Reporting Trigger
\- Report Interval
\- Report Amount
\- Event Threshold
\- Logging Interval
\- Logging Duration
\- IP address of Trace Collection Entity
\- Measurement quantity
\- Measurement period UMTS (if either of the measurements M6, M7 is requested)
\- Collection period for RRM measurements UMTS (present only if any of M3, M4
or M5 measurements are requested).
\- Positioning method
\- MDT PLMN List
> Note that at the same time not all of the parameters can be present. The
> conditions which parameters shall be present is described in clause 5 of the
> present document.
##### 4.1.2.13.2a Activation of MDT task after UE attaches to the network
The MDT activation procedure after UE attaches to the network is shown in
figure 4.1.2.13.2a.1.
Figure 4.1.2.13.2a.1 MDT activation procedure in PS domain after UE attachs to
the network
When a UE registers with the network by sending an ATTACH_REQUEST message to
the SGSN, it updates the location information in the HSS by sending the
UPDATE_GPRS_LOCATION message to the HSS.
The Trace Session activation is started from the EMS, when it activates the
Trace Session to the HSS. When the HSS send trace activation to the SGSN, the
HSS shall propagate the trace control and configuration parameters to the SGSN
by sending a MAP-ACTIVATE_TRACE_MODE - see 3GPP TS 29.002 [11] message to the
SGSN (This message can be embedded also in the MAP INSERT SUBSCRIBER DATA
message). The SGSN receives and stores MDT user consent indication from HSS as
a part of subscriber information (details are available in Section 4. 6.1).
When an inter-SGSN routing area update occurs, HSS shall send the MAP-
ACTIVATE_TRACE_MODE message to the new SGSN. The Trace Session Activation from
HSS to SGSN shall contain the following MDT specific parameters in addition to
the existing trace parameters:
\- Job type
\- Area Scope
\- List of measurements
\- Reporting Trigger
\- Report Interval
\- Report Amount
\- Event Threshold
\- Logging Interval
\- Logging Duration
\- IP address of Trace Collection Entity
\- Measurement quantity
\- Measurement period UMTS (if either of the measurements M6, M7 is requested)
\- Collection period for RRM measurements UMTS (present only if any of M3, M4
or M5 measurements are requested).
\- Positioning method
\- MDT PLMN List
> Note that at the same time not all of the parameters can be present. The
> condition which parameters shall be present is described in clause 5 of the
> present document.
When SGSN receives the MAP-ACTIVATE_TRACE_MODE message it shall store the
trace control and configuration parameters and shall start a Trace Session and
shall send the CN_INVOKE_TRACE message to the RNC. The SGSN shall consider the
MDT user consent information when activating an MDT trace session for the UE.
The SGSN shall send the following parameters to the RNC beside the existing
trace parameters:
\- Job type
\- Area Scope
\- List of measurements
\- Reporting Trigger
\- Report Interval
\- Report Amount
\- Event Threshold
\- Logging Interval
\- Logging Duration
\- IP address of Trace Collection Entity
\- Measurement quantity
\- Measurement period UMTS (if either of the measurements M6, M7 is requested)
\- Collection period for RRM measurements UMTS (present only if any of M3, M4
or M5 measurements are requested).
\- Positioning method
\- MDT PLMN List
> Note that at the same time not all of the parameters can be present. The
> conditions which parameters shall be present is described in clause 5 of the
> present document.
##### 4.1.2.13.3 Handling of various scenarios during MDT activation
Handling of various scenarios for Signalling based Logged/Immediate MDT is
addressed below:
1) EM initiating MDT activation shall validate that the MCC and MNC specified
in the Trace reference is the same as the PLMN supported by all the RNCs
specified in the area scope. If the RNC receives a request with a PLMN in the
TraceReference that does not match any PLMN in its list, it shall ignore the
request.
2) SGSN shall trigger the MDT activation only when the MDT area criterion is
satisfied. But if the RNC receives a request that is outside the area scope
then the RNC shall store the MDT configuration and forward the request when a
handover occurs (intra PLMN).
3) When the UE re-enters the PLMN (in trace reference) which matches the area
scope defined in the MDT configuration then the SGSN shall be responsible for
restarting the Immediate MDT activation. However, this is best effort.
4) Void.
5) SGSN shall re-initiate CN Invoke Trace procedure to reactivate MDT job
after successful SRNS relocation if the RNC could not configure the UE since
it was in the middle of inter-RNC handover (refer to TS 25.413 [13]). SGSN
shall try to reactivate MDT in the target cell if the target cell scope meets
the MDT criteria.
6) Void.
7) Area based MDT criteria may consist of a cell list. SGSN shall validate
whether the UE is controlled by the same RNC as any other cell in the cell
list. If yes, the MDT activation shall be sent to the serving RNC. If the RNC
receives a Signalling Based MDT activation request when the UE is served by a
cell that is in the RNC but not in the MDT area scope then the RNC shall store
the MDT configuration and configure the UE when the UE moves to a cell in the
RNC (intra RNC handover) that satisfies the area scope in the request.
#### 4.1.2.14 CS domain activation mechanism for MDT
##### 4.1.2.14.0 Activation of MDT task before UE attaches to the network
In UMTS it is also possible to send the MDT job activation via the CS domain
instead of the PS domain. The activation mechanism is shown in figure
4.1.2.14.1.
Figure 4.1.2.14.1: MDT activation procedure in CS domain during attach
procedure
The Trace Session activation is started from the EMS, when it activates the
Trace Session to the HSS. The HSS stores the trace control and configuration
parameters in its database.
When a UE registers with the network by sending an ATTACH_REQUEST message to
the MSC Server, it updates the location information in the HSS by sending the
UPDATE_LOCATION message to the HSS. The HSS checks if the UE is being traced.
If it is being traced, the HSS shall propagate the trace control and
configuration parameters to the MSC Server by sending a MAP-
ACTIVATE_TRACE_MODE - see 3GPP TS 29.002 [11] message to the MSC Server (This
message can be embedded also in the MAP INSERT SUBSCRIBER DATA message). The
MSC Server receives and stores MDT user consent indication from HSS as part of
subscriber information at UE attachment (details are available in Section
4.2.8.1). When an inter-VLR Location Area update occurs, HSS shall send the
MAP-ACTIVATE_TRACE_MODE message to the new VLR / MSC Server. The Trace Session
Activation from HSS to MSC Server shall contain the following MDT specific
parameters in addition to the existing trace parameters:
\- Job type
\- Area Scope
\- List of measurements
\- Reporting Trigger
\- Report Interval
\- Report Amount
\- Event Threshold
\- Logging Interval
\- Logging Duration
\- IP address of Trace Collection Entity
\- Measurement quantity
\- Measurement period UMTS (if either of the measurements M6, M7 is requested)
\- Collection period for RRM measurements UMTS (present only if any of M3, M4
or M5 measurements are requested).
\- Positioning method
\- MDT PLMN List
> Note that at the same time not all of the parameters can be present. The
> condition under which parameters shall be present is described in clause 5
> of the present document.
When MSC Server receives the MAP-ACTIVATE_TRACE_MODE message it shall store
the trace control and configuration parameters and shall start a Trace Session
and shall send the CN_INVOKE_TRACE message to the RNC. The MSC Server shall
consider the MDT user consent information when activating an MDT trace session
for the UE. The MSC Server shall send the following parameters to the RNC
beside the existing trace parameters:
\- Job type
\- Area Scope
\- List of measurements
\- Reporting Trigger
\- Report Interval
\- Report Amount
\- Event Threshold
\- Logging Interval
\- Logging Duration
\- IP address of Trace Collection Entity
\- Measurement quantity
\- Measurement period UMTS (if either of the measurements M6, M7 is requested)
\- Collection period for RRM measurements UMTS (present only if any of M3, M4
or M5 measurements are requested).
\- Positioning method
\- MDT PLMN List
> Note that at the same time not all of the parameters can be present. The
> condition under which parameters shall be present is described in clause 5
> of the present document.
**In case of Immediate MDT trace (e.g., IMSI/IMEI based selection), the
Immediate MDT trace session context of the UE shall be preserved in the
network when the UE enters idle mode.**
**The Logged MDT trace session is preserved in the UE until the duration time
of the trace session expires, including also multiple idle periods interrupted
by idle-connected-idle state transitions.**
**The Logged MDT trace session context of the UE is stored in the network as
long as the trace session is active, including also the periods when the UE is
in connected state.**
##### 4.1.2.14.1 MDT Error Handling
Handling of various scenarios for Signalling based Logged/Immediate MDT is
addressed below:
  1. EM initiating MDT activation shall validate that the MCC and MNC specified in the Trace reference is the same as the PLMN supported by all the cells specified in the area scope. If the RNC receives a request with a PLMN in the TraceReference that does not match any PLMN in its list , it shall ignore the request
  2. MSC-S shall trigger the activation only when the MDT area criterion is satisfied. But if for some reason the RNC receives a request that is outside the area scope then the RNC shall store the MDT configuration and forward the request when a handover occurs (intra PLMN).
  3. When the UE re-enters the PLMN (in trace reference) which matches the area scope defined in the MDT configuration then the MSC shall be responsible for restarting the Immediate MDT activation. However this is best effort.
  4. Void.
  5. MSC-S shall re-initiate CN Invoke Trace procedure to reactivate MDT job after SRNS relocation (refer to TS 25.413 [13]) if the RNC could not configure the UE since it was in the middle of inter RNC handover. MSC-S shall try to reactivate MDT in the target cell if the target cell scope meets the MDT criteria.
  6. Void.
  7. Area based MDT criteria may consist of a cell list. MSC-S shall validate whether the UE is controlled by the same RNC as any other cell in the cell list. If yes, the MDT activation shall be sent to the serving RNC. If the RNC receives a Signalling Based MDT activation request when the UE is served by a cell that is in the RNC but not in the MDT area scope then the RNC shall store the MDT configuration and configure the UE when the UE moves to a cell in the RNC (intra RNC handover) that satisfies the area scope in the request
### 4.1.3 Management deactivation
#### 4.1.3.1 UTRAN deactivation mechanisms
When last Trace session is requested to be ended for an IMEI(SV) or a list of
IMEI(SV), the RNC shall send the requested IMEI(SV)/list of IMEI(SV)s in
\'Uplink Information Exchange Request\' to the interacting MSC Server(s) and
SGSN(s). The MSC Servers and SGSNs shall remove the requested IMEI(SV)s for
the RNC in question.
#### 4.1.3.2 PS Domain deactivation mechanisms
When a SGSN, GGSN or BM-SC receives a Trace Session Deactivation from its EM,
the Trace Session identified by the Trace Reference, shall be deactivated in
SGSN/GGSN/BM-SC.
If a Trace Recording Session is active at the time of receiving a Trace
Session deactivation from the EM, the SGSN/GGSN/BM-SC may choose to continue
the Trace Recording Session till it ends gracefully or may stop it
immediately. In all cases, the SGSN/GGSN/BM-SC shall deactivate the requested
Trace Session immediately at the end of the Trace Recording Session.
#### 4.1.3.3 CS Domain deactivation mechanisms
When a MSC Server receives a Trace Session Deactivation from its EM, the Trace
Session identified by the Trace Reference, shall be deactivated in MSC Server.
If a Trace Recording Session is active at the time of receiving a Trace
Session deactivation from the EM, the MSC Server may choose to continue the
Trace Recording Session till it ends gracefully or may stop it immediately. In
all cases, the MSC Server shall deactivate the requested Trace Session
immediately at the end of the Trace Recording Session.
#### 4.1.3.4 IP Multimedia Subsystem deactivation mechanisms
When a S-CSCF/P-CSCF receives a Trace Session deactivation from the EM, the
Trace Session identified by the Trace Reference, shall be deactivated.
If a Trace Recording Session is active at the time of receiving a Trace
Session deactivation from the EM, the S-CSCF/P-CSCF may choose to continue the
Trace Recording Session till it ends gracefully or may stop it immediately. In
all cases, the S-CSCF/P-CSCF shall deactivate the requested Trace Session
immediately at the end of the Trace Recording Session.
The following figure illustrates how the Trace Session is deactivated when a
Trace Recording Session is going on (e.g. a SIP INVITE method is being traced
in S-CSCF).
Figure 4.1.3.4.1: Trace session deactivation in IMS
#### 4.1.3.5 E-UTRAN deactivation mechanisms
In E-UTRAN the Cell Traffic trace functionality can be deactivated when the
eNodeB receives the Trace Session Deactivation message from the EM. At this
time the eNodeB shall deactivate the Trace Session for those E-UTRAN Cells
that have been indicated in the Trace Session Deactivation message received
from the EM.
#### 4.1.3.6 EPC Domain deactivation mechanisms
When a MME, SGW or PGW receives a Trace Session Deactivation from its EM, the
Trace Session identified by the Trace Reference, shall be deactivated in the
MME, SGW or PGW.
If a Trace Recording Session is active at the time of receiving a Trace
Session deactivation from the EM, the MME may choose to continue the Trace
Session and the Trace Recording Session till it ends gracefully or may stop it
immediately. In all cases, the MME shall deactivate the requested Trace
Session immediately at the end of the Trace Recording Session.
#### 4.1.3.7 E-UTRAN deactivation mechanisms for MDT
_When the eNodeB receives the indication from EM for MDT trace session
deactivation, it shall deactivate the trace session for those E-UTRAN cells
that have been indicated in the message. In case of immediate MDT trace
session the eNodeB shall deactivate the corresponding MDT RRC measurements in
the UEs that have been configured for immediate MDT as part of the given trace
session._
#### 4.1.3.8 Deactivation mechanisms at UE for MDT
The UE shall silently discard a logged MDT trace session when logging duration
expires and shall indicate the availability of logged measurement results to
the network next time it enters connected mode.
### 4.1.4 Signalling deactivation
#### 4.1.4.1 General
In Signalling deactivation, the Trace Deactivation shall always be carried out
from the Core Network EM only [EM (PS), EM (CS), EM(EPC) and EM (HSS) are
generally considered to be in the Core Network. A Core Network EM can be any
of these or their combinations]. In case of home subscriber trace (i.e. in the
HPLMN) the Trace Session deactivation shall go to the HSS, MSC Server/VLR,
SGSN or MME. In case of foreign subscriber trace (i.e. the HPLMN operator
wishes to deactivate tracing on foreign subscribers roaming in his PLMN) the
Trace Session deactivation shall go the MSC Server/VLR SGSN or MME. The
Management System shall deactivate the Trace Session in the same NE where it
activated the Trace Session.
When an HSS receives a Trace Session deactivation from its Management system,
it shall deactivate the active Trace Session corresponding to the Trace
Reference received in the deactivation message. The HSS shall delete all trace
control and configuration parameters associated with this Trace Session. If a
Trace Recording Session is active at the time of receiving a Trace Session
deactivation message from the EM, the HSS may choose to continue the Trace
Recording Session till it ends gracefully or may stop it immediately. In all
cases, the HSS shall deactivate the requested Trace Session immediately at the
end of the Trace Recording Session.
#### 4.1.4.2 UTRAN deactivation mechanisms
When RNC receives the CN_DEACTIVATE_TRACE message it shall deactivate the
Trace Session for the indicated Trace Reference in the CN_DEACTIVATE_TRACE
message. In case of simultaneous CS/PS connections, the trace session for the
indicated trace reference shall be closed upon reception of the CN DEACTIVATE
TRACE message from any of the CN domain, whether it was the one which
initiated trace session activation or not.
The Trace Session is also deactivated in the RNC when the Iu connection to the
Core Network is released.
If CN_INVOKE_TRACE message is received for only one Iu connection (either CS
or PS) the Trace Session shall be deactivated in the RNC when the
IU_RELEASE_COMMAND message is received from the Core Network for that Iu
connection where the CN_INVOKE_TRACE message is sent.
The following figure shows this behaviour:
Figure 4.1.4.2.1: Trace session deactivation (Signalling) in UTRAN 1
If CN_INVOKE_TRACE message is received by the RNC for both Iu-CS and Iu-PS
connection with the same Trace Reference number than the Trace Session shall
not be deactivated in the RNC when any of the Iu connection is released (when
the first IU_RELEASE_COMMAND message is received). The Trace Session shall be
deactivated when the second Iu connection is released (the second
IU_RELEASE_COMMAND message is received). The following figure shows the
situation.
Figure 4.1.4.2.2: Trace session deactivation (Signalling) in UTRAN 2
Interaction with Soft-handover
The Trace Session should be deactivated in a Drift RNC when the DRNC receives
the IUR_DEACTIVATE_TRACE message or the Iur connection is released.
When an RNC deactivates a Trace Session the Trace Recording Session shall also
be stopped at the same time.
NOTE: In RNC the Trace Session and the Trace Recording Session always the
same.
#### 4.1.4.3 PS Domain deactivation mechanisms
When an HSS receives a Trace Session deactivation from the Management System
it shall send a MAP_DEACTIVATE_TRACE_MODE message to the SGSN.
When the SGSN receives a MAP_DEACTIVATE_TRACE_MODE message it shall deactivate
the Trace Session identified by the Trace reference received in the
MAP_DEACTIVATE_TRACE_MODE message.
If a Trace Recording Session is active at the time of receiving a deactivation
message (in SGSN it is the MAP-DEACTIVATE_TRACE_MODE, in GGSN it is the GTP
Update PDP Context Request or the Update MBMS Context Request, in BM-SC it is
the Diameter Gmb STR message), the SGSN and/or the GGSN and/or the BM-SC may
choose to continue the Trace Recording Session till it ends gracefully or may
stop it immediately. In all cases, the SGSN/GGSN/BM-SC shall deactivate the
requested Trace Session immediately at the end of the Trace Recording Session.
When the SGSN deactivates the Trace Session, it shall delete all trace control
and configuration parameters associated with the corresponding Trace Session.
If SGSN deactivates the Trace Session during the Trace Recording Session, the
SGSN should deactivate the trace to the RNC by using the CN_DEACTIVATE_TRACE
RANAP message and should deactivate the trace to the GGSN by sending the GTP
Update PDP Context Request or the Update MBMS Context Request message with
Trace Activity Control set to Trace Deactivation.
If the GGSN deactivates the Trace Session during the Trace Recording Session,
the GGSN should deactivate the trace to the BM-SC (by sending a Diameter Gmb
STR message).
#### 4.1.4.4 CS Domain deactivation mechanisms
When an HSS receives Trace Session deactivation from the Management System it
shall send a MAP_DEACTIVATE_TRACE_MODE message to the MSC Server.
When the MSC Server receives a MAP_DEACTIVATE_TRACE_MODE message it shall
deactivate the Trace Session identified by the Trace reference received in the
MAP_DEACTIVATE_TRACE_MODE message.
If a Trace Recording Session is active at the time of receiving a
MAP_DEACTIVATE_TRACE_MODE message from the HSS, the MSC Server may choose to
continue the Trace Recording Session till it ends gracefully or may stop it
immediately. In all cases, the MSC Server shall deactivate the requested Trace
Session immediately at the end of the Trace Recording Session. When the MSC
Server deactivates the Trace Session it shall delete all trace control and
configuration parameters associated with the corresponding Trace Session. .
If MSC Server deactivates the Trace Session during a Trace Recording Session,
it should deactivate the trace to the RNC by sending the CN_DEACTIVATE_TRACE
RANAP message and should deactivate the trace to the MGW.
#### 4.1.4.5 Void
#### 4.1.4.6 void
##### 4.1.4.6.1 void
##### 4.1.4.6.2 void
##### 4.1.4.6.2.1 void
##### 4.1.4.6.2.2 void
##### 4.1.4.6.2.3 void
##### 4.1.4.6.3 Void
#### 4.1.4.7 EPC deactivation mechanisms
When an HSS receives a Trace Session Deactivation from the Management System
it shall send an S6a-Delete Subscriber Data Request message to the MME at
which the UE is currently registered if MME is included in the NE types for
Tracing, via the S6a interface to remove the "trace data" from subscription
data (see 3GPP TS 29.272[26]). The HSS shall deactivate trace if trace is
active at the HSS.
When the MME receives the S6a-Delete Subscriber Data Request message to remove
the "trace data" from subscription data (see 3GPP TS 29.272 [26]) or the Trace
Session is deactivated directly from the EM it shall deactivate the Trace
Session identified by the Trace Reference.
If the UE was registered to the HSS by an MME via the S6a interface, (i.e. the
user is attached to a 3GPP access network), the Trace Session shall be
deactivated to the MME via the S6a interface.
If the user was registered by a AAA server via the SWx interface (i.e. the
user is attached to a non-3GPP network) the HSS shall send the Trace Session
deactivation request with a push profile request.
The AAA server shall examine the received user profile and if it detects that
the Trace Session shall be deactivated, it shall initiate a re-authorization
procedure towards the PDN GW. The Trace Session is deactivated in the PDN GW
by using this re-authorization procedure.
When the PDN GW receives the updated authorization data with trace information
that represents Trace Session deactivation request, it shall deactivate the
Trace Session identified by the Trace Reference.
The following figure illustrates the Trace Session deactivation when the user
is attached to a non-3GPP access network for DSMIPv6 on S2c or PMIP on
S2a/S2b.
{width="3.8541666666666665in" height="3.1666666666666665in"}
Figure 4.1.4.7.1: Trace Session deactivation in case UE attached from non-3GPP
access network for DSMIPv6 on S2c or PMIP on S2a/S2b
If the user was registered by a AAA server via the SWx interface (i.e. the
user is attached to a non-3GPP network) the HSS shall send the Trace Session
deactivation request with a push profile request.
The AAA server shall examine the received user profile and if it detects that
the Trace Session shall be deactivated, it shall initiate a re-authorization
procedure towards the ePDG.\ The ePDG shall examine the received information
from the AAA and if it detects that the Trace Session shall be deactivated
(see 3GPP TS 29.273 [22]), it shall initiate a trace deactivation procedure
towards the PDN GW (see 3GPP TS 29.274 [34]).
When the PDN GW receives the data with trace information that represents Trace
Session deactivation request, it shall deactivate the Trace Session identified
by the Trace Reference.
Figure 4.1.4.7.2: Trace Session deactivation in case UE attached from non-3GPP
access network for GTP based S2b interface
When the MME receives the S6a-Delete Subscriber Data Request message to remove
the "trace data" from subscription data (see 3GPP TS 29.272 [26]) or the Trace
Session is deactivated directly from the EM it shall deactivate the Trace
Session identified by the Trace Reference.
If a Trace Recording Session is active at the time of receiving a deactivation
message, the MME may choose to continue the Trace Recording Session until it
ends gracefully or may stop it immediately. In all cases, the MME shall
deactivate the requested Trace Session immediately at the end of the Trace
Recording Session. When the MME deactivates the Trace Session, it shall delete
all trace control and configuration parameters associated with the
corresponding Trace Session.
If MME deactivates the Trace Session during the Trace Recording Session, the
MME should deactivate the trace at the eNB by sending the S1-Deactivate Trace
message to the eNodeB via the S1 interface and should deactivate the trace at
the SGW by sending an S11-Trace Session Deactivation message to the SGW via
the S11 interface. The message sent by MME shall include the Trace Reference
to identify the Trace Session that is to be deactivated.
When SGW receives an S11-Trace Session Deactivation message from the MME, the
SGW may choose to continue the Trace Recording Session until it ends
gracefully or may stop it immediately. In all cases, the SGW shall deactivate
the requested Trace Session immediately at the end of the Trace Recording
Session. If SGW deactivates the Trace Session during the Trace Recording
Session, the SGW should deactivate the trace at the PDN GW by sending the
S5-Trace Session Deactivation message to the PGW via the GTP based S5
interface. In case of PMIP based S5 interface the SGW should deactivate the
trace to the PDN GW using PCC signalling, i.e. by sending a Trace Deactivation
message to the PCRF and PCRF forwards the trace deactivation message to the
PDN GW [29].When the SGW deactivates the Trace Session, it shall delete all
trace control and configuration parameters associated with the corresponding
Trace Session.
When PGW receives an S5-Trace Session Deactivation message from the SGW, or
S2b-Trace Session Deactivation message from the ePDG, or it receives the Trace
Session Deactivation message from PCRF in case of PMIP based S5, the PDN GW
may choose to continue the Trace Recording Session until it ends gracefully or
may stop it immediately. In all cases, the PDN GW shall deactivate the
requested Trace Session immediately at the end of the Trace Recording Session.
When the PDN GW deactivates the Trace Session, it shall delete all trace
control and configuration parameters associated with the corresponding Trace
Session.
When a Trace Session Deactivation message is sent on any interface the Trace
Reference that identifies the Trace Session shall be included to the Trace
Session Deactivation message.
#### 4.1.4.8 E-UTRAN deactivation mechanisms
There are two different events that deactivate a Trace Session:
  1. When eNB receives the S1- Deactivate Trace message it shall deactivate the Trace Session for the indicated Trace Reference.
```{=html}
``` 1\. When the eNB releases the UE context the Trace Recording Session shall
be stopped and the Trace Session is deactivated at the eNB.
#### 4.1.4.9 EPC deactivation mechanisms for MDT
When the MME receives a Trace Session Deactivation request for an MDT Trace
Session of a UE, it shall act according to the following.
In case of an immediate MDT trace session and the UE being in connected mode,
the MME shall send trace session deactivation toward the eNodeB. The eNodeB
shall deactivate the corresponding MDT RRC measurements in the UE and shall
discard the given trace session context.
In case of an immediate MDT trace session and the UE being in idle mode, the
MME shall silently discard the stored trace session context.
Note: Signaling based deactivation does not apply for logged MDT trace
sessions, the logged MDT trace session terminates when logging duration
expires.
#### 4.1.4.10 Deactivation mechanisms at UE for MDT
The UE shall discard a logged MDT trace session when logging duration expires
and shall indicate the availability of logged measurement results to the
network next time it enters connected mode.
### 4.1.5 MDT Trace selection conditions
**In Immediate MDT, both in case of signalling based and management based MDT
trace activation, it is always the network that evaluates all selection
conditions for activating the MDT measurements and deactivating the MDT
measurements (this evaluation is done continuously during the selected call
session). The network activates and deactivates the MDT measurements toward
the UE accordingly via RRC.**
**In Logged MDT, the network configures UEs for MDT tracing that are eligible
based on the specified selection criteria. If area based condition is
specified in the trace configuration, it is sent to the UE at configuration
time and the UE will evaluate the area condition as it moves in the network in
idle mode.**
**Immediate and Logged MDT measurements shall always be configured as separate
trace sessions.**
**In cases of overlapping MDT configuration request the signaling based
request shall override the management based request. For logged MDT, prior to
re configuring, the eNB shall retrieve the MDT logs from the UE.**
## 4.2 Trace Recording Session Start / Stop triggering for Trace and MDT
### 4.2.1 General
The Trace Session activation contains the triggering events parameter. The
actual start/stop triggering events corresponding to the values of the
triggering events parameter are defined in triggering events tables in sub-
clause 5.1 in the present document.
If the NE failed to start the Trace Recording Session, a Trace failure
notification shall be sent to the TCE, and the Trace failure notification has
the the same parameters as the notification notifyTraceRecordingSessionFailure
defined in 3GPP TS 32.442 [24], the Trace failure notification file XML schema
is defined in Annex A.
### 4.2.2 Starting a trace recording session - management based
#### 4.2.2.1 UTRAN starting mechanisms
In an RNC, a Trace Recording Session should start after the reception of the
CN_INVOKE_TRACE message from the CN and if some activities have been started
on the interfaces that have been requested to be traced. The RNC shall record
those signalling messages in the interfaces that are defined in the _list of
interfaces_ parameter. Trace depth defines whether entire signalling messages
or just some IEs needs to be recorded.
The RNC may not start a Trace Recording Session if there are insufficient
resources available for the recording.
When RNC starts a Trace Recording Session it shall assign a Trace Recording
Session Reference for the Trace Recording Session.
When several PLMNs are supported in the RAN, for starting Trace and management
based MDT the RNC shall only select UEs where the pLMNTarget = PLMN identity
that the UE includes in Initial Direct Transfer message 3GPP TS 25.331 [31].
#### 4.2.2.2 PS Domain starting mechanisms
In a SGSN/GGSN/BM-SC, a Trace Recording Session should start after the
reception of a Trace Session Activation from EM and if any of the defined
_start triggering events_ occur. During the Trace Recording Session, the
SGSN/GGSN/BM-SC shall record those signalling messages in the interfaces that
are defined in the _list of interfaces_ parameter. The _Trace Depth_ parameter
defines whether entire signalling messages or just some IEs need to be
recorded.
The IMSI and IMEISV shall be available in the SGSN, in the GGSN and in the BM-
SC for at least those connections which shall be traced.
The SGSN/GGSN/BM-SC may not start a Trace Recording Session if there are
insufficient resources available for the recording.
If the SGSN/GGSN/BM-SC receives the Trace Session Activation during an
established session (e.g. during an active PDP context or an active MBMS
context), it _may_ start the Trace Recording Session immediately. However, if
any of the start triggering events occur in the SGSN/GGSN/BM-SC after
receiving the Trace Session Activation, it shall start the Trace Recording
Session.
When a Trace Recording Session is started, the SGSN/GGSN/BM-SC shall assign a
Trace Recording Session Reference for the Trace Recording Session.
#### 4.2.2.3 CS Domain starting mechanisms
In a MSC Server, a Trace Recording Session shall start after the reception of
a Trace Session Activation from EM and if any of the defined _start triggering
events_ occur. During the Trace Recording Session, the MSC Server shall record
those signalling messages in the interfaces that are defined in the _list of
interfaces_ parameter. The _Trace Depth_ parameter defines whether entire
signalling messages or just some IEs needs to be recorded.
The IMSI and the IMEISV shall be available in the MSC Server for at least
those connections which shall be traced.
The MSC Server may not start a Trace Recording Session if there are
insufficient resources available for the recording.
If the MSC Server receives the Trace Session Activation during an established
call, it _may_ start the Trace Recording Session immediately. However, if any
of the start triggering events occurs in MSC Server after receiving the Trace
Session Activation, it shall start the Trace Recording Session.
When a Trace Recording Session is started, the MSC Server shall assign a Trace
Recording Session Reference for the Trace Recording Session.
#### 4.2.2.4 Void
#### 4.2.2.5 E-UTRAN starting mechanism
In E-UTRAN, after the Cell Traffic Trace has been activated in the monitored
cell(s), the eNodeB shall start a Trace Recording Session for new
call(s)/session(s) and for already existing call(s)/session(s) (events for
existing call(s)/session(s) are not required to be recorded prior to the
activation of the cell traffic trace). When the eNodeB starts a Trace
Recording Session it shall allocate a Trace Recording Session Reference for
the given call or session. The eNodeB shall send the allocated Trace Recording
Session Reference, and the Trace Reference and the Trace Collection Entity
address in the CELL TRAFFIC TRACE message to the MME via the S1 connection.
When MME receives this new S1 signalling message containing the Trace
Recording Session Reference and Trace Reference, the MME shall look up the
IMSI/IMEI(SV) of the given call from its database and shall send the
IMSI/IMEI(SV) numbers together with the Trace Recording Session Reference and
Trace Reference to the Trace Collection Entity.
When several PLMNs are supported in the RAN, for starting Trace the eNB shall
only select UEs where the pLMNTarget = selectedPLMN-Identity that the UE
includes in RRCConnectionSetup message 3GPP TS 36.331 [32].
The format of the file sent to the TCE from the MME is defined in 3GPP TS
32.423, clause A.2.2.
The figure 4.2.2.5.1 illustrates the procedure.
Figure 4.2.2.5.1
#### 4.2.2.6 EPC Domain starting mechanisms
In a MME, SGW or PGW, a Trace Recording Session should start after the
reception of a Trace Session Activation from EM and if any of the defined
_start triggering events_ occur. During the Trace Recording Session, the MME,
SGW or PGW shall record those signalling messages in the interfaces that are
defined in the _list of interfaces_ parameter. The _Trace Depth_ parameter
defines whether entire signalling messages or just some IEs need to be
recorded.
The IMSI and IMEISV shall be available in the MME and in the SGW for at least
those connections which shall be traced.
The MME, SGW or PGW may not start a Trace Recording Session if there are
insufficient resources available for the recording.
If the MME, SGW or PGW receives the Trace Session Activation during an
established session (e.g. during an active PDP context), it may start the
Trace Recording Session immediately. However, if any of the start triggering
events occur in the MME, SGW or PGW after receiving the Trace Session
Activation, it shall start the Trace Recording Session.
When a Trace Recording Session is started, the MME, SGW or PGW shall assign a
Trace Recording Session Reference for the Trace Recording Session.
#### 4.2.2.7 E-UTRAN starting mechanisms for MDT
_A trace recording session of immediate MDT or logged MDT shall be started in
the eNodeB for each selected UE that satisfy the MDT UE selection criteria
(i.e. capability condition), provided that a cell trace session for immediate
MDT or logged MDT has been activated in the eNodeB from EM for the given
cell(s) before_.
_The eNodeB shall configure the corresponding MDT RRC measurements at the
selected UE._
When several PLMNs are supported in the RAN for management based MDT, possibly
combined with Trace, the eNB shall only select UEs where the pLMNTarget =
selectedPLMN-Identity that the UE includes in RRCConnectionSetup message 3GPP
TS 36.331 [32].
#### 4.2.2.8 Starting mechanisms at UE for MDT
_There is no starting mechanism at the UE for MDT trace recording sessions.
The UE shall execute the received MDT measurement configuration. In case of
logged MDT, the UE shall store the trace recording session parameters as
received from the eNodeB._
When several PLMNs are supported in the RAN, for starting logged MDT the UE
shall only perform logging for the cells recived in the MDT measuerment
configuration, if they are allowed as selected PLMNs.
### 4.2.3 Starting a trace recording session - signalling based
#### 4.2.3.1 UTRAN starting mechanisms
In an RNC the Trace Recording Session will always be the same as the Trace
Session as no triggering events are defined in UTRAN. Therefore a Trace
Recording Session should be started in an SRNC when the SRNC receives the
CN_INVOKE_TRACE message from the Core Network and if some activities have been
started on the interfaces that have been requested to be traced.
The CN_INVOKE_TRACE message that is received from the Core Network (MSC Server
or SGSN) contains the following information:
\- Trace Reference
\- UE identity (IMSI or IMEI(SV)
\- Trace Recording Session Reference
\- Trace Depth
\- List of interfaces for RNC
\- Job type
\- Area scope
\- List of measurements
\- Reporting Trigger
\- Report Interval
\- Report Amount
\- Event Threshold
\- Logging Interval
\- Logging Duration
\- IP address of Trace Collection Entity
\- MDT PLMN List
Note that at the same time not all of the parameters can be present. The
conditions which parameters shall be present is described in clause 5 of the
present document.
If the Job type parameter indicates MDT (e.g. Immediate or logged MDT is
required) in the CN_INVOKE_TRACE message the RNC shall also configure MDT to
the UE. The detailed mechanism of the MDT configuration to the UE is defined
in TS 37.320 [30] and TS 25.331 [31].
The RNC shall send the following parameters to the UE in case of Logged MDT:
\- Trace Reference
\- Trace Recording Session Reference
\- Area scope
\- TCE Id (The value signalled as IP address of TCE is mapped to a TCE Id,
using a configured mapping in the RNC).
\- Logging Interval
\- Logging Duration
\- MDT PLMN List
In case of Immediate MDT the RNC shall send the following parameters to the
UE:
\- List of measurements
\- Reporting Trigger
\- Report Interval
\- Report Amount
\- Event Threshold
Note that at the same time not all of the parameters can be present. The
conditions which parameters shall be present is described in clause 5 of the
present document.
If the SRNC does not have enough resources it may not start a Trace Recording
Session.
The Trace Recording Session Reference shall be the same as received in the
CN_INVOKE_TRACE message.
In a DRNC the Trace Recording Session should be started when the DRNC receives
the IUR_INVOKE_TRACE message. If the DRNC does not have enough resources it
may not start a Trace Recording Session.
The Trace Session is activated to the RNC by sending a CN_INVOKE_TRACE message
from the CN (MSC Server or SGSN). When RNC receives the CN_INVOKE_TRACE
message it should immediately start a Trace Session and a Trace Recording
Session according to the trace control and configuration parameters received
in the CN_INVOKE_TRACE message.
If there are not enough resources in RNC to start a Trace Recording Session,
the RNC may reject to start a Trace Recording Session. However the RNC shall
start the Trace Session. Session and if MDT activation is requested shall
activate the MDT to the UE.
When SRNC/DRNC receives the trace control and configuration parameters:
\- If the Trace Reference is the same as an existing Trace Session for the
same subscriber or equipment in SRNC/DRNC, the SRNC/DRNC shall not activate a
new Trace Session and the existing Trace Session will not be impacted;
\- If the Trace Recording Session Reference is the same as an existing Trace
Recording Session in the existing Trace Session having the same Trace
Reference, the SRNC/DRNC shall not start a new Trace Recording Session;
\- If the trace control and configuration parameters are received from the
same CN domain (CS/PS) as the existing Trace Recording Session(s) if any, and
the Trace Recording Session Reference is not the same as any existing Trace
Recording Session(s) in the existing Trace Session having the same Trace
Reference, the SRNC/DRNC shall start a new Trace Recording Session;
\- If the trace control and configuration parameters are received from
different CN domain (CS/PS) as the existing Trace Recording Session(s) if any
(i.e. the RNC has simultaneoud CS and PS connection and CN_INVOKE_TRACE is
received from both connection), regardless of the Trace Recording Session
Reference is the same or not as any existing Trace Recording Session(s) in the
existing Trace Session having the same Trace Reference, the SRNC shall not
start a new Trace Recording Session;
\- If the Trace Reference is the same as an existing Trace Session for
different subscriber(s) or equipment(s) in SRNC/DRNC, the SRNC /DRNC shall not
activate a new Trace Session, and the SRNC/DRNC shall not start a new Trace
Recording Session.
The following figure shows an example for a CS call how the Trace Session is
activated to RNC. In the example it is assumed that there is no PS connection
at all during the CS call.
Figure 4.2.3.1.1: Starting a Trace Recording Session (Signalling) in UTRAN
##### Interaction with soft-handovers {#interaction-with-soft-handovers .H6}
If the subscriber or equipment, which is traced, makes a soft handover the
SRNC should propagate the trace control and configuration parameters
(including MDT specific parameters if they are available) further to the DRNC
by using the IUR_INVOKE_TRACE message. When the DRNC receives the
IUR_INVOKE_TRACE message it should immediately start a Trace Session and a
Trace Recording Session according to the trace control and configuration
parameters received in the IUR_INVOKE_TRACE message.
If there are insufficient resources in the DRNC, the DRNC may not start a
Trace Recording Session.
The Trace Recording Session Reference sent by the SRNC to the DRNC shall be
the same what SRNC has received in the CN_INVOKE_TRACE message from the CN.
##### Interaction with Relocation {#interaction-with-relocation-1 .H6}
If the tracing shall continue also after the relocation has been performed,
the CN Invoke Trace procedure shall be re-initiated from the CN towards the
future SRNC after the Relocation Resource Allocation procedure has been
executed successfully.
#### 4.2.3.2 PS Domain starting mechanisms
In SGSN/GGSN/BM-SC a Trace Recording Session should start after the reception
of a Trace Session Activation message (in SGSN it is the MAP-
ACTIVATE_TRACE_MODE, in GGSN it is the GTP-Create PDP Context request or
Update PDP Context request, in BM-SC it is the Diameter Gmb AAR message) and
if any of the defined _start triggering events_ occur. During the Trace
Recording Session, the SGSN/GGSN/BM-SC shall record the signalling messages in
the interfaces that are defined in the _list of interfaces_ parameter. The
_Trace Depth_ parameter defines whether entire signalling messages or just
some IEs need to be recorded.
The SGSN/GGSN/BM-SC may not start a Trace Recording Session if there are
insufficient resources available for the recording.
In case of an established session, the SGSN may start the Trace Recording
Session immediately after the reception of the Trace Session Activation
message. However, if any of the start triggering events occurs in SGSN after
receiving the Trace Session activation message, it shall start the Trace
Recording.
When a Trace Recording Session is started in SGSN, it shall assign a Trace
Recording Session Reference for the Trace Recording Session. When the SGSN
propagates the Trace control and configuration parameters to GGSN or to UTRAN
(I.e. activates a Trace Session in GGSN/UTRAN), it shall include the assigned
Trace Recording Session Reference in the Trace Session Activation message.
When an SGSN starts a Trace Recording Session and the list of NE types
parameter requires GGSN tracing, it shall send the GTP- Update PDP Context
Request or Create PDP Context Request message for activating the Trace Session
to GGSN. When a GGSN starts a Trace Recording Session and the list of NE types
parameter requires BM-SC tracing, it shall send a Diameter Gmb AAR message to
the BM-SC in order to activate a Trace Session in the BM-SC. Also, when an
SGSN starts a Trace Recording Session and the list of NE types parameter
requires RNC tracing, it shall send the CN_INVOKE_TRACE message to the RNC in
order to activate a Trace Session in RNC. In both cases the Trace Session and
the Trace Recording Session in the receiving NE should start at the same time.
In case of SRNS relocation the SGSN shall send the CN_INVOKE_TRACE message to
the new SRNC after the successful Relocation Resource Allocation procedure.
SGSN has to find the identity of the mobile before it activates a Trace
Session towards other NE. The IMEI(SV) can be got from the Mobile by using the
Identification procedure on the Iu interface.
When the SGSN sends the Trace Session activation (CN_INVOKE_TRACE) message to
RNC it shall include the following parameters to the message:
  * IMSI or IMEI (SV) (M).
  * Trace reference (M).
  * Trace Recording Session Reference (M).
  * Trace Depth (M).
  * List of interfaces (O).
  * IP address of Trace Collection Entity (O).
#### 4.2.3.3 CS Domain starting mechanisms
In MSC Server/MGW a Trace Recording Session should start after the reception
of a Trace Session Activation message (MAP-ACTIVATE TRACE MODE in MSC Server
and ADD/MOD command with Trace package in MGW) and if any of the defined
_start triggering events_ occur. During the Trace Recording Session the MSC
Server/MGW shall record the signalling messages in the interfaces that are
defined in the _list of interfaces_ parameter. The _Trace Depth_ parameter
defines whether entire signalling messages or just some IEs need to be
recorded.
The MSC Server may not start a Trace Recording Session if there are
insufficient resources available for the recording.
In case of an established call, the MSC Server may start the Trace Recording
Session immediately after the reception of the MAP-ACTIVATE_TRACE_MODE
message. However, if any of the start triggering events occur in the MSC
Server after receiving the Trace Session activation message, it shall start
the Trace Recording Session.
When a Trace Recording Session is started in MSC Server, it shall assign a
Trace Recording Session Reference for the Trace Recording Session. When the
MSC Server propagates the Trace control and configuration parameters to MGW or
to UTRAN (I.e. activates a Trace Session in MGW/UTRAN) it shall include the
assigned Trace Recording Session Reference in the Trace Session Activation
message.
When an MSC Server starts a Trace Recording Session and the list of NE types
parameter requires MGW tracing, it shall send the ADD/MOD command with trace
package to MGW in order to activate the trace in MGW. Also, when an MSC Server
starts a Trace Recording Session and the list of NE types parameter requires
RNC tracing, it shall send the CN_INVOKE_TRACE message to the RNC. In both
cases the Trace Session and the Trace Recording Session in the receiving NE
should start at the same time.
MSC Server has to find the identity of the mobile before it activates a Trace
Session towards other NE. The IMEI(SV) can be got from the Mobile by using the
Identification procedure on the Iu interface.
In case of SRNS relocation the MSC Server shall send the CN_INVOKE_TRACE
message to the new SRNC after the successful Relocation Resource Allocation
procedure. The following figure shows an example how the Trace Session is
activated with CN_INVOKE_TRACE message in case of relocation.
Figure 4.2.3.3.1: Starting a Trace Recording Session (Signalling) in CS Domain
When the new SRNC receives the CN_INVOKE_TRACE message it should start
immediately a Trace Session and a Trace Recording session according to the
trace control and configuration parameters received in the CN_INVOKE_TRACE
message. The Trace Session shall automatically be deactivated in the old RNC
when the Iu connection is released.
When the MSC Server sends the Trace Session activation (CN_INVOKE_TRACE)
message to RNC it shall include the following parameters to the message:
  * IMSI or IMEI (SV) (M).
  * Trace reference (M).
  * Trace Recording Session Reference (M).
  * Trace Depth (M).
  * List of interfaces to trace (O).
  * IP address of Trace Collection Entity (O).
#### 4.2.3.4 Void
#### 4.2.3.5 void
##### 4.2.3.5.1 void
##### 4.2.3.5.2 void
##### 4.2.3.5.3 void
##### 4.2.3.5.4 void
#### 4.2.3.6 E-UTRAN starting mechanism
In an eNB the Trace Recording Session will always be the same as the Trace
Session as no triggering events are defined in eNB.
Tracing starts immediately at eNodeB upon reception of the trace control and
configuration parameters. The eNodeB may not start a Trace Recording Session
if there are insufficient resources available for the recording, however, the
eNodeB shall store the trace control and configuration parameters, and forward
these parameters when the UE handovers to other eNBs over X2.
The Trace Recording Session shall be started at the eNB when it receives trace
control and configuration parameters via one of the following messages:
  1. via an S1-Initial Context Setup Request message from the MME in response to an S1-Initial UE Message
  2. via an S1-Trace Start message from the MME in response to an S1-Initial UE Message or when an established S1AP connection exists
  3. via an S1-Handover Request message from the target MME as part of intra/inter-MME handover procedures via S1
  4. via an X2-Handover Request message from a source eNodeB as part of inter-eNodeB handover procedures via X2
There can only be one Trace Recording Session Reference per Trace Reference at
one given time for a UE trace session. So there shall be only one TR/TRSR to
be propagated during S1 and X2 handover.
If the Trace Reference is the same as an existing Trace Session for the same
subscriber or equipment, and the Trace Recording Session Reference is the same
as the existing Trace Recording Session in the existing Trace Session having
the same Trace Reference, the eNB shall not start a new Trace Recording
Session and shall continue with the existing trace session and ignore the
second request.
If the Trace Reference is the same as an existing Trace Session for the same
subscriber or equipment, and the Trace Recording Session Reference is not the
same as the existing Trace Recording Session in the existing Trace Session
having the same Trace Reference, the eNB shall continue with the existing
trace session and ignore the second request.
#### 4.2.3.7 EPC starting mechanisms
In MME/SGW/PGW a Trace Recording Session should start after the reception of a
Trace Session Activation message and if any of the defined _start triggering
events_ occur. During the Trace Recording Session, the MME/SGW/PGW shall
record the signalling messages in the interfaces that are defined in the _list
of interfaces_ parameter. The _Trace Depth_ parameter defines whether entire
signalling messages or just some IEs need to be recorded.
The MME/SGW/PGW may not start a Trace Recording Session if there are
insufficient resources available for the recording.
In case of an established session, the MME/SGW/PGW may start the Trace
Recording Session immediately after the reception of the trace control and
configuration parameters. However, if any of the start triggering events
occurs in MME/SGW/PGW after receiving the trace control and configuration
parameters, it shall start the Trace Recording Session.
In the case of the _triggering events_ come into collision on the same traced
UE as defined in 3GPP TS 24.301[33], the MME shall not start a new Trace
Recording Session for the later event(s), and shall use the existing Trace
Recording Session and Trace Recording Session Reference to continuing the
trace recording for these events until one stop triggerring event occurs.
MME shall start a Trace Recording Session for a certain Trace Session only if
there is no ongoing Trace Recording Session for this Trace Session. i.e. at
any given time, there can be a maximum of one Trace Recording Session for a
certain Trace Session.
When a Trace Recording Session is started in MME, it shall assign a Trace
Recording Session Reference for the Trace Recording Session. When the MME
propagates the Trace control and configuration parameters to E-UTRAN (i.e.
activates a Trace Session in eNB), it shall include the assigned Trace
Recording Session Reference in the Trace Session Activation message.
Also, when an MME starts a Trace Recording Session and the list of NE types
parameter requires eNB tracing, it shall propagate the trace control and
configuration parameters including the Trace Recording Session Reference via
the S1 interface to the eNodeB per one of the following messages:
  1. if an S1 connection exists, via the S1-Trace Start message
  2. if the S1 connection does not exist, via the S1-Trace Start message prior to S1 connection setup, or via the S1-Initial Context Setup Request message during S1 connection setup
  3. during intra/inter-MME handover over S1, via the S1-Handover Request message
In above cases the Trace Session and the Trace Recording Session in the
receiving NE should start at the same time
If all events are set in the triggering event parameter at the MME, MME shall
send Trace Session Activation message to eNB not only when the MME starts the
Trace Recording Session, but also when an Intra-MME handover happens. In this
case the MME shall send Trace Session activation to the target eNB via the
S1-Handover Request message..
NOTE: In case of \"UE-Initiated Detach Procedure with UE camping on
GERAN/UTRAN and ISR activated / SGSN-Initiated Detach Procedure with ISR
activated\",\ Trace is not activated in eNB.
#### 4.2.3.8 EPC starting mechanisms for MDT
In the MME, no trace recording sessions are started for MDT trace sessions.
The MME sends the trace session activation to the eNodeB with parameters as
specified in 4.1.2.12.
#### 4.2.3.9 E-UTRAN starting mechanisms for MDT
A trace recording session of either immediate or logged MDT shall be started
in the eNodeB for a given UE when a trace session activation request is
received from the MME for the UE and the MDT UE selection conditions are
satisfied for the UE. The eNodeB shall configure the corresponding MDT RRC
measurements at the UE. If selection conditions are not satisfied, the eNodeB
shall store the trace control and configuration parameters, and forward these
parameters when the UE handovers to other eNBs over X2 or S1.
If the eNodeB receives a Signalling Based MDT activation request when the UE
is served by a cell that is in the eNodeB but not in the MDT area scope then
the eNodeB shall store the MDT configuration and configure the UE when the UE
moves to a cell in the eNodeB (intra eNodeB handover) that satisfies the area
scope in the request.
#### 4.2.3.10 Starting mechanisms at UE for MDT
_There is no starting mechanism at the UE for MDT trace recording sessions.
The UE shall execute the received MDT measurement configuration. In case of
logged MDT, the UE shall store the trace recording session parameters as
received from the eNodeB._
### 4.2.4 Stopping a trace recording session - management based
#### 4.2.4.1 UTRAN stopping mechanisms
The Trace Recording Session in the RNC shall be stopped when the last
connection, which belongs to the traced subscriber/mobile, is released.
#### 4.2.4.2 PS Domain stopping mechanisms
In SGSN, GGSN and BM-SC a Trace Recording Session shall be stopped when any of
the defined stop triggering events occur. If Trace Session deactivation is
received during the Trace Recording Session, the SGSN is allowed to finish
tracing of the on-going procedures (e.g. session). In this case the Trace
Recording Session shall be stopped between the reception of the Trace Session
deactivation and the appropriate stop-triggering event.
The following figure illustrates the successful case in tracing a PDP context
when a Trace Recording Session is stopped.
Figure 4.2.4.2.1: Stopping a Trace Recording Session for a PDP Context
(Management Based) - PS domain
The following figure illustrates the successful case in tracing a MBMS context
when a Trace Recording Session is stopped.
Figure 4.2.4.2.2: Stopping a Trace Recording Session for a MBMS Context
(Management Based) - PS domain
#### 4.2.4.3 CS Domain stopping mechanisms
In MSC Server a Trace Recording Session shall be stopped when any of the
defined stop triggering events occur. If Trace Session deactivation is
received during the Trace Recording Session, the MSC Server is allowed to
finish tracing of the on-going procedures (e.g. calls). In this case the Trace
Recording Session shall be stopped in MSC Server between the reception of the
Trace Session deactivation and the appropriate stop-triggering event.
The following figure illustrates the successful case in tracing a call and the
time of stopping a Trace Recording Session.
Figure 4.2.4.3.1: Stopping a Trace Recording Session (Management Based) \- CS
domain
#### 4.2.4.4 Void
#### 4.2.4.5 E-UTRAN stopping mechanisms
The Trace Recording Session in the eNodeB shall be stopped when the
call/session is ended in the cell under trace or the call/session is haneded
over to another cell. If the Trace Session is deactivated at a time when there
are ongoing sessions the trace recording session may be stopped immediately or
gracefully when the session ends.
#### 4.2.4.6 EPC Domain stopping mechanisms
In MME, SGW and PGW a Trace Recording Session shall be stopped when any of the
defined stop triggering events occur. If Trace Session deactivation is
received from its EM during the Trace Recording Session, the MME, SGW and PGW
are allowed to finish tracing of the on-going procedures (e.g. session). In
this case the Trace Recording Session shall be stopped between the reception
of the Trace Session deactivation and the appropriate stop-triggering event.
#### 4.2.4.7 E-UTRAN stopping mechanisms for MDT
In case of immediate MDT, the eNodeB shall stop a trace recording session for
a given UE when the UE changes cell or goes to idle mode or when the cell
trace session is deactivated at the eNodeB from its EM. The eNodeB shall
deactivate the corresponding MDT RRC measurements in the UE.
In case of logged MDT, there is no stopping mechanism in the eNodeB. The
eNodeB does not need to maintain a logged MDT trace recording session once it
has been configured in the UE.
#### 4.2.4.8 Stopping mechanisms at UE for MDT
In case of logged MDT, the UE shall stop an ongoing trace recording session
when logging duration expires and it shall indicate the availability of logged
measurement results to the network next time it enters connected mode.
The UE shall discard an ongoing logged MDT trace recording session when it
receives a new logged MDT trace recording session configuration from the
network.
### 4.2.5 Stopping a trace recording session - signalling based
#### 4.2.5.1 UTRAN stopping mechanisms
In an RNC the Trace Recording Session will always be the same as the Trace
Session as no triggering events are defined in UTRAN. Therefore a Trace
Recording Session shall always be stopped in an RNC when the RNC deactivates
the Trace Session. For more information on Trace Session deactivation in UTRAN
see subclause 4.1.4.2.
#### 4.2.5.2 PS Domain stopping mechanisms
A Trace Recording Session shall be stopped when the SGSN/GGSN/BM-SC detect any
of the stop triggering events.
However, if a SGSN receives a Trace Session deactivation either from its EM
(in case of tracing roaming subscribers) or from HSS (in case of tracing home
subscribers) during an ongoing Trace Recording Session, it may stop it
immediately or at any time until the occurrence of an appropriate stop-
triggering event.
A GGSN shall stop a Trace Recording Session when it receives a Trace Session
deactivation message (GTP- Update PDP Context Request and Trace Activity
Control is set to Trace Deactivation )from the SGSN or at any time until the
occurrence of an appropriate stop-triggering event.
A BM-SC shall stop a Trace Recording Session when it receives a Diameter Gmb
STR message from the GGSN or at any time until the occurrence of an
appropriate stop-triggering event.
When a Trace Recording Session is stopped in a SGSN, the SGSN shall send a
Trace Session deactivation message to the NEs where tracing was required, as
defined in the \"List of NE types\" configuration parameter, received in the
Trace Session activation message. The Trace Reference, used for the
deactivation procedure, shall be the same as used in the SGSN for the
activation of the Trace Session.
The following figure illustrates a successful case in tracing a PDP context,
when a Trace Recording Session is stopped. (Reference 3GPP TS 23.060 [6].)
NOTE: The activation to SGSN can come from EM-SGSN (in the figure just EM) or
from the HSS.
Figure 4.2.5.2.1: Stopping a Trace Recording Session for a PDP Context
(Signalling based) - PS domain
The following figure illustrates a successful case in tracing a MBMS context,
when a Trace Recording Session is stopped. (Reference 3GPP TS 23.246 [9].)
Figure 4.2.5.2.2: Stopping a Trace Recording Session for a MBMS Context
(Signalling based) - PS domain
#### 4.2.5.3 CS Domain stopping mechanisms
A Trace Recording Session shall be stopped when the MSC Server and MGW detect
any of the stop triggering events.
However, if a MSC Server receives a Trace Session deactivation either from its
EM (in case of tracing roaming subscribers) or from HSS (in case of tracing
home subscribers) during an ongoing Trace Recording Session, it may stop it
immediately or at any time until the occurrence of an appropriate stop-
triggering event.
A MGW shall stop a Trace Recording Session when it receives a MOD command with
trace package (indicating Trace Deactivation) from the MSC Server or at any
time until the occurrence of an appropriate stop-triggering event.
When a Trace Recording Session is stopped in a MSC Server, the MSC Server
shall send a Trace Session deactivation message to the NEs where tracing was
required, as defined in the \"List of NE types\" configuration parameter,
received in the Trace Session activation message. The Trace Reference, used
for the deactivation procedure, shall be the same as used in the MSC Server
for the activation of the Trace Session.
The following figure illustrates a successful case in tracing a call, when a
Trace Recording Session is stopped. (Reference 3GPP TS 23.205 [7] and 3GPP TS
23.108 [8].)
Figure 4.2.5.3.1: Stopping a Trace Recording Session (Signalling based) \- CS
domain
#### 4.2.5.4 Void
#### 4.2.5.5 void
##### 4.2.5.5.1 void
##### 4.2.5.5.2 void
##### 4.2.5.5.3 void
#### 4.2.5.6 void
#### 4.2.5.7 E-UTRAN stopping mechanisms
In an eNB the Trace Recording Session will always be the same as the Trace
Session as no triggering events are defined in E-UTRAN. Therefore a Trace
Recording Session shall always be stopped in an eNB when the eNB deactivates
the Trace Session since there can be only 1 trace reference/trace recoding
session reference combination per Trace Session at any given time. For more
information on Trace Session deactivation in E-UTRAN, see subclause 4.1.4.8.
#### 4.2.5.8 EPC Domain stopping mechanisms
A Trace Recording Session may be stopped when the MME/SGW/PGW detect any of
the stop triggering events. Detection of a stop trigger event results in
MME/SGW/PGW immediately stopping the trace recording session.
However, if an MME receives a Trace Session deactivation either from its EM
(in case of tracing roaming subscribers) or from HSS (in case of tracing home
subscribers) during an ongoing Trace Recording Session, it may stop it
immediately or at any time until the occurrence of an appropriate stop-
triggering event.
When a Trace Recording Session is stopped in an MME, the MME may send a
S1-Deactivate Trace message to the eNB where tracing was required, as defined
in the \"List of NE types\" configuration parameter, received in the Trace
Session activation message. . If the triggering event parameter indicates that
all events shall be traced, the MME shall not send the S1-Deactivate Trace
message to the eNB. If the Trace Recording Session is not terminated in the
MME, then it shall not be deactivated in the eNB. The Trace Reference, used
for the deactivation procedure, shall be the same as used in the MME for the
activation of the Trace Session. This only applies to the eNB as the PGW and
SGW have their own triggering criteria.
#### 4.2.5.9 EPC stopping mechanisms for MDT
There is no stopping mechanism in the EPC for MDT trace recording sessions, as
there are no starting mechanisms either (see also clause 4.2.3.8).
#### 4.2.5.10 E-UTRAN stopping mechanisms for MDT
In case of immediate MDT, the eNodeB shall stop an ongoing trace recording
session for a given UE when a trace session deactivation is received from the
MME. The eNodeB shall deactivate the corresponding MDT measurements in the UE.
If the configured area scope is not satifisfied in the target cell after a
handover, the eNB may deactivate the Immediate MDT configured to the UE like
explained in clause 4. 4.
In case of logged MDT, there is no stopping mechanism in the eNodeB. The
eNodeB does not need to maintain a logged MDT trace recording session once it
has been configured in the UE.
#### 4.2.5.11 Stopping mechanisms at UE for MDT
In case of logged MDT, the UE shall stop an ongoing trace recording session
when logging duration expires and it shall indicate the availability of logged
measurement results to the network next time it enters connected mode.
The UE shall discard an ongoing logged MDT trace recording session when it
receives a new logged MDT trace recording session configuration from the
network.
### 4.2.6 Void
### 4.2.7 Void
### 4.2.8 Void
#### 4.2.8.1 Void
#### 4.2.8.2 Void
### 4.2.9 Void
## 4.3 RLF reporting
### 4.3.1 Trace session activation for RLF reporting
RLF reporting is activated to the eNB as a special Trace Session where the job
type indicates RLF reporting only. The detailed procedure is shown in figure
4.3.1 where one UE experiences an RLF event and the reestablishment is
successful to the source eNB.
Figure 4.3.1.1 Example scenario for RLF reporting when UE reestablishment is
successful at source eNB.
When the eNB receives the Trace Session activation indicating RLF reporting
only, the eNB shall start a Trace Session. This Trace Session shall collect
only RLF reports received from the UE. The Trace Session activation message
received from the EMS shall contain the following information:
  * Trace Reference
  * Job type=RLF reporting only
  * IP address of the TCE
Figure 4.3.2 shows another example where the UE reestablishment is failed in
the source eNB, but successful at a target eNB.
**Figure 4.31.2 Example scenario for RLF reporting when the UE reestablishment
is successful at target eNB**
If the UE re-establishes the RRC connection successfully at the target eNB the
RLF reports are fetched by the target eNB. The target eNB forwards the RLF
report in the X2 RLF Indication message. The procedures to be used at eNB to
forward the RLF reports towards the management system is the same as the
reporting will be done by the source eNB in this case.
If a UE detects a Radio Link Failure event, it collects certain information as
described in TS 36.300[37] and TS 36.331 [32]. Once the eNB retrieved the RLF
report from the UE or received it from the target eNB via X2, as defined in TS
36.300[37], it shall save to the Trace Record. The Trace Record containing the
RLF reports can be transferred to the TCE in the same mechanism as for normal
subscriber and equipment trace or for MDT.
### 4.3.2 Trace session deactivation for RLF reporting
_When the eNB receives the indication from the EM for trace session
deactivation with the job type "RLF reporting only", it shall deactivate the
trace session for the indicated trace reference of RLF reporting and stop RLF
reporting to the TCE._
## 4.4 Handling of MDT Trace sessions at handover for Immediate MDT
**The eNB/RNC shall activate the Immediate MDT in the UE if the area based
selection conditions are satisfied or not in the target cell after a handover
that is made over X2 or S1 (or over Iur or Iu in case of UMTS). If the area
based selection conditions are not satisfied in the handover target cell, the
eNB/ RNC may deactivate the Immediate MDT in the UE. The trace sessions and
trace recording sessions are not visible for the UE.**
**In case of signalling based trace activation (subscription based MDT), the
eNB/RNC shall propagate the Trace Session parameters together with the MDT
specific parameters to the target cell regardless of whether the source or
target cell is part of the configured area scope in case of an Intra-PLMN
handover over X2 or S1 (or Iur or Iu in case of UMTS).**
**In case of UTRAN the RNC shall propagate the Trace Session of the UE to the
target cell in case of a handover over Iur or Iu. Any trace recording session
shall be maintained, stopped or started in the target cell according to the
evaluation of the selection criteria.**
For LTE, the MDT configuration received by signalling based trace messages for
a specific UE will propagate during intra-PLMN handover, and may propagate
during inter-PLMN handover if the Signalling Based MDT PLMN List is available
and includes the target PLMN. This behaviour applies also for MDT
configuration that includes area scope, regardless of whether the source or
target cell is part of the configured area scope.
For UMTS, the MDT configuration received by signalling based trace messages
for a specific UE will continue during intra-PLMN handover, and may continue
during inter-PLMN handover if the Signalling Based MDT PLMN List is available
and includes the target PLMN, except for the case of SRNS relocation. In the
case of SRNS relocation, MDT may be reactivated by the Core Network following
a successful relocation.
For signalling based MDT configuration (i.e. subscription based MDT), when a
UE that has been configured with MDT hands over to another eNB (i.e., in
connected mode) and the Signalling Based MDT PLMN List conditions mentioned
above are satisfied:
\- with an X2 handover: the MDT configuraiton shall be passed to the eNB in
the X2 handover request for continuity of MDT data collection . The new eNB
shall stop the MDT collection if the new conditions are not within the
criteria for MDT data collection.
\- with an S1 handover and with no MME relocation: with S1 handover the MME
shall ensure the MDT configuration is sent to the new eNB.
\- with an S1 handover and with MME relocation: MDT configuration shall be
passed on to the new MME on MME relocation. During inter-MME handover, the MME
shall propagate the MDT configuration parameters to the target MME within an
S10- Forward Relocation Request message as part of inter-MME handover
procedures. The new MME shall save the information as part of the UE context
and forward the MDT configuration to the new eNB.
The following MDT configuration shall be passed during handovers (Either
intra-eNB, inter-eNB or inter-MME HO):
\- Trace Session Reference
\- Trace Recording Session Reference
\- Area scope
\- List of measurements
\- Report Amount
\- Reporting Trigger
\- Event Threshold
\- Report Interval
\- IP address of TCE
\- Job type
\- Measurement period LTE (if either of the measurements M4, M5 is requested)
\- Positioning method
\- Collection period for RRM measurements LTE (present only if any of M2 or M3
measurements are requested)
\- MDT PLMN List
Note that at the same time not all the parameters can be present. The
conditions are described in clause 5.10 of the present document.
## 4.5 Handling of MDT Trace sessions at handover for Logged MDT
In logged MDT mode, no propagation of the MDT configuration is performed.
## 4.6 User consent handling in MDT
#### 4.6.1 Signalling based MDT
In case of signalling based MDT getting user consent before activating the MDT
functionality is required because of privacy and legal obligations. It is the
Operator responsibility to collect user consent before initiating an MDT for a
specific IMSI or IMEI number.
Collecting the user consent shall be done via customer care process. The user
consent information availability should be considered as part of the
subscription data and as such this shall be provisioned to the HSS database.
The following figure summarizes the functionality.
Figure 4.5.1.1
When the IMSI based MDT is activated it is targeted the HSS. Once the user
consent availability information is stored in the HSS database, the HSS can
check the user consent availability before starting a Trace Session for the
given subscriber. If there is no user consent given by the specific user to
network where TCE resides, the HSS should not start a Trace Session for the
given subscriber.
As the user consent availability information is stored as part of the
subscription data it should also be transferred to the MME/SGSN/MSC-S during
update location procedure. This is required if the subscription based MDT is
started from MME/SGSN/MSC-S. In that case similar checking is required as in
the HSS case.
It should also be possible to handle user consent revocation. The process of
user consent revocation shall be done also via customer care process and the
user consent availability information should be updated in the HSS DB when a
user consent revocation happens.
If the user consent revocation happens during an ongoing Trace Session with
MDT, it is not required to stop and deactivate the Trace Recording Session,
Trace Session respectively immediately i.e. to stop an ongoing Trace Recording
Session in case of Immediate MDT. A notification to the management system
should be sent and the management system should deactivate the Trace Session.
#### 4.6.2 Area based MDT
In case of area based MDT getting user consent is required before activating
the MDT functionality because of privacy and legal obligations. The same user
consent information can be used for area based MDT and for signalling based
MDT (i.e. there is no need to differentiate the user consent per MDT type).
Collecting the user consent shall be done via customer care process. The user
consent information availability shall be considered as part of the
subscription data and as such this shall be provisioned to the HSS database.
The following figure shows an example scenario summarizing the functionality.
Figure 4.6.2.1: Example for delivering user consent information in area based
MDT
When UE attaches to the network, the HSS shall forward the user consent
information, stored in the HSS database, to the corresponding MME/SGSN/MSC-S.
When the MME/SGSN/MSC-S receive the user consent information it shall store it
in its subscriber database.
The MME/SGSN/MSC-S shall also check the roaming status of the user. If the
user is within his home operator's PLMNs and the user has given his consent,
the MME/ SGSN/MSC-S shall send the Management Based MDT Allowed IEto the
eNB/RNC during the UE context setup procedure. Otherwise the MME/ SGSN/MSC-S
shall not send the Management Based MDT Allowed IE to the eNB/RNC.
If the result of the roaming status check indicates a home subscriber,
MME/SGSN/MSC-S shall forward the already stored user consent information to
the corresponding eNodeB/RNC as part of Management Based MDT Allowed IE.
When the area based MDT activation is sent to eNodeB/RNC, eNodeB/RNC shall
check the availability of the Management Based MDT Allowed IE before making
the UE selection. In case the Management Based MDT Allowed IE is not
available, the eNodeB/RNC shall not select the UE. In case the Management
Based MDT Allowed IE is available, the eNodeB/RNC shall verify if the UE's
RPLMN matches the PLMN where TCE resides -- Trace Reference PLMN (PLMN portion
of the Trace Reference). In case of a mismatch, the eNodeB/RNC shall not
select the UE.The eNB/RNC shall forward the received Management Based MDT
Allowed IE during X2/Iur based handovers to the target node. The Management
Based MDT Allowed IE is stored in the eNB/RNC as part of the UE context. If
the user consent information is updated while a UE context is already set up
in the eNB, the changed user consent should be taken into account in the next
call/session setup.
## 4.7 Anonymization of MDT data for area based MDT
If the job type is either Immediate MDT or Logged MDT or combined Immediate
MDT and trace, the anonymization requirements are applicable as described in
this clause.
In case of UTRAN/E-UTRAN the anonymization of MDT data depends on the
configuration parameter received at the MDT configuration. There are two
levels of anonymization:
\- Using IMEI-TAC.
\- Not sending any identity to the TCE.
If the anonymization indicates that no identity should be sent to the TCE:
\- For E-UTRAN the eNB should not send the CELL TRAFFIC TRACE message to the
MME.
\- For UTRAN the RNC should not send the UPLINK INFORMATION EXCHANGE REQUEST
message to the SGSN/MSC Server.
If the anonymization indicates that thIMEI-TACe is required:
\- For E-UTRAN eNB should send the CELL TRAFFIC TRACE message to the MME and
shall put immediate MDT or logged MDT in the privacy indicator IE according to
the job type parameter.. MME shall look up of the IMEI-TAC and send to the TCE
if the privacy indicator indicates logged MDT or Immediate MDT
\- For UTRAN the RNC shall send the UPLINK INFORMATION EXCHANGE REQUEST
message to the SGSN/MSC Server with IMSI information. SGSN/MSC Server shall
find the corresponding IMEI and send the IMEI-TAC to the TCE..
## 4.8 RCEF reporting
### 4.8.1 Trace session activation for RCEF reporting
RCEF reporting is activated to the eNB as a special Trace Session where the
job type indicates RCEF reporting only. The detailed procedure is shown in
figure 4.8.1.1 where a UE experiences an RCEF event and the RRC establishment
is successful to the same eNB.
Figure 4.8.1.1 Example scenario for RCEF reporting when UE RRC establishment
is successful to the same eNB.
When the eNB receives the Trace Session activation indicating RCEF reporting
only, the eNB shall start a Trace Session. This Trace Session shall collect
only RCEF reports received from the UE. The Trace Session activation message
received from the EMS shall contain the following information:
  * Trace Reference
  * Job type=RCEF reporting only
  * IP address of the TCE
Figure 4.8.1.2 shows another example where the UE RRC Establishment is failed
to one eNB, but successful to another eNB.
Figure 4.8.1.2 Example scenario for RCEF reporting when the UE RRC
establishment is successful to a different eNB
If the UE establishes the RRC connection successfully the RCEF reports are
fetched by the eNB. The procedures to be used at eNB to forward the RCEF
reports towards the management system are the same regardless of whether RCEF
occurred at this eNB or a different eNB.
If a UE detects a RRC Connection Establishment Failure event, it collects
certain information as described in TS 37.320[30]. Once the eNB retrieved the
RCEF report from the UE, as defined in TS 37.320[30], it shall save it to the
Trace Record. The Trace Record containing the RCEF reports can be transferred
to the TCE in the same mechanism as for normal subscriber and equipment trace
or for MDT.
### 4.8.2 Trace session deactivation for RCEF reporting
_When the eNB receives the indication from the EM for trace session
deactivation with the job type "RCEF reporting only", it shall deactivate the
trace session for the indicated trace reference of RCEF reporting and stop
RCEF reporting to the TCE._
# 5 Trace/UE measurement control and configuration parameters
## 5.1 Triggering events (M)
This mandatory parameter defines when to start a Trace Recording Session and
which message shall be recorded first, when to stop a Trace Recording Session
and which message shall be recorded last respectively. The messages in the
start triggering event tables indicate the transaction to be recorded first
and the starting time of the Trace Recording Session within a Trace Session
for the traced MS/subscriber in the given NE.
The messages in the stop triggering event tables indicate the transaction to
be recorded last and the stopping time of the Trace Recording Session.
* * *
MSC Server Start triggering events Stop triggering events Mobile Originated
Call Receipt of the CM SERVICE-REQUEST message with service type set to
originating call establishment Reception of CC-RELEASE COMPLETE or CM-SERVICE
ABORT message Mobile Terminated Call Sending of PAGING REQUEST message
Reception of CC-RELEASE COMPLETE or CM-SERVICE ABORT message Mobile Originated
SMS Receipt of the CM SERVICE-REQUEST message with service type set to Short
Message service Transmission of RP-ACK/RP-NACK message Mobile Terminated SMS
Sending of PAGING REQUEST message Reception of RP-ACK/RP-NACK message IMSI
Attach Receipt of the MM-LOCATION UPDATING REQUEST message Sending of MM-
LOCATION-UPDATING ACCEPT or MM-LOCATION-UPDATING-REJECT message Location
Update Receipt of the MM-LOCATION UPDATING REQUEST message Sending of MM-
LOCATION-UPDATING ACCEPT or MM-LOCATION-UPDATING-REJECT message IMSI Detach
Receipt of the MM-IMSI DETACH INDICATION message Reception of MM-IMSI DETACH
INDICATION message Handover Receipt of the BSSMAP-HANDOVER-REQUIRED message in
case of GSM or RANAP-RELOCATION-REQUIRED message in case of UMTS Reception of
BSSMAP-CLEAR COMPLETE message in case of GSM or RANAP-IU RELEASE COMPLETE
message in case of UMTS or BSSMAP-HANDOVER FAILURE in case of GSM or RANAP-
RELOCATION FAILURE in case of UMTS. Supplementary Service TBD TBD
* * *
* * *
MGW Start triggering events Stop triggering events Context Reception of
H.248-ADD command, or reception of H.248 MODIFY command Sending of H.248-
SUBTRACT reply
* * *
* * *
SGSN Start triggering events Stop triggering events PDP Context Reception of
SM-ACTIVATE PDP CONTEXT REQUEST or sending SM-REQUEST PDP CONTEXT ACTIVATION
or reception of SM- MODIFY PDP CONTEXT REQUEST Reception or sending of SM-
DEACTIVATE PDP CONTEXT REQUEST or sending SM-ACTIVATE PDP CONTEXT REJECT
Mobile Originated SMS Receipt of RP-DATA message Transmission of RP-ACK/RP-
NACK message Mobile Terminated SMS Transmission of RP-DATA message Reception
of RP-ACK/RP-NACK message GPRS Attach Reception of MM-ATTACH-REQUEST Sending
MM-ATTACH-ACCEPT or MM-ATTACH-REJECT Routing Area Update Reception of MM-
ROUTING AREA UPDATE REQUEST Sending MM-ROUTING AREA UPDATE ACCEPT or MM-
ROUTING AREA UPDATE REJECT GPRS Detach Reception MM-DETACH REQUEST Reception
of MM-DETACH ACCEPT MBMS Context Sending SM-Request MBMS Context Activation or
reception of SM-Update MBMS Context Request Sending of SM-Deactivate MBMS
Context Request or sending of SM-Activate MBMS Context Reject
* * *
* * *
GGSN Start triggering events Stop triggering events PDP Context Reception of
GTP Create PDP context request or reception of GTP Update PDP context request
Sending of GTP Delete PDP context response MBMS Context Reception of GTP
Create MBMS Context Request or reception of GTP Update MBMS Context Request
Sending of GTP Delete MBMS Context Response
* * *
* * *
IMS Network Element Start triggering events Stop triggering events SIP session
or standalone transaction Reception of an initial SIP request that matches the
start trigger event configured by the Management System via the Trace IRP TS
32.442 [24] Sending of a SIP final response to a SIP BYE or other request
(originating or terminating), timer expiry or other event that matches the
stop trigger event configured by the Management System via the Trace IRP TS
32.442 [24].
* * *
* * *
BM-SC Start triggering events Stop triggering events MBMS Multicast service
activation Reception of MBMS Authorization Request Reception of Deactivation
Indication for user deactivation or sending of Session Stop Request for
service deactivation
* * *
+----------------------+----------------------+----------------------+ | MME | Start triggering | Stop triggering | | | events | events | +----------------------+----------------------+----------------------+ | Service request | Reception of NAS: | Reception of S11: | | | Service Request | Modify Bearer | | | message or S11: | Response or sending | | | Downlink Data | of NAS: SERVICE | | | Notification | REJECT | | | | | | | Note: The Service | Note: Modify Bearer | | | Request message | Response shall stop | | | shall not start a | the Trace Recording | | | new Trace Recording | Session only if it | | | Session when | has been sent as | | | received after a | part of the Service | | | Downlink Data | Request procedure | | | Notification for the | | | | same service request | | | | instance. | | +----------------------+----------------------+----------------------+ | UE initiated PDN | Reception of NAS: | Reception of NAS PDN | | connectivity | PDN connectivity | Connectivity | | | Request message | Complete | +----------------------+----------------------+----------------------+ | Initial Attach, | Initial Attach: | Initial Attach: | | Tracking area | Reception of the | Reception of the | | update, Detach | NAS: ATTACH REQUEST | NAS: ATTACH COMPLETE | | | or of S6a Update | or sending of the | | | Location Answer | NAS: ATTACH REJECT | | | | | | | Tracking Area | Tracking Area | | | Update: Reception of | Update: Sending of | | | the NAS: TRACKING | the NAS: TRACKING | | | AREA UPDATE REQUEST | AREA UPDATE ACCEPT | | | | or sending of NAS: | | | Detach: Reception of | TRACKING AREA UPDATE | | | the NAS: DETACH | REJECT | | | REQUEST or S3 Detach | | | | Notification or S6a | Detach: Sending of | | | Cancel Location | NAS: DETACH ACCEPT | | | Request or sending | or S3 Detach | | | of S11 Delete | Acknowledgement | | | Session Request. | message or S6a | | | | Cancel Location | | | Note: Cancel | Answer message or | | | location location | reception S11 Delete | | | shall not trigger | Session Response | | | new Trace Recording | | | | Session if it is | Note: Cancel | | | sent as part of the | Location Answer | | | tracking area update | shall not stop a | | | procedure. | Trace Recording | | | | Session if it is | | | Note: The Delete | sent as part of the | | | Session Request | TAU procedure. | | | message shall | | | | trigger a new Trace | Note: The Delete | | | Recording Session | Session Response | | | only if sent as part | message shall stop a | | | of a Detach | Trace Recording | | | procedure and only | Session only if sent | | | if a Detach Request | as part of a Detach | | | has not been | procedure and only | | | received for the | if a Detach Request | | | same instance of the | has not been | | | procedure. | received for the | | | | same instance of the | | | Note: Update | procedure. | | | Location Answer | | | | shall be a start | | | | trigger for a Trace | | | | Recording Session | | | | only if sent as part | | | | of Attach procedure | | | | and if containing | | | | Trace Data. | | +----------------------+----------------------+----------------------+ | UE initiated PDN | Sending of the S11: | Reception of NAS | | disconnection | Delete Session | Deactivate EPS | | | Request | Bearer Context | | | | Accept | | | Note: The S11 Delete | | | | Session Request | | | | message shall | | | | trigger a new Trace | | | | Recording Session | | | | only if it is sent | | | | as part of the UE | | | | initiated PDN | | | | disconnection | | | | procedure. | | +----------------------+----------------------+----------------------+ | Bearer | Bearer Activation: | Bearer Activation: | | Activation/Modif | Reception of S11: | Sending of S11: | | ication/Deactivation | Create Bearer | Create Bearer | | | Request | Response | | | | | | | Bearer Modification: | Bearer Modification: | | | Reception of S11: | Sending of S11: | | | Update Bearer | Update Bearer | | | Request | Response | | | | | | | Bearer Deactivation: | Bearer Deactivation: | | | Reception of S11 | Sending of S11: | | | Delete Bearer | Delete Bearer | | | Request | Response | | | | | | | Note: Create Bearer | | | | Request shall not | | | | trigger a new trace | | | | recording session if | | | | it is sent due to | | | | Dedicated bearer | | | | activation in | | | | combination with the | | | | default bearer | | | | activation at Attach | | | | and UE requested PDN | | | | connectivity | | | | procedures | | +----------------------+----------------------+----------------------+ | Handover | Inter-eNB/Intra-MME: | Inter-eNB/Intra-MME: | | | Reception of S1AP: | Sending of S1AP: | | | Path Switch Request | Path Switch Request | | | or S1AP Handover | Acknowledge or S1AP: | | | Required | Path Switch Request | | | | Failure, or S1AP: | | | Inter-eNB/Inter-MME | Handover Preparation | | | - Inter RAT (source | Failure or S1AP: | | | MME): Reception of | Handover Cancel | | | S1AP: Handover | Acknowledge or | | | Required | receiving Handover | | | | Notify | | | Inter-eNB/Inter-MME | | | | -- Inter RAT (target | Inter eNB - Inter | | | MME): Reception of | MME / Inter RAT | | | S10/S3: Forward | (source MME): | | | Relocation Request | Reception of S10/S3 | | | | Forward Relocation | | | | Complete | | | | Notification or | | | | sending of S1AP | | | | Handover Cancel | | | | Acknowledge or S1AP | | | | Handover Preparation | | | | Failure | | | | | | | | Inter eNB - Inter | | | | MME /Inter RAT | | | | (target MME): | | | | Sending of S10/S3 | | | | Forward Relocation | | | | Complete | | | | Notification or of | | | | S10/S3 Relocation | | | | Cancel Response or | | | | of S10/S3 Forward | | | | Relocation Response | | | | with reject cause | | | | value | +----------------------+----------------------+----------------------+
+----------------------+----------------------+----------------------+ | SGW | Start triggering | Stop triggering | | | events | events | +----------------------+----------------------+----------------------+ | PDN connection | Reception of the | Sending of the S11: | | creation | S11: Create Session | Create Session | | | Request | Response | +----------------------+----------------------+----------------------+ | PDN connection | Reception of the | Sending of the S11: | | termination | S11: Delete Session | Delete Session | | | Request | Response | +----------------------+----------------------+----------------------+ | Bearer | Bearer Activation: | Bearer Activation: | | Activation/Modif | Reception of the S5: | Sending of the S5: | | ication/Deactivation | Create Bearer | Create Bearer | | | Request or S11: | Response | | | Bearer Resource | | | | Command | Bearer Modification: | | | | Sending of the S11: | | | Bearer Modification: | Modify Bearer | | | Reception of the | Response or S5: | | | S11: Modify Bearer | Update Bearer | | | Request or S5: | Response | | | Update Bearer | | | | Request | Bearer Deletion: | | | | Sending of S5: | | | Bearer Deletion: | Delete Bearer | | | Reception of the | Response | | | S11: Deactivate | | | | Bearer Command or | | | | S5: Delete Bearer | | | | Request | | +----------------------+----------------------+----------------------+
+----------------------+----------------------+----------------------+ | PGW | Start triggering | Stop triggering | | | events | events | +----------------------+----------------------+----------------------+ | PDN connection | Reception of S5: | Sending of S5: | | creation | Create Session | Create Session | | | Request (GTP) or | Response (GTP) or | | | Proxy Binding Update | Proxy Binding Update | | | (PMIP) | Ack (PMIP) | | | | | | | Reception of S2b: | Sending of S2b: | | | Create Session | Create Session | | | Request (GTP) | Response (GTP) | +----------------------+----------------------+----------------------+ | PDN connection | Reception of the S5: | Sending of the S5: | | termination | Delete Session | Delete Session | | | Request or Proxy | Response (GTP) or | | | Binding Update | Proxy Binding Update | | | | ACK (PMIP) | | | Reception of the | | | | S2b: Delete Session | Sending of the S2b: | | | Request | Delete Session | | | | Response (GTP) | +----------------------+----------------------+----------------------+ | Bearer | Bearer Activation: | Bearer Activation: | | Activation/Modif | Sending of the | Reception of the | | ication/Deactivation | S5/S2b: Create | S5/S2b: Create | | | Bearer Request | Bearer Response | | Note: this is | | | | applicable only to | Bearer Modification: | Bearer Modification: | | GTP based S5 | Reception of the S5: | Sending of the S5: | | interface. | Modify Bearer | Modify Bearer | | | Request or sending | Response or | | | of the S5/S2b: | reception of the | | | Update Bearer | S5/S2b: Update | | | Request | Bearer Response | | | | | | | Bearer Deletion: | Bearer Deletion: | | | Reception of the S5: | Reception of the | | | Delete Bearer | S5/S2b: Delete | | | Command or sending | Bearer Response | | | of S5/S2b: Delete | | | | Bearer Request | | +----------------------+----------------------+----------------------+
* * *
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 MSC Server
MGW  
SGSN
GGSN  
BM-SC  
MME  
PGW SGW
* * *
* * *
MSC Server  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 spare spare SS Handovers LU,
IMSI attach, IMSI detach MO and MT SMS MO and MT calls  
spare
* * *
* * *
MGW  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 spare spare Context
* * *
* * *
SGSN  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 spare MBMS Context RAU, GPRS
attach, GPRS detach MO and MT SMS PDP context  
Reserved
* * *
* * *
GGSN  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 spare MBMS Context PDP Context
* * *
+-------+-------+-------+-------+-------+-------+-------+-------+ | MME | | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+ | Bit 8 | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | +-------+-------+-------+-------+-------+-------+-------+-------+ | spare | Spare | Han | B | UE | In | Se | UE | | | | dover | earer | init | itial | rvice | init | | | | | | iated | At | req | iated | | | | | Activ | PDN | tach, | uests | PDN | | | | | ation | dis | Tra | | co | | | | | | conne | cking | | nnect | | | | | Mo | ction | area | | ivity | | | | | dific | | up | | re | | | | | ation | | date, | | quest | | | | | | | D | | | | | | | Del | | etach | | | | | | | etion | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+
+-------+-------+-------+-------+-------+-------+-------+-------+ | PGW | SGW | | | | | | | +-------+-------+-------+-------+-------+-------+-------+-------+ | Bit 8 | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | +-------+-------+-------+-------+-------+-------+-------+-------+ | spare | B | PDN | PDN | Spare | B | PDN | PDN | | | earer | conne | conne | | earer | conne | Conne | | | | ction | ction | | | ction | ction | | | Activ | t | cre | | Activ | t | cre | | | ation | ermin | ation | | ation | ermin | ation | | | | ation | | | | ation | | | | Mo | | | | Mo | | | | | dific | | | | dific | | | | | ation | | | | ation | | | | | | | | | | | | | | Del | | | | Del | | | | | etion | | | | etion | | | +-------+-------+-------+-------+-------+-------+-------+-------+
If a bit is set to 1 the given event shall be traced, i.e. a Trace Recording
Session shall be started for that event.
If a bit is set to 0 the given event should not be traced, i.e. Trace
Recording Session should not be started.
## 5.2 void
## 5.3 Trace Depth (M)
This mandatory parameter defines how detailed information should be recorded
in the Network Element. The Trace Depth is a paremeter for Trace Session
level, i.e., the Trace Depth is the same for all of the NEs to be traced in
the same Trace Session.
The following table describes the values of the Trace Depth parameter.
* * *
Trace Depth Meaning Minimum Recording of some IEs in the signalling messages
plus any vendor specific extensions to this definition, in decoded format.
Medium Recording of some IEs in the signalling messages together with the
radio measurement IEs plus any vendor specific extensions to this definition,
in decoded format. Maximum Recording entire signalling messages plus any
vendor specific extensions to this definition, in encoded format.
MinimumWithoutVendorSpecificExtension Recording of some IEs in the signalling
messages in decoded format. MediumWithoutVendorSpecificExtension Recording of
some IEs in the signalling messages together with the radio measurement IEs in
decoded format. MaximumWithoutVendorSpecifcExtension Recording entire
signalling messages in encoded format.
* * *
At least one of Minimum, Medium or Maximum trace Depth shall be supported
depending on the NE type (see trace record description in TS 32.423 [3] for
details).
_Trace depth shall be an enumerated parameter with the following possible
values:_
0 --Minimum,
1 -- Medium
2 -- Maximum
3 -- MinimumWithoutVendorSpecificExtension
4 -- MediumWithoutVendorSpecificExtension
5 - MaximumWithoutVendorSpecificExtension
## 5.4 List of NE types (M)
This conditional mandatory parameter defines the Network Element types where
Trace Session activation is needed. The condition of this parameter is that
signalling based activation mechanism is used except in IMS. This parameter
determines whether the Trace Session Activation shall be propagated further to
other Network Elements. In the management based activation mechanism, and in
the signalling based activation mechanism for IMS, this parameter is not
needed.
The following list contains the Network Element types:
\- MSC Server
\- MGW
\- RNC
\- SGSN
\- GGSN
\- BM-SC
\- MME
\- SGW
\- PDN GW
\- eNB
* * *
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 SGW MME BM-SC RNC GGSN SGSN
MGW MSC-S spare eNB PDN GW
* * *
If a bit is set to 1, Trace Session to that Network Element shall be
activated.
If a bit is set to 0, Trace Session is not needed in that Network Element.
## 5.5 List of interfaces (O)
This is an optional parameter, which defines the interfaces to be recorded in
the Network Element.
The following list contains the list of interfaces in each Network Element:
\- MSC Server: A, Iu-CS, Mc and MAP (G, B, E, F, D, C) interfaces, CAP.
\- MGW: Mc, Nb-UP, Iu-UP.
\- RNC: Iu-CS, Iu-PS, Iur, Iub and Uu interfaces.
\- SGSN: Gb, Iu-PS, Gn, MAP (Gr, Gd, Gf), CAP (Ge), Gs, S6d, S4, S3, S13\'
interfaces.
\- GGSN: Gn, Gi and Gmb interfaces.
\- S-CSCF: Mw, Mg, Mr and Mi interfaces.
\- P-CSCF: Gm and Mw interfaces.
\- I-CSCF: Cx, Dx, Mg, Mw.
\- MRFC: Mp, Mr.
\- MGCF: Mg, Mj, Mn.
\- IBCF: Ix, Mx.
\- E-CSCF: Mw, Ml, Mm, Mi/Mg.
\- BGCF: Mi, Mj, Mk.
\- AS: Dh, Sh, ISC, Ut.
\- HSS: MAP (C, D, Gc, Gr), Cx, S6d interfaces, S6a, Sh and location and
subscription information.
\- EIR: MAP (F), S13, S13', MAP (Gf)
\- BM-SC: Gmb interface.
\- MME: S1-MME, S3, S6a, S10, S11, S13
\- SGW: S4, S5, S8, S11, Gxc
\- PDN GW: S2a, S2b, S2c, S5, S6b, Gx, S8, SGi
\- eNB: S1-MME, X2, Uu
NOTE: For IMS Network Elements other than P-CSCF and S-CSCF the interfaces
included in the Trace Job for a particular type of IMS session are configured
in the Management System via the Trace IRP (3GPP TS 32.442 [24]).
* * *
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 MSC Server
MGW  
SGSN
GGSN  
RNC  
BM-SC  
MME  
SGW  
PDN GW  
eNB  
HSS  
EIR
* * *
* * *
MSC Server  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 CAP MAP-F MAP-E MAP-B MAP-G Mc
Iu A spare MAP-C MAP-D
* * *
* * *
SGSN  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Ge Gs MAP-Gf MAP-Gd MAP-Gr Gn
Iu Gb spare S13\' S3 S4 S6d
* * *
* * *
MGW  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Spare Iu-UP Nb-UP Mc
* * *
* * *
GGSN  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 spare Gmb Gi Gn
* * *
* * *
RNC  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Spare Uu Iub Iur Iu
* * *
* * *
BM-SC  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 spare Gmb
* * *
* * *
MME  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Spare S13 S11 S10 S6a S3
S1-MME
* * *
* * *
SGW  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Spare Gxc S11 S8b S5 S4
* * *
* * *
PDN GW  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 SGi S8b Gx S6b S5 S2c S2b S2a
* * *
* * *
eNB  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Spare Uu X2 S1-MME
* * *
* * *
HSS  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Sh S6a S6d Cx MAP-Gr MAP-Gc
MAP-D MAP-C
* * *
* * *
EIR  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Spare MAP-Gf S13' S13 MAP-F
* * *
If a bit is set to 1, the interface should be traced in the given Network
Element.
If a bit is set to 0, that interface should not be traced in the given Network
Element.
NOTE: The bit significance of the bitmaps defined above for the OAM interface
can be different from the bit significance of the corresponding bitmaps in the
signalling interface specifications.
## 5.6 Trace Reference (M)
The Trace Reference parameter shall be globally unique, therefore the Trace
Reference shall compose as follows:
MCC+MNC+Trace ID, where the MCC and MNC are coming with the Trace activation
request from the EM/NM to identify one PLMN containing the EM/NM, and Trace ID
is a 3 byte Octet String.
NOTE 1: Trace ID referred here is the same as Trace reference in previous
releases.
NOTE 2: The MCC+MNC being part of the Trace Reference from Rel-8 onwards (e.g.
ignored by Rel-6 / Rel-7 UTRAN Network Elements), the uniqueness of the Trace
Reference may not be guaranteed with Rel-6 / Rel-7 Network Element(s) involved
in the Trace.
## 5.7 Trace Recording Session Reference (M)
This parameter shall be a 2 byte Octet String.
## 5.8 Void
## 5.9 IP Address of Trace Collection Entity (CM,CO)
This is a parameter which defines the IP address to which the Trace records
shall be transferred. IPv4 and/or IPv6 address(es) may be signalled.
This parameter is mandatory when tracing in EPS is supported.
This parameter is mandatory when MDT is supported.
This parameter is optional when tracing in UMTS is supported.
## 5.9a Job type (CM)
The Job type is a conditional mandatory parameter. The condition is either MDT
or RLF or RCEF data collection functionality is supported. It defines if a
single trace job, a combined MDT and trace job or RLF report collection job or
RCEF report collection job is activated. This parameter also defines the MDT
mode. The Job type parameter is an enumerated type with the following values:
\- Immediate MDT only (0);
\- Logged MDT only (1);
\- Trace only (2);
\- Immediate MDT and Trace (3);
\- RLF reports only (4) ;
\- RCEF reports only (5).
NOTE: The Job type "RLF reports only" and "RCEF reports only" are applicable
only in management based trace activation in E-UTRAN.
## 5.9b PLMN Target (CM)
This parameter defines the PLMN for which sessions shall be selected in the
Trace Session in case of management based activation when several PLMNs are
supported in the RAN (this means that shared cells and not shared cells are
allowed for the specified PLMN. Furthermore, several PLMNs can be used for not
shared RAN cases as well as for shared RAN cases.). Only the sessions may be
selected where the PLMN that the UE reports as selected PLMN is the same as
the PLMN Target.
Note that the PLMN Target might differ from the PLMN specified in the Trace
Reference, as that specifies the PLMN that is containing the EM/NM requesting
the Trace Session from the NE.
## 5.10 MDT specific configuration parameters (CM)
### 5.10.1 Void
### 5.10.2 Area Scope
The Area Scope optional parameter defines the area in terms or Cells or
Tracking Area/Routing Area/Location Area where the MDT data collection shall
take place. The area scope specified in a MDT session shall support the PLMN s
of the MDT PLMN list (defined in clause 5.10.24). If the parameter is not
present the MDT data collection shall be done throughout the PLMNs of the MDT
PLMN list For further details see also TS 37.320 [30]..
The Area Scope parameter in UMTS is either
\- list of Cells, identified by CGI. Maximum 32 CGI can be defined.
\- List of Routing Area, identified by RAI. Maximum of 8 RAIs can be defined.
\- List of Location Area, identified by LAI. Maximum of 8 LAIs can de defined.
The Area Scope parameter in LTE is either
\- list of Cells, identified by E-UTRAN-CGI. Maximum 32 CGI can be defined.
\- List of Tracking Area, identified by TAC with associated plmn-Identity-
perTAC-List containing the PLMN identity for each TAC. Maximum of 8 TAC can be
defined. For further details see also TS 36.331 [32].
### 5.10.3 List of measurements
This parameter is mandatory if the Job type is configured for Immediate MDT or
combined Immediate MDT and Trace. This parameter defines the measurements that
shall be collected. For further details see also TS 37.320 [30]. The parameter
is 4 octet long bitmap with the following values in UMTS:
  * M1: CPICH RSCP and CPICH Ec/No measurement by UE with Periodic or event 1F as reporting triggers.
  * M2: For 1.28 Mcps TDD, P-CCPCH RSCP and Timeslot ISCP measurement by UE with event 1I as reporting triggers.
  * M3: SIR and SIR error (FDD) by NodeB
  * M4: UE power headroom (UPH) by the UE, applicable for E-DCH transport channels.
  * M5: Received total wideband power (RTWP) by Node B
  * M6: Data Volume measurement, separately for DL and UL, by RNC.
  * M7: Throughput measurement, separately for DL and UL, per RAB and per UE, by RNC.
  * Any combination of the above
  * 
The parameter can have the following values in LTE:
  * M1: RSRP and RSRQ measurement by UE with Periodic, event A2 as reporting triggers
  * M2: Power Headroom (PH) measurement by UE\ NOTE: Available from MAC layer
  * M3: Received Interference Power measurement by eNB
  * M4: Data Volume measurement separately for DL and UL by eNB
  * M5: Scheduled IP Throughput measurement separately for DL and UL by eNB
  * And any combination of above
* * *
LTE  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 spare M5 for UL M5 for DL M4
for UL M4 for DL M3 M2 M1 spare  
UMTS  
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 M7 for DL M6 for UL M6 for DL
M5 M4 M3 M2 M1 spare M7 for UL
* * *
### 5.10.4 Reporting Trigger
This parameter is mandatory if the list of measurements parameter is
configured for UE side measurement (such as M1 measurement in LTE and M1/M2
measurement in UMTS) and the jobtype is configured for Immediate MDT or
combined Immediate MDT and Trace.
The parameter shall not have the combination of periodical, event based and
event based periodic reporting at the same time, i.e. :
  * For LTE, only one of the bits 1, 2, and 5 can be set.
  * For UMTS, bit 1 cannot be set at the same time with either bit 3 or bit 4.
The parameter is one octet long bitmap and can have the following values
(detailed definition of the parameter is in 3GPP TS 37.320 [30]):
  * Periodical,
  * Event A2 for LTE:
  * Event 1F for UMTS,
  * Event 1I for UMTS 1.28 Mcps TDD,
  * A2 event triggered periodic for LTE.
  * All configured RRM event triggers for M1 measurement. S ee also TS 37.320 section 5.2.1.1 [30]
* * *
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Reserved All configured RRM
event triggers for UMTS All configured RRM event triggers for LTE A2 event
triggered periodic for LTE Event 1I for UMTS 1.28 MCPS TDD Event 1F for UMTS
Event A2 for LTE Periodical
* * *
### 5.10.5 Report Interval
This parameter is mandatory if the Reporting trigger is configured for
Periodic UE side measurements a(such as M1 measurement in LTE and M1/M2
measurements in UMTS)nd the jobtype is configured for Immediate MDT or
combined Immediate MDT and Trace. The parameter indicates the interval between
the periodical measurements to be taken when UE is in connected.
The parameter is enumerated type with the following values in milliseconds in
case of UMTS (detailed definition is in 3GPP TS 25.331 [31]:
  * 250 ms (0),
  * 500 ms (1),
  * 1000 ms (2),
  * 2000 ms (3),
  * 3000 ms (4),
  * 4000 ms (5),
  * 6000 ms (6),
  * 8000 ms (7),
  * 12000 ms (8),
  * 16000 ms (9),
  * 20000 ms (10),
  * 24000 ms (11),
  * 28000 ms (12),
  * 32000 ms (13),
  * 64000 ms (14)
The parameter can have the following values in LTE (detailed definition is in
3GPP TS 36.331 [32]):
  * 120 ms (15),
  * 240 ms (16),
  * 480 ms (17),
  * 640 ms (18),
  * 1024 ms (19),
  * 2048 ms (20),
  * 5120 ms (21),
  * 10240ms (22),
  * 1 min=60000 ms (23),
  * 6 min=360000 ms (24),
  * 12 min=720000 ms (25),
  * 30 min=1800000 ms (26),
  * 60 min=3600000 ms (27)
### 5.10.6 Report Amount
The parameter is mandatory if the reporting trigger is configured for
periodical UE side measurement (such as M1 measurement in LTE and M1/M2
measurements in UMTS) and the jobtype is configured for Immediate MDT or
combined Immediate MDT and Trace. The parameter defines the number of
measurement reports that shall be taken for periodical reporting while UE is
in connected. Detailed definition of the paremeter is in 3GPP TS 36.331 and
3GPP TS 25.331[31].
The parameter is an enumerated type with the following values in UMTS and in
LTE:
  * _1 (0),_
  * _2 (1),_
  * _4 (2),_
  * _8 (3),_
  * _16 (4),_
  * _32 (5),_
  * _64 (6),_
  * _infinity (7)_
### 5.10.7 Event Threshold for RSRP
The parameter is mandatory if the report trigger parameter is configured for
A2 event reporting or A2 event triggered periodic reporting and the job type
parameter is configured for Immediate MDT or combined Immediate MDT and Trace.
Detailed definition of the parameter is in 3GPP TS 36.331 [32].
  * The parameter is an Integer number between 0-97.
### 5.10.7a Event Threshold for RSRQ
The parameter is mandatory if the report trigger parameter is configured for
A2 event reporting or A2 event triggered periodic reporting and the job type
parameter is configured for Immediate MDT or combined Immediate MDT and Trace.
Detailed definition of the parameter is in 3GPP TS 36.331 [32].
The parameter is an Integer number between 0-34.
### 5.10.8 Logging Interval
The parameter is mandatory if the job type is configured for Logged MDT. The
parameter defines the periodicity for logging MDT measurement results for
periodic downlink pilot strength measurement when UE is in Idle.
Detailed definition of the parameter is in 3GPP TS 37.320 [30].
The parameter is an enumerated type with the following values in UMTS and LTE
as per defined in 3GPP TS 25.331 [31] and 36.331 [32]:
  * 1.28 (0),
  * 2.56 (1),
  * 5.12 (2),
  * 10.24 (3),
  * 20.48 (4),
  * 30.72 (5),
  * 40.96 (6),
  * 61.44 (7)
### 5.10.9 Logging Duration
The parameter is mandatory if the the job type parameter is configured for
Logged MDT. The parameter determines the validity of MDT logged configuration
for IDLE. The timer starts at time of receiving configuration by the UE, and
continues independent of UE state transitions and RAT or RPLMN changes.
Detailed definition of the parameter is in 3GPP TS 37.320 [30], 3GPP TS 25.331
[31] and 3GPP TS 36.331 [32]:
The parameter is an enumerated type with the following values in UMTS and LTE:
  * 600 sec (0),
  * 1200 sec (1),
  * 2400 sec (2),
  * 3600 sec (3),
  * 5400 sec (4),
  * 7200 sec (5)
### 5.10.10 Void
### 5.10.11 Trace Collection Entity Id
This is a mandatory parameter for Logged MDT which defines the TCE Id which is
sent to the UE. The UE returns it to the network together with the logged
data. The network has a configured mapping of the IP address of the TCE (to
which the Trace records shall be transferred) and the TCE Id. The mapping
needs to be unique within the PLMN. The size of the parameter is one byte.
### 5.10.12 Anonymization of MDT data
This is a mandatory parameter for area based MDT when Job Type is
\- Immediate MDT only (0);
\- Logged MDT only (1);
\- Immediate MDT and Trace (3).
This configuration parameter provides anonymization of MDT data (Refer to
clause 4. 4).
The _parameter is an enumerated type with the following possible values:_
  * _No Identity (0);_
  * IMEI-TAC _(1)_
### 5.10.13 Event Threshold for Event 1F
The parameter is mandatory if the reporting trigger parameter is configured
for 1F event reporting and the job type parameter is configured for Immediate
MDT or combined Trace and Immediate MDT.
The parameter defines the threshold for reporting UMTS M1 measurements for 1F
event based reporting trigger Detailed definition of the parameter is in 3GPP
TS 25.331 section 14.1.2.6 [31].
  * The parameter is an Integer number between -120-165
The range used depends on the measurement:
  * CPICH RSCP the range is: -120 -- 25 dBm
  * For CPICH Ec/No the range is -24 - 0 dB
  * For Pathloss 30-165 dB.
### 5.10.14 Event threshold for Event 1I
The parameter is mandatory if the reporting trigger parameter is configured
for 1l event reporting and the job type parameter is configured for Immediate
MDT or combined Trace and Immediate MDT.
The parameter defines the threshold for reporting UMTS M2 measurements for 1I
event based reporting trigger. Detailed definition of the parameter is in 3GPP
TS 25.331 section 14.1.3.3. [31].
  * The parameter is an Integer number between -120 .. -25
### 5.10.15 Measurement quantity
The parameter is mandatory if the reporting trigger parameter is configured
for 1F reporting and the job type parameter is configured for Immediate MDT or
combined Trace and Immediate MDT.
The parameter describes for what M1 measurements the Event Threshold 1F
parameter is applicable.
The parameter is a bitmap with the following values:
* * *
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Reserved Reserved Reserved
Reserved Reserved Pathloss CPICH RSCP CPICH Ec/N0
* * *
No more than one bit shall be selected at a time.
### 5.10.16 void
### 5.10.17 void
### 5.10.18 void
### 5.10.19 Positioning Method
This parameter is optional and is used only if the job type is set to
Immediate MDT or Immediate MDT and Trace.
This parameter defines what positioning method should be used for the MDT job.
The parameter is a bitmap, each bit represents a positioning method. The
parameter is applicable only for LTE. The bit1 (GNSS) may be selected only if
the M1 measurement is selected in the "List of measurements" parameter
(defined in Section 5.10.3).
If the positioning method parameter indicates both E-Cell ID and GNSS
positioning, the eNB may use E-Cell ID measurement collection only if the UE
does not provide GNSS based location information.
* * *
Bit 8 Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Spare E-Cell ID GNSS
* * *
If the parameter is not present, then best effort positioning method is used
(i.e. in worst scenario only cell ID).
### 5.10.20 Collection period for RRM measurements LTE
This parameter is mandatory if the job type is set to Immediate MDT or
Immediate MDT and Trace and the bits 3 (M3) of the list of measurements
parameter (defined in Section 5.10.3) in LTE is set to 1. The parameter is
used only in case of RAN side measurements whose configuration is determined
by RRM.
This measurement parameter defines the collection period that should be used
to collect available measurement samples in case of RRM configured
measurements. The same collection period should be used for all such
measurements that are requested in the same MDT or combined Trace and MDT job.
The parameter is an enumerated type with the following values (detailed
definition is in 3GPP TS 36.413 [36]):
\- 100 ms (0)
\- 1000 ms (1)
\- 1024 ms (2),
\- 1280 ms (3),
\- 2048 ms (4),
\- 2560 ms (5),
\- 5120 ms (6),
\- 10000 ms (7)
\- 10240 ms (8),
\- 1 min (9).
Some values may not be always available e.g., due to the large amount of
logging they would generate in a highly loaded network. The selection of a
specific subset of supported values at the eNB is vendor-specific.
### 5.10.21 Collection period for RRM measurements UMTS
This parameter is mandatory if the job type is set to Immediate MDT or
Immediate MDT and Trace and any of the bits 3 (M3), 4 (M4), 5 (M5) of the list
of measurements parameter (defined in Section 5.10.3) in UMTS is set to 1. The
parameter is used only in case of RAN side measurements whose configuration is
determined by RRM.
This measurement parameter defines the collection period that should be used
to collect available measurement samples in case of RRM configured
measurements. The same collection period should be used for all such
measurements that are requested in the same MDT or combined Trace and MDT job.
The parameter is an enumerated type with the following values:
  * 250 ms (0)
  * 500 ms (1)
  * 1000 ms (2),
  * 2000 ms (3),
  * 3000 ms (4),
  * 4000 ms (5),
  * 6000 ms (6),
  * 8000 ms (7),
  * 12000 ms (8),
  * 16000 ms (9),
  * 20000 ms (10),
  * 24000 ms (11),
  * 28000 ms (12),
  * 32000 ms (13),
  * 64000 ms (14)
Some values may not be always available e.g., due to the large amount of
logging they would generate in a highly loaded network. The selection of a
specific subset of supported values at the RNC is vendor-specific.
### 5.10.22 Measurement period UMTS
This parameter is mandatory if the job type is set to Immediate MDT or
Immediate MDT and Trace and either the bit 6 or bit 7 or bit 8 or bit 9 of
list of measurements parameter in UMTS (M6 for DL or M6 for UL or M7 for DL or
M7 for UL) is set to 1.
This measurement parameter defines the measuremet period that should be used
for the Data Volume and Throughput measurements made by the RNC. The same
measurement period should be used for the UL and DL.
The parameter is an enumerated type with the following values (the values
250ms (0) and 500ms (1) are not valid for this parameter):
  * 250 ms (0),
  * 500 ms (1),
  * 1000 ms (2),
  * 2000 ms (3),
  * 3000 ms (4),
  * 4000 ms (5),
  * 6000 ms (6),
  * 8000 ms (7),
  * 12000 ms (8),
  * 16000 ms (9),
  * 20000 ms (10),
  * 24000 ms (11),
  * 28000 ms (12),
  * 32000 ms (13),
  * 64000 ms (14).
Some values may not be always available e.g., due to the large amount of
logging they would generate in a highly loaded network. The selection of a
specific subset of supported values at the RNC is vendor-specific.
### 5.10.23 Measurement period LTE
This parameter is mandatory if the job type is set to Immediate MDT or
Immediate MDT and Trace and either the bit 4 or bit 5 or bit 6 or bit7 of list
of measurements parameter in LTE (M4 for DL or M4 for UL or M5 for DL or M5
for UL) is set to 1.
This measurement parameter defines the measuremet period that should be used
for the Data Volume and Scheduled IP Throughput measurements made by the eNB.
The same measurement period should be used for the UL and DL.
The parameter is an enumerated type with the following values:
  * 1024 ms (0),
  * 1280 ms (1),
  * 2048 ms (2),
  * 2560 ms (3),
  * 5120 ms (4),
  * 10240 ms (5)
  * 1 min (6).
Some values may not be always available e.g., due to the large amount of
logging they would generate in a highly loaded network. The selection of a
specific subset of supported values at the eNB is vendor-specific.
### 5.10.24 MDT PLMN List
This is an optional parameter indicating the PLMNs where measurement
collection, status indication and log reporting is allowed. E.g. the UE
performs these actions for Logged MDT when the RPLMN is part of this set of
PLMNs. Maximum of 16 PLMNs can be defined.
To the UE it is communicated as the plmn-IdentityList. Between the NEs it is
communicated either as the Management Based MDT PLMN List or as the Signalling
Based MDT PLMN List, depending on how the MDT was activated. For further
details see also TS 37.320 [30], TS 36.331 [32] and TS 36.413 [36].
### 5.10.25 Collection period M4, M5 in LTE
This parameter is mandatory if the job type is set to Immediate MDT or
Immediate MDT and Trace and any of bits 4 (M4) or 5 (M5) of list of
measurements parameter (defined in clause 5.10.3) in LTE is set to 1.
This measurement parameter defines the collection period that should be used
to collect available measurement samples in case of data volume measurement
and scheduled IP throughput measurements. The same collection period should be
used for all such measurements that are requested in the same MDT or combined
Trace and MDT job.
The parameter is an enumerated type with the following values (detailed
definition is in 3GPP TS 36.413 [36]):
\- 1024 ms (0),
\- 2048 ms (1),
\- 5120 ms (2),
\- 10240 ms (3),
\- 1 min (4)
Some values may not be always available e.g., due to the large amount of
logging they would generate in a highly loaded network. The selection of a
specific subset of supported values at the eNB is vendor-specific.
### 5.10.26 Collection period M6 in LTE
This parameter is mandatory if the job type is set to Immediate MDT or
Immediate MDT and Trace and either the bit 7 of list of measurements parameter
(defined in Section 5.10.3) in LTE (M6 for DL or M6 for UL) is set to 1.
This measurement parameter defines the collection period that should be used
for packet delay measurement made by the eNB. The same collection period
should be used for the UL and DL.
The parameter is an enumerated type with the following values (detailed
definition is in 3GPP TS 36.413 [36]):
\- 1024 ms (0),
\- 2048 ms (1),
\- 5120 ms (2),
\- 10240 ms (3)
Some values may not be always available e.g., due to the large amount of
logging they would generate in a highly loaded network. The selection of a
specific subset of supported values at the eNB is vendor-specific.
### 5.10.27 Collection period M7 in LTE
This parameter is mandatory if the job type is set to Immediate MDT or
Immediate MDT and Trace and either the bit 8 of list of measurements parameter
(defined in Section 5.10.3) in LTE (M7 for DL or M7 for UL) is set to 1.
This measurement parameter defines the collection period that should be used
for packet loss rate measurement made by the eNB. The same collection period
should be used for the UL and DL.
The parameter is an integer type with the following values (detailed
definition is in 3GPP TS 36.413 [36]):
1..60 min
Some values may not be always available e.g., due to the large amount of
logging they would generate in a highly loaded network. The selection of a
specific subset of supported values at the eNB is vendor-specific.
# 6 MDT Reporting
MDT reporting in case of Immediate MDT:
Figure 6.1 illustrates an example of the procedure for Immediate MDT
reporting.
Figure 6.1
In case of Immediate MDT, the MDT related measurements are sent in RRC as part
of the existing RRC measurements. Whenever the eNB/RNC receives the MDT
measurements it shall save it to a Trace Record. The Trace Records are sent to
the TCE either directly or via EM (where EM can reside in the eNB/RNC).
The time and the criteria when the Trace Records are sent to the TCE is vendor
specific however if the Trace Session is deactivated, the Trace Records shall
be sent to the TCE latest by 2 hours ( the exact time is FFS) after the Trace
Session deactivation.
Figure 6.2 illustrates an example of the MDT reporting in case of Logged MDT:
Figure 6.2:
In case of Logged MDT, the UE collects the measurements while it is in IDLE
mode. Once the UE goes to RRC CONNECTED mode, the UE indicates MDT log
availability in the RRCConnectionSetupComplete message to the eNB/RNC. When
the eNB/RNC receives this indication it can request the MDT log (if the UE is
still in the same RAT type where the MDT configuration was done) by sending
the UEInformationRequest message to the UE. The MDT logs are sent to the
network in the UEInformationResponse message. At the reception of the
UEInformationResponse message the eNB/RNC shall save the received MDT log to
the Trace Record. The Trace Records are sent to the TCE either directly or via
EM (where EM can reside in the eNB/RNC).
The time and criteria when the Trace Records are sent to the TCE is vendor
specific however if the Trace Session is deactivated, the Trace Records shall
be sent to the TCE latest by 2 hours ( the exact time is FFS) after the Trace
Session deactivation.
###### ## Annex A (normative):Trace failure notification file format
# A.1 Global structure
See 3GPP TS 32.615 [27].
The following XML namespaces are potentially used in Trace failure
notification XML files:
\- traceFailureNotification.xsd (see A.5)
# A.2 XML elements fileHeader and fileFooter
## A.2.1 XML elements fileHeader
See 3GPP TS 32.615 [27]
## A.2.2 XML element fileFooter
See 3GPP TS 32.615 [27]
# A.3 Trace failure notification specific XML elements
See A.5.
# A.4 Trace IRP XML File Name Conventions
For Trace failure notification XML File Name Conventions the generic file name
definitions as specified by the FT IRP apply (see [28]) with the "specificIRP
extension" defined below.
\.\
SenderType field is the type of NE defined by IOC attribute managedElementType
in 3GPP TS 32.622 [35] that recorded and sent the trace failure notification
file; SenderName field is the identifier of the NE that recorded and sent the
trace failure notification file.
Some examples describing the use of the "specificIRP_extension" in Trace
failure notification naming:
> specificIRP_extension: MME.MME04\ meaning: file produced by MME\.
>
> specificIRP_extension: ENB.ENB122\ meaning: file produced by ENB\.
>
> file name: CT201105131405-060012MME.MME04\ meaning: unique call trace (Trace
> failure notification) file produced by MME\ on May 13, 2011 at 14:05
> local with a time differential of -6 hours against UTC and expiring in 12
> hours after creation
>
> file name: CT201105131315-060012ENB.ENB122_-_2\ meaning: second non-unique
> (RC="2") call trace (Trace failure notification) file produced by
> ENB\ on May 13, 2011 at 13:15 local with a time differential of -6
> hours against UTC and expiring in 12 hours after creation.
# A.5 Trace failure notification file XML schema
\
\
\
\
\
\\ \\ \
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
#