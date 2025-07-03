import argparse

from load_data import load_data


def main(filepath):
  df = load_data(filepath)
  

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Data Quality Checker")
  parser.add_argument('--file', required=True, help="Path to CSV or JSON file")
  args = parser.parse_args()

  main(args.file)