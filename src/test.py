import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

def test_message(event):

    if event.message.text != 'help':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text)
        )

    else :
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='Need Help?')
        )
