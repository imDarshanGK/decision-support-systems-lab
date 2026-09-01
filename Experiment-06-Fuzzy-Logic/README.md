# Experiment 06 - Fuzzy Logic

## Decision Support Systems Lab

### Experiment Title

Implement Fuzzy Logic for Decision Making

### Aim

To implement a Fuzzy Logic-based decision support system for temperature control using Python and scikit-fuzzy.

### Problem Statement

A temperature-control system is developed using Fuzzy Logic.

The system takes temperature as input and determines the appropriate fan speed.

### Input

- Temperature

### Output

- Fan Speed

### Temperature Categories

- Cold
- Warm
- Hot

### Fan Speed Categories

- Low
- Medium
- High

### Fuzzy Rules

1. If temperature is Cold, then fan speed is Low.
2. If temperature is Warm, then fan speed is Medium.
3. If temperature is Hot, then fan speed is High.

### Algorithm

1. Define temperature and fan-speed variables.
2. Define membership functions.
3. Define fuzzy rules.
4. Create the fuzzy control system.
5. Enter a crisp temperature value.
6. Perform fuzzification.
7. Apply fuzzy inference rules.
8. Perform defuzzification.
9. Display the recommended fan speed.
10. Plot membership functions.

## Assignment

### Title

Extend the Temperature-Control DSS using Humidity

The temperature-control system is extended by introducing Humidity as a second input variable.

### Inputs

- Temperature: Cold / Warm / Hot
- Humidity: Low / Medium / High

### Output

- Fan Speed: Low / Medium / High

### Assignment Requirements

1. Define membership functions for humidity.
2. Develop at least 6 fuzzy rules.
3. Implement the system using scikit-fuzzy.
4. Test the system with at least five temperature-humidity combinations.
5. Record the fuzzification values.
6. Calculate the defuzzified fan speed.
7. Plot the input and output membership functions.
8. Compare the results with the single-input temperature system.

### Files

- `fuzzy_temperature_control.py` - Main Experiment 6 program.
- `fuzzy_temperature_humidity_control.py` - Assignment program using temperature and humidity.

### Technologies Used

- Python
- scikit-fuzzy
- NumPy
- Matplotlib

### Result

The Fuzzy Logic-based temperature control system was successfully implemented using Python and scikit-fuzzy. The extended system also considers humidity to provide a more detailed fan-speed decision.