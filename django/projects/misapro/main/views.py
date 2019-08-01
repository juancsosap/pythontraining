# Django Libraries
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.views import View
# Custom Libraries
from main.models import Dictionary
from main.tools import get_context, get_lang

@require_http_methods(["GET"])
class RedirectView(View):
	path = ''

	def get(self, request):
		# Path Redirection
		if not self.path:
			self.path = request.session['path']
		else:
			request.session['path'] = self.path
		
		return HttpResponseRedirect(reverse(self.path))

@require_http_methods(["GET"])
class ChangeLangView(RedirectView):

	def get(self, request, **kwargs):
		# Languaje Redirection
		if 'lang' in kwargs: 
			self.lang = kwargs['lang']
		if not self.lang: 
			self.lang = request.session['lang']
		else: 
			request.session['lang'] = self.lang
		
		return super(ChangeLangView, self).get(request)

@require_http_methods(["GET"])
class IndexView(View):
	app = ''
	url = ''
	template = ''
	authenticated = False
	require_auth = True
	data = {}

	def get(self, request):
		
		# If Authentication depended
		if self.require_auth:

			# If user is authenticated and must be authenticated
			# or if user is not authenticated and must not be authenticated
			if self.authenticated == request.user.is_authenticated:
				request.session['path'] = self.url
				dic = get_context(request,self.app)
				dic.update(self.data)
				request.session['redirected'] = False
				return render(request, self.template, {'dic':dic})	
			else:
				request.session['redirected'] = True
				request.session['path'] = self.url
				if self.authenticated:
					return HttpResponseRedirect(reverse(settings.LOGIN_URL))
				else:
					return HttpResponseRedirect(reverse(settings.HOME_URL))
		else:
			request.session['path'] = self.url
			dic = get_context(request,self.app)
			return render(request, self.template, {'dic':dic})