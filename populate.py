import sqlite3

# Connect to the database
conn = sqlite3.connect("class.db")
cr = conn.cursor()

# Define Function to populate data
def add_QnA(question, answer):
    cr.execute("INSERT INTO Buss_Dev_App (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    print("Question added to Buss Dev :)")

# Adding questions outside the function
#add_QnA("What is the Accronym for Cost Of Goods Sold?", "COGS")
# add_QnA("What is the term for software applications designed to support business growth and expansion?", "APPLICATIONS")
# add_QnA("Define 'customer relationship management (CRM)' in business development applications.", "CRM")
# add_QnA("What type of application is used to manage sales activities and customer interactions?", "SALES")
# add_QnA("Explain the concept of 'lead generation' in business development applications.", "LEADS")
# add_QnA("What is the term for software that helps businesses manage their marketing campaigns and strategies?", "MARKETING")
# add_QnA("Define 'business intelligence (BI)' in the context of business development applications.", "INTELLIGENCE")
# add_QnA("What type of application is used to streamline and automate business processes?", "AUTOMATION")
# add_QnA("Explain the concept of 'pipeline management' in business development applications.", "PIPELINE")
# add_QnA("What is the term for software that facilitates communication and collaboration within an organization?", "COLLABORATION")
# add_QnA("Define 'enterprise resource planning (ERP)' in the context of business development applications.", "ERP")


# Close the connection
conn.close()