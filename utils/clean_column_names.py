#import pandas as pd
import re

def clean_names(name):
    """
    Clean a given name (column or index name) for safe use in databases.
    - Convert to lowercase.
    - Replace spaces and special characters with underscores.
    - Ensure the name does not start with numbers.
    - Handle names that are entirely numeric.
    """
    # Replace spaces and special characters with underscores
    clean_name = re.sub(r'\W+', '_', name)

    # Convert to lowercase
    clean_name = clean_name.upper()

    # Ensure it doesn't start with a number
    if re.match(r'^\d', clean_name):
        clean_name = f'COL_{clean_name}'

    # Handle entirely numeric names
    if clean_name.isdigit():
        clean_name = f'COL_{clean_name}'

    return clean_name

def clean_column_and_index_names(df):
    """
    Clean the column and index names of a pandas DataFrame for safe use in databases.
    """
    # Clean column names
    df.columns = [clean_names(col) for col in df.columns]

    # Clean index name
    if df.index.name:
        df.index.name = clean_names(df.index.name)

    return df

# Example Usage
# df = pd.DataFrame({...}) # Your DataFrame
# df = clean_column_and_index_names(df)
