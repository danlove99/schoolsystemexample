import getpass
import os
import time 

class school:
	def __init__(self, name, location, noofstudents):
		self.name = name
		self.location = location
		self.noofstudents = noofstudents

	def __str__(self):
		return('{} is a school in {} with {} students'.format(self.name, self.location, self.noofstudents))
		

class student:
	def __init__(self, name, year, grades, form, user, password):
		self.name = name
		self.year = year
		self. grades = grades
		self.form = form
		self.user = user
		self.password = password


class teacher:
	def __init__(self, name, yearsofservice, formclass, pay, age):
		self.name = name
		self.yearsofservice = yearsofservice
		self.formclass = formclass
		self.pay = pay
		self.age = age
	


# defanitions

summerhigh = school('summer high', 'london', 0)

studentlist = {'danlove99' : 'password', 'rowan' : 'password', 'scott' : 'password'}

stafflist = {'mr good' : 'password' , 'mr bad' : 'password', 'mr nice' : 'password'}

studentgrades = {'danlove99' : 'A', 'rowan' : 'B', 'scott' : 'C'}

staffnumbers = {'mr good' : '073849274', 'mr nice' : '83783489', 'mr bad' : '1928384'}

teach = teacher(' ', ' ', ' ', 0.00, 0)

# startup options

def addStudent():
	os.system('clear')
	a = input('username: ')
	b = getpass.getpass('password: ')
	c = getpass.getpass('re-enter password: ')
	if b != c:
		print('passwords do not match!')
		addStudent()
	elif b == c:
		studentlist[a] = b
		mainSystemStudent()

def addStaff():
	os.system('clear')
	a = input('username: ')
	b = getpass.getpass('password: ')
	c = getpass.getpass('re-enter password: ')
	if b != c:
		print('passwords do not match!')
		time.sleep(4)
		addStaff()
	elif b == c:
		stafflist[a] = b

def login():
	os.system('clear')
	usr = input('username: ')
	global usr
	if usr in studentlist:
		passw = getpass.getpass('password: ')
		if passw == studentlist[usr]:
			
			mainSystemStudent()
		else:
			print('Incorrect password!')
			login()
	elif usr in stafflist:
		if usr in 'mr good':
			teach.name = usr
			teach.yearsofservice = 40
			teach.formclass = '7E'
			teach.pay = 11.90 	
			teach.age = 61
		elif usr in 'mr bad':
			teach.name = usr
			teach.yearsofservice = 17
			teach.formclass = '8F'
			teach.pay = 10.45 	
			teach.age = 42
		elif usr in 'mr nice':
			teach.name = usr
			teach.yearsofservice = 10
			teach.formclass = '9E'
			teach.pay = 8.50 	
			teach.age = 30

		passw = getpass.getpass('password: ')
		if passw == stafflist[usr]:
			mainSystemStaff()
	else:
		print('unknown user')
		presstocont()
		login()
	return usr


def presstocont():
	a = input('press enter to continue...\n')


# student options

def getFiles():
	os.system('clear')
	os.system('Files')
	presstocont()
	mainSystemStudent()

def schoolinfo():
	print(summerhigh)
	presstocont()
	mainSystemStudent()

# staff options

def getTimeLeft():
	os.system('clear')
	print(65 - teach.age)
	presstocont()
	mainSystemStudent()

def getStudentList():
	os.system('clear')
	print (studentgrades)
	presstocont()
	mainSystemStaff()

def getStaffNumbers():
	os.system('clear')
	print(staffnumbers)
	presstocont()
	mainSystemStaff()

def getPayCheque():
	os.system('clear')
	how = float(input('how many days have you worked?'))
	money = ((teach.pay * 7.0) * how)
	print(money , 'pounds')
	presstocont()
	mainSystemStaff()


# systems

def mainSystemStudent():
	os.system('clear')
	action = input('grades \ntime left in school \nfiles \nschool info \nlog out \n')
	if action in 'grades':
		try:
			print(studentgrades[usr])
			presstocont()
		except:
			os.system('clear')
			print('no grades yet\n')
			presstocont()
	elif action in 'files':
		getFiles()
		presstocont()
	elif action in 'school info':
		schoolinfo()
	elif action in 'log out':
		login()
	else:
		print('action unavailable')
		presstocont()
	mainSystemStudent()


def mainSystemStaff():
	os.system('clear')
	action = input('students \nstaff numbers \npay cheque \ntime left till retirement \nschool info \nlog out \n')
	if action in 'students':
		getStudentList()
	elif action in 'time':
		getTimeLeft()
		presstocont()
	elif action in 'staff numbers':
		getStaffNumbers()
	elif action in 'paycheque':
		getPayCheque()
	elif action in 'school info':
		schoolinfo()
	elif action in 'log out':
		login()


def main():
	for i in studentlist:
		summerhigh.noofstudents += 1
	os.system('clear')
	a = input('create an account or log in? \n')
	os.system('clear')
	if a in 'create':

		b = input('student or teacher?\n')
		if b in 'student':
			addStudent()
			print('account created!')
			login()
		elif b in 'teacher' or b in 'staff':
			addStaff()
	elif a in 'log in':
		login()

main()