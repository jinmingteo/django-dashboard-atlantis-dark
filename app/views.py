# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.db.models import Sum, Count
from django.http import HttpResponse
from .models import Workout, Participant
from datetime import datetime


@login_required(login_url="/login/")
def index(request):
    daily_workout = Workout.objects.filter(date__date = datetime.today())
    context = daily_workout.aggregate(Sum("duration"), Sum("calories"), Count('participant', distinct=True))
    context['total_participants'] = Participant.objects.all().count()
    # print (context) {'duration__sum': 30, 'calories__sum': 220, 'participant__count': 2}

    return render(request, "index.html", context)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))
