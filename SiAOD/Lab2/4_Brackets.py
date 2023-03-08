
# with open('Lab2\input4.txt', 'r') as f:
#     string = f.read()


string = "(())()()()"
stack = []
out = open('output.txt', 'w')
flag = True
for i in range(len(string)):
    if not (string[i] in "()"):
        continue

    if string[i] == "(":
        stack.append(string[i])

    if len(stack) == 0:
        print("no")
        out.write("no")
        flag = False
        break

    if string[i] == ")":
        if stack[-1] == "(":
            stack.pop()

if flag:
    if len(stack) != 0:
        print("no")
        out.write("no")
    else:
        print("yes")
        out.write("yes")

out.close()
