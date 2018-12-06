from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F

CHOICES = (('Earned Leave','Earned Leave'),('Casual Leave','Casual Leave'),('Sick Leave','Sick Leave'),('Paid Leave','Paid Leave'))
STATUS_CHOICES = (('0', 'Rejected'),('1', 'Accepted'),)
MANAGER_CHOICES = (('0001_manager', '0001_manager'),('0002_manager', '0002_manager'))
DEPARTMENT_CHOICES = (('Python','Python'), ('Javascripr','Javascript'))
DESIGNATION_CHOICES = (('Developer', 'Developer'), ('Designer','Designer'))

class Leave(models.Model):

    employee_ID = models.CharField(max_length = 20)
    name = models.CharField(max_length = 50)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null =True)
    department = models.CharField(max_length = 50, choices = DEPARTMENT_CHOICES)
    designation = models.CharField(max_length = 50, choices = DESIGNATION_CHOICES)
    type_of_leave = models.CharField(max_length = 15, choices = CHOICES)
    from_date = models.DateField()
    to_date = models.DateField()
    reporting_manager = models.CharField(max_length = 50, choices = MANAGER_CHOICES)
    reason = models.CharField(max_length= 180)
    status = models.CharField(max_length = 15, choices = STATUS_CHOICES)
    reason_reject = models.CharField(('reason for rejection'),max_length=50, default = '-') #blank=True)
    created = models.DateField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateField(auto_now=True, editable=False, null=False, blank=False)


    def __str__(self):
        return self.name

    @property
    def date_diff(self):
        return (self.to_date - self.from_date).days + 1
         

    class Meta:
        verbose_name = "Leaves Applied"
        verbose_name_plural = "Leaves Applied"
    
    def save(self, *args, **kwargs):
        super(Leave, self).save()
        if self.status == '1':
            if self.type_of_leave == 'Earned Leave':
                    history = History.objects.filter(employee_ID=self.employee_ID).update(
                earned_leave = F('earned_leave') - self.date_diff,  
            )
            elif self.type_of_leave == 'Casual Leave':
                    history = History.objects.filter(employee_ID=self.employee_ID).update(
                casual_leave = F('casual_leave') - self.date_diff,  
            )
            elif self.type_of_leave == 'Sick Leave':
                    history = History.objects.filter(employee_ID=self.employee_ID).update(
                sick_leave = F('sick_leave') - self.date_diff,  
            )
            elif self.type_of_leave == 'Paid Leave':
                    history = History.objects.filter(employee_ID=self.employee_ID).update(
                paid_leave = F('paid_leave') - self.date_diff,  
            )


   


class History(models.Model):

    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    employee_ID = models.CharField(max_length = 20)
    earned_leave = models.IntegerField()
    casual_leave = models.IntegerField()
    sick_leave = models.IntegerField()
    paid_leave =models.IntegerField()

    class Meta:
        verbose_name = "Employee's Leaves Eligibility"
        verbose_name_plural = "Employee's Leaves Eligibility"

class Calendar(models.Model):

    date = models.DateField()
    occasion = models.CharField(max_length = 20)