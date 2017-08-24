from django.conf.urls import url
from app import views
from app import views

urlpatterns = [
    url(r'^email/$', views.email, name='email'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^', views.IndexView.as_view(), name='index'),

]