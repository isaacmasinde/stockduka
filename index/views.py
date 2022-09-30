from django.shortcuts import render,redirect
from .models import *
from django.http import *
from django.db.models import *
from django.contrib.auth.models import *
from django.contrib.auth import *
from django.core.paginator import Paginator
def index(request):
	templatename='index/home.html'
	popular=Brand.objects.filter(Category=1)
	brands=Brand.objects.all().order_by('Category')
	paginator = Paginator(popular, 4) 
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	if request.session.get('has_cart', False):
		cart=Cart.objects.filter(Session=request.session['cartid']).last()
		count=Order.objects.filter(Cart=cart)
		count=count.aggregate(Sum('Quantity'))
		count=count['Quantity__sum']
	else:
		count=0
	context={'page_obj':page_obj, 'count':count,}
	return render(request, templatename, context)
def cart(request):
	if not request.session.get('has_cart', False):
		return redirect('index')
	cart=Cart.objects.filter(Session=request.session['cartid']).last()
	count=Order.objects.filter(Cart=cart)
	count=count.aggregate(Sum('Quantity'))
	count=count['Quantity__sum']
	total=Order.objects.filter(Cart=cart).aggregate(Sum('Quantity'))
	total=total["Quantity__sum"]
	templatename='user/cart.html'
	context={'cart':cart, 'count':count, 'total':total}
	return render(request, templatename, context)
def out(request):
	logout(request)
	return redirect('index')
def register(request):
	if request.method=='POST':
		fname=request.POST.get('fname')
		lname=request.POST.get('lname')
		contact=request.POST.get('contact')
		password=request.POST.get('password')
		bizloc=request.POST.get('bizloc')
		bizname=request.POST.get('bizname')
		if not User.objects.filter(username=contact).exists():
			user=User.objects.create_user(username=contact,password=password,first_name=fname,last_name=lname)
			login(request, user)
			userobj=Userdetail()
			userobj.Firstname=fname
			userobj.Secondname=lname
			userobj.Contact=contact
			userobj.Status='Client'
			userobj.save()
			bizobj=Biz()
			bizobj.Name=bizname
			bizobj.Location=bizloc
			bizobj.Owner=userobj
			bizobj.save()
			return redirect('index')
		else:
			error='User exists'
			context={'error':error,}
			return render(request, 'index/register.html', context)
	if request.session.get('has_cart', False):
		cart=Cart.objects.filter(Session=request.session['cartid']).last()
		count=Order.objects.filter(Cart=cart)
		count=count.aggregate(Sum('Quantity'))
		count=count['Quantity__sum']
	else:
		count=0
	context={'count':count,}
	templatename='index/register.html'
	return render(request, templatename, context)

def enter(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			if request.user.is_staff:
				return redirect('items')
			if request.session.get('has_cart', False):
				cart=Cart.objects.get(Session=request.session['cartid'])
				for x in cart.order_set.all():
					x.User=Userdetail.objects.get(Contact=request.user.username)
					x.save()
			return redirect('index')
		else:
			error='Wrong details!'
			context={'error':error,}
			templatename='index/login.html'
			return render(request, templatename, context)
	if request.session.get('has_cart', False):
		cart=Cart.objects.filter(Session=request.session['cartid']).last()
		count=Order.objects.filter(Cart=cart)
		count=count.aggregate(Sum('Quantity'))
		count=count['Quantity__sum']
	else:
		count=0
	context={'count':count,}
	templatename='index/login.html'
	return render(request, templatename, context)
def validate(request):
    username = request.GET.get('username')
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
def ajaxlogin(request):
	username = request.GET.get('username')
	password = request.GET.get('password')
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		data={'loggedin':True,}
		if request.session.get('has_cart', False):
			cart=Cart.objects.get(Session=request.session['cartid'])
			for x in cart.order_set.all():
				x.User=Userdetail.objects.get(Contact=request.user.username)
				x.save()
	else:
		data={'loggedin':False,}
	return JsonResponse(data)
def ajaxregister(request):
	fname=request.POST.get('fname')
	lname=request.POST.get('lname')
	contact=request.POST.get('contact')
	password=request.POST.get('password')
	bizloc=request.POST.get('bizloc')
	bizname=request.POST.get('bizname')
	if not User.objects.filter(username=contact).exists():
		user=User.objects.create_user(username=contact,password=password,first_name=fname,last_name=lname)
		login(request, user)
		userobj=Userdetail()
		userobj.Firstname=fname
		userobj.Secondname=lname
		userobj.Contact=contact
		userobj.Status='Client'
		userobj.save()
		bizobj=Biz()
		bizobj.Name=bizname
		bizobj.Location=bizloc
		bizobj.Owner=userobj
		bizobj.save()
		if request.session.get('has_cart', False):
			cart=Cart.objects.get(Session=request.session['cartid'])
			for x in cart.order_set.all():
				x.User=Userdetail.objects.get(Contact=request.user.username)
				x.save()
		data={'loggedin':True,}
	else:	
		data={'loggedin':False,}
	return JsonResponse(data)
def search(request):
	templatename='index/home.html'
	if request.method=='POST':
		hint=request.POST.get('search')
		results=Brand.objects.filter(Name__icontains=hint)
		results.distinct('id')
		paginator = Paginator(results, 4) 
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		if request.session.get('has_cart', False):
			cart=Cart.objects.filter(Session=request.session['cartid']).last()
			count=Order.objects.filter(Cart=cart)
			count=count.aggregate(Sum('Quantity'))
			count=count['Quantity__sum']
		else:
			count=0
		context={'page_obj':page_obj, 'count':count,}
		return render(request, templatename, context)
# Create your views here.
