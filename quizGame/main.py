from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

qlist = []
for x in question_data:
    qtxt = x["text"]
    qans = x["answer"]
    newQ = Question(qtxt, qans)
    qlist.append(newQ)

quiz = QuizBrain(qlist)
while quiz.still_has_questions():
    quiz.next_question()

print(f'congratulation You have completed the quiz! Your total score is {quiz.current_score}/{len(qlist)}')