from django.forms import ModelForm, Textarea, DateInput
from lrequests.models import Leave, History
from django import forms
# from django.utils import timezone

class LeaveRequestForm(ModelForm):

    class Meta:
        fields = ("name", "employee_ID" ,"department", "designation", "type_of_leave", "from_date", "to_date", "reporting_manager", "reason")
        model = Leave

        widgets =  {
            'name': Textarea(attrs = {'cols' : 20, 'rows': 1}),
            'employee_ID' : Textarea(attrs = {'cols' : 20, 'rows': 1}),
            'from_date' : DateInput(attrs={'class': 'datepicker'}),
            'to_date' : DateInput(attrs={'class': 'datepicker'}),
            'reason_reject' : forms.HiddenInput()

        }
    
    def __init__(self, *args, **kwargs):
         super(LeaveRequestForm, self).__init__(*args, **kwargs)
         self.fields['name'].widget.attrs['readonly'] = True
         self.fields['employee_ID'].widget.attrs['readonly'] = True
         self.fields['from_date'].widget.attrs['placeholder'] = 'mm/dd/yy'
         self.fields['to_date'].widget.attrs['placeholder'] = 'mm/dd/yy'
         self.fields['reporting_manager'].widget.attrs['placeholder'] = '000X_manager'

    def clean(self):

        cleaned_data = super().clean()
        to_date = cleaned_data.get("to_date")
        from_date = cleaned_data.get("from_date")

        if from_date < to_date:
            pass
        else:
            raise forms.ValidationError(
                "From Date should be lesser than To Date "
            )

class HistoryForm(ModelForm):
    class Meta:
        model = History
        exclude = ('name',)