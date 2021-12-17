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

# Simple linear regression equation
def predict(b0, b1, predictionValue):
    predictedPrice = b0 + b1*predictionValue
    return predictedPrice

def main():
	predictionValue = getUserInput()
	b0, b1 = getTrainedCoeffiecients()
	print('predictedPrice', predict(b0, b1, predictionValue))

if __name__ == "__main__":
	main()