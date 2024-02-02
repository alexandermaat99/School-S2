# mlr multiple linear regression, mx+mx+mx+b mx is now called beta coefficient
# 1 effect size (overall model effect size r2)(mae, rmse)
# (individual feature effect size)(beta coefficient)

import pandas as pd 
import statsmodels.api as sm

df= pd.read_csv('/Users/alexandermaat/Downloads/insurance.csv')
# print(df.head())
# only numeric values
# dummy coding for region
# print(df.corr(numeric_only=True))
print("")
print("")

y=df['charges']
# manual process of selecting features
X =df[['age','bmi','children']]
# more dynamic way of selecting features
# fix uncentered 
X  = df.select_dtypes(['number']).assign(const=1)
#  drop the target variable
X.drop(columns=['charges'], inplace=True)
# print(x.head())

# ols is one algorython for mlr
model =sm.OLS(y,X)
results = model.fit()
# print(results.summary())

# goal is highest rsquared with fewest features 
# deviance between adjusted r suqared and r squared is bad 
# coef is the measure of effect size for individual features (beta coefficient)
# 239.9945  for every year older i get, i cost 239.9945 
# 332.0834 for every unit of bmi i get, i cost 332.0834
# t and p tell us how much we can rely on this number, if p is less than .05 then we can rely on it
# lower p value is more reliable 

# reliability, or statistical significance, is the t and p value 

# print(results.predict([44, 18, 3, 1]))

#   ---------------------  ----------------------

df= pd.read_csv('/Users/alexandermaat/Downloads/insurance.csv')
# manual dummy coding
df = pd.get_dummies(df, columns=['sex', 'smoker', 'region'],drop_first=True)
# drop one column from each dummy variable to avoid multicollinearity

# more dynamic 
df = pd.get_dummies(df, columns=df.select_dtypes(['object']).columns,drop_first=True)
print(df.head())

df = df * 1
y = df['charges']
x = df.drop(columns=['charges'])
print(sm.OLS(y, X.assign(const=1)).fit().summary())
