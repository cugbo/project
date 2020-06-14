# Django
from django.urls import path

# Local
from websocket import views

app_name = 'websocket'

urlpatterns = [
    path('test/', views.test, name='test'),
    path('disconnect/', views.disconnect, name='disconnect'),
    path('send_message/', views.send_message, name='send_message'),
    path('connect/', views.connect, name='connect'),
    path('recent_messages/', views.recent_messages, name='recent_messages')
]
