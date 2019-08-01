# Django Libraries
from django.conf.urls import url
# Custom Libraries
from .views import CondosView

app_name = 'condos'

urlpatterns = [
	# /condos/
	url(r'^$', CondosView.as_view(), name='index'),
]