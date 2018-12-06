from django.contrib import admin
from .models import Leave, History, Calendar

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ["name", "id","employee_ID", "department", "designation", "type_of_leave", "from_date", "to_date", "reporting_manager", 
    "reason", "created", "last_modified",  "status" ]
    
    list_filter = ['department','type_of_leave']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return (qs.filter(reporting_manager=request.user.username))#or qs.filter(employee_ID=request.user.username))
    
    def get_readonly_fields(self, request, obj=None):     
        if obj and request.user.is_staff:
            readonly_fields = [f.name for f in self.opts.fields]
            readonly_fields.remove('status')
            readonly_fields.remove('reason_reject')      
        return readonly_fields

    radio_fields = {"status": admin.HORIZONTAL}

    class Media:
        js = ('http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js',
            'leavemanager/js/master.js')


@admin.register(History)
class History(admin.ModelAdmin):
    list_display = ['employee_ID', 'first_name', 'last_name',
    'earned_leave','casual_leave', 'sick_leave', 'paid_leave' ]

@admin.register(Calendar)
class Calendar(admin.ModelAdmin):
    list_display= ['date', 'occasion']