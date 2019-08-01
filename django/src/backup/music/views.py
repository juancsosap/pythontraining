"""
from django.shortcuts import render, get_object_or_404
#from django.http import Http404, HttpResponse
#from django.template import loader
from .models import Album, Song

# Create your views here.
def index(request):
	all_albums = Album.objects.all()
	""" """
	html = '<h1>This is the music app homepage</h1><br>'
	for album in all_albums:
		url = '/music/%s/' % (str(album.id))
		html += '<a href="%s">%s</a><br>' % (url, album.album_title)
	return HttpResponse(html)
	""" """
	""" """
	context = {'all_albums':all_albums}
	template = loader.get_template('index.html')
	return HttpResponse(template.render(context,request))
	""" """
	return render(request, 'index.html', {'all_albums':all_albums})

def detail(request, album_id):
	""" """
	try:
		album = Album.objects.get(id=album_id)
	except Album.DoesNotExist:
		raise Http404("Album does not exist")
	""" """
	album = get_object_or_404(Album, id=album_id)
	return render(request, 'detail.html', {'album':album})

def favorite(request, album_id):
	album = get_object_or_404(Album, id=album_id)
	try:
		selected_song = album.song_set.get(id=request.POST['song'])	
	except (KeyError, Song.DoesNotExist):
		return render(request, 'detail.html', {'album':album,'error_message':"You did't select a valid song"})
	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'detail.html', {'album':album})
"""

from django.views import generic
from .models import Album

class IndexView(generic.ListView):
	template_name = 'index.html'

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = 'detail.html'


