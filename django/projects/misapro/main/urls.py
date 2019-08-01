from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from .views import RedirectView, ChangeLangView

urlpatterns = [
	# Admin Portal
    url(r'^dbadmin/', admin.site.urls, name='dbadmin'),
    # Apps URL
    url(r'^about/', include('about.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^condos/', include('condos.urls')),
    url(r'^administrations/', include('administrations.urls')),
    url(r'^properties/', include('properties.urls')),
    url(r'^providers/', include('providers.urls')),
    url(r'^accounts/', include('accounts.urls')),
    # Aditional Actions
    url(r'^$', RedirectView.as_view(path='about:index'), name='index'),
    url(r'^actions/chlang/(?P<lang>[a-z\-]+)/$', ChangeLangView.as_view(), name='chlang'),
]