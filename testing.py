import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, linregress

file_path = '/Users/alexandermaat/Desktop/School/NBA/nba_2022-23_all_stats_with_salary.csv'
df = pd.read_csv(file_path)

columns_to_remove = [1, 3, 5]
filtered_df = df.drop(columns=df.columns[columns_to_remove], inplace=False)
filtered_df = filtered_df.dropna()

# Calculate p-values and correlation coefficients
p_values = {}
r_values = {}
for column in filtered_df.columns:
    correlation, p_value = pearsonr(filtered_df[column], filtered_df['Salary'])
    p_values[column] = p_value
    r_values[column] = correlation

# Display correlation coefficients and p-values
# print("\nCorrelation Coefficients:")
# for key, value in r_values.items():
#     print(f"{key}: {value}")

# print("\nP-Values:")
# for key, value in p_values.items():
#     print(f"{key}: {value}")

# Perform linear regression for FieldGoalsAtempted vs. Salary
slope, intercept, r_value, p_value, std_err = linregress(filtered_df['FGA'], filtered_df['Salary'])

# Display regression results
print("\nLinear Regression Results (FieldGoalsAtempted vs. Salary):")
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
print(f"P-value: {p_value}")

# Create scatter plot with linear regression line
plt.figure(figsize=(12, 6))

# Scatter plot
sns.scatterplot(x=filtered_df['FGA'], y=filtered_df['Salary'], label='Data Points')

# Linear regression line
plt.plot(filtered_df['FGA'], slope * filtered_df['FGA'] + intercept, color='red', label='Linear Regression Line')

plt.title('Linear Regression: FieldGoalsAtempted vs. Salary')
plt.xlabel('FieldGoalsAtempted')
plt.ylabel('Salary')
plt.legend()
plt.show()
