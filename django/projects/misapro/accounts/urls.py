from django.conf.urls import url
from accounts.views import AuthenticationView, LogoutView
from main.views import IndexView
from . import views

app_name = 'accounts'

urlpatterns = [
	# User Authentication
    url(r'^login/$', AuthenticationView.as_view(), name='login'),
    url(r'^login_user/$', AuthenticationView.as_view(failed=True), name='login_user'),
    url(r'^auth/$', AuthenticationView.as_view(), name='auth'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    # User Registration
    url(r'^checkin/$', IndexView.as_view(
        app='checkin',
        url='accounts:checkin',
        template='accounts/checkin.html'
    ), name='checkin'),
    url(r'^register$', views.register, name='register'),
    # User Profile
    url(r'^profile/$', IndexView.as_view(
        app='profile',
        url='accounts:profile',
        template='accounts/profile.html',
        authenticated=True
    ), name='profile'),
    
]