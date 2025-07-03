import numpy as np
import pandas as pd
import pytest

from src.check_data_type import check_data_types
from src.check_null import check_nulls
from src.load_data import load_data
from utils.config import logger


def test_load_csv():
    df = load_data("test_files/sample.csv", logger)
    assert not df.empty


def test_null_values():
  df = pd.DataFrame({'a': [1, None, 3], 'b': [None, None, 3]})
  result = check_nulls(df, logger)
  assert result['a'] == 1
  assert result['b'] == 2


def test_data_types():
  df = pd.DataFrame({'id': [1, 2], 'price': ['12.5', '13.5']})
  result = check_data_types(df, logger)

  assert result['id'] == np.dtype('int64')
  assert isinstance(result['price'], object)
