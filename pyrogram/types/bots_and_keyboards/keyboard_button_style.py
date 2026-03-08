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
        # Import dari __init__.py package, bukan file individual
        import pyrogram.raw.types as raw_types
        
        if self.bg_primary:
            return raw_types.KeyboardButtonStyleBgPrimary()
        if self.bg_danger:
            return raw_types.KeyboardButtonStyleBgDanger()
        if self.bg_success:
            return raw_types.KeyboardButtonStyleBgSuccess()
        return None
