from django import forms


Choice = (
    ('parked','PARKED'),
    ('unparked', 'UNPARKED'),
    ('finished','FINISHED'),
    )



class LengthException(Exception):
    pass
class ContactForm(forms.Form):
    task_name = forms.CharField(required=True,max_length=30)
    task_description = forms.EmailField(required=True)
    task_status = forms.CharField(max_length=15, choices=Choice, default='green')
    def clean_name(self):
        data = self.cleaned_data['task_name']
        if len(data)<=3:
            raise forms.ValidationError("name the correct task")
        return data
    def clean_email(self):
        data = self.cleaned_data['task_description']
        if not data.endswith['.com']:
            raise forms.ValidationError('must be parked')
        return data
    def clean_city(self):
        data = self.cleaned_data['task_status']
        if data == 'NONE':
            raise forms.ValidationError("choose the status")
        return data
