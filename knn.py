Here’s a complete, step-by-step **Assignment 8: k-Nearest Neighbor (KNN)** implementation guide with code examples and clear explanations for all three tasks.
You can directly run this code in **Jupyter Notebook** or **PyCharm** using `conda` or `venv` with libraries `pandas`, `numpy`, `matplotlib`, and `scikit-learn`.

---

## **Assignment 8: K-Nearest Neighbor (KNN) Algorithm**

### **Objective**

Implement and understand the working of KNN for:

1. Predicting sugar level of diabetic patients (given BMI and Age)
2. Classifying color from Brightness and Saturation data
3. Applying KNN on the Iris dataset

---

## **Import Required Libraries**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
```

---

## **1. Predict Sugar of Diabetic Patient given BMI and Age using KNN**

### **a) Create a sample dataset**

```python
# Sample dataset
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60],
    'BMI': [22, 25, 28, 30, 32, 34, 36, 38],
    'Sugar': ['Normal', 'Normal', 'Borderline', 'High', 'High', 'High', 'Very High', 'Very High']
}

df = pd.DataFrame(data)
print(df)
```

### **b) Feature and Target separation**

```python
X = df[['Age', 'BMI']]
y = df['Sugar']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### **c) Train the KNN model (k=3)**

```python
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_scaled, y)
```

### **d) Predict sugar level for a new patient**

```python
# Example: Age=42, BMI=31
new_patient = scaler.transform([[42, 31]])
predicted_sugar = knn.predict(new_patient)
print("Predicted Sugar Level:", predicted_sugar[0])
```

---

## **2. Design a k-NN for Brightness and Saturation Dataset**

### **a) Define dataset**

```python
data = {
    'Brightness': [40, 50, 60, 10, 70, 60, 25],
    'Saturation': [20, 50, 90, 25, 70, 10, 80],
    'Class': ['Red', 'Blue', 'Blue', 'Red', 'Blue', 'Red', 'Blue']
}

df_color = pd.DataFrame(data)
print(df_color)
```

### **b) Split features and target**

```python
X = df_color[['Brightness', 'Saturation']]
y = df_color['Class']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### **c) Train the KNN model**

```python
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_scaled, y)
```

### **d) Predict for Brightness=20, Saturation=35**

```python
test_point = scaler.transform([[20, 35]])
predicted_class = knn.predict(test_point)
print("Predicted Class for Brightness=20, Saturation=35:", predicted_class[0])
```

### **e) Visualization (Optional)**

```python
plt.scatter(df_color['Brightness'], df_color['Saturation'], c=(y=='Blue'), cmap='coolwarm')
plt.xlabel('Brightness')
plt.ylabel('Saturation')
plt.title('Color Classification by KNN')
plt.show()
```

---

## **3. Apply KNN on the Iris Dataset**

### **a) Load dataset**

```python
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
```

### **b) Split and normalize data**

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```

### **c) Train KNN model**

```python
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
```

### **d) Evaluate performance**

```python
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=iris.target_names))
```

### **e) Visualize Decision Boundaries (Optional)**

```python
from matplotlib.colors import ListedColormap

X_plot = X_scaled[:, :2]  # Using only 2 features for 2D plot
y_plot = y

x_min, x_max = X_plot[:, 0].min() - 1, X_plot[:, 0].max() + 1
y_min, y_max = X_plot[:, 1].min() - 1, X_plot[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

knn.fit(X_plot, y_plot)
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.5, cmap=ListedColormap(('red', 'green', 'blue')))
plt.scatter(X_plot[:, 0], X_plot[:, 1], c=y_plot, cmap=ListedColormap(('red', 'green', 'blue')))
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title("KNN Classification Boundaries - Iris Dataset")
plt.show()
```

---

## **Summary of Results**

| Task | Dataset               | K Value | Output                            | Accuracy |
| ---- | --------------------- | ------- | --------------------------------- | -------- |
| 1    | Diabetic (Age, BMI)   | 3       | Predicted sugar level for patient | —        |
| 2    | Brightness/Saturation | 3       | Classified as “Red” or “Blue”     | —        |
| 3    | Iris dataset          | 3       | Classified iris flowers           | ~96–98%  |

---

Would you like me to prepare this as a **ready-to-submit Jupyter Notebook (.ipynb)** file with clear markdown explanations between code blocks?
