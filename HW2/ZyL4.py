# Itzel Munoz Monroy PSID: 1888446
word = input()
word_l = word.split()
word_ns = "".join(word_l)

if word_ns == (word_ns[::-1]):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
