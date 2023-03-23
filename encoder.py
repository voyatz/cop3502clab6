#Vasilios Voyatzoglou UFID: 58855925
#Universty of Florida COP3502C
#Description: Encoder and debugger demonstration


def encode(message):
    result = ""
    for digit in message:
        if int(digit) < 7:
            result = result + str(int(digit) + 3)
        else:
            result = result + str(int(digit) - 7)
    return result

def decode(message):
    result = ""
    for digit in message:
        if int(digit) > 2:
            result = result + str(int(digit) - 3)
        else:
            result = result + str(int(digit) + 7)
    return result

if __name__ == "__main__":
    program_continue = True
    while program_continue:
        select = input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\nPlease enter an option: ")

        if select == "1":
            password = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")

        elif select == "2":
            print("The encoded password is " + password + ", and the original password is " + decode(password) + ".")

        elif select == "3":
            program_continue = False

        else:
            print("Invalid selection!")