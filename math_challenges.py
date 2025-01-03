import random

def factorial(n):
    final = 1
    for i in range(2,n+1):
        final = final*i
    return final


def math_challenge_factorial():
    n = random.randint(1,10)
    print("Math Challenge ! Calculate the factorial of", n)
    userInput = int(input("Your answer: "))
    if userInput == factorial(n):
        print("Well Done ! You won a key")
        return True
    else:
        print("You failed...")
        return False


def math_roulette_challenge():
    l = [random.randint(1,20) for i in range(5)]
    print("Numbers of the roulette :", l)
    operations = ["addition", "subtraction", "multiplication"]
    opChoice = random.choice(operations)
    match opChoice:
        case "addition":
            r = sum(l)
        case "subtraction":
            r = l[0]
            for i in range(1,5):
                r -= l[i]
        case "multiplication":
            r = l[0] * l[1] * l[2] * l[3] * l[4]
    print("Calculate the result by combining these numbers with", opChoice)
    userInput = int(input("Your answer: "))
    if userInput == r:
        print("Well Done ! You won a key")
        return True
    else:
        print("You failed...")
        return False


def solve_linear_equation() :
    a,b = random.randint(1,10), random.randint(1,10)
    x = -b/a
    return (a,b,x)

def math_challenge_equation() :
    a,b,x = solve_linear_equation()
    print("Math Challenge: Solve the equation",a,"x +",b,"= 0")
    y = float(eval(input("What is the value of x:")))
    if x == y :
        print("Correct! You win a key.")
        return True
    print(x,y)
    return False


def is_prime(n):
    if n < 2  :
        n= int(input('Enter an integer superior at 1 :'))
    cpt = 0
    for i in range (1,n+1):
        if n%i == 0 :
            cpt += 1
    if cpt != 2 :
        return False
    else :
        return True
def nearest_prime(n):
    cpt = 0
    while is_prime(n) == False :
        n -= 1
    return n

def math_challenge_prime() :
    n = random.randint(10, 20)
    user_answer = int(input(f"Math Challenge: Find the nearest prime to {n}:"))
    print("Your answer is :", user_answer)
    good_answer = nearest_prime(n)
    if user_answer == good_answer :
        print("Correct! You win a key.")
        return True
    else :
        print('You lost !')
        return False


def math_challenge() :
    challenges = [math_challenge_factorial,math_roulette_challenge,math_challenge_equation, math_challenge_prime]
    select_challenge = random.choice(challenges)
    return select_challenge()




