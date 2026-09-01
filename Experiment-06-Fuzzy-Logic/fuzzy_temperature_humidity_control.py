# ============================================================
# Decision Support Systems Laboratory
# Experiment No. 6 - Assignment
#
# Extend Temperature Control DSS using Humidity
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

humidity = ctrl.Antecedent(
    np.arange(0, 101, 1),
    'humidity'
)

fan_speed = ctrl.Consequent(
    np.arange(0, 101, 1),
    'fan_speed'
)

# ------------------------------------------------------------
# Step 2: Define Temperature Membership Functions
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

# ------------------------------------------------------------
# Step 3: Define Humidity Membership Functions
# ------------------------------------------------------------

humidity['low'] = fuzz.trimf(
    humidity.universe,
    [0, 0, 50]
)

humidity['medium'] = fuzz.trimf(
    humidity.universe,
    [25, 50, 75]
)

humidity['high'] = fuzz.trimf(
    humidity.universe,
    [50, 100, 100]
)

# ------------------------------------------------------------
# Step 4: Define Fan Speed Membership Functions
# ------------------------------------------------------------

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
# Step 5: Define Fuzzy Rules
# ------------------------------------------------------------

rule1 = ctrl.Rule(
    temperature['cold'] & humidity['low'],
    fan_speed['low']
)

rule2 = ctrl.Rule(
    temperature['cold'] & humidity['medium'],
    fan_speed['low']
)

rule3 = ctrl.Rule(
    temperature['warm'] & humidity['low'],
    fan_speed['medium']
)

rule4 = ctrl.Rule(
    temperature['warm'] & humidity['high'],
    fan_speed['high']
)

rule5 = ctrl.Rule(
    temperature['hot'] & humidity['low'],
    fan_speed['high']
)

rule6 = ctrl.Rule(
    temperature['hot'] & humidity['medium'],
    fan_speed['high']
)

rule7 = ctrl.Rule(
    temperature['hot'] & humidity['high'],
    fan_speed['high']
)

rule8 = ctrl.Rule(
    temperature['warm'] & humidity['medium'],
    fan_speed['medium']
)

# ------------------------------------------------------------
# Step 6: Create Fuzzy Control System
# ------------------------------------------------------------

fan_control = ctrl.ControlSystem([
    rule1,
    rule2,
    rule3,
    rule4,
    rule5,
    rule6,
    rule7,
    rule8
])

# ------------------------------------------------------------
# Step 7: Test Cases
# ------------------------------------------------------------

test_cases = [
    (15, 30),
    (25, 50),
    (30, 40),
    (35, 70),
    (45, 80)
]

print("==============================================")
print("FUZZY TEMPERATURE-HUMIDITY CONTROL SYSTEM")
print("==============================================")

# ------------------------------------------------------------
# Step 8: Process Test Cases
# ------------------------------------------------------------

for i, (input_temperature, input_humidity) in enumerate(
    test_cases, start=1
):

    fan_simulation = ctrl.ControlSystemSimulation(
        fan_control
    )

    fan_simulation.input['temperature'] = input_temperature
    fan_simulation.input['humidity'] = input_humidity

    fan_simulation.compute()

    output_speed = fan_simulation.output['fan_speed']

    # Temperature Membership Values

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

    # Humidity Membership Values

    low_membership = fuzz.interp_membership(
        humidity.universe,
        humidity['low'].mf,
        input_humidity
    )

    medium_membership = fuzz.interp_membership(
        humidity.universe,
        humidity['medium'].mf,
        input_humidity
    )

    high_membership = fuzz.interp_membership(
        humidity.universe,
        humidity['high'].mf,
        input_humidity
    )

    print("\n----------------------------------------------")
    print("Test Case", i)
    print("----------------------------------------------")

    print(
        "Temperature :",
        input_temperature,
        "°C"
    )

    print(
        "Humidity    :",
        input_humidity,
        "%"
    )

    print("\nTemperature Membership Values")

    print(
        "Cold :",
        round(cold_membership, 3)
    )

    print(
        "Warm :",
        round(warm_membership, 3)
    )

    print(
        "Hot  :",
        round(hot_membership, 3)
    )

    print("\nHumidity Membership Values")

    print(
        "Low    :",
        round(low_membership, 3)
    )

    print(
        "Medium :",
        round(medium_membership, 3)
    )

    print(
        "High   :",
        round(high_membership, 3)
    )

    print(
        "\nDefuzzified Fan Speed :",
        round(output_speed, 2),
        "%"
    )

    if output_speed < 35:
        print("Fan Speed Level : LOW")

    elif output_speed < 70:
        print("Fan Speed Level : MEDIUM")

    else:
        print("Fan Speed Level : HIGH")

# ------------------------------------------------------------
# Step 9: Plot Temperature Membership Functions
# ------------------------------------------------------------

temperature.view()

plt.title(
    "Temperature Membership Functions"
)

plt.show()

# ------------------------------------------------------------
# Step 10: Plot Humidity Membership Functions
# ------------------------------------------------------------

humidity.view()

plt.title(
    "Humidity Membership Functions"
)

plt.show()

# ------------------------------------------------------------
# Step 11: Plot Fan Speed Membership Functions
# ------------------------------------------------------------

fan_speed.view()

plt.title(
    "Fan Speed Membership Functions"
)

plt.show()

# ------------------------------------------------------------
# Step 12: Comparison with Single-Input System
# ------------------------------------------------------------

print("\n==============================================")
print("COMPARISON WITH SINGLE-INPUT SYSTEM")
print("==============================================")

print("Single-input system considers only temperature.")

print(
    "Extended system considers both temperature and humidity."
)

print(
    "The extended system provides a more detailed fan-speed decision."
)