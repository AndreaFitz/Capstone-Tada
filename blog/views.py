from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Comment, Question
from .forms import (
    EventForm, CommentForm, QuestionForm, AnswerForm, SocietySubmissionForm,
    ContactForm
)


# Main views


def index(request):
    return render(request, 'blog/index.html')


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Here you could save to database or send email
            # For now, we'll just show a success message
            messages.success(
                request,
                'Thanks! Your message has been sent successfully. '
                'We\'ll get back to you soon!'
            )
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'blog/contact.html', {'contact_form': form})


def directory(request):
    if request.method == 'POST' and request.user.is_authenticated:
        society_form = SocietySubmissionForm(request.POST)
        if society_form.is_valid():
            society = society_form.save(commit=False)
            society.submitted_by = request.user
            society.save()
            messages.success(
                request,
                'Thank you! Your society submission has been received '
                'and will be reviewed.'
            )
            return redirect('directory')
    else:
        society_form = SocietySubmissionForm()

    return render(request, 'blog/directory.html', {'society_form': society_form})


def riverside_players(request):
    # Get events and questions from database filtered by society
    events = Event.objects.filter(society='riverside_players').order_by('-created_at')
    questions = Question.objects.filter(society='riverside_players').order_by('-created_at')

    # Handle form submissions
    if request.method == 'POST':
        if 'event_form' in request.POST and request.user.is_authenticated:
            event_form = EventForm(request.POST, request.FILES)
            if event_form.is_valid():
                event = event_form.save(commit=False)
                event.created_by = request.user
                event.society = 'riverside_players'  # Set the society
                event.save()
                messages.success(request, 'Event created successfully!')
                return redirect('riverside_players')
        elif 'question_form' in request.POST and request.user.is_authenticated:
            question_form = QuestionForm(request.POST)
            if question_form.is_valid():
                question = question_form.save(commit=False)
                question.author = request.user
                question.society = 'riverside_players'  # Set the society
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


def metropolitan_drama(request):
    # Get events and questions from database filtered by society
    events = Event.objects.filter(society='metropolitan_drama').order_by('-created_at')
    questions = Question.objects.filter(society='metropolitan_drama').order_by('-created_at')

    # Handle form submissions
    if request.method == 'POST':
        if 'event_form' in request.POST and request.user.is_authenticated:
            event_form = EventForm(request.POST, request.FILES)
            if event_form.is_valid():
                event = event_form.save(commit=False)
                event.created_by = request.user
                event.society = 'metropolitan_drama'  # Set the society
                event.save()
                messages.success(request, 'Event created successfully!')
                return redirect('metropolitan_drama')
        elif 'question_form' in request.POST and request.user.is_authenticated:
            question_form = QuestionForm(request.POST)
            if question_form.is_valid():
                question = question_form.save(commit=False)
                question.author = request.user
                question.society = 'metropolitan_drama'  # Set the society
                question.save()
                messages.success(request, 'Question posted successfully!')
                return redirect('metropolitan_drama')

    # Create fresh forms for GET requests
    event_form = EventForm()
    question_form = QuestionForm()

    context = {
        'events': events,
        'questions': questions,
        'event_form': event_form,
        'question_form': question_form,
    }
    return render(request, 'blog/metropolitan_drama.html', context)


def experimental_theatre_lab(request):
    # Get events and questions from database filtered by society
    events = Event.objects.filter(society='experimental_theatre_lab').order_by('-created_at')
    questions = Question.objects.filter(society='experimental_theatre_lab').order_by('-created_at')

    # Handle form submissions
    if request.method == 'POST':
        if 'event_form' in request.POST and request.user.is_authenticated:
            event_form = EventForm(request.POST, request.FILES)
            if event_form.is_valid():
                event = event_form.save(commit=False)
                event.created_by = request.user
                event.society = 'experimental_theatre_lab'  # Set the society
                event.save()
                messages.success(request, 'Event created successfully!')
                return redirect('experimental_theatre_lab')
        elif 'question_form' in request.POST and request.user.is_authenticated:
            question_form = QuestionForm(request.POST)
            if question_form.is_valid():
                question = question_form.save(commit=False)
                question.author = request.user
                question.society = 'experimental_theatre_lab'  # Set the society
                question.save()
                messages.success(request, 'Question posted successfully!')
                return redirect('experimental_theatre_lab')

    # Create fresh forms for GET requests
    event_form = EventForm()
    question_form = QuestionForm()

    context = {
        'events': events,
        'questions': questions,
        'event_form': event_form,
        'question_form': question_form,
    }
    return render(request, 'blog/experimental_theatre_lab.html', context)


def cats_theatre(request):
    # Get events and questions from database filtered by society
    events = Event.objects.filter(society='cats_theatre').order_by('-created_at')
    questions = Question.objects.filter(society='cats_theatre').order_by('-created_at')

    # Handle form submissions
    if request.method == 'POST':
        if 'event_form' in request.POST and request.user.is_authenticated:
            event_form = EventForm(request.POST, request.FILES)
            if event_form.is_valid():
                event = event_form.save(commit=False)
                event.created_by = request.user
                event.society = 'cats_theatre'  # Set the society
                event.save()
                messages.success(request, 'Event created successfully!')
                return redirect('cats_theatre')
        elif 'question_form' in request.POST and request.user.is_authenticated:
            question_form = QuestionForm(request.POST)
            if question_form.is_valid():
                question = question_form.save(commit=False)
                question.author = request.user
                question.society = 'cats_theatre'  # Set the society
                question.save()
                messages.success(request, 'Question posted successfully!')
                return redirect('cats_theatre')

    # Create fresh forms for GET requests
    event_form = EventForm()
    question_form = QuestionForm()

    context = {
        'events': events,
        'questions': questions,
        'event_form': event_form,
        'question_form': question_form,
    }
    return render(request, 'blog/cats_theatre.html', context)


# CRUD Functions for Events


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect(event.society)  # Redirect to correct society page
    else:
        form = EventForm(instance=event)
    return render(request, 'blog/edit_event.html', {'form': form, 'event': event})


@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    if request.method == 'POST':
        event_society = event.society  # Get the society before deleting
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect(event_society)  # Redirect to correct society page
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
    
    # Redirect to the correct society page based on the event's society
    return redirect(event.society)


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment updated successfully!')
            return redirect(comment.event.society)
    else:
        form = CommentForm(instance=comment)
    
    return render(request, 'blog/edit_comment.html', {
        'form': form, 
        'comment': comment,
        'event': comment.event
    })


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.method == 'POST':
        event_society = comment.event.society  # Get the society before deleting
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
        return redirect(event_society)
    return render(request, 'blog/delete_comment.html', {'comment': comment})


# CRUD Functions for Questions


@login_required
def edit_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question updated successfully!')
            # Redirect based on the question's society
            return redirect(question.society)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'blog/edit_question.html', {
        'form': form, 'question': question
    })


@login_required
def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    
    if request.method == 'POST':
        # Store the society before deleting the question
        society = question.society
        question.delete()
        messages.success(request, 'Question deleted successfully!')
        # Redirect based on the question's society
        return redirect(society)
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
    
    # Redirect based on the question's society
    return redirect(question.society)


@login_required
def edit_answer(request, answer_id):
    from .models import Answer
    answer = get_object_or_404(Answer, id=answer_id)
    
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Answer updated successfully!')
            # Redirect based on the question's society
            return redirect(answer.question.society)
    else:
        form = AnswerForm(instance=answer)
    
    return render(request, 'blog/edit_answer.html', {
        'form': form, 
        'answer': answer,
        'question': answer.question
    })


@login_required
def delete_answer(request, answer_id):
    from .models import Answer
    answer = get_object_or_404(Answer, id=answer_id)
    
    if request.method == 'POST':
        question_society = answer.question.society  # Get the society before deleting
        answer.delete()
        messages.success(request, 'Answer deleted successfully!')
        # Redirect based on the question's society
        return redirect(question_society)
    return render(request, 'blog/delete_answer.html', {'answer': answer})


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
            form.save()
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
