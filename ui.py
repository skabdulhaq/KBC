from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("Kaun Banega Crorepathi")	
        self.quiz = quiz_brain
        self.label = Label(text=f"Score:{self.quiz.score}", bg=THEME_COLOR, font=("Arial", 14, "bold"), fg="white")
        self.window.config(bg=THEME_COLOR, padx=20, pady=30)
        self.correct_image = PhotoImage(file="images/true.png")
        self.incorrect_image = PhotoImage(file="images/false.png")
        self.canvas = Canvas(width=350, height=300)
        # self.canvas.config(bg="green")
        self.question = self.canvas.create_text(175,
                                                150,
                                                text="This Is A Question",
                                                fill=THEME_COLOR,
                                                font=("Arial", 20, "italic"),
                                                width=330)
        self.correct_button = Button(image=self.correct_image,
                                     highlightthickness=0,
                                     command=self.correct)
        self.correct_button.config(padx=30, pady=30)
        self.incorrect_button = Button(image=self.incorrect_image,
                                       highlightthickness=0,
                                       command=self.incorrect
                                       )
        self.incorrect_button.config(padx=30, pady=30,)
        self.label.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.correct_button.grid(column=0, row=2)
        self.incorrect_button.grid(column=1, row=2)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.itemconfig(self.question, text=self.quiz.next_question())

    def correct(self):
        self.feedback(self.quiz.check_answer("True"))

    def incorrect(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, answer):
        if answer:
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question, fill="white")
            times = self.window.after(1500, self.next_bg)
            # self.window.after_cancel(times)

        else:
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question, fill="white")
            times = self.window.after(1500, self.next_bg)
            # self.window.after_cancel(times)

    def next_bg(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question, fill=THEME_COLOR)
            self.next_question()
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question, fill=THEME_COLOR)
            self.label.config(text="")
            self.canvas.itemconfig(self.question, text=f"Your Quiz Is Completed Your Final Score Is {self.quiz.score}")
            self.correct_button.config(state="disable")
            self.incorrect_button.config(state="disable")

