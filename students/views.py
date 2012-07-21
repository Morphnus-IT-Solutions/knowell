# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext

from random import randint

from web.models import Page
from students.models import *
from students.forms import *


def student_registration(request):
    form =  StudentForm()
    errors = []
    try:
        page = Page.objects.get(page='student')
    except Page.DoesNotExist:
        page = ''
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            obj.registration_number = str(obj.first_name[:3]).lower() + str(randint(1,9999999))
            obj.save()
        else:
            errors = form.errors
    ctxt = {
        'form': form,
        'page': page,
        'prev': '/welcome/',
        'next': '',
        'errors': errors
    }
    return render_to_response('students/registration.html',
            ctxt,
            context_instance=RequestContext(request))
