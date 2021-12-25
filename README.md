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

## Method 2 - Training linear regression model with a gradient descent algorithm

### Math

During each iteration, the coefficients (w) in machine learning language are updated using the equation:

`
w(t+1) = w(t) - learningRate * error * input value
`

`
error = prediction - expected
`

### Usage - trainModel.py

First, you will need to train the coefficients (beta0, beta1), which are stored in ./coefficients/b0b1.csv
The initial value for beta0 and beta1 is zero.

```
python3 trainModel.py
```

After you execute the program, you will be prompted to do the following steps:

**1) Choose that data set for training the model, which needs to be located in './data/'**

The CSV needs to follow certain formatting rules:

- First row describes the column names
- It can't be empty
- It needs to have exactly two columns
- It can only contain numeric values as int or float (besides the columns labels)

#### Example

```
km, price
240000,3650
139800,3800
150500,4400
185530,4450
.
.
.
```

**2) Choose a learning rate between 0 - 1**

"Learning rate is a hyper-parameter that controls the weights of our linear regression model with respect to the loss gradient. A desirable learning rate is low enough that the network converges to something useful, but high enough that it can be trained in a reasonable amount of time. Smaller learning rates require more training epochs (requires more time to train) due to the smaller changes made to the weights in each update, whereas larger learning rates result in rapid changes and require fewer training epochs. ​ However, larger learning rates often result in a sub-optimal final set of weights." - (https://www.educative.io/edpresso/learning-rate-in-machine-learning)

**3) Choose the number of epoch (iteration/cycles) the gradient descent should go through. The value needs be > 0.**

**4) The trained weights (b0, b1) are saved in ./coeffiecients/b0b1.csv which will be used for executing trainedGradientDescentPrediction.py **


### Usage - trainedGradientDescentPrediction.py


```
python3 trainedGradientDescentPrediction.py
```

Run the program and enter a value for the prediction.

### Usage - accuracy.py

Run this program to calculate the current RMSE of the trained model. It will use by default a dataset named 'data.csv' located in './data/' 

### Normalized value graph of gradient descent algorithm method
![normalizedData](./graphs/normalized_data.png?raw=true)



