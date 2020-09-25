from django import forms
from . models import status

class StatusForm(forms.Form):
    gender=forms.CharField(max_length=6)
    age=forms.IntegerField()
    openness=forms.IntegerField()
    neuroticism=forms.IntegerField()
    conscientiousness=forms.IntegerField()
    agreeableness=forms.IntegerField()
    extraversion=forms.IntegerField()

'''
class MyForm(ModelForm):
	class Meta:
		model=status
		fields = '__all__'
'''	