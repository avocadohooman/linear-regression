# Simple linear regression model trained with gradient descent algorithm
The aim of this project is to explore the basic concept behind machine learning. For this project, I will create a program that predicts the price of a car by using a linear function train with a gradient descent algorithm. 

No machine learning libraries will be used for this project, to better understand the fundamentals of machine learning.

In step 1 I will create a simple linear regression model, without training.

Step 2 will then incorporate the gradient descent algorithm to train my model for higher confidence.

## Usage

```
git clone https://github.com/avocadohooman/linear-regression.git
cd linear-regression
python3 -m pip install -r requirements.txt
python3 simpleLinearRegression.py <km>
```

After each execution, a new simple linear regerssion model graph is being generated in ./graphs


## Step 1 - Creating a simple linear regression model

I will use a simple linear regression model as we have linear realtionship between two data points, of which both are known.
The formula for the simple regression model: 

`
y(estimate y) = beta0(interceptor) * beta1(slope) * x(km)
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

### Example graph of a simple linear regression model
![simpleLinearRegression](./graphs/simpleLinearRegressionModel.png?raw=true)

## Step 2 - Training my model with a gradient descent algorithm

Work in progress.


