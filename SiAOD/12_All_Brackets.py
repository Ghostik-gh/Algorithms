
with open('input.txt', 'r') as f:
    string = f.readline().strip()

arr = []
out = open('output.txt', 'w')
flag = True
for i in range(len(string)):
    if string[i] in "({[":
        arr.append(string[i])

    if len(arr) == 0:
        out.write("no")
        flag = False
        break

    if string[i] in ")}]":
        arr.append(string[i])
        if arr[-1] == ")" and arr[-2] == "(" or\
            arr[-1] == "}" and arr[-2] == "{" or\
                arr[-1] == "]" and arr[-2] == "[":
            arr.pop()
            arr.pop()
        else:
            out.write("no")
            flag = False
            break

if flag:
    if len(arr) != 0:
        out.write("no")
    else:
        out.write("yes")

out.close()
