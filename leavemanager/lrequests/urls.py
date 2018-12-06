from django.urls import path, include
from . import views

app_name='lrequests'

urlpatterns = [
    path('lrequests/',views.leaveRequest, name = 'request'),
    path('status/', views.get_data, name = 'status'),
    path('calendar/', views.calendar_data, name = 'calendar')
 

    
]