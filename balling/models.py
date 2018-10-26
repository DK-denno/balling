from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Leagues(models.Model):
    user = models.ForeignKey(User,related_name='league')
    name = models.CharField(max_length=10)
    dp =  models.ImageField(upload_to='images')
    captain = models.OneToOneField(User,related_name='admin',null=True)
    locale = models.CharField(max_length=20)
   
    def __str__(self):
        return self.name

class Teams(models.Model):
    name = models.CharField(max_length=50)
    league = models.ForeignKey(Leagues,related_name='teams')
    dp =  models.ImageField(upload_to='images')
   
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    league = models.ForeignKey(Leagues,related_name='users',null=True)
    dp =  models.ImageField(upload_to='images')
    bio = models.CharField(max_length=500)
    position_played = models.CharField(max_length=1000)
    phone_number = models.BigIntegerField(null=True)
    team = models.ForeignKey(Teams,related_name='team',null=True)
    
    def __str__(self):
        return self.user.username

class Message(models.Model):
    message = models.CharField(max_length=100000)
    user = models.ForeignKey(User,related_name='message')
    league = models.ForeignKey(Leagues,related_name='mess')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'from {}' .format(self.user.username)

    
class Fixtures(models.Model):
    teamA = models.ForeignKey(Teams,related_name='fixture')
    teamB = models.ForeignKey(Teams,related_name='fix')
    league = models.ForeignKey(Leagues,related_name='fixture')
    time = models.DateTimeField()

    
    def __str__(self):
        return self.league.name