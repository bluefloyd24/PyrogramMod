from ..object import Object


class KeyboardButtonStyleBgPrimary(Object):
    """Blue/primary background style for keyboard buttons.
    
    Constructor: keyboardButtonStyleBgPrimary#a3c61f72
    """

    ID = 0xa3c61f72
    QUALNAME = "types.KeyboardButtonStyleBgPrimary"

    def __init__(self):
        super().__init__()

    @staticmethod
    def read(b: "BytesIO", *args) -> "KeyboardButtonStyleBgPrimary":
        return KeyboardButtonStyleBgPrimary()

    def write(self, *args) -> bytes:
        return self.ID.to_bytes(4, "little")
