# coding:utf-8

from pydub import AudioSegment
# from task import filepath
import os

file_folder = '/home/gmy/Documents/201806'
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

def fenge(file_path):
    path_list = filepath(file_path)
    for i in path_list:
        print i
        path = (str(i).split('/'))
        del path[-1]
        head = ''
        for k in path:
            head = os.path.join(head,k)
        wav_name = os.path.splitext(str(i).split('/')[-1])[0]
        sound = AudioSegment.from_wav(i)
        if len(sound) > 60 * 50 * 1000:
            a = len(sound)/(50*60*1000)+1
            print a
            for j in range(a):
                if j<(a-1):
                    sound[j * 50*60* 1000:(j + 1) * 50 *60* 1000].export('/'+head + '/' + wav_name +'_' + str(j) + '.wav',
                                                                    format='wav')
                else:
                    sound[j * 50 *60* 1000:].export('/'+head + '/' + wav_name +'_' + str(j) + '.wav',
                                                                    format='wav')
            os.remove(i)
fenge(file_folder)


