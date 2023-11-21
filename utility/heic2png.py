import os
from PIL import Image
from pillow_heif import register_heif_opener
import typeCheck

def heic2png():
    register_heif_opener()
    path = input('Input file or path: ')
    if typeCheck.isHeic(path):
        image = Image.open(path)
        image.save(os.path.splitext(path)[0] + '.png')
    elif typeCheck.isDirectory(path):
        files = [f for f in os.listdir(path) if f.endswith('.heic')]
        for filename in files:
            image = Image.open(os.path.join(path, filename))
            image.save(os.path.join(path, os.path.splitext(filename)[0] + '.png'))
    else:
        raise ValueError('Input must be a valid image or directory.')
    print('File converted successfully')

# path = 'data/'
if __name__ == '__main__':
    heic2png()
