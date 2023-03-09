from django import forms
from django.contrib.auth.models import User

class userRegistrationForm(forms.Form):

    firstName = forms.CharField(help_text="First Name")
    lastName = forms.CharField(help_text="Last Name")
    username = forms.CharField(help_text="username")
    email = forms.EmailField(help_text="email")
    password = forms.CharField(help_text="password")
    Entry1 = forms.CharField(help_text='entry1')
    Entry2 = forms.CharField(help_text='entry2')
    Entry3 = forms.CharField(help_text='entry3')

    def userModelObjectSave(self):
        first_name = self.firstName 
        last_name = self.lastName
        username = self.username
        email = self.email
        password = self.password
        user = User.objects.create_user(username,
                                        email,
                                        password,
                                        first_name=first_name,
                                        last_name=last_name)
        user.save()

#end class userRegistrationForm