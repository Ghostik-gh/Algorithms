import sys
sys.setrecursionlimit(10000)

with open("input.txt") as f:
    n, m = f.readline().strip().split()
    n = int(n)
    m = int(m)
    nums = [[] for i in range(n + 1)]
    for i in range(m):
        fr, to = f.readline().strip().split()
        fr = int(fr)
        to = int(to)
        nums[fr].append(to)
        nums[to].append(fr)

visited = [False for i in range(n + 1)]
components = [0 for i in range(n + 1)]


def dfs(nums, visited, components, now, comp):
    visited[now] = True
    components[now] = comp
    # print(f"был в вершине {now} и добавил ее в {comp} компонент")
    for i in nums[now]:
        if not visited[i]:
            dfs(nums, visited, components, i, comp)


dfs(nums, visited, components, 1, 1)

# print(components)
# print(nums)
# print(visited)

ans = []
ans_count = 0
for i in range(1, n+1):
    if components[i] == 1:
        ans.append(i)
        ans_count += 1

print(ans_count)
ans.sort()
print(*ans)
