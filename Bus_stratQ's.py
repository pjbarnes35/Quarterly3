import sqlite3

strategy_questions = [
    {
        "question": "What is competitive advantage?",
        "options": ["A. The unique position a company occupies in its industry", "B. The amount of market share a company has", "C. The level of profitability a company achieves", "D. The number of products a company offers"],
        "correct_answer": "A"
    },
    {
        "question": "What is strategic planning?",
        "options": ["A. The process of setting short-term goals and objectives", "B. The development of long-term plans to achieve organizational goals", "C. The analysis of competitors' strengths and weaknesses", "D. The implementation of tactical initiatives"],
        "correct_answer": "B"
    },
    {
        "question": "What is SWOT analysis?",
        "options": ["A. Assessing a company's strengths, weaknesses, opportunities, and threats", "B. Calculating return on investment", "C. Identifying key performance indicators", "D. Analyzing market segmentation"],
        "correct_answer": "A"
    },
    {
        "question": "What is market segmentation?",
        "options": ["A. Dividing a market into distinct groups of buyers with different needs, characteristics, or behaviors", "B. Analyzing customer satisfaction levels", "C. Forecasting future market trends", "D. Developing pricing strategies"],
        "correct_answer": "A"
    },
    {
        "question": "What is differentiation strategy?",
        "options": ["A. Creating unique products or services that offer superior value to customers", "B. Selling products at the lowest possible price", "C. Expanding into new geographic markets", "D. Developing a niche market"],
        "correct_answer": "A"
    },
    {
        "question": "What is cost leadership?",
        "options": ["A. Becoming the lowest-cost producer in an industry", "B. Differentiating products based on quality and features", "C. Pursuing growth through mergers and acquisitions", "D. Focusing on a narrow market segment"],
        "correct_answer": "A"
    },
    {
        "question": "What is blue ocean strategy?",
        "options": ["A. Creating uncontested market space by offering innovative products or services", "B. Expanding market share through aggressive pricing tactics", "C. Achieving growth through strategic alliances", "D. Targeting high-value customers with premium offerings"],
        "correct_answer": "A"
    },
    {
        "question": "What is strategic alignment?",
        "options": ["A. Ensuring that organizational goals and activities are coordinated and supportive", "B. Managing risk through diversification", "C. Identifying opportunities for international expansion", "D. Implementing technology to improve operational efficiency"],
        "correct_answer": "A"
    },
    {
        "question": "What is corporate governance?",
        "options": ["A. The system of rules, practices, and processes by which a company is directed and controlled", "B. The process of managing"],
        "correct_answer": "A"
    },
    {
        "question": "What is the role of a mission statement in business strategy?",
        "options": ["A. Communicating the company's purpose and values to stakeholders", "B. Setting financial targets and performance metrics", "C. Analyzing market trends and competitive forces", "D. Identifying opportunities for cost reduction"],
        "correct_answer": "A"
    },
]

def insert_questions():
    try:
        conn = sqlite3.connect('class.db')
        cursor = conn.cursor()

        for question in strategy_questions:
            q = question["question"]
            options = ', '.join(question["options"])
            correct_answer = question["correct_answer"]
            
            cursor.execute('''INSERT INTO Bus_strat (question, options, correct_answer) VALUES (?, ?, ?)''',
                           (q, options, correct_answer))

        conn.commit()
        print("Questions inserted successfully!")

    except sqlite3.Error as e:
        print("Error inserting questions:", e)

    finally:
        if conn:
            conn.close()

# Call the function to insert questions into the Bus_strat table
insert_questions()
