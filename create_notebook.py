"""
Utility script to build a Jupyter notebook for the synthetic project analysis.

Running this script generates ``analysis_notebook.ipynb`` in the ``analysis_project``
directory. The notebook includes exploratory data analysis (EDA), basic
visualizations, and a simple predictive model to classify project success.

"""
import json
from pathlib import Path

import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell


def create_notebook(output_dir: Path) -> None:
    """Create a Jupyter notebook with EDA and modeling steps.

    Parameters
    ----------
    output_dir : Path
        Directory where the notebook will be saved.
    """
    nb = new_notebook()

    cells = []
    # Title and description
    cells.append(
        new_markdown_cell(
            """
            # Synthetic Project Analysis

            This notebook demonstrates exploratory data analysis and a simple predictive model on a synthetic
            project management dataset. The goal is to provide a hands‑on example for roles such as
            Business Analyst, Program Manager and Data Analyst. We will explore relationships between
            team size, budget, duration and other factors and determine how they influence project success.
            """
        )
    )

    # Load libraries and dataset
    cells.append(
        new_code_cell(
            """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression

%matplotlib inline

# Load the dataset
df = pd.read_csv('project_data.csv')
df.head()
"""
        )
    )

    # Show basic information
    cells.append(
        new_code_cell(
            """
# Display basic information about the dataset
df.info()

# Statistical summary
df.describe()
"""
        )
    )

    # Visualizations
    cells.append(
        new_markdown_cell(
            """
            ## Exploratory Data Analysis

            We'll visualize distributions of numeric features and examine relationships with the target variable
            `project_success`. These plots help identify patterns and potential predictors.
            """
        )
    )
    cells.append(
        new_code_cell(
            """
# Histograms for continuous features
continuous_cols = ['team_size', 'budget', 'duration_months', 'complexity', 'client_satisfaction']
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 8))
axes = axes.flatten()
for ax, col in zip(axes, continuous_cols):
    sns.histplot(df[col], bins=20, ax=ax, kde=True)
    ax.set_title(f'Distribution of {col}')
plt.tight_layout()

# Relationship between budget and success
plt.figure(figsize=(6, 4))
sns.boxplot(x='project_success', y='budget', data=df)
plt.title('Budget vs Project Success')
plt.xticks([0, 1], ['Failure', 'Success'])
plt.show()
"""
        )
    )

    # Correlation heatmap
    cells.append(
        new_code_cell(
            """
# Correlation matrix
corr = df.drop(columns=['project_id']).corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
"""
        )
    )

    # Predictive modeling
    cells.append(
        new_markdown_cell(
            """
            ## Predictive Modeling

            We'll train a logistic regression model to predict project success. First, we split the data
            into training and testing sets, fit the model, then evaluate its performance using
            classification metrics and a confusion matrix.
            """
        )
    )
    cells.append(
        new_code_cell(
            """
# Features and target
X = df[['team_size', 'budget', 'duration_months', 'scope_changes', 'complexity', 'client_satisfaction']]
y = df['project_success']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Fit logistic regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluation
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
"""
        )
    )

    # Conclusion cell
    cells.append(
        new_markdown_cell(
            """
            ## Conclusion

            This simple analysis illustrates how data-driven approaches can inform project management
            decisions. The visualizations and correlation analysis reveal how factors like budget,
            client satisfaction, scope changes, and team size can influence project success. The
            logistic regression model serves as a baseline predictive tool; you can explore more
            advanced models (e.g., random forests or gradient boosting) to improve accuracy and
            incorporate additional domain knowledge.
            """
        )
    )

    nb['cells'] = cells
    output_path = output_dir / 'analysis_notebook.ipynb'
    nbformat.write(nb, str(output_path))


def main():
    output_dir = Path('analysis_project')
    output_dir.mkdir(parents=True, exist_ok=True)
    create_notebook(output_dir)


if __name__ == '__main__':
    main()