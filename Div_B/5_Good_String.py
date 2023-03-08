n = int(input())
min = -1
a = []
p = int(input())
a.append(p)
s = 0
for i in range(n-1):
    p = int(input())
    if p > a[-1]:
        s += a[-1]
    else:
        s += p
    a.append(p)
print(s)
