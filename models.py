# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class ScrapeInputDraft(models.Model):
    class Meta:
        db_table = u'scrape_input_draft'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = u'django_content_type'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80, unique=True)
    class Meta:
        db_table = u'auth_group'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey(DjangoContentType)
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = u'auth_permission'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = u'django_site'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey(DjangoContentType, null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class FootballLeagues(models.Model):
    rj_league_id = models.IntegerField(primary_key=True)
    league_host = models.CharField(max_length=200, blank=True)
    host_league_id = models.CharField(max_length=50, blank=True)
    league_name = models.CharField(max_length=250, blank=True)
    league_url = models.CharField(max_length=1000, blank=True)
    league_photo_url = models.CharField(max_length=1000, blank=True)
    league_init_email = models.CharField(max_length=200, blank=True)
    date_add = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'football_leagues'
        options.managed = False

class FootballTeams(models.Model):
    rj_team_id = models.IntegerField(primary_key=True)
    rj_league_id = models.IntegerField(null=True, blank=True)
    team_url = models.CharField(max_length=1000, blank=True)
    team_name = models.CharField(max_length=500, blank=True)
    owner_name = models.CharField(max_length=250, blank=True)
    date_add = models.DateTimeField(null=True, blank=True)
    team_photo_url = models.CharField(max_length=1000, blank=True)
    class Meta:
        db_table = u'football_teams'
        options.managed = False


class FootballViewWeeklyStats(models.Model):
    player_name = models.CharField(max_length=250, blank=True)
    player_position = models.CharField(max_length=50, blank=True)
    player_rank_season = models.IntegerField(null=True, blank=True)
    pick_number_position = models.IntegerField(null=True, blank=True)
    pick_value = models.IntegerField(null=True, blank=True)
    team_name = models.CharField(max_length=500, blank=True)
    rj_team_id = models.IntegerField(null=True, blank=True)
    rj_league_id = models.IntegerField(null=True, blank=True)
    player_pts_season = models.DecimalField(null=True, max_digits=65535, decimal_places=65535, blank=True)
    week_num = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'football_view_weekly_stats'
        options.managed = False

