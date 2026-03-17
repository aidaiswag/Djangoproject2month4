from django import forms
from celebrities.models import Category, Professions

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



class SearchForm(forms.Form):
    career_celebrity = [("career1", "succesful"), ("career2", "failed")]
    example_choice = [("example1", "smth"),("example2","noth")]
    search = forms.CharField(required=False)        
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False) 
    career = forms.ChoiceField(choices=career_celebrity, required=False)
    professions = forms.ModelMultipleChoiceField(queryset=Professions.objects.all(), required=False)
    example = forms.MultipleChoiceField(choices=example_choice, required=False)
