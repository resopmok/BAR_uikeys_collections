import pytest

from unit import Unit
from binding import Binding
from key_binding_generator import KeyBindingGenerator
from pathlib import Path
from cache_manager import CacheManager


def make_unit(
    key: str = "",
    name: str = "",
    faction: str = "",
    unit_type: str = "",
    unit_group: str = "",
    tier: str = "",
    description: str = "",
    metal_cost: int = 0,
    energy_cost: int = 0,
    builder: bool = "",
    can_move: bool = "",
    can_fly: bool = False,
    can_capture: bool = False,
    can_attack: bool = False,
    has_weapon: bool = False,
    categories: list = [],
    build_options: list = [],
    energy_make: int = 0,
    energy_storage: int = 0,
    metal_make: int = 0,
    metal_storage: int = 0,
):
    if not faction:
        if key[0] == "a":
            faction = "Armada"
        else:
            faction = "Cortex"
    return Unit(
        key=key,
        name=name,
        faction=faction,
        unit_type=unit_type,
        unit_group=unit_group,
        tier=tier,
        description=description,
        metal_cost=metal_cost,
        energy_cost=energy_cost,
        builder=builder,
        can_move=can_move,
        can_fly=can_fly,
        can_capture=can_capture,
        can_attack=can_attack,
        has_weapon=has_weapon,
        categories=categories,
        build_options=build_options,
        energy_make=energy_make,
        energy_storage=energy_storage,
        metal_make=metal_make,
        metal_storage=metal_storage,
    )


def make_units(units: list[Unit]):
    return {unit.key: unit for unit in units}


def test_metal_sorting():
    units = make_units(
        [
            make_unit(key="aa", tier="T1", metal_cost=10, metal_storage=10),
            make_unit(key="ab", tier="T2", metal_cost=20, metal_storage=10),
            make_unit(key="ac", tier="T1", metal_cost=30, metal_storage=10),
            make_unit(key="ca", tier="T1", metal_cost=10, metal_storage=10),
            make_unit(key="cb", tier="T2", metal_cost=20, metal_storage=10),
            make_unit(key="cc", tier="T1", metal_cost=29, metal_storage=10),
        ]
    )
    key_binding_generator = KeyBindingGenerator(units)
    bindings = key_binding_generator.generate_bindings()
    computed = [b.unit for b in bindings if not b.shortcut.startswith(("Shift"))]
    expected = [
        make_unit(key="aa", tier="T1", metal_cost=10, metal_storage=10),
        make_unit(key="ca", tier="T1", metal_cost=10, metal_storage=10),
        make_unit(key="cc", tier="T1", metal_cost=29, metal_storage=10),
        make_unit(key="ac", tier="T1", metal_cost=30, metal_storage=10),
        make_unit(key="ab", tier="T2", metal_cost=20, metal_storage=10),
        make_unit(key="cb", tier="T2", metal_cost=20, metal_storage=10),
    ]
    assert expected == computed
