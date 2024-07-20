def main():
    filePath = "books/frankenstein.txt"
    text = getText(filePath)
    lowText = text.lower()
    wordCount = wc(text)
    chars = findChars(lowText)
    charDict = makeCharDict(chars, lowText)
    dictLst = listDict(charDict)
    dictLst.sort(reverse=True, key=sort_on)#built in sort function sorted in reversed based on sort_on function return
    alphaDict = alphaOnly(dictLst)

    print(f"there are {wordCount} words in the frankenstein book")
    print("Here is a labled list of dictionarys with the values sorted highest to lowest and only alphabet")
    print(alphaDict)

    return

def alphaOnly(oldLst):
    newLst = []
    for diction in oldLst:#acces my dictionaries
        if diction["name"].isalpha() == True:#check alpha
            newLst.append(diction)
    return newLst

def sort_on(dict):
    return dict["num"]# return value of "num" key granted it exists

def listDict(oldDict):
    dictLst = [{"name": key, "num": value} for key, value in oldDict.items()] # format list with data from old dict
    return dictLst

def makeCharDict(chars, strText):
    strLetters = list(strText)
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
    chars = list(textStr)
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
