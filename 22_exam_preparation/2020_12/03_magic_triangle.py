def get_magic_triangle(current_num: int):
    num_list = []
    for x in range(current_num):
        current_list = []
        if x == 0:
            num_list.append([1])
            continue
        else:
            for y in range(len(num_list[x - 1]) + 1):
                first_num_index = y - 1
                if first_num_index < 0:
                    first_num = 0
                else:
                    first_num = int(num_list[x - 1][first_num_index])
                second_num_index = y
                if second_num_index == len(num_list[x - 1]):
                    second_num = 0
                else:
                    second_num = int(num_list[x - 1][second_num_index])

                current_list.append(first_num + second_num)
        num_list.append(current_list)

    return num_list


print(get_magic_triangle(10))
