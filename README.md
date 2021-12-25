#  Linear regression model with two approaches: least square method, and trained with gradient descent algorithm
The aim of this project is to explore the basic concept behind machine learning. For this project, I will create a program that predicts the price of a car by using a linear function train with a gradient descent algorithm. 

No machine learning libraries will be used for this project, to better understand the fundamentals of machine learning.

There are two approaches for this linear regression:

1) Least squares
2) Gradient descent algorithm

## General Setup

```
git clone https://github.com/avocadohooman/linear-regression.git
cd linear-regression
python3 -m pip install -r requirements.txt
```

## Accuracy 

To compare the accuracy of both methods, I am using the Root Mean Squared Error (RMSE) method. RMSE is calculated
as the square root of the mean of the squared differences between actual outcomes and predictions. 
Squaring each error forces the values to be positive, and the square root of the mean squared error returns the
error metric back to the original units for comparison.

## Method 1 - Linear regression with least squares method

### Usage

```
python3 leastSquaresPrediction.py <km>
```

#### Example

```
$ python3 leastSquaresPrediction.py 75000
$ beta0, beta1 8499.599649933216 -0.021448963591702303
$ predictedPrice 6890
$ RMSE: 667.567
```

The formula for the linear regression model: 

`
y(estimated price) = beta0(interceptor) * beta1(slope) * x(km)
`

### Calculating the slope

`
beta1 = SSxx/SSxy
`

SSxx is the SumSquare of x, and SSxy the SumSquare of x * y

`
SSxx = SumOf((mean)x - x)^2
`

`
SSxy = SumOf((mean)x - x) * ((mean)y - y)
`

### Calculating the interceptor

`beta0 = (mean)prices - beta1*(mean)km`


### Combining all and creating a prediction function

```
def predict(km):
    predictedPrice = beta0 + beta1*km
    return predictedPrice
```

### Real value graph of least squares prediction
![leastSquaresPrediction](./graphs/leastSquaresPrediction.png?raw=true)

## Step 2 - Training my model with a gradient descent algorithm

Work in progress.


