# Aircraft Cargo System Requirements & Traceability Lab

A systems-engineering portfolio project demonstrating the flow from high-level customer needs through technical requirements, interfaces, verification planning, executable testing, and requirements traceability.

The project models a simplified Aircraft Cargo Door Control System for educational purposes.

---

## Project Objective

The goal of this project was to practice a basic systems-engineering workflow by:

- Translating customer needs into system requirements
- Defining hardware/software-style interfaces
- Creating unique requirement identifiers
- Building a Requirements Traceability Matrix
- Defining verification methods
- Writing detailed verification test cases
- Building a simplified Python controller simulation
- Executing verification tests
- Recording PASS/FAIL evidence

---

## Systems Engineering Workflow

```mermaid
flowchart LR

A[Customer Needs]
B[System Requirements]
C[Interface Requirements]
D[Traceability Matrix]
E[Verification Methods]
F[Test Cases]
G[Python Simulation]
H[Test Execution]
I[Verification Evidence]

A --> B
B --> C
C --> D
D --> E
E --> F
F --> G
G --> H
H --> I