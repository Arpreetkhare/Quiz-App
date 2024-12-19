from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_Quiz, name='start_quiz'),
    path('submit/', views.submit_answer, name='submit_answer'),
    path('summary/', views.quiz_summary, name='quiz_summary'),
]
