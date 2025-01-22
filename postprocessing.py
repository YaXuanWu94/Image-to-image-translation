import os
from PIL import Image

river = './river/pix2pixHD/results/RIVER/test_latest/images'
road = './road/pix2pixHD/results/ROAD/test_latest/images'
target = './private_output'


# river
for i in os.listdir(river):
    if i[15:16] == 's':
        img = Image.open(os.path.join(river, i))
        img = img.resize((428, 240))
        img.save(os.path.join(target, i[0:14] + '.jpg'))
# road
for i in os.listdir(road):
    if i[15:16] == 's':
        img = Image.open(os.path.join(road, i))
        img = img.resize((428, 240))
        img.save(os.path.join(target, i[0:14] + '.jpg'))
