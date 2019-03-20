# coding:utf-8

import pandas as pd
import os
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)

csv_file = os.path.join(os.getcwd(),'test.csv')
f = open(csv_file)
data = pd.read_csv(f)
# print data
print data.loc[data['wav_path'] == '/usr/local/src/tecent_asr/audio_file/sound/201805/北京金茂府/中原5.24/5.24 中原 勾丽丽/王女士138xxxx0132有效复方5.24_0.wav']
print data.loc[data['wav_path'] == '/usr/local/src/tecent_asr/audio_file/201805/北京金茂府/中原5.24/5.24 中原 勾丽丽/王女士138xxxx0132有效复方5.24_0.wav']
# print type('usr/local/src/tecent_asr/audio_file/201805/北京金茂府/中原5.24/5.24 中原 勾丽丽/王女士138xxxx0132有效复方5.24_0.wav')
# print data.loc[data['status']==0]
# print status
# if status.any() == 0:
#     print 'ok'
# data.to_csv(csv_file, index=False)
# data.loc[data['requestId'] == int(434742188), 'data_path'] = '456'
# data.to_csv(csv_file, index=False)
# print data[data['requestId']==434742188]['txt_path']
# print data