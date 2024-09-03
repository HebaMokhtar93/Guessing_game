"""Write a Python program that simulates a basic guessing game. The program should generate a random number between 1 and 100 and ask the user to guess it. Provide feedback to the user whether their guess is high, low, or correct. Use a while loop to allow multiple guesses until the        user correctly guesses the number."""
import random
correct_num=random.randint(0,100)
while True:
    gusse_num=int(input("please enter random nuber:"))
    if gusse_num==correct_num:
        print(f"{correct_num} is correct number")
        break
    elif gusse_num>correct_num:
        print("number is greater than correct nuber ")
    else:
        print("number is smaller than correct number ")