from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Create a question bank from question data
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create a QuizBrain instance with the question bank
quiz = QuizBrain(question_bank)

# Create a QuizInterface instance for the user interface
quiz_ui = QuizInterface(quiz)
