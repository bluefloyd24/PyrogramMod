from io import BytesIO
from typing import Any
from pyrogram.raw.core.primitives import Int
from pyrogram.raw.core import TLObject


class KeyboardButtonStyleBgPrimary(TLObject):  # type: ignore
    """Blue/primary background style for keyboard buttons."""

    __slots__ = []

    ID = 0xa3c61f72
    QUALNAME = "types.KeyboardButtonStyleBgPrimary"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonStyleBgPrimary":
        return KeyboardButtonStyleBgPrimary()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        return b.getvalue()
