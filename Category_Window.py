import tkinter as tk
import sqlite3

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz App")

        self.categories = ["Finance", "Business Applications Development", "Advanced Business Analytics Capstone", "Business Strategy", "Business Communications 2"]

        self.category_var = tk.StringVar()
        self.category_var.set(self.categories[0])

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Select Category:").pack()

        self.category_menu = tk.OptionMenu(self.master, self.category_var, *self.categories)
        self.category_menu.pack()

        start_button = tk.Button(self.master, text="Start Quiz Now", command=self.start_quiz)
        start_button.pack()

    def start_quiz(self):
        category = self.category_var.get()
        self.master.destroy()  # Close the current window
        QuizWindow(category)   # Open the quiz window with the selected category

class QuizWindow:
    def __init__(self, category):
        self.category = category
        self.questions = self.fetch_questions()
        self.current_question_index = 0

        self.master = tk.Tk()
        self.master.title("Quiz Window")

        self.question_label = tk.Label(self.master, text="")
        self.question_label.pack()

        self.option_var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            option_button = tk.Radiobutton(self.master, text="", variable=self.option_var, value=str(i))
            option_button.pack()
            self.option_buttons.append(option_button)

        next_button = tk.Button(self.master, text="Next", command=self.next_question)
        next_button.pack()

        self.display_question()

    def fetch_questions(self):
        conn = sqlite3.connect('class.db')
        c = conn.cursor()
        c.execute('SELECT * FROM questions WHERE category=?', (self.category,))
        questions = c.fetchall()
        conn.close()
        return questions

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data[2])
            options = question_data[3:7]
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
        else:
            tk.messagebox.showinfo("Quiz Finished", "End of questions!")

    def next_question(self):
        selected_option_index = int(self.option_var.get())
        selected_option = self.option_buttons[selected_option_index].cget("text")
        correct_answer = self.questions[self.current_question_index][7]

        if selected_option == correct_answer:
            tk.messagebox.showinfo("Result", "Correct!")
        else:
            tk.messagebox.showinfo("Result", "Incorrect!")

        self.current_question_index += 1
        self.display_question()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
