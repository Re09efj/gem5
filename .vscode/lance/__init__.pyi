from .objects import *
from . import stats

class _Options:
    outdir: str

options: _Options

def instantiate(*args, **kwargs) -> None: ...

def simulate(*args, **kwargs): ...