# Name: <Aidyn Somerville>
# I certify that this lab is my own work, but I discussed it with
#   <Oscar> in CSL.

from random import *
from graphics import *


# reads words from file + separates them
def readWords():
    infileName = "wordlist.txt"
    infile = open(infileName, "r")
    lines = infile.readlines()
    return lines

# pick random word from document - calls readWords function
def randomWord():
    words = readWords()
    value = randint(0, 23)
    pick = words[value]
    return pick

# called in the guess function, activates when word it wrong first time
def printMan(win, guessLeft): 
    w = win.getWidth()#500
    h = win.getHeight()#600
    if guessLeft == 6:
        hang1 = Line(Point(w/2-100, h-500), Point(w/2-100, h-200))
        hang1.setWidth(10)
        hang1.setFill(color_rgb(255,0,127))
        hang2 = Line(Point(w/2-100, h-500), Point(w/2+100, h-500))
        hang2.setWidth(10)
        hang2.setFill(color_rgb(255,0,127))
        hang3 = Line(Point(w/2+100, h-500), Point(w/2+100, h-480))
        hang3.setWidth(10)
        hang3.setFill(color_rgb(255,0,127))
        hang1.draw(win)
        hang2.draw(win)
        hang3.draw(win)
    elif guessLeft == 5:#consider radius with height
        head = Circle(Point(w/2+100, h-440), 40)
        head.setFill(color_rgb(0,204,0))
        head.setOutline(color_rgb(0,204,0))
        head.draw(win)
        #hat
        brim = Oval(Point(w/2, h-475), Point(w/2+200, h-465))
        brim.setFill("black")
        brim.draw(win)
        hat = Polygon(Point(w/2+60, h-475), Point(w/2+140, h-475), Point(w/2+100,h-540))
        hat.setFill("black")
        hat.draw(win)
        # eyes
        leftEye = Circle(Point(w/2+82, h-440), 13)
        leftEye.setFill("white")
        leftEye.setOutline("white")
        leftEye.draw(win)
        rightEye = leftEye.clone()
        rightEye.move(34,0)
        rightEye.draw(win)
        # pupils
        leftPupil = Circle(Point(w/2+82, h-440), 6)
        leftPupil.setFill("black")
        leftPupil.draw(win)
        rightPupil = leftPupil.clone()
        rightPupil.move(34,0)
        rightPupil.draw(win)
    elif guessLeft == 4:
        body = Line(Point(w/2+100, h-400),Point(w/2+100, h-300))
        body.setFill(color_rgb(0,204,0))
        body.setWidth(10)
        body.draw(win)
    elif guessLeft == 3:
        arm1 = Line(Point(w/2+100, h-380), Point(w/2+50, h-320))
        arm1.setWidth(5)
        arm1.setFill(color_rgb(0,204,0))
        arm1.draw(win)
    elif guessLeft == 2:
        arm2 = Line(Point(w/2+100, h-380), Point(w/2+150, h-320))
        arm2.setWidth(5)
        arm2.setFill(color_rgb(0,204,0))
        arm2.draw(win)
    elif guessLeft == 1:
        leg1 = Line(Point(w/2+100, h-300), Point(w/2+50, h-200))
        leg1.setWidth(5)
        leg1.setFill(color_rgb(0,204,0))
        leg1.draw(win)
    elif guessLeft == 0:
        leg2 = Line(Point(w/2+100, h-300), Point(w/2+150, h-200))
        leg2.setWidth(5)
        leg2.setFill(color_rgb(0,204,0))
        leg2.draw(win)

    
                    

        
# parameters - window + randomized word
# main function - recieves letter from user + controlls how program reacts to it
#  calls other functions to draw witch, fill blanks with correct letters +
#  sets list of guessed letters 
def guess(win, word):
    w = win.getWidth()
    h = win.getHeight()
    
    #create list for incorrect guessed letters - dont take off points
    guessedLetters = []
    guessedPt = Point(w/2, h-170)
    guessedTxt = Text(guessedPt, guessedLetters)
    guessedTxt.setTextColor(color_rgb(255,0,127))
    guessedTxt.setSize(16)
    guessedTxt.draw(win)
    
    #initilize num of guesses at 7 and count down
    guessLeft = 7
    txt = Text(Point(w/2,h-580), f"guesses left: {guessLeft}")
    txt.setTextColor(color_rgb(255,0,127))
    txt.setSize(16)
    txt.draw(win)
    #lines 
    blankLst = Text(Point(w/2,h-100), blanks(word, guessedLetters))
    blankLst.draw(win)
    #tell user to retry letter
    incorrectPt = Point(w/2, h-550)
    incorrectTxt = Text(incorrectPt, "")
    incorrectTxt.setTextColor(color_rgb(255,0,127))
    incorrectTxt.setSize(16)
    while guessLeft > 0:
        txtPt = Point(w/2, h-30)
        instruct = Text(txtPt, "click to submit answer.")
        instruct.setTextColor(color_rgb(255,0,127))
        instruct.setSize(16)
        instruct.draw(win)
        #entry box for user
        boxPt = Point(w/2, h-70)
        box = Entry(boxPt, 10)
##        box.setText("hmmm..")
        box.draw(win)
        pause = win.getMouse()
        ans = str(box.getText())
        answer = ans.lower()
        incorrectTxt.undraw()
        #compare letter to letters in word
        check = checkMatch(win, word, answer)
        #tell user to try new letter
        repeatLetter = getGuess(win, guessedLetters, answer, check)
        if check == True: #check if letter matches word 
            blankLst.setText(blanks(word, guessedLetters))# pass random + lst
            # replace - remove spaces in list to compare to word
            # strip - does same to word. strips of whitespace
            # smoothly compare these 
            if blanks(word, guessedLetters).replace(" ", "") == word.strip():
                happy = Text(Point(w/2, h-550), "you rock!")
                happy.setTextColor("yellow")
                happy.setSize(22)
                happy.draw(win)
                button(win)
        else:
            if repeatLetter == True: #check if letter is repeated
                incorrectTxt.setText("You've tried that... do better")
                incorrectTxt.draw(win)
            else:
                guessLeft -= 1
                printMan(win, guessLeft)
                txt.setText(f"guesses left: {guessLeft}")
        guessedTxt.setText(guessedLetters)
    else:
        button(win)



# word bank for already guessed words
def getGuess(win, lst, answer, check):
    w = win.getWidth()
    h = win.getHeight()
    if answer in lst: #show to user
        return True
    else: #warning
        lst.append(answer)
        return False

# check to see if the entered letter matches any in randomized word
def checkMatch(win, word, answer):
    w = win.getWidth()
    h = win.getHeight()
    for letter in word:
        if answer == letter :
            return True
    return False

##    answerPt = Point(w/2, h-260)
##    letterGuess = Text(answerPt, " ")

# fill each space with correct letter when guessed
def blanks(word, guessedLetters):
    fill = ['_']*(len(word)-1)
    for i in range(len(word)):
        for j in range(len(guessedLetters)):
            if guessedLetters[j] == word[i]:
                fill[i] = guessedLetters[j]#word[i]
    fill = " ".join(fill)
    return fill


# tells playGame to exit or create a new window
def button(win):
    w = win.getWidth()
    h = win.getHeight()
    
    red = Rectangle(Point(w-450, h-50), Point(w-400, h-100))
    red.setFill(color_rgb(255,102,102))
    red.draw(win)
    
    green = Rectangle(Point(w-450, h-150), Point(w-400, h-200))
    green.setFill(color_rgb(255,255,102))
    green.draw(win)

    leave = Text(Point(w-425, h-75), "exit")
    leave.draw(win)

    play = Text(Point(w-425, h-175), "play")
    play.draw(win)

    while True:
        user = win.getMouse()
        x = user.getX()
        y = user.getY()
        if x>(w-450) and x<(w-400):
            if y>(h-100) and y<(h-50):
                exit()
        if x>(w-450) and x<(w-400):
            if y>(h-200) and y<(h-150):
                return True
                win.close()
            


# runs game - while loop that tells game to play or not
def playGame():
    while True:
        width = 500
        height = 600
        win = GraphWin("hangman", width, height)
        win.setBackground(color_rgb(153,0,76))
        pick = randomWord()
        print(pick)
        guessedLetters = guess(win, pick)
        playAgain = button(win)
        print(playAgain)
        if not playAgain:
            break
playGame()


    
