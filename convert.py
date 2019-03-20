# coding:utf-8
import subprocess,os

#音频文件格式转换
def ffmpeg(src_path, dst_path):
    command = "ffmpeg -y -i '{}' -ar 16000  '{}' ".format(src_path, dst_path)
    try:
        subprocess.check_call(command, shell=True)
        is_success = True
    except subprocess.CalledProcessError as e:
        print ("error code: {}! shell command: {}".format(e.returncode, e.cmd))
        is_success = False
    return is_success

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

file_folder = '/home/gmy/Documents/201806'
file_list = filepath(file_folder)

for i in file_list:
    print i
    print os.path.splitext(i)[1]
    if os.path.splitext(i)[1] == '.WAV':
        ffmpeg(i,os.path.splitext(i)[0]+'.wav')
    else:
        ffmpeg(i, os.path.splitext(i)[0] + '.WAV')
    os.remove(i)


