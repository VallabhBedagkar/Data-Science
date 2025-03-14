# Machine Learning Projects

## Overview
This repository contains three different machine learning models built for three different datasets: Task 1, Task 2, and Task 3.

## Task 1: Model for Dataset 1
- **Dataset**: Title: Advertising Dataset

Abstract: This dataset contains information about the advertising expenditure in three different media channels (TV, Radio, and Newspaper) and their impact on sales. 
          It aims to analyze the effectiveness of advertising strategies on sales performance.
Content and Structure:
Number of rows: 200
Number of columns: 4
Columns: TV, Radio, Newspaper, Sales
Source: kaggle
Usage Notes:
This dataset can be used to analyze the impact of different advertising channels on sales performance.
It is suitable for regression analysis to predict sales based on advertising expenditure.
  
- **Model**: Linear Regression

Overview: Linear Regression is a simple yet powerful statistical technique used to model the relationship between a dependent variable and one or more independent variables. In Task 1, we used Linear Regression to predict sales based on the amount of money spent on TV, Radio, and Newspaper advertising.

Training the Model:

Data Preparation:

Ensure the data has no missing values.

Standardize or normalize the data if necessary.

Fitting the Model:

Use the training data to estimate the coefficients (𝛽) by minimizing the sum of squared residuals.

The LinearRegression class from scikit-learn is used to fit the model.

Model Evaluation:

Evaluate the model using metrics such as R-squared, Mean Absolute Error (MAE), and Mean Squared Error (MSE).

Perform residual analysis to check for any patterns or deviations from assumptions.

Model Performance:

R-squared: Measures the proportion of variance in the dependent variable that is predictable from the independent variables. A higher R-squared indicates a better fit.

MAE and MSE: Provide insights into the average magnitude of the errors in predictions.
.
- **Results**: 
Linear Regression Summary:
Coefficients:

Value: 0.05483488

Interpretation: For every additional thousand dollars spent on TV advertising, sales are predicted to increase by approximately 0.055 thousand units (or 55 units).

Intercept:

Value: 7.206554548173255

Interpretation: When the expenditure on TV advertising is zero, the baseline sales are predicted to be approximately 7.21 thousand units.

R-squared (R²):

Value: 0.814855389208679

Interpretation: About 81.5% of the variance in sales can be explained by the expenditure on TV advertising alone. This indicates a strong linear relationship between TV ad expenditure and sales.

Mean Squared Error (MSE):

Value: 5.179525402166653

Interpretation: On average, the squared difference between the actual and predicted sales values is about 5.18 units. A lower MSE indicates a better fit of the model to the data.
