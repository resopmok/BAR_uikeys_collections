from unit import Unit
from binding import Binding
from functools import cmp_to_key


class KeyBindingGenerator:
    def __init__(self, units: dict[str, Unit]):
        self._units = units

    def generate_bindings(self) -> list[Binding]:
        bindings = [
            self._comment(
                "This file helps you to cycle throught different construction with hotkeys"
            ),
            self._comment(
                "To use it, copy/past the sections you want in your uikeys.txt, and comment/uncomment units which interest you."
            ),
            self._comment("Categories:"),
            self._comment("z: metal related constructions"),
            self._comment("x: energy related constructions"),
            self._comment("c: utilities related constructions"),
            self._comment("v: defense related constructions"),
            self._comment("b: factory constructions"),
            self._comment(""),
        ]
        bindings += self._generate_title("Cycle through metal related constructions")
        bindings += self._generate_metal_bindings("sc_z")
        bindings += self._generate_title("Cycle through energy related constructions")
        bindings += self._generate_energy_bindings("sc_x")
        bindings += self._generate_title(
            "Cycle through utilities constructions (radars, jammers & co)"
        )
        bindings += self._generate_utilities_bindings("sc_c")
        bindings += self._generate_title(
            "Cycle through defensive turrets constructions"
        )
        bindings += self._generate_turret_bindings("sc_v")
        bindings += self._generate_title("Cycle through factories")
        bindings += self._generate_factory_bindings("sc_b")
        return bindings

    def _generate_metal_bindings(self, shortcut) -> list[Binding]:
        def selector(unit: Unit) -> bool:
            return (
                unit.faction in ["Armada", "Cortex"]
                and (
                    unit.metal_storage
                    and unit.metal_storage > 0
                    and not unit.is_factory
                    and not unit.is_commander
                )
                or ("Energy Converter" in unit.name)
            )

        bindings = self._generate_cycle(shortcut, selector)
        self._sort_binding(bindings, ["tier", "metal_cost", "name", "faction"])
        return bindings

    def _generate_energy_bindings(self, shortcut) -> list[Binding]:
        def selector(unit: Unit) -> bool:
            return (
                unit.faction in ["Armada", "Cortex"]
                and unit.energy_storage
                and unit.energy_storage > 0
                and not unit.can_move
                and not unit.is_factory
                and (not unit.has_weapon or unit.energy_make)
                and not unit.is_commander
            )

        bindings = self._generate_cycle(shortcut, selector)
        self._sort_binding(bindings, ["tier", "metal_cost", "name", "faction"])
        return bindings

    def _generate_utilities_bindings(self, shortcut) -> list[Binding]:
        def selector(unit: Unit) -> bool:
            return (
                unit.faction in ["Armada", "Cortex"]
                and unit.is_building
                and ("NOWEAPON" in unit.categories or "nuke" in unit.unit_group)
                and not unit.energy_storage
                and not unit.metal_storage
                and not unit.is_factory
                and "Energy Converter" not in unit.name
                and not unit.builder
            ) or unit.name in ["Juno", "Catalyst", "Keeper", "Overseer"]

        bindings = self._generate_cycle(shortcut, selector)
        self._sort_binding(bindings, ["tier", "metal_cost", "name", "faction"])
        return bindings

    def _generate_turret_bindings(self, shortcut) -> list[Binding]:
        def selector(unit: Unit) -> bool:
            return (
                unit.faction in ["Armada", "Cortex"]
                and unit.is_building
                and unit.has_weapon
                and not unit.metal_storage
                and not unit.energy_make
                and "NOWEAPON" not in unit.categories
                and unit.unit_group != "explo"
                and "nuke" not in unit.unit_group
                and unit.name not in ["Juno", "Catalyst"]
            )

        bindings = self._generate_cycle(shortcut, selector)
        self._sort_binding(bindings, ["tier", "metal_cost", "name", "faction"])
        return bindings

    def _generate_factory_bindings(self, shortcut) -> list[Binding]:
        def selector(unit: Unit) -> bool:
            return (
                unit.faction in ["Armada", "Cortex"]
                and unit.is_building
                and unit.builder
            )

        bindings = self._generate_cycle(shortcut, selector)
        self._sort_binding(bindings, ["tier", "metal_cost", "name", "faction"])
        return bindings

    @staticmethod
    def _sort_binding(bindings: list[Binding], attribute_orders: list):
        def comparer(a: Binding, b: Binding):
            if a.unit == b.unit:
                return a.shortcut < b.shortcut
            for attribute in attribute_orders:
                a_value = getattr(a.unit, attribute)
                b_value = getattr(b.unit, attribute)
                if a_value != b_value:
                    return -1 if a_value < b_value else 1
            return a.unit.key < b.unit.key

        bindings.sort(key=cmp_to_key(comparer))

    @classmethod
    def _prepend_title(cls, bindings: list[Binding], title: str) -> list[Binding]:
        return cls._generate_title(title) + bindings

    @classmethod
    def _generate_title(cls, title: str):
        return [
            cls._comment(""),
            cls._comment("=" * 30),
            cls._comment(title),
            cls._comment("=" * 30),
        ]

    @staticmethod
    def _comment(comment) -> Binding:
        return Binding(unit=None, shortcut=None, comment=comment)

    def _generate_cycle(self, shortcut: str, selector) -> list[Binding]:
        result = []
        for unit in self._units.values():
            if selector(unit):
                result.append(Binding(shortcut, unit))
                result.append(Binding("Shift+" + shortcut, unit))
        return result
