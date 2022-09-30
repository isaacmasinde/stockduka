from django.shortcuts import render,redirect
from django.http import *
from index.models import *
from django.db.models import *
from django.contrib.auth.models import *
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import random
from datetime import datetime
import requests
@login_required(login_url='/login/')
def profile(request):
	if request.method=='POST':
		fname=request.POST.get('fname')
		lname=request.POST.get('lname')
		contact=request.POST.get('contact')
		bizloc=request.POST.get('bizloc')
		bizname=request.POST.get('bizname')
		user=User.objects.get(username=request.user.username)
		user.username=contact
		user.last_name=lname
		user.first_name=fname
		user.save()
		userobj=Userdetail.objects.get(Contact=request.user.username)
		userobj.Firstname=fname
		userobj.Secondname=lname
		userobj.Contact=contact
		biz=Biz.objects.get(Owner=userobj)
		biz.Location=bizloc
		biz.Name=bizname
		biz.save()
		userobj.save()
		login(request, user)
	username=request.user.username
	user=Userdetail.objects.get(Contact=username)
	biz=Biz.objects.get(Owner=user)
	if request.session.get('has_cart', False):
		cart=Cart.objects.filter(Session=request.session['cartid']).last()
		count=Order.objects.filter(Cart=cart)
		count=count.aggregate(Sum('Quantity'))
		count=count['Quantity__sum']
	else:
		count=0
	context={'user':user, 'biz':biz, 'count':count}
	templatename='user/profile.html'
	return render(request, templatename, context)

def addon(request):
	name=request.GET.get("name")
	quantity=request.GET.get("quantity")
	price = Brand.objects.get(Name=name).Sold
	data={}
	if request.session.get('has_cart', False):
		cart=Cart.objects.filter(Session=request.session['cartid']).last()
		brand=Brand.objects.get(Name=name)
		if Order.objects.filter(Cart=cart, Brand=brand).exists():
			order=Order.objects.get(Cart=cart, Brand=brand)
			bill=int(quantity)*price
			order.Bill=order.Bill+bill
			order.Quantity=order.Quantity+int(quantity)
			quantity=order.Quantity
			order.save()
			cart=Cart.objects.get(Session=request.session['cartid'])
			count=Order.objects.filter(Cart=cart)
			count=count.aggregate(Sum('Quantity'))
			count=count['Quantity__sum']
			brand=Brand.objects.get(Name=name)
			maxim=brand.Quantity
			if maxim <=0:
				brand.Instock=False
			brand.save()
			total=Order.objects.filter(Cart=cart).aggregate(Sum('Bill'))
			total=total["Bill__sum"]
			cart.Total=total
			cart.save()
			data = {
			'quantity':quantity,
			'maxim':maxim,
			'count': count,
			}
			return JsonResponse(data)
		order=Order()
		order.Cart=Cart.objects.get(Session=request.session['cartid'])
		order.Brand=Brand.objects.get(Name=name)
		order.Bill=int(quantity)*price
		order.Quantity=int(quantity)
		if request.user.is_authenticated:
			order.User=Userdetail.objects.get(Contact=request.user.username)
		order.Wakati=datetime.now()
		order.Status='uncomplete'
		order.save()
		cart=Cart.objects.get(Session=request.session['cartid'])
		count=Order.objects.filter(Cart=cart).count()
		brand=Brand.objects.get(Name=name)
		maxim=brand.Quantity
		if maxim <= 0:
			brand.Instock=False
		brand.save()
		total=Order.objects.filter(Cart=cart).aggregate(Sum('Bill'))
		total=total["Bill__sum"]
		cart.Total=total
		cart.save()
		data = {
		'quantity':quantity,
		'maxim':maxim,
		'count': count,
		}
		return JsonResponse(data)
	request.session['has_cart'] = True
	cart=Cart()
	cart.Session=str(random.randint(1000, 9999))
	cart.save()
	request.session['cartid']=cart.Session
	order=Order()
	order.Cart=cart
	order.Brand=Brand.objects.get(Name=name)
	order.Bill=int(quantity)*price
	order.Quantity=int(quantity)
	if request.user.is_authenticated:
		order.User=Userdetail.objects.get(Contact=request.user.username)
	order.Wakati=datetime.now()
	order.Status='uncomplete'
	order.save()
	brand=Brand.objects.get(Name=name)
	brand.save()
	count=Order.objects.filter(Cart=cart).count()
	maxim=brand.Quantity
	if maxim<=0:
		brand.Instock=False
	brand.save()
	total=Order.objects.filter(Cart=cart).aggregate(Sum('Bill'))
	total=total["Bill__sum"]
	cart.Total=total
	cart.save()
	data = {
	'quantity':quantity,
	'maxim':maxim,
	'count': count,
	}
	return JsonResponse(data)


def remove(request):
	brand=request.GET.get('brand')
	brand=int(brand)
	cart=Cart.objects.get(Session=request.session['cartid'])
	brand=Brand.objects.get(id=brand)
	order=Order.objects.get(Brand=brand, Cart=cart)
	cart.Total=cart.Total-order.Bill
	brand.Quantity=brand.Quantity+order.Quantity
	brand.save()
	cart.save()
	order.delete()
	count=Order.objects.filter(Cart=cart)
	count=count.aggregate(Sum('Quantity'))
	count=count['Quantity__sum']
	data={'count':count,}
	return JsonResponse(data)

@login_required(login_url='/login/')
def details(request):
	user=Userdetail.objects.get(Contact=request.user.username)
	order=Order.objects.filter(User=user).last()
	cart=order.Cart
	orders=Order.objects.filter(Cart=cart)
	if request.session.get('has_cart', False):
		cart=Cart.objects.get(Session=request.session['cartid'])
		count=Order.objects.filter(Cart=cart)
		count=count.aggregate(Sum('Quantity'))
		count=count['Quantity__sum']
	else:
		count=0
	context={'count':count, 'orders':orders,}
	templatename='user/orders.html'
	return render(request, templatename, context)
@login_required(login_url='/login/')
def orders(request):
	user=Userdetail.objects.get(Contact=request.user.username)
	carts=Cart.objects.none()
	orders=Order.objects.filter(User=user)
	for x in orders:
		cart=Cart.objects.filter(id=x.id)
		carts=carts.union(cart)
	carts=carts.distinct('id')
	if request.session.get('has_cart', False):
		cart=Cart.objects.get(Session=request.session['cartid'])
		count=Order.objects.filter(Cart=cart)
		count=count.aggregate(Sum('Quantity'))
		count=count['Quantity__sum']
	else:
		count=0
	context={'count':count, 'carts':carts,}
	templatename='user/carts.html'
	return render(request, templatename, context)
def complete(request):
	if request.method=="POST":
		loc=request.POST.get('loc')
		delivery=Delivery()
		cart=Cart.objects.get(Session=request.session['cartid'])
		delivery.Cart=cart
		delivery.Status='undelivery'
		delivery.Location=loc
		delivery.Ordertime=datetime.now()
		delivery.save()
		for x in cart.order_set.all():
			x.Status='onroute'
			x.save()
		contact=request.user.username
		if len(contact) == 10:
			contact=contact[1:10]
			contact='+254'+contact
		secret=cart.id
		del request.session['has_cart']
		del request.session['cartid']
		message='Hi there, Your order is being delivered and your order secret number is %s. Our agents will need it on order delivery. '%secret
		url ="https://my.jisort.com/messenger/send_message/?username=isaacmasinde2019@gmail.com&password=14414@starehe&recipients=%s&message="%contact +message	
		payload = {}
		headers = {}
		response = requests.request("GET", url, headers=headers, data = payload)
		return redirect('orders')
	if request.session.get('has_cart', False):
		cart=Cart.objects.filter(Session=request.session['cartid']).last()
		count=Order.objects.filter(Cart=cart)
		count=count.aggregate(Sum('Quantity'))
		count=count['Quantity__sum']
	else:
		count=0
	if cart.Total == 0:
		return redirect('details')
	total=cart.Total+50.00
	if request.user.is_authenticated:
		user=Userdetail.objects.get(Contact=request.user.username)
		biz=Biz.objects.get(Owner=user)
		context={
		'user':user,'biz':biz,'count':count,'total':total,'cart':cart,
		}
		templatename='user/complete.html'
		return render(request, templatename, context)
	context={
	'count':count,'total':total,'cart':cart,
	}
	templatename='user/complete.html'
	return render(request, templatename, context)






# Create your views here.
