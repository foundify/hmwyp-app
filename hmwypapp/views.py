from django.shortcuts import render
from .models import VintageMac, Nike, Parking, Milk, Money
from .forms import VintageMacForm, NikeForm, ParkingForm, MilkForm, MoneyForm
from django.db.models import Avg, Max, Min


# Create your views here.
def home(request):
	price_avg = VintageMac.objects.all().aggregate(Avg('price'))
	price_max = VintageMac.objects.all().aggregate(Max('price'))
	price_min = VintageMac.objects.all().aggregate(Min('price'))
	if request.method == "POST":
		form = VintageMacForm(request.POST)
		if form.is_valid():
			form.save()
			form = VintageMacForm()
	else:
		form = VintageMacForm()
	return render(request, 'hmwypapp/index.html', {'form': form})

def nike(request):
	if request.method == "POST":
		form = NikeForm(request.POST)
		if form.is_valid():
			form.save()
			form = NikeForm()
	else:
		form = NikeForm()
	return render(request, 'hmwypapp/index.html', {'form': form})

def parking(request):
	if request.method == "POST":
		form = ParkingForm(request.POST)
		if form.is_valid():
			form.save()
			form = ParkingForm()
	else:
		form = ParkingForm()
	return render(request, 'hmwypapp/index.html', {'form': form})

def milk(request):
	if request.method == "POST":
		form = MilkForm(request.POST)
		if form.is_valid():
			form.save()
			form = MilkForm()
	else:
		form = MilkForm()
	return render(request, 'hmwypapp/index.html', {'form': form})

def money(request):
	if request.method == "POST":
		form = MoneyForm(request.POST)
		if form.is_valid():
			form.save()
			form = MoneyForm()
	else:
		form = MoneyForm()
	return render(request, 'hmwypapp/index.html', {'form': form})