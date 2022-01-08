from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.quiz, name='quiz'),
    path('<int:id_quiz>/<int:number_question>/', views.question, name='question'),
    path('result', views.result, name='result')
]
