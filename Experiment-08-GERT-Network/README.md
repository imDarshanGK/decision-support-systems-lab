# Experiment 8 - GERT Network

## Aim

To design, visualize, and evaluate a GERT (Graphical Evaluation and Review Technique) network for a project lifecycle using Python and Graphviz.

## Problem Statement

A project lifecycle consists of the following activities:

1. Requirements Analysis
2. System Design
3. Prototype Development
4. Prototype Evaluation
5. System Integration
6. Testing
7. Deployment

After prototype development, the prototype can either be successfully evaluated or require rework.

The GERT network represents these alternative paths using activity durations and probabilities.

## Software Requirements

- Python
- Graphviz
- Python Graphviz package

## Project Activities

| Activity | From | To | Duration | Probability |
|---|---|---|---:|---:|
| Requirements Analysis | Start | Requirements | 4 days | 1.00 |
| System Design | Requirements | Design | 5 days | 1.00 |
| Prototype Development | Design | Prototype | 6 days | 1.00 |
| Successful Evaluation | Prototype | Integration | 3 days | 0.80 |
| Prototype Rework | Prototype | Rework | 4 days | 0.20 |
| Re-evaluation | Rework | Integration | 3 days | 1.00 |
| System Testing | Integration | Testing | 5 days | 1.00 |
| Deployment | Testing | Deployment | 2 days | 1.00 |

## GERT Network Paths

### Successful Prototype Path

Start → Requirements → Design → Prototype → Integration → Testing → Deployment

Duration:

4 + 5 + 6 + 3 + 5 + 2 = 25 days

Probability:

0.80

### Prototype Rework Path

Start → Requirements → Design → Prototype → Rework → Integration → Testing → Deployment

Duration:

4 + 5 + 6 + 4 + 3 + 5 + 2 = 29 days

Probability:

0.20

## Expected Project Duration

The probability-weighted expected duration is calculated as:

Expected Duration  
= (0.80 × 25) + (0.20 × 29)  
= 20 + 5.8  
= 25.8 days

Therefore, the expected project duration is:

**25.80 days**

## Assignment

### Exercise 1: Change Prototype Evaluation Probability

The successful prototype evaluation probability was changed from:

0.80 → 0.70

Therefore:

- Successful path probability = 0.70
- Rework path probability = 0.30

Expected duration:

(0.70 × 25) + (0.30 × 29)  
= 17.5 + 8.7  
= 26.20 days

Result:

**26.20 days**

### Exercise 2: Add Security Validation

A Security Validation activity of 3 days was added between Integration and Testing.

New path durations:

- Successful path = 25 + 3 = 28 days
- Rework path = 29 + 3 = 32 days

Expected duration:

(0.70 × 28) + (0.30 × 32)  
= 19.6 + 9.6  
= 29.20 days

Result:

**29.20 days**

### Exercise 3: Add Three Prototype Outcomes

Three possible outcomes were specified:

| Outcome | Probability |
|---|---:|
| Successful | 0.70 |
| Minor Rework | 0.20 |
| Major Rework | 0.10 |
| Total | 1.00 |

The manual does not specify durations for Minor Rework and Major Rework.

Therefore, the probability-weighted expected duration for Exercise 3 cannot be calculated without the corresponding duration values.

## Algorithm

1. Start.
2. Define the project nodes.
3. Define directed activities between nodes.
4. Assign activity durations.
5. Assign probabilities to probabilistic activities.
6. Create the GERT network using Graphviz.
7. Add activity names, durations, and probabilities as edge labels.
8. Identify the alternative paths from Start to Deployment.
9. Calculate the duration of each path.
10. Calculate the probability-weighted expected project duration.
11. Render the GERT network using Graphviz.
12. Display the network and results.
13. End.

## Files

Experiment-08-GERT-Network/
├── gert_network.py
├── gert_network_assignment.py
├── gert_network.png
└── README.md

## Technologies Used

- Python
- Graphviz
- Python Graphviz package

## Result

The GERT network was successfully designed and visualized using Graphviz.

The original network produced an expected project duration of:

**25.80 days**

The assignment exercises were also implemented and evaluated successfully.

- Exercise 1 Expected Duration: **26.20 days**
- Exercise 2 Expected Duration: **29.20 days**
- Exercise 3 Probability Total: **1.00**