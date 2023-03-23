#Vasilios Voyatzoglou UFID: 58855925
#Universty of Florida COP3502C
#Description: Encoder and debugger demonstration

#encodes string by adding 3 to each digit
def encode(message):

    #init result string
    result = ""

    #loop through each digit in original string
    for digit in message:

        #add 3 when less than 7
        if int(digit) < 7:
            result = result + str(int(digit) + 3)

        #else subtract 7
        else:
            result = result + str(int(digit) - 7)

    #return string
    return result

#decodes string by subtracting 3 from each digit
def decode(message):

    #init result string
    result = ""

    #loop through each digit in original string
    for digit in message:

        #subtract 3 when greater than 2
        if int(digit) > 2:
            result = result + str(int(digit) - 3)

        #else add 7
        else:
            result = result + str(int(digit) + 7)

    #return string
    return result

if __name__ == "__main__":

    program_continue = True

    #main loop
    while program_continue:

        #ask user for program select
        select = input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\nPlease enter an option: ")

        #encode
        if select == "1":
            password = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")

        #decode
        elif select == "2":
            print("The encoded password is " + password + ", and the original password is " + decode(password) + ".")

        #quit program
        elif select == "3":
            program_continue = False

        #invalid selectg
        else:
            print("Invalid selection!")