# Itzel Munoz Monroy PSID: 1888446
class FoodItem:
    def __init__(self, name="None", fat=0.00, carbs=0.00, protein=0.00, num_servings=0.00):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.num_servings = num_servings

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    food1 = FoodItem()
    food1.name = input()
    food1.fat = float(input())
    food1.carbs = float(input())
    food1.protein = float(input())
    food1.num_servings = float(input())

    food2 = FoodItem()
    food2.print_info()
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(food1.num_servings, 0))
    print("")

    food1.print_info()
    cal = food1.get_calories(food1.num_servings)
    print("Number of calories for {:.2f} serving(s): {:.2f}".format(food1.num_servings, cal))
