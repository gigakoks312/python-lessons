import random
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

def PlaceWords(): #defines direction of how is word placed
    for word in words:
        if len(word) > rowMax or len(word) > colMax: continue
        direction = random.randint(0,3)
        if direction == 0:
            print("placing", word, "from left to right")
            min = 0
            max = colMax - len(word)
        elif direction == 1:
            print("placing", word, "from right to left")
            min = len(word) - 1
            max = colMax - 1
        elif direction == 2:
            print ("placing", word, "from top to bottom")
            min = 0
            max = rowMax - len(word)
        elif direction == 3:
            print("placing", word, "from bottom to top")
            min = len(word)-1
            max = rowMax - 1
    print("Word length is ", len(word), " so:")
    print("min: ", min, " max:", max)
    square = random.randint(min,max)
    print("Square chosen is ", square)
    if direction < 2:
        row = random.randint(0,rowMax-1)
        col = square
        print (" in row ", row)
    else:
        col = random.randint(0,colMax-1)
        row = square
        print (" in column ", col)
    foundValidLocation = CheckWordWillFit(word, row, col,direction)
    if foundValidLocation:
        PlaceWord(word, row, col, direction)

def PlaceWord(word, row, col, direction): #placing words in random order
    for charOfWord in range(len(word)):
        grid[row][col] = word[charOfWord]
        if direction == 0: col+=1
        if direction == 1: col-=1
        if direction == 2: row+=1
        if direction == 3: row-=1

def CheckWordWillFit(word, row,col, direction): #checking if words will fit in
    for charOfWord in range(len(word)):
        if grid[row][col] == '-' or grid[row][col] == word[charOfWord]:
            if direction == 0: col+=1
            if direction == 1: col-=1
            if direction == 2: row+=1
            if direction == 3: row-=1
        else:
            print ('Word will not fit')
            return False
    return True

words = GetWordsFromUser()
DisplayWords()
rowMax = int(input("Enter number of rows: "))
colMax = int(input("Enter number of columns: "))
grid = GenerateGrid()
DisplayGrid()
PlaceWords()