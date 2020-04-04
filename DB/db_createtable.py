#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect("localhost","testuser","test123","Name" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS INFO")

# Create table as per requirement
sql = """CREATE TABLE INFO (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   SEX CHAR(1),
   Birthday FLOAT )"""

cursor.execute(sql)

# disconnect from server
db.close()