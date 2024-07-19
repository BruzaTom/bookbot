def main():
    filePath = "books/frankenstein.txt"
    text = getText(filePath)
    wordCount = wc(text)
    chars = findChars(text)
    charDict = makeCharDict(chars, text)

    print(f"there are {wordCount} words in the frankenstein book")
    print("Here is a dictionary with the counts of each charactor used")
    print(charDict)
    #print(charCount) #debug

    return

def makeCharDict(chars, strText):
    lowerStr = strText.lower()
    strLetters = list(lowerStr)
    charDict = {}
    for i in range(0, len(chars)): # go through each letter found
        count = 0
        for j in range(0, len(strLetters)):# increment the count if you find the letter
            if chars[i] == strLetters[j]:
                count += 1
        charDict.update({chars[i]: count}) #update dict with current count and letter inquery
    #print(charDict) #debug
    return charDict

def wc(fileStr):
    words = fileStr.split() #fileStr.split() turns your long string into list of words
    return len(words)

def getText(path):
    with open(path) as f:
        file_contents = f.read() #f.read() turns book text into long string
    return file_contents

def findChars(textStr):
    lowerStr = textStr.lower()
    chars = list(lowerStr)
    charFound = []
    foundChar = None
    for i in range(0, len(chars)): # go though chars
        foundChar = False
        for j in range(0, len(charFound)):# compare chars to found chars
            if chars[i] == charFound[j]:
                foundChar = True # if current char already exists aknowlege
        if foundChar == False: #if char was not found 
            charFound.append(chars[i])
            #print(chars[i]) #debug
    return charFound


main()
