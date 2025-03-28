import time
from io import text_encoding

THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self , quiz_brain: QuizBrain):
        self.quiz   = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20 , pady=20 , bg=THEME_COLOR)
        self.score_label = Label(text='Score: 0' , fg='white' , bg=THEME_COLOR)
        self.score_label.grid(row=0 , column=1)

        self.canvas = Canvas(width=300 , height=350)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Some Question Text' ,
            fil=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        ##True Button
        true_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=true_image , highlightthickness=0, command=self.true_press)
        self.true_button.grid(row=2 , column=0 )

        ##False Image
        false_image =  PhotoImage(file='./images/false.png')
        self.false_button = Button(image=false_image , highlightthickness=0, command=self.false_press)
        self.false_button.grid(row=2 ,column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score_label.config(text=f'score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='End of the Quiz')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_press(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_press(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)


