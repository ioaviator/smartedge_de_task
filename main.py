import argparse

from check_data_type import check_data_types
from check_null import check_nulls
from config import logger
from load_data import load_data


def main(filepath):
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