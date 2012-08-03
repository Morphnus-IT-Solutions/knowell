# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext

from random import randint, shuffle

from web.models import Page
from students.models import *
from students.forms import *


def generate_unique_random(total, rmax, rmin=0):
    if total > rmax:
        return []
    i = 0
    arr = []
    while(i < rmax):
        r = randint(rmin, rmax)
        if r not in arr:
            arr.append(r)
            i += 1
    return arr


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
            stream = obj.stream
            standard = obj.standard
            test = Test.objects.filter(standard=standard, stream=stream, is_active=True)
            if test:
                test = test[0]
                ts = test.testsection_set.all()
                if ts:
                    qdict = {}
                    for t in ts:
                        sec = t.section
                        lod = t.level_of_difficulty
                        tq = t.total_questions
                        questions = Question.objects.filter(section=sec, level_of_difficulty=lod, is_active=True)
                        print "q:::%s" % questions
                        if questions:
                            qlen = len(questions)
                            random = generate_unique_random(tq, qlen-1)
                            q = []
                            for r in random:
                                if sec not in qdict:
                                    qdict[sec] = [questions[r]]
                                else:
                                    qdict[sec].append(questions[r])
                        else:
                            print "No questions"
                    print qdict
                    create_student_test(obj, test, qdict)
                else:
                    print "No sections found"

            else:
                print "No test found"
        else:
            errors = form.errors
            print errors
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
