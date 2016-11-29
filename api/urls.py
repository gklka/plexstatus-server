from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add_token/$', views.add_token, name='add_token'),
]
