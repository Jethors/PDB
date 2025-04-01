import pandas as pd

def read_excel_column(file_path, column_index=1):
    """Reads an Excel file and returns a list of values from the specified column index defaults to second column.
    Arguments
    file_path: path to the excell file
    column_index: Index of the column in the excell file which should become a list

    Can give full filepath to the excell document or /files/excelllist.xlsx
    """
    try:
        df = pd.read_excel(file_path)  # read document
        return df.iloc[:, column_index].tolist() # return list of selected column
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []
