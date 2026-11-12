S = int(float(input()))

if S <= 55867.00:
    bracket = 1
elif 55867.00 <= S <= 111733.00:
    bracket = 2
elif 111733.00 <= S <= 173205.00:
    bracket = 3
elif 173205.00 <= S <= 246752.00:
    bracket = 4
elif S >= 246752.00:
    bracket = 5
else:
    print('Invalid input')
    
print(bracket)