# def switch_A_B():
#     if len(a) == 0 and len(b) == 0:
#         return

#     if len(a) != 0 and (len(b) == 0 or b[-1] > a[-1]):
#         b.append(a[-1])
#         a.pop()
#     else:
#         a.append(b[-1])
#         b.pop()


# def switch_A_C():
#     if len(a) == 0 and len(c) == 0:
#         return

#     if len(a) != 0 and (len(c) == 0 or c[-1] > a[-1]):
#         c.append(a[-1])
#         a.pop()
#     else:
#         a.append(c[-1])
#         c.pop()


# def switch_B_C():
#     if len(b) == 0 and len(b) == 0:
#         return

#     if len(b) != 0 and (len(c) == 0 or c[-1] > b[-1]):
#         c.append(b[-1])
#         b.pop()
#     else:
#         b.append(c[-1])
#         c.pop()


with open('Lab2\input3.txt', 'r') as f:
    n = int(f.read().strip())

a = []
b = []
c = []


def switch(stack1, stack2):
    if len(stack1) == 0 and len(stack2) == 0:
        return

    if len(stack1) != 0 and (len(stack2) == 0 or stack2[-1] > stack1[-1]):
        stack2.append(stack1[-1])
        stack1.pop()
    else:
        stack1.append(stack2[-1])
        stack2.pop()


for i in range(n, 0, -1):
    a.append(i)

while len(c) != n:
    print(a, b, c)
    if n % 2 == 0:
        switch(a, b)
        switch(a, c)
        switch(b, c)
        # switch_A_B()
        # switch_A_C()
        # switch_B_C()
    else:
        switch(a, c)
        switch(a, b)
        if len(c) == n:
            break
        switch(b, c)
        # switch_A_C()
        # switch_A_B()
        # switch_B_C()


print(a, b, c)
