#algorithm imports:
import secrets
import string
import random

#visual imports:
import pyfiglet
from termcolor import colored

def header():
	t = pyfiglet.figlet_format("Password generator", font = "digital" )
	print()
	print(colored(t, attrs = ['bold']))
	print("v1.0.\nwritten by Substing as a project for the OSSSSC.")
	print()

def main():
	
	header()

	pw = ""

	
	length = int(input('Please input the desired password length of 4 or over. \n>> '))

	#create a list of all ascii
	allchars = string.ascii_letters + string.digits + string.punctuation

	#create random string using characters
	for i in range(length):
		pw += secrets.choice(allchars)


	#include upper, lower, num, and special characters: most websited require this
	#generate 4 random unique integers
	torep = random.sample(range(length), 4)

	pw = list(pw)
	#the somewhere in the list, one of each case will be placed. 
	pw[torep[0]] = secrets.choice(string.ascii_letters.upper())
	pw[torep[1]] = secrets.choice(string.ascii_letters.lower())
	pw[torep[2]] = secrets.choice(string.digits)
	pw[torep[3]] = secrets.choice(string.punctuation)

	#convert to string again. 
	pw = "".join(pw)

	print('\n'+ "Generated password:\n" + colored(pw, 'green') + '\n')

try:
	main()
#exception handling
except ValueError:
	print("\n" + colored("Error", 'red') + ": You must input an integer value of 4 or over.")
except KeyboardInterrupt:
	print("\n" + colored("Quitting...", 'green'))
except:
	print("\n" + colored("Error", 'red') + ": Unknown error.")
