Here’s a **complete structured guide with Python code examples** for **Assignment 4: Implementing Neural Networks**, covering all parts (a–g). You can run these in **Google Colab, Jupyter Notebook, or PyCharm** with the following libraries installed:

```bash
pip install numpy pandas tensorflow scikit-learn
```

---

## **Assignment 4 – Implementing Neural Networks**

---

### **a) AND Classifier using Neural Network**

```python
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Input (X) and Output (y)
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[0],[0],[1]])

# Model
model = Sequential()
model.add(Dense(1, input_dim=2, activation='sigmoid'))

# Compile and Train
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=500, verbose=0)

# Test
print("Predictions for AND gate:")
print(model.predict(X).round())
```

---

### **b) OR Classifier**

```python
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[1]])

model = Sequential()
model.add(Dense(1, input_dim=2, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=500, verbose=0)

print("Predictions for OR gate:")
print(model.predict(X).round())
```

---

### **c) NAND Classifier**

```python
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[1],[1],[1],[0]])

model = Sequential()
model.add(Dense(1, input_dim=2, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=500, verbose=0)

print("Predictions for NAND gate:")
print(model.predict(X).round())
```

---

### **d) XOR Classifier**

```python
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

model = Sequential()
model.add(Dense(1, input_dim=2, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=1000, verbose=0)

print("Predictions for XOR gate:")
print(model.predict(X).round())
```

🧠 **Comment:**
A single-layer neural network cannot classify XOR correctly because **XOR is not linearly separable**. It requires **a hidden layer** with a nonlinear activation function to learn the complex boundary.

✅ **Fix (Multi-layer XOR Neural Network):**

```python
model = Sequential()
model.add(Dense(2, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=1000, verbose=0)
print("Predictions for XOR gate (multi-layer):")
print(model.predict(X).round())
```

---

### **e) Neural Network Classifier for Iris Dataset**

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.utils import to_categorical

iris = load_iris()
X = iris.data
y = to_categorical(iris.target)  # One-hot encoding

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential()
model.add(Dense(10, input_dim=4, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))  # 3 classes

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=100, batch_size=5, verbose=0)

loss, acc = model.evaluate(X_test, y_test)
print(f"Iris Test Accuracy: {acc*100:.2f}%")
```

🔧 **Hyperparameters to Tune:**

* Learning Rate (use `tf.keras.optimizers.Adam(learning_rate=0.01)`)
* Epochs (e.g. 50, 100, 200)
* Layers and Neurons (e.g. `Dense(16, activation='relu')`)

---

### **f) Neural Network for Diabetes Dataset**

```python
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential()
model.add(Dense(64, input_dim=X.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1))  # Regression output

model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.fit(X_train, y_train, epochs=150, batch_size=10, verbose=0)

loss, mae = model.evaluate(X_test, y_test)
print(f"Diabetes Mean Absolute Error: {mae:.2f}")
```

🔧 **Tuning Tip:**
Try different learning rates and hidden layer sizes to see how error changes.

---

### **g) Neural Network for Heart Dataset**

```python
import pandas as pd

# Example heart dataset (You can replace with your provided file)
url = "https://raw.githubusercontent.com/plotly/datasets/master/heart.csv"
df = pd.read_csv(url)

X = df.drop('target', axis=1)
y = df['target']

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Sequential()
model.add(Dense(16, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=100, batch_size=8, verbose=0)

loss, acc = model.evaluate(X_test, y_test)
print(f"Heart Disease Classification Accuracy: {acc*100:.2f}%")
```

---

✅ **Summary Table**

| Task | Dataset / Function | Type                       | Output        |
| ---- | ------------------ | -------------------------- | ------------- |
| a–d  | Logic Gates        | Binary Classification      | 0 or 1        |
| e    | Iris               | Multi-class Classification | 3 Species     |
| f    | Diabetes           | Regression                 | Numeric Value |
| g    | Heart              | Binary Classification      | Disease (0/1) |

---

Would you like me to create a **single Jupyter notebook (.ipynb)** combining all these sections with explanations and outputs? I can prepare it so you can directly upload it to **Google Colab**.
