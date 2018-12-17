from django import forms

from .models import VintageMac, Nike, Parking, Milk, Money

class VintageMacForm(forms.ModelForm):
	class Meta:
		model = VintageMac
		fields = ('price',)

class NikeForm(forms.ModelForm):
	class Meta:
		model = Nike
		fields = ('price',)

class ParkingForm(forms.ModelForm):
	class Meta:
		model = Parking
		fields = ('price',)

class MilkForm(forms.ModelForm):
	class Meta:
		model = Milk
		fields = ('price',)

class MoneyForm(forms.ModelForm):
	class Meta:
		model = Money
		fields = ('price',)