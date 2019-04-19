sentence = input('Please enter a sentence: ').split(' ')
stored_words = {}

for word in sentence:
    if word in stored_words:
        stored_words[word] += 1
    else:
        stored_words[word] = 1

print(stored_words)