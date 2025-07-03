
def check_data_types(df, logger) -> dict[str, str]:
    """
    Check data types of each column.

    Args:
        df (pd.DataFrame): The DataFrame to inspect.
        logger (Logger): Logger for logging messages.

    Returns:
        dict[str, str]: Column names and their data types.
    """
    
    # print(df.dtypes)
    dtype_report = {col: str(dtype) for col, dtype in df.dtypes.items()}
    logger.info(f"Data types: {dtype_report}")
    return dtype_report
