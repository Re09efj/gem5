import inspect
from pathlib import Path

import m5.objects

out = Path("gem5_objects.pyi")

with out.open("w") as f:
    f.write("from typing import Any\n\n")

    for name in sorted(dir(m5.objects)):
        if name.startswith("_"):
            continue

        try:
            obj = getattr(m5.objects, name)
        except Exception:
            continue

        if not inspect.isclass(obj):
            continue

        bases = [
            b.__name__
            for b in obj.__bases__
            if b.__name__ != "object"
        ]

        if bases:
            f.write(
                f"class {name}({', '.join(bases)}):\n"
            )
        else:
            f.write(f"class {name}:\n")

        try:
            params = obj._params.keys()

            for p in params:
                f.write(f"    {p}: Any\n")

        except Exception:
            pass

        f.write("\n")
        f.write("    def __init__(self, *args, **kwargs) -> None: ...\n")
        f.write("\n\n")

print("generated:", out)