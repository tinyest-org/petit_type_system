"""
Special added types
"""

from typing import Any, Final, Union

INLINE_TOKEN: Final = "__inline__"

NoneType = type(None)


pseudo_classes = Union[dict, None, Any]

BASIC_TYPES = Union[int, str, float, bool, None]


class undefined:
    """
    to use like undefined in typescript
    """
    ...


class null:
    """
    to use like null in typescript
    """
    ...
