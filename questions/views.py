from django.shortcuts import render
from django.shortcuts import redirect

from questions.models import Quiz, Question, Choice
from quiz.dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List
from quiz.services import QuizResultService


def index(request):
    quizzes = Quiz.objects.all()
    ctx = {
        'quizzes': quizzes,
    }
    return render(request, 'questions/index.html', ctx)


def quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    question = Question.objects.filter(quiz=id)
    id_q = question[0].id
    ctx = {
        'quiz': quiz,
        'id_q': id_q,
    }
    return render(request, 'questions/quiz.html', ctx)


def question(request, id_quiz, number_question):
    quiz = Quiz.objects.get(id=id_quiz)
    questions = Question.objects.filter(quiz=id_quiz)
    question = questions[number_question - 1]
    choices = Choice.objects.filter(question=question.id)
    finish = number_question == len(Question.objects.filter(quiz=id_quiz))

    if request.method == 'POST':
        request.session['quiz'] = id_quiz
        request.session[question.number] = []
        for k, v in request.POST.items():
            if k.isnumeric():
                request.session[question.number].append(k)
        if finish:
            return redirect('result')
        return redirect('question', id_quiz, number_question + 1)

    ctx = {
        'quiz': quiz,
        'question': question,
        'choices': choices,
        'number_question': number_question,
        'next': number_question + 1,
        'finish': finish,
    }

    return render(request, 'questions/question.html', ctx)


def result(request):
    quiz = request.session['quiz']
    quiz_db = Quiz.objects.get(id=quiz)
    questions_db = Question.objects.filter(quiz=quiz)
    questions: List[QuestionDTO] = []
    for question_db in questions_db:
        choices = Choice.objects.filter(question=question_db.id)
        choices_list = list(choices)
        options: List[ChoiceDTO] = []
        for choice in choices:
            option = ChoiceDTO('{}-{}-{}'.format(quiz, question_db.number, choices_list.index(choice)+1),
                               choice.text, choice.is_correct)
            options.append(option)

        questions.append(QuestionDTO('{}-{}'.format(quiz, question_db.number), question_db.text, options))

    quiz_dto = QuizDTO(
        quiz,
        quiz_db.title,
        questions
    )

    answers: List[AnswerDTO] = []
    for k, v in request.session.items():
        if k.isnumeric():
            choices = []
            for index_choice in range(len(v)):
                choices.append('{}-{}-{}'.format(quiz, k, v[index_choice]))
            answers.append(AnswerDTO(
                '{}-{}'.format(quiz, k),
                choices
            ))

    answers_dto = AnswersDTO(
        str(quiz),
        answers
    )

    quiz_result_service = QuizResultService(
        quiz_dto,
        answers_dto
    ).get_result()

    ctx = {
        'quiz_result_service': quiz_result_service,
    }

    return render(request, 'questions/result.html', ctx)
