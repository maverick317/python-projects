# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:06:57 2019

@author: Maverick
"""

#Guess The Number 

#import the necessary libraries
import random as rd

#generate random numbers
choice = rd.randint(1,10)

#ask the user for their input
number = int(input("Please enter a random number between 1 and 10: "))
if number > 10:
    print("Please enter a number between 1 and 10")
else:
    print("This is the number you have entered: ",number)

#compare the number with the random numner
if choice == number:
    print("You have guessed the correct number !!!")
else:
    print("You have guessed the wrong number !!!")

#print both the numbers
print("You have guessed:",number)
print("The correct choice is:",choice)
