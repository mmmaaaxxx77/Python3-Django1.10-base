from django.conf.urls import url
from django.contrib import admin
from apps.dashboard.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.index),
    url(r'^2/', IndexView.index2),
    #url(r'^$', 'apps.dashboard.views.IndexView.index'),
]
