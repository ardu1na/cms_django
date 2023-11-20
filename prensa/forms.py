from django import forms
from prensa.models import Articulo

class ArticuloAdminForm(forms.ModelForm):
    texto= forms.CharField(widget=forms.Textarea(attrs={'id':"richtext_field"}))
    class Meta:
        model = Articulo
        fields = '__all__'
        






    """    
## para la implementación de la libreria django-tinymice comentada en settings.py

from django import forms 
from tinymce import TinyMCE
from prensa.models import Articulo 


class TinyMCEWidget(TinyMCE): 
	def use_required_attribute(self, *args): 
		return False


class PostForm(forms.ModelForm): 
	texto = forms.CharField( 
		widget=TinyMCEWidget( 
			attrs={'required': False, 'cols': 90, 'rows': 30} 
		) 
	) 
	class Meta: 
		model = Articulo 
		fields = '__all__'
"""