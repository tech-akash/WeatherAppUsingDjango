from django import forms
from .models import City

class Addcity(forms.ModelForm):
    class Meta:
        model=City
        fields=['cityName']
        





# class Addcity(forms.Form):
#     citytoadd=forms.CharField(max_length=200,help_text="Enter the city name",label="cityname")
#     def return_clean_data(self):
#         data=self.cleaned_data['citytoadd']
#         return data