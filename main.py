from loader import loader
from renderer import renderer
from setup import setup

devidor = "|--------------------------------|"

def main():
    print("Starting Python Instagram Creator")
    print("Input directory to read from (absolute or relative)")
    directory = input("Source-Directory: ")
    squares = loader.loadDirectory(directory=directory)
    crops = loader.loadDirectory(directory=directory)

    squares = renderer.makeSquare(images=squares)
    crops = renderer.crop(images=crops)
    merges = renderer.mergeImages(squares=squares, crops=crops)
    print(f"Set the destination for the files, current destination: {setup.destination}")
    destination = input("Destination Location: ")
    renderer.render(merges, destination=destination)

if __name__ == "__main__":
    main()