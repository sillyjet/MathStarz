import math
import random
OP_ERROR_MSG = "Please select at least one operator."
CORRECT_MSG = "Correct!"
INCORRECT_MSG = "Incorrect! Press R to reveal the correct answer or enter another guess: "
REVEAL_MSG = "The correct answer is: "
formats = ["Beginner", "Intermediate", "Expert"]
operators = []
answer = ()
guess = ()
def loadOperators():
    global operators
    if addition == True:
        operators.append("a")
    if subtraction == True:
        operators.append("s")
    if multiplication == True:
        operators.append("m")
    if division == True:
        operators.append("d")
    if len(operators) == 0:
        print(OP_ERROR_MSG)
def selectOperator():
    operatorNumber = random.randint(0, len(operators) - 1)
    operator = operators[operatorNumber]
    return operator
def generateFactors(n):
    factors = []
    for E in range(1, math.ceil(math.sqrt(n))):
        if n % E == 0:
            factors.append(E)
            factors.append(n // E)
    return factors
def selectTwoOperands(a, o):
    if o == "a":
        operand1 = random.randint(0, a)
        operand2 = a - operand1
    if o == "s":
        operand1 = random.randint(a, max)
        operand2 = operand1 - a
    if o == "m":
        factors = generateFactors(a)
        operand1 = factors[random.randint(0, len(factors) - 1)]
        operand2 = a / operand1
    if o == "d":
        operand2 = random.randint(1, max)
        operand1 = a * operand2
    return operand1, operand2
def goMath():
    global answer
    answer = random.randint(0, max)
    operand1, operand2 = selectTwoOperands(answer, operator1)
    prompt = str(operand1) + " " + actualOperator1 + " " + str(operand2) + " = "
    return prompt
def userPrompt(prompt):
    global guess
    guess = int(input(prompt))
    gaveUp = False
    while guessCheck(guess) == False:
        again = input(INCORRECT_MSG)
        if again == "r" or again == "R":
            print(REVEAL_MSG + str(answer))
            gaveUp = True
            break
        else:
            guess = again
    if gaveUp == False:
        print(CORRECT_MSG)
def guessCheck(E):
    if guess == answer:
        return True
    else:
        return False
def selectThreeOperands():
    pass
formatNumber = random.randint(0, 2)
# format = formats[formatNumber]
format = "Intermediate"
addition = True
subtraction = True
multiplication = True
division = True
if format == "Beginner":
    loadOperators()
    operator1 = selectOperator()
    if operator1 == "a":
        max = 198
        actualOperator1 = "+"
    if operator1 == "s":
        max = 99
        actualOperator1 = "-"
    if operator1 == "m":
        max = 81
        actualOperator1 = "x"
    if operator1 == "d":
        max = 9
        actualOperator1 = "/"
    userPrompt(goMath())
if format == "Intermediate":
    # subFormat = random.randint(0, 1)
    subFormat = 0
    loadOperators()
    if subFormat == 0:
        operator1 = selectOperator()
        if operator1 == "a":
            max = 1998
            actualOperator1 = "+"
        if operator1 == "s":
            max = 999
            actualOperator1 = "-"
        if operator1 == "m":
            max = 9801
            actualOperator1 = "x"
        if operator1 == "d":
            max = 99
            actualOperator1 = "/"
        userPrompt(goMath())
    if subFormat == 1:
        operator1 = selectOperator()
        operator2 = selectOperator()
        #if operator2 == "m" or operator2 == "d":