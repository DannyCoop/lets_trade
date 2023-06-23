from enum import Enum

class RoomTypes(Enum):
    trade = "trade"
    store = "store"

class SurvivorStatus(Enum):
    player = "player"
    npc = "npc"