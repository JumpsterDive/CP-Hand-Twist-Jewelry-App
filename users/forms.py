from django import forms


class userRegistrationForm(forms.Form):

    firstName = forms.CharField(help_text="First Name")
    lastName = forms.CharField(help_text="Last Name")
    username = forms.CharField(help_text="username")
    email = forms.EmailField(help_text="email")
    password = forms.CharField(help_text="password",widget=forms.PasswordInput())
    Entry1 = forms.CharField(help_text='entry1')
    Entry2 = forms.CharField(help_text='entry2')
    Entry3 = forms.CharField(help_text='entry3')

#end class userRegistrationForm