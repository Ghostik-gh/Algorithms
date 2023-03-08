
with open('Lab2\input6.txt', 'r') as f:
    string = f.read().strip()


didgits = []
alpha = []
other = []

for i in string:
    if i.isdigit():
        print(i, end=" ")
    elif i.isalpha():
        alpha.append(i)
    else:
        other.append(i)

print(*alpha, "\n", *other, sep="")
