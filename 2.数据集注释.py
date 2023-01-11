# 给数据注释，分类，贴标签，用图片名称来分类注释
import os
import re
import pandas as pd

def getFileList(file_path):
    file_list = []
    for root, dirs, files in os.walk(file_path):
        for file in files:
            matchObj = re.match(r'~$', file, re.I)
            if not matchObj:
                if os.path.splitext(file)[1] in [".jpg", ".png"]:
                    file_list.append(os.path.join(file))
    return file_list

def classifier(freetext):
    if re.search(r"cat", freetext):
        return 0
    elif re.search(r"car", freetext):
        return 1

# training set
file_path = "./images"
file_list = getFileList(file_path)
df = pd.DataFrame(file_list)
df.columns = ['name']   # 查看标签

df['label'] = df['name'].apply(lambda x: classifier(x))    # 分类别用lambda函数
df.to_csv("./excel/annotations_cat_car.csv", index=False)   # 针对文件名输出一个标签，输出csv文件，做了一个分类

# test set
file_path = "./images_test"
file_list = getFileList(file_path)
df = pd.DataFrame(file_list)
df.columns = ['name']
df['label'] = df['name'].apply(lambda x: classifier(x))
df.to_csv("./excel/annotations_cat_car_test.csv", index=False)


# 上面两个步骤，是对训练集和测试集分类

