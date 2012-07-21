# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from web.models import Page
from students.models import *
from students.forms import *

def student_registration(request):
    form =  StudentForm()
    try:
        page = Page.objects.get(page='student')
    except Page.DoesNotExist:
        page = ''

    ctxt = {
        'form': form,
        'page': page,
        'prev': '/welcome/',
        'next': ''
    }
    return render_to_response('students/registration.html',
            ctxt,
            context_instance=RequestContext(request))
