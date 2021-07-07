# Itzel Munoz Monroy PSID: 1888446
user = ""
storage = []

while user != "-1":
    user = input()
    if user != "-1":
        try:
            words = user.split()
            if not words[1].isdigit():
                raise ValueError
            number = int(words[-1]) + 1
            correct_words = words[0] + " " + str(number)
            storage.append(correct_words)
        except ValueError:
            words = user.split()
            correct_words = words[0] + " 0"
            storage.append(correct_words)

for name in storage:
    print(name)
