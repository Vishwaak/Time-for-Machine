import json 
import os
import time
import math
import numpy as np
import re 
import emoji


def Deemoji(text):
    allchars = [str for str in text.encode('utf-8').decode('utf-8')]
    emoji_list = [c for c in allchars if c in emoji.UNICODE_EMOJI]
    clean_text = ' '.join([str for str in text.encode('utf-8').decode('utf-8').split() if not any(i in str for i in emoji_list)])
    return clean_text

file1 = open("chats.txt" , "a")
progress_String = "Converting JSON to Text file "
with open('result.json') as json_file:
    data = json.load(json_file)
    x = int(len(data['chats']['list']))
    for i in range(2,x):
        mine = dict(data['chats']['list'][i])
        for j in range(len(mine['messages'])):
            what = dict(mine['messages'][j])
            if 'from' in what.keys():
                #print(what['from'],":" , what["text"])
                if type(what['text']) is str:
                    killer = Deemoji(what['text'])
                    texter = what['from'] + ":" + killer+"\n"
                    file1.write(texter)
            #else:
                #print("I was on a Call")
        os.system("clear")
        print(progress_String + str(math.ceil((i/x)*100)) + "%")
        time.sleep(0.01)
file1.close()
print("Convertion Done :)")

        
   
        