from django.shortcuts import render
from .models import VintageMac, Nike, Parking, Milk, Money
from .forms import VintageMacForm, NikeForm, ParkingForm, MilkForm, MoneyForm
from django.db.models import Avg, Max, Min
from django.db.models import F, Func


# Create your views here.
class Round(Func):
	function = 'ROUND'
	template='%(function)s(%(expressions)s, 2)'

def home(request):
	form1_price_avg = VintageMac.objects.all().aggregate(price=Round(Avg('price'))).get('price', 'No Data Yet!')
	form1_price_max = VintageMac.objects.all().aggregate(Max('price')).get('price__max', 'No Data Yet!')
	form1_price_min = VintageMac.objects.all().aggregate(Min('price')).get('price__min', 'No Data Yet!')
	avg_dollar1 = '$'+str(form1_price_avg)
	min_dollar1 = '$'+str(form1_price_min)
	max_dollar1 = '$'+str(form1_price_max)
	if request.method == "POST":
		initial={'price': request.session.get('price', None)}
		form = VintageMacForm(request.POST, initial=initial)
		if form.is_valid():
			request.session['price'] = form.cleaned_data['price']
			form.save()
			form = VintageMacForm()
	else:
		form = VintageMacForm()

	user_submit = request.session['price']
	return render(request, 'hmwypapp/index.html', {'form': form, 'min_dollar1': min_dollar1, 'max_dollar1': max_dollar1, 'avg_dollar1': avg_dollar1, 'user_submit': user_submit})

def nike(request):
	form2_price_avg = Nike.objects.all().aggregate(price=Round(Avg('price'))).get('price', 'No Average Yet!')
	form2_price_max = Nike.objects.all().aggregate(Max('price')).get('price__max', 'No Data Yet!')
	form2_price_min = Nike.objects.all().aggregate(Min('price')).get('price__min', 'No Data Yet!')
	if request.method == "POST":
		form = NikeForm(request.POST)
		if form.is_valid():
			form.save()
			form = NikeForm()
	else:
		form = NikeForm()
	return render(request, 'hmwypapp/index.html', {'form': form, 'form2_price_min': form2_price_min, 'form2_price_max': form2_price_max, 'form2_price_avg': form2_price_avg})

def parking(request):
	form3_price_avg = Parking.objects.all().aggregate(price=Round(Avg('price'))).get('price', 'No Average Yet!')
	form3_price_max = Parking.objects.all().aggregate(Max('price')).get('price__max', 'No Data Yet!')
	form3_price_min = Parking.objects.all().aggregate(Min('price')).get('price__min', 'No Data Yet!')
	if request.method == "POST":
		form = ParkingForm(request.POST)
		if form.is_valid():
			form.save()
			form = ParkingForm()
	else:
		form = ParkingForm()
	return render(request, 'hmwypapp/index.html', {'form': form, 'form3_price_min': form3_price_min, 'form3_price_max': form3_price_max, 'form3_price_avg': form3_price_avg})

def milk(request):
	form4_price_avg = Milk.objects.all().aggregate(price=Round(Avg('price'))).get('price', 'No Average Yet!')
	form4_price_max = Milk.objects.all().aggregate(Max('price')).get('price__max', 'No Data Yet!')
	form4_price_min = Milk.objects.all().aggregate(Min('price')).get('price__min', 'No Data Yet!')
	if request.method == "POST":
		form = MilkForm(request.POST)
		if form.is_valid():
			form.save()
			form = MilkForm()
	else:
		form = MilkForm()
	return render(request, 'hmwypapp/index.html', {'form': form, 'form4_price_min': form4_price_min, 'form4_price_max': form4_price_max, 'form4_price_avg': form4_price_avg})

def money(request):
	form5_price_avg = Money.objects.all().aggregate(price=Round(Avg('price'))).get('price', 'No Average Yet!')
	form5_price_max = Money.objects.all().aggregate(Max('price')).get('price__max', 'No Data Yet!')
	form5_price_min = Money.objects.all().aggregate(Min('price')).get('price__min', 'No Data Yet!')
	if request.method == "POST":
		form = MoneyForm(request.POST)
		if form.is_valid():
			form.save()
			form = MoneyForm()
	else:
		form = MoneyForm()
	return render(request, 'hmwypapp/index.html', {'form': form, 'form5_price_min': form5_price_min, 'form5_price_max': form5_price_max, 'form5_price_avg': form5_price_avg})