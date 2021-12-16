from io import TextIOWrapper
import math
from csv import reader
import sys
import os
from utils import printList, calculateMean

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
			print('Loaded dataset {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
			return dataset
	except OSError:
		print('Could not open/find file: ', filename)

# Converting string values to floats and removing any whitespaces with strip()
def convertStrToFloat(dataset:list, column: int):
	for row in dataset:
			row[column] = float(row[column].strip())

# remove any non digit rows from the dataset
def removeNonDigitValues(dataset: list) -> list:
	for idx, row in enumerate(dataset):
		if row[0].isdigit() == False or row[1].isdigit() == False:
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

# normalize data with the equation normalizedValue = value - min / max - min
# here we normaize data between the rane 0 - 1
def normalizeData(dataset: list, minmax: list):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

def main():
	csvFile:str = './data/'
	csvFile += getCsvFileName()
	dataset = parseCsvFile(csvFile)
	dataset = removeNonDigitValues(dataset)
	for i in range(len(dataset[0])):
		convertStrToFloat(dataset, i)
	minmax = getMinMax(dataset)
	normalizeData(dataset, minmax)
	means = calculateMean(dataset)

if __name__ == "__main__":
	main()
