#Encoder/Decoder App By: Blake Coppens and Evan Harden

userPass = ''
convertedPass = ''
def encodeFunction(): # Blake Coppens' Encoder Function
    global userPass, convertedPass
    userPass = input("Please enter your password.\n")
    if len(userPass) > 8:
        print("Error! User password is longer than 8 digits.\nShortening to 8 digits...")
        userPass = userPass[:8] #Shortens the length of the password to 8 digits.
    for i in userPass:
        convertednum = int(i)+3
        if convertednum >9:
            if convertednum == 10:
                convertednum = 0
            elif convertednum == 11:
                convertednum = 1
            elif convertednum == 12:
                convertednum = 2
        convertedPass += str(convertednum)
    print(f"The result is: {convertedPass}") # IDK if this needs to be here but in case its just here to show that it works.
    return convertedPass


def decodeFunction(password):  #Evan Harden's awesome decoder
    decoded_list = []
    decoded_pw = ''
    for i in password:
        decoded_list.append(str(int(i) + 7))
    for i in decoded_list:
        decoded_pw += i[-1]
    return decoded_pw

def main(): # This is the main loop that will be repeated, add an if statement to edit it here
    UserInput = int(input("Choose your option:\n1. Encoder\n2. Decoder\n"))
    if UserInput == 1:
        encodeFunction()
    elif UserInput == 2:
        password = input("Enter password to be decoded: ")
        print(f'Your password has been decoded: {decodeFunction(password)}')
    else:
        print("Invalid Selection.")
        

if __name__ == '__main__': #Unit test
    main()