from django import forms

class UploadResumeForm(forms.Form):
    resume = forms.FileField(label="Upload your Resume in pdf format", help_text="max size 42MB")
