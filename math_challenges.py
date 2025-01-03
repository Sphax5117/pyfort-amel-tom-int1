import random

# Factorial challenge (weak)
def factorial(n):
    final = 1 # Start with 1 because the factorial of 0 or 1 is 1.
    for i in range(2,n+1):
        final = final*i
    return final

def math_challenge_factorial():
    n = random.randint(1,10) # Generate a random number between 1 and 10.
    print("Math Challenge ! Calculate the factorial of", n)
    user_input = int(input("Your answer: "))
    if user_input == factorial(n):
        print("Correct! You win a key.")
        return True
    else:
        print("You failed...")
        return False

# Linear equation test (weak)
def solve_linear_equation() :
    a,b = random.randint(1,10), random.randint(1,10) # Randomly generate the coefficients a and b of the linear equation ax + b = 0
    x = -b/a # Calculate the solution x of the linear equation.
    return (a,b,x)

def math_challenge_equation() :
    a,b,x = solve_linear_equation() # Generate a random linear equation using the solve_linear_equation function
    print("Math Challenge: Solve the equation",a,"x +",b,"= 0")
    y = float(eval(input("What is the value of x:")))
    if x == y :
        print("Correct! You win a key.")
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
    user_answer = int(input(f"Math Challenge: Find the nearest prime to {n}:"))
    print("Your answer is :", user_answer)
    good_answer = nearest_prime(n)
    if user_answer == good_answer :
        print("Correct! You win a key.")
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
            r = sum(l) # sûr de pouvoir utiliser la fonction somme ??
        case "subtraction":
            r = l[0]
            for i in range(1,5):
                r -= l[i]
        case "multiplication":
            r = l[0] * l[1] * l[2] * l[3] * l[4]
    print("Calculate the result by combining these numbers with", opChoice)
    user_input = int(input("Your answer: "))
    if user_input == r:
        print("Well Done ! You won a key")
        return True
    else:
        print("You failed...")
        return False

# math_challenge() function for random challenge selection
def math_challenge() :
    challenges =[math_challenge_factorial,math_roulette_challenge,math_challenge_equation] # List of math challenge functions
    challenge = random.choice(challenges) # Randomly select one of the challenge functions from the list.
    return challenge() # pas compris
