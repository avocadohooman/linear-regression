# Simple linear regression model trained with gradient descent algorithm
The aim of this project is to explore the basic concept behind machine learning. For this project, I will create a program that predicts the price of a car by using a linear function train with a gradient descent algorithm. 

No machine learning libraries will be used for this project, to better understand the fundamentals of machine learning.

## Usage

```
git clone https://github.com/avocadohooman/linear-regression.git
cd linear-regression
python -m pip install -r requirements.txt
python3 simpleLinearRegression.py <km>
```

After each execution, a new simple linear regerssion model graph is being generated in ./graphs


## Step 1 - Creating a simple linear regression model

I will use a simple linear regression model as we have linear realtionship between two data points, of which both are known.
The formula for the simple regression model: 

`
y(estimate y) = beta0(interceptor) * beta1(slope) * x(km)
`

To get bet0, the slope, we need to first calculate the SumOfSquare of x and the SumOfSquare of y

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

