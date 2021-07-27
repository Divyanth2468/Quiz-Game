from tkinter import *
import time
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280, text="dsdfhbdfbjkdf", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        right_image = PhotoImage(file='images/true.png')
        wrong_image = PhotoImage(file="images/false.png")
        self.right_button = Button(image=right_image, command=self.check_true)
        self.wrong_button = Button(image=wrong_image, command=self.check_false)
        self.right_button.grid(row=3, column=0)
        self.wrong_button.grid(row=3, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"The quiz is over, final score is Score: {self.quiz.score}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def check_true(self):
        self.check_answer("True")

    def check_false(self):
        self.check_answer("false")

    def check_answer(self, user_ans):
        correct = self.quiz.check_answer(user_ans)
        if correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(500, func=self.get_next_question)
