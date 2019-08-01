from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail

from .models import Join
from .forms import JoinForm

# Create your views here.
class JoinFormView(View):
	form_class = JoinForm
	template_name = 'join/home.html'

	def get(self, request):
		form = self.form_class(request.POST or None)
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST or None)
		if form.is_valid():
			new_join = form.save(commit=False)
			new_join.save()
			send = send_mail('Joined From MVP Landing', 'Person: %s\n Email: %s\n Timestamp: %s' % (new_join.full_name, new_join.email, str(new_join.timestamp)), ['juan.c.sosa.p@gmail.com'])
		return render(request, self.template_name, {'form':form})
