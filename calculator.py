from idna import valid_string_length


def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        print("Invalid: ")
    else:
        return x/y


def calculator():
    print("Select any one option: ")
    print("1- Addition: ")
    print("2- Subtraction: ")
    print ("3- Multiplication: ")
    print("4- Division: ")



    choice = input("Enter choice (1/2/3/4): ")



        # calculator()



    try:

        if choice not in ["1", "2", "3", "4"]:
            raise ValueError("Invalid input : ")


        input1 = float(input("Enter First Number: "))
        input2 = float(input("Enter Second Number:  "))

        if choice == "1":
            addition_result = input1 + input2
            print(addition_result)

        elif choice == "2":
            subtraction_result = input1 - input2
            print(subtraction_result)

        elif choice == "3":
            multiplication_result = input1 * input2
            print(multiplication_result)

        elif choice == "4":
            division_result = input1 / input2
            print(division_result)
        else:
            print("invalid Input: ")
    except ValueError:
        print("invalid Input! Please try again.: ")
        calculator()





calculator()



