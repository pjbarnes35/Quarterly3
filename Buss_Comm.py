import sqlite3

communications_questions = [
    {
        "question": "What is the purpose of a business report?",
        "options": ["A. Presenting financial statements to shareholders", "B. Providing information and analysis to support decision-making", "C. Communicating marketing messages to customers", "D. Documenting employee performance"],
        "correct_answer": "B"
    },
    {
        "question": "What is the difference between formal and informal communication?",
        "options": ["A. Formal communication follows established channels and protocols, while informal communication is casual and spontaneous", "B. Formal communication is written, while informal communication is verbal", "C. Formal communication is used for internal communication, while informal communication is used for external communication", "D. Formal communication is mandatory, while informal communication is optional"],
        "correct_answer": "A"
    },
    {
        "question": "What is active listening?",
        "options": ["A. Paying full attention to the speaker and providing feedback to confirm understanding", "B. Interrupting the speaker to ask questions or share opinions", "C. Focusing on one's own thoughts and ideas instead of listening to others", "D. Reacting emotionally to the speaker's message without considering its content"],
        "correct_answer": "A"
    },
    {
        "question": "What is the purpose of a business presentation?",
        "options": ["A. Sharing information with stakeholders", "B. Persuading others to take a specific action", "C. Providing updates on project progress", "D. All of the above"],
        "correct_answer": "D"
    },
    {
        "question": "What is the role of body language in communication?",
        "options": ["A. Reinforcing spoken messages and conveying emotions", "B. Providing additional information not included in the verbal message", "C. Interpreting data and presenting findings", "D. Ensuring that messages are received and understood by the intended audience"],
        "correct_answer": "A"
    },
    {
        "question": "What is the purpose of a business proposal?",
        "options": ["A. Soliciting feedback from stakeholders", "B. Outlining a plan for addressing a specific business need", "C. Reporting on the results of a research project", "D. Providing a summary of key findings and recommendations"],
        "correct_answer": "B"
    },
    {
        "question": "What is the difference between persuasion and manipulation?",
        "options": ["A. Persuasion involves influencing others through reasoning and evidence, while manipulation involves deceiving others for personal gain", "B. Persuasion focuses on building trust and rapport, while manipulation relies on coercion and intimidation", "C. Persuasion is ethical, while manipulation is unethical", "D. Persuasion leads to mutually beneficial outcomes, while manipulation leads to one-sided outcomes"],
        "correct_answer": "A"
    },
    {
        "question": "What is the purpose of a business memo?",
        "options": ["A. Providing feedback on employee performance", "B. Documenting decisions and agreements reached in meetings", "C. Sharing updates on project progress", "D. Soliciting input from team members"],
        "correct_answer": "B"
    },
    {
        "question": "What is the difference between formal and informal writing?",
        "options": ["A. Formal writing follows standard conventions and is structured, while informal writing is casual and conversational", "B. Formal writing is used for internal communication, while informal writing is used for external communication", "C. Formal writing is mandatory, while informal writing is optional", "D. Formal writing is professional, while informal writing is personal"],
        "correct_answer": "A"
    },
    {
        "question": "What is the purpose of a business email?",
        "options": ["A. Sending meeting invitations and scheduling appointments", "B. Sharing information and collaborating with colleagues", "C. Communicating with customers and clients", "D. All of the above"],
        "correct_answer": "D"
    },
]

def insert_questions():
    try:
        conn = sqlite3.connect('class.db')
        cursor = conn.cursor()

        for question in communications_questions:
            q = question["question"]
            options = ', '.join(question["options"])
            correct_answer = question["correct_answer"]
            
            cursor.execute('''INSERT INTO Bus_Comm (question, options, correct_answer) VALUES (?, ?, ?)''',
                           (q, options, correct_answer))

        conn.commit()
        print("Questions inserted successfully!")

    except sqlite3.Error as e:
        print("Error inserting questions:", e)

    finally:
        if conn:
            conn.close()

# Call the function to insert questions into the Bus_Comm table
insert_questions()
