from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('siteNavigator.views',
    # Examples:

    (r'^football/home', 'home'),
    (r'^football/loginScreen', 'loginPage'),
    (r'^football/LeagueSample', 'LeagueSample'),
    (r'^football/DreamTeam', 'DreamTeam'),
    (r'^football/LeagueRankings', 'LeagueRankings'),
    (r'^football/StartingPercentages', 'StartingPercentages'),
    (r'^football/DreamTeam', 'DreamTeam'),
     (r'^football/stats/PlayerValues', 'PlayerValues'),
    (r'^football/CreateAccount', 'CreateAccount'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^football/(?P<league_id>\d+)/TeamOwnerPage/(?P<owner_id>\d+)', 'TeamOwnerPage'),
    # url(r'^$', 'football.views.home', name='home'),
    # url(r'^football/', include('football.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
