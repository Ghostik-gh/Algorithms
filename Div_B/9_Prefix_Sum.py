def rows_sum(
        first: list[int],
        second: list[int]
) -> list[int]:
    sum_: list[int] = []
    for i in range(len(first)):
        sum_.append(first[i] + second[i])
    return sum_


n, m, k = map(int, input().split())

pref_matrix: list[list[int]] = [[]] * n
pref_matrix.insert(0, [0] * (m + 1))
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    pref_row = [0]
    for j in range(1, m + 1):
        pref_row.append(
            pref_row[j - 1] + row[j - 1]
        )
    pref_row = rows_sum(pref_row, pref_matrix[i - 1])
    pref_matrix[i] = pref_row

for _ in range(k):
    x_from, y_from, x_to, y_to = map(int, input().split())
    sum_ = pref_matrix[x_to][y_to] - pref_matrix[x_from - 1][y_to] - pref_matrix[x_to][y_from - 1] + \
           pref_matrix[x_from - 1][y_from - 1]
    print(sum_)
