import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('class.db')
        cursor = conn.cursor()
        
        # Creating a table called 'students' with fields: id, name, age, and grade
        cursor.execute('''CREATE TABLE IF NOT EXISTS Finance
                          (id INTEGER PRIMARY KEY,
                           name TEXT NOT NULL,
                           age INTEGER,
                           grade TEXT)''')
        
        conn.commit()
        print("Database 'class.db' created successfully!")
        
    except sqlite3.Error as e:
        print("Error creating database:", e)
        
    finally:
        if conn:
            conn.close()

# Call the function to create the database
create_database()
