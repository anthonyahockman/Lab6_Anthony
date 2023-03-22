# This is Anthony Hockman's code for Lab 6


# This method displays the menu and asks for user selection
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")
    selection = int(input("Please enter an option: "))
    print("")

    return selection


# This method encodes the user's inputted password
def encode(password):
    encode = ''
    for i in password:
        if (int(i) + 3) > 9:
            dif = (int(i) + 3) - 10
            encode += str(dif)
        else:
            encode += str(int(i) + 3)
    return encode


def decode(string_encoded):  # decode string function
    decoded_string = ""  # start decoded string as empty string
    for i in string_encoded:
        temp = int(i) - 3  # create a variable for new value of decoded number
        if temp < 0:
            decoded_string += str(temp + 10)  # if less than 0, add 10
        else:
            decoded_string += str(temp)  # if not, add the value
    return decoded_string


if __name__ == "__main__":

    power = True
    # This is the main loop for the program
    while power:
        selection = menu()
        if selection == 1:
            password = input("Please enter your password to encode: ")  # Store the original password
            encoded_pass = encode(password)  # Store the new encoded password
            print("\nYour password has been encoded and stored!")
        elif selection == 2:
            print(f"The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}.")
        elif selection == 3:
            power = False  # Terminate the program on the next loop
        else:
            print("Invalid selection! Please enter a menu option 1 - 3.")  # Ask the user for a proper input
