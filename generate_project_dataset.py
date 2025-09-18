import numpy as np
import pandas as pd


def generate_synthetic_project_data(n=500, random_state=42):
    """Generate a synthetic dataset simulating program/project management metrics.

    Parameters
    ----------
    n : int
        Number of project instances to generate.
    random_state : int
        Seed for reproducibility.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing synthetic features and a binary success label.
    """
    rng = np.random.default_rng(random_state)

    # Core features
    team_size = rng.integers(3, 20, size=n)
    budget = rng.normal(200_000, 50_000, size=n).clip(min=50_000)  # budgets in dollars
    duration = rng.normal(12, 3, size=n).clip(min=3)  # project duration in months
    scope_changes = rng.poisson(lam=2, size=n)
    complexity = rng.uniform(1, 10, size=n)  # subjective complexity score 1-10
    client_satisfaction = rng.uniform(1, 5, size=n)

    # Calculate a latent success score
    # The coefficients reflect plausible relationships:
    # larger teams and bigger budgets help, but too many scope changes and high complexity hurt
    latent = (
        0.5 * (team_size / team_size.max())
        + 0.4 * (budget / budget.max())
        - 0.3 * (scope_changes / (scope_changes.max() if scope_changes.max() > 0 else 1))
        - 0.3 * (complexity / 10)
        + 0.6 * (client_satisfaction / 5)
        - 0.1 * (duration / duration.max())
    )
    # Add noise
    latent += rng.normal(0, 0.1, size=n)
    # Convert to probability via logistic function
    prob_success = 1 / (1 + np.exp(-5 * (latent - latent.mean())))
    # Binary success outcome
    project_success = rng.binomial(1, prob_success)

    df = pd.DataFrame(
        {
            "project_id": np.arange(1, n + 1),
            "team_size": team_size,
            "budget": budget.round(2),
            "duration_months": duration.round(1),
            "scope_changes": scope_changes,
            "complexity": complexity.round(2),
            "client_satisfaction": client_satisfaction.round(2),
            "project_success": project_success,
        }
    )
    return df


def main():
    df = generate_synthetic_project_data()
    # Save dataset to the `analysis_project` directory
    output_path = "analysis_project/project_data.csv"
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    main()