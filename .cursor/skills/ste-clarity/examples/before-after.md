# Meaning-preserving examples

Each rewrite uses only its source. Review notes flag missing information; they are not additions to the rewritten text.

## 1. Engineering status report

### Source

The implementation of the authentication-related enhancement is progressing well overall, with most core components already having been completed, although there remain several integration-related dependencies which will need to be addressed before the solution can be considered fully production-ready.

### Rewrite

The authentication enhancement is progressing well overall. Most core components are complete. Several integration dependencies remain and must be addressed before the enhancement is fully ready for production.

### Review note

The source does not name the dependencies, owners, or completion criteria. Do not infer specific service integrations, completed implementation, or a specific test gate.

## 2. API failure behavior

### Source

In circumstances where verification is unsuccessful, relevant information relating to the reason for the unsuccessful verification should ideally be made available to downstream consumers so that they can understand what happened.

### Rewrite

When verification fails, downstream consumers should ideally receive information that explains the failure.

### Review note

The responsible component, response fields, and delivery mechanism are unspecified. Preserve “should ideally”; do not convert this recommendation into a mandatory API contract.

## 3. Architecture explanation

### Source

The event is subsequently picked up by the downstream service, which then performs processing on it and updates the record after which a response may be propagated to other interested components.

### Rewrite

1. The downstream service receives and processes the event.
2. The downstream service updates the record.
3. A response may then be sent to other interested components.

### Review note

The source does not identify the event, service, record, or component that sends the response. It does not establish whether this flow is synchronous or asynchronous. Preserve “may.”

## 4. Procedure

### Source

Prior to attempting to restart the application, the operator should ensure that the database connection has been restored and, if this is the case, the application may then be restarted and subsequently monitored to determine whether normal operation has resumed.

### Rewrite

1. Before attempting a restart, the operator should confirm that the database connection has been restored.
2. If the connection has been restored, the application may be restarted. After the restart, it may be monitored to check whether normal operation has resumed.

### Review note

The source leaves the restart and monitoring actors unspecified. It does not identify a health endpoint, expected response, or troubleshooting action. A rewrite must not supply them.

## 5. Investment report

### Source

The portfolio experienced a modest decline during the review period, primarily as a consequence of weakness across several technology-related holdings and unfavorable currency movements, though the overall investment thesis remains broadly unchanged at this stage.

### Rewrite

The portfolio fell modestly during the review period. The main causes were weakness in several technology-related holdings and unfavorable currency movements. The overall investment thesis remains broadly unchanged at this stage.

### Review note

No exact return, named holdings, contribution figures, calendar event, or investment action is supplied. Preserve the qualitative assessment without inventing numbers or advice.

## 6. Requirement with missing performance criteria

### Source

The API should quickly return useful error information.

### Rewrite

The API should return useful error information quickly.

### Review note

“Quickly” and “useful” need definitions before this requirement is testable. Ask for the response-time target and required error information if a complete specification is requested. Do not invent a threshold or change “should” to “must.”

## 7. Ambiguous ownership

### Source

After Service A calls Service B, it retries twice if the request times out.

### Rewrite

After Service A calls Service B, it retries twice if the request times out.

### Review note

“It” could refer to either service. Ask which service retries if the task requires a definitive revision. Until clarified, retain the original rather than choosing an owner.
