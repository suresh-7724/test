Concept Recap:

Candidate Elimination maintains two boundaries:

S (Specific boundary): most specific hypotheses

G (General boundary): most general hypotheses

For positive examples:
→ Generalize S minimally
→ Remove inconsistent hypotheses from G

For negative examples:
→ Specialize G minimally
→ Remove inconsistent hypotheses from S

The version space is all hypotheses between S and G.


import pandas as pd

# Dataset (same as before)
data = pd.DataFrame([
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
], columns=['Sky', 'AirTemp', 'Humidity', 'Wind', 'Water', 'Forecast', 'EnjoySport'])

print("Training Data:\n", data, "\n")

# Extract features and labels
attributes = data.columns[:-1]
target = data.columns[-1]

# Initialize S (Specific boundary)
S = [['ϕ'] * len(attributes)]

# Initialize G (General boundary)
G = [['?'] * len(attributes)]

def is_consistent(h, example):
    for i in range(len(h)):
        if h[i] != '?' and h[i] != example[i]:
            return False
    return True

for i in range(len(data)):
    instance = data.iloc[i, :-1]
    label = data.iloc[i, -1]

    if label == 'Yes':
        # Remove any G inconsistent with instance
        G = [g for g in G if is_consistent(g, instance)]

        # Generalize S minimally
        for s in S:
            for j in range(len(s)):
                if s[j] == 'ϕ':
                    s[j] = instance[j]
                elif s[j] != instance[j]:
                    s[j] = '?'
    else:
        # For negative examples
        new_G = []
        for g in G:
            if is_consistent(g, instance):
                for j in range(len(g)):
                    if g[j] == '?':
                        for val in data[attributes[j]].unique():
                            if val != instance[j]:
                                new_hyp = g.copy()
                                new_hyp[j] = val
                                if any(is_consistent(s, new_hyp) for s in S):
                                    new_G.append(new_hyp)
            else:
                new_G.append(g)
        G = new_G

print("Final Specific Boundary (S):", S)
print("Final General Boundary (G):", G)

