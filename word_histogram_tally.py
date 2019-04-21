sentence = 'To be or not to be do be do be do'.lower().split(' ')
counted_words = {}
count_top_3 = 0

for word in sentence:
    if word in counted_words:
        counted_words[word] += 1
    else:
        counted_words[word] = 1

# solution found online: https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
for key, value in sorted(counted_words.items(), key = lambda item: item[1],reverse = True):
    if count_top_3 < 3:
        print("%s: %s" % (key, value))
        count_top_3 += 1
    else:
        break