import json

import requests

hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/99.0.4844.82 Safari/537.36'}
url = 'https://xuanguapi.eastmoney.com/Stock/JS.aspx?type=xgq&sty=xgq&token=eastmoney&c=[gf2]&p=1&jn=kuAPFImR&ps=3000&s=stockcode&st=1&r=1659237663728'
response = requests.get(url, headers=hd)
info = response.text
info = info[13:len(info)]
info = json.loads(info)
code_all = []
for i in range(len(info['Results'])):
    code_all.append(info['Results'][i][2:8])
date_all = []
num = 0
num_0 = 0
for i in range(len(code_all)):
    cn_code = code_all[i]
    cn_code = cn_code.zfill(6)
    start_time = '19900101'
    end_time = '20220101'
    url = 'https://q.stock.sohu.com/hisHq?code=cn_' + cn_code + '&start=' + start_time + '&end=' + end_time
    response = requests.get(url, headers=hd)
    info = response.json()
    try:
        if info[0]['status'] == 0:
            date_all.append([cn_code, info[0]['hq']])
            num = num + 1
        print(cn_code)
    except:
        continue
    if num == 150:
        num = 0
        num_0 = num_0 + 1
        with open('data' + str(num_0) + '.json', 'w') as f:
            json.dump(date_all, f)
            print('ok')
        date_all = []
