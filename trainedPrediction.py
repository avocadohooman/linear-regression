import pandas as pd
import matplotlib.pyplot as plt
import sys
from csv import reader

# Get user input
def getUserInput():
	while 1:
		print("Please enter a value for the prediction")
		try:
			value = input()
			if (value):
				break 
		except EOFError:
			sys.exit('Error on Input. Exit..')
		except:
			sys.exit('Error on Input. Exit...')
	return float(value)

def getTrainedCoeffiecients():
	b0, b1 = 0, 0
	try:
		file = open('./coefficients/b0b1.csv', "r")
		with file:
			lines = reader(file)
			for row in lines:
				if not row:
					continue
				b0 = float(row[0])
				b1 = float(row[1])
	except OSError:
		sys.exit('Could not load latest beta0, beta1 values. Exit...')
	return (b0,b1)

# Simple prediction function
def predict(b0, b1, predictionValue):
    predictedPrice = b0 + b1*predictionValue
    return predictedPrice

def main():
	predictionValue = getUserInput()
	b0, b1 = getTrainedCoeffiecients()
	print('predictedPrice', predict(b0, b1, predictionValue))

if __name__ == "__main__":
	main()