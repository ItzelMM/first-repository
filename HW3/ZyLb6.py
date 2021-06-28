# Itzel Munoz Monroy PSID: 1888446
words = input()
words_list = words.split()
for word in words_list:
    count = words_list.count(word)
    print(word, count)
