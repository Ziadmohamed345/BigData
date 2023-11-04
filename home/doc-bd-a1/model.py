from dpre import df
import pandas as pd
from sklearn.cluster import KMeans
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import StandardScaler
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.metrics import accuracy_score



# Select the columns for K-means
X = df[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']]

# Perform K-means clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Get the number of records in each cluster
counts = pd.Series(kmeans.labels_).value_counts()

# Save the counts to a text file
with open('k.txt', 'w') as f:
    for i in range(len(counts)):
        f.write(f'Cluster {i}: {counts[i]} records\n')

