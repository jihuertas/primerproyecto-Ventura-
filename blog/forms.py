from django import forms
from .models import Autor

class post_form (forms.Form):
    titulo = forms.CharField(label="Título", max_length=200)
    cuerpo = forms.CharField(label="Cuerpo", widget=forms.Textarea)
    fpublicado = forms.DateField(label='Fecha de publicación')
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), label="Autor")

class post_form_model (forms.ModelForm):
    