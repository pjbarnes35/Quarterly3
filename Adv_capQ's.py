import sqlite3

analytics_questions = [
     {
        "question": "What is predictive modeling?",
        "options": ["A. A statistical technique used to predict future events or outcomes", "B. A method for organizing and analyzing large datasets", "C. A process for creating data visualizations", "D. An approach to optimizing business processes"],
        "correct_answer": "A"
    },
    {
        "question": "What is clustering analysis?",
        "options": ["A. A technique for classifying data into groups based on similarity", "B. A method for calculating statistical correlations", "C. A process for identifying outliers in a dataset", "D. An approach to detecting patterns in time-series data"],
        "correct_answer": "A"
    },
    {
        "question": "What is text mining?",
        "options": ["A. Analyzing unstructured text data to extract meaningful insights", "B. Identifying trends in numerical datasets", "C. Classifying data into predefined categories", "D. Forecasting future events based on historical data"],
        "correct_answer": "A"
    },
    {
        "question": "What is sentiment analysis?",
        "options": ["A. Evaluating the emotional tone of text data", "B. Analyzing financial markets", "C. Assessing the performance of predictive models", "D. Measuring customer satisfaction"],
        "correct_answer": "A"
    },
    {
        "question": "What is time series forecasting?",
        "options": ["A. Predicting future values based on past observations in sequential data", "B. Analyzing cross-sectional data at a single point in time", "C. Estimating the impact of variables on an outcome", "D. Forecasting trends using regression analysis"],
        "correct_answer": "A"
    },
    {
        "question": "What is association rule mining?",
        "options": ["A. Identifying patterns in transactional data", "B. Analyzing variance in experimental designs", "C. Predicting outcomes using decision trees", "D. Calculating probabilities in Bayesian statistics"],
        "correct_answer": "A"
    },
    {
        "question": "What is anomaly detection?",
        "options": ["A. Identifying unusual patterns or outliers in data", "B. Predicting future events based on past observations", "C. Classifying data into distinct categories", "D. Estimating unknown parameters in a model"],
        "correct_answer": "A"
    },
    {
        "question": "What is regression analysis?",
        "options": ["A. Modeling the relationship between variables in numerical data", "B. Identifying clusters in multidimensional datasets", "C. Calculating probabilities based on observed frequencies", "D. Forecasting future events based on historical data"],
        "correct_answer": "A"
    },
    {
        "question": "What is machine learning?",
        "options": ["A. A branch of artificial intelligence that enables computers to learn from data", "B. A method for optimizing business processes", "C. A technique for analyzing financial markets", "D. An approach to database management"],
        "correct_answer": "A"
    },
    {
        "question": "What is optimization?",
        "options": ["A. Finding the best solution to a problem under given constraints", "B. Predicting future events based on historical data", "C. Analyzing patterns in large datasets", "D. Testing hypotheses using statistical methods"],
        "correct_answer": "A"
    },
]

def insert_questions():
    try:
        conn = sqlite3.connect('class.db')
        cursor = conn.cursor()

        for question in analytics_questions:
            q = question["question"]
            options = ', '.join(question["options"])
            correct_answer = question["correct_answer"]
            
            cursor.execute('''INSERT INTO Adv_cap (question, options, correct_answer) VALUES (?, ?, ?)''',
                           (q, options, correct_answer))

        conn.commit()
        print("Questions inserted successfully!")

    except sqlite3.Error as e:
        print("Error inserting questions:", e)

    finally:
        if conn:
            conn.close()

# Call the function to insert questions into the Adv_cap table
insert_questions()
