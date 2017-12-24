# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

import os
import sys
import json
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerMessage,
    StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('z0g2r0/7tVh6rEYEMA/Utv6G5d9y3LEtpgRdLHUSrSQOAfl7iQCwtaZ/TEEVAxE6DKLtOShFdloBJv9pU/RFw87WfvmwT/aW5rNLttga0N8fOjSmET3QWgozNt35VnDK4+faM2ACvG2fqpr5vIB88QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ee6ad8acedc43c85b4a0a277807d5df5')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """ Handles all received message from user and process it through the
    controll flow below """

    # Available commands
    cmd = ['/course','/ask','/docs','/dev','/group','/donate','/feedback','/key']
    text = event.message.text

    # Get User Profile
    user_profile = line_bot_api.get_profile(event.source.user_id)

    def course_message():
        """ Enter the course option and select from a few different course option """

        line_bot_api.reply_message(
        event.reply_token,[
        TextSendMessage(text="Lets enroll the course!".format(text)),
        TextSendMessage(text="Choose the course you want to learn : \n + Getting Started \n + Basic \n + File Operation \n + Python Standard Module \n + Python Third Party Module ")])

    def ask_message():
        pass

    def docs_message():
        pass

    def dev_message():
        pass

    def group_message():
        pass

    def donate_message():
        pass

    def feedback_message():
        pass

    def key_message():
        pass

    if text == cmd[0]:
        course_message()
    elif text == cmd[1]:
        ask_message()
    elif text == cmd[2]:
        docs_message()
    elif text == cmd[3]:
        dev_message()
    elif text == cmd[4]:
        group_message()
    elif text == cmd[5]:
        donate_message()
    elif text == cmd[6]:
        feedback_message()
    elif text == cmd[7]:
        key_message()
    else :
        line_bot_api.reply_message(
        event.reply_token,[
        TextSendMessage(text="Sorry {} is not a valid command".format(text)),
        TextSendMessage(text="Enter /key for commands or /ask for guide \uDBC0\uDC84")])


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
