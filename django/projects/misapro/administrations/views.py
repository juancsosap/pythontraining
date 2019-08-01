# Custom Libraries
from main.views import IndexView

class AdministrationsView(IndexView):
	app='administrations'
	url='administrations:index'
	template='administrations/index.html'
	authenticated=True