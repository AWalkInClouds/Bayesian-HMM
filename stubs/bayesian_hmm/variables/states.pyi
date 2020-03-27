# Stubs for bayesian_hmm.variables.states (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import collections
from typing import Any

class State:
    ___slots__: Any = ...
    value: Any = ...
    def __init__(self, value: collections.abc.Hashable) -> Any: ...
    @property
    def special(self) -> bool: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...

class SpecialState(State):
    def __init__(self, value: str) -> Any: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...

class StartingState(SpecialState):
    def __init__(self) -> None: ...

class AggregateState(SpecialState):
    def __init__(self) -> None: ...

class MissingState(SpecialState):
    def __init__(self) -> None: ...