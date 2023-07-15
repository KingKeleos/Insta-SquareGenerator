# Insta-Square Generator

## What it does

This software takes whatever photos you provide in one directory.
Those photos will be read and transformed into a square ratio.
THe background will be filled with a darkened and blurred version of the photo.

## Setup

It is possible to congfigure the software using the 
```bash
setup/setup.py
```
In there, you can configure the following parameters:

```
directory: the directory, that the photos are being read off of
size: the size of the square images (default: 1000)
factor: the factor with which the image brightness will be altered
destination: directory, in which the photos should be generated into
blur: amount of blur
```

THe description, of how to set these parameters is also described in the `setup.py`

## Be Aware

This software is just there to create the square images.
It will not take care of your photos.
It will also overwrite the photos, if you put the same directory for source and destination.
Also the files in the destination directory will be overwritten, as the names are just generated through a counter.

## How to run

You can easily start the software using `python`
using the command 
```
python main.py
```
while being in the directory of the files, it will be executed.