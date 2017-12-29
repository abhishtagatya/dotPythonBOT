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
from __future__ import unicode_literals

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
    ImageMessage, ImageSendMessage, VideoMessage, AudioMessage,
    FileMessage,
)

app = Flask(__name__)
version = '0.1 ALPHA BUILD'

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
    cmd = ['/course','/ask','/docs','/dev','/group','/donate','/feedback','/key',]
    text = (event.message.text).lower()
    text_argument = text.split()

    def course_message(option=[]):
        """ Enter the course option and select from a few different course option """
        if 'get_started' in option:

            with open('src/course/getting_started.json','r') as course_getting_started:
                # Opens the src/course/getting started and reading it!
                lesson = json.load(course_getting_started)

                # Below is the Controll flow for the statement 'getting started'
                if 'intro' in option:
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=lesson['lesson']['introduction_lesson']))
                elif 'install' in option:
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=lesson['lesson']['install_lesson']))
                elif 'version' in option:
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=lesson['lesson']['version_lesson']))
                elif 'script' in option:
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=lesson['lesson']['script_lesson']))
                elif 'run_program' in option:
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=lesson['lesson']['pyrun_lesson']))
                else :
                    line_bot_api.reply_message(
                        event.reply_token,[
                        TextSendMessage(text=lesson['description']),
                        TextSendMessage(text=lesson['menu_option']),
                        TextSendMessage(text="To enroll, type : /course (chapter) (lesson)")])

        elif 'basic' in option:

            with open('src/course/basic_course.json','r') as course_basic:
                # Opens basic_course.json from src/course
                lesson = json.load(course_basic)
                if 'syntax' in option:
                    if 'var' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['syntax']['variable']))
                    elif 'bool' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['syntax']['boolean']))
                    elif 'reassign' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['syntax']['reassign']))
                    elif 'comment' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['syntax']['comment']))
                    elif 'operator' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['syntax']['operator']))
                    elif 'type' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['syntax']['data_type']))
                    else :
                        line_bot_api.reply_message(
                            event.reply_token,[
                            TextSendMessage(text=lesson['lesson']['syntax']['description']),
                            TextSendMessage(text=lesson['lesson']['syntax']['menu_option']),
                            TextSendMessage(text="To enroll, type : /course (chapter) (lesson) (sublesson)")])

                elif 'strings' in option:
                    if 'index' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['strings']['str_index']))
                    elif 'operate' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['strings']['str_operate']))
                    elif 'func' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['strings']['str_func']))
                    elif 'format' in option:
                        if isinstance(event.source, SourcUser):
                            # Get User Profile
                            user_profile = line_bot_api.get_profile(event.source.user_id)
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text=(lesson['lesson']['strings']['str_format']).format(user_profile.display_name)))
                        else :
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text=lesson['lesson']['strings']['str_format_debug']))
                    elif 'input' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['strings']['str_input']))
                    elif 'typecast' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['strings']['typecast']))
                    else :
                        line_bot_api.reply_message(
                            event.reply_token,[
                            TextSendMessage(text=lesson['lesson']['strings']['description']),
                            TextSendMessage(text=lesson['lesson']['strings']['menu_option']),
                            TextSendMessage(text="To enroll, type : /course (chapter) (lesson) (sublesson)")])

                elif 'multi_data' in option:
                    pass

                else :
                    line_bot_api.reply_message(
                        event.reply_token,[
                        TextSendMessage(text=lesson['description']),
                        TextSendMessage(text=lesson['menu_option']),
                        TextSendMessage(text="To enroll, type : /course (chapter) (lesson) (sublesson)")])


        else :
            line_bot_api.reply_message(
                event.reply_token,[
                TextSendMessage(text="Lets enroll the course!".format(text)),
                TextSendMessage(
                text="Choose the course you want to learn : \n 1. Getting Started (get_started) \n 2. Basic (basic) \n 3. File Operation (file_ops) \n 4. Python Standard Module (module) \n 5. Python Third Party Module (third_party) "),
                TextSendMessage(text="To enroll, type : /course (chapter)")])


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

    if cmd[0] in text:
        course_message(text_argument)
    elif cmd[1] in text:
        ask_message()
    elif cmd[2] in text:
        docs_message()
    elif cmd[3] in text:
        dev_message()
    elif cmd[4] in text:
        group_message()
    elif cmd[5] in text:
        donate_message()
    elif cmd[6] in text:
        feedback_message()
    elif cmd[7] in text:
        key_message()
    else :
        line_bot_api.reply_message(
        event.reply_token,[
        TextSendMessage(text="Sorry {} is not a valid command".format(text)),
        TextSendMessage(text="Enter /key for commands or /ask for guide \uDBC0\uDC84")])


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
