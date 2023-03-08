with open("input.txt") as f:
    n = int(f.readline().strip())
    nums = list(map(int, f.read().strip().split()))

print(nums)