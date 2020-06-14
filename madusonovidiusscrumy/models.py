from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.forms import ModelForm, CharField, widgets, PasswordInput


# Create your models here.
class GoalStatus(models.Model):
    status_name = models.CharField(max_length=50)

    def __str__(self):
        return self.status_name


class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length=50)
    goal_id = models.IntegerField()
    created_by = models.CharField(max_length=50)
    moved_by = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.PROTECT,)
    user = models.ForeignKey(User,
                             related_name='created_by',
                             on_delete=models.PROTECT,)

    def __str__(self):
        return self.goal_name


class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    moved_from = models.CharField(max_length=50)
    moved_to = models.CharField(max_length=50)
    time_of_action = models.DateTimeField(timezone.now)
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by


class SignupForm(ModelForm):
    password = CharField(widget=PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


class CreateGoalForm(ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'user']
        permissions = (
            ("can_create_personal_weekly", "Create Personal Weekly Goal"),
        )



class MoveGoalForm(ModelForm):
    goal_name = CharField(disabled=True)
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'goal_status']




