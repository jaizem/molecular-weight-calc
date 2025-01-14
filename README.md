# Molecular Weight Calculator
## Overview
The Molecular Weight Calculator project is a Python-based toolkit designed to assist chemists, students, and researchers by automating essential chemical computations. It currently features:
1. Molecular Weight Calculation: Computes the molecular weight of a compound from its chemical formula.
2. Chemical Equation Balancer: Balances chemical equations given reactants and products.
3. 3D Molecular Visualization (in development): Models molecules in 3D using RDKit and Py3Dmol.

## Features  
#### Molecular Weight Calculator
This program takes a chemical formula as input (e.g., H2O, C6H12O6) and calculates its molecular weight using data from the periodic table. The function has been rigorously tested against a dataset containing 273 different compounds to ensure accuracy.

**How it Works**
1. Parses the chemical formula to identify each element and its count.
2. Looks up atomic weights from a periodic table data structure.
3. Calculates the total molecular weight by summing the products of element counts and their atomic weights.

#### Chemical Equation Balancer
The equation balancer takes a series of reactants and products and outputs a balanced chemical equation. This feature ensures compliance with the law of conservation of mass.

**How it Works**
1. Parses reactants and products to create a matrix representation of the chemical equation.
2. Uses matrix algebra to solve for coefficients that balance the equation.
   
#### 3D Molecular Visualization (In Progress)
This functionality will visualize molecules in 3D and include features such as:
- Reading molecular data from a CSV file using pandas.
- Signal processing with numpy to analyze spectral data:
  - Transform data into numpy arrays.
  - Identify peaks and troughs in spectral lines.
- Spectral line plotting using seaborn and matplotlib.

**How it Works**
1. Loads molecular data from a CSV file.
2. Processes signals by transforming data into numpy arrays. Uses arrays to identify spectral peaks and troughs.
3. Plots spectral data with seaborn/matplotlib.
4. Generates 3D molecular models with RDKit and Py3Dmol.

## Getting Started
### Prerequisites:
- Python 3.8+
- Required Python libraries:
  - numpy
  - pandas
  - seaborn
  - matplotlib
  - RDKit
  - Py3Dmol
### Installation
1. Clone the repo:
   ```
   git clone https://github.com/jaizem/molecular-weight-calc.git
   ```
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
### Usage
**Molecular Weight Calculator**

Run the script and input a chemical formula:
   ```
   python molecular_weight_calculator.py
   ```
**Chemical Equation Balancer**

Run the script ad input reactants and products:
   ```
   python chemical_eqquation_balancer.py
   ```
### Under Development 
- Complete the 3D molecular visualization feature.
- Add functionality for advanced spectral analysis.
- Develop a GUI for an improved user experience.

### Testing 
- The molecular weight calculator has been validated using a dataset of 273 compounds.
- The equation balancer has been tested with standard chemical equations from textbooks.

### Contributing
This is a personal project, but feedback is welcome. Please fork the repository and submit a pull request. 

### License 
This project is licensed under the MIT License.
