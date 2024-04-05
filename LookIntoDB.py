import sqlite3

def count_questions_in_table(table_name):
    try:
        conn = sqlite3.connect('class.db')
        cursor = conn.cursor()

        # Execute a SQL query to count the number of rows in the specified table
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]  # Fetch the result of the query

        print(f"Number of questions in {table_name}: {count}")

    except sqlite3.Error as e:
        print("Error:", e)

    finally:
        if conn:
            conn.close()

def count_tables_in_database():
    try:
        conn = sqlite3.connect('class.db')
        cursor = conn.cursor()

        # Get a list of all tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        print("List of tables in the database:")
        for table in tables:
            print(table[0])

        print(f"\nTotal number of tables: {len(tables)}")

    except sqlite3.Error as e:
        print("Error:", e)

    finally:
        if conn:
            conn.close()

# Call the functions to count questions in each table and the total number of tables
count_tables_in_database()
print()
count_questions_in_table('Finance')
count_questions_in_table('Business_app')
count_questions_in_table('Adv_cap')
count_questions_in_table('Bus_strat')
count_questions_in_table('Bus_Comm')
