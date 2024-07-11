# quiz/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('start/', views.start_quiz, name='start_quiz'),
    path('quiz/', views.quiz, name='quiz'),
    # path('answer/', views.answer, name='answer'),
    path('results/', views.results, name='results'),
    path('score/create/', views.create_score),
    path('countries-flags/', views.get_countries_and_flags, name='countries-flags'),
]
