nums = []
with open("input.txt") as f:
    n, m = f.readline().strip().split()
    n = int(n)
    m = int(m)
    for i in range(n):
        tmp = list(map(int, f.readline().strip().split()))
        nums.append(tmp)


ans = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            ans[i][j] = nums[0][0]
        elif j == 0:
            ans[i][j] = ans[i-1][j] + nums[i][j]
        elif i == 0:
            ans[i][j] = ans[i][j-1] + nums[i][j]
        else:
            ans[i][j] = min(ans[i-1][j] + nums[i][j],
                            ans[i][j-1] + nums[i][j])


print(ans[-1][-1])
