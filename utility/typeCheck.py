import os

def isImage(filename:str, extension=('.png', '.jpg', '.jpeg', '.bmp', '.dib', 
                                 '.pbm', '.pgm', '.ppm' '.pxm', '.pnm')):
    """ Return True if input image file except for heif, more extension can be added later """
    return filename.endswith(extension)

def isHeic(filename:str, extension='.heic'):
    return filename.endswith(extension)

def isDirectory(path:str):
    return os.path.isdir(path)


