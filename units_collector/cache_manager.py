import json
from pathlib import Path
from unit import Unit
from dataclasses import asdict


class CacheManager:
    def __init__(self, folder: Path):
        self._cache_folder = folder

    @property
    def unit_file(self):
        return self._cache_folder.joinpath("units.json")

    @property
    def metadata_file(self):
        return self._cache_folder.joinpath("metadata.json")

    def save_units(self, units: dict[str, Unit]):
        if not self._cache_folder.exists():
            self._cache_folder.mkdir()
        data = [asdict(unit) for unit in units.values()]
        with self.unit_file.open("w") as f:
            json.dump(data, f, indent=2)
        print(f"Units wrote in file {self.unit_file}")

    def load_units(self) -> dict[str, Unit]:
        with self.unit_file.open() as f:
            units = json.load(f)
        return {unit["key"]: Unit(**unit) for unit in units}

    def is_cache_exists(self):
        return self.unit_file.exists()
