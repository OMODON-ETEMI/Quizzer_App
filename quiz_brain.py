import html  # Import the HTML module for unescaping HTML entities.

class QuizBrain:

    def __init__(self, q_list):
        # Initialize the QuizBrain with a list of questions.
        self.question_number = 0  # Track the current question number.
        self.score = 0  # Initialize the score to 0.
        self.question_list = q_list  # Store the list of questions.
        self.current_question = None  # Initialize the current question as None.

    def still_has_questions(self):
        # Check if there are more questions in the list.
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Get the next question and format it for display.
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)  # Unescape HTML entities in the question text.
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer):
        # Check if the user's answer matches the correct answer and update the score.
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True  # Return True for a correct answer.
        else:
            return False  # Return False for an incorrect answer.
