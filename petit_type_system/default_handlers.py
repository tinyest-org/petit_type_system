from __future__ import annotations

from dataclasses import is_dataclass
from enum import Enum
from typing import (TYPE_CHECKING, Any, List, Literal, Optional,
                    Union)

from .base_handler import BasicHandler, ClassHandler
from .named_types import NamedLiteral, NamedUnion

if TYPE_CHECKING:
    from .store import TypeStore  # pragma: no cover


class UnionHandler(BasicHandler):
    @staticmethod
    def should_handle(cls, store: TypeStore, origin, args) -> bool:
        return origin in (NamedUnion, Union)


class LiteralHandler(BasicHandler):
    @staticmethod
    def should_handle(cls, store: TypeStore, origin, args) -> bool:
        return origin in (Literal, NamedLiteral)


class EnumHandler(ClassHandler[Enum]):

    @staticmethod
    def should_handle(cls: type, store: TypeStore, origin, args) -> bool:
        return issubclass(cls, Enum)


class DataclassHandler(ClassHandler):
    @staticmethod
    def is_mapping() -> bool:
        return True

    @staticmethod
    def should_handle(cls: type, store: TypeStore, origin, args) -> bool:
        return is_dataclass(cls)


class TupleHandler(BasicHandler):
    @staticmethod
    def should_handle(cls: Any, store: TypeStore, origin: Optional[type], args: List[Any]) -> bool:
        return origin is tuple


class ArrayHandler(BasicHandler):
    @staticmethod
    def should_handle(cls: Any, store: TypeStore, origin: Optional[type], args: List[Any]) -> bool:
        return origin == list and len(args) == 1


class MappingHandler(BasicHandler):
    @staticmethod
    def should_handle(cls: Any, store: TypeStore, origin: Optional[type], args: List[Any]) -> bool:
        return origin == dict and len(args) == 2
