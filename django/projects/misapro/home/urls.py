# Django Libraries
from django.conf.urls import url
# Custom Libraries
from .views import HomeView

app_name = 'home'

urlpatterns = [
	# /home/
	url(r'^$', HomeView.as_view(), name='index'),
]