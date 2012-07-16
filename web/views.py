# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from web.models import Banner

def home(request):
    banner = Banner.objects.all()
    if banner:
        banner = banner[0]
    ctxt = {
        'banner': banner,
    }
    return render_to_response('web/home.html',
            ctxt,
            context_instance=RequestContext(request))
