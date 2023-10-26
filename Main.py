userPass = ''
convertedPass = ''
def encodeFunction(): # This is my encoder function, Feel free to add your decode function or just to put it in the main function.
    global userPass, convertedPass
    userPass = input("Please enter your password.\n")
    if len(userPass) > 8:
        print("Error! User password is longer than 8 digits.\nShortening to 8 digits...")
        userPass = userPass[:8]
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
##def decodeFunction():
    #Place your code here

def main(): # This is the main loop that will be repeated, add an if statement to edit it here
    UserInput = int(input("Choose your option:\n1. Encoder\n2. Decoder\n"))
    if UserInput == 1:
        encodeFunction()
    elif UserInput == 2:
        decodeFunction()
    else:
        print("Invalid Selection.")
    UserInput = 0    
        

while 1==1:
    main()