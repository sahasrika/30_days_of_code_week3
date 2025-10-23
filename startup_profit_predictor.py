import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import joblib

# 1️⃣ Load dataset
data = pd.read_csv(r"C:\Users\sahas\Downloads\startup_profit_data.csv")

# 2️⃣ Split features & target
X = data[["R&D_Spend", "Marketing_Spend", "Administration_Spend", "Team_Experience"]]
y = data["Profit"]

# 3️⃣ Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4️⃣ Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5️⃣ Predictions
y_pred = model.predict(X_test)

# 6️⃣ Evaluate
print("R² Score:", r2_score(y_test, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))

# 7️⃣ Visualize Actual vs Predicted
plt.figure(figsize=(8,5))
plt.scatter(y_test, y_pred, color="blue", s=70)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.xlabel("Actual Profit")
plt.ylabel("Predicted Profit")
plt.title("Startup Profit Prediction (Random Forest)")
plt.show()

# 8️⃣ Save model
joblib.dump(model, "startup_profit_model.pkl")
print("✅ Model saved as 'startup_profit_model.pkl'")
