# Itzel Munoz Monroy PSID: 188446
def partition(list_v, lowest, highest):
    pivot = list_v[highest]
    check = lowest - 1
    for x in range(lowest, highest):
        if list_v[x] < pivot:
            check += 1
            holder = list_v[x]
            list_v[x] = list_v[check]
            list_v[check] = holder
    check += 1
    list_v[highest] = list_v[check]
    list_v[check] = pivot
    return check


def quicksort(list_v, lowest, highest):
    if lowest < highest:
        pivot = partition(list_v, lowest, highest)
        quicksort(list_v, lowest, pivot - 1)
        quicksort(list_v, pivot + 1, highest)


answer = ""
values = []
while answer != "-1":
    answer = input()
    if answer != "-1":
        values.append(answer)
num_calls = (len(values) * 2) - 1
quicksort(values, 0, (len(values)-1))
print(num_calls)
for ID in values:
    print(ID)
