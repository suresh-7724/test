def filter_names(name_list, substring):
    for name in name_list:
        if substring.lower() in name.lower():
            yield name

# Example usage
names = ["Alice", "Bob", "Charlie", "David", "Alicia"]
sub = input("Enter substring to filter names: ")
for name in filter_names(names, sub):
    print(name)
