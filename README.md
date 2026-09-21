# 2D Flood Risk Assessment and Mitigation Analysis Using PCSWMM and Python

## Project Overview

This project evaluates flood hazards around a hospital located within a river floodplain using PCSWMM 2D hydraulic modeling and Python-based analysis.

The objective was to assess whether increasing culvert capacity could reduce flooding impacts near critical infrastructure and improve flood conveyance through the study area.

---

## Software Used

- PCSWMM 2D
- EPA SWMM 5.2.4
- Python
- Pandas
- Matplotlib

---

## Study Area

The study area consists of a hospital complex located within a flood-prone river corridor in France. The hydraulic model includes:

- 2D floodplain mesh
- Directional river channels
- Culvert crossing beneath a parking area
- Downstream boundary conditions
- DEM-based terrain representation

---

## Model Development

The PCSWMM model was developed using:

- Digital Elevation Model (DEM)
- 2D mesh generation
- River centerline definition
- Boundary polygons
- Obstruction layers
- Upstream inflow hydrograph
- Downstream hydraulic controls

A 12-hour simulation was performed using PCSWMM's 2D hydraulic engine.

### Model Stability

| Parameter | Value |
|------------|------------|
| Surface Runoff Continuity Error | 0.00% |
| Flow Routing Continuity Error | -0.01% |
| Water Quality Continuity Error | 0.00% |

The model demonstrated excellent numerical stability and mass balance performance.

---

## Scenarios Evaluated

### Existing Condition

Original culvert dimensions:

- Width = 5 m
- Depth = 1.5 m

### Flood Mitigation Scenario

Modified culvert dimensions:

- Width = 10 m
- Depth = 3.0 m

The culvert cross-sectional area was increased to improve conveyance capacity through the floodplain.

---

## Results

| Parameter | Existing Condition | Mitigation Scenario |
|------------|------------|------------|
| Maximum Flood Depth (m) | 3.49 | 3.10 |
| Maximum Velocity (m/s) | 14.08 | 14.08 |

---

### Performance Improvement

### Flood Depth Reduction

Calculation:

(3.49 - 3.10) / 3.49 × 100 = 11.17%

**Maximum Flood Depth Reduction = 11.17%**

### Velocity Reduction

Calculation:

(14.08 - 14.08) / 14.08 × 100 = 0.00%

**Maximum Velocity Reduction = 0.00%**

---

## Key Engineering Findings

Increasing the culvert dimensions produced a measurable reduction in flood depth while having little influence on peak flow velocity.

Results indicate that:

- Culvert enlargement reduced flood severity.
- Flood depths decreased by approximately 11%.
- Maximum flow velocities remained unchanged.
- Flood behavior appears to be controlled primarily by floodplain hydraulics and boundary conditions rather than culvert capacity alone.

These findings suggest that additional flood mitigation measures may be required to significantly reduce flood risk around the hospital.

---

## Python Analysis

Python was used to:

- Calculate flood depth reductions
- Compare mitigation performance
- Generate engineering summary tables
- Create flood depth comparison charts
- Create velocity comparison charts

Libraries used:

```python
pandas
matplotlib
```

---

## Figures

### Existing Condition Flood Depths

figures/Existing_Flood_Depths.png

### Flood Mitigation Scenario

figures/Mitigation_Flood_Depths.png

### Existing Condition Flow Velocities

figures/Existing_Flow_Velocities.png

### Flood Mitigation Scenario

figures/Mitigation_Flow_Velocities.png

---

## Conclusions

A PCSWMM 2D flood model was successfully developed to evaluate flood hazards around a hospital located within a river floodplain.

Increasing culvert dimensions from 5 m × 1.5 m to 10 m × 3.0 m reduced maximum flood depths by 11.17%, while maximum velocities remained unchanged.

The results indicate that while culvert enlargement provides some improvement, floodplain storage and downstream hydraulic controls likely govern flooding within the study area.

Future work may include:

- Alternative downstream boundary conditions
- Additional culvert crossings
- Floodplain grading modifications
- Levee or floodwall assessments
- Climate change inflow scenarios

---

## Author

Gener Francis Lambayan

Civil Engineering Technician 

Hydraulic Modeling | Stormwater Management | PCSWMM | EPA SWMM5 | Python
