from load import df
import pandas as pd

# Data Cleaning
# Fill in missing values
df.fillna(0, inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Data Transformation
# Convert categorical variables to numerical
df = pd.get_dummies(df, columns=['Sex'])

# Data Reduction


# Data Discretization
# Convert continuous variables to categorical
df['age_group'] = pd.cut(df['Age'], bins=[0, 18, 30, 50, 100], labels=['0-18', '18-30', '30-50', '50+'])

# Save the resulting data frame as a new CSV file
df.to_csv('res_dpre.csv', index=False)