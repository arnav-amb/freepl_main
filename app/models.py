from django.contrib.auth.models import User
from django.db import models
import datetime

from django.contrib import admin

class Person(models.Model):
    class Meta:
        db_table = 'person'

    user = models.OneToOneField(User)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,default="")
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Match(models.Model):
    class Meta:
        db_table = 'match'

    country1 = models.TextField(max_length=100, default="")
    country2 = models.TextField(max_length=100, default="")
    day = models.DateField(default=datetime.datetime.today())
    can_edit = models.BooleanField(default=True)

    def __str__(self):
        return self.country1 + ' vs ' + self.country2 

class Player(models.Model):
    class Meta:
        db_table = 'player'

    name = models.TextField(max_length=30, default="")
    country = models.TextField(max_length=100, default="")
    cost = models.IntegerField(default=0)
    role = models.TextField(max_length=25,default="")

    def __str__(self):
        return self.name

class PlayertoMatch(models.Model):
    class Meta:
        db_table = 'PlayertoMatch'

    match = models.ForeignKey(Match)
    player = models.ForeignKey(Player)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.player.name + "for the match " + self.match.country1 + 'vs' + self.match.country2 + str(self.match.day) + "scored : " + str(self.score)

class PersontoPM(models.Model):
    class Meta:
        db_table = 'person_PM'

    person = models.ForeignKey(Person)
    pm = models.ForeignKey(PlayertoMatch)
    power_player = models.BooleanField(default=False)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.person.name + ' ' + self.pm.match.__str__() + ' ' + self.pm.player.name

admin.site.register(Player)
admin.site.register(Person)
admin.site.register(PersontoPM)
admin.site.register(Match)
admin.site.register(PlayertoMatch)
