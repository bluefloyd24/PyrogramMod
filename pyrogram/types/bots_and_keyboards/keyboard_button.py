#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from pyrogram import raw, types
from ..object import Object


class KeyboardButton(Object):
    """One button of the reply keyboard.

    Parameters:
        text (``str``):
            Text of the button.

        request_contact (``bool``, *optional*):
            If True, the user's phone number will be sent as a contact when the button is pressed.

        request_location (``bool``, *optional*):
            If True, the user's current location will be sent when the button is pressed.

        web_app (:obj:`~pyrogram.types.WebAppInfo`, *optional*):
            Web App launched when the button is pressed.

        style (:obj:`~pyrogram.types.KeyboardButtonStyle`, *optional*):
            Style for the button background color (primary/blue, danger/red, success/green).
    """

    def __init__(
        self,
        text: str,
        request_contact: bool = None,
        request_location: bool = None,
        web_app: "types.WebAppInfo" = None,
        style: "types.KeyboardButtonStyle" = None,
    ):
        super().__init__()

        self.text = str(text)
        self.request_contact = request_contact
        self.request_location = request_location
        self.web_app = web_app
        self.style = style

    @staticmethod
    def read(b):
        if isinstance(b, raw.types.KeyboardButton):
            return b.text

        if isinstance(b, raw.types.KeyboardButtonRequestPhone):
            return KeyboardButton(
                text=b.text,
                request_contact=True
            )

        if isinstance(b, raw.types.KeyboardButtonRequestGeoLocation):
            return KeyboardButton(
                text=b.text,
                request_location=True
            )

        if isinstance(b, raw.types.KeyboardButtonSimpleWebView):
            return KeyboardButton(
                text=b.text,
                web_app=types.WebAppInfo(url=b.url)
            )

    def write(self):
        if self.request_contact:
            btn = raw.types.KeyboardButtonRequestPhone(text=self.text)
        elif self.request_location:
            btn = raw.types.KeyboardButtonRequestGeoLocation(text=self.text)
        elif self.web_app:
            btn = raw.types.KeyboardButtonSimpleWebView(
                text=self.text,
                url=self.web_app.url
            )
        else:
            btn = raw.types.KeyboardButton(text=self.text)

        # Inject style sebagai bytes langsung ke field style
        if self.style is not None:
            style_bytes = self.style.write()
            if style_bytes is not None:
                try:
                    btn.style = style_bytes
                except AttributeError:
                    pass

        return btn
