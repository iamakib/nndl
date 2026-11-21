
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==================================
# 1. Dataset Configuration
# ==================================

NUM_SAMPLES = 1000
X_MIN = -10
X_MAX = 10

ADD_NOISE = False
NOISE_LEVEL = 5

# ==================================
# 2. Original Mathematical Equation
# ==================================

def original_equation(x):
    return 3*x**3 + 2*x**2 - 5*x + 7

# ==================================
# 3. Generate Input Data
# ==================================

np.random.seed(42)

X = np.linspace(X_MIN, X_MAX, NUM_SAMPLES)

# ==================================
# 4. Generate Output Data
# ==================================

Y = original_equation(X)

# Optional noise
if ADD_NOISE:
    noise = np.random.normal(0, NOISE_LEVEL, NUM_SAMPLES)
    Y = Y + noise

# ==================================
# 5. Create Dataset
# ==================================

dataset = pd.DataFrame({
    "X": X,
    "Y": Y
})

# ==================================
# 6. Save Dataset
# ==================================

dataset.to_csv("mathematical_dataset.csv", index=False)

print("Dataset Generated Successfully!")
print("Total Samples:", len(dataset))
print("\nFirst 10 Rows:")
print(dataset.head(10))

# ==================================
# 7. Visualize Dataset
# ==================================

plt.figure(figsize=(10, 6))

plt.scatter(X, Y, s=10, label="Generated Dataset")

plt.xlabel("Input (X)")
plt.ylabel("Output (Y)")
plt.title("Mathematical Equation Dataset")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# ==================================
# 8. Display Original Equation
# ==================================

print("\nOriginal Equation:")
print("Y = 3X^3 + 2X^2 - 5X + 7")

print("\nDataset saved as mathematical_dataset.csv")
