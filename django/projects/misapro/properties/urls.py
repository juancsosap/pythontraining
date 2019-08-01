# Django Libraries
from django.conf.urls import url
# Custom Libraries
from .views import PropertiesView

app_name = 'properties'

urlpatterns = [
	# /properties/
	url(r'^$', PropertiesView.as_view(), name='index'),
]