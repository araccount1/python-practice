user_input = input()

first_space = True
    
for index in range(len(user_input)):
    if user_input[index] == ' ':
        if first_space == True:
            first_space = False
            print(index, end ='')
        elif first_space == False:
            print(f', {index}', end ='')
                      
if ' ' not in user_input:
    print('no spaces found')