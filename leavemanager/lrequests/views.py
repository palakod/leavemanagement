from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LeaveRequestForm
from django.shortcuts import render_to_response
from .models import Leave, History, Calendar
from django.views.generic import DetailView

def leaveRequest(request):

    if request.method == "POST":
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave = form.save(commit = False)
            leave.user = request.user
            form.save()
        else:
            return HttpResponseRedirect("/error/")
        return HttpResponseRedirect("/thanks/")
    else:
        return auto_fill_form(request)
    
def get_data(request):
    data = Leave.objects.filter(employee_ID = request.user.username)
    count = History.objects.filter(employee_ID = request.user.username)
    return render(request, "status.html",{'data':data, 'count':count})

def calendar_data(request):
    holidays = Calendar.objects.order_by('date')
    return render(request, 'calendar.html', {'holidays':holidays})


def auto_fill_form(request):
    form = LeaveRequestForm(initial = dict(name = (request.user.first_name +" "+ request.user.last_name), employee_ID = request.user.username))
    context = dict(form=form)
    return render(request, "request_form.html", context)










    

    