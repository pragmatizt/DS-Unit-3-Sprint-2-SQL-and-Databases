import pandas as pd
import sqlite3 as sqlite3
# import tabulate

# define our connection and our cursor.
conn = sqlite3.connect('demo_data.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE demo (s TEXT, x REAL, y REAL)""")

c.execute("INSERT INTO demo VALUES ('g', 3, 9)")
c.execute("INSERT INTO demo VALUES ('v', 5, 7)")
c.execute("INSERT INTO demo VALUES ('f', 8, 7)")

conn.commit()
conn.close()

# 1: Count how many rows you have
query1 = c.execute("SELECT COUNT(*) from demo")
print(count)

#2 is incomplete.  the query is not adding the results of my x and y columns
# 2: how many rows where both x and y are at least 5
query2 = c.execute("""SELECT x, y
                    FROM demo
                    WHERE x AND y >= 5.0""")

# again... same as #2.  I don't know how to basically do a search that INCLUDES
# both columns.  It looks like it's only reading ONE column.
# 3: how many unique values of y are there
query3 = c.execute("SELECT DISTINCT x, y FROM demo")
