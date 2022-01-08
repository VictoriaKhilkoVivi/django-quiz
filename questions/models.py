from django.db import models


class Quiz(models.Model):
    title = models.CharField('Название', max_length=256)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.CharField('Название', max_length=256)
    quiz = models.ForeignKey(Quiz, verbose_name='Вопрос из теста',
                             on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='Номер вопроса в тесте')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.CharField('Название', max_length=256)
    is_correct = models.BooleanField('Правильность')
    question = models.ForeignKey(Question, verbose_name='Ответ к вопросу',
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.text
