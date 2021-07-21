from django import forms
from .models import Question, Choice, Code
from django_ace import AceWidget


class QuestionForm(forms.ModelForm):
    question_text = forms.CharField()
    pub_date = forms.DateTimeField()

    class Meta:
        model = Question
        fields = '__all__'


class ChoiceForm(forms.ModelForm):
    question = forms.ChoiceField()
    choice_text = forms.TextInput()
    votes = forms.IntegerField()

    class Meta:
        model = Choice
        fields = '__all__'


class CodeForm(forms.ModelForm):
    code = forms.CharField(widget=AceWidget(
        mode='xml',  # try for example "python"
        theme='monokai',  # try for example "twilight" "monokai" "sublime"
        wordwrap=False,
        width="1000px",
        height="500px",
        minlines=None,
        maxlines=None,
        showprintmargin=True,
        showinvisibles=False,
        usesofttabs=True,
        tabsize=2,
        fontsize=16,
        toolbar=True,
        readonly=False,
        showgutter=True,  # To hide/show line numbers
        behaviours=True,  # To disable auto-append of quote when quotes are entered
    ))

    class Meta:
        model = Code
        fields = '__all__'
