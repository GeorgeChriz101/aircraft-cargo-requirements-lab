# System Requirements

This document defines the system-level requirements for the Aircraft Cargo Door Control System.

Each requirement is assigned a unique identifier so it can later be traced to customer needs, verification methods, and test cases.

---

## SYS-REQ-001 — Open Command Response

The system shall initiate cargo door opening when a valid OPEN command is received and all required safety conditions are satisfied.

Related Customer Need:
CN-001 — Safe Door Operation

Verification Method:
Test

---

## SYS-REQ-002 — Close Command Response

The system shall initiate cargo door closing when a valid CLOSE command is received and all required safety conditions are satisfied.

Related Customer Need:
CN-001 — Safe Door Operation

Verification Method:
Test

---

## SYS-REQ-003 — Door Position Indication

The system shall provide an indication of the cargo door position as OPEN, CLOSED, or IN TRANSITION.

Related Customer Need:
CN-002 — Door Position Awareness

Verification Method:
Test

---

## SYS-REQ-004 — Locked Status Indication

The system shall provide a LOCKED indication only when the cargo door is confirmed closed and the locking mechanism is confirmed engaged.

Related Customer Need:
CN-003 — Locking Confirmation

Verification Method:
Test

---

## SYS-REQ-005 — Unsafe Operation Inhibit

The system shall prevent cargo door movement when an unsafe operating condition is detected.

Related Customer Need:
CN-004 — Unsafe Command Prevention

Verification Method:
Test

---

## SYS-REQ-006 — Fault Indication

The system shall provide a fault indication when a monitored sensor or actuator fault is detected.

Related Customer Need:
CN-005 — Fault Notification

Verification Method:
Test

---

## SYS-REQ-007 — Power Interface

The system shall operate when valid aircraft electrical power is available at the defined system power interface.

Related Customer Need:
CN-006 — Reliable Power Interface

Verification Method:
Test and Inspection

---

## SYS-REQ-008 — Maintenance Fault Identification

The system shall make detected fault information available for maintenance troubleshooting.

Related Customer Need:
CN-007 — Maintenance Support

Verification Method:
Inspection and Test

---

## SYS-REQ-009 — Controlled Door Movement

The system shall command cargo door movement in a controlled open or close direction without commanding both directions simultaneously.

Related Customer Need:
CN-008 — Controlled Door Movement

Verification Method:
Test

---

## SYS-REQ-010 — Open Limit Protection

The system shall stop the opening command when the cargo door reaches the fully open position.

Related Customer Need:
CN-001 — Safe Door Operation
CN-008 — Controlled Door Movement

Verification Method:
Test

---

## SYS-REQ-011 — Closed Limit Protection

The system shall stop the closing command when the cargo door reaches the fully closed position.

Related Customer Need:
CN-001 — Safe Door Operation
CN-008 — Controlled Door Movement

Verification Method:
Test

---

## SYS-REQ-012 — Locking Sequence

The system shall command the locking mechanism only after the cargo door is confirmed closed.

Related Customer Need:
CN-003 — Locking Confirmation
CN-004 — Unsafe Command Prevention

Verification Method:
Test