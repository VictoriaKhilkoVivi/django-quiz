from django import forms

from questions.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'text',
            'choices',
        ]

    choices = forms.ModelMultipleChoiceField(queryset=Question.choice_set, widget=forms.RadioSelect)
