import sqlite3

business_apps_dev_questions = [
    {
        "question": "Which programming language is commonly used for web development?",
        "options": ["A. Java", "B. Python", "C. C++", "D. HTML/CSS/JavaScript"],
        "correct_answer": "D"
    },
    {
        "question": "What does API stand for?",
        "options": ["A. Application Program Interface", "B. Advanced Programming Interface", "C. Application Process Integration", "D. Automated Program Interaction"],
        "correct_answer": "A"
    },
    {
        "question": "What is the difference between front-end and back-end development?",
        "options": ["A. Front-end focuses on user interface, while back-end focuses on server-side logic", "B. Front-end is for mobile apps, while back-end is for web apps", "C. Front-end uses Python, while back-end uses JavaScript", "D. Front-end is for design, while back-end is for marketing"],
        "correct_answer": "A"
    },
    {
        "question": "What is an API?",
        "options": ["A. Automated Program Interaction", "B. Application Program Interface", "C. Advanced Programming Interface", "D. Application Process Integration"],
        "correct_answer": "B"
    },
    {
        "question": "What is the purpose of version control systems like Git?",
        "options": ["A. Managing customer relationships", "B. Tracking changes to code and collaborating with others", "C. Analyzing market trends", "D. Automating business processes"],
        "correct_answer": "B"
    },
    {
        "question": "What is an IDE?",
        "options": ["A. Integrated Development Environment", "B. International Data Encryption", "C. Internet Data Exchange", "D. Internal Data Evaluation"],
        "correct_answer": "A"
    },
    {
        "question": "What is the purpose of database management systems (DBMS)?",
        "options": ["A. Managing physical office locations", "B. Organizing and retrieving data", "C. Designing marketing campaigns", "D. Analyzing financial reports"],
        "correct_answer": "B"
    },
    {
        "question": "What is a framework in software development?",
        "options": ["A. A set of pre-written code that developers can use to build applications more efficiently", "B. A project management tool", "C. A type of testing methodology", "D. A legal document outlining project requirements"],
        "correct_answer": "A"
    },
    {
        "question": "What is the role of an API in web development?",
        "options": ["A. Analyzing performance metrics", "B. Providing a way for different software applications to communicate with each other", "C. Managing employee schedules", "D. Designing user interfaces"],
        "correct_answer": "B"
    },
    {
        "question": "What is the purpose of user acceptance testing (UAT)?",
        "options": ["A. Testing software before it is released to the public", "B. Ensuring that software meets the needs of end-users", "C. Analyzing market trends", "D. Monitoring server performance"],
        "correct_answer": "B"
    },
]

def insert_questions():
    try:
        conn = sqlite3.connect('class.db')
        cursor = conn.cursor()

        for question in business_apps_dev_questions:
            q = question["question"]
            options = ', '.join(question["options"])
            correct_answer = question["correct_answer"]
            
            cursor.execute('''INSERT INTO Business_app (question, options, correct_answer) VALUES (?, ?, ?)''',
                           (q, options, correct_answer))

        conn.commit()
        print("Questions inserted successfully!")

    except sqlite3.Error as e:
        print("Error inserting questions:", e)

    finally:
        if conn:
            conn.close()

# Call the function to insert questions into the Business_app table
insert_questions()
