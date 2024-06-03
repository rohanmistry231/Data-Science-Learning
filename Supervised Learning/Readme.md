# Supervised Learning

This section covers supervised learning, a type of machine learning where the model is trained on labeled data, and learns to predict outcomes based on input features.

## What is Supervised Learning?

Supervised learning is a machine learning technique where the algorithm learns from labeled training data. The training data consists of input-output pairs, where the inputs are the features and the outputs are the corresponding labels or target variables. The goal of supervised learning is to learn a mapping from inputs to outputs, such that the model can make accurate predictions on unseen data.

Supervised learning can be divided into two main categories:

1. **Regression:** In regression tasks, the model predicts continuous values. Examples include predicting house prices based on features like area, number of bedrooms, etc., or predicting the temperature based on weather features.

2. **Classification:** In classification tasks, the model predicts discrete class labels. Examples include predicting whether an email is spam or not, classifying images into different categories (e.g., cats vs. dogs), or predicting whether a customer will churn or not.

## Resources

Here are some resources to learn more about supervised learning:

### Tutorials and Courses
- [Supervised Learning - Coursera](https://www.coursera.org/learn/supervised-learning)

### Books
- "Introduction to Statistical Learning" by Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani
- "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" by Aurélien Géron

### Documentation
- [Scikit-Learn Documentation](https://scikit-learn.org/stable/)

### Blogs and Articles
- [A Gentle Introduction to Supervised Learning](https://machinelearningmastery.com/supervised-learning/)

## Code Examples

### Regression Example (using Scikit-Learn)

```python
from sklearn.linear_model import LinearRegression

# Sample data
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Predict
predictions = model.predict([[6]])
print(predictions)  # Output: [12.]