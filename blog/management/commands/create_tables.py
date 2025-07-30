from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Create database tables manually'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            # Create Event table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS blog_event (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title VARCHAR(200) NOT NULL,
                    description TEXT NOT NULL,
                    date DATETIME NOT NULL,
                    location VARCHAR(200) NOT NULL,
                    created_by_id INTEGER NOT NULL REFERENCES auth_user(id),
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL,
                    photo VARCHAR(100),
                    poster VARCHAR(100)
                )
            ''')
            
            # Create Comment table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS blog_comment (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_id INTEGER NOT NULL REFERENCES blog_event(id),
                    author_id INTEGER NOT NULL REFERENCES auth_user(id),
                    content TEXT NOT NULL,
                    created_at DATETIME NOT NULL
                )
            ''')
            
            # Create Question table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS blog_question (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title VARCHAR(200) NOT NULL,
                    content TEXT NOT NULL,
                    author_id INTEGER NOT NULL REFERENCES auth_user(id),
                    created_at DATETIME NOT NULL,
                    updated_at DATETIME NOT NULL
                )
            ''')
            
            # Create Answer table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS blog_answer (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question_id INTEGER NOT NULL REFERENCES blog_question(id),
                    author_id INTEGER NOT NULL REFERENCES auth_user(id),
                    content TEXT NOT NULL,
                    created_at DATETIME NOT NULL
                )
            ''')
            
        self.stdout.write(self.style.SUCCESS('Successfully created database tables'))
