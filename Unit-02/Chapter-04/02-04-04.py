fizz_buzz_num = int(input())

if (fizz_buzz_num % 3 == 0) and (fizz_buzz_num % 5 == 0):
    output = 'Fizz Buzz'
elif fizz_buzz_num % 3 == 0:
    output = 'Fizz'
elif fizz_buzz_num % 5 == 0:
    output = 'Buzz'
else:
    output = fizz_buzz_num
    
    
print(output)
