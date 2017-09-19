from django import forms
from .models import Document

''' Original form
class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length = 50)
    file = forms.FileField()
'''

class DocumentForm(forms.ModelForm):
        class Meta:
                model = Document
                fields = ('document', )



