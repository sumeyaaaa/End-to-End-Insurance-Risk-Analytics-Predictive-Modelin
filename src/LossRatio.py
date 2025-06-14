import pandas as pd

# === Function to calculate overall loss ratio ===
def calculate_overall_loss_ratio(df, claims_col='TotalClaims', premium_col='TotalPremium'):
    total_claims = df[claims_col].sum()
    total_premium = df[premium_col].sum()
    if total_premium == 0:
        return None
    return round(total_claims / total_premium, 4)

# === Function to calculate loss ratio by category (e.g., Province, Gender) ===
def calculate_loss_ratio_by_category(df, category, claims_col='TotalClaims', premium_col='TotalPremium'):
    grouped = df.groupby(category)[[claims_col, premium_col]].sum()
    grouped['LossRatio'] = grouped[claims_col] / grouped[premium_col]
    return grouped[['LossRatio']].sort_values('LossRatio', ascending=False)

# === Optional: Function to print summary ===
def summarize_loss_ratios(df, categories, claims_col='TotalClaims', premium_col='TotalPremium'):
    print(f"✅ Overall Loss Ratio: {calculate_overall_loss_ratio(df, claims_col, premium_col)}\n")
    for cat in categories:
        print(f"🔹 Loss Ratio by {cat}:\n")
        print(calculate_loss_ratio_by_category(df, cat, claims_col, premium_col))
        print("\n" + "="*60 + "\n")
import seaborn as sns
import matplotlib.pyplot as plt

def plot_loss_ratio_by_category(df, category, claims_col='TotalClaims', premium_col='TotalPremium'):
    # Calculate loss ratio
    grouped = df.groupby(category)[[claims_col, premium_col]].sum()
    grouped['LossRatio'] = grouped[claims_col] / grouped[premium_col]
    grouped = grouped.sort_values('LossRatio', ascending=False).reset_index()
    
    # Set up plot style
    plt.figure(figsize=(10, 6))
    sns.barplot(data=grouped, x='LossRatio', y=category, palette='coolwarm')

    # Labels and title
    plt.title(f'Loss Ratio by {category}', fontsize=14)
    plt.xlabel('Loss Ratio')
    plt.ylabel(category)
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
# --- New modular function to analyze vehicle model loss ratios ---
def analyze_loss_ratio_for_models(df, model_list, model_col='Model', claims_col='TotalClaims', premium_col='TotalPremium'):
    """
    Filters the dataframe to the selected model list, calculates and plots the loss ratio.

    Parameters:
    - df: Full DataFrame
    - model_list: List of model names to filter
    - model_col: Column name for vehicle model (default: 'Model')
    - claims_col: Column name for total claims (default: 'TotalClaims')
    - premium_col: Column name for total premium (default: 'TotalPremium')
    """
    filtered_df = df[df[model_col].isin(model_list)].copy()

    print(f"✅ Overall Loss Ratio for selected models: {calculate_overall_loss_ratio(filtered_df, claims_col, premium_col)}\n")
    print("🔍 Loss Ratio by Model:")
    print(calculate_loss_ratio_by_category(filtered_df, model_col, claims_col, premium_col))

    plot_loss_ratio_by_category(filtered_df, model_col, claims_col, premium_col)