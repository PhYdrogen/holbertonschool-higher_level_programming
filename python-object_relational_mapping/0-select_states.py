#!/usr/bin/python3
""" DOCUMENTATIONS """
import MySQLdb as DB
# establish a database connection
db_connect = DB.connect(host="localhost", port=3306, user="root", passwd="data", db="hbtn_0e_0_usa")
# create a cursor to enable SQL queries
db_cursor = db_connect.cursor()
# execute SQL code
db_cursor.execute("SELECT * FROM states")
# accessing the data retrieved
rows_selected = db_cursor.fetchall()
for row in rows_selected:
    print(row)