import matplotlib.pyplot as plt
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

# Printing a scatter graph of current data set in ./graph folder 
def createScatterGraph(dataSet: list, dataSetName: str):
	data = pd.read_csv('./data/{0}'.format(dataSetName))
	graphName = dataSetName.split('.')
	columnOne = dataSet[0][0]
	columnTwo = dataSet[0][1]
	x = data[columnOne]
	y = data[columnTwo]
	plt.scatter(x, y)
	plt.savefig('./graphs/{0}.png'.format(graphName[0]))
