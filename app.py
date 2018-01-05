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
import random

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
    controll flow below. Only takes message of type Text"""

    # Available commands
    cmd = ['/course','/ask','/docs','/dev','/group','/donate','/feedback','/key','/credits']
    text = (event.message.text).lower()
    text_argument = text.split()

    # Get User Profile
    user_profile = line_bot_api.get_profile(event.source.user_id)

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
                        try :
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text=(lesson['lesson']['strings']['str_operate']).format(user_profile.display_name,
                                user_profile.status_message)))
                        except LineBotApi :
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text=(lesson['lesson']['strings']['str_operate']).format("John","happy")))
                    elif 'func' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['strings']['str_func']))
                    elif 'format' in option:
                        try :
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text=(lesson['lesson']['strings']['str_format']).format(user_profile.display_name)))
                        except LineBotApi:
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text=(lesson['lesson']['strings']['str_format']).format('He/She')))
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

                elif 'data_structure' in option:
                    if 'list' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['data_structure']['list']))
                    elif 'tuple' in option:
                        try :
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text=(lesson['lesson']['data_structure']['tuple']).format(user_profile.display_name)))
                        except LineBotApi:
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text=(lesson['lesson']['data_structure']['tuple']).format('you')))
                    elif 'dict' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['data_structure']['dict']))
                    elif 'sets' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['data_structure']['sets']))
                    elif 'frozensets' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['data_structure']['frozensets']))
                    else :
                        line_bot_api.reply_message(
                            event.reply_token,[
                            TextSendMessage(text=lesson['lesson']['data_structure']['description']),
                            TextSendMessage(text=lesson['lesson']['data_structure']['menu_option']),
                            TextSendMessage(text="To enroll, type : /course (chapter) (lesson) (sublesson)")])

                elif 'loops_cond' in option:
                    if 'while' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['loops_cond']['while_loop']))
                    elif 'for' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['loops_cond']['for_loop']))
                    elif 'if_else' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=(lesson['lesson']['loops_cond']['if_else']).format(random.randint(0,9))))
                    elif 'nested' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['loops_cond']['nested']))
                    elif 'break_cont' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['loops_cond']['break_cont']))
                    else :
                        line_bot_api.reply_message(
                            event.reply_token,[
                            TextSendMessage(text=lesson['lesson']['loops_cond']['description']),
                            TextSendMessage(text=lesson['lesson']['loops_cond']['menu_option']),
                            TextSendMessage(text="To enroll, type : /course (chapter) (lesson) (sublesson)")])

                elif 'def' in option:
                    if 'declare' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['function']['declare']))
                    elif 'call' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['function']['call']))
                    elif 'arg' in option:
                        try :
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text=(lesson['lesson']['function']['argument']).format(user_profile.display_name)))
                        except LineBotApi :
                            line_bot_api.reply_message(
                                event.reply_token,
                                TextSendMessage(text=(lesson['lesson']['function']['argument']).format('user')))
                    elif 'varscope' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=(lesson['lesson']['function']['varscope']).format(random.randint(0,9),random.randint(0,9))))
                    elif 'nested' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['function']['nested']))
                    elif 'decorator' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=lesson['lesson']['function']['decorator']))
                    elif 'overload' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=(lesson['lesson']['function']['overloading']).format(random.randint(0,9))))
                    elif 'recursion' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=(lesson['lesson']['function']['recursion']).format(random.randint(0,9))))
                    elif 'generator' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=(lesson['lesson']['function']['generator']).format(random.randint(0,9))))
                    elif 'lambda' in option:
                        line_bot_api.reply_message(
                            event.reply_token,
                            TextSendMessage(text=(lesson['lesson']['function']['lambda']).format(random.randint(0,9))))
                    else :
                        line_bot_api.reply_message(
                            event.reply_token,[
                            TextSendMessage(text=lesson['lesson']['function']['description']),
                            TextSendMessage(text=lesson['lesson']['function']['menu_option']),
                            TextSendMessage(text="To enroll, type : /course (chapter) (lesson) (sublesson)")])

                elif 'classobj' in option:
                    unavailableMessage('WIP')

                else :
                    line_bot_api.reply_message(
                        event.reply_token,[
                        TextSendMessage(text=lesson['description']),
                        TextSendMessage(text=lesson['menu_option']),
                        TextSendMessage(text="To enroll, type : /course (chapter) (lesson) (sublesson)")])

        elif 'file_ops' in option:
            pass

        elif 'module' in option:
            pass

        elif 'third_party' in option:
            pass

        elif 'challange' in option:
            pass

        else :
            line_bot_api.reply_message(
                event.reply_token,[
                TextSendMessage(text="Lets enroll the course!".format(text)),
                TextSendMessage(
                text="Choose the course you want to learn : \n 1. Getting Started (get_started) \n 2. Basic (basic) \n 3. File Operation (file_ops) \n 4. Python Standard Module (module) \n 5. Python Third Party Module (third_party) "),
                TextSendMessage(text="To enroll, type : /course (chapter)")])


    def ask_message(option=[]):
        """ Enter to ask questions about Python programming and FAQ """

        with open('src/ask/ask.json','r') as ask_file:
            question = json.load(ask_file)
            if 'faq' in option:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=question['ask']['FAQ']))
            elif 'promote' in option:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=question['ask']['promote']))
            elif 'course' in option:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=question['ask']['course']))
            elif 'version' in option:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=(question['ask']['version']).format(version)))
            elif 'link' in option:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=question['ask']['link']))
            elif 'about' in option:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=question['ask']['about']))
            elif 'python' in option:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=question['ask']['python']))
            else :
                line_bot_api.reply_message(
                    event.reply_token,[
                    TextSendMessage(text=question['ask']['description']),
                    TextSendMessage(text=question['ask']['menu_option'])])

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

    def credits_message():
        pass

    def unavailableMessage(condition):
        ''' Prints Unavailable Messages when somethin goes wrong '''
        # Keyword : WIP (Work in Progress); NAV (Not Available); BKF (Broken Feature)

        if condition == 'WIP':
            line_bot_api.reply_message(
                event.reply_token,[
                TextSendMessage(text="Sorry but the keyword you are trying to access is currently unavailable."),
                TextSendMessage(text="Still under construction, please wait for an update \uDBC0\uDC84")])
        elif condition == 'NAV':
            line_bot_api.reply_message(
                event.reply_token,[
                TextSendMessage(text="Sorry but the keyword you are trying to access is currently unavailable."),
                TextSendMessage(text="Feature currently unavailable, please wait for a notice \uDBC0\uDC84")])
        elif condition == 'BKF':
            line_bot_api.reply_message(
                event.reply_token,[
                TextSendMessage(text="Sorry but the keyword you are trying to access is currently unavailable."),
                TextSendMessage(text="Feature currently broken, please wait for a notice or update \uDBC0\uDC84")])
        else :
            pass


    if cmd[0] in text:
        course_message(text_argument)
    elif cmd[1] in text:
        ask_message(text_argument)
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
    elif cmd[7] in text:
        credits_message()
    else :
        line_bot_api.reply_message(
        event.reply_token,[
        TextSendMessage(text="Sorry {} is not a valid command".format(text)),
        TextSendMessage(text="Enter /key for commands or /ask for guide \uDBC0\uDC84")])


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
