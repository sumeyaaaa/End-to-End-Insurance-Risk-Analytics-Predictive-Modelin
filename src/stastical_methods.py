from scipy.stats import chi2_contingency
import pandas as pd

def run_chi_squared_test(df, group_col, outcome_col='HasClaim'):
    """
    Run a chi-squared test between a categorical grouping column (e.g., Province)
    and a binary outcome column (e.g., HasClaim).
    
    Parameters:
        df (pd.DataFrame): The dataset
        group_col (str): Column name to group by (e.g., 'Province', 'Gender', 'PostalCode')
        outcome_col (str): Binary target column (default is 'HasClaim')
    
    Returns:
        dict: {
            'group_col': column name used for grouping,
            'chi2': test statistic,
            'p_value': p-value,
            'dof': degrees of freedom,
            'contingency_table': the actual table used
        }
    """
    # Create contingency table
    contingency = pd.crosstab(df[group_col], df[outcome_col])
    
    # Perform test
    chi2, p_val, dof, expected = chi2_contingency(contingency)

    return {
        'group_col': group_col,
        'chi2': chi2,
        'p_value': p_val,
        'dof': dof,
        'contingency_table': contingency
    }
from scipy.stats import f_oneway
import pandas as pd

def run_anova_test(df, group_col, value_col, condition_col=None, condition_value=True):
    """
    Run one-way ANOVA for a continuous variable across categories of a grouping column.
    
    Parameters:
        df (pd.DataFrame): The dataset.
        group_col (str): Categorical column to group by (e.g., 'Province', 'PostalCode').
        value_col (str): Continuous variable to compare (e.g., 'TotalClaims', 'Margin').
        condition_col (str): Optional filter column (e.g., 'HasClaim').
        condition_value (bool or any): Value to filter by in condition_col.
    
    Returns:
        dict: {
            'group_col': group_col,
            'value_col': value_col,
            'f_statistic': float,
            'p_value': float,
            'group_count': int
        }
    """
    # Optional filter (e.g., only rows where HasClaim == True)
    if condition_col:
        df = df[df[condition_col] == condition_value]

    # Drop NA in the value column
    df = df[[group_col, value_col]].dropna()

    # Group data
    groups = [
        group[value_col].values
        for _, group in df.groupby(group_col)
        if len(group[value_col]) > 1  # skip groups with 1 value
    ]

    if len(groups) < 2:
        return {
            'group_col': group_col,
            'value_col': value_col,
            'f_statistic': None,
            'p_value': None,
            'group_count': len(groups),
            'note': 'Not enough groups with sufficient data to run ANOVA'
        }

    # Run ANOVA
    f_stat, p_val = f_oneway(*groups)

    return {
        'group_col': group_col,
        'value_col': value_col,
        'f_statistic': f_stat,
        'p_value': p_val,
        'group_count': len(groups)
    }
def run_margin_anova(df, group_col):
    """
    Computes Margin (TotalPremium - TotalClaims) and runs ANOVA across the given group column.
    
    Parameters:
        df (pd.DataFrame): Dataset
        group_col (str): Column to group by (e.g., 'Province', 'PostalCode', 'Gender')
    
    Returns:
        dict: ANOVA results including F-statistic and p-value
    """
    # Ensure margin column exists
    if 'Margin' not in df.columns:
        df['Margin'] = df['TotalPremium'] - df['TotalClaims']
    
    # Drop rows with missing values in relevant columns
    df_filtered = df[[group_col, 'Margin']].dropna()

    # Group values for ANOVA
    groups = [
        group['Margin'].values
        for _, group in df_filtered.groupby(group_col)
        if len(group['Margin']) > 1
    ]

    if len(groups) < 2:
        return {
            'group_col': group_col,
            'value_col': 'Margin',
            'f_statistic': None,
            'p_value': None,
            'group_count': len(groups),
            'note': 'Not enough data to perform ANOVA'
        }

    f_stat, p_val = f_oneway(*groups)

    return {
        'group_col': group_col,
        'value_col': 'Margin',
        'f_statistic': f_stat,
        'p_value': p_val,
        'group_count': len(groups)
    }
