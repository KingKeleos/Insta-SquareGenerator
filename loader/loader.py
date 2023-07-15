import os
from PIL import Image
from setup import setup


def loadDirectory(directory):
    try:
        images = listDirectory(directory)
        return images
    except:
        print(f"Could not find files for directory {directory}")

def listDirectory(directory):
    images = []
    for root, dirs, files in os.walk(directory, topdown=False):
        print(f"Loading files from {directory}")
        for name in files:
            print(f"Found File: {os.path.join(root, name)}")
            im = Image.open(os.path.join(root, name))
            images.append(im)
    
    if len(images) == 0:
        print("Unable to find any images.")
    return images
    