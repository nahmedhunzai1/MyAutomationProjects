
def process_number (number1, number2):
    while True:
        try:
            number1 = float(input("Enter any number between 1 and 5 (inclusive): "))
            if number1 > 5 or number1 < 1:
                raise ValueError("Invalid Number! Please enter a number between 1 and 5.")

            number2 = float(input("Enter any number less than 99: "))
            if number2 >= 99 or number2 <= 0:
                raise ValueError("Invalid Number! Please enter a number between 1 and 98.")

            print("Valid inputs received:", number1, number2)
            break  # Exit loop if valid inputs are given

        except ValueError as e:
            print(e)  # Print the actual error message

            for i in range(len(number2)):
                for j in range(len(number2)):
                    if i*j == number1:
                        return (i,j)



