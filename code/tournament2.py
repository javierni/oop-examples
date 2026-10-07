#tournament.py

class Player:
    pass

class Tournament:
    def __init__(self):
        self._players = set()
        self._maxNumPlayers = 2

    def isPlayerAccepted(self, p: Player) -> bool:
       return p in self._players

    def getNumPlayers(self)-> int:
       return len(self._players)

    def getMaxNumPlayers(self) -> int:
       return self._maxNumPlayers

    def addPlayer(self, p: Player) -> None:
        # check precondition: !isPlayerAccepted(p)
        if  self.isPlayerAccepted(p):
            raise ValueError("the player can't be added twice")
        # check precondition:  getNumPlayers()<getMaxNumPlayers()
        if   self.getNumPlayers() == self.getMaxNumPlayers():
           raise ValueError("maximum number of players reached")
        # add player
        self._players.add(p)
        # check postcondition: isPlayerAccepted(p)
        if not self.isPlayerAccepted(p):
            raise ValueError('player not added')
        # check invariant:  getMaxNumPlayers()>0
        if self.getMaxNumPlayers() <= 0:
            raise ValueError("illegal maximum number of players")


torneo = Tournament()
jugador = Player()
torneo.addPlayer(jugador)

try:
    # no se puede incorporar 2 veces al mismo jugador
    torneo.addPlayer(jugador)
except ValueError as err:
    print('Error: ',err) # Error:  the player can't be added twice

try:
    torneo.addPlayer(Player())
    # numero maximo de jugadores alcanzado
    torneo.addPlayer(Player())
except ValueError as err:
    print('Error: ',err) # Error:  maximum number of players reached
