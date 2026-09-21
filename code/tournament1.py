#tournament1.py

class Tournament:
    def __init__(self):
        self._players = list()

    def add_player(self, player):
        if (player is not None) and (not player in self._players):
            self._players.append(player)
            player.add_tournament(self)

class Player:
    def __init__(self):
        self._tournaments = list()

    def add_tournament(self, tournament):
        if  (tournament is not None) and (not tournament in self._tournaments):
            self._tournaments.append(tournament)
            tournament.add_player(self)

jugador = Player()
torneo = Tournament()
torneo.add_player(jugador)
print(torneo, torneo._players)
print(jugador, jugador._tournaments)
torneo.add_player(None)
