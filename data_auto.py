import os
import shutil

path = 'G:\sem 7\data mining\lab\classification report\Data Mining Lab 1'

for file in os.listdir(path):
    if file.endswith('_AI.pdf'):
        # shutil.copy(os.path.join(path, file), 'AI/'+file)
        shutil.copy(path+'\\'+file, 'AI/'+file)
    elif file.endswith('_WEB.pdf'):
        shutil.copy(os.path.join(path, file),'WEB/'+file)
   