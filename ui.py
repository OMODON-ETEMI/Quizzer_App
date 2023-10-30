from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizzUi:
    def __init__(self, quiz_brain: QuizBrain):
        # Initialize the quiz UI
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create a label to display the score
        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Create a canvas to display questions
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Some texts", fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Create buttons for true and false answers
        true_image = PhotoImage(file="Quizzer/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_command)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="Quizzer/images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_command)
        self.false_button.grid(row=2, column=1)

        # Get the first question
        self.get_next_question()

        # Start the main application loop
        self.window.mainloop()

    def get_next_question(self):
        # Get the next question and update the UI
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the Quiz. Your score is {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_command(self):
        # Handle true button click
        self.give_feedback(self.quiz.check_answer('true'))

    def false_command(self):
        # Handle false button click
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, response):
        # Give feedback based on the answer
        if response:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)  # Delay before showing the next question
