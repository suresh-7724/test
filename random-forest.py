Here’s a complete, step-by-step **Assignment 7: Random Forest Algorithm** implementation guide with code and explanations for each dataset. You can directly run this in **Jupyter Notebook** or **PyCharm** with a `conda` or `venv` environment containing `pandas`, `numpy`, `matplotlib`, and `scikit-learn`.

---

## **Assignment 7: Random Forest Algorithm**

### **Objective**

Implement the Random Forest Algorithm on three datasets:

1. MNIST handwritten digits dataset
2. Mental health dataset
3. Default payment dataset

---

## **1. Import the Required Libraries**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.utils import resample
import seaborn as sns
```

---

## **2. Implementation on MNIST Dataset**

### **a) Load MNIST dataset**

```python
from sklearn.datasets import fetch_openml

# Load dataset
mnist = fetch_openml('mnist_784', version=1)
X, y = mnist.data, mnist.target.astype('int')

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### **b) Train the Random Forest Model**

```python
rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
```

### **c) Evaluate the Model**

```python
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
```

---

## **3. Implementation on Mental Health Dataset**

*(Assume `mental_health.csv` is provided in the working directory)*

### **a) Load and Explore the Dataset**

```python
df = pd.read_csv('mental_health.csv')
print(df.head())
print(df.info())
print(df.isnull().sum())
```

### **b) Handle Missing Values**

```python
df = df.dropna()
```

### **c) Convert Categorical Variables**

```python
df = pd.get_dummies(df, drop_first=True)
```

### **d) Split and Train the Model**

```python
X = df.drop('Target', axis=1)  # replace 'Target' with actual target column
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

rf = RandomForestClassifier(n_estimators=150, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
```

### **e) Evaluate**

```python
print("Accuracy:", accuracy_score(y_test, y_pred))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d')
plt.title("Confusion Matrix - Mental Health Data")
plt.show()
```

---

## **4. Implementation on Default Payment Dataset**

### **a) Load the Dataset**

```python
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00350/default%20of%20credit%20card%20clients.xls"
df = pd.read_excel(url, header=1)
df.head()
```

### **b) Drop ID column**

```python
df.drop(['ID'], axis=1, inplace=True)
```

### **c) Analyze Missing Data**

```python
print(df.isnull().sum())
print(df['EDUCATION'].unique())
print(df['MARRIAGE'].unique())
```

### **d) Filter Valid Rows**

```python
df = df[(df['EDUCATION'] != 0) & (df['MARRIAGE'] != 0)]
```

### **e) Check Target Variable Balance**

```python
sns.countplot(x='default payment next month', data=df)
plt.title("Target Variable Balance")
plt.show()
```

### **f) Downsample Data**

```python
default_df = df[df['default payment next month'] == 1]
non_default_df = df[df['default payment next month'] == 0]

default_downsampled = resample(default_df, replace=False, n_samples=1000, random_state=42)
non_default_downsampled = resample(non_default_df, replace=False, n_samples=1000, random_state=42)

df_downsampled = pd.concat([default_downsampled, non_default_downsampled])
```

### **g) Hot Encode and Prepare Data**

```python
X = df_downsampled.drop('default payment next month', axis=1).copy()
y = df_downsampled['default payment next month']

X = pd.get_dummies(X, drop_first=True)
```

### **h) Split the Dataset**

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

### **i) Train and Evaluate Random Forest**

```python
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d')
plt.title("Confusion Matrix - Credit Default Data")
plt.show()
```

### **j) Hyperparameter Tuning**

```python
rf_tuned = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    max_leaf_nodes=50,
    random_state=42
)
rf_tuned.fit(X_train, y_train)
y_pred_tuned = rf_tuned.predict(X_test)

print("Tuned Accuracy:", accuracy_score(y_test, y_pred_tuned))
print("\nClassification Report:\n", classification_report(y_test, y_pred_tuned))
```

---

## **Output Summary**

| Dataset         | Accuracy (approx.) | Comments                     |
| --------------- | ------------------ | ---------------------------- |
| MNIST           | 96–98%             | Excellent for classification |
| Mental Health   | Depends on dataset | Requires clean features      |
| Default Payment | 78–85%             | Improved after tuning        |

---

Would you like me to include this as a **ready-to-submit .ipynb (Jupyter Notebook)** file with explanations and markdown cells?
