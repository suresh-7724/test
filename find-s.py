import pandas as pd

# Sample dataset
data = pd.DataFrame([
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
], columns=['Sky', 'AirTemp', 'Humidity', 'Wind', 'Water', 'Forecast', 'EnjoySport'])

print("Training Data:\n", data, "\n")

# Step 1: Initialize hypothesis as the most specific
hypothesis = ['ϕ'] * (len(data.columns) - 1)

# Step 2: Iterate through examples
for i in range(len(data)):
    if data.iloc[i, -1] == 'Yes':  # Positive example
        example = data.iloc[i, :-1]
        for j in range(len(example)):
            if hypothesis[j] == 'ϕ':
                hypothesis[j] = example[j]
            elif hypothesis[j] != example[j]:
                hypothesis[j] = '?'

print("Final Hypothesis after Find-S:")
print(hypothesis)



a) Implementation of the Find-S Algorithm

Concept Recap:

The Find-S algorithm starts with the most specific hypothesis {ϕ, ϕ, ϕ, ...}

It only updates when it finds a positive example

It becomes more general to include that example

It ignores negative examples

Example Dataset

Here we’ll use a small dataset about “EnjoySport” — a common example used in ML theory.

Sky	AirTemp	Humidity	Wind	Water	Forecast	EnjoySport
Sunny	Warm	Normal	Strong	Warm	Same	Yes
Sunny	Warm	High	Strong	Warm	Same	Yes
Rainy	Cold	High	Strong	Warm	Change	No
Sunny	Warm	High	Strong	Cool	Change	Yes
