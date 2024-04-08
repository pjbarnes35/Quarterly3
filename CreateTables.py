import sqlite3

def add_tables():
    try:
        conn = sqlite3.connect('class.db')
        cursor = conn.cursor()

         # Adding the questions table with fields: id, name, and description
        cursor.execute('''CREATE TABLE IF NOT EXISTS questions
                          (id INTEGER PRIMARY KEY,
                           name TEXT NOT NULL,
                           description TEXT)''')
        
        # Adding the Finance table with fields: id, name, and description
        cursor.execute('''CREATE TABLE IF NOT EXISTS Finance
                          (id INTEGER PRIMARY KEY,
                           name TEXT NOT NULL,
                           description TEXT)''')

        # Adding the Business_app table with fields: id, name, and description
        cursor.execute('''CREATE TABLE IF NOT EXISTS Business_app
                          (id INTEGER PRIMARY KEY,
                           name TEXT NOT NULL,
                           description TEXT)''')

        # Adding the Adv_cap table with fields: id, name, and description
        cursor.execute('''CREATE TABLE IF NOT EXISTS Adv_cap
                          (id INTEGER PRIMARY KEY,
                           name TEXT NOT NULL,
                           description TEXT)''')

        # Adding the Bus_strat table with fields: id, name, and description
        cursor.execute('''CREATE TABLE IF NOT EXISTS Bus_strat
                          (id INTEGER PRIMARY KEY,
                           name TEXT NOT NULL,
                           description TEXT)''')

        # Adding the Bus_Comm table with fields: id, name, and description
        cursor.execute('''CREATE TABLE IF NOT EXISTS Bus_Comm
                          (id INTEGER PRIMARY KEY,
                           name TEXT NOT NULL,
                           description TEXT)''')
        
        conn.commit()
        print("Tables added successfully!")
        
    except sqlite3.Error as e:
        print("Error adding tables:", e)
        
    finally:
        if conn:
            conn.close()

# Call the function to add tables to the database
add_tables()
