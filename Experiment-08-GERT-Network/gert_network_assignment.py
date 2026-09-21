# Experiment 8 - GERT Network Assignment

# Exercise 1
# Change successful prototype evaluation probability
# from 0.80 to 0.70

successful_probability = 0.70
rework_probability = 0.30

successful_path_duration = 25
rework_path_duration = 29

expected_duration_ex1 = (
    successful_probability * successful_path_duration
    + rework_probability * rework_path_duration
)

print("Exercise 1: Changed Prototype Evaluation Probability")
print("-" * 50)
print(f"Successful Path Probability: {successful_probability}")
print(f"Rework Path Probability: {rework_probability}")
print(f"Successful Path Duration: {successful_path_duration} days")
print(f"Rework Path Duration: {rework_path_duration} days")
print(f"New Expected Duration: {expected_duration_ex1:.2f} days")


# Exercise 2
# Add Security Validation of 3 days
# between Integration and Testing

security_validation_duration = 3

successful_path_with_security = (
    successful_path_duration + security_validation_duration
)

rework_path_with_security = (
    rework_path_duration + security_validation_duration
)

expected_duration_ex2 = (
    successful_probability * successful_path_with_security
    + rework_probability * rework_path_with_security
)

print("\nExercise 2: Security Validation")
print("-" * 50)
print(f"Security Validation: {security_validation_duration} days")
print(
    f"Successful Path Duration: "
    f"{successful_path_with_security} days"
)
print(
    f"Rework Path Duration: "
    f"{rework_path_with_security} days"
)
print(
    f"New Expected Duration: "
    f"{expected_duration_ex2:.2f} days"
)

# Exercise 3
# Add a third outcome after Prototype Development

successful_probability_ex3 = 0.70
minor_rework_probability = 0.20
major_rework_probability = 0.10

print("\nExercise 3: Three Prototype Outcomes")
print("-" * 50)

print(
    f"Successful Prototype: "
    f"{successful_probability_ex3}"
)

print(
    f"Minor Rework: "
    f"{minor_rework_probability}"
)

print(
    f"Major Rework: "
    f"{major_rework_probability}"
)

print(
    f"Total Probability: "
    f"{successful_probability_ex3 + minor_rework_probability + major_rework_probability:.2f}"
)

print("\nNote:")
print(
    "The manual does not specify durations for "
    "Minor Rework and Major Rework."
)
print(
    "Therefore, expected duration cannot be calculated "
    "without those durations."
)