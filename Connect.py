import tkinter as tk
from tkinter import messagebox
from quiz_questions import *

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
        self.master.destroy()
        QuizWindow(category)

class QuizWindow:
    def __init__(self, category):
        self.category = category
        self.questions = {
            "Finance": 'finance_questions',
            "Business Applications Development": business_app_dev_questions,
            "Advanced Business Analytics Capstone": advanced_business_analytics_questions,
            "Business Strategy": business_strategy_questions,
            "Business Communications 2": business_communications_questions
        }

        self.current_question = 0
        self.correct_answers = 0

        self.master = tk.Tk()
        self.master.title(f"Quiz - {self.category}")

        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text=self.questions[self.category][self.current_question]["question"])
        self.question_label.pack()

        self.option_vars = []
        for option in self.questions[self.category][self.current_question]["options"]:
            var = tk.StringVar(value="")  # Create a string variable for each option
            self.option_vars.append(var)
            tk.Radiobutton(self.master, text=option, variable=var, value=option).pack()

        submit_button = tk.Button(self.master, text="Submit Answer", command=self.submit_answer)
        submit_button.pack()

    def submit_answer(self):
        selected_option = ""
        for var in self.option_vars:
            if var.get():
                selected_option = var.get()

        correct_answer = self.questions[self.category][self.current_question]["correct_answer"]

        if selected_option == correct_answer:
            messagebox.showinfo("Result", "Correct!")
            self.correct_answers += 1
        else:
            messagebox.showinfo("Result", f"Wrong! Correct answer is {correct_answer}")

        self.current_question += 1

        if self.current_question < len(self.questions[self.category]):
            # Update question and options for the next question
            self.question_label.config(text=self.questions[self.category][self.current_question]["question"])
            for i, option in enumerate(self.questions[self.category][self.current_question]["options"]):
                self.option_vars[i].set(option)
        else:
            # Display final score when all questions are answered
            messagebox.showinfo("Quiz Finished", f"Quiz Finished! Your Score: {self.correct_answers}/{len(self.questions[self.category])}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
