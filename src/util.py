import cv2
import numpy as np
import json
import os


def generate_show_img(img_list):
    show_img = np.zeros((900,900,3),dtype=np.uint8)+255
    for idx,img in enumerate(img_list):
        row = idx // 3
        col = idx % 3
        show_img[row*300:(row+1)*300, col*300:(col+1)*300,:]=img
    return show_img

def load_images(file_path, item_set):
    img_list = []
    for it in item_set:
        item_id = it['item_id']
        img = cv2.imread(os.path.join(file_path,item_id+'.jpg'))
        img_list.append(img)
        print(item_id)
    return img_list

class DataLoader(object):
    def __init__(self, json_path, save_path):
        with open(json_path, 'r') as f:
            self.annotations = json.load(f)
        self.save_path = save_path
        self.id_set = set(self.annotations.keys())
        self.total_num = len(self.annotations.keys())
        self.cur_num_left = self.total_num

    def get_data(self):
        set_id = self.id_set.pop()
        self.cur_num_left = len(self.id_set)
        return self.annotations[set_id]

        


if __name__ == '__main__':
    # im_list = []
    # for i in range(5):
    #     img = cv2.imread('/home/rangilyu/Pictures/{}.jpg'.format(i))
    #     img = cv2.resize(img,(300,300))
    #     im_list.append(img)
    # showimg = generate_show_img(im_list)
    # cv2.imshow('111', showimg)
    # cv2.waitKey(0)
    json_path = '/home/rangilyu/Projects/data_mark_tool_Qt5GUI/demo/data/set_item2.json'
    img_folder = '/home/rangilyu/Projects/data_mark_tool_Qt5GUI/demo/data/images'
    datalodaer = DataLoader(json_path, './')
    while datalodaer.cur_num_left > 0:
        data = datalodaer.get_data()
        print(data)
        img_list = load_images(img_folder, data)
        showimg = generate_show_img(img_list)
        cv2.imshow('111', showimg)
        cv2.waitKey(0)
