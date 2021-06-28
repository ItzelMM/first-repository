# Itzel Munoz Monroy PSID: 1888446
numbers = input()
list_int = numbers.split()
list_post = []

for num in list_int:
    if float(num) >= 0:
        list_post.append(int(num))

list_post.sort()

for positive in list_post:
    print(positive, end=" ")
