#requiered libreries
import pandas as pd
import numpy as np
#extraccion
wine_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine_data= pd.read_csv(wine_url, header= None)

wine_quality_url= "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine_quality_data= pd.read_csv(wine_quality_url, sep=";")

#initial look at the data
#print(wine_data.head())
#print(wine_quality_data.head())


#transformacion




#loading 
#saving the transformed data as a csv file
wine_data.to_csv('wine_dataset.csv', index=False)
wine_quality_data.to_csv('wine_quality.csv', index=False)

#Assigning meaningful columns names
wine_data.columns=['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavonoids', 'nonflavonoids_phenols', 'proanthocyanidis','color_intensity', 'hue', 'OD280/OD315 of diluted wines', 'proline']

#converting Class column into categorical datatype
wine_data['class'] = wine_data['class'].astype('category')

#Cheking for any missing values in both datasets
print(wine_data.isnull().sum())
print(wine_quality_data.isnull().sum())


#Normalizing 'alcohol' column in the wine_data using min-max normalizacion

wine_data['alcohol']= (wine_data['alcohol']-wine_data['alcohol'].min())/(wine_data['alcohol'].max()-wine_data['alcohol'].min())
wine_data['alcohol'] = wine_data['alcohol'] * 1

# Creating an average quality column in wine_quality_data
wine_quality_data['average_quality'] = wine_quality_data[['fixed acidity', 'volatile acidity', 'citric acid',
                                                          'residual sugar', 'chlorides', 'free sulfur dioxide',
                                                          'total sulfur dioxide', 'density', 'pH', 'sulphates',
                                                          'alcohol']].mean(axis = 1)


