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

import requests
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
version = 'v1.1 BETA RELEASE'

line_bot_api = LineBotApi('CHANNEL ACCESS TOKEN')
handler = WebhookHandler('CHANNEL SECRET')


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
    # Command = course / ask / docs / dev / group / donate / feedback / key / social
    cmd = ['course','ask','docs','dev','group','donate','feedback','key','credits','social','new']
    text = (event.message.text).lower()
    text_argument = text.split()

    # Get User Profile
    user_profile = line_bot_api.get_profile(event.source.user_id)

    def course_message(option=[]):
        """ Enter the course option and select from a few different course option """
        if ('gs' in option or
            'started' in option or
            'start' in option):
            # Get started key : 'gs'

            # Opens the github dlearn-res/course/getting_started.json and reading it!
            url_req = requests.get('https://raw.githubusercontent.com/abhishtagatya/dlearn-res/master/dotPython/course/getting_started.json')
            lesson = url_req.json()

            # Below is the Controll flow for the statement 'getting started'
            if 'intro' in option:
                # Introduction Keyword
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
            elif 'inter' in option:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=lesson['lesson']['interpreter_lesson']))
            elif 'script' in option:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=lesson['lesson']['script_lesson']))
            elif 'run' in option:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=lesson['lesson']['pyrun_lesson']))
            else :
                line_bot_api.reply_message(
                    event.reply_token,[
                    TextSendMessage(text=lesson['description']),
                    TextSendMessage(text=lesson['menu_option']),
                    TextSendMessage(text="To enroll, type : /course (chapter) (lesson)")])

        elif ('bsc' in option or
            'basic' in option):
            # Basic key : 'bsc'
            # Opens github dlearn-res/course/basic_course.json
            url_req = requests.get('https://raw.githubusercontent.com/abhishtagatya/dlearn-res/master/dotPython/course/basic_course.json')
            lesson = url_req.json()

            if 'syn' in option:
                # Syntax key : 'syn'
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

            elif 'str' in option:
                # Strings key : 'str'
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

            elif 'dts' in option:
                # Data structure key : 'dts'
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
                elif 'fsets' in option:
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=lesson['lesson']['data_structure']['frozensets']))
                else :
                    line_bot_api.reply_message(
                        event.reply_token,[
                        TextSendMessage(text=lesson['lesson']['data_structure']['description']),
                        TextSendMessage(text=lesson['lesson']['data_structure']['menu_option']),
                        TextSendMessage(text="To enroll, type : /course (chapter) (lesson) (sublesson)")])

            elif 'loc' in option:
                # Loops and Condition key : 'loc'
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
                elif 'bnc' in option:
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
                # Function key : 'def'
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

            elif 'cls' in option:
                # Class objects key : 'cls'
                unavailableMessage('WIP')

            else :
                line_bot_api.reply_message(
                    event.reply_token,[
                    TextSendMessage(text=lesson['description']),
                    TextSendMessage(text=lesson['menu_option']),
                    TextSendMessage(text="To enroll, type : /course (chapter) (lesson) (sublesson)")])

        elif ('fo' in option or
            'file' in option):
            # File operation key : 'fo'

            # Opens the github dlearn-res/course/fileops course and reading it!
            url_req = requests.get('https://raw.githubusercontent.com/abhishtagatya/dlearn-res/master/dotPython/course/fileops_course.json')
            lesson = url_req.json()

            # Below is the Controll flow for the statement 'file operation'
            if 'open' in option:
                # Introduction Keyword
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=lesson['lesson']['opening_file']))
            elif 'read' in option:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=lesson['lesson']['reading_file']))
            elif 'write' in option:
                try :
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=(lesson['lesson']['writing_file']).format(user_profile.display_name)))
                except :
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=(lesson['lesson']['writing_file']).format('dotPython')))
            elif 'clarg' in option:
                try :
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=(lesson['lesson']['cl_arg']).format(user_profile.display_name)))
                except :
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=(lesson['lesson']['cl_arg']).format('dotPython')))
            elif 'fys' in option:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=lesson['lesson']['file_system']))
            elif 'csv' in option:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=lesson['lesson']['csv_file']))
            elif 'json' in option:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=lesson['lesson']['json_file']))
            else :
                line_bot_api.reply_message(
                    event.reply_token,[
                    TextSendMessage(text=lesson['description']),
                    TextSendMessage(text=lesson['menu_option']),
                    TextSendMessage(text="To enroll, type : /course (chapter) (lesson)")])

        elif ('psm' in option or
            'standard' in option or
            'module' in option):
            # Python standard module key : 'psm'
            unavailableMessage('WIP')

        elif 'ptpm' in option:
            # Third Party key : 'ptpm'
            unavailableMessage('WIP')

        elif ('chal' in option or
            'challenge' in option or
            'trial' in option):
            # Challenge key : 'chal'
            if 'bc' in option:
                # Basic Challenge key : 'bc'
                url_req = requests.get('https://raw.githubusercontent.com/abhishtagatya/dlearn-res/master/dotPython/course/fileops_course.json')
                challenge = url_req.json()

                # The code below chooses a random key to be printed out as text from the JSON file

                if 'syn' in option:
                    chal_syn = random.choice(list(challenge['challenge']['syntax'].keys()))
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=challenge['challenge']['syntax'][chal_syn]))
                elif 'str' in option:
                    chal_str = random.choice(list(challenge['challenge']['strings'].keys()))
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=challenge['challenge']['strings'][chal_str]))
                elif 'dts' in option:
                    chal_dts = random.choice(list(challenge['challenge']['data_structure'].keys()))
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=challenge['challenge']['data_structure'][chal_dts]))
                elif 'loc' in option:
                    chal_lc = random.choice(list(challenge['challenge']['loops_cond'].keys()))
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=challenge['challenge']['loops_cond'][chal_lc]))
                elif 'def' in option:
                    chal_def = random.choice(list(challenge['challenge']['function'].keys()))
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=challenge['challenge']['function'][chal_def]))
                elif 'cls' in option:
                    unavailableMessage('WIP')

                else :
                    line_bot_api.reply_message(
                        event.reply_token,[
                        TextSendMessage(text=challenge['description']),
                        TextSendMessage(text=challenge['menu_option']),
                        TextSendMessage(text="To enroll, type : /course (chapter) (challenge)")])

            elif 'foc' in option:
                unavailableMessage('WIP')
            elif 'psmc' in option:
                unavailableMessage('WIP')
            elif 'ptpmc' in option:
                unavailableMessage('WIP')
            else:
                line_bot_api.reply_message(
                    event.reply_token,[
                    TextSendMessage(text="Lets start the challenge!"),
                    TextSendMessage(
                    text="Choose the course you want to challenge : \n 1. Basic (bc) \n 2. File Operation (foc) \n 3. Python Standard Module (psmc) \n 4. Python Third Party Module (ptpmc)"),
                    TextSendMessage(text="To enroll, type : /course (chapter) (challenge)")])

        else :
            line_bot_api.reply_message(
                event.reply_token,[
                TextSendMessage(text="Lets enroll the course!".format(text)),
                TextSendMessage(
                text="Choose the course you want to learn : \n 1. Getting Started (gs) \n 2. Basic (bsc) \n 3. File Operation (fo) \n 4. Python Standard Module (psm) \n 5. Python Third Party Module (ptpm) \n 6. Python Challenge (chal)"),
                TextSendMessage(text="To enroll, type : /course (chapter)")])


    def ask_message(option=[]):
        """ Enter to ask questions about Python programming and FAQ """

        url_req = requests.get('https://raw.githubusercontent.com/abhishtagatya/dlearn-res/master/dotPython/ask/ask.json')
        question = url_req.json()

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
        elif 'group' in option:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=question['ask']['group']))
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
                TextSendMessage(text=question['ask']['menu_option']),
                TextSendMessage(text="To ask questions, type : /ask (question)")])

    def docs_message():
        unavailableMessage('WIP')

    def dev_message():
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="dotPython was created by Abhishta Gatya, 2018\n\nabhishtagatya.onuniverse.com"))

    def group_message():
        url_req = requests.get('https://raw.githubusercontent.com/abhishtagatya/dlearn-res/master/dotPython/group/group.txt')
        mes = url_req.text

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=mes))


    def donate_message():
        unavailableMessage('WIP')

    def feedback_message():
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="If you have any feedbacks or complaints about dotPython chatbot, please send it over 'saveitcomm@yahoo.com' with the title '[FEEDBACK] TITLE - SENDER'"))

    def key_message():
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Available Keys :\n + Join Course (/course) \n + Ask Questions (/ask) \n + Python Documentations (/docs) \n + Developer (/dev) \n + Learning Group (/group) \n + Donation (/donate) \n + Feedbacks (/feedback) \n + Source Credits (/credits) \n + Social Media (/social) \n + Show Keys (/key)"))

    def credits_message():
        url_req = requests.get('https://raw.githubusercontent.com/abhishtagatya/dlearn-res/master/dotPython/credit/credit.txt')
        mes = url_req.text

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=mes))


    def social_message():
        unavailableMessage('WIP')

    def new_message():
        """ Sends a secret message weekly!"""
        unavailableMessage('WIP')

    def unavailableMessage(condition):
        """ Prints Unavailable Messages when somethin goes wrong """
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

    def chatInteraction(mes=[]):
        ''' Adds Human like interactions to python to make the bot doesnt really feel like a robot '''

        # Common Conversations
        # WARNING! : CONTAINS BAD JOKES, READ AT YOUR OWN RISK!
        url_req = requests.get('https://raw.githubusercontent.com/abhishtagatya/dlearn-res/master/dotPython/interact/bot_interact.json')
        reply_mes = url_req.json()

        if ('hello' in mes or 'hey' in mes or
            'hi' in mes or 'halo' in mes):
            try :
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=random.choice(reply_mes["greeting"]).format(user_profile.display_name)))
            except :
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=random.choice(reply_mes["greeting"]).format("Human")))

        elif ('joke' in mes or 'funny' in mes or
            'laugh' in mes):
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=random.choice(reply_mes["joke"])))
        else :
            line_bot_api.reply_message(
            event.reply_token,[
            TextSendMessage(text="Sorry {} is not a valid command".format(text)),
            TextSendMessage(text="Enter /key for commands or /ask for guide \uDBC0\uDC84")])

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
    elif cmd[8] in text:
        credits_message()
    elif cmd[9] in text:
        social_message()
    elif cmd[10] in text:
        new_message()
    else :
        chatInteraction(text_argument)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
