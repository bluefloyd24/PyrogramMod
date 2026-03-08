from pyrogram.raw.types import (
    KeyboardButtonStyleBgDanger,
    KeyboardButtonStyleBgPrimary,
    KeyboardButtonStyleBgSuccess,
)


class KeyboardButtonStyle:
    """Style object untuk keyboard button — mendukung warna background dan custom emoji icon.

    Parameters:
        bg_primary (``bool``, *optional*):
            Warna biru (primary). Default False.

        bg_danger (``bool``, *optional*):
            Warna merah (danger). Default False.

        bg_success (``bool``, *optional*):
            Warna hijau (success). Default False.

        icon (``int``, *optional*):
            Custom emoji ID untuk icon di tombol.

    Example:
        .. code-block:: python

            from pyrogram.types import KeyboardButtonStyle

            # Primary (biru)
            style = KeyboardButtonStyle(bg_primary=True)

            # Danger (merah)
            style = KeyboardButtonStyle(bg_danger=True)

            # Success (hijau)
            style = KeyboardButtonStyle(bg_success=True)

            # Custom emoji icon
            style = KeyboardButtonStyle(icon=5368324170671202286)
    """

    def __init__(
        self,
        bg_primary: bool = False,
        bg_danger: bool = False,
        bg_success: bool = False,
        icon: int = None,
    ):
        self.bg_primary = bg_primary
        self.bg_danger  = bg_danger
        self.bg_success = bg_success
        self.icon       = icon

    def write(self):
        # Import di sini (lazy) — hindari circular import saat startup
        from pyrogram.raw.types.keyboard_button_style_bg_primary import KeyboardButtonStyleBgPrimary
        from pyrogram.raw.types.keyboard_button_style_bg_danger import KeyboardButtonStyleBgDanger
        from pyrogram.raw.types.keyboard_button_style_bg_success import KeyboardButtonStyleBgSuccess

        if self.bg_primary:
            return KeyboardButtonStyleBgPrimary()
        if self.bg_danger:
            return KeyboardButtonStyleBgDanger()
        if self.bg_success:
            return KeyboardButtonStyleBgSuccess()
        return None
