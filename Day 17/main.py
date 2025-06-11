from data import question_data
import os
from quiz_brain import QuizBrain
from question_model import Question

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_quiz():
    question_bank = []

    for question in question_data:
        new_question = Question(question["question"], question["answer"])
        question_bank.append(new_question)

    qb = QuizBrain(question_bank)
    while qb.has_more_questions():
        qb.ask_next_question()

while True:
    start_quiz()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Goodbye!")
        break
    clear_screen()