arr = []

out = open('output.txt', 'w')

with open('input.txt', 'r') as f:
    string = ""
    while string != "exit":
        string = f.readline().strip()

        if string[:10] == "push_front":
            arr.append(string[11:])
            out.write("ok\n")

        if string[:9] == "push_back":
            tmp = arr
            arr = []
            arr.append(string[10:])
            arr += tmp
            out.write("ok\n")

        if string == "pop_front":
            if len(arr) == 0:
                out.write("error\n")
            else:
                out.write(f"{arr[-1]}\n")
                arr.pop()

        if string == "pop_back":
            if len(arr) == 0:
                out.write("error\n")
            else:
                out.write(f"{arr[0]}\n")
                arr.pop(0)

        if string == "front":
            if len(arr) == 0:
                out.write("error\n")
            else:
                out.write(f"{arr[-1]}\n")

        if string == "back":
            if len(arr) == 0:
                out.write("error\n")
            else:
                out.write(f"{arr[0]}\n")

        if string == "size":
            out.write(f"{len(arr)}\n")

        if string == "clear":
            arr = []
            out.write("ok\n")

        if string == "exit":
            out.write("bye\n")

out.close()
