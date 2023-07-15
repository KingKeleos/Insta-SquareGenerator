from loader import loader
from renderer import renderer
from setup import setup
import os

devidor = "|--------------------------------|"

def main():
    print("Starting Python Instagram Creator")
    print("Input directory to read from (absolute or relative)")
    directory = input("Source-Directory: ")

    if directory == "":
        print("No input of directory, using default location")
        directory = setup.directory
    if not os.path.exists(directory):
        print(f"Location {directory} does not exist... creating")
        os.makedirs(directory)

    squares = loader.loadDirectory(directory=directory)
    crops = loader.loadDirectory(directory=directory)

    squares = renderer.makeSquare(images=squares)
    crops = renderer.crop(images=crops)
    merges = renderer.mergeImages(squares=squares, crops=crops)
    print(f"Set the destination for the files, current destination: {setup.destination}")
    destination = input("Destination Location: ")

    if destination == "":
        print("No input of directory, using default location")
        destination = setup.destination
    if not os.path.exists(destination):
        print(f"Location {destination} does not exist... creating")
        os.makedirs(destination)

    renderer.render(merges, destination=destination)

if __name__ == "__main__":
    main()