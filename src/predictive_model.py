import pandas as pd
import numpy as np
import re

def extract_excess(value):
    if isinstance(value, str):
        if 'No excess' in value:
            return 0
        match = re.search(r'R\s?(\d[\d\s]*)', value)
        if match:
            return int(match.group(1).replace(' ', ''))  # Clean spaces like "10 000"
    return np.nan  # Return NaN for unknowns or nulls