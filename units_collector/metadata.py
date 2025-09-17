import json
from pathlib import Path
import requests


class Metadata:
    def __init__(self, names, factions, descriptions):
        self.names = names
        self.factions = factions
        self.descriptions = descriptions

    def get_name(self, key: str):
        return self.names.get(key)

    def get_faction(self, key: str):
        return self.factions.get(key)

    def get_description(self, key: str):
        return self.descriptions.get(key)


def load_metadata() -> Metadata:
    url = "https://raw.githubusercontent.com/beyond-all-reason/Beyond-All-Reason/master/language/en/units.json"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch unit names from github")
    data = response.json()
    names = data.get("units").get("names")
    factions = data.get("units").get("factions")
    descriptions = data.get("units").get("descriptions")
    return Metadata(names, factions, descriptions)
