from django.shortcuts import render,redirect
from django.http import *
from index.models import *
from django.core.paginator import Paginator
from django.db.models import *
from django.contrib.auth.models import *
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required,user_passes_test
import random
from datetime import datetime

def staff_check(user):
    return user.is_staff
    
@user_passes_test(staff_check, login_url='/login/')
def items(request):
	if request.method=="POST":
		category=request.POST['category']
		measure=request.POST['measure']
		name=request.POST['item']
		category=Category.objects.get(id=int(category))
		item=Item()
		item.Category=category
		item.Name=name
		item.Measure=measure
		item.save()
		return redirect('items')
	items=Item.objects.all()
	category=Category.objects.all()
	paginator = Paginator(items, 30) 
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context={'category':category,'page_obj': page_obj}
	templatename='stockadmin/items.html'
	return render(request, templatename, context)

@user_passes_test(staff_check, login_url='/login/')
def categories(request):
	if request.method=="POST":
		name=request.POST['name']
		item=Category()
		item.Name=name
		item.save()
		return redirect('categories')
	categories = Category.objects.all()
	paginator = Paginator(categories, 30)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'stockadmin/categories.html', {'page_obj': page_obj})
def brands(request):
	if request.method=="POST":
		name=request.POST['name']
		item=Category()
		item.Name=name
		item.save()
		return redirect('categories')
	brands = Brand.objects.all()
	paginator = Paginator(brands, 30)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'stockadmin/brand.html', {'page_obj': page_obj})

@user_passes_test(staff_check, login_url='/login/')
def users(request):
	users = Userdetail.objects.all()
	paginator = Paginator(users, 50)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request, 'stockadmin/users.html', {'page_obj': page_obj})



# Create your views here.
