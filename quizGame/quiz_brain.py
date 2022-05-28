class QuizBrain:
    def __init__(self, qlist):
        self.question_number = 0
        self.current_score = 0
        self.question_list = qlist

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_ans, cor_ans):
        if user_ans.lower() == cor_ans.lower():
            self.current_score += 1
            print('You got it right!')
        else:
            print('Your answer is wrong :/')
        print(f'The correct answer was {cor_ans}!')
        print(f"Your current score is {self.current_score} / {self.question_number}")

    def next_question(self):
        cur_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {cur_question.text} (True)/(False)? ")
        correct_ans = cur_question.ans
        self.check_answer(user_ans, correct_ans)


