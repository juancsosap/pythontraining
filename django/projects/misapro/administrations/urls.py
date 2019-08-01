# Django Libraries
from django.conf.urls import url
# Custom Libraries
from .views import AdministrationsView

app_name = 'administrations'

urlpatterns = [
	# /administrations/
	url(r'^$', AdministrationsView.as_view(), name='index'),
]