#PHASE 1: CHECKING AND SORTING USER INPUT

#First I make a function to capture the user input and make sure it aligns with what we want the user to input
def user_input_capture():

    userInput = input("Please enter your ISBN code to validate it.\nExample: 0987654321\n")
    userInput = userInput.upper() #Using the .upper() to make any X be X

    #Before I send the user Input to the next function I am going to loop through and make sure every index is appropriate
    x = 0

    for x in range(x, len(userInput)):

        i = userInput[x]

        #The code will do nothing if the checks are correct
        if ((i=="1") or (i=="2") or (i=="3") or (i=="4") or (i=="5") or (i=="6") or (i=="7") or (i=="8") or (i=="9") or (i=="0")):
            n = 0
            
        elif ((x == len(userInput) - 1) and (i == "X")):
            n = 0
        
        else:

            #If the string contains an inappropriate value I will ask the user to try again
            print("You have entered in invalid input: " + userInput[x] + ".\nPlease Try Again")
            user_input_capture()

        x += 1

    return input_sort(userInput) #Calling the next function with the user input as the parameters to sort the ISBN

#Next I create a function that will check which ISBN my code should be checking (10 or 13)
def input_sort(userISBN):

    length = len(userISBN) #I store the length of the userISBN for ease of use 

    if (length == 10):

        isbn_ten_check(userISBN)

    elif (length == 13):

        isbn_thirteen_check(userISBN)

    else:

        print("You have entered an invalid ISBN: " + userISBN + ". This has the incorrect amount of digits to be an ISBN-10 or ISBN-13")


#This function will do the final checks before validation of the ISBN 10
def isbn_ten_check(userISBN):

    isbnList = []

    #The code needs to find if there is an x and change it to 10
    if (userISBN[9] == "X"):
        
        x = 0

        for x in range(x, len(userISBN) - 1):

            isbnList.append(int(userISBN[x])) #This will change to variable int and add it to the list


        isbnList.append(10) #Since this is for the case that the final index is X so I make it 10

    else:

        x = 0

        for x in range(x, len(userISBN)):

            isbnList.append(int(userISBN[x]))

    return isbn_ten_valid(isbnList)

#This function will do the final checks before validation of the ISBN 13
def isbn_thirteen_check(userISBN):

    isbnList = []

    if (userISBN[12] == "X"):

        x = 0

        for x in range(x, len(userISBN) - 1):

            isbnList.append(int(userISBN[x]))

        isbnList.append(10)

    else:

        x = 0

        for x in range(x, len(userISBN)):

            isbnList.append(int(userISBN[x]))

    return isbn_thirteen_valid(isbnList)


#PHASE 2: VALIDATION CHECK

#This function will validate the ISBN 10
def isbn_ten_valid(isbnList):

    x = 0
    y = 10
    sum = 0

    for x in range(x, 10):

        sum += isbnList[x] * y

        x += 1
        y -= 1

    if (sum % 11 == 0):
        
        isbn_ten_add(isbnList)

    elif (sum % 11 != 0):

        print("Your ISBN-10 is Invalid\n")
        user_input_capture()

#This function will validate the ISBN 13
def isbn_thirteen_valid(isbnList):

    x = 0
    sum = 0

    for x in range(x, 13):

        if ((x == 0) or (x % 2 == 0)): #the first number and every second one after that must be multiplied by 1

            sum += isbnList[x]

        elif (x % 2 != 0): #every second number must be multiplied by 3

            sum += isbnList[x] * 3

    if (sum % 10 == 0):

        print("Your ISBN-13 is Valid")

    elif (sum % 10 != 0):

        print("Your ISBN-13 is Invalid\n")
        user_input_capture()

#This function will add 9 7 8 to the beginning of the list to begin the convertion process
def isbn_ten_add(isbnList):

    newISBNList = [9, 8, 7]
    x = 0

    for x in range(x, len(isbnList)):

        newISBNList.append(isbnList[x])

    return isbn_ten_convert(newISBNList)

#This function will validate the new ISBN-13
def isbn_ten_convert(newISBNList):

    x = 0
    sum = 0

    for x in range(x, len(newISBNList)):

        if ((x == 0) or (x % 2 == 0)): 

            sum += newISBNList[x]

        elif (x % 2 != 0):

            sum += newISBNList[x] * 3

    if (sum % 10 == 0):

        #The following lines of code format the output for the user
        strISBN = ' '.join(str(newISBNList))
        strISBN = strISBN.replace(' ', '')
        strISBN = strISBN.replace('[', '')
        strISBN = strISBN.replace(']', '')
        strISBN = strISBN.replace(',', '')
        print("Your ISBN-10 has been converted to a valid ISBN-10:\n" + strISBN)

    elif (sum % 10 != 0):

        isbn_thirteen_trial(newISBNList)


#This function will loop through the final list item until the ISBN is valid
lastItem = 0
def isbn_thirteen_trial(newISBNList):

    lastItem = 0
    x = 0
    sum = 0

    for lastItem in range(0, 11):

        newISBNList[12] = lastItem

        for x in range(0, len(newISBNList)):
                
            if ((x == 0) or (x % 2 == 0)):

                sum += newISBNList[x]

            elif (x % 2 != 0):

                sum += newISBNList[x] * 3

        if (sum % 10 == 0):

            if (newISBNList[12] == 10):

                newISBNList[12] = "X"

            #The following lines of code format the output for the user
            strISBN = ' '.join(str(newISBNList))
            strISBN = strISBN.replace(' ', '')
            strISBN = strISBN.replace('[', '')
            strISBN = strISBN.replace(']', '')
            strISBN = strISBN.replace(',', '')
            strISBN = strISBN.replace('\'', '')
            print("Your ISBN-10 has been converted to a valid ISBN-10:\n" + strISBN)
            break

        elif (sum % 10 != 0):

            lastItem += 1
    

#My code will call the user_input_capture function first to get the correct user input
user_input_capture()