import os
import random
import shutil
from tqdm import tqdm


def move(src_path,cat_path,dog_path):
    All_files = os.listdir(src_path)    #读取原路径下的所有文件，即图片
    length = len(All_files)
    cat,dog,i = 0,0,0
    while i < 5000:
        number = random.randint(0,length)   #生成随机数
        img_name = All_files[number]        #从图片中随机选择一个图片
        name = img_name.split('.')[0]   #根据图片名按 '.'分成段，如cat.1.jpg，即'cat'，'1','jpg'  0对应'cat',以此类推
        try:        #加报警检测机制，如果有重复的，不报错直接跳过
            if name == 'cat':      
                if cat < 2500:
                    shutil.move(src_path + '\\' +img_name, cat_path) #剪切到目标路径
                    cat = cat + 1
                    length = length - 1     #成功剪切一次后，总数减1
                    i = i + 1
            else:
                if dog < 2500:
                    shutil.move(src_path + '\\' +img_name, dog_path)
                    dog = dog + 1
                    length = length - 1
                    i = i + 1
            if cat == 2500 & dog ==2500:
                break
        except shutil.Error:
            i = i - 1   #若剪切不成功，则此次不加1
            continue

if __name__ == "__main__":
    move("E:\\deep_learning\\PycharmProjects\\pythonProject\\dogs-vs-cats\\test1",       #原目标文件夹
         "E:\\deep_learning\\PycharmProjects\\pythonProject\\dogs-vs-cats\\test1\\cat",        #猫
         "E:\\deep_learning\\PycharmProjects\\pythonProject\\dogs-vs-cats\\test1\\dog")        #狗