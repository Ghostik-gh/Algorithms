
with open('input.txt', 'r') as f:
    k = int(f.readline().strip())
    string = f.readline().strip()

windowStart = 0
maxLetterCount = 0
maxLength = 0
charFreqMap = {}

for i in range(len(string)):
    charFreqMap[string[i]] = 0

for i in range(len(string)):
    charFreqMap[string[i]] += 1

    maxLetterCount = max(windowStart, charFreqMap[string[i]])

    if i - windowStart + 1 - maxLetterCount > k:
        charFreqMap[string[windowStart]] -= 1
        windowStart += 1

    maxLength = max(maxLength, i - windowStart + 1)

out = open('output.txt', 'w')

out.write(f"{maxLength}")

out.close()
