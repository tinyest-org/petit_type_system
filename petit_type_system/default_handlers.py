from __future__ import annotations

from dataclasses import is_dataclass
from enum import Enum
from typing import (TYPE_CHECKING, Any, List, Literal, Optional,
                    Union)

from .base_handler import BasicHandler, ClassHandler
from .named_types import NamedLiteral, NamedUnion


class UnionHandler(BasicHandler):
    def should_handle(self, cls, origin, args) -> bool:
        return origin in (NamedUnion, Union)


class LiteralHandler(BasicHandler):
    def should_handle(self, cls, origin, args) -> bool:
        return origin in (Literal, NamedLiteral)


class EnumHandler(ClassHandler[Enum]):
    def should_handle(self, cls: type, origin, args) -> bool:
        return issubclass(cls, Enum)


class DataclassHandler(ClassHandler):
    def is_mapping(self) -> bool:
        return True

    def should_handle(self, cls: type, origin, args) -> bool:
        return is_dataclass(cls)


class TupleHandler(BasicHandler):
    def should_handle(self, cls: Any, origin: Optional[type], args: List[Any]) -> bool:
        return origin is tuple


class ArrayHandler(BasicHandler):
    def should_handle(self, cls: Any, origin: Optional[type], args: List[Any]) -> bool:
        return origin == list and len(args) == 1


class MappingHandler(BasicHandler):
    def should_handle(self, cls: Any, origin: Optional[type], args: List[Any]) -> bool:
        return origin == dict and len(args) == 2
