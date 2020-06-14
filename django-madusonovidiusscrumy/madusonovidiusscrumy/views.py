# Standard library
from random import randint

# Django
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

# Local
from madusonovidiusscrumy.models import *

# def get_grading_parameters(request):
# response = ScrumyGoals.objects.filter(goal_name__exact='Learn Django')
# return HttpResponse(response)


def move_goal(request, goal_id):
    message = {'error': 'A record with that goal id does not exist'}
    try:
        obj = ScrumyGoals.objects.get(id=goal_id)
    except Exception as e:
        return render(request, 'madusonovidiusscrumy/exception.html', message)
    else:
        return HttpResponse(obj.goal_name)


def add_goal(request):
    already_used = []
    number = randint(1000, 9999)
    if number not in already_used:
        addgoal = ScrumyGoals.objects.create(goal_name='Keep Learning Django',
                                             goal_id=number,
                                             created_by='Louis',
                                             moved_by='Louis', owner='Louis',
                                             goal_status=GoalStatus.objects.get
                                             (status_name='Weekly Goal'),
                                             user=User.objects.get(
                                                 username='Louis Oma')
                                             )
        already_used.append(number)
        return HttpResponse(addgoal)


def home(request):
    scrumygoals = ScrumyGoals.objects.all()
    dictionary = {
        'scrumygoals': scrumygoals

    }
    return render(request, 'madusonovidiusscrumy/home.html', dictionary)

# Create your views here.
