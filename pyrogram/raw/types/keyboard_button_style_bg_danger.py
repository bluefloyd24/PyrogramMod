from ..object import Object


class KeyboardButtonStyleBgDanger(Object):
    """Red/danger background style for keyboard buttons.
    
    Constructor: keyboardButtonStyleBgDanger#99700f13
    """

    ID = 0x99700f13
    QUALNAME = "types.KeyboardButtonStyleBgDanger"

    def __init__(self):
        super().__init__()

    @staticmethod
    def read(b: "BytesIO", *args) -> "KeyboardButtonStyleBgDanger":
        return KeyboardButtonStyleBgDanger()

    def write(self, *args) -> bytes:
        return self.ID.to_bytes(4, "little")
