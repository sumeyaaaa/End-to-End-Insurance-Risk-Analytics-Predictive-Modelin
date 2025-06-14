import pandas as pd
import matplotlib.pyplot as plt

def calculate_monthly_claim_stats(df, date_col='TransactionMonth', claim_col='TotalClaims', policy_col='PolicyID'):
    """
    Aggregates monthly claim statistics from a DataFrame.

    Parameters:
    - df: DataFrame with insurance data
    - date_col: Column with transaction dates
    - claim_col: Column with claim values
    - policy_col: Column with policy or transaction identifiers

    Returns:
    - monthly_claims: DataFrame with claim count, frequency, total and average severity per month
    """
    monthly_claims = df.groupby(df[date_col].dt.to_period('M')).agg(
        claim_count=(policy_col, 'count'),
        claim_frequency=(claim_col, lambda x: (x > 0).sum()),
        total_claims=(claim_col, 'sum'),
        avg_claim_severity=(claim_col, lambda x: x[x > 0].mean())
    ).reset_index()

    # Convert period back to timestamp for plotting
    monthly_claims[date_col] = monthly_claims[date_col].dt.to_timestamp()

    return monthly_claims

def plot_monthly_claim_frequency(monthly_df, date_col='TransactionMonth', freq_col='claim_frequency'):
    """
    Plots monthly claim frequency over time.

    Parameters:
    - monthly_df: DataFrame with aggregated monthly statistics
    - date_col: Column with datetime values
    - freq_col: Column with claim frequency values
    """
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_df[date_col], monthly_df[freq_col], marker='o')
    plt.title("Monthly Claim Frequency Over Time")
    plt.xlabel("Month")
    plt.ylabel("Number of Claims")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_monthly_trend(monthly_df, date_col='TransactionMonth', value_col='claim_frequency', title='', ylabel=''):
    """
    Plots a time series trend of a specified value over months.

    Parameters:
    - monthly_df: DataFrame with monthly data
    - date_col: Column name for date (must be datetime)
    - value_col: Column name for the value to plot
    - title: Title of the plot
    - ylabel: Label for the y-axis
    """
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_df[date_col], monthly_df[value_col], marker='o', color='orange' if 'severity' in value_col else 'blue')
    plt.title(title or f"{value_col} Over Time")
    plt.xlabel("Month")
    plt.ylabel(ylabel or value_col)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

