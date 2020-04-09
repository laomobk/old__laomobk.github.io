import os
from PIL import Image

imgp_list = [path for path in os.listdir('.') if path[-4:] == '.png']

def open_all_image():
    return [Image.open(path) for path in imgp_list]


def save_all_image(imgs):
    for img, path in zip(imgs, imgp_list):
        path = path[:-4] + '.jpg'
        print('Saving...', path)
        img.save('E:\\imgs\\' + path, quality=25)

save_all_image(open_all_image())
