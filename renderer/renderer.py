from setup import setup
from PIL import Image, ImageFilter, ImageEnhance
import os

def makeSquare(images):
    squares = []
    k = 0
    for i in images:
        print(f"Generating Thumbnails fitting for size {setup.size}")
        i.thumbnail((setup.size, setup.size))
        squares.append(i)
        k+=1
    return squares

def crop(images):
    crops = []
    k = 0
    for i in images:
        if checkLandscape(i):
            c = cropLandscape(i)
        else:
            c = cropPortrait(i)
        crops.append(c)
        k+=1
    return crops

def cropLandscape(image):
    width, height = image.size
    
    hsize = (setup.size/float(height))
    wpercent = int((float(width)*float(hsize)))

    resize = image.resize((wpercent, setup.size))
    blur = blurImage(image=resize)

    dark = darkenImage(blur)

    left = (dark.size[0] - setup.size)/2
    right = (dark.size[0] + setup.size)/2

    c = dark.crop((left, 0, right, setup.size))
    return c

def cropPortrait(image):
    width, height = image.size
    
    wpercent = (setup.size/float(width))
    hsize = int((float(height)*float(wpercent)))

    resize = image.resize((hsize, setup.size))
    blur = blurImage(image=resize)

    dark = darkenImage(blur)

    left = (dark.size[0] - setup.size)/2
    right = (dark.size[0] + setup.size)/2

    c = dark.crop((left, 0, right, setup.size))
    return c

def mergeImages(squares, crops):
    print(f"Merging crops and Squares...")
    merges = []
    sq = 0
    for c in crops:
        if checkLandscape(squares[sq]):
            mask = generateMaskLandscape(squares[sq])
        else:
            mask = generateMaskPortrait(squares[sq])
        c.paste(mask, (0, 0), mask)
        sq += 1
        merges.append(c)
    return merges

def checkLandscape(image):
    if image.size[0] > image.size[1] or image.size[0] == image.size[1]:
        return True
    else:
        return False

def blurImage(image):
    blur = image.filter(ImageFilter.GaussianBlur(setup.blur))
    return blur

def darkenImage(image):
    factor = setup.factor
    enhancer = ImageEnhance.Brightness(image=image)
    output = enhancer.enhance(factor=factor)
    return output

def generateMaskLandscape(thumb):
    mask = thumb
    margin = int((setup.size - mask.size[1])/2)
    mask = add_margin(mask, margin, 0, margin, 0)
    return mask

def generateMaskPortrait(thumb):
    mask = thumb
    margin = int((setup.size - mask.size[0])/2)
    mask = add_margin(mask, 0, margin, 0, margin)
    return mask

def add_margin(pil_img, top, right, bottom, left):
    if not top == bottom:
        bottom += 1
    if not right == left:
        right += 1
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(mode="RGBA", size=(new_width, new_height), color=(0,0,0,0))
    result.paste(pil_img, (left, top))
    return result

def render(images, destination):
    if destination == "":
        destination = setup.destination
    k = 0
    for i in images:
        k += 1
        destination = os.path.join(setup.destination, f"instagram_{k}.png")
        i.save(destination)