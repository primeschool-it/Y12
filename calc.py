#Operations :
# # + , - ,  * , /
# 1 : +
# 2 : -
# 3 : *
# 4 : /

def get_two_numbers():
    user_input = input("Enter two numbers, comma separated!")
    numbers = user_input.split(',')
    n1 = int(numbers[0])
    n2 = int(numbers[1])
    return  n1, n2

operation = input( "Press 1 for addition \n Press 2 for substraction \n press 3 for multiplication \n press 4 for division: \n")
if operation == '1':
    print ("You chose +")
    n1, n2 =
    print("The sum of both numbers is:", n1 + n2)
elif operation == '2':
    print("You chose -")
    n1, n2 = get_two_numbers()
    print("The substraction of both numbers is:", n1 - n2)
elif operation == '3':
    print ("You chose *")
    n1, n2 = get_two_numbers()
    print("The multiplication of both numbers is:", n1 * n2)
elif operation == '4':
    print ("You chose /")
    n1, n2 = get_two_numbers()
    print("The division of both numbers is:", n1 / n2)
else:
    print ("Wrong Choice!!")