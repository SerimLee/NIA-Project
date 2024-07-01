import json
import numpy as np
import os

folder_path = "./E2ON_JSON/C042"
folder_list = os.listdir(folder_path) # 1-1 ... 706-1

#folder_list.sort(key=lambda x:(int(x.split('-')[0]), int(x.split('-')[1])))

cnt = 1
for i in folder_list:
    old_name = folder_path + '/' + '{}'.format(i)
    new_name = folder_path + '/' + '{}'.format(i.replace("_check", ""))
    print(old_name, new_name)
    os.rename(old_name, new_name)