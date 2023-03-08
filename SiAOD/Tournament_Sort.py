with open("input.txt") as f:
    arr = f.readline().strip().split()

arr = list(map(int, arr))
heap = []

if len(arr) < 7:
    heap = arr
else:
    for i in range(7):
        heap.append(arr[-1])
        arr.pop()


def HeapSift(heap, start):
    end = len(heap) - 1
    while True:
        left = start * 2 + 1
        right = start * 2 + 2
        if left > end:
            break

        if left == end:
            if heap[left] < heap[start]:
                heap[left], heap[start] = heap[start], heap[left]
            break

        if right <= end:
            if heap[left] < heap[start] and heap[left] <= heap[right]:
                heap[left], heap[start] = heap[start], heap[left]
                HeapSift(heap, left)
            if heap[right] < heap[start] and heap[right] < heap[left]:
                heap[right], heap[start] = heap[start], heap[right]
                HeapSift(heap, right)
            break


for start in range((len(heap) - 2)//2, -1, -1):
    HeapSift(heap, start)

print(heap)

winners = []
losers = []

while len(heap) > 0:
    pass
    if len(arr) > 0:
        winners.append(heap[0])
        heap.pop(0)

        if arr[-1] < winners[-1]:
            losers.append(arr[-1])
            arr.pop()
            HeapSift(heap, 0)
        else:
            heap.insert(0, arr[-1])
            arr.pop()
            HeapSift(heap, 0)
    else:
        winners.append(heap[0])
        heap.pop(0)
        HeapSift(heap, 0)

print(winners)
print(losers)
print(heap)
