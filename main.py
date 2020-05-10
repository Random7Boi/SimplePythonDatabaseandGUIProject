#region import modules and packages

import sqlite3

import os

#endregion

#region variables

tableID = 0
_firstName = None
_lastName = None
_email = None
_address = None
_city = None
_state = None
_zipcode = None 

#endregion

#region Initialize

os.system('cls') # clears the terminal from code, use 'clear' on linux/Mac

#endregion

#region Database

# function to create database if not already made
def createDatabase():

	#searches for database with name provided to connect to, if no db found, it will create one
	conn = sqlite3.connect('FirstTry.db')

	# create cursor to edit and work the database
	c = conn.cursor()

	# create table, execute function launches parameter commands to database, 
	# paranthesis in table name define the table dimensions and properties,
	# IF NOT EXISTS should return null instead of errors if the table already exists
	# also the string format matters alot to avoid syntax errors
	c.execute("""CREATE TABLE IF NOT EXISTS testing (
		ID INTEGER, 
		first_name TEXT, 
		last_name TEXT, 
		email TEXT,
		address TEXT,
		city TEXT,
		state TEXT,
		zipcode INTEGER
		) """)

	# commit changes to database
	conn.commit()

	#close database connection
	conn.close()

# display the items stored in database
def showTable():
	
	# Create a database or connect to one
	conn = sqlite3.connect('FirstTry.db')
	# Create cursor
	c = conn.cursor()

	# pull data from database, select everything from table
	c.execute('SELECT * FROM testing')
	# # fetchone, fetchmany, fetchall records from table to use them
	# # [0] will print the whole tuple, [0][#] will print the item in tuple
	items = c.fetchall()

	for item in items:
		print(str(item[0]) + " " + item[1] + " " + item[2] + " " + item[3] + " " + item[4] + " " + item[5] + " " + item[6] + " " + item[7] + " " + item[8])

	# commit changes to database
	conn.commit()

	#close database connection
	conn.close()

# Create Update function to update a record
def update(orderID, firstName, lastName, email, address, city, state, zipcode):

	global _firstName
	global _lastName
	global _email
	global _address
	global _city
	global _state
	global _zipcode

	_firstName = firstName
	_lastName = lastName
	_email = email
	_address = address
	_city = city
	_state = state
	_zipcode = zipcode

	# Create a database or connect to one
	conn = sqlite3.connect('FirstTry.db')
	# Create cursor
	c = conn.cursor()

	# update table, insert data to table
	c.execute("""UPDATE testing SET
	first_name = :first,
	last_name = :last,
	email = :eml,
	address = :addrss,
	city = :cty,
	state = :stt,
	zipcode = :zcode
	WHERE ID = :tID""", 
	{
		'first': _firstName,
		'last': _lastName,
		'eml': _email,
		'addrss': _address,
		'cty': _city,
		'stt': _state,
		'zcode': _zipcode,
		'tID': orderID
	})

	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()

# insert a new record to table
def insert(firstName, lastName, email, address, city, state, zipcode):

	global tableID

	# Create a database or connect to one
	conn = sqlite3.connect('FirstTry.db')
	# Create cursor
	c = conn.cursor()

	#count the number of rows in table to calculate tableID
	rowCount = c.execute('select count(*) from testing')
	tableID = rowCount.fetchone()[0]
	tableID += 1

	# list all the arguments needed to insert into the table
	parameters = [tableID, firstName, lastName, email, address, city, state, zipcode]

	# update table, insert data to table
	c.execute("INSERT INTO testing VALUES (?, ?, ?, ?, ?, ?, ?, ?) ", parameters)

	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()

# query function, does what show table does, but for the GUI instead of the console
def show_query():
	
	# Create a database or connect to one
	conn = sqlite3.connect('FirstTry.db')
	# Create cursor
	c = conn.cursor()

	# pull data from database, select everything from table
	c.execute('SELECT * FROM testing')
	# # fetchone, fetchmany, fetchall records from table to use them
	# # [0] will print the whole tuple, [0][#] will print the item in tuple
	items = c.fetchall()

	print_Items = ''

	# change this for query function, + "\t" + str(item[1]) + ", "
	for item in items:
		print_Items += str(item[0]) + ", " + str(item[1]) + ", " + str(item[2]) + ", " + str(item[3]) + ", " + str(item[4]) + ", " + str(item[5]) + ", " + str(item[6]) + ", " + str(item[7]) + "\n"

	print(print_Items)

	# commit changes to database
	conn.commit()

	#close database connection
	conn.close()

	return print_Items

# delete query from record
def delete(orderID):

	# Create a database or connect to one
	conn = sqlite3.connect('FirstTry.db')
	# Create cursor
	c = conn.cursor()

	#delete a row from the table
	entry = (orderID,)
	c.execute("DELETE FROM testing WHERE ID = ?;",entry)

	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()

#createDatabase()
#insert("anonymous", "penguin", "ap@gmail.com")
#update(2, "two", "man", "atm@gmail.com")
#delete(2)
#showTable()
#print(str(_firstName) + " " + str(_lastName) + " " + str(_email) + " " + str(tableID))

#endregion