# dappx/urls.py
from django.conf.urls import url
from django.urls import path
from . import views
# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    path('start/',views.newpre,name='newprescription'),
    url(r'^new/$', views.new, name='new'),
    path('record/', views.record, name='record'),
    path('mail/',views.sendmail,name='mail')
]