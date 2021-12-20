from math import sqrt
from leastSquaresPrediction import getData, getColumnValues
from trainedGradientDescentPrediction import getTrainedCoeffiecients, predict
from utils import normalizeElemt, denormalizeElem, printList
from trainModel import parseCsvFile

def addPredictions(coeff,minMaxX,minMaxY,km):
	predictedPrice = list()
	for row in km:
		predictedPrice.append(float(predict(coeff,minMaxX,minMaxY, int(row))))
	return predictedPrice

# RMSE is calculated as the square root of the mean of the squared differences between actual outcomes and predictions.
# Squaring each error forces the values to be positive, 
# and the square root of the mean squared error returns the error metric back to the original units for comparison.
def calculateRMSEAccuracy(actualPrices, predictedPrices, minMaxY):
	sum_error = 0.0
	for i in range(len(actualPrices)):
		# prediction_error = normalizeElemt(minMaxY[0][0], minMaxY[0][1], predictedPrices[i]) - normalizeElemt(minMaxY[0][0], minMaxY[0][1], float(actualPrices[i]))
		prediction_error =  predictedPrices[i] - actualPrices[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(predictedPrices))
	return sqrt(mean_error)

# A quick way to evaluate a set of predictions on a classification problem is by using accuracy. 
# Classification accuracy is a ratio of the number of correct predictions out of all predictions that were made. 
# It is often presented as a percentage between 0% for the worst possible accuracy and 100% for the best possible accuracy.
def calculateClassificationAccuracy(actualPrices, predictedPrices):
	correct = 0
	for i in range(len(actualPrices)):
		if (actualPrices[i] == predictedPrices[i]):
			correct += 1
	classificationAccuracy = correct / float(len(actualPrices)) * 100
	return classificationAccuracy

def main():
	data = getData()
	km, actualPrices = getColumnValues(data)
	coeff,minMaxX,minMaxY = getTrainedCoeffiecients()
	predictedPrices = addPredictions(coeff,minMaxX,minMaxY,km)
	classificationAccuracy = calculateClassificationAccuracy(actualPrices, predictedPrices)
	rootMeanSquareError = calculateRMSEAccuracy(actualPrices, predictedPrices, minMaxY)
	print('classificationAccuracy', classificationAccuracy)
	print('RMSE: %.3f' % (rootMeanSquareError))


if __name__ == "__main__":
	main()