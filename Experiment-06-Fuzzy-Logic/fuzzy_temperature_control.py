# ============================================================
# Decision Support Systems Laboratory
# Experiment No. 6
#
# Implement Fuzzy Logic for Decision Making
# ============================================================

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Step 1: Define Input and Output Variables
# ------------------------------------------------------------

temperature = ctrl.Antecedent(
    np.arange(0, 51, 1),
    'temperature'
)

fan_speed = ctrl.Consequent(
    np.arange(0, 101, 1),
    'fan_speed'
)

# ------------------------------------------------------------
# Step 2: Define Membership Functions
# ------------------------------------------------------------

temperature['cold'] = fuzz.trimf(
    temperature.universe,
    [0, 0, 20]
)

temperature['warm'] = fuzz.trimf(
    temperature.universe,
    [10, 25, 40]
)

temperature['hot'] = fuzz.trimf(
    temperature.universe,
    [30, 50, 50]
)

fan_speed['low'] = fuzz.trimf(
    fan_speed.universe,
    [0, 0, 50]
)

fan_speed['medium'] = fuzz.trimf(
    fan_speed.universe,
    [25, 50, 75]
)

fan_speed['high'] = fuzz.trimf(
    fan_speed.universe,
    [50, 100, 100]
)

# ------------------------------------------------------------
# Step 3: Define Fuzzy Rules
# ------------------------------------------------------------

rule1 = ctrl.Rule(
    temperature['cold'],
    fan_speed['low']
)

rule2 = ctrl.Rule(
    temperature['warm'],
    fan_speed['medium']
)

rule3 = ctrl.Rule(
    temperature['hot'],
    fan_speed['high']
)

# ------------------------------------------------------------
# Step 4: Create Control System
# ------------------------------------------------------------

fan_control = ctrl.ControlSystem([
    rule1,
    rule2,
    rule3
])

fan_simulation = ctrl.ControlSystemSimulation(
    fan_control
)

# ------------------------------------------------------------
# Step 5: Enter Crisp Temperature
# ------------------------------------------------------------

input_temperature = 30

fan_simulation.input[
    'temperature'
] = input_temperature

# ------------------------------------------------------------
# Step 6: Perform Fuzzy Inference
# ------------------------------------------------------------

fan_simulation.compute()

# ------------------------------------------------------------
# Step 7: Display Output
# ------------------------------------------------------------

output_speed = fan_simulation.output['fan_speed']

print("==============================================")
print("FUZZY TEMPERATURE CONTROL SYSTEM")
print("==============================================")

print(
    "Input Temperature :",
    input_temperature,
    "°C"
)

print(
    "Recommended Fan Speed :",
    round(output_speed, 2),
    "%"
)

# ------------------------------------------------------------
# Step 8: Display Temperature Membership Values
# ------------------------------------------------------------

cold_membership = fuzz.interp_membership(
    temperature.universe,
    temperature['cold'].mf,
    input_temperature
)

warm_membership = fuzz.interp_membership(
    temperature.universe,
    temperature['warm'].mf,
    input_temperature
)

hot_membership = fuzz.interp_membership(
    temperature.universe,
    temperature['hot'].mf,
    input_temperature
)

print("\nMembership Values")
print("----------------------------------------------")

print(
    "Cold :",
    round(cold_membership, 3)
)

print(
    "Warm :",
    round(warm_membership, 3)
)

print(
    "Hot :",
    round(hot_membership, 3)
)

# ------------------------------------------------------------
# Step 9: Interpret Decision
# ------------------------------------------------------------

print("\nDecision")

if output_speed < 35:
    print("Fan Speed Level : LOW")

elif output_speed < 70:
    print("Fan Speed Level : MEDIUM")

else:
    print("Fan Speed Level : HIGH")

# ------------------------------------------------------------
# Step 10: Plot Membership Functions
# ------------------------------------------------------------

temperature.view()

plt.title(
    "Temperature Membership Functions"
)

plt.show()

fan_speed.view(
    sim=fan_simulation
)

plt.title(
    "Fan Speed Membership Functions"
)

plt.show()