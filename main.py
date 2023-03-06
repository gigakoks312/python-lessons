def GetWordsFromUser():
    words = []
    while True:
        word = input("enter word and press <enter>")
        if word != "":
            words.append(word)
        else:
            return words
words = GetWordsFromUser()
def DisplayWords():
    for word in words:
        print(word)
rowMax = int(input("Enter number of rows: "))
colMax = int(input("Enter number of columns: "))
def GenerateGrid():
    grid = [['-' for x in range(colMax)] for y in range(rowMax)]
    return grid
grid = GenerateGrid()
def DisplayGrid():
    for row in range(rowMax):
        for col in range(colMax):
            print (grid[row][col] + ' ', end="")
        print ()
DisplayGrid()