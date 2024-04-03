import tkinter as tk

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
        # Add code to initialize the quiz window with the selected category

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
