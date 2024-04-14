# Assignment 12

import sqlite3


conn = sqlite3.connect('massage_therapy_clients.db')
c = conn.cursor()

# 1. Add a text column to your database/table
def add_text_column():
    c.execute("ALTER TABLE client_table ADD COLUMN new_column TEXT")
    conn.commit()

# 2. Add data to the newly created text column
def add_data_to_text_column():
    data = [('Jazlene', 'new 1'),
            ('Andrew', 'new 2'),
            ('Jenny', 'new 3'),
            ('Nancy', 'new 4'),
            ('Jovan', 'new 5')]
    c.executemany("UPDATE client_table SET new_column = ? WHERE name = ?", data)
    conn.commit()

# 3. Modify the new column to be all the same value "ABCD"
def modify_text_column():
    c.execute("UPDATE client_table SET new_column = 'ABCD'")
    conn.commit()

# 4. Update two of the rows using the Update SQL statement and where clause
def update_rows():
    c.execute("UPDATE client_table SET new_column = 'insurance' WHERE name = 'Jazlene'")
    c.execute("UPDATE client_table SET new_column = 'No insurance' WHERE name = 'Andrew'")
    conn.commit()

# 5. Delete a row based on where clause
def delete_row():
    c.execute("DELETE FROM client_table WHERE name = 'Nancy'")
    conn.commit()

# 6. Show a list of all the columns and rows (table dump)
def show_table_dump():
    c.execute("SELECT * FROM client_table")
    print("\nTable Dump:")
    for row in c.fetchall():
        print(row)


    c.close()
    conn.close()


add_text_column()
add_data_to_text_column()
modify_text_column()
update_rows()
delete_row()
show_table_dump()

