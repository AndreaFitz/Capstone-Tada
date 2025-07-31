from django import forms
from .models import Event, Comment, Question, Answer, SocietySubmission

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'photo', 'poster']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Event title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Event description'
            }),
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Event location'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'poster': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Add a comment...'
            }),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Question title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Your question...'
            }),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Your answer...'
            }),
        }

class SocietySubmissionForm(forms.ModelForm):
    class Meta:
        model = SocietySubmission
        fields = ['name', 'location', 'email']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of your theatre society'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Location/Address of your society'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Contact email'
            }),
        }