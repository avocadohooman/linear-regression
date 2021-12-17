import csv
from io import TextIOWrapper
import math
from csv import reader, writer
import sys
import os
from utils import printList, calculateMean, createRealValueGraph, createNormalizedGraph

# Here we prompt the user to provide the filne name of the data set for training the model
# The file needs to be located in ./data
def getCsvFileName() -> str:
	while 1:
		print("Please enter the data set <name.csv> for training located in ./data")
		try:
			csvFile = input()
			if (csvFile):
					break
		except EOFError:
			sys.exit('EOF on input. Exit...')
		except:
			sys.exit('EOF on input. Exit...')
	return csvFile

# Here we parse the CSV file and store the data 
# In case the file doesn't exist we throw an error
def parseCsvFile(filename:str) -> list:
	dataset = list()
	try:
		file: TextIOWrapper = open(filename, "r")
		with file:
			lines = reader(file)
			for row in lines:
				if not row:
					continue
				dataset.append(row)
			if len(dataset[0]) == 2:
				print('Loaded dataset {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
				return dataset
			sys.exit('Error: dataset needs to have exactly 2 colummns')
	except OSError:
		sys.exit('Could not open/find file: {0}'.format(filename))

# Converting string values to floats and removing any whitespaces with strip()
def convertStrToFloat(dataset:list, column: int):
	for row in dataset:
			row[column] = float(row[column].strip())

# remove any non digit rows from the dataset
def removeNonDigitValues(dataset: list) -> list:
	for idx, row in enumerate(dataset):
		if row[0].strip().isdigit() == False or row[1].strip().isdigit() == False:
			dataset.pop(idx)
	return dataset

# get min and max value for each column of the dataset
def getMinMax(dataset:list) -> list:
	minmax = list()
	for i in range(len(dataset[0])):
		columnValue = [row[i] for row in dataset]
		valueMin = min(columnValue)
		valueMax = max(columnValue)
		minmax.append([valueMin, valueMax])
	return minmax

# normalizing data with the equation normalizedValue = value - min / max - min
# here we normaize data between the range 0 - 1
def normalizeData(dataset: list, minmax: list):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# here we get the current yhat value with the current beta0 and beta1 coefficient
def predict(row, beta0, beta1):
	yhat = beta0
	for i in range(len(row)-1):
		yhat += beta1 * row[i]
	return yhat

# this gradientdecent algorithm estimates the linear regression coefficients beta0 and beta1
# the basic equation we are using for estimating the coefficient is:
# b(coefficent) = b - learning rate(configured learning rate) * error(prediction error) * inputValue
# error = yhat(prediction) - expected_value_i
# b0(t+1) = b0 - learning rate * error
# b1(t+1) = b1 - learning rate * error * input_value_i
def gradientDecent(train, learningRate, numberEpoche):
	beta0 = 0.0
	beta1 = 0.0
	for epoch in range(numberEpoche):
		sumError = 0
		for row in train:
			predictedValue = predict(row, beta0, beta1)
			error = predictedValue - row[-1]
			sumError += error ** 2
			beta0 = beta0 - learningRate * error
			for i in range(len(row)-1):
				beta1 = beta1 - learningRate * error * row[i]
		print('>>>>>epoch=%d, learningRate=%.3f, error=%.3f' % (epoch, learningRate, sumError))
	return beta0, beta1

def saveCoefficient(tbeta0, tbeta1, minmax, file):
	with open(file, 'w') as csvFile:
		csvWriter = writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csvWriter.writerow([tbeta0, tbeta1])
		csvWriter.writerows(minmax)

def main():
	csvFile:str
	csvFile = getCsvFileName()
	csvFilePath = './data/' + csvFile
	dataset:list = parseCsvFile(csvFilePath)
	filtereDataSet = removeNonDigitValues(dataset)
	for i in range(len(filtereDataSet[0])):
		convertStrToFloat(filtereDataSet, i)
	minmax:list = getMinMax(filtereDataSet)
	normalizeData(filtereDataSet, minmax)
	tbeta0 = 0.0
	tbeta1 = 0.0
	tbeta0, tbeta1 = gradientDecent(filtereDataSet, 0.01, 500)
	fileName = './coefficients/b0b1.csv'
	print('tbeta0, tbeta1', tbeta0, tbeta1)
	createRealValueGraph(csvFile, tbeta0, tbeta1)
	createNormalizedGraph(filtereDataSet, csvFile, tbeta0, tbeta1)
	saveCoefficient(tbeta0, tbeta1, minmax, fileName)

if __name__ == "__main__":
	main()

