from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url']

class ImageUploadForm(forms.Form):
    title = forms.CharField(max_length=200, label='Titre')
    image = forms.FileField(label='Choisir une image')

