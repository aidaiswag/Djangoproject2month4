from django import forms

class CreateCelebrityForm(forms.Form):
    name = forms.CharField()
    biography = forms.CharField()
    childhood = forms.CharField()
    image = forms.ImageField()
    career = forms.CharField()

    def clean(self):
        data = self.cleaned_data
        if data.get("name") == data.get("biography"):
            raise forms.ValidationError ("Name and boigraphy must be different!")
        return data