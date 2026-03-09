from io import BytesIO
from typing import Any
from pyrogram.raw.core.primitives import Int
from pyrogram.raw.core import TLObject


class KeyboardButtonStyleBgDanger(TLObject):  # type: ignore
    """Red/danger background style for keyboard buttons."""

    __slots__ = []

    ID = 0x99700f13
    QUALNAME = "types.KeyboardButtonStyleBgDanger"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonStyleBgDanger":
        return KeyboardButtonStyleBgDanger()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        return b.getvalue()
