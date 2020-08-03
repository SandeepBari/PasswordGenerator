from datetime import datetime
import os 
from os import path
import random
import string

print('1. Manual')
print('2. Automatic')
entry = input();

passTemp1= ""
checkFlag= 0;

if entry == '1':
	numVal= input('Enter Password Length: ')
	print('Enter the Number Range between 0 to 9')
	lowRangeNum= input("Enter lowest range of number: ")
	highRangeNum= input("Enter highest range of number: ")

	if lowRangeNum < highRangeNum:
		StringTemp= input("Enter the characters you want: ")

		for i in range(int(numVal)):
			num= str(random.randint(int(lowRangeNum), int(highRangeNum)))
			alpha= str(random.choice(StringTemp))

			seq= random.randint(0,9)
			if seq % 2 == 0:
				passTemp1 = passTemp1+ alpha+ num

			else:
				passTemp1 = passTemp1+ num+ alpha

		passTemp= passTemp1[1:int(numVal)+1]
		print('Your Password: '+ passTemp)
		checkFlag= 0          

	else:
		print("Please Enter Proper Range")
		checkFlag= 1

elif (entry == '2'):
	numVal= input('Enter Password Length: ')

	for i in range(int(numVal)):
		num= str(random.randint(0,9))
		alphaUpper= str(random.choice(string.ascii_uppercase))
		alphaLower= str(random.choice(string.ascii_lowercase))
		
		seq= random.randint(0,9)
		if seq % 2 == 0:
			passTemp1 = passTemp1+ alphaLower+ num+ alphaUpper
		else:
			passTemp1 = passTemp1+ num+ alphaUpper+ alphaLower
 
	passTemp= passTemp1[1:int(numVal)+1]
	print('Your Password: '+ passTemp)
	checkFlag= 0
   
else:
	print("Please Select Proper Mode Of Generating Password")
	checkFlag= 1


if checkFlag == 0:
	check= input('Do you want to Randomize it More(Y/N)')

	if check == 'y' or check == 'Y':
		password= " "

		for i in range(int(numVal)):
			passTemp2 = random.choice(passTemp1)
			password = password + passTemp2

		print(password)
		passTemp= password;

if path.exists("Password.txt"):
	os.remove("Password.txt")

datetimeVal = str(datetime.now())
f = open("Password.txt", "a")
f.write("Your Password is: ")
f.write(passTemp)
f.write("\n"+ datetimeVal)
f.close()		