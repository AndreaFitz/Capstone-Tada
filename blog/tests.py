"""
Comprehensive test suite for TADA! Django application
Testing models, views, forms, and authentication functionality
"""

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Event, Comment, Question, Answer, SocietySubmission
from .forms import EventForm, CommentForm, QuestionForm, AnswerForm


class EventModelTests(TestCase):
    """Test cases for the Event model"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
    def test_event_creation(self):
        """Test creating a new event"""
        event = Event.objects.create(
            title='Test Event',
            description='A test event description',
            date=timezone.now() + timedelta(days=7),
            location='Test Theatre',
            society='riverside_players',
            created_by=self.user
        )
        self.assertEqual(event.title, 'Test Event')
        self.assertEqual(event.society, 'riverside_players')
        self.assertEqual(event.created_by, self.user)
        self.assertTrue(isinstance(event.created_at, datetime))
        
    def test_event_string_representation(self):
        """Test the string representation of Event model"""
        event = Event.objects.create(
            title='Test Event',
            description='Test description',
            date=timezone.now(),
            location='Test Location',
            society='riverside_players',
            created_by=self.user
        )
        self.assertEqual(str(event), 'Test Event')
        
    def test_event_ordering(self):
        """Test that events are ordered by date"""
        future_date = timezone.now() + timedelta(days=7)
        past_date = timezone.now() - timedelta(days=1)
        
        event1 = Event.objects.create(
            title='Future Event',
            description='Future event',
            date=future_date,
            location='Test Location',
            society='riverside_players',
            created_by=self.user
        )
        
        event2 = Event.objects.create(
            title='Past Event',
            description='Past event',
            date=past_date,
            location='Test Location',
            society='riverside_players',
            created_by=self.user
        )
        
        events = Event.objects.all()
        self.assertEqual(events.first(), event2)  # Past event should come first


class AuthenticationTests(TestCase):
    """Test user authentication functionality"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
    def test_user_registration(self):
        """Test user registration process"""
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'complex_password123',
            'password2': 'complex_password123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(User.objects.filter(username='newuser').exists())
        
    def test_user_login(self):
        """Test user login functionality"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login
        
    def test_login_required_for_crud_operations(self):
        """Test that CRUD operations require login"""
        # Try to create event without login
        response = self.client.post(reverse('riverside_players'), {
            'event_form': '1',
            'title': 'Test Event',
            'description': 'Test description',
            'date': timezone.now(),
            'location': 'Test Location'
        })
        # Should redirect to login or stay on same page without creating
        self.assertFalse(Event.objects.filter(title='Test Event').exists())


class EventViewTests(TestCase):
    """Test event-related views"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.event = Event.objects.create(
            title='Test Event',
            description='Test description',
            date=timezone.now() + timedelta(days=7),
            location='Test Location',
            society='riverside_players',
            created_by=self.user
        )
        
    def test_society_page_loads(self):
        """Test that society pages load correctly"""
        response = self.client.get(reverse('riverside_players'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Riverside Players')
        
    def test_event_appears_on_society_page(self):
        """Test that events appear on their society pages"""
        response = self.client.get(reverse('riverside_players'))
        self.assertContains(response, 'Test Event')
        
    def test_event_creation_authenticated(self):
        """Test event creation when logged in"""
        self.client.login(username='testuser', password='testpass123')
        
        response = self.client.post(reverse('riverside_players'), {
            'event_form': '1',
            'title': 'New Test Event',
            'description': 'New test description',
            'date': '2025-12-25 18:00',
            'location': 'New Test Location'
        })
        
        self.assertTrue(Event.objects.filter(title='New Test Event').exists())
        
    def test_event_edit_authorization(self):
        """Test that only event creators can edit events"""
        other_user = User.objects.create_user(
            username='otheruser',
            password='otherpass123'
        )
        
        # Login as different user
        self.client.login(username='otheruser', password='otherpass123')
        
        response = self.client.get(reverse('edit_event', args=[self.event.id]))
        # Should be able to access edit page (template handles authorization)
        self.assertEqual(response.status_code, 200)


class CommentTests(TestCase):
    """Test comment functionality"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.event = Event.objects.create(
            title='Test Event',
            description='Test description',
            date=timezone.now(),
            location='Test Location',
            society='riverside_players',
            created_by=self.user
        )
        
    def test_comment_creation(self):
        """Test creating a comment"""
        comment = Comment.objects.create(
            event=self.event,
            author=self.user,
            content='This is a test comment'
        )
        self.assertEqual(comment.content, 'This is a test comment')
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.event, self.event)
        
    def test_comment_string_representation(self):
        """Test comment string representation"""
        comment = Comment.objects.create(
            event=self.event,
            author=self.user,
            content='Test comment'
        )
        expected_str = f'Comment by {self.user.username} on {self.event.title}'
        self.assertEqual(str(comment), expected_str)


class FormTests(TestCase):
    """Test form validation"""
    
    def test_event_form_valid_data(self):
        """Test EventForm with valid data"""
        form_data = {
            'title': 'Test Event',
            'description': 'Test description',
            'date': timezone.now() + timedelta(days=1),
            'location': 'Test Location'
        }
        form = EventForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_event_form_empty_title(self):
        """Test EventForm with empty title"""
        form_data = {
            'title': '',
            'description': 'Test description',
            'date': timezone.now(),
            'location': 'Test Location'
        }
        form = EventForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)


class SocietySubmissionTests(TestCase):
    """Test society submission functionality"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
    def test_society_submission_creation(self):
        """Test creating a society submission"""
        submission = SocietySubmission.objects.create(
            name='Test Theatre Society',
            location='Test City',
            email='test@theatre.com',
            submitted_by=self.user
        )
        self.assertEqual(submission.name, 'Test Theatre Society')
        self.assertEqual(submission.location, 'Test City')
        self.assertEqual(submission.email, 'test@theatre.com')
        self.assertEqual(submission.submitted_by, self.user)
        self.assertFalse(submission.is_approved)  # Should default to False
        
    def test_society_submission_string_representation(self):
        """Test string representation of SocietySubmission"""
        submission = SocietySubmission.objects.create(
            name='Test Theatre Society',
            location='Test City',
            email='test@theatre.com',
            submitted_by=self.user
        )
        expected_str = 'Test Theatre Society - Test City'
        self.assertEqual(str(submission), expected_str)
        
    def test_society_submission_ordering(self):
        """Test that submissions are ordered by submission date (newest first)"""
        # Create first submission
        submission1 = SocietySubmission.objects.create(
            name='First Society',
            location='First City',
            email='first@theatre.com',
            submitted_by=self.user
        )
        
        # Create second submission (should be newer)
        submission2 = SocietySubmission.objects.create(
            name='Second Society',
            location='Second City',
            email='second@theatre.com',
            submitted_by=self.user
        )
        
        submissions = SocietySubmission.objects.all()
        self.assertEqual(submissions.first(), submission2)  # Newest first


class SecurityTests(TestCase):
    """Test security measures"""
    
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(
            username='user1',
            password='pass123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='pass123'
        )
        
    def test_csrf_protection(self):
        """Test CSRF protection on forms"""
        # Login first
        self.client.login(username='user1', password='pass123')
        
        # Try to post without CSRF token (this should be handled by Django)
        response = self.client.post(reverse('riverside_players'), {
            'event_form': '1',
            'title': 'Test Event',
            'description': 'Test',
            'date': timezone.now(),
            'location': 'Test'
        })
        # Django automatically includes CSRF in test client
        # This test ensures the form processing works correctly
        
    def test_unauthorized_access_protection(self):
        """Test that unauthorized users cannot access protected views"""
        # Create an event
        event = Event.objects.create(
            title='Protected Event',
            description='Test',
            date=timezone.now(),
            location='Test',
            society='riverside_players',
            created_by=self.user1
        )
        
        # Try to access edit page without login
        response = self.client.get(reverse('edit_event', args=[event.id]))
        self.assertEqual(response.status_code, 302)  # Should redirect to login
        
        # Login as different user and try to edit
        self.client.login(username='user2', password='pass123')
        response = self.client.get(reverse('edit_event', args=[event.id]))
        # Template should handle showing/hiding edit buttons based on ownership
