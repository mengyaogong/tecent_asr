# coding:utf-8
import json
from flask import Flask
from flask import request
import urllib
import os,re
import sys
import pandas as pd
# reload(sys)
# sys.setdefaultencoding('utf-8')
app = Flask(__name__)

data_file = '/usr/local/src/tecent_asr/data'
txt_file = '/usr/local/src/tecent_asr/txt'
csv_file = os.path.join(os.getcwd(),'test.csv')

@app.route('/url', methods=['GET', 'POST'])
def route_url():
    code = 0
    message = "成功"
    if request.method == 'POST':
        data = request.get_data()
        text = request.form.get('text')
        requestId = request.form.get('requestId')
        # print data
        print 'text:%s'%text
        url = request.form.get('audioUrl')
        name = urllib.unquote(str(url).split('/')[-1])
        name = os.path.splitext(name)[0]
        print name
        print requestId
        if text:
            f1 = open(data_file+'/'+name+'_data.txt','w')
            f1.write(str(data).encode('utf-8'))
            f1.close()
            f2 = open(txt_file+'/'+name +'.txt','w')
            f2.write(text.encode('utf-8'))
            f2.close()
            data = pd.read_csv(csv_file)
            data.loc[data['requestId'] == int(requestId), 'txt_path'] = txt_file+'/'+name +'.txt'
            data.loc[data['requestId'] == int(requestId), 'data_path'] = txt_file+'/'+name +'_data.txt'
            data.to_csv(csv_file,index=False)

    return json.dumps({"code":code,"message":message},ensure_ascii=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5003, debug=False)
