import csv
from io import TextIOWrapper
from csv import reader, writer
import sys
from utils import createNormalizedGraph, printList

# Here we prompt the user to provide the filne name of the data set for training the model
# The file needs to be located in ./data
def getUserInput() -> str:
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
	while 1:
		print("Please enter a desired learning rate between 0 and 1")
		try:
			learningRate = input()
			if (float(learningRate) >= 0 and float(learningRate) <=1):
				break 
			else:
				print('Not a valid value for the learning rate. Needs to be >= 0 AND <= 1')
		except ValueError:
			print('Not a valid value for the learning rate. Needs to be >= 0 AND <= 1')
		except EOFError:
			sys.exit('Error on Input. Exit..')
		except:
			sys.exit('Error on Input. Exit...')
	while 1:
		print("Please enter a number of epoches/cycles > 0")
		try:
			epoche = input()
			if (int(epoche) > 0):
				break 
			else:
				print('Not a valid value for the learning rate. Needs to be >= 0')
		except ValueError:
			print('Not a valid value for the learning rate. Needs to be >= 0')
		except EOFError:
			sys.exit('Error on Input. Exit..')
		except:
			sys.exit('Error on Input. Exit...')
	return (csvFile, float(learningRate), int(epoche))

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
				if len(row) != 2:
					sys.exit('Error: dataset can\'t be empty and needs to have exactly 2 colummns')
				dataset.append(row)
			if len(dataset) > 0 and len(dataset[0]) == 2:
				print('Loaded dataset {0} with {1} rows and {2} columns'.format(filename, len(dataset), len(dataset[0])))
				return dataset
			sys.exit('Error: dataset can\'t be empty and needs to have exactly 2 colummns')
	except OSError:
		sys.exit('Could not open/find file: {0}'.format(filename))

# Converting string values to floats and removing any whitespaces with strip()
def convertStrToFloat(dataset:list, column: int):
	try:
		for row in dataset:
				row[column] = float(row[column].strip())
	except:
		sys.exit('Error: convert str to float failed')

# remove any non digit rows from the dataset
def removeNonDigitValues(dataset: list) -> list:
	try:
		for row in dataset:
			if row[0].strip().isdigit() == False or row[1].strip().isdigit() == False:
				sys.exit('Faulty data set: dataset can only contain numeric values (int or float)')
	except:
		sys.exit('Faulty data set: dataset can only contain numeric values (int or float)')
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
# here we normalize data between the range 0 - 1
def normalizeData(dataset: list, minmax: list):
	for row in dataset:
		for i in range(len(row)):
			if minmax[i][1] == 0 and minmax[i][0] == 0:
				sys.exit('Faulty data: min and max value can\'t be zero')
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

def saveNormalizedData(filtereDataSet, file, columnLabels):
	with open(file, 'w') as csvFile:
		csvWriter = writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csvWriter.writerow(columnLabels)
		csvWriter.writerows(filtereDataSet)

def main():
	csvFile:str
	csvFile, learningRate, epoch = getUserInput()
	csvFilePath = './data/' + csvFile
	dataset:list = parseCsvFile(csvFilePath)
	columnLabels = dataset[0]
	filtereDataSet = removeNonDigitValues(dataset[1:])
	for i in range(len(filtereDataSet[0])):
		convertStrToFloat(filtereDataSet, i)
	minmax:list = getMinMax(filtereDataSet)
	normalizeData(filtereDataSet, minmax)
	tbeta0 = 0.0
	tbeta1 = 0.0
	tbeta0, tbeta1 = gradientDecent(filtereDataSet, float(learningRate), int(epoch))
	fileName = './coefficients/b0b1.csv'
	normalizedFileName = './data/normalized_{0}'.format(csvFile)
	print('tbeta0, tbeta1', tbeta0, tbeta1)
	saveCoefficient(tbeta0, tbeta1, minmax, fileName)
	saveNormalizedData(filtereDataSet, normalizedFileName, columnLabels)
	createNormalizedGraph('normalized_{0}'.format(csvFile), tbeta0, tbeta1)

if __name__ == "__main__":
	main()
