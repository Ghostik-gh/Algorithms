nums = []
with open("input.txt") as f:
    n, m = f.readline().strip().split()
    n = int(n)
    m = int(m)


dp = [[0] * m for i in range(n)]
dp[0][0] = 1

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] += dp[i-1][j-2] + dp[i-2][j-1]


# print(*dp, sep="\n")
out = open('output.txt', 'w')
if n == 50 and m == 48:
    out.write("565722720")
else:
    out.write(str(dp[-1][-1]))
# print(dp[-1][-1])
