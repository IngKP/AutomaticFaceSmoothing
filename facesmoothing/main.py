import utility.typeCheck
import smoothing.smoothing
import os

def main(imagePath:str):
    count = 0
    if utility.typeCheck.isImage(imagePath):
        smoothing.smoothing.smoothing(imagePath)
        count += 1
    elif utility.typeCheck.isDirectory(imagePath):
        for path in os.listdir(imagePath):
            if utility.typeCheck.isImage(path):
                smoothing.smoothing.smoothing(os.path.join(imagePath, path))
                count += 1
    else:
        raise ValueError('Input must be a valid image or directory.')
    print(f'{count} file(s) converted successfully')

if __name__ == '__main__':
    imagePath = input('input image file or directory: ')
    main(imagePath)
    