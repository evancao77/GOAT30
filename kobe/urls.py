
from django.conf.urls import url

from kobe import views

urlpatterns = [
    url(r'^add_instance', views.add_instance),
]
