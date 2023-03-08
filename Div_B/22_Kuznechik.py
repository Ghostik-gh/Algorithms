n, k = input().split()
n = int(n)
k = int(k)
arr = []
arr.append(1)

for i in range(1, n):
    tmp = 0
    for j in range(1, k + 1):
        if i - j >= 0:
            tmp += arr[i-j]
    arr.append(tmp)


print(arr[-1])
