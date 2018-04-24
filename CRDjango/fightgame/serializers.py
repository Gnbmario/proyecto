from rest_framework import serializers

from .models import Tournament, Combat, Fighter


class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tournament
        fields = ('name', 'start_date', 'end_date', 'category')

class CombatSerializer(serializers.HyperlinkedModelSerializer)
    class Meta:
        model = Combat
        fields = ('date', 'loser', 'winner')

class FighetSerializer(serializers.HyperlinkedModelSerializer)
    class Meta:
        model = Fighter
        fields = ('alias', 'skill', 'force', 'resistance')