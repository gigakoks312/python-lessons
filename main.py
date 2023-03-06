def GetWordsFromUser():
    words = []
    while True:
        word = input("enter word and press <enter>")
        if word != "":
            words.append(word)
        else:
            return words

def DisplayWords():
    #for word in words:
    print(words)

def GenerateGrid():
    grid = [['-' for x in range(colMax)] for y in range(rowMax)]
    return grid

def DisplayGrid():
    for row in range(rowMax):
        for col in range(colMax):
            print (grid[row][col] + ' ', end="")
        print ()

def PlaceWords(): #
    pass


words = GetWordsFromUser()
DisplayWords()
rowMax = int(input("Enter number of rows: "))
colMax = int(input("Enter number of columns: "))
grid = GenerateGrid()
DisplayGrid()