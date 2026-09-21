from graphviz import Digraph


# Create GERT network
gert = Digraph("GERT_Network", format="png")

# Set graph direction from left to right
gert.attr(rankdir="LR")


# Add project nodes
nodes = [
    "Start",
    "Requirements",
    "Design",
    "Prototype",
    "Rework",
    "Integration",
    "Testing",
    "Deployment"
]

for node in nodes:
    gert.node(node)


# Add activities and their details
gert.edge(
    "Start",
    "Requirements",
    label="Requirements Analysis\n4 days, p=1.00"
)

gert.edge(
    "Requirements",
    "Design",
    label="System Design\n5 days, p=1.00"
)

gert.edge(
    "Design",
    "Prototype",
    label="Prototype Development\n6 days, p=1.00"
)

# Successful prototype evaluation
gert.edge(
    "Prototype",
    "Integration",
    label="Successful Evaluation\n3 days, p=0.80"
)

# Prototype rework
gert.edge(
    "Prototype",
    "Rework",
    label="Prototype Rework\n4 days, p=0.20"
)

# Re-evaluation after rework
gert.edge(
    "Rework",
    "Integration",
    label="Re-evaluation\n3 days, p=1.00"
)

gert.edge(
    "Integration",
    "Testing",
    label="System Testing\n5 days, p=1.00"
)

gert.edge(
    "Testing",
    "Deployment",
    label="Deployment\n2 days, p=1.00"
)


# Calculate path durations
successful_path_duration = 4 + 5 + 6 + 3 + 5 + 2

rework_path_duration = 4 + 5 + 6 + 4 + 3 + 5 + 2


# Probabilities
successful_probability = 0.80
rework_probability = 0.20


# Calculate expected project duration
expected_duration = (
    successful_probability * successful_path_duration
    + rework_probability * rework_path_duration
)


# Print results
print("GERT Network Evaluation")
print("-" * 40)

print(
    f"Successful Prototype Path: "
    f"{successful_path_duration} days"
)

print(
    f"Prototype Rework Path: "
    f"{rework_path_duration} days"
)

print(
    f"Successful Path Probability: "
    f"{successful_probability}"
)

print(
    f"Rework Path Probability: "
    f"{rework_probability}"
)

print(
    f"Expected Project Duration: "
    f"{expected_duration:.2f} days"
)


# Generate Graphviz visualization
output_file = gert.render(
    "gert_network",
    cleanup=True
)

print("\nGERT network generated successfully.")
print(f"Network image: {output_file}")