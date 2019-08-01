# Custom Libraries
from main.views import IndexView

@login_required(["GET"])
class ProvidersView(IndexView):
	app='providers'
	url='providers:index'
	template='providers/index.html'
	authenticated=True