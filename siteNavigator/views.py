# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
import datetime

def home(request):
    t = get_template('homeB.html')
    c = RequestContext(request, {'smiley':'cheese',})
    return HttpResponse(t.render(c))

def loginPage(request):
    t = get_template('HomeSample.html')
    c = RequestContext(request, {'blah':'cheese',})
    return HttpResponse(t.render(c))
    #return render_to_response('TestC.html',{'blah':'buh',}, context_instance=RequestContext(request))

def hero(request):
    t = get_template('heroHome.html')
    c = RequestContext(request, {'smiley':'cheese',})
    return HttpResponse(t.render(c))

def LeagueSample(request):
    t = get_template('SampleLeague.html')
    c = RequestContext(request, {'smiley':'cheese',})
    return HttpResponse(t.render(c))
 
def DreamTeam(request):
    t = get_template('DreamTeam.html')
    c = RequestContext(request, {'smiley':'cheese',})
    return HttpResponse(t.render(c))
 
def LeagueRankings(request):
    t = get_template('LeagueRankings.html')
    c = RequestContext(request, {'smiley':'cheese',})
    return HttpResponse(t.render(c))