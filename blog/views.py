from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Comment, Question, Answer
from .forms import EventForm, CommentForm, QuestionForm, AnswerForm

# Main views

def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def directory(request):
    return render(request, 'blog/directory.html')

def riverside_players(request):
    # Get events and questions from database
    events = Event.objects.all().order_by('-created_at')
    questions = Question.objects.all().order_by('-created_at')
    
    # Handle form submissions
    if request.method == 'POST':
        if 'event_form' in request.POST and request.user.is_authenticated:
            event_form = EventForm(request.POST, request.FILES)
            if event_form.is_valid():
                event = event_form.save(commit=False)
                event.created_by = request.user
                event.save()
                messages.success(request, 'Event created successfully!')
                return redirect('riverside_players')
        elif 'question_form' in request.POST and request.user.is_authenticated:
            question_form = QuestionForm(request.POST)
            if question_form.is_valid():
                question = question_form.save(commit=False)
                question.author = request.user
                question.save()
                messages.success(request, 'Question posted successfully!')
                return redirect('riverside_players')
    
    # Create fresh forms for GET requests
    event_form = EventForm()
    question_form = QuestionForm()
    
    context = {
        'events': events,
        'questions': questions,
        'event_form': event_form,
        'question_form': question_form,
    }
    return render(request, 'blog/riverside_players.html', context)

# CRUD Functions for Events
@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('riverside_players')
    else:
        form = EventForm(instance=event)
    return render(request, 'blog/edit_event.html', {'form': form, 'event': event})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('riverside_players')
    return render(request, 'blog/delete_event.html', {'event': event})

@login_required
def add_comment(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.event = event
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
    return redirect('riverside_players')

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    # Check if user owns the comment or is admin
    if request.user == comment.author or request.user.is_staff:
        if request.method == 'POST':
            comment.delete()
            messages.success(request, 'Comment deleted successfully!')
            return redirect('riverside_players')
        return render(request, 'blog/delete_comment.html', {'comment': comment})
    else:
        messages.error(request, 'You can only delete your own comments.')
        return redirect('riverside_players')

# CRUD Functions for Questions
@login_required
def edit_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question updated successfully!')
            return redirect('riverside_players')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'blog/edit_question.html', {'form': form, 'question': question})

@login_required
def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        question.delete()
        messages.success(request, 'Question deleted successfully!')
        return redirect('riverside_players')
    return render(request, 'blog/delete_question.html', {'question': question})

@login_required
def add_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            messages.success(request, 'Answer added successfully!')
    return redirect('riverside_players')

# Authentication views
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('directory')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'blog/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('directory')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, "You've left the stage!")
        return redirect('home')
    else:
        # Handle GET requests (direct access to logout URL)
        logout(request)
        messages.info(request, "You've left the stage!")
        return redirect('home')
