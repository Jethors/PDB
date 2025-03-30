import pandas as pd

def read_excel_column(file_path, column_index=1):
    """Reads an Excel file and returns a list of values from the specified column index."""
    try:
        df = pd.read_excel(file_path)
        return df.iloc[:, column_index].tolist()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []
