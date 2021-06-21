# Itzel Munoz Monroy PSID: 1888446
start = input("Please enter a password: ")
letters = list(start)
password = []
for letter in letters:
    if letter == "i":
        password.append("!")
    elif letter == "a":
        password.append("@")
    elif letter == "m":
        password.append("M")
    elif letter == "B":
        password.append("8")
    elif letter == "o":
        password.append(".")
    else:
        password.append(letter)
password.append("q*s")
string1 = ""
password = string1.join(password)
print(password)
