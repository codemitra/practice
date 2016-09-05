#!/usr/bin/env python

import random

'''I wanted to write the program using very simple code and only plain logic. All the comented code was just 
used for debugging and can be deleted.You can add some code to make it more pretty or for example to check
if the number entered has length 4 , but that is just extra..

'''

def compare(our,user):
	cows=0 						#We set the initial value of guessed cows
	bulls=0						#We set the initial value of guessed bulls
	cowIndex=[0,0,0,0]			#The list we use to mark the positions of Cows
	bullIndex=[0,0,0,0]			#The list we use to mark the positions of Bulls

	for i in range(4):			#We first compare the numbers and check for cows
		if our[i]==user[i]:
			#print(i)
			cows+=1
			#loop_break=True
			cowIndex[i]=1		#We mark the positions which have "cows"
			#print(cows)
			#print(bulls)
			#break

	loop_break=False
	for i in range(4):			#We look for bulls
		for j in range(4):
			if (our[i]==user[j] and i!=j and 1!=cowIndex[j] and 1!=cowIndex[i] and \
				1!=bullIndex[j]): 				     							  #If the digit is the same,
				#print(i)														  # but on the different
				#print(j)														  # position, and if there
				bulls+=1														  # is no Cow on that position
				bullIndex[j]=1	#We mark the positions which have "bulls"		  # then we have a Bull

				loop_break=True	#if we find Bull we move to next digit.           
				#print(cows)    # this is so we would avoid having several
				#print(bulls)   # bulls for one digit
				break
			else:
				#print(i)
				#print(j)
				#print(cows)
				#print(bulls)
				continue
		if loop_break:
			#print(i)
			#print(j)
			#print(cows)
			#print(bulls)
			continue
	return(cows,bulls)

def start():
	ournumber=str(random.randint(1000,9999))
	#ournumber="7885"
	print("Let's play a game of Cowbull!") #explanation
	print("I will generate a number, and you have to guess the numbers one digit at a time.")
	print("For every number in the right place, you get a cow. For every one in the wrong place, you get a bull.")
	print("The game ends when you get 4 cows!")
	print("Type exit at any prompt to exit.")
	usernumber=input("\n\nEnter a 4 digit number: ")
	a=1
	while (ournumber!=usernumber):
		#print(ournumber)
		print("\nNumber of times you tried:%i"%a)
		a+=1
		print("Your number:%s\n"%usernumber)
		cows,bulls=compare(ournumber,usernumber)
		print("Cows:%s"%cows)
		print("Bulls:%s"%bulls)
		usernumber=input("\nTry another one: ")
		if usernumber== "exit":
			break

	if ournumber==usernumber:
		print("Congratulations,you guessed it!!!")
	else:
		print ("Better luck next time!")

if __name__ == '__main__':
	start()
	print ("the end")