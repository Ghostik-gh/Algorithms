n = int(input())
dp = []
prev = []

# 0
dp.append(-1)
prev.append(-1)

# n = 1
dp.append(0)
prev.append(-1)

# n = 2

dp.append(1)
prev.append(1)

# n = 3

dp.append(1)
prev.append(1)

i = 4
while i <= n:
    if i % 3 == 0 and i % 2 == 0:
        if dp[i//3] <= dp[i//2]:
            dp.append(dp[i//3])
            prev.append(i//3)
        else:
            dp.append(dp[i//2])
            prev.append(i//2)
    elif i % 2 == 0:
        if dp[i//2] < dp[i-1]:
            dp.append(dp[i//2])
            prev.append(i//2)
        else:
            dp.append(dp[i-1])
            prev.append(i-1)
    elif i % 3 == 0:
        if dp[i//3] < dp[i-1]:
            dp.append(dp[i//3])
            prev.append(i//3)
        else:
            dp.append(dp[i-1])
            prev.append(i-1)
    else:
        dp.append(dp[i-1])
        prev.append(i-1)

    dp[-1] += 1
    i += 1


print(dp[n])


cur = prev[-1]
ans = []
ans.append(n)
while cur > 1:
    ans.append(cur)
    cur = prev[cur]
if n != 1:
    ans.append(cur)

ans.reverse()
print(*ans)
