import random

with open("Lab2/input1.txt") as f:
    arr = f.read().split("\n")

# for i in range(100):
#     a = random.randint(0, len(arr) - 1)
#     b = random.randint(0, len(arr) - 1)
#     arr[a], arr[b] = arr[b], arr[a]

first = [arr[0]]
arr.pop(0)
second = []

while len(arr) > 0:
    if arr[0] > first[-1]:
        first.append(arr[0])
        arr.pop(0)
    elif arr[0] < first[0]:
        first.insert(0, arr[0])
        arr.pop(0)
    else:
        while arr[0] <= first[-1]:
            second.append(first[-1])
            first.pop()
        first.append(arr[0])
        arr.pop(0)
        for i in range(len(second)):
            first.append(second[-1])
            second.pop()


print(*first, sep="\n")
print(*arr, sep="\n")
