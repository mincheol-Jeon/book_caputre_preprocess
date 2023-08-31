import pytesseract
from PIL import Image
import glob, datetime, pandas as pd
import json, os

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

image_files = glob.glob('./image_file/*')

dic = dict()
str_list = []

for i in image_files:
    dic[int(os.path.getmtime(i))] = i
    
idx = list(dic.keys())
idx = sorted(idx)

for i in idx:
    f = open("{}".format(dic[i]),'r')
    sentence = f.readlines()
    str_list += sentence
    f.close()


time = datetime.datetime.today()
accurate_today = str(time.year) + '_' + str(time.month).zfill(2) + '_' + str(time.day).zfill(2)

result = pytesseract.image_to_string(test,lang='kor')

print(result)

# 이미지 품질이 너무 떨어짐