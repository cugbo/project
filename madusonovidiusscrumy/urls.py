#Django
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#Local
from . import views

app_name = 'madusonovidiusscrumy'

urlpatterns = [
    #path('', views.get_grading_parameters, name='get_grading_parameters'),
    path('movegoal/<int:goal_id>', views.move_goal, name='movegoal'),
    path('addgoal/', views.add_goal, name='addgoal'),
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('index/', views.index, name='index'),
    path('welcome', views.welcome, name='welcome')
]

urlpatterns += staticfiles_urlpatterns()

