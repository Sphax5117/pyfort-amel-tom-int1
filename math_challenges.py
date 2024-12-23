import random
from fractions import Fraction

def factorial(n):
    final = 1
    for i in range(2, n + 1):
        final *= i
    return final

def math_challenge_factorial():
    """
    Returns (challenge_text, correct_answer).
    Example: "Calculate the factorial of 5" => correct_answer = 120
    """
    n = random.randint(1, 10)
    challenge_text = f"Calculate the factorial of {n}"
    correct_answer = factorial(n)  # an integer
    return challenge_text, correct_answer

def math_roulette_challenge():
    """
    Returns (challenge_text, correct_answer) for a random 'roulette' of 5 numbers
    with addition, subtraction, or multiplication.
    """
    nums = [random.randint(1, 20) for _ in range(5)]
    operations = ["addition", "subtraction", "multiplication"]
    op_choice = random.choice(operations)

    if op_choice == "addition":
        correct_answer = sum(nums)  # int
        challenge_str = " + ".join(str(x) for x in nums)
    elif op_choice == "subtraction":
        correct_answer = nums[0]
        for i in range(1, 5):
            correct_answer -= nums[i]
        challenge_str = " - ".join(str(x) for x in nums)
    else:  # multiplication
        correct_answer = 1
        for x in nums:
            correct_answer *= x
        challenge_str = " * ".join(str(x) for x in nums)

    challenge_text = f"{challenge_str} = ?"
    return challenge_text, correct_answer

def solve_linear_equation():
    """
    Returns (a, b, fraction_solution) for a*x + b = 0
    x = -b / a
    """
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    # We'll store the solution as a Fraction, e.g. -b/a
    fraction_solution = Fraction(-b, a)
    return a, b, fraction_solution

def math_challenge_equation():
    """
    Returns (challenge_text, correct_answer) for a linear eqn: a*x + b = 0
    Acceptable answers are floats or fractions like "-4/37".
    """
    a, b, fraction_solution = solve_linear_equation()
    challenge_text = f"Solve the equation {a}x + {b} = 0"
    correct_answer = fraction_solution  # a Fraction
    return challenge_text, correct_answer

def random_math_challenge():
    """
    Randomly picks one of the three math sub-challenges
    and returns (challenge_text, correct_answer).
    """
    challenges = [math_challenge_factorial, math_roulette_challenge, math_challenge_equation]
    chosen_func = random.choice(challenges)
    return chosen_func()
