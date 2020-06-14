# Standard library
from random import randint

# Django
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

# Local
from madusonovidiusscrumy.models import *
from .decorators import allowed_users


# def get_grading_parameters(request):
# response = ScrumyGoals.objects.filter(goal_name__exact='Learn Django')
# return HttpResponse(response)


@login_required
def move_goal(request, goal_id):
    """message = {'error': 'A record with that goal id does not exist'}
    try:
        obj = ScrumyGoals.objects.get(goal_id=goal_id)
    except Exception as e:
        return render(request, 'exception.html', message)
    else:
        return HttpResponse(obj.goal_name)"""
    user = request.user
    goal = get_object_or_404(ScrumyGoals, goal_id=goal_id)
    if User.objects.filter(username=user, groups__name='Developer').exists():
        if request.method == 'POST':
            form = MoveGoalForm(request.POST, instance=goal)
            if goal.user == request.user:
                if form.is_valid():
                    if GoalStatus.objects.get(
                            status_name='Done Goal') != goal.goal_status:
                        form.save()
                        return redirect('madusonovidiusscrumy:home')
                    else:
                        messages.error(
                            request,
                            "Your group policy doesn't permit this operation"
                        )
            else:
                messages.error(request, "You cannot move this goal")
        else:
            form = MoveGoalForm(instance=goal)
        return render(request, 'movegoal.html',
                      {'form': form, 'post': goal})

    elif User.objects.filter(username=user,
                             groups__name='Quality Assurance').exists():
        if request.method == 'POST':
            form = MoveGoalForm(request.POST, instance=goal)
            if goal.user != request.user:
                if GoalStatus.objects.get(
                        status_name='Verify Goal') == goal.goal_status:
                    if form.is_valid():
                        if GoalStatus.objects.get(
                                status_name='Verify Goal') != goal.goal_status \
                                and GoalStatus.objects.get(
                                status_name='Done Goal') != goal.goal_status:
                            messages.error(request,
                                           'You cannot perform this operation')
                        else:
                            form.save()
                            return redirect('madusonovidiusscrumy:home')
                else:
                    messages.error(request, 'You can only move a verified goal for this user')
            elif goal.user == request.user:
                if form.is_valid():
                    if GoalStatus.objects.get(
                            status_name='Weekly Goal') == goal.goal_status:
                        messages.error(request,
                                       'You cannot perform this operation')
                    else:
                        form.save()
                        return redirect('madusonovidiusscrumy:home')
        else:
            form = MoveGoalForm(instance=goal)
        return render(request, 'movegoal.html',
                      {'form': form, 'post': goal})

    elif User.objects.filter(username=user, groups__name='Admin').exists():
        if request.method == 'POST':
            form = MoveGoalForm(request.POST, instance=goal)
            if form.is_valid():
                goal.save()
                return redirect('madusonovidiusscrumy:home')
        else:
            form = MoveGoalForm(instance=goal)
        return render(request, 'movegoal.html',
                      {'form': form, 'post': goal})

    elif User.objects.filter(username=user, groups__name='Owner').exists():
        if request.method == 'POST':
            form = MoveGoalForm(request.POST, instance=goal)
            if goal.user == request.user:
                if form.is_valid():
                    goal = form.save(commit=False)
                    goal.save()
                    return redirect('madusonovidiusscrumy:home')
            else:
                messages.info(request, 'You cannot perform this operation')
        else:
            form = MoveGoalForm(instance=goal)
        return render(request, 'movegoal.html',
                      {'form': form, 'post': goal})


@login_required
@allowed_users(allowed_roles=['Quality Assurance', 'Developer', 'Owner'])
def add_goal(request):
    user = request.user
    already_used = []
    number = randint(1000, 9999)
    form = CreateGoalForm()
    if number not in already_used:
        form = CreateGoalForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            if instance.user == request.user:
                instance.goal_status = get_object_or_404(GoalStatus,
                                                         status_name='Weekly Goal')
                instance.goal_id = number
                already_used.append(number)
                instance.save()
                return redirect('madusonovidiusscrumy:home')
            else:
                messages.info(request,
                              'You cannot create a goal for this user')
    return render(request, 'madusonovidiusscrumy/addgoal.html', {'form': form})


@login_required
def home(request):
    scrumygoals = ScrumyGoals.objects.all()
    user = User.objects.all()
    dictionary = {
        'users': user,
        'scrumygoals': scrumygoals
    }
    return render(request, 'home.html', dictionary)


def index(request):
    groups = Group.objects.get(name='Developer')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            groups.user_set.add(user)

            return redirect('madusonovidiusscrumy:welcome')

    else:
        form = SignupForm()

    return render(request, 'index.html', {'form': form})


def welcome(request):
    dictionary = {
        'welcome': 'Your account has been successfully created'
    }
    return render(request, 'welcome.html', dictionary)
