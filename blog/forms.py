from django import forms
from .models import Autor, Post
from django.contrib.admin.widgets import AdminDateWidget
from datetime import date
from django.core.exceptions import ValidationError

class post_form (forms.Form):
    titulo = forms.CharField(label="Título", max_length=200)
    cuerpo = forms.CharField(label="Cuerpo", widget=forms.Textarea)
    fpublicado = forms.DateField(label='Fecha de publicación')
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), label="Autor")

class post_form_model (forms.ModelForm):
    fpublicado = forms.DateField(label='Fecha de publicación', 
                                #  input_formats=['%d/%m/%Y', '%Y-%m-%d'],
                                 widget=forms.DateInput(attrs={
                                    #  'class': 'form-control',

                                    #  'placeholder': 'dd/mm/aaaa',
                                     'type':'date'}))
    class Meta:
        model = Post
        fields = '__all__' #['titulo', 'autor', 'cuerpo', 'fpublicado']


    def clean_fpublicado(self):
        fpublicado = self.cleaned_data.get('fpublicado')
        if fpublicado and fpublicado > date.today():
            raise ValidationError("La fecha de publicación no puede ser mayor que la actual.")
        return fpublicado
    
class autor_form_model (forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'