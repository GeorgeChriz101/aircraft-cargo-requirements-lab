# Aircraft Cargo Door Control System

## Project Purpose

This project is a small systems-engineering laboratory that demonstrates how high-level customer needs can be converted into system requirements, interface requirements, verification methods, and test cases.

## System Description

The Aircraft Cargo Door Control System manages the operation of an electrically actuated cargo door.

The system receives commands from an operator and uses sensors to determine the position and locking state of the cargo door.

A controller processes the sensor information and determines whether the door can safely open, close, lock, or unlock.

## Main Components

The simplified system contains:

1. Operator Control Panel
2. System Controller
3. Door Position Sensor
4. Lock Position Sensor
5. Door Actuator
6. Locking Actuator
7. Warning Indicator
8. Aircraft Power Interface

## Basic Operating Sequence

A simplified cargo-door operating sequence is:

Operator Command
        |
        v
System Controller
        |
        v
Check Sensors
        |
        v
Safety Conditions Satisfied?
        |
   Yes / No
    |      |
    v      v
Operate   Reject Command
Actuator  + Warning
        |
        v
Verify Door Position
        |
        v
Lock Door
        |
        v
Confirm Locked Status