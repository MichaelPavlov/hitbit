from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.template import RequestContext

from nav.models import FormWithCaptcha

def home(request):
	print "Hello1"
	if request.session.get('address',False):
		return render(request, 'index.html')
	return render(request, 'work.html',{'id': request.session['address']})

def session(request):
	if 'address' in request.POST:
		request.session['address'] = request.POST['address']
		request.session['bitcoins'] = 0
		form = FormWithCaptcha()
		return render(request, 'work.html',{'id': request.session['address'],'bit':request.session['bitcoins'],'form': form})
	return render(request, 'index.html')

def submitwork(request):
	if request.method == 'POST':
		form=FormWithCaptcha(request.POST)
		if form.is_valid():
			request.session['bitcoins']= request.session['bitcoins'] + 1
	else:
		form = FormWithCaptcha()
	return render(request, 'work.html',{'id': request.session['address'],'bit':request.session['bitcoins'],'form': form})

