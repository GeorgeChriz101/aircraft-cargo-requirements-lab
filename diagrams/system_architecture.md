# Aircraft Cargo Door Control System Architecture

```mermaid
flowchart LR

A[Operator Control Panel]
B[System Controller]
C[Door Position Sensor]
D[Lock Position Sensor]
E[Door Actuator]
F[Locking Actuator]
G[Warning Indicator]
H[Aircraft Power Interface]

A -->|OPEN / CLOSE Commands| B

C -->|Door Position| B
D -->|Lock Status| B
H -->|Power Available| B

B -->|OPEN / CLOSE / STOP| E
B -->|LOCK / UNLOCK| F
B -->|Status / Fault| G