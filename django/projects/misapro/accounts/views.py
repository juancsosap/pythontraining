from main.tools import load_page 

# Django Libraries
from django.conf import settings
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout 
# Custom Libraries
from main.tools import get_context, get_lang
from main.views import RedirectView

"""
que
url

quien
object = auth
auth.admin1

auth.admin1.condo1  que1
auth.admin1.condo2  que2

auth.admin1.condo1.proper1

invitaciones por token

"""




@require_http_methods(["GET","POST"])
class AuthenticationView(View):

	failed = False

	def get(self, request):
		if not self.failed:
			request.session['error'] = 200
			if not request.user.is_authenticated:
				return HttpResponseRedirect(reverse('accounts:login_user'))
			else:
				request.session['redirected'] = True
				return HttpResponseRedirect(reverse(settings.HOME_URL))
		else:
			if not request.user.is_authenticated:
				if 'redirected' not in request.session: 
					request.session['redirected'] = False
				if not request.session['redirected']: 
					request.session['path'] = settings.LOGIN_URL
				dic = get_context(request,'login')
				return render(request, 'accounts/login.html', {'dic':dic})	
			else:
				request.session['redirected'] = True
				return HttpResponseRedirect(reverse(settings.HOME_URL))

	def post(self, request):
		if request.user.is_authenticated:
			request.session['path'] = settings.HOME_URL
			return HttpResponseRedirect(reverse(request.session['path']))
		else:
			tenant = request.POST.get('tenant','')
			username = request.POST.get('username','')
			password = request.POST.get('password','')
			if (not tenant) or (not username) or (not password):
				request.session['error'] = 400 
				return HttpResponseRedirect(reverse('accounts:login_user'))
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				request.session['error'] = 200
				if not request.session['redirected']: 
					return HttpResponseRedirect(reverse(settings.HOME_URL))
				else:
					return HttpResponseRedirect(reverse(request.session['path']))
			else:
				request.session['error'] = 401 
				return HttpResponseRedirect(reverse('accounts:login_user'))

@require_http_methods(["GET"])
class LogoutView(RedirectView):
	path='about:index'

	def get(self, request, **kwargs):		
		if request.user.is_authenticated: 
			logout(request)
		
		return super(LogoutView, self).get(request)


from django.contrib.auth.forms import UserCreationForm

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('accounts:checkin_success'))
	return render(request, 'accounts/success.html',{'data':{'user':username}})