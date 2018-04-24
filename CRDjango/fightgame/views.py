from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views import View
from .models import Combat, Tournament, Fighter
from rest_framework import viewsets
from .serializers import*


class GameIndex(TemplateView):
    template_name = "game.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tournamnets'] = Tournament.objects.all()
        context['combats'] = Combat.objetcs.order_by('-date')
        context['fighters'] = Fighter.objects.all()
        return context

    """
    Una página con torneos y jugadores del torneo de forma anidada.
    Debajo ponemos lista de combates.
    Debajo ponemos lista de luchadores ordenados por el número de combates que han ganados
    """
class TournamentsView(TemplateView):
    template_name = "tournaments.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tournamnets'] = Tournament.objects.all()
        return context

class FightersView(View):
    def get(self, request):
        return HttpResponse('Luchadores')

class CombatsView(ListView):
    model = Combat
    template_name = 'combats.html'

class GameIndex(TemplateView)
    template_name = 'gameindex.html'

    def get_context_data(self, **kwargs):
        context['tournamentts'] = Tournament.objects.all()
        context ['combats'] = Combat.objet.order_by('-date')
        context ['fighter'] = Fighter.objects.all()
        return context

""" Ejemplos:

def fighters(request):
    return HttpResponse('Luchadores')

def combats(request):
    return HttpResponse('Combats')

"""

class FighterViewSet(viewsets.ModelViewSet):
    queryset = Fighter.objects.all()
    serializer_class = FighetSerializer

class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Fighter.objects.all()
    serializer_class = FighetSerializer

class CombatViewSet(viewsets.ModelViewSet):
    queryset = Fighter.objects.all()
    serializer_class = FighetSerializer

