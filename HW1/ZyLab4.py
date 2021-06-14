# Itzel Munoz Monroy PSID: 1888446
import math
height = int(input("Enter wall height (feet):"))
print("")
width = int(input("Enter wall width (feet):"))
print("")
area = height * width
paint = area / 350
cans = math.ceil(paint)
print("Wall area: {} square feet".format(area))
print("Paint needed: {:.2f} gallons".format(paint))
print("Cans needed: {} can(s)".format(cans))
print("")
prices = {"red": 35, "blue": 25, "green": 23}
color = input("Choose a color to paint the wall:")
print("")
if color.lower() == "red":
    print("Cost of purchasing red paint: ${}".format((cans*prices["red"])))
elif color.lower() == "blue":
    print("Cost of purchasing blue paint: ${}".format((cans*prices["blue"])))
elif color.lower() == "green":
    print("Cost of purchasing green paint: ${}".format((cans*prices["green"])))
else:
    print("ERROR: You didn't enter a valid color")
