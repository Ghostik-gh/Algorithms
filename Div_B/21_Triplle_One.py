n = int(input())
arr = [0]
arr.append(2)
arr.append(4)
arr.append(7)

for i in range(4, n + 1):
    arr.append(arr[i-1] + arr[i-2] + arr[i-3])

print(arr[n])
