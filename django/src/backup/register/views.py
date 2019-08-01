from django.shortcuts import render
from .models import User, Register

# Create your views here.
def index(request):
	return render(request, 'index.html')