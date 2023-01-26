from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=25, label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=25, label='Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    role = forms.CharField(max_length=50, label='Role', widget=forms.TextInput(attrs={'class':'form-control','data-bs-toggle': 'tooltip', 'data-bs-placement': 'right', 'title': "If you don't have a role at a university, put 'hobbyist' or 'independant scholar'"}))
    institution = forms.CharField(max_length=50, label='Institution (Optional; leave blank if not associated with a university)', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.role = self.cleaned_data['role']
        user.institution = self.cleaned_data['institution']
        user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = ''
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = ''