def apply_to_words(func, sentence):
    return func(sentence.split())

# Example:
reverse_func = lambda words: ' '.join(reversed(words))
print(apply_to_words(reverse_func, "This is a test"))  # Output: "test a is This"
