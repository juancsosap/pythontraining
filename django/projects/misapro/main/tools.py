# Django Libraries
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
# Custom Libraries
from main.models import Dictionary

def get_context(request,app):
	lang = get_lang(request)
	dic = Dictionary.objects.filter(lang=lang)
	menus = dic.filter(ttype='navbar').filter(code='menu')
	menu,field = {},{}
	for m in menus:
		menu[m.app] = m.value
	title = dic.filter(app=app).filter(code='title')[0].value
	fields = dic.filter(app=app)
	for f in fields:
		if f.ttype in field: field[f.ttype][f.code] = f.value
		else: field[f.ttype] = { f.code : f.value } 
	if 'error' not in request.session: request.session['error'] = False
	field.update({'app':{'name':app,'title':title,'lang':lang, 'error':request.session['error']},'menu':menu})
	return field

def get_lang(request):
	if 'lang' in request.session: return request.session['lang'] 
	return 'es'

def load_page(request, authenticated, appname, template, link, data={}):
	if authenticated == request.user.is_authenticated:
		request.session['path'] = reverse(link)
		dic = get_context(request,appname)
		dic.update(data)
		request.session['redirected'] = False
		return render(request, template, {'dic':dic})	
	else:
		request.session['redirected'] = True
		request.session['path'] = reverse(link)
		if authenticated:
			return HttpResponseRedirect(reverse(settings.LOGIN_URL))
		else:
			return HttpResponseRedirect(reverse(settings.HOME_URL))