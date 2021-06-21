# Itzel Munoz Monroy PSID: 1888446

def exact_change(user_total):
    import math

    pennies = 0

    if user_total == 0:
        dollars = "no change"
        quarters = "no change"
        dimes = "no change"
        nickels = "no change"

        return dollars, quarters, dimes, nickels, pennies

    values = {100: 0, 25: 0, 10: 0, 5: 0}

    for value in values:
        if user_total >= value and user_total % value != 0:
            close = user_total / value
            values[int(value)] = math.floor(close)
            user_total = user_total - ((values.get(int(value))) * value)
        elif user_total >= value and user_total % value == 0:
            values[int(value)] = int(user_total / value)
            user_total = user_total - ((values.get(int(value))) * value)
            break
        else:
            continue

    if user_total != 0:
        pennies = user_total

    dollars = values[100]
    quarters = values[25]
    dimes = values[10]
    nickels = values[5]

    return dollars, quarters, dimes, nickels, pennies


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
    numbers = [num_dollars, num_quarters, num_dimes, num_nickels, num_pennies]
    coins = ["dollar", "quarter", "dime", "nickel", "penny"]
    order = 0
    for num in numbers:
        if num == "no change":
            print("no change")
            break
        if num != 0 and num > 1:
            if order == 4:
                print(num, "pennies")
            else:
                print(num, coins[order] + "s")
        elif num != 0 and num == 1:
            print(num, coins[order])
        order += 1
