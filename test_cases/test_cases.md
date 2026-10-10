# Aircraft Cargo Door Control System Test Cases

These test cases verify the Aircraft Cargo Door Control System requirements.

Each test case contains:

- Requirement under test
- Preconditions
- Test input
- Procedure
- Expected result
- Pass/Fail criteria

---

## TC-001 — Valid Open Command

Requirement:
SYS-REQ-001

Purpose:
Verify that the system initiates cargo door opening when a valid OPEN command is received and all required safety conditions are satisfied.

Preconditions:
- Aircraft power is available.
- Cargo door is closed.
- Cargo door is unlocked.
- No fault condition is active.
- Safety conditions are satisfied.

Test Input:
OPEN command

Procedure:
1. Confirm the cargo door is in the CLOSED state.
2. Confirm the locking mechanism is UNLOCKED.
3. Confirm that no unsafe condition is active.
4. Send an OPEN command.
5. Observe the controller output.

Expected Result:
The controller commands the door actuator to begin opening.

Pass Criteria:
The OPEN actuator command is generated.

Fail Criteria:
The OPEN command is rejected or no actuator command is generated.

---

## TC-002 — Valid Close Command

Requirement:
SYS-REQ-002

Purpose:
Verify that the system initiates cargo door closing when a valid CLOSE command is received.

Preconditions:
- Aircraft power is available.
- Cargo door is open.
- No fault condition is active.
- Safety conditions are satisfied.

Test Input:
CLOSE command

Procedure:
1. Confirm the cargo door is OPEN.
2. Confirm no unsafe condition is active.
3. Send a CLOSE command.
4. Observe the controller output.

Expected Result:
The controller commands the door actuator to begin closing.

Pass Criteria:
The CLOSE actuator command is generated.

Fail Criteria:
The CLOSE command is rejected or no actuator command is generated.

---

## TC-003 — Door Position Indication

Requirement:
SYS-REQ-003

Purpose:
Verify that the system correctly reports cargo door position.

Preconditions:
- System is powered.
- Door position sensor is operational.

Test Inputs:
- OPEN
- CLOSED
- IN TRANSITION

Procedure:
1. Set the simulated door position to OPEN.
2. Observe the system status.
3. Set the simulated door position to CLOSED.
4. Observe the system status.
5. Set the simulated door position to IN TRANSITION.
6. Observe the system status.

Expected Result:
The displayed system state matches the simulated sensor state.

Pass Criteria:
OPEN, CLOSED, and IN TRANSITION are correctly reported.

Fail Criteria:
Any state is reported incorrectly.

---

## TC-004 — Locked Status Confirmation

Requirement:
SYS-REQ-004

Purpose:
Verify that LOCKED status is only provided when the cargo door is closed and the locking mechanism is engaged.

Preconditions:
- System is powered.
- Door position sensor is operational.
- Lock position sensor is operational.

Test Inputs:
1. Door CLOSED + Lock LOCKED
2. Door OPEN + Lock LOCKED
3. Door CLOSED + Lock UNLOCKED

Procedure:
1. Apply each input combination.
2. Observe the LOCKED indication.

Expected Result:
LOCKED indication appears only when:
- Door = CLOSED
- Lock = LOCKED

Pass Criteria:
Only the valid closed-and-locked condition produces the LOCKED indication.

Fail Criteria:
LOCKED is displayed under any invalid condition.

---

## TC-005 — Unsafe Operation Inhibit

Requirement:
SYS-REQ-005

Purpose:
Verify that cargo door movement is prevented when an unsafe condition exists.

Preconditions:
- System is powered.
- Door is closed.
- Unsafe condition input is active.

Test Input:
OPEN command

Procedure:
1. Activate the unsafe-condition input.
2. Send an OPEN command.
3. Observe the controller output.

Expected Result:
The controller does not command cargo door movement.

Pass Criteria:
No OPEN actuator command is generated.

Fail Criteria:
The system commands the door to move.

---

## TC-006 — Fault Indication

Requirement:
SYS-REQ-006

Purpose:
Verify that the system provides a fault indication when a monitored fault is detected.

Preconditions:
- System is powered.

Test Inputs:
- Door position sensor fault
- Lock position sensor fault
- Door actuator fault

Procedure:
1. Introduce each simulated fault one at a time.
2. Observe the system warning indication.
3. Record the response.

Expected Result:
A FAULT indication is generated for each monitored fault.

Pass Criteria:
Each simulated fault results in a fault indication.

Fail Criteria:
A fault occurs without a fault indication.

---

## TC-007 — Aircraft Power Availability

Requirement:
SYS-REQ-007

Purpose:
Verify system behavior when valid aircraft electrical power is available.

Preconditions:
- Cargo door control system is connected to the simulated aircraft power interface.

Test Inputs:
1. Power Available
2. Power Unavailable

Procedure:
1. Set aircraft power to AVAILABLE.
2. Attempt a valid system command.
3. Confirm the system responds normally.
4. Remove aircraft power.
5. Attempt another command.
6. Observe the system response.

Expected Result:
The system operates when valid power is available and does not operate when power is unavailable.

Pass Criteria:
System operation correctly follows power availability.

Fail Criteria:
The system fails while valid power is available or operates when power is unavailable.

---

## TC-008 — Maintenance Fault Information

Requirement:
SYS-REQ-008

Purpose:
Verify that detected fault information is available for maintenance troubleshooting.

Preconditions:
- System is powered.
- Maintenance status output is available.

Test Input:
Simulated lock position sensor fault

Procedure:
1. Introduce a lock position sensor fault.
2. Observe the maintenance fault information.
3. Record the displayed or logged fault condition.

Expected Result:
The system identifies that a lock position sensor fault has occurred.

Pass Criteria:
The correct fault information is available for troubleshooting.

Fail Criteria:
No fault information is available or the wrong fault is identified.

---

## TC-009 — Simultaneous Direction Protection

Requirement:
SYS-REQ-009

Purpose:
Verify that OPEN and CLOSE actuator commands are not generated simultaneously.

Preconditions:
- System is powered.
- Door actuator interface is available for monitoring.

Test Input:
Conflicting OPEN and CLOSE command condition

Procedure:
1. Simulate conflicting movement requests.
2. Observe the actuator control output.
3. Record the commanded direction.

Expected Result:
The controller never commands OPEN and CLOSE at the same time.

Pass Criteria:
Only one direction or STOP is commanded.

Fail Criteria:
OPEN and CLOSE commands are active simultaneously.

---

## TC-010 — Fully Open Limit Protection

Requirement:
SYS-REQ-010

Purpose:
Verify that the system stops commanding the door open after the fully open position is reached.

Preconditions:
- System is powered.
- Door is opening.

Test Input:
Door position changes to fully OPEN.

Procedure:
1. Begin an OPEN operation.
2. Simulate the door reaching the fully OPEN position.
3. Observe the actuator command.

Expected Result:
The controller removes the OPEN actuator command.

Pass Criteria:
The OPEN command stops when fully open status is detected.

Fail Criteria:
The OPEN actuator remains commanded.

---

## TC-011 — Fully Closed Limit Protection

Requirement:
SYS-REQ-011

Purpose:
Verify that the system stops commanding the door closed after the fully closed position is reached.

Preconditions:
- System is powered.
- Door is closing.

Test Input:
Door position changes to fully CLOSED.

Procedure:
1. Begin a CLOSE operation.
2. Simulate the door reaching the fully CLOSED position.
3. Observe the actuator command.

Expected Result:
The controller removes the CLOSE actuator command.

Pass Criteria:
The CLOSE command stops when fully closed status is detected.

Fail Criteria:
The CLOSE actuator remains commanded.

---

## TC-012 — Locking Sequence

Requirement:
SYS-REQ-012

Purpose:
Verify that the locking mechanism is commanded only after the cargo door is confirmed closed.

Preconditions:
- System is powered.
- Lock actuator is available.

Test Inputs:
1. Door CLOSED
2. Door OPEN
3. Door IN TRANSITION

Procedure:
1. Apply each simulated door-position state.
2. Observe the locking actuator command.

Expected Result:
The LOCK command is generated only when the door is confirmed CLOSED.

Pass Criteria:
LOCK is commanded only in the CLOSED state.

Fail Criteria:
LOCK is commanded while the door is OPEN or IN TRANSITION.