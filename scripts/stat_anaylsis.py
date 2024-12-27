import pandas as pd
from scipy.stats import chi2_contingency, pearsonr

def chi_squared_test(df, column1, column2):
    """Perform chi-squared test between two categorical columns."""
    contingency_table = pd.crosstab(df[column1], df[column2])
    stat, p, dof, expected = chi2_contingency(contingency_table)
    return {"statistic": stat, "p_value": p, "degrees_of_freedom": dof}

def calculate_correlation(df, col1, col2):
    """Calculate Pearson correlation between two numerical columns."""
    corr, _ = pearsonr(df[col1], df[col2])
    return corr

if __name__ == "__main__":
    data_path = "../data/insurance_data.csv"
    df = pd.read_csv(data_path)
    print(chi_squared_test(df, "Province", "CoverCategory"))
    print(calculate_correlation(df, "TotalPremium", "TotalClaims"))
