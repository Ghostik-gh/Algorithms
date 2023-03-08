with open('input.txt', 'r') as f:
    k = int(f.readline().strip())
    for i in range(k):
        n = int(f.readline().strip())
        path_1 = f.readline().strip().split()

        out = open('output.txt', 'w')

        stack = []
        path_2 = []

        stack.append(path_1[0])
        path_1.pop(0)

        while len(path_1) != 0:
            if path_2[-1] > stack[-1] and path_2[-1] > path_1[0]:
                out.write("0\n")
                break
            elif path_2[-1] < stack[-1] and stack[-1] <= path_1[0]:
                path_2.append(stack[-1])
                stack.pop()
            else:
                path_2.append(path_1[0])
                path_1.pop(0)
