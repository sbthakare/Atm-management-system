

import string
import os
# creatinga lists of users, their PINs and bank statements
users = ['user1', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0
# while loop checks existance of the enterd username
while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	if user in users:
		if user == users[0]:
			n = 0
		elif user == users[1]:
			n = 1
		else:
			n = 2
		break
	else:
		print('----------------')
		
		print('INVALID USERNAME')
		
		print('----------------')

# comparing pin
while count < 3:
	print('------------------')
	
	pin = input('PLEASE ENTER PIN: ')
	
	print('------------------')
	if pin.isdigit():
		if user == 'user1':
			if pin == pins[0]:
				break
			else:
				count += 1
				print('-----------')
				
				print('INVALID PIN')
				
				print('-----------')
				print()

		if user == 'user2':
			if pin == pins[1]:
				break
			else:
				count += 1
				print('-----------')
				print('***********')
				print('INVALID PIN')
				print('***********')
				print('-----------')
				print()
				
		if user == 'user3':
			if pin == pins[2]:
				break
			else:
				count += 1
				print('-----------')
				
				print('INVALID PIN')
				
				print('-----------')
				print()
	else:
		print('------------------------')
		
		print('PIN CONSISTS OF 4 DIGITS')
		
		print('------------------------')
		count += 1
	


	
print(str.capitalize(users[n]), 'welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')
# Main menu
while True:
	#os.system('clear')
	print('-------------------------------')
	print('*******************************')
	response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nDeposit__(D)    \nQuit_______(Q) \n: ').lower()
	
	print('-------------------------------')
	valid_responses = ['s', 'w', 'd', 'p', 'q']
	response = response.lower()
	if response == 's':
		print('---------------------------------------------')
		print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],' ON YOUR ACCOUNT.')
		print('---------------------------------------------')
	elif response == 'w':
		print('---------------------------------------------')
		cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
		print('---------------------------------------------')
		if cash_out%100 != 0:
			print('------------------------------------------------------')
			print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 100 rs NOTES')
			print('------------------------------------------------------')
		elif cash_out > amounts[n]:
			print('-----------------------------')
			print('YOU HAVE INSUFFICIENT BALANCE')
			print('-----------------------------')
		else:
			amounts[n] = amounts[n] - cash_out
			print('-----------------------------------')
			print('YOUR NEW BALANCE IS: ', amounts[n], )
			print('-----------------------------------')
			
	elif response == 'd':
		
		print('---------------------------------------------')
		cash_in = int(input('ENTER AMOUNT YOU WANT TO Deposit: '))
		print('---------------------------------------------')
		print()
		if cash_in%100 != 0:
			print('----------------------------------------------------')
			print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 100')
			print('----------------------------------------------------')
		else:
			amounts[n] = amounts[n] + cash_in
			print('----------------------------------------')
                        print('YOUR NEW BALANCE IS: ', amounts[n], )
			print('----------------------------------------')
	
	elif response == 'q':
		exit()
	else:
		print('------------------')
		print('******************')
		print('RESPONSE NOT VALID')
		print('******************')
		print('------------------')
