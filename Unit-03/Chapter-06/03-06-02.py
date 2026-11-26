some_num = int(input())

if 1 <= some_num <= 9:
    for i in range(1, some_num + 1):
        for j in range(1, some_num + 1):
            if j < some_num:
                print(i * j, end=" ")
            else:
                print(i * j)
