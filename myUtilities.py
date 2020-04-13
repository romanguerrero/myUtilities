# myUtilities.py
# Roman Guerrero
# 4/13/20
# Library of utility functions I've developed



def getInt(low, high):
    '''
    Prompts user to enter an integer, then validates integer
    :arg list: range of allowed integers [inclusive]
    :returns: validated integer within given range
    '''

    validationFlag = False

    while (validationFlag == False):
    
        userInput = input('Enter a integer between [' + str(low) + ', ' + str(high) + ']: ')    

        # Integer check 
        try:
            userInput = int(userInput)

            # Range check
            if (userInput < low or userInput > high):
                print('That is not within the allowed range, please try again.')
        
            else:
                validationFlag = True


        # Repeat prompt if necessary
        except ValueError: 
            print('That is not an integer, please try again.')


if __name__ == '__main__':
    getInt(0, 10)



