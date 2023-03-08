arr: list[int] = list()
with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    path_1 = f.readline().strip().split()

out = open('output.txt', 'w')

stack = []
path_2 = []

for i in range(len(path_1)):
    path_1[i] = int(path_1[i])

cur = 1

while len(path_1) != 0:
    tmp = path_1[0]
    path_1.pop(0)

    if tmp == cur:
        path_2.append(tmp)
        cur += 1
    else:
        stack.append(tmp)
        continue

    while len(stack) > 0 and stack[-1] == cur:
        path_2.append(stack[-1])
        stack.pop()
        cur += 1
        if cur > n:
            break

if len(stack) == 0:
    out.write("YES")
else:
    out.write("NO")


out.close()
