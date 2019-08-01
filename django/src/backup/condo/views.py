from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Condo
# Create your views here.
def index(request):
	all_condos = Condo.objects.all()
	#template = loader.get_template('index.html')
	context = { 'all_condos' : all_condos }
	#return HttpResponse(template.render(context, request))
	return render(request, 'index.html', context))

def detail(request, condo_id):
	return HttpResponse(template.render(context, request))