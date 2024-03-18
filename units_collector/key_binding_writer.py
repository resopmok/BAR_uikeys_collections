from binding import Binding
from pathlib import Path


class KeyBindingWriter:

    def write_bindings(self, output: Path, bindings: list[Binding]):
        with output.open("w") as f:
            for binding in bindings:
                line = binding.format_line() + "\n"
                f.write(line)
