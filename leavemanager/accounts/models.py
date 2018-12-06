from django.contrib import auth
from django.db import models
from lrequests.models import History


class User(auth.models.User, auth.models.PermissionsMixin):
    
    def __str__(self):
        return "@{}".format(self.username)
    
    class Meta:
        verbose_name = "Employee Details"
        verbose_name_plural = "Employee Details"
    
    # def save(self, *args, **kwargs):
    #     super(User, self).save()
    #     print('started')
    #     history = History.objects.create(
    #         employee_ID = self.username,
    #         first_name = self.first_name,
    #         last_name = self.last_name,
    #         earned_leave = 10,
    #         casual_leave = 10,
    #         sick_leave = 10,
    #         paid_leave = 10,

    #     )
        
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from lrequests.models import History

def send_data(sender, instance, created, **kwargs):
    if created:
        history = History()
        history.employee_ID = instance.username
        history.first_name = instance.first_name
        history.last_name = instance.last_name
        history.earned_leave = 10
        history.casual_leave = 10
        history.sick_leave = 10
        history.paid_leave = 10
        history.save()
        print('data sent') 

post_save.connect(receiver = send_data, sender= User)
