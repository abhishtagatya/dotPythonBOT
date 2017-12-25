import json

with open('src/course/getting_started.json','r') as json_file:
    lesson = json.load(json_file)

    print lesson["lesson"][0]
    print None
    print None
    print None
