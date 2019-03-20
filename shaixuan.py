# coding:utf-8
import os
import urllib
file_path = '/home/gmy/Documents/201805'
import pandas as pd

def filepath(basepath):
    for item in os.listdir(basepath):
        path = os.path.join(basepath,item)
        if os.path.isfile(path):
            if os.path.splitext(path)[1] == '.WAV':
                print path
                os.remove(path)
        else:
            filepath(path)

filepath(file_path)



