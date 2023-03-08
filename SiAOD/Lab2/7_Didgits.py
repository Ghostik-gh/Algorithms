with open('Lab2\input7.txt', 'r') as f:
    string = map(int, f.read().split())

didgits = []

for i in string:
    if i >= 0:
        didgits.append(i)
    else:
        didgits.insert(0, i)

print(*didgits)
