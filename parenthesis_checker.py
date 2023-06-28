def main():
    userInput = input("enter a text: ")
    inputList = list(userInput)
    checker(inputList)


def checker(list):
    openParenthesis = 0
    closedParenthesis = 0

    openParenthesis = getCharAmount(list, '(')
    closedParenthesis = getCharAmount(list, ')')

    if(closedParenthesis == openParenthesis):
        print('It has a parenthesis and closes well :)')
    else:
        print('The text has a parenthesis and dont closes well :(')


def getCharAmount(list, char):
    amount = 0
    for c in list:
        if(c == char):
            amount += 1

    return amount        

main()