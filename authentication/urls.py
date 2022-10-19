from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('account', views.account, name='account'),
	path('send-sms', views.sendsms, name='send-sms'),
	path('check-sms', views.checksms, name='check-sms'),
]