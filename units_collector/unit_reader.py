from pathlib import Path
from typing import Optional
import os
import copy
from slpp import slpp as lua
from unit import Unit
from metadata import Metadata


class UnitReader:
    def __init__(self, units_folder: Path, metadata: Metadata):
        self._units_folder = units_folder
        self._metadata = metadata

    def load_units(self) -> dict[str, Unit]:
        lua_files = self._collect_lua_files(self._units_folder)
        units = self._load_all_units(lua_files)
        return units

    @classmethod
    def _collect_lua_files(cls, units_folder: Path) -> list[Path]:
        lua_files = []
        for root, dirs, files in os.walk(units_folder):
            for file in files:
                if file.endswith(".lua"):
                    lua_files.append(Path(root, file))
        return lua_files

    def _load_all_units(self, lua_files: list[Path]) -> dict[str, Unit]:
        result = {}
        for lua_file in lua_files:
            unit = self._load_units_data_from_lua(lua_file)
            if not unit:
                continue
            unit = self._update_unit_from_path(unit, lua_file)
            if not unit:
                continue
            unit = self._update_unit_from_metadata(unit)
            self._fix_tier(unit)
            result[unit.key] = unit
        self._make_cormine4(result)
        return result

    def _update_unit_from_metadata(self, unit: Unit) -> Unit:
        unit.name = self._metadata.get_name(unit.key) or unit.key
        unit.description = self._metadata.get_description(unit.key)
        unit.faction = self._metadata.get_faction(unit.faction)
        return unit

    @staticmethod
    def _fix_tier(unit: Unit):
        if not unit.name:
            return
        if unit.name.startswith("T2") or unit.name.startswith("Advanced"):
            if unit.name != "Advanced Solar Collector":
                unit.tier = "T2"

    def _make_cormine4(self, units: dict[str, Unit]):
        cormine4 = copy.deepcopy(units["cormine2"])
        cormine4.key = "cormine4"
        self._update_unit_from_metadata(cormine4)
        units[cormine4.key] = cormine4

    @classmethod
    def _load_units_data_from_lua(cls, lua_file: Path) -> Optional[Unit]:
        try:
            data = cls._load_lua(lua_file)
            unit = cls._make_unit_from_lua_data(data)
            return unit
        except Exception as e:
            print(f"Error while loading {lua_file}: {e}")
        return None

    @staticmethod
    def _load_lua(lua_file):
        with open(lua_file, "r") as f:
            content = f.read()
        content = content[content.find("{") : content.rfind("}") + 1]
        return lua.decode(content)

    @classmethod
    def _make_unit_from_lua_data(cls, data: dict) -> Unit:
        key = list(data.keys())[0]
        unit_data = data[key]
        build_options = unit_data.get("buildoptions", [])
        if isinstance(build_options, dict):
            build_options = list(build_options.values())
        tech_level = unit_data.get("customparams", {}).get("techlevel", "")
        if tech_level:
            tier = f"T{tech_level}"
        else:
            tier = ""
        return Unit(
            key=key,
            name=key,
            description="",
            unit_type="",
            unit_group=unit_data.get("customparams", {}).get("unitgroup", ""),
            faction="",
            tier=tier,
            metal_cost=unit_data.get(
                "metalcost", unit_data.get("buildcostmetal", None)
            ),
            energy_cost=unit_data.get(
                "energycost", unit_data.get("buildcostenergy", None)
            ),
            builder=unit_data.get("builder", False),
            can_move=unit_data.get("canmove", False),
            can_fly=unit_data.get("canfly", False),
            can_capture=unit_data.get("cancapture", False),
            can_attack=unit_data.get("canattack", False),
            has_weapon=unit_data.get("weapons") and True or False,
            categories=unit_data.get("category", "").split(" "),
            build_options=build_options,
            metal_make=unit_data.get("metalmake", 0),
            metal_storage=unit_data.get("metalstorage", 0),
            energy_make=unit_data.get("energymake", 0),
            energy_storage=unit_data.get("energystorage", 0),
        )

    @classmethod
    def _update_unit_from_path(cls, unit: Unit, lua_file: Path) -> Optional[Unit]:
        cls._update_tier(unit, lua_file)
        category_folder = lua_file.parent
        while category_folder.name.lower() != "units":
            dir_name = category_folder.name.lower()
            if dir_name == "other":
                return None
            elif dir_name.startswith("arm") or dir_name.startswith("cor"):
                cls._update_cor_arm_unit(unit, dir_name)
                break
            elif dir_name in ["legion", "scavengers"]:
                unit = cls._update_legion_commander(unit, lua_file)
                break
            elif category_folder.parent.name.lower() in ["legion", "scavengers"]:
                cls._update_legion_scavengers_units(unit, category_folder)
                break
            category_folder = category_folder.parent
        else:
            unit = cls._update_commanders(unit, lua_file)
        return unit

    @staticmethod
    def _update_tier(unit: Unit, lua_file: Path):
        if unit.tier:
            return
        dir_name = lua_file.parent.name.lower()
        if dir_name.startswith("t2"):
            unit.tier = "T2"
        elif dir_name.endswith("gantry") or dir_name.startswith("t3"):
            unit.tier = "T3"
        else:
            unit.tier = "T1"

    @staticmethod
    def _update_cor_arm_unit(unit: Unit, dir_name: str):
        unit_type = dir_name[3:]
        if unit_type == "gantry":
            unit.unit_type = "experimental"
        elif unit_type.endswith("s"):
            unit.unit_type = unit_type[:-1]
        else:
            unit.unit_type = unit_type
        unit.faction = dir_name[:3]

    @staticmethod
    def _update_legion_scavengers_units(unit: Unit, category_folder: Path):
        unit.unit_type = category_folder.name.lower()
        unit.faction = category_folder.parent.name.lower()

    @staticmethod
    def _update_legion_commander(unit: Unit, lua_file: Path) -> Optional[Unit]:
        file_name = lua_file.name.lower()[0:-4]
        if not file_name.startswith("legcom"):
            return None
        unit.unit_type = "commander"
        unit.faction = lua_file.parent.name.lower()
        level = file_name[6:]
        if level:
            unit.tier = f"T{level[-1]}"
        else:
            unit.tier = "T1"
        return unit

    @staticmethod
    def _update_commanders(unit: Unit, lua_file: Path) -> Optional[Unit]:
        file_name = lua_file.name.lower()[0:-4]
        if file_name == "armcom":
            unit.unit_type = "commander"
            unit.faction = "arm"
            unit.tier = "T1"
        elif file_name == "corcom":
            unit.unit_type = "commander"
            unit.faction = "cor"
            unit.tier = "T1"
        else:
            print(f"Error while parsing {lua_file}: no unit type found")
            return None
        return unit
