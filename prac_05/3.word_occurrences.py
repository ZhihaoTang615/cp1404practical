text = input("Text: ").lower()
words = text.split()
word_to_count = {}

for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
print(word_to_count)

max_length = max(len(word) for word in word_to_count)

for word in sorted(word_to_count):
        print(f"{word:{max_length}}: {word_to_count[word]}")



# Word Occurrences
# Estimate: 20 minutes
# Actual:   18 minutes