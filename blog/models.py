from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='event_photos/', blank=True, null=True)
    poster = models.ImageField(upload_to='event_posters/', blank=True, null=True)
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f'Comment by {self.author.username} on {self.event.title}'

class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f'Answer by {self.author.username}'

class SocietySubmission(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=True, null=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-submitted_at']
    
    def __str__(self):
        return f'{self.name} - {self.location}'
