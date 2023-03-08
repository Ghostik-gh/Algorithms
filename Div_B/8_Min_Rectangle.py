arr_x = []
arr_y = []
with open('input.txt', 'r') as f:
    k = int(f.readline().strip())
    for i in range(k):
        x, y = f.readline().split()
        # y = int(f.read())
        arr_x.append(int(x))
        arr_y.append(int(y))

# print(arr_x)
# print(arr_y)

min_x = int(10e10)
max_x = int(-10e10)
min_y = int(10e10)
max_y = int(-10e10)

for i in arr_x:
    if i < min_x:
        min_x = i
    if i > max_x:
        max_x = i

for i in arr_y:
    if i < min_y:
        min_y = i
    if i > max_y:
        max_y = i


out = open('output.txt', 'w')

# print(min_x, min_y, max_x, max_y)
out.write(f"{min_x} {min_y} {max_x} {max_y}")

out.close()
