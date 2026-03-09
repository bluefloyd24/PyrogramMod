from io import BytesIO
from typing import Any
from pyrogram.raw.core.primitives import Int
from pyrogram.raw.core import TLObject


class KeyboardButtonStyleBgSuccess(TLObject):  # type: ignore
    """Green/success background style for keyboard buttons."""

    __slots__ = []

    ID = 0x8a0d5de7
    QUALNAME = "types.KeyboardButtonStyleBgSuccess"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonStyleBgSuccess":
        return KeyboardButtonStyleBgSuccess()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))
        return b.getvalue()
