import PIL.Image as image_read
import pytesseract as pyt
from gtts import gTTS
import os

pyt.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def convert():
    img=image_read.open('dumb.jpeg')
    text=pyt.image_to_string(img)
    
    new_text = ""
    for word in text:
        if word is not "\n":
            new_text+=word
        if word is ".":
            new_text += '\n'
    text=new_text
    with open("some.txt","w") as fp:
        fp.write(text)
    
    
    with open("some.txt", "r") as fp:
        new_text=fp.read()
    

    print(new_text)
    tt = gTTS(new_text, lang='en',slow=False,tld="ca")
    tt.save("good.mp3")
    os.system("start good.mp3")
convert()
