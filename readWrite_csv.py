import csv
import os
import pandas as pd


def write_csv(filename="output.csv",data_list=None, directory="files"):
    """Writes a list of items to a CSV file in the specified directory.

    - Defaults:
      - `filename`: "output.csv"
      - `directory`: "files" (relative to working directory)
    - `data_list`: List of items to write (one per row).
    """
    if data_list is None:
        data_list = []

    # Ensure directory exists
    os.makedirs(directory, exist_ok=True)

    # Create full file path
    file_path = os.path.join(directory, filename)
    full_path = os.path.abspath(file_path)

    try:
        with open(full_path, "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for item in data_list:
                writer.writerow([item])
        print(f"✅ CSV file saved at: {full_path}")
    except Exception as e:
        print(f"❌ Error writing CSV: {e}")


def read_csv(filename="input.csv", directory="files"):
    """Reads a CSV file from the specified directory and returns the first column as a list."""
    file_path = os.path.join(directory, filename)
    full_path = os.path.abspath(file_path)

    try:
        df = pd.read_csv(full_path, header=None)
        print(f"📂 Read CSV from: {full_path}")
        return df[0].tolist()  # Return first column as a list
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return None  # Return None if reading fails
