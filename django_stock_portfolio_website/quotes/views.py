from django.shortcuts import render,redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm

# Create your views here.
def home(request):
	import requests
	import json

	if request.method == 'POST':
		ticker = request.POST['ticker']

		# pk_6d4d45f7690a4ca396852e93c3b05a67
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_your public key")
		
		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request,'home.html',{'api':api})

	else:
		return render(request,'home.html',{'ticker':"Enter a ticker symbol above..."})


def about(request):
	return render(request,'about.html',{})

def add_stock(request):
	import requests
	import json

	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, (form.cleaned_data['ticker']+" Stock Has Been Added"))
			return redirect('add_stock')
	else:
		ticker = Stock.objects.all()
		list=[]
		for item in ticker:

			api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(item) + "/quote?token=pk_6d4d45f7690a4ca396852e93c3b05a67")
			
			try:
				api = json.loads(api_request.content)
				list.append(api)
			except Exception as e:
				api = "Error..."

		return render(request,'add_stock.html',{'ticker':ticker,'list':list})
	
def delete(request, stock_id, flag):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, ("Stock Has Been Delete"))
	print("flag",flag)
	if flag == 1:
		return redirect('add_stock')
	else:
		return redirect('delete_stock')

def delete_stock(request):
	ticker = Stock.objects.all()
	return render(request,'delete_stock.html',{'ticker':ticker})