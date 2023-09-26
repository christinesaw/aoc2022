input = """noop
noop
addx 5
addx 29
addx -28
addx 5
addx -1
noop
noop
addx 5
addx 12
addx -6
noop
addx 4
addx -1
addx 1
addx 5
addx -31
addx 32
addx 4
addx 1
noop
addx -38
addx 5
addx 2
addx 3
addx -2
addx 2
noop
addx 3
addx 2
addx 5
addx 2
addx 3
noop
addx 2
addx 3
noop
addx 2
addx -32
addx 33
addx -20
addx 27
addx -39
addx 1
noop
addx 5
addx 3
noop
addx 2
addx 5
noop
noop
addx -2
addx 5
addx 2
addx -16
addx 21
addx -1
addx 1
noop
addx 3
addx 5
addx -22
addx 26
addx -39
noop
addx 5
addx -2
addx 2
addx 5
addx 2
addx 23
noop
addx -18
addx 1
noop
noop
addx 2
noop
noop
addx 7
addx 3
noop
addx 2
addx -27
addx 28
addx 5
addx -11
addx -27
noop
noop
addx 3
addx 2
addx 5
addx 2
addx 27
addx -26
addx 2
addx 5
addx 2
addx 4
addx -3
addx 2
addx 5
addx 2
addx 3
addx -2
addx 2
noop
addx -33
noop
noop
noop
noop
addx 31
addx -26
addx 6
noop
noop
addx -1
noop
addx 3
addx 5
addx 3
noop
addx -1
addx 5
addx 1
addx -12
addx 17
addx -1
addx 5
noop
noop
addx 1
noop
noop"""



# input = """noop
# addx 3
# addx -5"""

# input = """addx 15
# addx -11
# addx 6
# addx -3
# addx 5
# addx -1
# addx -8
# addx 13
# addx 4
# noop
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx -35
# addx 1
# addx 24
# addx -19
# addx 1
# addx 16
# addx -11
# noop
# noop
# addx 21
# addx -15
# noop
# noop
# addx -3
# addx 9
# addx 1
# addx -3
# addx 8
# addx 1
# addx 5
# noop
# noop
# noop
# noop
# noop
# addx -36
# noop
# addx 1
# addx 7
# noop
# noop
# noop
# addx 2
# addx 6
# noop
# noop
# noop
# noop
# noop
# addx 1
# noop
# noop
# addx 7
# addx 1
# noop
# addx -13
# addx 13
# addx 7
# noop
# addx 1
# addx -33
# noop
# noop
# noop
# addx 2
# noop
# noop
# noop
# addx 8
# noop
# addx -1
# addx 2
# addx 1
# noop
# addx 17
# addx -9
# addx 1
# addx 1
# addx -3
# addx 11
# noop
# noop
# addx 1
# noop
# addx 1
# noop
# noop
# addx -13
# addx -19
# addx 1
# addx 3
# addx 26
# addx -30
# addx 12
# addx -1
# addx 3
# addx 1
# noop
# noop
# noop
# addx -9
# addx 18
# addx 1
# addx 2
# noop
# noop
# addx 9
# noop
# noop
# noop
# addx -1
# addx 2
# addx -37
# addx 1
# addx 3
# noop
# addx 15
# addx -21
# addx 22
# addx -6
# addx 1
# noop
# addx 2
# addx 1
# noop
# addx -10
# noop
# noop
# addx 20
# addx 1
# addx 2
# addx 2
# addx -6
# addx -11
# noop
# noop
# noop
# """


input_list = input.split()
# print(input_list)
cycle = 1
x_val = 1
final_sum = 0


# ######################## part one ########################
# for each in input_list:
#     if cycle == 20:
#         # print(cycle*x_val)
#         final_sum += cycle*x_val
#     elif cycle == 60:
#         # print(cycle*x_val)
#         final_sum += cycle*x_val
#     elif cycle == 100:
#         # print(cycle*x_val)

#         final_sum += cycle*x_val
#     elif cycle == 140:
#         # print(cycle*x_val)

#         final_sum += cycle*x_val
#     elif cycle == 180:
#         # print(cycle*x_val)

#         final_sum += cycle*x_val
#     elif cycle == 220:
#         # print(cycle*x_val)
#         # print(cycle)
#         # print(x_val)
#         final_sum += cycle*x_val

#     if each == 'noop':
#         cycle += 1

#     elif each == 'addx':
#         cycle += 1

#     else:
#         x_val += int(each)
#         cycle += 1
# print(final_sum)
# ######################## part one ########################


# ######################## part two ########################

pxls = ''
cycle = 1
x_val = 1
cnt_pxls = 0

for ii in range(len(input_list)):

    crt = cycle-1
    sprite_range = [x_val-1, x_val, x_val+1]
    print(sprite_range)
    # print(crt)
    print(input_list[ii])
    if crt in sprite_range:
        pxls += '#'
    else:
        pxls += '.'
        
    if input_list[ii] == "noop":
        cycle += 1

    elif input_list[ii] == 'addx':
        cycle += 1

    else:
        x_val += int(input_list[ii])
        cycle +=1

    cnt_pxls += 1
    if cnt_pxls in [40,80,120,160,200,240]:
        pxls += '\n'
        cycle = 1

print(pxls)

# ######################## part two ########################
