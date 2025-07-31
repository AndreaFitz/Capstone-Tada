"""
URL configuration for theatre_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import (
    index, about, directory, riverside_players, metropolitan_drama,
    experimental_theatre_lab, register_view, login_view, logout_view,
    edit_event, delete_event, add_comment, delete_comment, add_answer,
    edit_question, delete_question, contact
)

urlpatterns = [
    path('', index, name='home'),  # Add root URL
    path('about/', about, name='about'),  # About page
    path('directory/', directory, name='directory'),  # Directory page
    path('contact/', contact, name='contact'),  # Contact page
    path('society/riverside-players/', riverside_players,
         name='riverside_players'),  # Riverside Players page
    path('society/metropolitan-drama/', metropolitan_drama,
         name='metropolitan_drama'),  # Metropolitan Drama Society page
    path('society/experimental-theatre-lab/', experimental_theatre_lab,
         name='experimental_theatre_lab'),  # Experimental Theatre Lab page
    path('event/edit/<int:event_id>/', edit_event,
         name='edit_event'),  # Edit event
    path('event/delete/<int:event_id>/', delete_event,
         name='delete_event'),  # Delete event
    path('event/<int:event_id>/comment/', add_comment,
         name='add_comment'),  # Add comment
    path('comment/delete/<int:comment_id>/', delete_comment,
         name='delete_comment'),  # Delete comment
    path('question/<int:question_id>/answer/', add_answer,
         name='add_answer'),  # Add answer
    path('question/edit/<int:question_id>/', edit_question,
         name='edit_question'),  # Edit question
    path('question/delete/<int:question_id>/', delete_question,
         name='delete_question'),  # Delete question
    path('register/', register_view, name='register'),  # Registration page
    path('login/', login_view, name='login'),  # Login page
    path('logout/', logout_view, name='logout'),  # Logout action
    path('admin/', admin.site.urls),
    path('blog/', index, name='my_blog'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
