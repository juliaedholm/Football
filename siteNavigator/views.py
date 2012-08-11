# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
import models
from models import FootballMainWeeklyMatchResults
from models import FootballViewWeeklyStats
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

    gameList = FootballMainWeeklyMatchResults.objects.filter(week_num='1')  

    c = Context({'pageType':'LeagueSample', 'valueList': ''})
    return HttpResponse(t.render(c))
 
def DreamTeam(request):
    return render_to_response('DreamTeam.html', { 'pageType':'DreamTeam'} )
 
def LeagueRankings(request):
    return render_to_response('DreamTeam.html', { 'pageType':'LeagueRankings'} )

def PlayerValues(request):
    ownerERList=FootballViewWeeklyStats.objects.filter(week_num='10', rj_team_id='1').order_by("-pick_value")
    return render_to_response('PlayerValues.html', { 'pageType':'PlayerValues', 'ERList': ownerERList} )

def StartingPercentages(request):
    c = RequestContext(request, {'Player1':'Joe','Player2':'Bill','Player3':'Jessica','Player4':'Sally', 'pageType':'StartingPercentages'})
    return render_to_response('StartingPercentages.html', c )