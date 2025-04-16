import itertools

elements=input("enter numbers seperated by space").split()
print("All combinations: ")

for r in (range(len(elements)+1)):
    for combo in itertools.combinations(elements, r):
        print(combo)