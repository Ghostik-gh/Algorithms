with open('input.txt', 'r') as f:
    string = f.read().strip()


arr = []
for i in string.split():
    if i.isnumeric():
        arr.append(int(i))
    else:
        result = 0
        if i == "+":
            result = arr[-1] + arr[-2]
        elif i == "-":
            result = arr[-2] - arr[-1]
        else:
            result = arr[-1] * arr[-2]
        arr.pop()
        arr.pop()
        arr.append(result)

out = open('output.txt', 'w')

out.write(f"{arr[0]}")

out.close()
