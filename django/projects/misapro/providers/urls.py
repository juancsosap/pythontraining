# Django Libraries
from django.conf.urls import url
# Custom Libraries
from .views import ProvidersView

app_name = 'providers'

urlpatterns = [
	# /providers/
	url(r'^$', ProvidersView.as_view(), name='index'),
]