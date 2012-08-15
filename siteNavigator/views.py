# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
import models
from models import FootballMainWeeklyMatchResults
from models import FootballViewWeeklyStats
from models import FootballTeams
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
    ownersInLeague=FootballTeams.objects.filter(rj_league_id='1')
    t = get_template('SampleLeagueA.html')
    gameList = FootballMainWeeklyMatchResults.objects.filter(week_num='1')  
    c = Context({'pageType':'LeagueSample', 'valueList': '','ownerList': ownersInLeague , 'matchList': gameList})
    return HttpResponse(t.render(c))
 
def DreamTeam(request):
    ownersInLeague=FootballTeams.objects.filter(rj_league_id='1')
    return render_to_response('DreamTeam.html', { 'pageType':'DreamTeam', 'ownerList': ownersInLeague} )
 
def TeamOwnerPage (request, owner_id, league_id):
    ownersInLeague=FootballTeams.objects.filter(rj_league_id=league_id)
    teamOwner=FootballTeams.objects.get(rj_team_id=owner_id)
    ownerERList=FootballViewWeeklyStats.objects.filter(week_num='10', rj_team_id=owner_id).order_by("-pick_value")
    return render_to_response('TeamOwnerPage.html', { 'ownerInfo': teamOwner, 'pageType': 'PlayerValues', 'ERList': ownerERList, 'ownerList': ownersInLeague} )
        
def LeagueRankings(request):
    ownersInLeague=FootballTeams.objects.filter(rj_league_id='1')
    return render_to_response('LeagueRankings.html', { 'pageType':'LeagueRankings', 'ownerList': ownersInLeague} )

def PlayerValues(request):
    ownersInLeague=FootballTeams.objects.filter(rj_league_id='1')
    return render_to_response('PlayerValues.html', { 'pageType':'PlayerValues', 'ownerList': ownersInLeague } )

def StartingPercentages(request):
    ownersInLeague=FootballTeams.objects.filter(rj_league_id='1')
    c = RequestContext(request, {'ownerList': ownersInLeague,'Player1':'Joe','Player2':'Bill','Player3':'Jessica','Player4':'Sally', 'pageType':'StartingPercentages'})
    return render_to_response('StartingPercentages.html', c )