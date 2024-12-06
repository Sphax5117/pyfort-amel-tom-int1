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
                r = 0

    print("Calculate the result by combining these numbers with", opChoice)

def solve_linear_equation() :
    a,b = random.randint(1,10), random.randint(1,10)
    x = -b/a
    return (a,b,x)

def math_challenge_equation() :
    a,b,x = solve_linear_equation()
    print(a,"x +",b,"= 0")
    y = float(eval(input("solve the equation")))
    if x == y :
        return True
    return False


