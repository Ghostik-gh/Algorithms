def coord_to_num(x, y):
    return (y - 1)*2 + x


def num_to_coord(num):
    x = 0
    y = 0
    if num % 2 == 0:
        x = 2
        y = num/2
    else:
        x = 1
        y = (num+1)/2
    return x, int(y)


with open('input.txt', 'r') as f:
    people = int(f.readline().strip())
    variants = int(f.readline().strip())
    y = int(f.readline().strip())
    x = int(f.readline().strip())


out = open('output.txt', 'w')
petya_num = int(coord_to_num(x, y))

forw_num = petya_num - variants
back_num = petya_num + variants


forw_x, forw_y = num_to_coord(forw_num)
back_x, back_y = num_to_coord(back_num)

flag = True
# print(forw_x, forw_y)
# print(back_x, back_y)
# print(forw_num)
# print(back_num)


if forw_num <= 0 and back_num < people:
    out.write(f"{back_y} {back_x}")

elif back_num > people and forw_num > 0:
    out.write(f"{forw_y} {forw_x}")

elif back_y - y > y - forw_y:
    out.write(f"{forw_y} {forw_x}")

elif back_y - y <= y - forw_y:
    if back_num > people:
        out.write("-1")
    else:
        out.write(f"{back_y} {back_x}")

else:
    out.write("-1")


out.close()
