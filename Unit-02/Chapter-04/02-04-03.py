A = int(input())
B = int(input())
C = int(input())

if A >= B and A >= C:
    output =  A
elif B >= A and B >= C:
    output = B
elif C >= A and C >= B:
    output = C
else:
    output = 'Error in input'
    
    
print(output)