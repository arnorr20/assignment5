# Design an algorithm that generates the first n numbers 
# in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, 

# User inputs an integer
# For as many times as user input
# run the sequence that prints n every time
# if n gets higher than 3 then
# n is the sum of previous 3 printed numbers
# for exapmle: 1+2+3=6 then 2+3+6=11

n = int(input("Enter the length of the sequence: ")) # Do not change this line
a,b,c=1,2,3
for i in range(1,n+1):
    
    if i < 4:
        print(i)
    else:
        sum_num = a+b+c
        print(sum_num)
        a,b,c = b,c,sum_num
