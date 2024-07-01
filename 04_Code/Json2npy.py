import json
import numpy as np
import os
import csv

json_data = []

path_dir = './E2ON_C021/C021_test/blockinfo'  # 경로 변경 가능, blockinfo.json파일이 있는 폴더로 지정
file_list = os.listdir(path_dir)    # npy파일을 만들기 위한 blockinfo.json파일 list
csv_list = './E2ON_C021/testing/trajectories/01' # test용 csv파일 위치
save_dir = './E2ON_C021/testing/frame_level_masks'

traj = len(os.listdir(csv_list)) # test 파일 개수, 63개
traj_line = []

for i in range(traj):
    csv_frame = list()
    data = list()
    file_name = os.listdir(csv_list + '/{:02d}'.format(i + 1))
    for j in file_name:
        traj_file = open(csv_list + '/{:02d}/'.format(i + 1) + j, 'r')
        read = csv.reader(traj_file)
        for k in read:
            data.append(k)
        traj_file.close
        csv_frame.append(data[-1][0])

    traj_line.append(max(csv_frame)) # 파일당 csv line
    print(traj_line[i])

# json_data
# list of json file
for name in file_list:
    with open(path_dir + '/' + name, 'r') as f:
        json_data.append(json.load(f))

for i in range(len(file_list)):
    # 
    block = len(json_data[i]['block_information'])
    npy = []

    # file name
    name = file_list[i]
    name = name.replace("_blockinfo.json", "")

    cnt = 0
    
    for j in range(block):
        frame_level_masks = 0
        start = int(json_data[i]['block_information'][j]['start_frame_index'])
        end = int(json_data[i]['block_information'][j]['end_frame_index']) + 1

        if (json_data[i]['block_information'][j]['block_type'] == 'action'):
            frame_level_masks = 1
        elif (json_data[i]['block_information'][j]['block_type'] == 'symptom'):
            frame_level_masks = 1

        for k in range(start, end):
            npy.append(frame_level_masks)
            cnt += 1
    
    for j in range(int(traj_line[i]) - cnt + 1):
        npy.append(0)
        
    npy = np.array(npy)
    #np.save(path_dir + '/' + name + '.npy', npy)
    np.save(save_dir + '/' + '01_{:02d}.npy'.format(i + 1), npy)
    # 저장위치 변경 가능, path_dir만 변경 가능
