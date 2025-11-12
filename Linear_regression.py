from sklearn.linear_model import LinearRegression
import numpy as np

# Data: Study hours vs Scores
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([40, 50, 60, 70, 80])

model = LinearRegression()
model.fit(X, y)

hours = 6
pred = model.predict([[hours]])
print(f"Predicted score for {hours} hours: {pred[0]:.2f}")
