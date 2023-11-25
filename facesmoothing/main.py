import utility.typeCheck
import smoothing
import os

def main(imagePath: str, d: int = 9, 
         sigmaColor: float = 75, sigmaSpace: float = 75):
    """
    """
    count = 0
    if utility.typeCheck.isImage(imagePath):
        smoothing.smoothing(imagePath, d, sigmaColor, sigmaSpace)
        count += 1
    elif utility.typeCheck.isDirectory(imagePath):
        for path in os.listdir(imagePath):
            if utility.typeCheck.isImage(path):
                smoothing.smoothing(os.path.join(imagePath, path), 
                                              d, sigmaColor, sigmaSpace)
                count += 1
    else:
        raise ValueError('Input must be a valid image or directory.')
    print(f'{count} file(s) converted successfully')

if __name__ == '__main__':
    imagePath = input('input image file or directory: ')
    d, sigmaColor, sigmaSpace = input('input d, sigmaColor, sigmaSpace: ')
    main(imagePath, d, sigmaColor, sigmaSpace)
    