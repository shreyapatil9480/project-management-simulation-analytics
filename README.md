# Synthetic Project Analysis

This repository showcases a self‑contained data analysis project designed to
demonstrate skills relevant to business analysts, program managers, and data
analysts. It includes a **synthetic dataset** simulating project management
metrics, an **exploratory data analysis (EDA) and predictive modeling
notebook**, and helper scripts for generating the data and notebook from
scratch. The project is ready to use out of the box and can be extended or
customized to suit your needs.

## Dataset

The `project_data.csv` file contains 500 synthetic project records with the
following fields:

| Column | Description |
|---|---|
| `project_id` | Unique identifier for each project |
| `team_size` | Number of team members assigned to the project |
| `budget` | Total project budget (USD) |
| `duration_months` | Planned duration of the project in months |
| `scope_changes` | Number of significant scope changes encountered |
| `complexity` | Subjective complexity score (1–10) |
| `client_satisfaction` | Satisfaction rating from the client (1–5) |
| `project_success` | Binary outcome (1 = success, 0 = failure) |

These features capture common aspects of program and project management. The
`project_success` label is generated using a logistic model that assigns
higher success probability to projects with adequate budgets, satisfied
clients, and fewer scope changes.

## Contents

* **`project_data.csv`** – Synthetic dataset described above.
* **`analysis_notebook.ipynb`** – Jupyter notebook performing EDA and a
  baseline predictive model (logistic regression). It contains:
  * Summary statistics and data overview
  * Visualizations of feature distributions and relationships
  * Correlation matrix heatmap
  * Train/test split and model evaluation
* **`requirements.txt`** – List of Python dependencies needed to run the
  notebook and scripts.
* **`generate_project_dataset.py`** – Script to create a new synthetic
  dataset. You can adjust the sample size or random seed as desired.
* **`create_notebook.py`** – Script that programmatically builds the
  notebook. Useful if you modify the dataset schema or want to regenerate
  the notebook from scratch.

## Getting Started

### Prerequisites

Ensure you have Python 3.8 or later installed. Clone this repository and
install the required packages:

```bash
git clone https://github.com/<your‑username>/<your‑repo>.git
cd <your‑repo>
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Running the Notebook

Launch Jupyter and open `analysis_notebook.ipynb`:

```bash
jupyter notebook
```

The notebook will guide you through the exploratory analysis and model
training. Feel free to tweak the code to experiment with different models
or visualizations.

### Regenerating the Dataset or Notebook

If you'd like to create a fresh dataset or regenerate the notebook:

```bash
python analysis_project/generate_project_dataset.py
python analysis_project/create_notebook.py
```

These commands overwrite `project_data.csv` and `analysis_notebook.ipynb`
with new versions. Adjust parameters within the scripts (e.g., sample size
or random seed) to explore different scenarios.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE)
file for details.