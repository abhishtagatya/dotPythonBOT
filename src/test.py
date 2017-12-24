# -*- coding: utf-8 -*-
import json

with open('src/course/getting_started.json', 'r') as json_file:
    lesson = json.load(json_file)
    print lesson["lesson"]["introduction_lesson"]
