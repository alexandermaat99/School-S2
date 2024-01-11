# univariate analysis
def univariate(df):
    
    import pandas as pd

    df_output = pd.DataFrame(columns=['type', 'missing','unique', 'min', 'q1', 'median', 'q3', 'max', 'mean', 'std', 'mode', 'skew', 'kurt'])

    for col in df:
        missing = df[col].isna().sum()
        if pd.api.types.is_numeric_dtype(df[col]):
            unique = df[col].nunique()
            min = df[col].min()
            q1 = df[col].quantile(0.25)
            median = df[col].median()
            q3 = df[col].quantile(0.75)
            max = df[col].max()
            mean = df[col].mean()
            std = df[col].std()
            mode = df[col].mode()[0]
            skew = df[col].skew()
            kurt = df[col].kurt()
        
            df_output.loc[col] = ['numeric', missing, unique, min, q1, median, q3, max, mean, std, mode, skew, kurt]
        else:
            df_output.loc[col] = ['categorical', missing, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', df[col].mode()[0], 'NA', 'NA']
        
    print(df_output)

