customers = []
with open("input.txt") as f:
    n = int(f.readline().strip())
    for i in range(n):
        nums = f.readline().strip().split()
        nums = list(map(int, nums))
        customers.append(nums)

dp = [0]
if n == 1:
    print(customers[0][0])
elif n == 2:
    print(min(customers[0][1], customers[0][0] + customers[1][0]))
else:
    dp.append(customers[0][0])
    dp.append(min(customers[0][1], customers[0][0] + customers[1][0]))
    cur = 2
    while cur < n:
        a = dp[-3] + customers[cur-2][2]
        b = dp[-2] + customers[cur-1][1]
        c = dp[-1] + customers[cur][0]
        # print(a)
        # print(b)
        # print(c, end="\n===========\n")
        dp.append(min(a, b, c))
        cur += 1
    print(dp[-1])
