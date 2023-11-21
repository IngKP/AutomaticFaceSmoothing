import os

# more extension can be added
def isImage(filename:str, extension=('.png', '.jpg', '.jpeg', '.bmp', '.dib', 
                                 '.pbm', '.pgm', '.ppm' '.pxm', '.pnm')):
    return filename.endswith(extension)

def isHeic(filename:str, extension='.heic'):
    return filename.endswith(extension)

def isDirectory(path:str):
    return os.path.isdir(path)


