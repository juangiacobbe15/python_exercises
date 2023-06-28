def main():
    userInput = input('Enter a word: ').lower()
    listWord = list(userInput)
    invertedWord = getInvertedWord(listWord)
    checkEquality(userInput, invertedWord)

def getInvertedWord(word):
    invertedWord = ''
    for char in reversed(word):
        invertedWord += char

    return invertedWord

def checkEquality(word1, word2):
    if(word1 == word2):
        print('The word entered is a palindrome!')
    else:
        print('The word entered is not a palindrome :(')


main()