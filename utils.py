import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Nice way of printing a list
def printList(label: str, list: list):
	if label:
		print(label)
	for row in list:
		print(row)

# Calculate mean value of a column in a dataset
def calculateMean(dataset: list) -> list:
	means = [0 for i in range(len(dataset[0]))]
	for i in range(len(means)):
		columnValue = [row[i] for row in dataset]
		means[i] = sum(columnValue) / float(len(dataset))
	return means

def createNormalizedGraph(dataSetName: str, beta0, beta1):
	dataNorm = pd.read_csv('./data/{0}'.format(dataSetName))
	graphName = dataSetName.split('.')
	xNorm = dataNorm[dataNorm.columns[0]]
	yNorm = dataNorm[dataNorm.columns[1]]
	plt.title('Normalized values')
	plt.xlabel('Km')
	plt.ylabel('Price')
	plt.scatter(xNorm, yNorm)
	plt.plot(xNorm, beta0 + beta1 * xNorm, 'r')
	plt.savefig('./graphs/{0}.png'.format(graphName[0]))
	plt.clf()

def normalizeElemt(min, max, inputValue):
	return ((float(inputValue) - float(min)) / (float(max) - float(min)))

def	denormalizeElem(min, max, predictedValue):
	return ((float(predictedValue) * (float(max) - float(min))) + float(min))

