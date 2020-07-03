#! /usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'exec(%matplotlib inline)'

from sklearn.datasets import load_iris
iris = load_iris()
print('Features: ', iris.feature_names)
print('Label: ', iris.target_names, type(iris.target_names))
df = pd.DataFrame(np.column_stack([iris.data, iris.target]),
		columns=iris.feature_names + ['label'])

print('a) How many columns, rows')
dim = df.shape
print('No of rows: {}'.format(dim[0]))		# 150 rows
print('No of columns: {}'.format(dim[1]))	# 5 columns
print('Column names: {}'.format(list(df.columns)))	#['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'label']
print('')

print('b)')
print('min,max petal_length of all samples')
wk1 = df['petal length (cm)']
print('\tMin val: {}'.format(min(wk1)))		# 1.0
print('\tMax val: {}'.format(max(wk1)))		# 6.9
print('')

print('min,max petal_lenth of setosa samples')
target_dict = {iris.target_names[i]: i for i in range(len(iris.target_names))}
wk2 = df.loc[df.label == target_dict['setosa'], 'petal length (cm)']
print('\tMin val: {}'.format(min(wk2)))		# 1.0
print('\tMax val: {}'.format(max(wk2)))		# 1.9
print('')

print('c) Plot histogram')
print('... all samples')
plt.hist(wk1)
plt.show()
print('... setosa samples')
plt.hist(wk2)
plt.show()
print('')

print('d) Plot scatter plot of sepal_length and sepal_width')
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'])
plt.show()
