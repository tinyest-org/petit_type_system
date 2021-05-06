from __future__ import annotations

from abc import ABC, abstractmethod, abstractstaticmethod
from typing import Generic, TYPE_CHECKING, Any, Dict, List, Optional, Tuple, TypeVar, Union

if TYPE_CHECKING:
    from .store import TypeStore  # pragma: no cover

T = TypeVar('T')


class BaseHandler(ABC, Generic[T]):
    def __init__(self, store: TypeStore, **options):
        self.store = store

    @abstractmethod
    def should_handle(self, cls: Any,
                      origin: Optional[type], args: List[Any]) -> bool:
        ...

    @abstractmethod
    def build(self, cls: T, origin: Optional[type],
              args: List[Any], is_mapping_key: bool) -> Tuple[Optional[str], Union[str, Dict[str, Any]]]:
        ...


class BasicHandler(BaseHandler[T]):
    @abstractmethod
    def build(self, cls: T, origin: Optional[type],
              args: List[Any], is_mapping_key: bool) -> Tuple[Optional[str], str]:
        ...


class ClassHandler(BaseHandler[T]):
    @abstractmethod
    def is_mapping(self) -> bool:
        ...

    @abstractmethod
    def build(self, cls: T, origin: Optional[type],
              args: List[Any], is_mapping_key: bool) -> Tuple[Optional[str], Union[str, Dict[str, Any]]]:
        ...


class StructHandler(ABC):
    def __init__(self, store: TypeStore, **options):
        self.store = store

    def make_inline_struct(self, cls: Any, fields: Dict[str, Any]) -> str:
        raise NotImplementedError('The transcripter does not support inline types')

    @abstractmethod
    def make_struct(self, cls: Any, name: str, fields: Dict[str, Any]) -> str:
        ...
