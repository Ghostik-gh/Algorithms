arr = 1000*[0]

with open('input.txt', 'r') as f:
    str = f.read().strip()
out = open('output.txt', 'w')

for i in str:
    if i in " \n":
        continue
    arr[ord(i)] += 1
arr[ord(" ")] = 0
ma = -1

for i in arr:
    if i > ma:
        ma = i
while ma > 0:
    for i in arr:
        if i == 0:
            continue
        if i >= ma:
            out.write("#")
        else:
            out.write(" ")
    ma -= 1
    out.write("\n")
for i in range(len(arr)):
    if arr[i] != 0:
        out.write(chr(i))

out.close()
