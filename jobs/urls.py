from django.conf.urls import url
from . import views

app_name = 'jobs'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<job_id>[0-9]+)$', views.detail, name='detail')
]