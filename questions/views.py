from django.shortcuts import render

from questions.models import Quiz, Question, Choice


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
    question = questions[number_question-1]
    choices = Choice.objects.filter(question=question.id)
    finish = True if number_question == len(Question.objects.filter(quiz=id_quiz)) else False
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
    return render(request, 'questions/result.html')
