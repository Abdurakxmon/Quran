from django.shortcuts import render
from .models import *
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
import random
from django.db.models import Q
from django.views.generic import ListView


def main(request):
    recently_surais = None
    surai = Surai.objects.all()
    ls=[]
    while len(ls)<5:
        t=random.randint(1, 114)
        if t not in ls:
            ls.append(t)
    random_surah = Surai.objects.filter(number__in=ls)

    try:
        recently_surais = Surai.objects.filter(slug__in=request.session['recently_views'])
    except:
        pass
    context = {
        'surai':surai,
        'recently_surais':recently_surais,
        'random_surah':random_surah,

    }
    return render(request, 'index.html',context)

class SuraiViewDetail(View):
    def get(self,request,surai_slug): 
        pervous=None
        next_s = None
        surai = get_object_or_404(Surai, slug=surai_slug)
        try:
            pervous = Surai.objects.get(id=(int(surai.id)-1))
        except:
            pass
        try:
            next_s = Surai.objects.get(id=(int(surai.id)+1))
        except:
            pass
        try:
            if surai_slug in request.session['recently_views']:
                request.session['recently_views'].remove(surai_slug)

            request.session['recently_views'].insert(0,surai_slug)

            if len(request.session['recently_views'])>10:
                request.session['recently_views'].pop()
        except:
            request.session['recently_views'] = [surai_slug]
        request.session.modified = True
        
        context = {
            'surai':surai,
            'pervous':pervous,
            'next':next_s,
            }
        return render(request, 'details.html', context)


def search(request):
    print('?')

    if request.method == "POST":
        print('!')
        var = request.POST["q"]
        print(var)
    return render(request, 'index.html')