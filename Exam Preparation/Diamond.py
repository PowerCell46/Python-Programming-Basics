input_number = int(input())

start_list = [" "]
normal_list = []

for i in range(((input_number) -1), -1, -1):
    start_list.append("*")
    start_list.append(" ")

normal_list.append("".join(start_list))

for i in range(((input_number -2)), -1, -1):
    if "*" in start_list:
        index_1 = start_list.index("*")
        start_list.pop(index_1)
    start_list.append(" ")
    normal_list.append("".join(start_list))

for i in range(len(normal_list) -1, -1, -1):
    print(normal_list[i])

for i in range(1, len(normal_list),):
    print(normal_list[i])
