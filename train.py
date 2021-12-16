from io import TextIOWrapper
import math
from csv import reader
import sys
import os

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
def convertStrToFloat(dataset, column):
	for idx, row in enumerate(dataset):
		if idx == 0:
			continue
		else:
			row[column] = float(row[column].strip())

def main():
	csvFile:str = './data/'
	csvFile += getCsvFileName()
	dataset = parseCsvFile(csvFile)
	for i in range(len(dataset[0])):
		convertStrToFloat(dataset, i)

if __name__ == "__main__":
	main()