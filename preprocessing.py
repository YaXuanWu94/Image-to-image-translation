import os
import shutil
from PIL import Image

river = './river/pix2pixHD/datasets/cityscapes'
road = './road/pix2pixHD/datasets/cityscapes'

# train
train = './training_dataset'
for i in os.listdir(os.path.join(train, 'label_img')):
    if i[4:6] == 'RI':
        # train_A
        label_img = Image.open(os.path.join(train, 'label_img', i))
        label_img = label_img.resize((1024, 512))
        label_img.save(os.path.join(river, 'train_A', i))
        # train_B
        img = Image.open(os.path.join(train, 'img', i[:-4] + '.jpg'))
        img = img.resize((1024, 512))
        img.save(os.path.join(river, 'train_B', i[:-4] + '.jpg'))
        
    elif i[4:6] == 'RO':
        # train_A
        label_img = Image.open(os.path.join(train, 'label_img', i))
        label_img = label_img.resize((1024, 512))
        label_img.save(os.path.join(road, 'train_A', i))
        # train_B
        img = Image.open(os.path.join(train, 'img', i[:-4] + '.jpg'))
        img = img.resize((1024, 512))
        img.save(os.path.join(road, 'train_B', i[:-4] + '.jpg'))

# test
test = './private_testing_dataset'
for i in os.listdir(test):
    if i[4:6] == 'RI':
        # test_A
        label_img = Image.open(os.path.join(test, i))
        label_img = label_img.resize((1024, 512))
        label_img.save(os.path.join(river, 'test_A', i))
        
    elif i[4:6] == 'RO':
        # test_A
        label_img = Image.open(os.path.join(test, i))
        label_img = label_img.resize((1024, 512))
        label_img.save(os.path.join(road, 'test_A', i))
