# Itzel Munoz Monroy PSID: 1888446
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
services = {"oil change": 35, "tire rotation": 19, "car wash": 7, "car wax": 12}
print("")
serv1 = input("Select first service:")
print("")
serv2 = input("Select second service:")
print("")
print("")
print("Davy's auto shop invoice")
print("")
if serv1 == "-":
    print("Service 1: No service")
    money1 = 0
else:
    check1 = serv1.lower()
    print("Service 1: {}, ${}".format(serv1, services[str(check1)]))
    money1 = services[str(check1)]
if serv2 == "-":
    print("Service 2: No service")
    money2 = 0
else:
    check2 = serv2.lower()
    print("Service 2: {}, ${}".format(serv2, services[str(check2)]))
    money2 = services[str(check2)]
total = money1 + money2
print("")
print("Total: ${}".format(total))
