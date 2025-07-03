
def check_data_types(df, logger):
    # print(df.dtypes)
    dtype_report = {col: str(dtype) for col, dtype in df.dtypes.items()}
    logger.info(f"Data types: {dtype_report}")
    return dtype_report
