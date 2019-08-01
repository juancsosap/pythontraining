# Custom Libraries
from main.views import IndexView

class AboutView(IndexView):
	app='about'
	url='about:index'
	template='about/index.html'
	require_auth=False