#player.py

class League:
    def __init__(self):
        self._players = {}

    def add_player(self, nickname, player):
        if not nickname in self._players.keys():
            self._players[nickname] = player
            player.add_league(nickname, self)

class Player:

    def __init__(self):
        self._leagues = {}

    def add_league(self, nickname, league):
        if not league in self._leagues.keys():
            self._leagues[league] = nickname
            league.add_player(nickname, self)

javier = Player()
liga = League()
liga.add_player('javi', javier)
print(javier._leagues)
print(liga._players)
