from django.contrib import admin

from fightgame.models import *

class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'finish_date']
    list_filter = ['name']
    search_fields = ['start_date', 'finish_date']
    
class FighterAdmin(admin.ModelAdmin):
    list_display = ['alias', 'skills', 'force', 'resistance']
    search_fields = ['alias']

class CombatAdmin(admin.ModelAdmin):
    list_display = ['__str__' ,'tournament', 'date', 'fighter1', 'fighter2']
    list_filter = []
    search_fields = ['tournament', 'date']

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Fighter, FighterAdmin)
admin.site.register(Combat, CombatAdmin)

