# coding:utf-8
import os
import pandas as pd

file_folder = os.getcwd()+'/audio_file/sound/201806'
print file_folder
path_List = []
def filepath(basepath):
    for item in os.listdir(basepath):
        path = os.path.join(basepath,item)
        if os.path.isfile(path):
            if os.path.splitext(path)[1] == '.WAV' or os.path.splitext(path)[1] == '.wav':
                path_List.append(path)
        else:
            filepath(path)
    return path_List

path_List = filepath(file_folder)
for i in path_List:
    dataFrame = pd.DataFrame({'wav_path': [i],'status':[0]},
                             columns=['requestId', 'wav_path', 'wav_len', 'txt_path', 'data_path','status'])
    dataFrame.to_csv(os.path.join(os.getcwd(), 'test.csv'), mode='a', header=False, index=False, sep=',')


