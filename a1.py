# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
[Paste the prompt you used to generate your problem set here]
I am a highschool begginer in python but have some experience with java up to things like arrays, while loops, and making both methods and classes. I do not know much of python at all. Give me 5 practice problems for python that cover basics like variables, while loops, arrays, asking for user input, and conditionals like if, if else, else. These are to help me learn, so go easy on me.
Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
1. Simple Number Guessing Game

Ask the user to guess a number between 1 and 10.

If the guess is correct (choose a fixed number, like 7), print "You guessed it!"

Otherwise, print "Try again!" and keep asking until they guess correctly.

Concepts: variables, input, while loop, if-else

2. Sum of Numbers

Ask the user to enter numbers one by one.

Keep adding them to a total sum.

When the user enters 0, stop asking for numbers.

Print the total sum of all numbers entered (except the 0).

Concepts: input, while loop, variables

3. Check Even or Odd

Ask the user to enter a number.

Print "Even" if the number is even, or "Odd" if the number is odd.

Concepts: input, variables, conditionals, modulo operator %

4. List and Print Fruits

Create a list of 5 fruits (hard-coded).

Print each fruit on a new line using a loop.

Concepts: lists (arrays), loops

5. Find the Largest Number

Ask the user to enter 5 numbers (one by one).

Store them in a list.

Find and print the largest number from the list.

Concepts: lists, input, variables, loops, conditionals
"""

# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable
"""

"""
Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False

"""


def guess():
    """
    Number guessing.
    Asks user for number. they must guess 6

    """
    usernumber = input("Give me a number between 1-10. I will tell you if you got thenumber correct :D ")
    guess = int(usernumber)
    number = 6
    if guess == number:
         print("Wow, you actually got it right!")
    else:
        print("Ya got it wrong. you suck.")

def infinite():
    """
    User adds numbers until they put the number zerio, which stops the loop. 
    """
    print("I want you to keep adding numbers, atleast until you add zero, which will stop everything :D you will start with 0.")
    n = int(0)
    life = int(8)
    god = int(0)
    while life != n:
        life = int(input("give numbers :D "))
        god += life
    print("You ended with " + str(god))

def even():
    """
    To see if Users number is even or odd. It justs ask the user and they must put a number in, then it finds the remainder of the number. 
    If the nmber is even, the remainder should be zero when divided by two.
    If the number is odd, a remainder should exist when divided by two.
    """
    num = int(input("Give me a number :D "))
    if num % 2 == 0:
        print("Your number is even :D")
    else: 
        print("Your number is odd :D") 


def listFruit():
    """
    Prints a list of five fruits. Uses a while loop to print them all
    """
    list = ["Apple", "Orange", "Grape", "Mango", "DragonFruit"]
    nn = int(0)
    while nn < 5:
        print (list[nn])
        nn = nn + 1


def big():
    """
    Made to find the biggest number of a list of five numbers that the user gives.
    Goes through a while loop to see which numbers the user printed is bigger.
    If it comes across a number bigger than the previous number, it will save the bigger number, and repeat.
    At the end, it prints the bigger number.
    """
    nnn = int(0)
    great = int(0)
    numList = [0,0,0,0,0]
    while nnn < 5:
        numb = int(input("Give me 5 numbers: "))
        numList[nnn] = numb
        if numb > great:
            great = numb
            nnn += 1
        else:
            nnn += 1
        print(str(nnn))
    print("The greatest number is: " + str(great))










print("Testing Problem 1:")
guess()



#usernumber = input("Give me a number between 1-10. I will tell you if you got thenumber correct :D ")
#guess = int(usernumber)
#number = 6
#if usernumber == number:
   # print("Wow, you actually got it right!")
#else:
    #print("Ya got it wrong. you suck.")

print("\nTesting Problem 2:")
infinite()



#print("I want you to keep adding numbers, atleast until you add zero, which will stop everything :D you will start with 0.")
#n = int(0)
#life = int(8)
#god = int(0)
#while life != n:
    #life = int(input("give numbers :D "))
    #god += life
#print("You ended with " + str(god))



print("\nTesting Problem 3:")
even()



#num = int(input("Give me a number :D "))
#if num % 2 == 0:
   # print("Your number is even :D")

#else: 
   # print("Your number is odd :D") 



print("\nTesting Problem 4:")
listFruit()


#list = ["Apple", "Orange", "Grape", "Mango", "DragonFruit"]
#nn = int(0)
#while nn < 5:
    #print (list[nn])
    #nn = nn + 1


print("\nTesting Problem 5:")
big()


# nnn = int(0)
# great = int(0)
# numList = [0,0,0,0,0]
# while nnn < 5:
#     numb = int(input("Give me 5 numbers: "))
#     numList[nnn] = numb
#     if numb > great:
#         great = numb
#         nnn += 1
#     else:
#         nnn += 1
# print("The greatest number is: " + str(great))

