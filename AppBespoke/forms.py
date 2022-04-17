from django import forms


class PartesFormulario(forms.Form):
    #especificar los campos
    nombre = forms.CharField(max_length=40)
    stock = forms.IntegerField()
    pedido= forms.BooleanField()
    
