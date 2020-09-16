import sqlite3
import pandas as pd
connection = sqlite3.connect("Data.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE employees (Employee_ID INTEGER, First_Name TEXT, Last_Name TEXT,Age INTEGER,Salary TEXT,primary key(Employee_ID))")
cursor.execute("INSERT INTO employees VALUES (1, 'Evelyn', 'Grace',26,'280$')")
cursor.execute("INSERT INTO employees VALUES (2, 'Olivia', 'Harper',28,'320$')")
cursor.execute("INSERT INTO employees VALUES (3, 'Robert', 'Hall',24,'310$')")
cursor.execute("INSERT INTO employees VALUES (4, 'Doug', 'Judi',32,'370$')")
cursor.execute("INSERT INTO employees VALUES (5, 'Leo', 'Valdez',22,'270$')")
display (pd.read_sql_query("SELECT * FROM employees", connection))