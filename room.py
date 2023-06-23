from uuid import uuid4
from utils import RoomTypes
from typing import List
class Room:
    def __init__(self, room_name: str, type: RoomTypes) -> None:
        self.id: str = str(uuid4())
        self.name = room_name
        self.room_type = type
        self.player_list: List = []
    