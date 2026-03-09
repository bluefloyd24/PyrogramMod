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

from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types
from ..object import Object


class InlineKeyboardButton(Object):
    """One button of an inline keyboard.

    Parameters:
        text (``str``):
            Label text on the button.

        callback_data (``str`` | ``bytes``, *optional*):
            Data to be sent in a callback query, 1-64 bytes.

        url (``str``, *optional*):
            HTTP url to be opened when button is pressed.

        web_app (:obj:`~pyrogram.types.WebAppInfo`, *optional*):
            Web App launched when the button is pressed.

        login_url (:obj:`~pyrogram.types.LoginUrl`, *optional*):
            HTTP URL for automatic user authorization.

        user_id (``int``, *optional*):
            User id, for links to the user profile.

        switch_inline_query (``str``, *optional*):
            Prompt user to select a chat and insert bot's username + query.

        switch_inline_query_current_chat (``str``, *optional*):
            Insert bot's username and query in current chat's input field.

        callback_game (:obj:`~pyrogram.types.CallbackGame`, *optional*):
            Description of the game launched when user presses button.

        style (:obj:`~pyrogram.types.KeyboardButtonStyle`, *optional*):
            Style for the button background color (primary/blue, danger/red, success/green).
    """

    def __init__(
        self,
        text: str,
        callback_data: Union[str, bytes] = None,
        url: str = None,
        web_app: "types.WebAppInfo" = None,
        login_url: "types.LoginUrl" = None,
        user_id: int = None,
        switch_inline_query: str = None,
        switch_inline_query_current_chat: str = None,
        callback_game: "types.CallbackGame" = None,
        style: "types.KeyboardButtonStyle" = None,
    ):
        super().__init__()

        self.text = str(text)
        self.callback_data = callback_data
        self.url = url
        self.web_app = web_app
        self.login_url = login_url
        self.user_id = user_id
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.callback_game = callback_game
        self.style = style

    @staticmethod
    def read(b: "raw.base.KeyboardButton"):
        if isinstance(b, raw.types.KeyboardButtonCallback):
            try:
                data = b.data.decode()
            except UnicodeDecodeError:
                data = b.data
            return InlineKeyboardButton(text=b.text, callback_data=data)

        if isinstance(b, raw.types.KeyboardButtonUrl):
            return InlineKeyboardButton(text=b.text, url=b.url)

        if isinstance(b, raw.types.KeyboardButtonUrlAuth):
            return InlineKeyboardButton(text=b.text, login_url=types.LoginUrl.read(b))

        if isinstance(b, raw.types.KeyboardButtonUserProfile):
            return InlineKeyboardButton(text=b.text, user_id=b.user_id)

        if isinstance(b, raw.types.KeyboardButtonSwitchInline):
            if b.same_peer:
                return InlineKeyboardButton(
                    text=b.text,
                    switch_inline_query_current_chat=b.query
                )
            else:
                return InlineKeyboardButton(
                    text=b.text,
                    switch_inline_query=b.query
                )

        if isinstance(b, raw.types.KeyboardButtonGame):
            return InlineKeyboardButton(text=b.text, callback_game=types.CallbackGame())

        if isinstance(b, raw.types.KeyboardButtonWebView):
            return InlineKeyboardButton(
                text=b.text,
                web_app=types.WebAppInfo(url=b.url)
            )

    def _inject_style(self, btn):
        """Inject style bytes ke button object jika ada."""
        if self.style is not None:
            style_bytes = self.style.write()
            if style_bytes is not None:
                try:
                    btn.style = style_bytes
                except AttributeError:
                    pass
        return btn

    async def write(self, client: "pyrogram.Client"):
        if self.callback_data is not None:
            data = (
                bytes(self.callback_data, "utf-8")
                if isinstance(self.callback_data, str)
                else self.callback_data
            )
            btn = raw.types.KeyboardButtonCallback(text=self.text, data=data)
            return self._inject_style(btn)

        if self.url is not None:
            btn = raw.types.KeyboardButtonUrl(text=self.text, url=self.url)
            return self._inject_style(btn)

        if self.login_url is not None:
            # login_url.write() tidak support style injection
            return self.login_url.write(
                text=self.text,
                bot=await client.resolve_peer(self.login_url.bot_username or "self")
            )

        if self.user_id is not None:
            btn = raw.types.InputKeyboardButtonUserProfile(
                text=self.text,
                user_id=await client.resolve_peer(self.user_id)
            )
            return self._inject_style(btn)

        if self.switch_inline_query is not None:
            btn = raw.types.KeyboardButtonSwitchInline(
                text=self.text,
                query=self.switch_inline_query
            )
            return self._inject_style(btn)

        if self.switch_inline_query_current_chat is not None:
            btn = raw.types.KeyboardButtonSwitchInline(
                text=self.text,
                query=self.switch_inline_query_current_chat,
                same_peer=True
            )
            return self._inject_style(btn)

        if self.callback_game is not None:
            btn = raw.types.KeyboardButtonGame(text=self.text)
            return self._inject_style(btn)

        if self.web_app is not None:
            btn = raw.types.KeyboardButtonWebView(text=self.text, url=self.web_app.url)
            return self._inject_style(btn)
