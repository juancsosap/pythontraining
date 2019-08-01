# Custom Libraries
from main.views import IndexView

class CondosView(IndexView):
	app='condos'
	url='condos:index'
	template='condos/index.html'
	authenticated=True