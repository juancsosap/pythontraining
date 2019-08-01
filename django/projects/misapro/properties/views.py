# Custom Libraries
from main.views import IndexView

class PropertiesView(IndexView):
	app='properties'
	url='properties:index'
	template='properties/index.html'
	authenticated=True