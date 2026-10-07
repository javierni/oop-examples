# vip.py
from typing import Protocol

# definition of interface in Python
class SeatImplementation(Protocol):
    def getPosition(self) -> int:
        pass
    def setPosition(self, newPosition:int) -> None:
        pass

class StubCode:
    def getPosition(self) -> int:
        return 15 # stub code for GetPosition
    def setPosition(self, newPosition:int) -> None:
        pass

class AimSeat:
    def getPosition(self) -> int:
        # actual call to the Adaptative Information Manager (AIM) system
        pass

class SARTSeat: 
    def getPosition(self) -> int:
        # actual call to the Seat Access Real Time (SART) system
        pass

class Seat:
    def __init__(self, imp: SeatImplementation):
        self._imp = imp
    def getPosition(self) -> int:
        return self._imp.getPosition()
    def setPosition(self, newPosition:int) -> None:
        self._imp.setPosition(newPosition)

class VIP:
    def __init__(self, seat: Seat):
        self._seat = seat
    def display_position(self):
        print(f"The seat back recline is {self._seat.getPosition()} degrees from the vertical.")

vip = VIP(Seat(StubCode()))
vip.display_position() # The seat back recline is 15 degrees from the vertical.
