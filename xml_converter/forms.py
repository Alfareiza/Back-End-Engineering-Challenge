from django import forms
from django.core.validators import FileExtensionValidator


class XmlForm(forms.Form):
    #  Option 1
    # file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['xml'])])
    #  Option 2
    file = forms.FileField()
