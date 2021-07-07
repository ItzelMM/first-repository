# Itzel Munoz Monroy PSID: 1888446

def get_age():
    try:
        age = int(input())

        if age < 18 or age > 75:
            raise ValueError("Invalid age.")

        return age
    except ValueError as excpt:
        print(excpt)
        print("Could not calculate heart rate info.\n")


def fat_burning_heart_rate(age):
    if type(age) == int:
        rate = .7 * (220 - age)
        print("Fat burning heart rate for a {} year-old: {} bpm".format(age, rate))


if __name__ == "__main__":
    u_age = get_age()
    fat_burning_heart_rate(u_age)
