
def findLen(string, k, ch):
    maxlen = 1
    count = 0
    l = 0
    r = 0
    while r < len(string):

        if string[r] != ch:
            count += 1

        while count > k:
            if string[l] != ch:
                count -= 1
            l += 1

        maxlen = max(maxlen, r - l + 1)
        r += 1

    return maxlen


def answer(string, k):
    maxlen = 1

    charFreqMap = {}
    for i in range(len(string)):
        charFreqMap[string[i]] = 0

    for i in charFreqMap:
        maxlen = max(maxlen, findLen(string, k, i))

    return maxlen


with open('input.txt', 'r') as f:
    k = int(f.readline().strip())
    string = f.readline().strip()

out = open('output.txt', 'w')

out.write(f"{answer(string, k)}")

out.close()
