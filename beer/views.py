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
	beers = Beer.objects.filter(name__icontains=query.lower())
	if beers:
		return render(request, 'beer/search.html', { 'all_beers': beers })
	return HttpResponse("<h1>You searched for: {0}".format(query))


def browse(request, query):
	if query == 'brewer':
		brewers = list(Beer.objects.values_list('brewer', flat=True).distinct())
		resultset = list(Manufacturer.objects.filter(pk__in=brewers).values_list('name', flat=True).order_by('name'))
	elif query == 'beer_type':
		resultset = list(Beer.objects.values_list('beer_type', flat=True).distinct().order_by('beer_type'))
	else:
		raise Http404('You cannot browse by that category... Don\'t try to be smart ;)')
	return render(request, 'beer/browse.html', { 'resultset': resultset, 'query': query })


def browse_item(request, query, item):
	if query == 'brewer':
		brewer = Manufacturer.objects.filter(name=item).first()
		resultset = Beer.objects.filter(brewer=brewer.id)
	elif query == 'beer_type':
		resultset = Beer.objects.filter(beer_type__icontains=item.lower())
	else:
		raise Http404('You cannot browse by that category... Don\'t try to be smart ;)')
	return render(request, 'beer/search.html', { 'all_beers': resultset })

