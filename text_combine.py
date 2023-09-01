# 사진 찍고 텍스트 합본 만들기 
# 편집 당일로 만든 텍스트 -> 아이폰이 읽은 텍스트만 그냥 combine 해주는 것

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
print('텍스트 변환 완료')
    
book_name = str(input())
with open('{}/combine_{}_{}.txt'.format(path['path']['combine_path'],accurate_today,book_name),'w') as file:
    file.writelines(str_list)
