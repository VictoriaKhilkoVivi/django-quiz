from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List


class QuizResultService():
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    def get_result(self) -> float:

        count_correct = 0
        count_all = len(self.quiz_dto.questions)

        for question in self.quiz_dto.questions:
            correct_choices = [correct_choice.uuid for correct_choice in question.choices
                               if correct_choice.is_correct]
            if self.answers_dto.answers[int(self.quiz_dto.questions.index(question))].choices == correct_choices:
                count_correct += 1

        return count_correct/count_all
