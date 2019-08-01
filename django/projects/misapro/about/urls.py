# Django Libraries
from django.conf.urls import url
# Custom Libraries
from .views import AboutView

app_name = 'about'

urlpatterns = [
	# /about/
	url(r'^$', AboutView.as_view(), name='index'),
]