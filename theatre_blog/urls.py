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
from blog.views import (
    index, about, directory, riverside_players, register_view, login_view, logout_view
)

urlpatterns = [
    path('', index, name='home'),  # Add root URL
    path('about/', about, name='about'),  # About page
    path('directory/', directory, name='directory'),  # Directory page
    path('society/riverside-players/', riverside_players, name='riverside_players'),  # Riverside Players page
    path('register/', register_view, name='register'),  # Registration page
    path('login/', login_view, name='login'),  # Login page
    path('logout/', logout_view, name='logout'),  # Logout action
    path('admin/', admin.site.urls),
    path('blog/', index, name='my_blog'),
]
