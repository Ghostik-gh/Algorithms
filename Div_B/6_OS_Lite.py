m = int(input())
n = int(input())
k = 0
arr = []
for i in range(n):
    k += 1
    arr.append(input().split(' '))
    arr[-1][0] = int(arr[-1][0])
    arr[-1][1] = int(arr[-1][1])
    for j in arr[:-1]:
        if ((arr[-1][0] <= j[0]) and (arr[-1][1] >= j[0])) or ((arr[-1][0] <= j[1]) and (arr[-1][1] >= j[1])) or ((arr[-1][0] >= j[0]) and (arr[-1][1] <= j[1])):
            k -= 1
            arr.pop(arr.index(j))
print(k)
