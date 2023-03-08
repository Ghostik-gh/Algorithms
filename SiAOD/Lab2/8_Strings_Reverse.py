
with open('Lab2\input8.txt', 'r') as f:
    string = f.read().split("\n")

ans = []

for i in string:
    ans.insert(0, i)

print(*ans, sep="\n")
