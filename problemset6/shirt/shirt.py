import os, sys
from PIL import Image


def main():
    paste_image(validate_args()[0], validate_args()[1])

def paste_image(back, final):
    try:
        with  Image.open(back) as backImage, Image.open("shirt.png") as shirt:
            backImage = backImage.convert("RGBA")
            shirt = shirt.convert("RGBA")
            backImage.paste(shirt)
            backImage = backImage.convert("RGB")
            backImage.save(final)
    except FileNotFoundError:
        sys.exit("File does not exist")



def validate_args():

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    filename2 = sys.argv[2]
    filename1 = sys.argv[1]
    if filename1.lower().endswith((".jpg", "png", "jpeg")):
        if filename2.lower().endswith((".jpg", "png", "jpeg")):
            if os.path.splitext(filename1)[1] == os.path.splitext(filename2)[1]:
                return [filename1, filename2]
            else:
                sys.exit("jdjdj")
        else:
            sys.exit("Invalid output")
    else:
        sys.exit("This file is not a picture.")


if __name__ == "__main__":
    main()
