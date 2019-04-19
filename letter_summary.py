word = input('Please enter a word: ').lower()
alpha = {}

for letter in word:
    if letter in alpha:
        alpha[letter] += 1
    else:
        alpha[letter] = 1

print(alpha)