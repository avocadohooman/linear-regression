import pandas as pd
import matplotlib.pyplot as plt
import sys
from csv import reader
from utils import normalizeElemt, denormalizeElem

# Get user input
def getUserInput():
	while 1:
		print("Please enter a value for the prediction")
		try:
			value = input()
			if (int(value) >= 0):
				break 
			else:
				print('Not a valid value for the prediction model. Needs to be >= 0')
		except ValueError:
			print('Not a valid value for the prediction model. Needs to be >= 0')
		except EOFError:
			sys.exit('Error on Input. Exit..')
		except:
			sys.exit('Error on Input. Exit...')
	return float(value)

# Here we are loading the latest value for the coeffiecients beta0 and beta1
# which have been trained with trainModel.py
def getTrainedCoeffiecients():
	coeff = list()
	minMaxX = list()
	minMaxY = list()
	try:
		file = open('./coefficients/b0b1.csv', "r")
		with file:
			lines = reader(file)
			for idx, row in enumerate(lines):
				if not row:
					continue
				if (idx == 0):
					coeff.append(row)
				elif (idx == 1):
					minMaxX.append(row)
				elif (idx == 2):
					minMaxY.append(row)
	except OSError:
		sys.exit('Could not load latest beta0, beta1 values. Exit...')
	return (coeff,minMaxX,minMaxY)

# Simple linear regression equation
def predict(coeff,minMaxX,minMaxY, inputValue):
	b0 = coeff[0][0]
	b1 = coeff[0][1]
	minX = minMaxX[0][0]
	minY = minMaxY[0][0]
	maxX = minMaxX[0][1]
	maxY = minMaxY[0][1]
	predictedPrice = float(b0) + float(b1)*normalizeElemt(minX, maxX, inputValue)
	return denormalizeElem(minY, maxY, predictedPrice)
def getData():
	data = pd.read_csv('./data/data.csv')
	x = data.km
	y = data.price

def main():
	inputValue = getUserInput()
	coeff = list
	minMaxX = list
	minMaxY = list
	coeff,minMaxX,minMaxY = getTrainedCoeffiecients()
	print('predictedPrice', int(predict(coeff, minMaxX, minMaxY, inputValue)))

if __name__ == "__main__":
	main()