class _StyleBgPrimary:
    pass

class _StyleBgDanger:
    pass

class _StyleBgSuccess:
    pass

class KeyboardButtonStyle:
    def __init__(self, bg_primary=False, bg_danger=False, bg_success=False, icon=None):
        self.bg_primary = bg_primary
        self.bg_danger  = bg_danger
        self.bg_success = bg_success
        self.icon       = icon

    def write(self):
        if self.bg_primary:
            return _StyleBgPrimary()
        if self.bg_danger:
            return _StyleBgDanger()
        if self.bg_success:
            return _StyleBgSuccess()
        return None
