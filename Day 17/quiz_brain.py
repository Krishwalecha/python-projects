import art

class QuizBrain:
    def __init__(self, question_list):
        print(art.quiz, "\n")
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def has_more_questions(self):
        return self.question_number < len(self.question_list)
    
    def ask_next_question(self):
        self.current_question = self.question_list[self.question_number].question
        self.current_answer = self.question_list[self.question_number].answer
        self.user_answer = input(f"Q{self.question_number + 1}: {self.current_question} (True/False): ").capitalize()
        while self.user_answer not in ["True", "False"]:
            self.user_answer = input("Please enter 'True' or 'False': ").strip().capitalize()
        self.question_number += 1
        self.evaluate_answer(self.current_answer, self.user_answer)

    def evaluate_answer(self, correct_answer, user_answer):
        if correct_answer == user_answer:
            self.score += 1
            print(f"✅ You're right! Current Score: {self.score}/{self.question_number}\n")
        else:
            print(f"❌ You're wrong! The correct answer was: {correct_answer}")
            print(f"Current Score: {self.score}/{self.question_number}\n")

        if not self.has_more_questions():
            percentage = (self.score / self.question_number) * 100
            print(f"🏁 Final Score: {self.score}/{self.question_number}")
            print(f"📊 Accuracy: {percentage:.1f}%")
            print("Thanks for playing!\n")
