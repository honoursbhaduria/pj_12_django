from django import forms 

class Url(forms.Form):
    url = forms.CharField(label="URL")  #input field for the origin URL

