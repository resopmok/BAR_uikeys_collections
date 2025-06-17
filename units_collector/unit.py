from dataclasses import dataclass, asdict


@dataclass
class Unit:
    key: str
    name: str
    faction: str
    unit_type: str
    unit_group: str
    tier: str
    description: str
    metal_cost: int
    energy_cost: int
    builder: bool
    can_move: bool
    can_fly: bool
    can_capture: bool
    can_attack: bool
    has_weapon: bool
    categories: list[str]
    build_options: list[str]
    energy_make: int
    energy_storage: int
    metal_make: int
    metal_storage: int

    @property
    def is_factory(self):
        return self.build_options and self.is_building

    @property
    def is_engineer(self):
        return self.build_options and not self.is_building

    @property
    def is_building(self):
        return self.unit_type == "building"

    @property
    def is_aircraft(self):
        return self.can_fly and not self.is_building

    @property
    def is_commander(self):
        return self.key in ["armcom", "corcom"]

    @property
    def builder_type(self):
        if self.is_factory:
            return "factory"
        elif self.is_engineer:
            return "engineer"
        elif self.is_building:
            return "building"
        else:
            return "unknown"

    def __str__(self):
        result = f"{self.tier} {self.unit_type} '{self.name}' ({self.key})"
        return result

    def __repr__(self):
        result = ""
        for k, v in asdict(self).items():
            if v:
                if result:
                    result += ", "
                if isinstance(v, str):
                    result += f"{k}='{v}'"
                else:
                    result += f"{k}={v}"
        return f"Unit({result})"
