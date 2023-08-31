import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

test = Image.open('./Untitled.png')

result = pytesseract.image_to_string(test,lang='kor')

print(result)