import pathlib

import pytesseract.pytesseract
from PIL import Image

PATH_TO_TESSERACT = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def parse_image(path_to_image):
    with Image.open(path_to_image) as image:
        pytesseract.pytesseract.tesseract_cmd = PATH_TO_TESSERACT
        return pytesseract.image_to_string(image)


if __name__ == "__main__":
    print(parse_image(pathlib.Path(__file__).parent / "test.JPG")[:-1])
