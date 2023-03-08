
arr = []
out = open('output.txt', 'w')
with open('input.txt', 'r') as f:
    string = ""
    while string != "exit":
        string = f.readline().strip()

        if string[:4] == "push":
            arr.append(string[5:])
            out.write("ok\n")

        if string == "pop":
            if len(arr) == 0:
                out.write("error\n")
            else:
                out.write(arr[0]+"\n")
                arr.pop(0)

        if string == "front":
            if len(arr) == 0:
                out.write("error\n")
            else:
                out.write(arr[0]+"\n")

        if string == "size":
            out.write(f"{len(arr)}\n")

        if string == "clear":
            arr = []
            out.write("ok\n")

        if string == "exit":
            out.write("bye\n")

out.close()
