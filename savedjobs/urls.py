from django.conf.urls import url
from savedjobs import views

urlpatterns = [
    url(r'^$', views.savedjob_list),
    url(r'^(?P<pk>[0-9]+)/$', views.savedjob_detail),
]