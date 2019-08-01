from django.conf.urls import url
from . import views

app_name = 'join'

urlpatterns = [
    # /join/ 
    url(r'^$', views.JoinFormView.as_view(), name='home'),
]