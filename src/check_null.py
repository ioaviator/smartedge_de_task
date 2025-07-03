
def check_nulls(df, logger) -> dict[str, int]:
    """
    Check for null values in the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to check for nulls.
        logger (Logger): Logger for logging messages.

    Returns:
        dict[str, int]: Columns with count of null values.
    """

    null_values = df.isnull().sum()
    # print(null_values.items())
    null_report = {col: count 
                   for col, count in null_values.items() 
                   if count > 0}
    
    logger.info(f"Null values found: {null_report}")
    return null_report