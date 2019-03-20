# coding:utf-8
import os
import urllib
from pydub import AudioSegment
import time
from tengxun_asr import task_process
import pandas as pd
import json
import thread,threading
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#文件存放路径
file_folder = '/usr/local/src/tecent_asr/audio_file/sound/201806'
#数据记录文件
csv_file = os.path.join(os.getcwd(),'test.csv')
path_List = []

#获取文件列表
def filepath(basepath):
    for item in os.listdir(basepath):
        path = os.path.join(basepath,item)
        if os.path.isfile(path):
            if os.path.splitext(path)[1] == '.WAV' or os.path.splitext(path)[1] == '.wav':
                path_List.append(path)
        else:
            filepath(path)
    return path_List
files = filepath(file_folder)

#调用接口识别，将文件初始状态值0更新为1,记录reauestId、wav_len
def translate(threadName,lock,appid,secret_id,secret_key):
    for i in files:
        print "%s: %s : %s" % (threadName, time.ctime(time.time()),i)
        wav_file = AudioSegment.from_wav(i)
        wav_len = '%fh'%(float(len(wav_file))/(1000*60*60))
        pre_str = 'http://audio.luowr.com:8080/download/'
        folder_name = 'sound'
        url = str(i)[str(i).index(folder_name):]
        link = pre_str + url
        # print link
        link1 = urllib.quote(link,':/')
        # print link1
        lock.acquire()
        data = pd.read_csv(csv_file)
        status = data.loc[data['wav_path'] == i, 'status']
        if status.any() == 0:
            print "%s: %s" % (threadName, i)
            print "%s: %s" % (threadName, wav_len)
            # data.loc[data['wav_path'] == i, 'status'] = 1
            # data.to_csv(csv_file, index=False)
            req_content = task_process(link1,appid,secret_id,secret_key)
            print "%s: %s : %s" % (threadName,i, req_content)
            requestId = int(json.loads(req_content)['requestId'])
            data.loc[data['wav_path'] == i, 'requestId'] = requestId
            data.loc[data['wav_path'] == i, 'wav_len'] = wav_len
            data.loc[data['wav_path'] == i, 'status'] = 1
            data.to_csv(csv_file,index=False)
            lock.release()
            time.sleep(5*60)
        else:
            lock.release()

appid1 = "1258751657"
secret_id1 = "AKIDbIOsaRXznMRsEZJ4dFWQnBYJB9jEtox0"
secret_key1 = "572z5Rkw25fDZr24fCsT1Qfnp1ACnMn3"

appid2 = '1258805798'
secret_id2 = 'AKID2undXJpXwCIwcMEgkldNMMVFoElApbu2'
secret_key2 = '6qU4Wov2FWcZVefWI4f5MaAauIZkkcRP'

appid3 = '1258851135'
secret_id3 = 'AKIDzkLmzXk20jIetwCPo25uYyDD9vTpnseC'
secret_key3 = 'UotoOitpbAUZP3R4Wmob9SWMzQcT6UdW'

appid4 = '1258851306'
secret_id4 = 'AKIDGPPEsQs24z8MVW644PfkfPzOcfHmqJLC'
secret_key4 = 'oTxxoW3QmxxnRinhPzObdfIk164rUwCB'

#定义线程锁
lock = threading.Lock()
#开启线程
try:
    # thread.start_new_thread(translate, ('Thread-1', lock, appid1, secret_id1, secret_key1))
    # thread.start_new_thread(translate, ('Thread-2', lock, appid2, secret_id2, secret_key2))
    thread.start_new_thread(translate, ('Thread-3', lock, appid3, secret_id3, secret_key3))
    thread.start_new_thread(translate, ('Thread-4', lock, appid4, secret_id4, secret_key4))
except:
    print "Error: unable to start thread"

#保持主进程，
while 1:
    pass



