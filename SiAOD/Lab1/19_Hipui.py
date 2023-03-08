def HeapSift(heap, pos):
    end = len(heap) - 1
    left = pos * 2 + 1
    right = pos * 2 + 2

    while True:
        if left > end:
            break

        if left == end:
            if heap[left] > heap[pos]:
                heap[left], heap[pos] = heap[pos], heap[left]
            break

        if right <= end:
            if heap[left] >= heap[right]:
                if heap[left] > heap[pos]:
                    heap[left], heap[pos] = heap[pos], heap[left]
                    HeapSift(heap, left)
            else:
                if heap[right] > heap[pos]:
                    heap[right], heap[pos] = heap[pos], heap[right]
                    HeapSift(heap, right)
        break


def HeapSiftTop(heap, pos):
    if pos == 0:
        return
    parent = (pos - 1)//2

    if heap[parent] < heap[pos]:
        heap[parent], heap[pos] = heap[pos], heap[parent]
        HeapSiftTop(heap, parent)


heap = []
out = open('output.txt', 'w')

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    for i in range(n):
        command = f.readline().strip()

        if command == '1':
            out.write(f"{heap[0]}\n")
            heap[0] = heap[-1]
            heap.pop()
            HeapSift(heap, 0)
        else:
            heap.append(int(command[2:]))
            HeapSiftTop(heap, len(heap) - 1)

out.close()
