import sys, glob, pandas, numpy, os, json, requests
# import selenium, seleniumwire, chromedriver # hoxy..?
import uuid, time, base64, datetime
from tqdm import tqdm

with open('/Users/jeonmincheol/Book_Capture/path_box.json') as f:
    path = json.load(f)
    
book_name = str(input("책 이름을 입력해주세요."))
dic = dict()
sentences = ""
time_ = datetime.datetime.today()
accurate_today = str(time_.year) + '_' + str(time_.month).zfill(2) + '_' + str(time_.day).zfill(2)

api_url = path['path']['api_url']
secret_key = path['path']['ocr_secret_key']

image_folder = glob.glob('./image_file/*.JPG')

for i in image_folder:
    dic[int(os.path.getmtime(i))] = i
    
idx = list(dic.keys())
idx = sorted(idx)

for i in idx:
    image_file = dic[i]
        
    with open(image_file,'rb') as f:
        file_data = f.read()

    request_json = {
        'images': [
            {
                'format': 'jpg',
                'name': 'demo',
                'data': base64.b64encode(file_data).decode()
            }
        ],
        'requestId': str(uuid.uuid4()),
        'version': 'V2',
        'timestamp': int(round(time.time() * 1000))
    }

    payload = json.dumps(request_json).encode('UTF-8')
    headers = {
    'X-OCR-SECRET': secret_key,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", api_url, headers=headers, data = payload)

    words = json.loads(response.text)
    li = len(words['images'][0]['fields'])
    
    for i in range(li):
        word = words['images'][0]['fields'][i]['inferText']
        sentences += ' ' + word
    
    sentences += '\n' + '*' * 100 + '\n' 

with open('{}/combine_{}_{}.txt'.format(path['path']['combine_path'],accurate_today,book_name),'w') as file:
    file.writelines(sentences)