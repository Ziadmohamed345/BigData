from dpre import df
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



#sns.histplot(df['Survived'], bins=5, kde=True, color='skyblue', edgecolor='black')
#sns.countplot(df['Survived'])
sns.countplot( x='Survived', data =df)
#plt.title('Distribution of Survivals')
#plt.xlabel('Survived')
#plt.ylabel('Frequency')
plt.show()

# Save the plot as a PNG file
plt.savefig('vis.png')


