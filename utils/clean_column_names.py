#import pandas as pd
import re

def clean_column_names(df):
    """
    Clean the column names of a pandas DataFrame for safe use in databases.
    - Convert to lowercase.
    - Replace spaces and special characters with underscores.
    - Ensure column names do not start with numbers.
    - Handle columns with names that are entirely numeric.
    """
    clean_names = []
    for col in df.columns:
        # Replace spaces and special characters with underscores
        clean_name = re.sub(r'\W+', '_', col)

        # Convert to lowercase
        clean_name = clean_name.upper()

        # Ensure it doesn't start with a number
        if re.match(r'^\d', clean_name):
            clean_name = f'col_{clean_name}'

        # Handle entirely numeric column names
        if clean_name.isdigit():
            clean_name = f'col_{clean_name}'

        clean_names.append(clean_name)

    # Assign cleaned names back to the DataFrame's columns
    df.columns = clean_names

    return df

# Example Usage
# df = pd.DataFrame({...}) # Your DataFrame
# df = clean_column_names(df)
