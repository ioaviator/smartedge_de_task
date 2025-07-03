import argparse

from src.check_data_type import check_data_types
from src.check_null import check_nulls
from src.load_data import load_data
from utils.config import logger


def main(filepath: str) -> None:
  """
    Main function that performs data quality checks and 
    prints results to console

    Args:
        filepath (str): Path to the dataset file.

    Returns:
        None
  """
    
  df = load_data(filepath, logger)
  nulls = check_nulls(df, logger)
  data_type = check_data_types(df, logger)

  print("printing result values to console")

  print("\n Null Values:")  
  print({col: null_count 
         for col, null_count in nulls.items() })

  print("\n Data Types:")
  for col, dtype in data_type.items():
    print(f"{col}: {dtype}")

  return None
  

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Data Quality Checker")
  parser.add_argument('--file', required=True, help="Path to CSV or JSON file")
  args = parser.parse_args()

  main(args.file)