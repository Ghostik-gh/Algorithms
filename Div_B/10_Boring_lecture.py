
with open('input.txt', 'r') as f:
    k = f.readline().strip()

letters = dict()

for i in k:
    letters[i] = 0


for i in range(len(k)):
    letters[k[i]] += (len(k) - i) * (i + 1)


letters = dict(sorted(letters.items()))
out = open('output.txt', 'w')

for i in letters:
    out.write(f"{i}: {letters.get(i)}\n")


out.close()
