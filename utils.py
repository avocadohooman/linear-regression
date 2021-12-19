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

# Printing a real value scatter graph of current data set in ./graph folder 
def createRealValueGraph(dataSetName: str, beta0, beta1):
	dataReal = pd.read_csv('./data/{0}'.format(dataSetName))
	graphName = dataSetName.split('.')
	xReal = dataReal[dataReal.columns[0]]
	yReal = dataReal[dataReal.columns[1]]
	plt.scatter(xReal, yReal)
	plt.title('Real values')
	plt.xlabel('Km')
	plt.ylabel('Price')
	# plt.plot(xReal, beta0 + beta1 * xReal, 'r')
	plt.savefig('./graphs/{0}_real.png'.format(graphName[0]))
	plt.clf()

def createNormalizedGraph(dataSetName: str, beta0, beta1):
	dataReal = pd.read_csv('./data/{0}'.format(dataSetName))
	graphName = dataSetName.split('.')
	xNorm = dataReal[dataReal.columns[0]]
	yNorm = dataReal[dataReal.columns[1]]
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

