
arr = []
with open('input.txt', 'r') as f:
    first = f.readline().strip().split()
    second = f.readline().strip().split()

first = list(map(int, first))
second = list(map(int, second))

out = open('output.txt', 'w')

cur = 0

while (len(first) != 0 and len(second) != 0) and cur < 1000000:
    cur += 1

    if first[0] == 9 and second[0] == 0:
        second.append(first[0])
        second.append(second[0])
        first.pop(0)
        second.pop(0)
        continue

    if first[0] == 0 and second[0] == 9:
        first.append(first[0])
        first.append(second[0])
        first.pop(0)
        second.pop(0)
        continue

    if first[0] > second[0]:
        first.append(first[0])
        first.append(second[0])
        first.pop(0)
        second.pop(0)
    else:
        second.append(first[0])
        second.append(second[0])
        first.pop(0)
        second.pop(0)

if len(first) == 0:
    out.write(f"second {cur}")
elif len(second) == 0:
    out.write(f"first {cur}")
else:
    out.write("botva")


out.close()
