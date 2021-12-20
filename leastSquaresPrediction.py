from math import sqrt
import pandas as pd
import matplotlib.pyplot as plt
import sys

## We will use a simple linear regression model as we have linear realtionship between two data points, of which both are known.
## The formula for the simple regression model: y(estimate y) = beta0(interceptor) * beta1(slope) * x(km)

# Simple prediction function
def predict(km, beta0, beta1):
    predictedPrice = beta0 + beta1*km
    return predictedPrice

def getData():
	data = pd.read_csv('./data/data.csv')
	return data

def getColumnValues(data):
	x = data.km
	y = data.price
	return (x, y)

# To get bet0, the slope, we need to first calculate the SumOfSquare of x and the SumOfSquare of y
# beta1 = SSxx/SSxy
# variance: SSxx = SumOf((mean)x - x)^2 
def calculateVariance(data, x):
	kmMean = x.mean()
	data['kmMean'] = kmMean
	data['diffkm'] = kmMean - x
	data['diffkmSquared'] = data.diffkm ** 2
	SSxx = data.diffkmSquared.sum()
	return SSxx

# covariance: SSxy = SumOf((mean)x - x) * ((mean)y - y)
def calculateCovariance(data, y):
	priceMean = y.mean()
	data['priceMean'] = priceMean
	data['diffPrice'] = priceMean - y
	SSxy = (data.diffkm * data.diffPrice).sum()
	return SSxy

def createRealValueGraph(dataSetName: str):
	dataReal = pd.read_csv('./data/{0}'.format(dataSetName))
	x, y = getColumnValues(dataReal)
	graphName = dataSetName.split('.')
	variance = calculateVariance(dataReal, x)
	covariance = calculateCovariance(dataReal, y)
	## Calculating the Slope = beta1 = covariance/variance
	beta1 = covariance / variance
	## Calculating the interceptor: beta0 = (mean)y - beta1*(mean)x
	beta0 = y.mean() - beta1*x.mean()
	plt.title('Real values')
	plt.xlabel('Km')
	plt.ylabel('Price')
	plt.scatter(x, y)
	plt.plot(x, beta0 + beta1*x, 'r')
	plt.savefig('./graphs/{0}_real.png'.format(graphName[0]))
	plt.clf()

def addPredictions(x, beta0, beta1):
	predictedPrice = list()
	for row in x:
		predictedPrice.append(float(predict(row, beta0, beta1)))
	return predictedPrice

# RMSE is calculated as the square root of the mean of the squared differences between actual outcomes and predictions.
# Squaring each error forces the values to be positive, 
# and the square root of the mean squared error returns the error metric back to the original units for comparison.
def calculateRMSEAccuracy(actualPrices, predictedPrices):
	sum_error = 0.0
	for i in range(len(actualPrices)):
		prediction_error =  predictedPrices[i] - actualPrices[i]
		sum_error += (prediction_error ** 2)
	mean_error = sum_error / float(len(predictedPrices))
	return sqrt(mean_error)

def main():
	## Here we check if the arguments given are exactly 2, if not show usage
	if (len(sys.argv) != 2 or sys.argv[1].isdigit() == False):
		print('Usage: python3 simpleLinearRegression.py <km>')

	## If we got 2 arguments, we take the 
	if (len(sys.argv) == 2 and sys.argv[1].isdigit() == True):
		data = getData()
		x, y = getColumnValues(data)
		variance = calculateVariance(data, x)
		covariance = calculateCovariance(data, y)
		## Calculating the Slope = beta1 = covariance/variance
		beta1 = covariance / variance
		## Calculating the interceptor: beta0 = (mean)y - beta1*(mean)x
		beta0 = y.mean() - beta1*x.mean()
		print('beta0, beta1', beta0, beta1)
		km = float(sys.argv[1])
		print('predictedPrice', int(predict(km, beta0, beta1)))
		predictedPrices = addPredictions(x, beta0, beta1)
		rootMeanSquareError = calculateRMSEAccuracy(y, predictedPrices)
		print('RMSE: %.3f' % (rootMeanSquareError))
		plt.title('Real values')
		plt.xlabel('Km')
		plt.ylabel('Price')
		plt.scatter(x, y)
		plt.plot(x, beta0 + beta1*x, 'r')
		plt.savefig('./graphs/simpleLinearRegressionModel.png')

if __name__ == "__main__":
	main()