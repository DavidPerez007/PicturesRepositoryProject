from django import forms
from .utils import validate_image_size, validate_image_type


class postForm(forms.Form):
    image = forms.ImageField(required=True, validators=[validate_image_size, validate_image_type])
    image_name = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 30}))

