from django.shortcuts import render, redirect
from .models import Question
import random
# Create your views here.

def start_Quiz(request):
    if 'quiz_data' not in request.session:
        request.session['quiz_data'] = {'total': 0, 'correct': 0, 'incorrect': 0}

    # Get all questions or a random selection
    questions = Question.objects.all()

    return render(request, 'quiz/start_quiz.html', {'questions': questions})

def submit_answer(request):
    if request.method == 'POST':
        quiz_data = request.session.get('quiz_data', {'total': 0, 'correct': 0, 'incorrect': 0})

        #

        # Loop through each question and check the selected answer
        for question in Question.objects.all():
            selected_option = request.POST.get(f'answers[{question.id}]') # Get the selected option for the question

            if selected_option:
                if selected_option == str(question.correct_option):
                    quiz_data['correct'] += 1
                else:
                    quiz_data['incorrect'] += 1

                quiz_data['total'] += 1

        # Update session data
        request.session['quiz_data'] = quiz_data

        return redirect('quiz_summary')



def quiz_summary(request):
    quiz_data = request.session.get('quiz_data' , {'total': 0, 'correct': 0, 'incorrect': 0})   
    return render(request, 'quiz/summary.html', quiz_data) 



