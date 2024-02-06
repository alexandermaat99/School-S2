# # univariate analysis
def univariate(df):
    
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt


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
            sns.histplot(data=df, x=col)
            plt.show()

        else:
            df_output.loc[col] = ['categorical', missing, 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', df[col].mode()[0], 'NA', 'NA']
            sns.countplot(data=df, x=col)
            plt.show()
        
        return df_output

# def univariate(df):
#     import pandas as pd
#     import seaborn as sns
#     import matplotlib.pyplot as plt

#     df_output = pd.DataFrame(columns=['type', 'missing', 'unique', 'min', 'q1', 'median', 'q3', 'max', 'mean', 'std', 'mode', 'skew', 'kurt'])

#     for col in df:
#         # Calculate values that apply to all types
#         missing = df[col].isna().sum()
#         unique = df[col].nunique()
#         mode = df[col].mode()[0]
#         if pd.api.types.is_numeric_dtype(df[col]):
#             # Calculate values that apply to numbers only
#             min_val = df[col].min()
#             q1 = df[col].quantile(0.25)
#             median = df[col].median()
#             q3 = df[col].quantile(0.75)
#             max_val = df[col].max()
#             mean = df[col].mean()
#             std = df[col].std()
#             skew = df[col].skew()
#             kurt = df[col].kurtosis()
#             df_output.loc[col] = ['numeric', missing, unique, min_val, q1, median, q3, max_val, mean, std, mode, skew, kurt]

#             sns.histplot(data=df, x=col)
#             plt.show()
#         else:
#             df_output.loc[col] = ['categorical', missing, unique, '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
#             sns.countplot(data=df, x=col)
#             plt.show()

#     return df_output

def basic_wrangling(df, unique_threshold=.95, missing_threshold=.5, messages=True):
  import pandas as pd

  # primary keys or too many unique values
  # too much missing data
  # single value columns

  for col in df:
    missing = df[col].isna().sum()
    unique = df[col].nunique()
    rows = df.shape[0]

    if missing / rows >= missing_threshold:
      df.drop(columns=[col], inplace=True)
      if messages: print(f'Column "{col}" dropped because of too much missing data ({round(missing/rows, 2)*100}%)')
    elif unique / rows >= unique_threshold:
      if df[col].dtype in ['object', 'int64']:
        df.drop(columns=[col], inplace=True)
        if messages: print(f'Column "{col}" dropped because of too many unique values ({round(unique/rows, 2)*100}%)')
    elif unique == 1:
      df.drop(columns=[col], inplace=True)
      if messages: print(f'Column "{col}" dropped because it has only one value ({df[col].unique()[0]})')
  return df