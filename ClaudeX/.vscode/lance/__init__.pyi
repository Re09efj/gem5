from . import stats
from .objects import *

class _Options:
    outdir: str

options: _Options

def instantiate(*args, **kwargs) -> None: ...
def simulate(*args, **kwargs): ...
