# The max integer algorithm is going to repeatedly ask the user to input an
# integer and but stop if the integer gets negative.
# When the integer gets negative and the program stops it
# is going to print out the highest integer the user inputed over that session.

# Repeatedly ask user for a integer
# if integer is positive
# store integer in a varible max_int
# if it is higher than the number stored in max_int
# if user input is a negative integer
# stop asking user to input a number
# and output the number stored in max_int variable


num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

max_int = 0

while num_int >= 0:

    # Store integer in max_int if the integer is higher than stored value
    if num_int > max_int:
        max_int = num_int
    
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line
