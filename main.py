def main():
    filePath = "books/frankenstein.txt"
    text = getText(filePath)
    wordCount = wc(text)
    charCount = cc(text)
    print(f"there are {wordCount} words in the frankenstein book")
    #print(f"there are {wordCount} words in the frankenstein book")
    print(charCount)

    return

def wc(fileStr):
    words = fileStr.split() #fileStr.split() turns your long string into list of words
    return len(words)

def getText(path):
    with open(path) as f:
        file_contents = f.read() #f.read() turns book text into long string
    return file_contents

def cc(textStr):
    lowerStr = textStr.lower()
    chars = list(lowerStr)
    charFound = []
    foundChar = None
    for i in range(0, len(chars)): # go though chars
        foundChar = False
        #charCount = 0
        for j in range(0, len(charFound)):# compare chars to found chars
            if chars[i] == charFound[j]:
                foundChar = True # if current char already exists aknowlege
                #charCount += 1

        if foundChar == False: #if char was not found 
            charFound.append(chars[i])
            print(chars[i])
            #print(charCount)


    return len(charFound)




main()
