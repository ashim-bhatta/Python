class QuizBrain:

    def __init__(self, question_list):
        self.no_of_question = 0
        self.question_list = question_list
        self.user_score = 0

    def next_question(self):
        current_question = self.question_list[self.no_of_question]
        self.no_of_question += 1
        user_input = input(f'Q.{self.no_of_question}: {current_question.question} (True/False): ')
        if user_input.lower() == 't' or user_input.lower() == 'true':
            user_answer = 'True'
        else:
            user_answer = 'False'

        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        if len(self.question_list) <= self.no_of_question:
            print(f'Your score is {self.user_score} out of {len(self.question_list)}')
            return False
        else:
            return True

    def check_answer(self, user_answer, current_question_answer):
        if user_answer == current_question_answer:
            print('You got it right!!!')
            self.user_score += 1
        else:
            print('Opps! Wrong answer')
        print('\n')
