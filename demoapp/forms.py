from django import forms
from .models import Logger, Registration


class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    email = forms.EmailField(label='enter your email')
    reservation_date = forms.DateField(
        widget=forms.NumberInput(attrs={'type': 'date'}))


class ApplicationForm(forms.Form):
    name = forms.CharField(label='Name of Applicant',
                           max_length=100, help_text="Enter full Name")
    address = forms.CharField(label="Address", max_length=100)
    post = (('Manager', 'Manager'), ('Cashier', 'Cashier',
            'Cashier'), ('Operator', 'Operator'))
    fields = forms.ChoiceField(choices=post)

# #using forms
# class InputForm(forms.Form):
#     SHIFTS  = (
#                ('1',"Morning"),
#                ("2", "Afternoon"),
#                ("3", "Evening"),
#                )
#     first_name = forms.CharField(max_length=200,)
#     last_name = forms.CharField(max_length=100)

#     time_log = forms.TimeField(required= False, help_text='enter exact time')
# We use ModelForm to get the same attributes from our models and inturn use it to create the form


class LogForm(forms.ModelForm):
    # here we write the model the form should inherit from
    class Meta:
        model = Logger
        fields = '__all__'  # it inherits all the fields in the Logger model


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'