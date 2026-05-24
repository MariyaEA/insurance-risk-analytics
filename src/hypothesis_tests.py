import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind


def claim_frequency_test(df: pd.DataFrame, group_col: str, group_a: str, group_b: str):
    """Run chi-square test for claim frequency between two groups."""

    subset = df[df[group_col].isin([group_a, group_b])].copy()

    contingency_table = pd.crosstab(
        subset[group_col],
        subset["HasClaim"]
    )

    chi2, p_value, dof, expected = chi2_contingency(contingency_table)

    return {
        "test": "Chi-square test",
        "group_a": group_a,
        "group_b": group_b,
        "p_value": p_value,
        "decision": "Reject H0" if p_value < 0.05 else "Fail to reject H0"
    }


def numerical_ttest(df: pd.DataFrame, group_col: str, group_a: str, group_b: str, target_col: str):
    """Run independent t-test for numerical KPI between two groups."""

    subset = df[df[group_col].isin([group_a, group_b])].copy()

    a_values = subset[subset[group_col] == group_a][target_col].dropna()
    b_values = subset[subset[group_col] == group_b][target_col].dropna()

    stat, p_value = ttest_ind(
        a_values,
        b_values,
        equal_var=False
    )

    return {
        "test": "Welch t-test",
        "group_a": group_a,
        "group_b": group_b,
        "target": target_col,
        "p_value": p_value,
        "decision": "Reject H0" if p_value < 0.05 else "Fail to reject H0"
    }
