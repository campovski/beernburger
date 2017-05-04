from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Burger
from beer.models import Manufacturer


def index(request, sort_by='-id'):
	all_burgers = Burger.objects.all().order_by(sort_by)
	if sort_by == 'grade_total':
		all_burgers.order_by('grade_taste')
	elif sort_by == '-grade_total':
		all_burgers.order_by('-grade_taste')
	if all_burgers:
		return render(request, 'burger/index.html', { 'all_burgers': all_burgers })
	return HttpResponse('<h2>You have no burgers in database...</h2>')

def detail(request, burger_id):
	burger = Burger.objects.filter(pk=burger_id)
	if burger:
		maker = Manufacturer.objects.filter(pk=burger.first().maker.id)
		context = {
			'burger': burger.first(),
			'maker': maker.first(),
		}
		if burger.first().image != 'null':
			return render(request, 'burger/detail.html', context)
		return render(request, 'burger/detail_old.html', context)
	raise Http404('Incorrect burger_id')


def search(request, query):
	union = Burger.objects.filter(name__icontains=query.lower())
	if union:
		return render(request, 'burger/search.html', { 'all_burgers': union })
	return HttpResponse("<h1>You searched for: {0}".format(query))


def browse(request):
        makers = list(Burger.objects.values_list('maker', flat=True).distinct())
        resultset = list(Manufacturer.objects.filter(pk__in=makers).values_list('name', flat=True).order_by('name'))
       	return render(request, 'burger/browse.html', { 'resultset': resultset })

def browse_item(request, item):
        maker = Manufacturer.objects.filter(name=item).first()
        resultset = Burger.objects.filter(maker=maker.id)
        return render(request, 'burger/search.html', { 'all_burgers': resultset })
