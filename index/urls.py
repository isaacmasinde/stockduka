from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
	path('', index, name='index'),
	path('cart/', cart, name='cart'),
	path('logout/', out, name='logout'),
	path('register/', register, name='register'),
	path('login/', enter,name='login'),
	path('validate/', validate,name='validate'),
	path('ajaxlogin/', ajaxlogin,name='ajaxlogin'),
	path('search/', search,name='search'),		
	path('ajaxregister/', ajaxregister,name='ajaxregister'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)