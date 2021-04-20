#!/usr/bin/python

# from mysql.connector import connect, Error

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="school"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
# import functions

# # this is sample of how we can use the login function for the whole system
# if functions.login():
#     functions.startMenu()  
# else:
#     # we simply log out the user due to failure to log in
#     exit()
