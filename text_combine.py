# 사진 찍고 텍스트 합본 만들기 
# 편집 당일로 만든 텍스트

import glob
import os
import datetime
import pandas as pd
import json
with open('/Users/jeonmincheol/Book_Capture/path_box.json') as f:
    path = json.load(f)

file = glob.glob("{}/*.txt".format(path['path']['text_path']))
dic = dict()
str_list = []
time = datetime.datetime.today()
accurate_today = str(time.year) + '_' + str(time.month).zfill(2) + '_' + str(time.day).zfill(2)
for i in file:
    dic[int(os.path.getmtime(i))] = i
    
idx = list(dic.keys())
idx = sorted(idx)

for i in idx:
    f = open("{}".format(dic[i]),'r')
    sentence = f.readlines()
    str_list += sentence
    f.close()
    

with open('{}/combine_{}.txt'.format(path['path']['combine_path'],accurate_today),'w') as file:
    file.writelines(str_list)
