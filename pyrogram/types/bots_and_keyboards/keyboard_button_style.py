class KeyboardButtonStyle:
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
        # Lazy import — hindari circular import saat startup pyrogram
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
