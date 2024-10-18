# Foreword
This Technical Report has been produced by the 3rd Generation Partnership
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
According to TS 33.501 [2], use of mutual TLS for authentication of NF
requires compliance to 3GPP TS 33.310 [3] section 6.1.3c for TLS client and
TLS server certificate profiles in addition to TLS profile compliance with
section 6.2a of TS 33.310.
The use of TLS certificates in 5G SBA is ubiquitous.
However, unlike standardised model using CMPv2 in RAN, SBA does not have a
standardised model and set of procedures for automated certificate management.
SBA also does not have a standardised protocol for managing life cycle events
of the certificates, e.g., bootstrap, request, issue, enrolment, revocation,
renewal etc.
  1. Lack of standardisation has resulted into number of bespoke methodologies and varying choices of certificate management protocols resulting into inconsistent model.
  2. Once service slicing and NPN are introduced in service provider network, manual management or lack of standardised procedures for life cycle management of TLS certificates belonging to separate legal entities could further complicate the architecture.
All the above have potential of increasing the security risk and impact the
deployment and availability of operators' 5G SBA network.
RAN has benefitted from the standardisation of CMPv2 to be used for
eNodeB/gNodeB automated certificate management. The specification defined a
bootstrap procedure based on the use of vendor certificate for requesting an
operator certificate for the set-up of IPSec IKE2 towards the SeGW. 5G SBA is
within the operator core network domain that could benefit from a study that
leads to the standardisation of an automated certificate management procedure
using a standardised protocol that fits for purpose to serve the 5G Core
Network.
# 1 Scope
The objectives of this study are to identify key issues, potential security
and privacy requirements and solutions with respect to
  * Standardise the use of a single automated certificate management protocol and procedures for certificate life cycle events within intra-PLMN 5G SBA (i.e. to be used by all 5GC NFs including NRF, SCP, SEPP etc.)
  * Study the impact of service mesh in certificate management within 5G SBA
  * _S_ tudy which lifecycle events (e.g., enrolment, renewal, revocation (e.g., OCSP, CRLs), status monitoring) of a certificate need to be covered.
  * Study the relation between certificate management lifecycle and NF management lifecycle.
  * _Study to reference at minimum following principles:_
  * Principle to be reusable when 5G SBA is for NPN (standalone and PNI)
  * Principles standardised to be able to support NFs doing mutual TLS in Slicing
  * Principles standardised to support both intra and inter PLMN, in the latter referring to SEPP certificates in N32 interfaces and potential cross-certification considerations
  * Principles involving 'Chain of Trust' of Certificate Authorities hierarchies
  * Principles for security of CA's cryptographic private key
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
[2] 3GPP TS 33.501: \"Security architecture and procedures for 5G System\".
[3] 3GPP TS 33.310: \"Network Domain Security (NDS); Authentication Framework
(AF)\".
[4] RFC 7515: \"JSON Web Signature\".
[5] 3GPP TS 23.501: \"System architecture for the 5G System (5GS) \".
[6] 3GPP TS 29.510: \"5G System; Network function repository services; Stage
3\".
[7] 3GPP TS 29.571: \"5G System; Common Data Types for Service Based
Interfaces; Stage 3\"
...
[x] \ \[ ([up to and
including]{yyyy[-mm]\|V\}[onwards])]: \"\\".
# 3 Definitions of terms, symbols and abbreviations
## 3.1 Terms
For the purposes of the present document, the terms given in 3GPP TR 21.905
[1] and the following apply. A term defined in the present document takes
precedence over the definition of the same term, if any, in 3GPP TR 21.905
[1].
**example:** text used to clarify abstract rules by applying them literally.
## 3.2 Symbols
For the purposes of the present document, the following symbols apply:
\ \
## 3.3 Abbreviations
For the purposes of the present document, the abbreviations given in 3GPP TR
21.905 [1] and the following apply. An abbreviation defined in the present
document takes precedence over the definition of the same abbreviation, if
any, in 3GPP TR 21.905 [1].
\ \
# 4 Architectural and security assumptions
Editor\'s note: This clause includes the architectural and security
assumptions applicable for the study.
# 5 Key issues
## 5.1 Key Issue #1: Single certificate management protocol and procedures
### 5.1.1 Key issue details
Considering virtualization in 5G SBA, it is impossible to manage certificates
manually.
If there is no standardized use of an automated cert management protocol, the
certificate management needs to be done manually which may lead to missing
refreshment of certificates and usage of expired certificates.
It will increase the implementation and deployment complexity when several
automated certificate management protocol and procedures are defined. And
there will be interoperability issue for different implementation because NF
may not be able to have a certificate from CA or may not be able to verify the
certificate of other NF.
This KI is to investigate required certificate management capabilities (e.g.,
enrolment, renewal), to be used for corresponding certificate life cycle
events, expected from a certificate management protocol and whether it is
feasible to have a single certificate management protocol and procedures for
all these certificate life cycle events within intra-PLMN 5G SBA, which is
mandatory for implementation.
### 5.1.2 Security threats
Not applicable.
### 5.1.3 Potential security requirements
Not applicable.
## 5.2 Key Issue #2: Security protection of NF certificate enrolment
### 5.2.1 Key issue details
An instantiated NF needs to obtain the certificate from the CA for securing
the communication with other NFs, encrypting messages, or signing tokens,
among other purposes in SBA. Thus, a secure and automated certificate
enrolment procedure is indispensable to obtain the certificates. Before
issuing a certificate, operator CA/RA needs to establish an initial trust with
the requestor NF instance, ensuring that the requestor NF instance is the
correct one and is entitled to request a certificate.
This key issue considers the procedure of certificate enrolment including the
establishment of the initial NF trust, the protection of certificate enrolment
procedure, and the authentication between NF and CA.
### 5.2.2 Security threats
If the NF cannot obtain a certificate, and the certificate enrolment procedure
is not secured, the following problems may occur:
  * The NF cannot communicate with each other.
  * If certificate enrolment parameters are tampered, the CA issues an incorrect certificate.
  * Without pre-established trust between the NF and CA/RA, an attacker claiming to be a trusted NF with connectivity in SBA could apply for a valid operator certificate.
### 5.2.3 Potential security requirements
New NF instances need an automated and secure procedure to build initial trust
with the CA/RA during certificate enrolment procedure.
5GS should support the means to secure the automated enrolment of
certificates, include integrity protection and Anti-replay protection of
enrolment procedure.
5GS should support the mutual authentication between involved parties during
the enrolment procedure.5GS should support the verifying of certificate
validity for certificate enrolment.
## 5.3 Key Issue #3: NF Certificate Update
### 5.3.1 Key issue details
NF certificate update is a necessary part of an automated certificate
management mechanism because the long validity period certificate is
considered not secure. Therefore, it is important that each certificate is set
with an appropriate period of validity. Furthermore, it is necessary to update
the NF certificate when the certificate is about to expire or has expired.
Otherwise, NF communication can be disrupted in the middle of operation due to
an unhandled certificate expiry.
### 5.3.2 Security threats
If the NF certificate is not updated, or the certificate update procedure is
not secured, the following problems can occur:
  * An attacker misuses the update mechanism to get hold of valid certificates from CA and mount impersonation attacks.
### 5.3.3 Potential security requirements
5GS should support to update the NF certificate securely.
## 5.4 Key Issue #4: Trust Chain of Certificate Authority Hierarchy
### 5.4.1 Key issue details
According to the scope of the present document, the study should reference _at
minimum_ the following principles:
_3\. Principles involving 'Chain of Trust' of Certificate Authorities._
_4\. Principles for security of CA's cryptographic private key._
As emphasized in the principles, the legitimacy and credibility of certificate
authority are critical for automated certificate management in SBA. Building
the legitimacy and credibility relies on a trust chain of CA hierarchy, which
specifies the CA hierarchy and their transitive trust relationship. Based on
the chain of trust, each CA can be verified by a trusted source. And after the
verification is passed, the CA can act as the new trusted source and issue the
digital certificate for the child CA or the TLS entity. This transitive trust
relationship enables TLS entities in 5G SBA to obtain their own certificates
and verify the certificate of other TLS entities. In the study of automated
certificate management in 5G SBA, the trust chain of CA hierarchy is
indispensable.
Currently, there is no clear requirement about the trust chain of CA hierarchy
in TS 33.310 [3]. The TS 33.310 [3] specifies SBA certificate profiles in
clause 6.1.3c and the general architecture for issuing TLS certificates in
clause 5.1.1.2. However, under the general architecture, it is unclear how to
generate different types of SBA certificates and how SBA certificates can be
verified between different types of NFs.
### 5.4.2 Security threats
Due to the lack of trust chain, the TLS entity in SBA cannot verify the
credibility of SBA certificates sent by other TLS entities. This means that
the connection cannot be established.
Under the Rel-17 general architecture for issuing TLS certificates, CAs may
not be able to generate all the SBA certificates as specified in TS 33.310 [3]
clause 6.1.3c.
### 5.4.3 Potential security requirements
The TLS entity in SBA should be able to verify the received certificate based
on the trust chain.
The TLS entity should be able to obtain the corresponding certificate based on
its role, e.g. the NF service producer shall be able to obtain the TLS server
certificate.
## 5.5 Key Issue #5: Certificates revocation procedures
### 5.5.1 Key issue details
Certificates revocation procedures are a critical part of the overall
certificate lifecycle management. Every certificate has a finite validity
period, during the one it is expected to be in use. However, during that
validity period the certificate owner and/or Certificate Authority may
consider and declare that a certificate is not longer trusted, i.e., invalid
prior to the expiration of the validity period, due to multiple circumstances
(e.g., suspected compromise of the private key).
Certificate Revocation Lists (CRLs), Online Certificate Status Protocol (OCSP)
and OCSP stapling are revocation schemes/functions of certificate revocation.
Clauses 6.1a and 6.1b of TS 33.310 [3] provides profiles for CRL and OCSP
respectively.
5G Core SBA Network functions and operator PKI need a certificate revocation
schema, part of the overall certificate lifecycle management framework, with
the following characteristics:
  * Scalable -- the number of revoked certificates should not be a concern in terms of latency and/or performance of the SBA architecture and network functions.
  * Providing fast/near real time responses -- the revocation function should serve in a highly dynamic environment hosted by virtualized cloud infrastructure.
  * Resilient -- in case of operator CA outages, or issues in the communication to revocation infrastructure, the revocation procedures should be minimally affected, and the Network Functions should be able to check the validity status of the certificate to be verified.
### 5.5.2 Security threats
If the process of publishing a new updated CRL is too slow, it can leave the
client open to attacks. E.g., a revoked certificate may be maliciously used
during the time window between the revocation and the reception of the CRLs.
The lifecycle of ephemeral/short live Network Functions (e.g., in Network
Slicing) will likely reduce even more the time window for distributing and
retrieve the information on the revocation status of the certificates. There
is a risk that the clients are not updated accordingly, creating a security
vulnerability.
Lean Network Function designs based on micro-services type of software
architectures are aiming to optimize the use of resources. Intensive demand of
revocation status checks can generate a severe impact in service availability
by downgrading the performance of the Network Function.
### 5.5.3 Potential security requirements
Not Applicable.
## 5.6 Key Issue #6: Relation between certificate management lifecycle and NF
management lifecycle
### 5.6.1 Key issue details
Although the NF management lifecycle and certificate management lifecycle can
require different management mechanisms and processes, they have some
relations because the certificates are issued for the NFs. Thus, it is
necessary to investigate the relations and consider these relations while
specifying the automated certificate management for SBA.
Generally, since NF lifecycle processes are independent from the validity
period of the associated certificates, if certificate management mechanism is
designed not considering the NF lifecycle, then there can be some cases such
as having NFs with no certificates or existing certificates belonging to no
NF. For example, when the certificate of a producer NF instance has been
revoked without the knowledge of the NRF, the NRF returns that producer NF
instance ID in the discovery procedure. In this case, the consumer NF will try
to get service from the producer NF, but it will not be able to get the
service because the producer NF's certificate has been revoked. This type of
cases will lead to inconsistent status in NRF and reduce the service
availability.
Because of the reasons explained above, the relations between NF management
and certificate management lifecycles need to be considered in the design of
an automated certificate management for SBA. Solutions to this key issue need
to explain how the relations between NF management and certificate lifecycles
can be considered in automated certificate management for SBA.
### 5.6.2 Security threats
Inconsistencies between the NF management lifecycle and certificate management
lifecycle processes can lead to severe vulnerabilities in the system. For
example, if after decommissioning of a NF instance, cryptographic keys and
certificates are still valid, they can be compromised by a potential attacker
and used to access the network and corresponding services.
### 5.6.3 Potential security requirements
In the certificate lifecycle management, NF lifecycle should be considered.
## 5.7 Key Issue #7: Multiples certificates to be associated with a Network
Function
### 5.7.1 Key issue details
In SBA the Network Functions (NFs) could require to support multiple operator
certificates, which can be issued by different operator sub-CAs or root CAs
depending on the established CA hierarchies and predefined network domains,
for different purposes and interfaces.
Each type of certificate per Network Function could have different security
considerations. The type of certificates in Network Functions of SBA are the
following:
  * TLS client EE certificates (for NF consumers)
  * TLS server EE certificates (for NF producers)
NOTE 1: Clause 6.1.3c of 3GPP TS 33.310 [3] profiles the TLS entity
certificates to be used for 5GC SBA.
  * Certificates for signing the access tokens for authorization (JSON Web Signature (JWS) as described in RFC 7515[4]) (for NRFs)
  * Certificates for encrypting HTTP messages between SEPPs (clause 13.2.4.4 of TS 33.501 [2])
  * Certificates for signing Client credentials assertion (CCA) tokens (clause 13.3.8.2 of TS 33.501 [2])
### 5.7.2 Security threats
If the purpose of the issued certificates is not restricted, i.e., the type of
operations for which a public key contained in the certificate can be used are
not specified, those certificated could be used for another purpose than
intended, violating the CA policies, and increasing the risk of cross-protocol
attacks.
Failure to ensure proper segregation of duties means that a NF who generates
the encryption keys and applies for a certificate to the operator CA, could
obtain a certificate which can be misused for tasks that this NF is not
entitled to perform. E.g., a consumer could impersonate producers using their
own client certificate.
### 5.7.3 Potential security requirements
The Network Functions should be able to indicate the purpose of the
certificate being requested in the CSR (Certificate Signing Request) to the
operator CA.
The certificate management framework, i.e., the set of protocols and
procedures for automated certificate management, in 5G SBA shall be able to
provide means for identifying, monitoring, and validating the usage of the
issued certificates.
## 5.8 Key Issue #8: Trusted Network Function instances identifiers
### 5.8.1 Key issue details
Service mesh describes a network of microservices, in which applications are
shared and interaction between applications is possible. To gain operational
control over such distributed microservice architecture, a service needs to be
identified.
SBA can be implemented as a service mesh architecture. In SBA Network Function
(NF) instances offer services to other NFs or NF instances. In order for a
requested NF type, NF service, or NF service instance, to be discovered via
the NRF, the NF instance needs to be registered in the NRF. After
registration, the NRF maintains NF profiles of available NF instances and
their supported services. The NF is identified by a NF instance ID. The
Information Element (IE) NFInstanceID among other IEs is included in the NF
profile maintained in the NRF are specified in 3GPP TS 23.501[5] clauses 6.2.6
and 6.3.1, and in 3GPP TS 29.510 [6].
When a NF requests a X.509 certificate needs to send a Certificate Signing
Request (CSR) message to the operator CA in order to get a X.509 certificate
created. A CSR is often generated by the same NF on which the certificate is
to be installed, although it can also be generated by other trusted
intermediary entity acting on behalf of the NF if the NF does not have such
capability. The public key is included in the CSR and used by the CA to create
the certificate, and the private key is used to sign the information contained
in the CSR (integrity protection). Apart from the public key, the CSR can have
other information (e.g., Common Name, Organization, location, etc.).
3GPP TS 23.501 [5] defines an NF instance as an identifiable instance of the
NF. CSRs must contain a trusted and unique identity of the NF instance
requesting the certificate. 3GPP TS 33.310 [3] in clause 6.1.3c describes
that, as part of the SBA NF certificate profile, the subjectAltName (SAN)
field should contain a URI-ID with the URI for the NF instance ID as an URN.
This URI-ID must contain the identifier of the NF (e.g., SCP, SEPP, NRF, AF,
etc.) instance (nfInstanceID), only using the format of clause 5.3.2 of TS
29.571 [7], what is a Universally Unique IDentifier (UUID). Thus, the
flexibility that a service mesh could offer by integrating different types of
services across heterogeneous environments (and in case of 5GS across
different operator domains) is limited by the use of UUID as identifier.
Operator RA/CA would need to keep track on UUIDs in order to be able to verify
and accept the CSRs, only based on those identifiers.
### 5.8.2 Security threats
A malicious or compromised NF instance can send a rogue CSR message using a
compromised NF Instance Id. Thus, same UUIDs would be used for various NF
instances, including the potential malicious or compromised NF. If the
operator RA/CA does not have the mechanisms to verify and accept a trusted NF
instance identity, then that malicious or compromised NF instance would fetch
a valid certificate and cause different types of attacks in the SBA.
### 5.8.3 Potential security requirements
The certificate management framework should be able to manage and track the NF
instance identifiers per end entity.
## 5.9 Key Issue #9: Automated Certificate Management for Network Slicing
### 5.9.1 Key issue details
A network slice can be understood as a logical network on top of a shared
infrastructure. Network slicing is a key feature of 5G wireless network
standards and allows operators to manage and orchestrate different logical
networks for different kinds of service level requirements. For example, the
communication services using network slicing may include:
• V2X services
• 5G seamless eMBB service with FMC
• massive IoT connections
There can be different network slices logically isolated based on Slice
Service Type (SST) value, as shown in the following diagram:
{width="4.843055555555556in" height="1.7395833333333333in"}
Figure 1 - Different slices logically isolated for different slice customers
Network slicing facilitates a lot of vertical industries to create and manage
logically separated resources across the 5G system dedicated for their own
applications, while ensuring the desired service level agreements are always
met.
Different slices allocated to different slice customers may have different
requirements for automated certificate management. Generally, network slices
need to rely on operator-provided services for automated certificate
management services. Nevertheless, certain slices allocated to slice customers
can require to peform management and operation tasks over operator CA, or even
to use their own CA and certificate management procedures for all or part of
the slice-specific services and NFs. For the latter case, both operator and
slice customer need to agree on how establish the trust between operator and
customer domain and interconnect their CAs, e.g., via cross-certification.
There are also several approaches to address access control and authorization
of NFs for slicing in SBA. The NF can be deployed to serve a dedicated slice
or multiple slices, and network slices can be dynamically or statically
created and removed as per business needs. Depending on NF deployment option,
the lifecycle of a NF can be different from a lifecycle of network slices
assigned to the NF. Therefore, when considering the alignment between NF
lifecycle and certificate lifecycle, the network slicing lifecycles can also
need to be taken into account depending on NF and network slices deployment
solution.
### 5.9.2 Security threats
A potential compromise or malfunction in the certificate management framework
of the operator may impact in the certificate management framework of the
slice and vice versa. E.g., if automated certificate updates are not completed
before the expiration dates, it can lead to service / slice un-availability,
requiring manual administration of certificates.
Misalignment between lifecycles of certificate and slices could lead to
service unavailability for customer specific slices.
### 5.9.3 Potential security requirements
The framework should take into account the fact that certificates might belong
to different domains, e.g. in deployment where different 3rd party slices co-
exist and interoperate.
# 6 Solutions
Editor's Note: This clause contains the proposed solutions addressing the
identified key issues.
## 6.Y Solution #Y: \
### 6.Y.1 Introduction
Editor's Note: Each solution should list the key issues being addressed.
### 6.Y.2 Solution details
### 6.Y.3 Evaluation
Editor's Note: Each solution should motivate how the potential security
requirements of the key issues being addressed are fulfilled.
# 7 Conclusions
Editor's Note: This clause contains the agreed conclusions that will form the
basis for any normative work.
#