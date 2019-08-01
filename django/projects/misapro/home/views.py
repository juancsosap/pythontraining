# Custom Libraries
from main.views import IndexView

class HomeView(IndexView):
	app='home'
	url='home:index'
	template='home/index.html'
	authenticated=True