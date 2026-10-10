# Interface Requirements

This document defines simplified interfaces between the major components of the Aircraft Cargo Door Control System.

---

## INT-REQ-001 — Operator Command Interface

The Operator Control Panel shall provide OPEN and CLOSE command signals to the System Controller.

Interface:

Operator Control Panel
→ System Controller

Data:
OPEN command
CLOSE command

---

## INT-REQ-002 — Door Position Sensor Interface

The Door Position Sensor shall provide door position status to the System Controller.

Interface:

Door Position Sensor
→ System Controller

Data:
OPEN
CLOSED
IN TRANSITION

---

## INT-REQ-003 — Lock Position Sensor Interface

The Lock Position Sensor shall provide LOCKED or UNLOCKED status to the System Controller.

Interface:

Lock Position Sensor
→ System Controller

Data:
LOCKED
UNLOCKED

---

## INT-REQ-004 — Door Actuator Interface

The System Controller shall provide OPEN or CLOSE commands to the Door Actuator.

Interface:

System Controller
→ Door Actuator

Commands:
OPEN
CLOSE
STOP

---

## INT-REQ-005 — Locking Actuator Interface

The System Controller shall provide LOCK or UNLOCK commands to the Locking Actuator.

Interface:

System Controller
→ Locking Actuator

Commands:
LOCK
UNLOCK

---

## INT-REQ-006 — Warning Indicator Interface

The System Controller shall provide system status and fault indications to the Warning Indicator.

Interface:

System Controller
→ Warning Indicator

Data:
DOOR OPEN
DOOR CLOSED
DOOR LOCKED
FAULT

---

## INT-REQ-007 — Aircraft Power Interface

The Aircraft Power Interface shall provide electrical power to the cargo door control system.

Interface:

Aircraft Electrical System
→ Cargo Door Control System

Data:
Power Available
Power Unavailable