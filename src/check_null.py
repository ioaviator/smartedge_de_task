
def check_nulls(df,logger):
    null_values = df.isnull().sum()
    # print(null_values.items())
    null_report = {col: count 
                   for col, count in null_values.items() 
                   if count > 0}
    
    logger.info(f"Null values found: {null_report}")
    return null_report