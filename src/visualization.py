import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution_and_boxplot(df, columns, bins=50):
    """
    Plots both histogram and boxplot for each specified numerical column.

    Parameters:
    - df: pandas DataFrame
    - columns: list of column names to plot
    - bins: number of bins for histograms
    """
    for col in columns:
        plt.figure(figsize=(12, 5))
        
        # Histogram with KDE
        plt.subplot(1, 2, 1)
        sns.histplot(df[col], kde=True, bins=bins)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')

        # Boxplot
        plt.subplot(1, 2, 2)
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot of {col}')
        plt.xlabel(col)

        plt.tight_layout()
        plt.show()
import matplotlib.pyplot as plt

def plot_avg_claim_by_model(df, make_col='make', model_col='Model', claim_col='TotalClaims', top_n=10):
    """
    Plots top and bottom N vehicle makes/models by average claim amount.

    Parameters:
    - df: DataFrame containing vehicle and claim info
    - make_col: Column name for make (default 'make')
    - model_col: Column name for model (default 'Model')
    - claim_col: Column name for claim amount (default 'TotalClaims')
    - top_n: Number of top/bottom makes/models to display
    """
    # Calculate average claim per model
    avg_claims = (
        df.groupby([make_col, model_col])[claim_col]
        .mean()
        .reset_index(name='AvgClaimAmount')
    )

    # Top and bottom
    top_claims = avg_claims.sort_values(by='AvgClaimAmount', ascending=False).head(top_n)
    bottom_claims = avg_claims.sort_values(by='AvgClaimAmount', ascending=True).head(top_n)

    # Plot top
    plt.figure(figsize=(10, 5))
    plt.barh(top_claims[make_col] + ' ' + top_claims[model_col], top_claims['AvgClaimAmount'])
    plt.title(f"Top {top_n} Makes/Models by Avg Claim Amount")
    plt.xlabel("Avg Claim Amount")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

    # Plot bottom
    plt.figure(figsize=(10, 5))
    plt.barh(bottom_claims[make_col] + ' ' + bottom_claims[model_col], bottom_claims['AvgClaimAmount'], color='green')
    plt.title(f"Bottom {top_n} Makes/Models by Avg Claim Amount")
    plt.xlabel("Avg Claim Amount")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_missing_and_numerical_distribution(df, 
                                               categorical_cols=None, 
                                               numerical_cols=None, 
                                               date_col=None):
    """
    Analyze missing values and plot distributions for selected numerical features.
    
    Parameters:
    - df: DataFrame to analyze
    - categorical_cols: List of categorical column names
    - numerical_cols: List of numerical column names
    - date_col: Name of the date column (optional)
    
    Returns:
    - missing_summary: A pandas Series showing percent of missing values
    """
    # Set defaults if None
    if categorical_cols is None:
        categorical_cols = []
    if numerical_cols is None:
        numerical_cols = []
    
    # Handle date conversion
    if date_col:
        if df[date_col].dtype != 'datetime64[ns]':
            df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
        columns_to_check = categorical_cols + numerical_cols + [date_col]
    else:
        columns_to_check = categorical_cols + numerical_cols

    # Calculate missing percentage
    missing_summary = df[columns_to_check].isnull().mean().sort_values(ascending=False) * 100
    print("📊 Missing Value Percentage:\n")
    print(missing_summary)

    # Plot numerical distributions
    if numerical_cols:
        fig, axes = plt.subplots(nrows=(len(numerical_cols) + 1) // 2, ncols=2, figsize=(14, 6))
        axes = axes.flatten()
        for idx, col in enumerate(numerical_cols):
            sns.histplot(df[col], kde=True, ax=axes[idx], bins=30)
            axes[idx].set_title(f"Distribution of {col}")
        for i in range(len(numerical_cols), len(axes)):
            fig.delaxes(axes[i])  # Remove unused axes
        plt.tight_layout()
        plt.show()
    
    return missing_summary
