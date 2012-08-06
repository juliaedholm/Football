# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
import datetime

def home(request):
   return render_to_response('heroHome.html')

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
<<<<<<< HEAD
    player={'name':'Joe','wins':'2'}
    c = Context({'person':player,})
=======
    player1={'name':'A', 'wins':'1', 'didWin':'yes'}
    player2={'name':'B', 'wins':'2'}
    player3={'name':'C', 'wins':'3'}
    player4={'name':'D', 'wins':'4'}
    c = Context({'team':[player1,player2,player3,player4]})
>>>>>>> making tables with logic
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
    c = RequestContext(request, {'Player1':'Joe','Player2':'Bill','Player3':'Jessica','Player4':'Sally'})
    return HttpResponse(t.render(c))