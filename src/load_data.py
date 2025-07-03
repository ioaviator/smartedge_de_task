import os
import sys

import pandas as pd


def load_data(file_path: str, logger) -> pd.DataFrame:
    """
    Load data from a CSV file using pandas.

    Args:
        file_path (str): Path to the dataset file (.csv ).
        logger (Logger): Logger for logging messages.

    Returns:
        pd.DataFrame: pandas DataFrame.

    Raises:
        FileNotFoundError: If the file does not exist.
    """

    if not os.path.exists(file_path):
      logger.error(f"File not found: {file_path}")
      raise FileNotFoundError(f"Error: File not found -> {file_path}")

    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
          logger.error("Unsupported file format. Use .csv or .json")
          sys.exit(f"Error: Unsupported file format.Check the logs")

        logger.info(f"Loaded file: {file_path} with shape {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
