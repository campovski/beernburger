from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Beer, Manufacturer


def index(request, sort_by='-id'):
	all_beers = Beer.objects.all().order_by(sort_by)
	if sort_by == 'grade_total':
		all_beers.order_by('grade_taste')
	elif sort_by == '-grade_total':
		all_beers.order_by('-grade_taste')
	if all_beers:
		return render(request, 'beer/index.html', { 'all_beers': all_beers })
	return HttpResponse('<h2>You have no beers in database...</h2>')

def detail(request, beer_id):
	beer = Beer.objects.filter(pk=beer_id)
	if beer:
		brewer = Manufacturer.objects.filter(pk=beer.first().brewer.id)
		context = {
			'beer': beer.first(),
			'brewer': brewer.first(),
		}
		if beer.first().image != 'null':
			return render(request, 'beer/detail.html', context)
		return render(request, 'beer/detail_old.html', context)
	raise Http404('Incorrect beer_id')

def search(request, query):
	names = Beer.objects.filter(name__icontains=query.lower())
	brewers = Beer.objects.filter(name__icontains=query.lower())
	union = (names | brewers).distinct()
	if union:
		return render(request, 'beer/search.html', { 'all_beers': union })
	return HttpResponse("<h1>You searched for: {0}".format(query))
