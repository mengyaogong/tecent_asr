# -*- coding:utf-8 -*-
import requests
import hashlib
import time
import hmac
import base64
import urllib

req_url = "https://aai.qcloud.com/asr/v1/"
#callback_url,需要搭建接收post数据的服务
callback_url = "http://audio.luowr.com:5003/url"
sign_url = "aai.qcloud.com/asr/v1/"

def task_process(audio_url,appid,secret_id,secret_key):
    request_data = dict()
    request_data['channel_num'] = 1
    request_data['secretid'] = secret_id
    request_data['engine_model_type'] = "16k_0"
    request_data['timestamp'] = int(time.time())
    request_data['expired'] = int(time.time()) + 3600
    request_data['nonce'] = 1234
    request_data['projectid'] = 0
    request_data['callback_url'] = callback_url
    request_data['res_text_format'] = 0
    request_data['res_type'] = 1
    request_data['source_type'] = 0
    request_data['sub_service_type'] = 0
    secret_key = secret_key

    request_data['url'] = urllib.quote(audio_url)
    authorization = generate_sign(request_data, appid,secret_key)
    task_req_url = generate_request(request_data, appid)
    header = {
        "Content-Type": "application/json",
        "Authorization": str(authorization)
    }
    r = requests.post(task_req_url, headers=header, data=request_data)
    return r.text


def generate_sign(request_data, appid,secret_key):
    sign_str = "POST" + sign_url + str(appid) + "?"
    sort_dict = sorted(request_data.keys())
    for key in sort_dict:
        sign_str = sign_str + key + "=" + urllib.unquote(str(request_data[key])) + '&'
    sign_str = sign_str[:-1]
    authorization = base64.b64encode(hmac.new(secret_key, sign_str, hashlib.sha1).digest())
    return authorization


def generate_request(request_data, appid):
    result_url = req_url + str(appid) + "?"
    for key in request_data:
        result_url = result_url + key + "=" + str(request_data[key]) + '&'
    result_url = result_url[:-1]
    return result_url

if __name__ == '__main__':
    audio_url = 'http://audio.luowr.com:8080/download/201804/%E4%BA%A6%E5%BA%84%E9%87%91%E8%8C%82%E5%BA%9C/4%E6%9C%8824%E6%97%A5/4.24%E4%B8%AD%E5%8E%9F/%E8%B5%B5%E6%99%93%E5%A6%83/4.24%E8%B0%A2%E5%85%88%E7%94%9F176-9966%E6%97%A0%E6%95%88.wav'
    task_process(audio_url)
