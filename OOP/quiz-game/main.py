from data import question_data
from question_model import Questions
from quiz_brain import QuizBrain

questions_bank = []
for data in question_data:
    new_question = Questions(data['question'], data['correct_answer'])
    questions_bank.append(new_question)

quiz = QuizBrain(questions_bank)
while quiz.still_has_question():
    quiz.next_question()
