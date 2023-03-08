
with open('Lab2\input4.txt', 'r') as f:
    string = f.read()

stack = []
out = open('output.txt', 'w')
flag = True
for i in range(len(string)):
    if not (string[i] in "[]"):
        continue

    if string[i] in "[":
        stack.append(string[i])

    if len(stack) == 0:
        print("no")
        out.write("no")
        flag = False
        break

    if string[i] in "]":
        stack.append(string[i])
        if stack[-2] == "[" and stack[-1] == "]":
            stack.pop()
            stack.pop()
        else:
            print("no")
            out.write("no")
            flag = False
            break

if flag:
    if len(stack) != 0:
        print("no")
        out.write("no")
    else:
        print("yes")
        out.write("yes")

out.close()
