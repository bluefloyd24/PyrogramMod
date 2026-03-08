from ..object import Object


class KeyboardButtonStyleBgSuccess(Object):
    """Green/success background style for keyboard buttons.
    
    Constructor: keyboardButtonStyleBgSuccess#8a0d5de7
    """

    ID = 0x8a0d5de7
    QUALNAME = "types.KeyboardButtonStyleBgSuccess"

    def __init__(self):
        super().__init__()

    @staticmethod
    def read(b: "BytesIO", *args) -> "KeyboardButtonStyleBgSuccess":
        return KeyboardButtonStyleBgSuccess()

    def write(self, *args) -> bytes:
        return self.ID.to_bytes(4, "little")
