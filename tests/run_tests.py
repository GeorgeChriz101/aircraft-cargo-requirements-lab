import csv
import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from src.cargo_controller import CargoDoorController


results = []


def record_result(test_case, requirement, passed, notes):
    result = "PASS" if passed else "FAIL"

    results.append({
        "Test_Case": test_case,
        "Requirement": requirement,
        "Execution_Status": "Executed",
        "Result": result,
        "Notes": notes
    })

    print(
        f"{test_case} | {requirement} | "
        f"{result} | {notes}"
    )


# TC-001
controller = CargoDoorController()

controller.power_available = True
controller.door_position = "CLOSED"
controller.lock_status = "UNLOCKED"
controller.unsafe_condition = False

controller.command_open()

passed = controller.actuator_command == "OPEN"

record_result(
    "TC-001",
    "SYS-REQ-001",
    passed,
    "Valid OPEN command"
)


# TC-002
controller = CargoDoorController()

controller.door_position = "OPEN"

controller.command_close()

passed = controller.actuator_command == "CLOSE"

record_result(
    "TC-002",
    "SYS-REQ-002",
    passed,
    "Valid CLOSE command"
)


# TC-003
controller = CargoDoorController()

positions = [
    "OPEN",
    "CLOSED",
    "IN TRANSITION"
]

passed = True

for position in positions:
    controller.update_door_position(position)

    if controller.get_door_status() != position:
        passed = False

record_result(
    "TC-003",
    "SYS-REQ-003",
    passed,
    "Door position reporting"
)


# TC-004
controller = CargoDoorController()

controller.door_position = "CLOSED"
controller.lock_status = "LOCKED"

valid_condition = controller.get_locked_indication()

controller.door_position = "OPEN"
controller.lock_status = "LOCKED"

invalid_condition_1 = not controller.get_locked_indication()

controller.door_position = "CLOSED"
controller.lock_status = "UNLOCKED"

invalid_condition_2 = not controller.get_locked_indication()

passed = (
    valid_condition
    and invalid_condition_1
    and invalid_condition_2
)

record_result(
    "TC-004",
    "SYS-REQ-004",
    passed,
    "Locked indication logic"
)


# TC-005
controller = CargoDoorController()

controller.door_position = "CLOSED"
controller.unsafe_condition = True

controller.command_open()

passed = controller.actuator_command == "STOP"

record_result(
    "TC-005",
    "SYS-REQ-005",
    passed,
    "Unsafe condition inhibits movement"
)


# TC-006
controller = CargoDoorController()

fault_tests = []

controller.door_sensor_fault = True
fault_tests.append(
    controller.detect_faults()
    == "DOOR POSITION SENSOR FAULT"
)

controller = CargoDoorController()
controller.lock_sensor_fault = True

fault_tests.append(
    controller.detect_faults()
    == "LOCK POSITION SENSOR FAULT"
)

controller = CargoDoorController()
controller.actuator_fault = True

fault_tests.append(
    controller.detect_faults()
    == "DOOR ACTUATOR FAULT"
)

passed = all(fault_tests)

record_result(
    "TC-006",
    "SYS-REQ-006",
    passed,
    "Fault indication behavior"
)


# TC-007
controller = CargoDoorController()

controller.power_available = True
controller.door_position = "CLOSED"

powered_operation = controller.command_open()

controller = CargoDoorController()

controller.power_available = False
controller.door_position = "CLOSED"

unpowered_operation = controller.command_open()

passed = (
    powered_operation is True
    and unpowered_operation is False
)

record_result(
    "TC-007",
    "SYS-REQ-007",
    passed,
    "Power availability behavior"
)


# TC-008
controller = CargoDoorController()

controller.lock_sensor_fault = True

fault = controller.detect_faults()

passed = (
    fault == "LOCK POSITION SENSOR FAULT"
)

record_result(
    "TC-008",
    "SYS-REQ-008",
    passed,
    "Maintenance fault information"
)


# TC-009
controller = CargoDoorController()

command = controller.conflicting_direction_request()

passed = command == "STOP"

record_result(
    "TC-009",
    "SYS-REQ-009",
    passed,
    "Conflicting direction protection"
)


# TC-010
controller = CargoDoorController()

controller.door_position = "CLOSED"

controller.command_open()

controller.update_door_position("OPEN")

passed = controller.actuator_command == "STOP"

record_result(
    "TC-010",
    "SYS-REQ-010",
    passed,
    "Fully open limit stops actuator"
)


# TC-011
controller = CargoDoorController()

controller.door_position = "OPEN"

controller.command_close()

controller.update_door_position("CLOSED")

passed = controller.actuator_command == "STOP"

record_result(
    "TC-011",
    "SYS-REQ-011",
    passed,
    "Fully closed limit stops actuator"
)


# TC-012
controller = CargoDoorController()

controller.door_position = "CLOSED"

valid_lock = controller.command_lock()

controller = CargoDoorController()

controller.door_position = "OPEN"

invalid_lock_open = not controller.command_lock()

controller = CargoDoorController()

controller.door_position = "IN TRANSITION"

invalid_lock_transition = not controller.command_lock()

passed = (
    valid_lock
    and invalid_lock_open
    and invalid_lock_transition
)

record_result(
    "TC-012",
    "SYS-REQ-012",
    passed,
    "Lock command only allowed when door closed"
)


# Save results
output_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "verification",
    "test_results.csv"
)

with open(
    output_path,
    "w",
    newline=""
) as file:

    fieldnames = [
        "Test_Case",
        "Requirement",
        "Execution_Status",
        "Result",
        "Notes"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(results)


print()
print("Test execution complete.")
print(
    f"Results saved to: "
    f"{os.path.abspath(output_path)}"
)