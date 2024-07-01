import json
import numpy as np
import os

json_data = []

path_dir = './E2ON_C021/C021_test/check'
file_list = os.listdir(path_dir) #json files
file_list.sort()

for name in file_list:
    with open(path_dir + '/' + name, 'r') as f:
        json_data.append(json.load(f)) # 1-1, 2-1, 4-1 ... 706-1

for j in range(len(file_list)):
    persons = 0
    #os.mkdir('./E2ON/csv/'+file_list[j].split('_')[0]+'/'+file_list[j].replace(".json", "")) #./AI-Hub_CSV2/1-1 ... ./AI-Hub_CSV2/706-1
    os.mkdir('./E2ON_C021/csv/'+'{:02d}'.format(j + 1))

    for i in range(len(json_data[j]['frames'])): # frame[0] ~ frame[i]
        if (len(json_data[j]['frames'][i]['persons']) > persons): # find max
            persons = len(json_data[j]['frames'][i]['persons']) # max
    
    for m in range(persons): # 0, 1, 2, ..., persons-1
        line = []
        for i in range(len(json_data[j]['frames'])): # save information of person_index m
            point = []
            if(len(json_data[j]['frames'][i]['persons']) > m):
                point.append('{}'.format(json_data[j]['frames'][i]['frame_index'])) # frame index
                for k in range(2): # 0
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][0].split(',')[k])))))
                for k in range(2): # 1
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][5].split(',')[k])))))
                    #point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][15].split(',')[k])))))
                    #point.append('{}'.format(str(0)))
                for k in range(2): # 2
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][5].split(',')[k])))))
                    #point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][16].split(',')[k])))))
                    #point.append('{}'.format(str(0)))
                for k in range(2): # 3
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][5].split(',')[k])))))
                    #point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][17].split(',')[k])))))
                    #point.append('{}'.format(str(0)))
                for k in range(2): # 4
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][5].split(',')[k])))))
                    #point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][18].split(',')[k])))))
                    #point.append('{}'.format(str(0)))
                for k in range(2): # 5
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][5].split(',')[k])))))
                for k in range(2):
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][2].split(',')[k])))))
                for k in range(2):
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][6].split(',')[k])))))
                for k in range(2):
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][3].split(',')[k])))))
                for k in range(2):
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][7].split(',')[k])))))
                for k in range(2):
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][4].split(',')[k])))))
                for k in range(2):
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][12].split(',')[k])))))
                for k in range(2):
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][9].split(',')[k])))))
                for k in range(2):
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][13].split(',')[k])))))
                for k in range(2):
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][10].split(',')[k])))))
                for k in range(2):
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][14].split(',')[k])))))
                for k in range(2):
                    point.append('{}'.format(str(round(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][11].split(',')[k])))))
                    
                line.append(point)

        line = np.array(line)
        #np.savetxt('./AI-Hub_CSV2/'+file_list[j].split('_')[0]+'/'+'{:04d}.csv'.format(m+1), line, fmt="%s", delimiter=",")
        #np.savetxt('./E2ON/csv/'+file_list[j].split('_')[0]+'/'+file_list[j].replace(".json", "")+'/'+'{:04d}.csv'.format(m+1), line, fmt="%s", delimiter=",")
        np.savetxt('./E2ON_C021/csv/'+'{:02d}'.format(j + 1)+'/'+'{:04d}.csv'.format(m+1), line, fmt="%s", delimiter=",")