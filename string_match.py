def string_match(s):
    vowels='aeiou'
    s=s.lower()
    if(s[0] in vowels):
        return "Starts with vowel"
    if(s and s[-1].isdigit()):
        return "ends with digit"
    if('python' in s):
        return "contains python"
    return "no match"

s=input("Enter a string: ")
print(string_match(s))