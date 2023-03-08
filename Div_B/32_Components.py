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


comp = 0
for i in range(1, len(nums)):
    if not visited[i]:
        comp += 1
        dfs(nums, visited, components, i, comp)

print(comp)
print(visited)
# print(components)

ans = [0] * (comp + 1)
print(ans)
tmp = 1
# while tmp <= comp:
for i in range(1, len(components)):
    ans[components[i]] += 1
print(ans)
