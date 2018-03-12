import pytesseract
from PIL import Image

image = Image.open(r'D:\Anaconda\test\tesseracttest.jpg')
text = pytesseract.image_to_string(image)
print(text)