"""
===============================================================================
PROJECT:
2D Flood Risk Assessment and Flood Mitigation Analysis
Hospital Floodplain Study

AUTHOR:
Gener Francis Lambayan

SOFTWARE:
PCSWMM + Python

DESCRIPTION:
This script compares Existing Conditions and Flood Mitigation scenarios
for a hospital floodplain model developed in PCSWMM.

Performance metrics evaluated:
    • Maximum Flood Depth
    • Maximum Flow Velocity
    • Percent Reduction

The script generates:
    • Engineering Summary
    • Flood Depth Comparison Chart
    • Velocity Comparison Chart

===============================================================================
"""

# =============================================================================
# IMPORT LIBRARIES
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# PROJECT DATA
# =============================================================================

# Existing Condition Results
existing_depth = 3.49          # m
existing_velocity = 14.08      # m/s

# Mitigation Scenario Results
mitigation_depth = 3.1        # m
mitigation_velocity = 14.08    # m/s


# =============================================================================
# CALCULATE IMPROVEMENTS
# =============================================================================

depth_reduction = (
    (existing_depth - mitigation_depth)
    / existing_depth
) * 100

velocity_reduction = (
    (existing_velocity - mitigation_velocity)
    / existing_velocity
) * 100


# =============================================================================
# CREATE SUMMARY TABLE
# =============================================================================

results = pd.DataFrame({
    "Scenario": [
        "Existing Condition",
        "Flood Mitigation"
    ],
    "Maximum Depth (m)": [
        existing_depth,
        mitigation_depth
    ],
    "Maximum Velocity (m/s)": [
        existing_velocity,
        mitigation_velocity
    ]
})

print("\n")
print("===================================================")
print("HOSPITAL FLOOD ANALYSIS SUMMARY")
print("===================================================")
print(results)
print("===================================================")

print(f"\nFlood Depth Reduction: {depth_reduction:.2f}%")
print(f"Velocity Reduction:    {velocity_reduction:.2f}%")

print("\nEngineering Interpretation:")
print(
    "Increasing culvert capacity resulted in a "
    f"{depth_reduction:.2f}% reduction in maximum flood depth "
    f"and a {velocity_reduction:.2f}% reduction in "
    "maximum flow velocity."
)

print(
    "\nThe results suggest that culvert capacity is "
    "not the dominant hydraulic control on flooding "
    "within the study area."
)

# =============================================================================
# FLOOD DEPTH COMPARISON CHART
# =============================================================================

plt.figure(figsize=(8, 5))

plt.bar(
    ["Existing", "Mitigation"],
    [existing_depth, mitigation_depth]
)

plt.ylabel("Maximum Flood Depth (m)")
plt.xlabel("Scenario")
plt.title("Hospital Flood Model: Maximum Flood Depth Comparison")

for i, value in enumerate([
    existing_depth,
    mitigation_depth
]):
    plt.text(
        i,
        value + 0.05,
        f"{value:.2f}",
        ha="center"
    )

plt.tight_layout()

plt.savefig(
    "Max_Flood_Depth_Comparison.png",
    dpi=300
)

plt.show()

# =============================================================================
