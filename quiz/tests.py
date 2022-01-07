from django.test import TestCase
from typing import List
from .services import QuizResultService
from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO


class BaseTestCase(TestCase):
    def setUp(self):
        choices: List[ChoiceDTO] = [
            ChoiceDTO(
                "1-1-1",
                "An elephant",
                True
            ),
            ChoiceDTO(
                "1-1-2",
                "A mouse",
                False
            )
        ]

        questions: List[QuestionDTO] = [
            QuestionDTO(
                "1-1",
                "Who is bigger?",
                choices
            )
        ]

        self.quiz_dto = QuizDTO(
            "1",
            "Animals",
            questions
        )

    def test_success_quiz_result(self):
        answers: List[AnswerDTO] = [
            AnswerDTO(
                "1-1",
                ["1-1-1"]
            )
        ]

        answers_dto = AnswersDTO(
            "1",
            answers
        )

        quiz_result_service = QuizResultService(
            self.quiz_dto,
            answers_dto
        )

        self.assertEqual(quiz_result_service.get_result(), 1.00)

    def test_failure_quiz_result(self):
        answers: List[AnswerDTO] = [
            AnswerDTO(
                "1-1",
                ["1-1-2"]
            )
        ]

        answers_dto = AnswersDTO(
            "1",
            answers
        )

        quiz_result_service = QuizResultService(
            self.quiz_dto,
            answers_dto
        )

        self.assertEqual(quiz_result_service.get_result(), 0.00)


class QuizTestCase(TestCase):
    def setUp(self):
        choices1: List[ChoiceDTO] = [
            ChoiceDTO(
                "1-1-1",
                "Haskell",
                False
            ),
            ChoiceDTO(
                "1-1-2",
                "Python",
                True
            ),
            ChoiceDTO(
                "1-1-3",
                "C++",
                False
            ),
            ChoiceDTO(
                "1-1-4",
                "Go",
                False
            )
        ]

        choices2: List[ChoiceDTO] = [
            ChoiceDTO(
                "1-2-1",
                "Tuple",
                True
            ),
            ChoiceDTO(
                "1-2-2",
                "Set",
                False
            ),
            ChoiceDTO(
                "1-2-3",
                "List",
                False
            ),
            ChoiceDTO(
                "1-2-4",
                "Dict",
                False
            )
        ]

        choices3: List[ChoiceDTO] = [
            ChoiceDTO(
                "1-3-1",
                "//",
                True
            ),
            ChoiceDTO(
                "1-3-2",
                "%",
                False
            ),
            ChoiceDTO(
                "1-3-3",
                "/",
                False
            ),
            ChoiceDTO(
                "1-3-4",
                "**",
                False
            )
        ]

        choices4: List[ChoiceDTO] = [
            ChoiceDTO(
                "1-4-1",
                "Laravel",
                False
            ),
            ChoiceDTO(
                "1-4-2",
                "Symfony",
                False
            ),
            ChoiceDTO(
                "1-4-3",
                "Django",
                True
            ),
            ChoiceDTO(
                "1-4-4",
                "Flask",
                True
            )
        ]

        choices5: List[ChoiceDTO] = [
            ChoiceDTO(
                "1-5-1",
                "DELETE",
                True
            ),
            ChoiceDTO(
                "1-5-2",
                "POST",
                False
            ),
            ChoiceDTO(
                "1-5-3",
                "PUT",
                True
            ),
            ChoiceDTO(
                "1-5-4",
                "CONNECT",
                False
            )
        ]

        questions: List[QuestionDTO] = [
            QuestionDTO(
                "1-1",
                "Which programming language is interpreted?",
                choices1
            ),
            QuestionDTO(
                "1-2",
                "Which datatype is immutable in python?",
                choices2
            ),
            QuestionDTO(
                "1-3",
                "What operator in python is used to divide without remainder?",
                choices3
            ),
            QuestionDTO(
                "1-4",
                "What frameworks are python frameworks?",
                choices4
            ),
            QuestionDTO(
                "1-5",
                "Which request methods are idempotent?",
                choices5
            )
        ]

        self.quiz_dto = QuizDTO(
            "1",
            "Python",
            questions
        )

    def test_success_quiz_result(self):
        answers: List[AnswerDTO] = [
            AnswerDTO(
                "1-1",
                ["1-1-2"]
            ),
            AnswerDTO(
                "1-2",
                ["1-2-1"]
            ),
            AnswerDTO(
                "1-3",
                ["1-3-1"]
            ),
            AnswerDTO(
                "1-4",
                ["1-4-3", "1-4-4"]
            ),
            AnswerDTO(
                "1-5",
                ["1-5-1", "1-5-3"]
            )
        ]

        answers_dto = AnswersDTO(
            "1",
            answers
        )

        quiz_result_service = QuizResultService(
            self.quiz_dto,
            answers_dto
        )

        self.assertEqual(quiz_result_service.get_result(), 1.00)

    def test_failure_quiz_result(self):
        answers: List[AnswerDTO] = [
            AnswerDTO(
                "1-1",
                ["1-1-1"]
            ),
            AnswerDTO(
                "1-2",
                ["1-2-2"]
            ),
            AnswerDTO(
                "1-3",
                ["1-3-3"]
            ),
            AnswerDTO(
                "1-4",
                ["1-4-1", "1-4-4"]
            ),
            AnswerDTO(
                "1-5",
                ["1-5-2", "1-5-3"]
            )
        ]

        answers_dto = AnswersDTO(
            "1",
            answers
        )

        quiz_result_service = QuizResultService(
            self.quiz_dto,
            answers_dto
        )

        self.assertEqual(quiz_result_service.get_result(), 0.00)
