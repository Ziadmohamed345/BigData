from load import df
import pandas as pd
import scipy.stats as stats

# Generate descriptive statistics
stats = df.describe()


# Count the number of occurrences of each value in a column
counts = df['SibSp'].value_counts()


contingency_table = pd.crosstab(df['Survived'], df['Age'])


with open('eda-in-1.txt', 'w') as f:
    f.write(stats.to_string() + '\n\n')
    f.write(counts.to_string()+ '\n\n')
    f.write(contingency_table.to_string()+ '\n\n')