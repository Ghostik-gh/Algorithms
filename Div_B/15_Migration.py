# Нахождение близжайщего правого

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    arr = f.readline().strip().split()

arr = list(map(int, arr))
stack = []
ans = [-1]*n

for i in range(len(arr)):
    if len(stack) == 0 or stack[-1][0] < arr[i]:
        stack.append([arr[i], i])
    else:
        while len(stack) > 0 and arr[i] < stack[-1][0]:
            ans[stack[-1][1]] = i
            stack.pop()
        stack.append([arr[i], i])

out = open('output.txt', 'w')

for i in ans:
    out.write(f"{i} ")

out.close()
