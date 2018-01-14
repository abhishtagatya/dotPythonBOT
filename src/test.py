import random
import json

with open('src/course/basic_challenge.json','r') as coord:
    gv = json.load(coord)
    print(gv['challenge']['syntax'][list(random.choice(gv['challenge']['syntax'].keys()))])
