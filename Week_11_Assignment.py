import sqlite3

# Assignment 11 / Week 11

#Create a SQLite database
conn = sqlite3.connect('massage_therapy_clients.db')
c = conn.cursor()

# Create a table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS client_table (name TEXT,age INTEGER, height REAL, city TEXT, phone TEXT, email TEXT)')
    conn.commit()
    

# Insert 5 rows into the table
def insert_data():
    data = [('Jazlene', 25, 5.2, 'Streamwood','111-111-1111', 'jaz@gmail.com'),
            ('Andrew', 30, 6.2, 'Hanover Park', '222-222-2222', 'andy@yahoo.com'),
            ('Jenny', 28, 5.8, 'Streamwood','333-333-3333', 'jenn@yahoo.com'),
            ('Nancy', 35, 5.6, 'Schaumburg', '444-444-4444', 'nancy@gmail.com'),
            ('Jovan', 22, 6.0, 'Palatine', '555-555-5555', 'jovan@ymail.com')]
    c.executemany("INSERT INTO client_table VALUES (?, ?, ?, ?, ?, ?)", data)
    conn.commit()

# Perform SQL queries using cursors
def read_from_db():
    
    # List all columns and rows
    c.execute("SELECT * FROM client_table")
    print("All columns and rows:")
    print(c.fetchall())

    # List all columns but using the where clause select only certain rows using a text column
    c.execute("SELECT * FROM client_table WHERE city='Streamwood'")
    print("\nSelected rows based on city (Streamwood):")
    for row in c.fetchall():
        print(row)
        

    # List only the text columns but all the rows
    c.execute("SELECT name, city, phone, email FROM client_table")
    print("\nOnly text columns but all rows:")
    for row in c.fetchall():
        print(row)

    # Sum one of the real number columns
    c.execute("SELECT SUM(height) FROM client_table")
    print("\nSum of heights:")
    print(c.fetchone()[0])

    # Provide a count of the rows in table
    c.execute("SELECT COUNT(*) FROM client_table")
    print("\nNumber of rows:")
    print(c.fetchone()[0])

    # f. Create a cursor showing all rows and columns
    c.execute("SELECT * FROM client_table")
    print("\nAll rows and columns:")
    for row in c.fetchall():
        print(row)
        
# close cursor and connection  
    c.close()     
    conn.close()

# Call functions 
create_table()
insert_data()
read_from_db()
