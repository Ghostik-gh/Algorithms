
def HeapSort(arr):
    # Для каждого у кого есть потомки
    # надо их отсортировать через просейку

    for start in range((len(arr) - 2)//2, -1, -1):
        HeapSift(arr, start)
    ans = []
    while len(arr) != 0:
        ans.append(arr[0])
        arr[0], arr[-1] = arr[-1], arr[0]
        arr.pop()
        HeapSift(arr, 0)

    ans.reverse()
    return ans


def HeapSift(arr, start):
    end = len(arr) - 1
    while True:
        left = start * 2 + 1
        right = start * 2 + 2
        if left > end:
            break

        if left == end:
            if arr[left] > arr[start]:
                arr[left], arr[start] = arr[start], arr[left]
            break

        if right <= end:
            if arr[left] > arr[start] and arr[left] >= arr[right]:
                arr[left], arr[start] = arr[start], arr[left]
                HeapSift(arr, left)
            if arr[right] > arr[start] and arr[right] > arr[left]:
                arr[right], arr[start] = arr[start], arr[right]
                HeapSift(arr, right)
            break


with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    arr = f.readline().strip().split()

arr = list(map(int, arr))
arr = HeapSort(arr)
out = open('output.txt', 'w')

for i in arr:
    out.write(f"{i} ")
out.close()
