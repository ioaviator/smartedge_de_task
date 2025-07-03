import os
import sys

import pandas as pd

from config import logger


def load_data(file_path):
    if not os.path.exists(file_path):
      logger.error(f"File not found: {file_path}")
      sys.exit(f"Error: File not found -> {file_path}")

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
