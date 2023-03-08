with open("input.txt") as f:
    n = int(f.readline().strip())
    nums = f.readline().strip().split()

nums = list(map(int, nums))

nums.sort()

dp = [0 for i in range(n)]


def maxl(i):
    if i > n - 3:
        return 0
    if dp[i] == 0:
        dp[i] = nums[i+1] - nums[i] + max(maxl(i + 2), maxl(i + 3))
    return dp[i]


print(nums[-1] - nums[0] - max(maxl(1), maxl(2)))
