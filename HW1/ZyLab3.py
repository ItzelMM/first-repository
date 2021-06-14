# Itzel Munoz Monroy UHID: 1888446
juice = float(input("Enter amount of lemon juice (in cups):"))
print("")
water = float(input("Enter amount of water (in cups):"))
print("")
nectar = float(input("Enter amount of agave nectar (in cups):"))
print("")
servings = float(input("How many servings does this make?"))
print("")
print("")
print("Lemonade ingredients - yields {:.2f} servings".format(servings))
print("{:.2f} cup(s) lemon juice".format(juice))
print("{:.2f} cup(s) water".format(water))
print("{:.2f} cup(s) agave nectar".format(nectar))
print("")
wanted = float(input("How many servings would you like to make?"))
print("")
print("")
ratio = wanted/servings
n_juice = juice*ratio
n_water = water*ratio
n_nectar = nectar*ratio
print("Lemonade ingredients - yields {:.2f} servings".format(wanted))
print("{:.2f} cup(s) lemon juice".format(n_juice))
print("{:.2f} cup(s) water".format(n_water))
print("{:.2f} cup(s) agave nectar".format(n_nectar))
g_juice = n_juice/16
g_water = n_water/16
g_nectar = n_nectar/16
print("")
print("Lemonade ingredients - yields {:.2f} servings".format(wanted))
print("{:.2f} gallon(s) lemon juice".format(g_juice))
print("{:.2f} gallon(s) water".format(g_water))
print("{:.2f} gallon(s) agave nectar".format(g_nectar))
