# Testimony Contradiction Detector

this is a Python-based framework that uses propositional logic and directed graphs to model and detect contradictions in witness testimonies with court records. This project is heavily inspired by the mechanics of the *Phoenix Wright: Ace Attorney*.
it's a bit of a hassle but it works :P

this tool automatically flags inconsistencies by mapping statements and evidence into logical propositions to generates truth tables for conflicting accounts, and visualizes the entire testimony as a dependency graph.

---

## Structure

* **`models.py`**: Contains the core data structures (`Node` and `Testimony`) representing statements, evidence, and the case container.
* **`logic.py`**: Handles the propositional logic engine, including contradiction checking and truth table generation.
* **`graph.py`**: Manages the NetworkX directed graph construction and prints the contradiction report to the console.
* **`visualization.py`**: Responsible for rendering the graph into a color-coded PNG image using Matplotlib.
* **`cases.py`**: Stores the case data definitions (e.g., *Turnabout Sisters* and templates for custom cases).
* **`main.py`**: The main execution script that ties everything together.
* **`test_logic.py`**: A suite of unit tests for the logical operations.
* **`requirements.txt`**: A list of the required Python packages to run the project.
```bash
pip install -r requirements.txt
```
to install the requirements

---

## Installation & Setup

1. **Clone or download the repository** to your local machine.
2. **(Optional but recommended)** Create a virtual environment:
   ```bash
   python -m venv venv
   ```
   ```bash
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```