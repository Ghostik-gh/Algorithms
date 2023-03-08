nums = []
with open("input.txt") as f:
    n, m = f.readline().strip().split()
    n = int(n)
    m = int(m)
    for i in range(n):
        tmp = list(map(int, f.readline().strip().split()))
        nums.append(tmp)


ans = [[0] * m for i in range(n)]
dp = [[-1] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            ans[i][j] = nums[0][0]
            dp[i][j] = [-1, -1]
        elif j == 0:
            ans[i][j] = ans[i-1][j] + nums[i][j]
            dp[i][j] = [i-1, j]
        elif i == 0:
            ans[i][j] = ans[i][j-1] + nums[i][j]
            dp[i][j] = [i, j-1]
        else:
            ans[i][j] = max(ans[i-1][j] + nums[i][j],
                            ans[i][j-1] + nums[i][j])
            if ans[i-1][j] + nums[i][j] > ans[i][j-1] + nums[i][j]:
                dp[i][j] = [i-1, j]
            else:
                dp[i][j] = [i, j-1]


# print(*nums, sep="\n")
# print(*ans, sep="\n")
# print(*dp, sep="\n")

print(ans[-1][-1])
i = n - 1
j = m - 1

string = []
while dp[i][j] != [-1, -1]:
    if i != dp[i][j][0]:
        string.append("D")
    else:
        string.append("R")
    i, j = dp[i][j]

string.reverse()

print(*string)
