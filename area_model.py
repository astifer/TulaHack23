from typing import List, Dict

class AreaLand():

    def __init__(self, 
                cadastral_number: int,
                file_name: str) -> None:
        self.labels = ['hangar', 'house', 'pool', 'garage', 'building']
        self.cadastral_number = cadastral_number
        self.file_name = file_name

    def get_area(self)->float:
        pass