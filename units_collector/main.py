from pathlib import Path
from unit_reader import UnitReader
from metadata import load_metadata
from cache_manager import CacheManager
from key_binding_writer import KeyBindingWriter
from key_binding_generator import KeyBindingGenerator


if __name__ == "__main__":
    this_folder = Path(__file__).parent
    cache_folder = this_folder.joinpath("cache")
    output_folder = this_folder.joinpath("output")
    if not output_folder.exists():
        output_folder.mkdir()

    cm = CacheManager(cache_folder)
    if cm.is_cache_exists():
        units = cm.load_units()
    else:
        bar_folder = this_folder.parent.parent.joinpath("Beyond-All-Reason")
        units_folder = bar_folder.joinpath("units")
        if not bar_folder.exists():
            raise FileNotFoundError(
                f"You need to clone Beyond-All-Reason repository in {bar_folder}"
            )
        metadata = load_metadata()
        unit_reader = UnitReader(units_folder, metadata)
        units = unit_reader.load_units()
        cm.save_units(units)

    binding_generator = KeyBindingGenerator(units)
    bindings = binding_generator.generate_bindings()
    binding_writer = KeyBindingWriter()
    output = output_folder.joinpath("build_cycle_constructions.txt")
    binding_writer.write_bindings(output, bindings)

    categories = set()
    for unit in units.values():
        categories |= set(unit.categories)
    categories = list(categories)
    categories.sort()
    categories_output = output_folder.joinpath("categories.txt")
    with categories_output.open("w") as f:
        f.write("\n".join(categories))
