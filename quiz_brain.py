import html
# from ui import QuizInterface


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer: str) -> bool:
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            # print(f"Your current score is: {self.score}/{self.question_number}")

            return True
        else:
            # print(f"Your current score is: {self.score}/{self.question_number}")

            return False

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")

    def present_score(self) -> int:
        return self.score
