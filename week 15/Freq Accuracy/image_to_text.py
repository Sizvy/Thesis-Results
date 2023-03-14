# import the following libraries
# will convert the image to text string
import pytesseract	

# adds image processing capabilities
from PIL import Image	

# converts the text to speech
import pyttsx3			

# opening an image from the source path
for i in range(1,101):
    img = Image.open('benign ' + str(i) + '.png')	

    # describes image format in the output
    print(img)						
    # path where the tesseract module is installed
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
    # converts the image to result and saves it into result variable
    result = pytesseract.image_to_string(img)
    # write text in a text file and save it to source path
    with open('benign ' + str(i) + '.txt',mode ='w') as file:	
        file.write(result)
        #print(result)
				

