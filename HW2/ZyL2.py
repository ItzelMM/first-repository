# Itzel Munoz Monroy PSID: 1888446
a1 = int(input("Enter an integer: "))
b1 = int(input("Enter an integer: "))
c1 = int(input("Enter an integer: "))
a2 = int(input("Enter an integer: "))
b2 = int(input("Enter an integer: "))
c2 = int(input("Enter an integer: "))

x = "no"
y = "no"

for r in range(-10, 11):
    for o in range(-10, 11):
        if ((a1*r) + (b1*o) - c1) == 0 and ((a2*r) + (b2*o) - c2) == 0:
            x = r
            y = o
            break
if x == "no" and y == "no":
    print("No solution")
else:
    print(x, y)
