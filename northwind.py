import pandas as pd
import sqlite3 as sqlite3

# define our connection and our cursor.
conn = sqlite3.connect('northwind_small.sqlite3')
c = conn.cursor()

def ten_most_expensive():
    ten_most_expensive_query = """SELECT UnitPrice
                            FROM OrderDetail
                            ORDER BY UnitPrice DESC
                            Limit 10"""

print(f'Ten most expensive by Unit Price:',c.execute(ten_most_expensive_query).fetchall())

def avg_age_employee():
    average_age_employee_query = """SELECT AVG(HireDate - Birthdate)
                                FROM Employee)
                                """
print(f'Average age:',c.execute(average_age_employee_query).fetchall())


### PART THREE
# What are the ten most expensive items (per unit price) in the database and their suppliers?

def most_expensive_supplier():
    most_expensive_supplier_query = """SELECT CompanyName, UnitPrice
                                FROM Supplier
                                INNER JOIN Product
                                ON Supplier.ID = Product.ID
                                ORDER BY UnitPrice DESC"""

print(f'Most Expensive, by supplier:',c.execute(most_expensive_query).fetchall())

def unique_products_category():
    unique_products_category_query = """SELECT DISTINCT ProductName, CategoryID
                                    FROM Product
                                    ORDER BY CategoryID DESC
                                    """
print(f'Most products by category:',c.execute(most_expensive_query).fetchall())

# c.close()
# conn.commit()
