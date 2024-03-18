from unit import Unit
from typing import Optional


class Binding:
    def __init__(
        self, shortcut: Optional[str], unit: Optional[Unit], comment: str = ""
    ):
        self.shortcut = shortcut
        self.unit = unit
        self.comment = comment

    def __repr__(self):
        return f"Binding({self.shortcut}, {repr(self.unit)})"

    def format_line(self):
        if self.unit:
            return f"bind{self.shortcut:>20} buildunit_{self.unit.key:<27}// {self.unit.name} ({self.unit.description}){self.comment}"
        elif self.comment:
            return f"// {self.comment}"
        else:
            return ""
