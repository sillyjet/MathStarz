# Author: Jessica Thomson
# Date written: 03/07/24
# Assignment:   Final Project
# Short Desc:   This program provides a way for people to practice their math skills. It allows the user to choose between three different
# difficulty levels and select which operators they want to use.
import math
import random
from tkinter import *

# These are the constants that are used to display specific messages to the user.
OP_ERROR_MSG = "Please select at least one operator."
GEN_ERROR_MSG = "Invalid guess."
CORRECT_MSG = "Correct!"
INCORRECT_MSG = "Incorrect! Press Give Up to reveal the correct answer or enter another guess: "
REVEAL_MSG = "The correct answer is: "

# These are global variables.
formats = ["Beginner", "Intermediate", "Expert"]
format = str
operators = []
operatorNumber = int
answer = int
guess = int
max = int
operator1 = str
operator2 = str
operand1 = int
operand2 = int
operand3 = int

# Here is where the main window is initiated, along with a total of 8 frames that are used to display various buttons and text.
root = Tk()
root.title("MathStarz")
root.minsize(450, 450)
root.maxsize(550, 550)
frame1 = Frame(root)
frame1.pack(side = TOP)
frame2 = Frame(root)
frame2.pack(side = TOP)
frame3 = Frame(root)
frame3.pack(side = TOP)
frame4 = Frame(root)
frame4.pack(side = TOP)
frame5 = Frame(root)
frame5.pack(side = TOP)
frame6 = Frame(root)
frame6.pack(side = TOP)
frame7 = Frame(root)
frame7.pack(side = TOP)
frame8 = Frame(root)
frame8.pack(side = TOP)

# These are all the functions that are used throughout the program. Expand each one to view more information.
def loadOperators():
    # This function is used to load all the selected operators onto a list.
    global operators
    if addition.get() == 1:
        operators.append("+")
    if subtraction.get() == 1:
        operators.append("-")
    if multiplication.get() == 1:
        operators.append("x")
    if division.get() == 1:
        operators.append("/")

def selectOperator():
    # This funciton chooses an operator from the list of selected operators.
    if len(operators) > 1:
        num = random.randint(0, len(operators) - 1)
    elif len(operators) == 1:
        num = 0
    return num

def generateFactors(n):
    # This function determines the factors of a given number. This is used to generate multiplication questions.
    factors = []
    s = math.ceil(math.sqrt(n))
    if s <= 2:
        s = 3
    for E in range(1, s):
        if n % E == 0:
            factors.append(E)
            factors.append(n / E)
    return factors

def selectTwoOperands(a, o):
    # This is where the operands are selected based on the operator and whatever the randomly generated answer is.
    if o == "+":
        one = int(random.randint(0, a))
        two = int(a - one)
    if o == "-":
        one = int(random.randint(a, max))
        two = int(one - a)
    if o == "x":
        factors = generateFactors(a)
        one = int(factors[random.randint(0, len(factors) - 1)])
        two = int(a / one)
    if o == "/":
        two = int(random.randint(1, max))
        one = int(a * two)
    return one, two

def goMath():
    # goMath generates a prompt.
    global answer, operand1, operand2, prompt, operatorNumber
    answer = random.randint(0, max)
    operand1, operand2 = selectTwoOperands(answer, operator1)
    prompt.set(str(operand1) + " " + operator1 + " " + str(operand2) + " = ")

def goMathExpert1():
    # This is the Expert version of goMath where there are three operands and two operators. This specific funciton is called when
    # the first operator takes precedence over the second in the order of operations.
    global answer, operand1, operand2, prompt, operatorNumber, operand3
    answer = random.randint(0, max)
    subAnswer, operand3 = selectTwoOperands(answer, operator2)
    operand1, operand2 = selectTwoOperands(subAnswer, operator1)
    prompt.set(str(operand1) + " " + operator1 + " " + str(operand2) + " " + operator2 + str(operand3) + " = ")

def goMathExpert2():
    # This is another Expert version of goMath, only this one is for when the second operator comes first.
    global answer, operand1, operand2, prompt, operatorNumber, operand3
    answer = random.randint(0, max)
    operand1, subAnswer = selectTwoOperands(answer, operator1)
    operand2, operand3 = selectTwoOperands(operand1, subAnswer)
    prompt.set(str(operand1) + " " + operator1 + " " + str(operand2) + " " + operator2 + str(operand3) + " = ")

def userPrompt():
    # This function's purpose is to change the dialogue label to the question for the user to answer, as well as changing the "Start"
    # button so that it says "Submit" and has a different command.
    global dialogue, next, dialogue2
    dialogue.config(text = prompt.get())
    next.config(text = "Submit", command = Validation)

def Validation():
    # This function validates whether the user's guess matches the answer.
    global dialogue2, next, guess, gaveUp, picture
    gaveUp = False
    if loadGuess() == True:
        if guess != answer:
            dialogue2.config(text = INCORRECT_MSG)
            picture.config(image = badjob)
        else:
            if gaveUp == False:
                dialogue2.config(text = CORRECT_MSG)
                picture.config(image = goodjob)
                # The "Start" button is reverted to its original state after the correct answer is guessed.
                next.config(text = "New Game", command = startGame)

def loadGuess():
    # The purpose of this function is to load the user's guess into the variable "guess" and also to check that it's
    # an integer and not something else, or empty.
    global guess, dialogue2, valid
    valid = False
    try:
        guess = int(userResponse.get())
    except:
        dialogue2.config(text = GEN_ERROR_MSG)
    else:
        guess = int(userResponse.get())
        valid = True
    return valid

def Priority(a, b):
    # Here the order of operations determines which operator gets priority.
    if a == "+" or a == "-":
        aPriority = 1
    else:
        aPriority = 2
    if b == "+" or b =="-":
        bPriority = 1
    else:
        bPriority = 2
    if aPriority > bPriority:
        priority = "first"
    elif bPriority > aPriority:
        priority = "second"
    else:
        priority = "equal"
    return priority

def smallMax(e):
    # This function is used for determining the maximum value for the answer.
    if e == "+":
        max = 198
    if e == "-":
        max = 99
    if e == "x":
        max = 81
    if e == "/":
        max = 9
    return max

def largeMax(e):
    # This function is used for determining the maximum value of the answer in Intermediate mode or Expert mode.
    if e == "+":
        max = 1998
    if e == "-":
        max = 999
    if e == "x":
        max = 9801
    if e == "/":
        max = 99
    return max

def resetGame():
    # This function resets the labels and picture, clears the entry box, and reverts the "Start" button to its original state. It does
    # not reset the difficulty level or the selected operators.
    global dialogue, dialogue2, next, userResponse
    dialogue.config(text = " ")
    dialogue2.config(text = " ")
    userResponse.delete(0, END)
    next.config(text = "Start", command = startGame)
    picture.config(image = "")

def startGame():
    # This is the function that's called when the user presses the "Start" button. It calls other functions like resetGame and
    # loadOperators. This allows the user to change the selected operators in between questions.
    global format, dialogue, dialogue2, next
    resetGame()
    format = formats[formatNumber.get()]
    loadOperators()
    if len(operators) == 0:
        dialogue.config(text = OP_ERROR_MSG)
    if formatNumber.get() == 0:
        beginnerGame()
    elif formatNumber.get() == 1:
        intermediateGame()
    elif formatNumber.get() == 2:
        expertGame()

def beginnerGame():
    # This function is called to initiate the game in Beginner mode.
    global max, operator1, dialogue, next, dialogue2
    operatorNumber = selectOperator()
    operator1 = operators[operatorNumber]
    max = smallMax(operator1)
    goMath()
    userPrompt()

def intermediateGame():
    # This function initiates the game in Intermediate mode.
    global max, operator1, dialogue, next, dialogue2
    operator1 = operators[selectOperator()]
    max = largeMax(operator1)
    goMath()
    userPrompt()

def expertGame():
    # This function initiates the game in Expert mode.
    global max, operator1, dialogue, next, dialogue2, operator2
    operator1 = operators[selectOperator()]
    operator2 = operators[selectOperator()]
    if Priority(operator1, operator2) == "first" or Priority(operator1, operator2) == "equal":
        max = int(largeMax(operator2))
        goMathExpert1()
        userPrompt()
    if Priority(operator1, operator2) == "second":
        max = int(largeMax(operator1))
        goMathExpert2()
        userPrompt()

# The following four functions are used to set the values of the operators so that the loadOperators function knows which operators to
# append to the list. This may or may not be necessary.
def Add():
    addition.set(1)

def Sub():
    subtraction.set(1)

def Mult():
    multiplication.set(1)

def Div():
    division.set(1)

def clear():
    # The clear function clears all the operators from the list and sets their values to zero so they will not be added again unless
    # the user selects them again. This function is called when the user presses the "Clear" button.
    addition.set(0)
    subtraction.set(0)
    multiplication.set(0)
    division.set(0)
    operators.clear()

def revealAnswer():
    # This function is called when the user presses the "Give Up" button. It displays the answer and resets the "Start" button.
    global dialogue2, gaveUp
    dialogue2.config(text = REVEAL_MSG + str(answer))
    gaveUp = True
    next.config(text = "New Game", command = startGame)

def quitApp():
    # This function exits the program. Very straightforward.
    root.quit()

def selectDifficulty():
    # This function defines a new window that displays over the main window. This is how the user will select their difficulty level. The
    # button will only change if the user presses the "Submit" button, not the "X" in the corner of the window.
    difficulty = Toplevel(root)
    difficulty.title("Difficulty")
    difficulty.minsize(300, 300)
    difficulty.maxsize(400, 400)
    def closeDiff():
        # The closeDiff function is used to close this specific window using .destroy() and also to change the text on the
        # button that launches the window.
        DifficultyLevel.config(text = formats[formatNumber.get()])
        difficulty.destroy()
    header = Label(difficulty, text = "Select a difficulty level:")
    header.pack()
    # These are radio buttons usesd to select the difficulty level. Only one can be selected at a time.
    checkB = Radiobutton(difficulty, text = formats[0], indicatoron = 0, variable = formatNumber, value = 0)
    checkB.pack()
    checkI = Radiobutton(difficulty, text = formats[1], indicatoron = 0, variable = formatNumber, value = 1)
    checkI.pack()
    checkE = Radiobutton(difficulty, text = formats[2], indicatoron = 0, variable = formatNumber, value = 2)
    checkE.pack()
    submit = Button(difficulty, text = "Submit", command = closeDiff)
    submit.pack()

# These are specific tkinter variables
formatNumber = IntVar()
addition = IntVar()
subtraction = IntVar()
multiplication = IntVar()
division = IntVar()
prompt = StringVar()

# This is the button and label for changing the difficulty level.
DifficultyLabel = Label(frame1, text = "Select Difficulty:")
DifficultyLabel.pack(side = LEFT)
DifficultyLevel = Button(frame1, text = formats[formatNumber.get()], command = selectDifficulty)
DifficultyLevel.pack(side = LEFT)

# Here are the checkbuttons that the user can use to select operators.
AddBox = Checkbutton(frame2, text = "Addition", variable = addition, onvalue = 1, offvalue = 0, command = Add)
AddBox.pack(side = LEFT)
SubBox = Checkbutton(frame2, text = "Subtraction", variable = subtraction, onvalue = 1, offvalue = 0, command = Sub)
SubBox.pack(side = LEFT)
MultBox = Checkbutton(frame2, text = "Multiplication", variable = multiplication, onvalue = 1, offvalue = 0, command = Mult)
MultBox.pack(side = LEFT)
DivBox = Checkbutton(frame2, text = "Division", variable = division, onvalue = 1, offvalue = 0, command = Div)
DivBox.pack(side = LEFT)
Clear = Button(frame2, text = "Clear", command = clear)
Clear.pack(side = LEFT)

# These labels are initiated with just a space for their text but are configured later to display prompts or error messages to the user.
dialogue = Label(frame3, text = " ")
dialogue.pack()
dialogue2 = Label(frame4, text = " ")
dialogue2.pack()

# This is the entry box that the user types their guess into.
userResponse = Entry(frame5)
userResponse.pack()

# The button called "next" is used as the "Start" button and the "New Game" button.
next = Button(frame6, text = "Start", command = startGame)
next.pack(side = LEFT)
# The "reveal" button is used to reveal the answer by calling the revealAnswer function listed above.
reveal = Button(frame6, text = "Give Up", command = revealAnswer)
reveal.pack(side = LEFT)
# The "exit" button quits the program. Very straightforward.
exit = Button(frame7, text = "Quit", command = quitApp)
exit.pack()

# These are the images that will display when the user submits a guess.
goodjob = PhotoImage(file = "Good job.gif")
badjob = PhotoImage(file = "Bad job.gif")
goodjob = goodjob.subsample(6, 6)
badjob = badjob.subsample(6, 6)
goodjob.config(alttext = "A poorly drawn picture of a smiling face and a thumbs up, with hand written words beneath it that say 'GOOD JOB!'")
badjob.config(alttext = "A poorly drawn picture of a crying face and a thumbs down, with hand written words beneath it that say 'AWW TRY AGAIN'")

picture = Label(frame8)
picture.pack(side = TOP)

root.mainloop()