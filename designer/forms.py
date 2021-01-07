from django import forms

class FrequencyForm(forms.Form):
	minfx = forms.DecimalField(label='minfx', min_value = 0, max_value = 1000000)
	maxfx = forms.DecimalField(label='maxfx', min_value = 0, max_value = 1000000)