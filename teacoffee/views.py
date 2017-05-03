from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Torc
from beer.models import Manufacturer


def index(request, sort_by='-id'):
	all_torcs = Torc.objects.all().order_by(sort_by)
	if sort_by == 'grade_total':
		all_torcs.order_by('grade_taste')
	elif sort_by == '-grade_total':
		all_torcs.order_by('-grade_taste')
	if all_torcs:
		return render(request, 'teacoffee/index.html', { 'all_torcs': all_torcs })
	return HttpResponse('<h2>You have no torcs in database...</h2>')

def detail(request, torc_id):
	torc = Torc.objects.filter(pk=torc_id)
	if torc:
		maker = Manufacturer.objects.filter(pk=torc.first().maker.id)
		context = {
			'torc': torc.first(),
			'maker': maker.first(),
		}
		if torc.first().image != 'null':
			return render(request, 'teacoffee/detail.html', context)
		return render(request, 'teacofee/detail_old.html', context)
	raise Http404('Incorrect torc_id')

def search(request, query):
	union = Torc.objects.filter(name__icontains=query.lower())
	if union:
		return render(request, 'torc/search.html', { 'all_torcs': union })
	return HttpResponse("<h1>You searched for: {0}".format(query))

def browse(request):
        makers = list(Torc.objects.values_list('maker', flat=True).distinct())
        resultset = list(Manufacturer.objects.filter(pk__in=makers).values_list('name', flat=True).order_by('name'))
        return render(request, 'teacoffee/browse.html', { 'resultset': resultset })

def browse_item(request, item):
        maker = Manufacturer.objects.filter(name=item).first()
        resultset = Torc.objects.filter(maker=maker.id)
        return render(request, 'teacoffee/search.html', { 'all_torcs': resultset })

