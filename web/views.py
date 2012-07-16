# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    ctxt = ''
    return render_to_response('web/home.html',
            ctxt,
            context_instance=RequestContext(request))
