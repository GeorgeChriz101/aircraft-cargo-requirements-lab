class CargoDoorController:
    def __init__(self):
        self.power_available = True
        self.door_position = "CLOSED"
        self.lock_status = "UNLOCKED"

        self.unsafe_condition = False

        self.door_sensor_fault = False
        self.lock_sensor_fault = False
        self.actuator_fault = False

        self.actuator_command = "STOP"
        self.lock_command = "NONE"

        self.fault_message = None

    def detect_faults(self):
        if self.door_sensor_fault:
            self.fault_message = "DOOR POSITION SENSOR FAULT"

        elif self.lock_sensor_fault:
            self.fault_message = "LOCK POSITION SENSOR FAULT"

        elif self.actuator_fault:
            self.fault_message = "DOOR ACTUATOR FAULT"

        else:
            self.fault_message = None

        return self.fault_message

    def get_door_status(self):
        if self.door_sensor_fault:
            return "UNKNOWN"

        return self.door_position

    def get_locked_indication(self):
        if self.lock_sensor_fault:
            return False

        return (
            self.door_position == "CLOSED"
            and self.lock_status == "LOCKED"
        )

    def command_open(self):
        self.detect_faults()

        if not self.power_available:
            self.actuator_command = "STOP"
            return False

        if self.unsafe_condition:
            self.actuator_command = "STOP"
            return False

        if self.fault_message:
            self.actuator_command = "STOP"
            return False

        if self.door_position == "OPEN":
            self.actuator_command = "STOP"
            return False

        self.actuator_command = "OPEN"
        return True

    def command_close(self):
        self.detect_faults()

        if not self.power_available:
            self.actuator_command = "STOP"
            return False

        if self.unsafe_condition:
            self.actuator_command = "STOP"
            return False

        if self.fault_message:
            self.actuator_command = "STOP"
            return False

        if self.door_position == "CLOSED":
            self.actuator_command = "STOP"
            return False

        self.actuator_command = "CLOSE"
        return True

    def update_door_position(self, new_position):
        valid_positions = ["OPEN", "CLOSED", "IN TRANSITION"]

        if new_position not in valid_positions:
            raise ValueError("Invalid door position")

        self.door_position = new_position

        if new_position == "OPEN" and self.actuator_command == "OPEN":
            self.actuator_command = "STOP"

        if new_position == "CLOSED" and self.actuator_command == "CLOSE":
            self.actuator_command = "STOP"

    def command_lock(self):
        if not self.power_available:
            self.lock_command = "NONE"
            return False

        if self.door_position != "CLOSED":
            self.lock_command = "NONE"
            return False

        self.lock_command = "LOCK"
        return True

    def command_unlock(self):
        if not self.power_available:
            self.lock_command = "NONE"
            return False

        self.lock_command = "UNLOCK"
        return True

    def conflicting_direction_request(self):
        # Simulated protection against OPEN and CLOSE
        # being commanded simultaneously.
        self.actuator_command = "STOP"

        return self.actuator_command