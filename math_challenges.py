import random

'''
Fort Boyard Project 
Authors : Amel Boulhamane and Tom Hausmann
Role of this file : 
This file aims at providing the math challenges for the Fort Boyard Game.
It encompass the four challenges (Factorial, Linear Equation, Prime Number and Math Roulette), and chose between them randomly.
All functions have been commented.
'''
# Factorial challenge (weak)
def factorial(n):
    final = 1 # Start with 1 because the factorial of 0 or 1 is 1.
    for i in range(2,n+1):
        final = final*i
    return final

def math_challenge_factorial():
    n = random.randint(1,10) # Generate a random number between 1 and 10.
    print("Math Challenge ! Calculate the factorial of", n)
    while True:
        try:
            userInput = int(input("Enter you choice : "))
            break
        except ValueError:
            print("Please enter a number (not text)")
    if userInput == factorial(n):
        print("Correct! You won a key.")
        return True
    else:
        print("You failed...")
        return False

# Linear equation test (weak)
def solve_linear_equation() :
    a,b = random.randint(1,10), random.randint(1,10) # Randomly generate the coefficients a and b of the linear equation ax + b = 0
    x = -b/a # Calculate the solution x of the linear equation.
    return a,b,x

def math_challenge_equation() :
    a,b,x = solve_linear_equation()
    print(x)# Generate a random linear equation using the solve_linear_equation function
    print("Math Challenge: Solve the equation",a,"x +",b,"= 0")
    while True:
        try:
            userInput = input("What is the value of x (be careful, expressions such as -3+2 will be evaluated as -1): ")
            if all(i in "0123456789,./-+" for i in userInput): #we check if all character in userInput are in "012 ... -+"
                safeUserInput = float(eval(userInput)) #if it's the case we evaluate expressions such as 3/2 and store it
                break  # after, we break the loop
            else:
                print("Please enter a valid number or mathematical expression.")
        except (ValueError, ZeroDivisionError): #we also handle division by zero and type errors
            print("Invalid input. Please enter a number or a valid mathematical expression without division by zero.")
    if x == safeUserInput :
        print("Correct! You won a key.")
        return True
    else :
        print("You failed...")
        return False

# Prime Numbers challenge (average)
def is_prime(n):
    if n < 2  :
        return False # Numbers less than 2 are not prime by definition
    cpt = 0 # Initialize a counter to count the number of divisors
    for i in range (1,n+1):
        if n%i == 0 : # Check if n is divisible by i
            cpt += 1
    if cpt != 2 : # A prime number has exactly two divisors: 1 and itself, so if the number of divisors isn't 2, it isn't prime.
        return False
    else :
        return True

def nearest_prime(n): # Check if n is prime, and if not, find the prime number greater than or equal to the original n
    while is_prime(n) == False :
        n += 1
    return n

def math_challenge_prime() :
    n = random.randint(10, 20)
    while True:
        try:
            userInput = int(input(f"Math Challenge: Find the nearest prime to {n}:"))
            break
        except ValueError:
            print("Please enter a number (not text)")
    good_answer = nearest_prime(n)
    if userInput == good_answer :
        print("Correct! You won a key.")
        return True
    else :
        print("You failed...")
        return False

# Math Roulette challenge (average)
def math_roulette_challenge():
    l = [random.randint(1,20) for i in range(5)] # Create a list of 5 random integers between 1 and 20.
    print("Numbers of the roulette :", l)
    operations = ["addition", "subtraction", "multiplication"]
    opChoice = random.choice(operations)
    match opChoice: # The match instruction allows you to perform different actions depending on the value of opChoice.
        case "addition":
            r = sum(l)
        case "subtraction":
            r = l[0]
            for i in range(1,5):
                r -= l[i]
        case "multiplication":
            r = l[0] * l[1] * l[2] * l[3] * l[4]
    print("Calculate the result by combining these numbers with", opChoice)
    while True:
        try:
            userInput = int(input("Enter you choice : "))
            break
        except ValueError:
            print("Please enter a number (not text)")
    if userInput == r:
        print("Well Done ! You won a key")
        return True
    else:
        print("You failed...")
        return False

# math_challenge() function for random challenge selection
def math_challenge() :
    challenges =[math_challenge_factorial,math_roulette_challenge,math_challenge_equation] # List of math challenge functions
    challenge = random.choice(challenges) # Randomly select one of the challenge functions from the list.
    return challenge() # returns the "call" of the randomly selected functions
