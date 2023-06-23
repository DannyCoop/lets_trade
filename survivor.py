from uuid import uuid4
from utils import SurvivorStatus
from item import item

class Survivor:
    def __init__(self, name: str, status: SurvivorStatus) -> None:
        self.id: str = str(uuid4())
        self.name = name
        self.status = status
        self.inventory = []

    def add_to_inventroy(self, item_to_add: item) -> None:
        self.inventory.append(item_to_add)

    def show_items(self) -> None:
        for item in self.inventory:
            print(item)
