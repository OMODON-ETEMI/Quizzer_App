
# Quizzer App

The Quizzer App is a Python-based quiz game that lets you test your knowledge with a series of True/False questions. The game fetches questions from an online trivia API and provides an interactive user interface for playing the quiz.

## Components

### Quiz Brain

The `QuizBrain` class is responsible for managing the quiz's logic. It keeps track of the questions, user scores, and whether there are more questions to answer. The game is won or lost based on the user's answers.

### User Interface

The user interface is provided by the `QuizzUi` class in the `ui.py` file. It displays the questions, handles user input, and shows the user's score. The UI is built using the Tkinter library.

### Open Trivia API

The app uses the Open Trivia API to fetch a set of questions. It sends a GET request to the API with specific parameters to get questions of a specified type and quantity.

## How to Play

1. The Quizzer App starts by fetching a set of True/False questions from the Open Trivia API.
2. The game initializes, and you are presented with one question at a time.
3. You can answer each question by clicking the "True" or "False" buttons on the UI.
4. The app will provide instant feedback on whether your answer was correct or not.
5. Your current score is displayed at the top of the UI.
6. When all questions have been answered, the app will show your final score.

## How to Run

To run the Quizzer App, execute the `main.py` script in your Python environment.

```bash
python main.py

