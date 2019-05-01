import urllib
from django import forms

class SearchForm(forms.Form):
    search = forms.CharField

    def as_url_args(self):
        return urllib.urlencode(self.cleaned_data)