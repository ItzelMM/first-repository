# Itzel Munoz Monroy PSID: 1888446
def selection_sort_descend_trace(values):
    copy_l = values[::]
    copy_l.sort(reverse=True)
    sort_list = []
    for times in range(len(values)-1):
        if times == 0:
            maxn = max(values)
            index = values.index(maxn)
            values[index] = values[0]
            values.pop(0)
            sort_list.append(maxn)
            sort_list.extend(values)
            for value in sort_list:
                print(value, end=" ")
            print("")
        elif copy_l == sort_list:
            for value in sort_list:
                print(value, end=" ")
            print("")
        else:
            maxn = max(values)
            index = values.index(maxn)
            values[index] = values[0]
            values.pop(0)
            del sort_list[times::]
            sort_list.append(maxn)
            sort_list.extend(values)
            for value in sort_list:
                print(value, end=" ")
            print("")


if __name__ == "__main__":
    test = input()
    separated = test.split()
    number_l = []
    for word in separated:
        number_l.append(int(word))
    selection_sort_descend_trace(number_l)
