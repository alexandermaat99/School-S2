import pandas as pd 
import statsmodels.api as sm

df= pd.read_csv('/Users/alexandermaat/Downloads/insurance.csv')
df = pd.get_dummies(df, columns=df.select_dtypes(['object']).columns,drop_first=True)
# print(df.head())

df = df * 1

y = df.charges
X = df.drop(columns=['charges']).assign(const=1)
model = sm.OLS(y, X).fit()
# print(model.summary())



from sklearn import preprocessing

df_zscore = pd.DataFrame(preprocessing.StandardScaler().fit_transform(df), columns=df.columns)
# print(df_zscore.head())

df_minMax = pd.DataFrame(preprocessing.MinMaxScaler().fit_transform(df), columns=df.columns)
# print(df_minMax.head())

y = df_zscore.charges
X = df_zscore.drop(columns=['charges']).assign(const=1)
model = sm.OLS(y, X).fit()
# print(model.summary())
# coef furtherst from zero is most important most impact

import numpy as np

df2 = df.copy()
df2['charges_sqrt'] = df2['charges']**.5
df2['charges_cbrt'] = df2['charges']**(1/3)
df2['charges_ln'] = np.log(df2['charges'])
# print(df2.head())   

import seaborn as sns 
import matplotlib.pyplot as plt

# print(df2['charges'].skew())
# print(df2['charges_sqrt'].skew())
# print(df2['charges_cbrt'].skew())
# print(df2['charges_ln'].skew())

# pich whichever one gets us closest to zero skew, most natural curve 
sns.histplot(df2, x='charges')
# plt.show()

sns.histplot(df2, x='charges_sqrt')
# plt.show()

sns.histplot(df2, x='charges_cbrt')
# plt.show()

# best natural curve
sns.histplot(df2, x='charges_ln')
# plt.show()

# r squared us way better of a match, and const is a normal number
y = df2.charges_ln
X = df2.drop(columns=['charges', 'charges_ln', 'charges_sqrt', 'charges_cbrt']).assign(const=1)
model = sm.OLS(y, X).fit()
# print(model.summary())

# now we have to reverse natural log to get back to original scale
# dollar amount is the original scale of the y intercept 
# print(np.exp(7.0306))


#  ---------------------  ----------------------
# RMSC and MAE for prediction 

y = df.charges
X = df.drop(columns=['charges']).assign(const=1)
model = sm.OLS(y, X).fit()


df2['Predicted'] = model.fittedvalues
# shows error
df2['Residual'] = abs(df2['charges'] - df2['Predicted'])
df2['Squared Residual'] = (df2['charges'] - df2['Predicted'])**2
print('')
print(f"Mean Absolute Error: {df2.Residual.mean()}")
print(f"Root Mean Squared Error: {df2['Squared Residual'].mean() ** .5}")
print('')
# change to absolute value then average out

print(df2.head())


