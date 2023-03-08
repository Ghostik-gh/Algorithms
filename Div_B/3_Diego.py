from bisect import bisect_left

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    arr1 = f.readline().strip().split()
    k = int(f.readline().strip())
    arr2 = f.readline().strip().split()


arr1 = set(arr1)

arr1 = list(map(int, arr1))
arr2 = list(map(int, arr2))

arr1.sort()


out = open('output.txt', 'w')
for i in arr2:
    index = bisect_left(arr1, i)
    out.write(f"{index}\n")


out.close()
