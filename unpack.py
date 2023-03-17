from db import DB
import os
from preset import picturesfolder

daba = DB()
if picturesfolder.split('\\')[-2] not in os.listdir():
    os.mkdir(picturesfolder)
for i in range(28):
    print(i)
    pic = daba.get_pictureb(i+1)
    file = open(picturesfolder + str(i+1) + '.jpg', 'wb')
    file.write(pic)
    file.close()
daba.clear()
print(daba.get_user(1))
