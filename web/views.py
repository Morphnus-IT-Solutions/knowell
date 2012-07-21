# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from web.models import Banner, Page

def home(request):
    banner = Banner.objects.filter(type="home")
    if banner:
        banner = banner[0]
    ctxt = {
        'banner': banner,
    }
    return render_to_response('web/home.html',
            ctxt,
            context_instance=RequestContext(request))

def welcome(request):
    try:
        page = Page.objects.get(page='welcome')
    except Page.DoesNotExist:
        page = ''

    banners = Banner.objects.filter(type="welcome")
    
    ctxt = {
        'banners': banners,
        'page': page,
        'prev': "/",
        'next': "/student-registration/"
    }
    return render_to_response('web/welcome.html',
            ctxt,
            context_instance=RequestContext(request))
