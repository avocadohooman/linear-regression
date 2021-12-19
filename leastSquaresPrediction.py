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
		plt.scatter(x, y)
		plt.plot(x, beta0 + beta1*x, 'r')
		plt.savefig('./graphs/simpleLinearRegressionModel.png')

if __name__ == "__main__":
	main()