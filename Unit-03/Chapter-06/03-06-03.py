some_num = int(input())

if 1 <= some_num <= 9:
    for i in range(some_num, 0, -1):
        for j in range(i, 0, -1):
            print(f'{j} ', end ='')
        print()