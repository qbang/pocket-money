from django import forms
from .models import Family

class UploadFileForm(forms.Form):
    class Meta:
        model = Family
        file = ('tphoto', 'gphoto')

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['file'].required = False