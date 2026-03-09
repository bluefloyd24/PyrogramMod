import struct


class KeyboardButtonStyle:
    """Style object untuk keyboard button — warna background.

    Parameters:
        bg_primary (``bool``, *optional*):
            Warna biru (primary).

        bg_danger (``bool``, *optional*):
            Warna merah (danger).

        bg_success (``bool``, *optional*):
            Warna hijau (success).

    Example:
        .. code-block:: python

            from pyrogram.types import KeyboardButtonStyle

            style = KeyboardButtonStyle(bg_primary=True)
            style = KeyboardButtonStyle(bg_danger=True)
            style = KeyboardButtonStyle(bg_success=True)
    """

    # Constructor IDs dari Telegram TL schema (little-endian 4 bytes)
    _ID_PRIMARY = 0xa3c61f72
    _ID_DANGER  = 0x99700f13
    _ID_SUCCESS = 0x8a0d5de7

    def __init__(
        self,
        bg_primary: bool = False,
        bg_danger:  bool = False,
        bg_success: bool = False,
    ):
        self.bg_primary = bg_primary
        self.bg_danger  = bg_danger
        self.bg_success = bg_success

    def write(self) -> bytes | None:
        """
        Serialize langsung ke bytes yang dikirim ke Telegram server.
        Return None jika tidak ada style yang di-set.
        """
        if self.bg_primary:
            return struct.pack("<I", self._ID_PRIMARY)
        if self.bg_danger:
            return struct.pack("<I", self._ID_DANGER)
        if self.bg_success:
            return struct.pack("<I", self._ID_SUCCESS)
        return None
