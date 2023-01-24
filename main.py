# Name: Dylan Hussain
# Student Number: C21331063

# Program Description:
# This program gets a user inputted range
# of numbers from 1-n and prints if each
# number from 1-n is a happy number;
# A happy number is when the digits of a
# number are squared and then added together
# then the same thing is done to the value
# of that number until the value is either
# 1 or 4, 1 being happy, 4 being sad.



def square(num):
    '''Takes in a number num, returns the square of num'''
    return num * num

def is_happy_number(num):
    '''
        Takes in a number num, returns the happy number of num.\n
        A happy number is when the digits of a number are squared and added together
        then then the same thing is done to the value of that number until the value is
        either 1 or 4.\n
        1 meaning its happy.\n
        4 meaning is sad.\n
    '''

    # Convert the num to string so we can index it
    num_str = str(num)
    # Convder the num_str into a list of chars
    nums = list(num_str)

    # Gets the total of the numbers being squared and checks if its 1 or 4
    # It will loop until its either 1 or 4
    total = 0
    while (total != 1 and total != 4):
        for i in range(len(nums)):
            total += square(int(nums[i]))

        # Resets the nums char list to the new number
        nums = list(str(total))

        # If its not ready to exit the loop, reset the total
        if total != 1 and total != 4:
            total = 0

    return total == 1    

def print_happy_range(n):
    '''
        Takes in a number n, prints a range of numbers from 1-n where number is a happy number
    '''
    # Loop and print out any happy number
    for i in range(1, n + 1):
        if (is_happy_number(i)):
            print(i, end=' ')
    print('\n')

def get_user_input(string, cast, error):
    '''
        Takes in the values string, cast, and error.\n
        string is the prompt message the user will get when inputting a value.\n
        cast is the type to cast the input to, e.g int.\n
        error is the error message prompt incase the wrong value type is inputted.\n
    '''

    input_valid = False
    while (not input_valid):
        try:
            # Checks to see if the input produces errors
            user_input = cast(input(string))
            if (user_input <= 0):
                # If user input is less than or equal to 0, throw error
                # Not too certain on how to throw an exception in python
                # so I just created a cast error which will get caught.

                user_input = int('error')
        except ValueError:
            # If errors occur; print an error message to output
            print("\n[ERROR]:", error, "\n")
        else:
            # If no errors exit loop and return user_input
            input_valid = True

    return user_input

def main():
    # This is the main function it will
    # get the happy range from the user
    # and output the happy numbers from
    # 1-n using other functions.

    happy_range = get_user_input(
        "\nPlease enter a number: ", # Input prompt message
        int, # Type to cast input to, e.g int(), str()..
        "You did not enter a positive whole number, please try again." # Error Message
    )

    print("\nAll the happy numbers that add up to {:d} are:".format(happy_range))
    print_happy_range(happy_range)

main()