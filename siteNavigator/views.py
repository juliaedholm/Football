# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
import datetime

def home(request):
    t = get_template('heroHome.html')
    c = RequestContext(request, {'smiley':'cheese',})
    return HttpResponse(t.render(c))

def CreateAccount(request):
    t = get_template('CreateAccount.html')
    c = RequestContext(request, {'smiley':'cheese',})
    return HttpResponse(t.render(c))

def loginPage(request):
    t = get_template('HomeSample.html')
    c = RequestContext(request, {'blah':'cheese',})
    return HttpResponse(t.render(c))
    #return render_to_response('TestC.html',{'blah':'buh',}, context_instance=RequestContext(request))

def LeagueSample(request):
    t = get_template('SampleLeagueA.html')
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

def StartingPercentages(request):
    t = get_template('StartingPercentages.html')
    c = RequestContext(request, {'smiley':'cheese',})
    return HttpResponse(t.render(c))