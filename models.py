# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MiniFbProfile(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    city = models.TextField()
    email_address = models.TextField()
    profile_img_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'mini_fb_profile'


class MiniFbProfileFriends(models.Model):
    from_profile = models.ForeignKey(MiniFbProfile, models.DO_NOTHING)
    to_profile = models.ForeignKey(MiniFbProfile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mini_fb_profile_friends'
        unique_together = (('from_profile', 'to_profile'),)


class MiniFbStatusmessage(models.Model):
    timestamp = models.TimeField()
    message = models.TextField()
    profile = models.ForeignKey(MiniFbProfile, models.DO_NOTHING)
    image_file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'mini_fb_statusmessage'


class ProjectAppointment(models.Model):
    date = models.DateField(blank=True, null=True)
    client = models.ForeignKey('ProjectClient', models.DO_NOTHING)
    doctor = models.ForeignKey('ProjectDoctor', models.DO_NOTHING)
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'project_appointment'


class ProjectClient(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    city = models.TextField()
    email_address = models.TextField()
    profile_img_url = models.CharField(max_length=200)
    blood_type = models.TextField()
    date_of_birth = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_client'


class ProjectDailylog(models.Model):
    time = models.TimeField()
    date = models.DateField(blank=True, null=True)
    oxygen_level = models.TextField(db_column='Oxygen_level')  # Field name made lowercase.
    emotions = models.TextField()
    comments = models.TextField(db_column='Comments')  # Field name made lowercase.
    client = models.ForeignKey(ProjectClient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_dailylog'


class ProjectDoctor(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    address = models.TextField()
    city = models.TextField()
    email_address = models.TextField()
    profile_img_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'project_doctor'


class ProjectProfile(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    city = models.TextField()
    email_address = models.TextField()
    profile_img_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'project_profile'


class ProjectProfileFriends(models.Model):
    from_profile = models.ForeignKey(ProjectProfile, models.DO_NOTHING)
    to_profile = models.ForeignKey(ProjectProfile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_profile_friends'
        unique_together = (('from_profile', 'to_profile'),)


class ProjectStatusmessage(models.Model):
    timestamp = models.TimeField()
    message = models.TextField()
    image_file = models.CharField(max_length=100)
    client = models.ForeignKey(ProjectClient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_statusmessage'


class QuotesImage(models.Model):
    image_url = models.CharField(max_length=200)
    person = models.ForeignKey('QuotesPerson', models.DO_NOTHING)
    image_file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'quotes_image'


class QuotesPerson(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'quotes_person'


class QuotesQuote(models.Model):
    text = models.TextField()
    person = models.ForeignKey(QuotesPerson, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'quotes_quote'
