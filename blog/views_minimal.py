from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Minimal views without database dependencies

def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def directory(request):
    return render(request, 'blog/directory.html')

def riverside_players(request):
    # Minimal context for template rendering without database
    context = {
        'events': [],
        'questions': [],
        'event_form': None,
        'question_form': None,
    }
    return render(request, 'blog/riverside_players.html', context)

# Authentication views
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')
