from django import forms


class PokemonForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=20)
    nivel = forms.IntegerField()
    

class EntrenadorForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    cantidad_de_medallas = forms.IntegerField()
    region = forms.CharField(max_length=20)


class HabilidadForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=20)
    


