import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column):
    """Plot histogram for a numerical column."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")
    plt.show()

def plot_correlation_matrix(df):
    """Plot a heatmap of correlation matrix."""
    corr_matrix = df.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

def plot_boxplot(df, x_col, y_col):
    """Plot a boxplot between two columns."""
    plt.figure(figsize=(12, 6))
    sns.boxplot(x=df[x_col], y=df[y_col])
    plt.title(f"Boxplot of {y_col} by {x_col}")
    plt.show()

if __name__ == "__main__":
    data_path = "../data/insurance_data.csv"
    df = pd.read_csv(data_path)
    plot_histogram(df, "TotalPremium")
    plot_correlation_matrix(df)
    plot_boxplot(df, "Province", "TotalClaims")
