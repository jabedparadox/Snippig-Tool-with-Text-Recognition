# Snipping-Tool-with-Text-Recognition
Snipping tools with ocr supported


## How it works
[![video](https://github.com/jabedparadox/Snipping-Tool-with-Text-Recognition/blob/main/snip.gif)](https://drive.google.com/file/d/1XHuolvyJQrRRe9rXFiLc_ZrxuUKok2fK/view)


## Operating System  

* Linux
* Windows

## Installation

### Linux

 - Install/Update python, preferably latest version as of (Python 3.9.4)
 - Install 'tesseract' (```sudo apt-get install tesseract-ocr```) and required dependency for tesseract.
 - Install 'Pyqt5' (```pip install PyQt5```) assuming python & pip is installed.
 - Install 'pyscreenshot' (```pip install pyscreenshot```) assuming python & pip is installed.
 - Install 'Pillow' (```pip install Pillow```) assuming python & pip is installed.
 - Tesseract Language eg: for bengali language
   sudo apt-get install tesseract-ocr-language
   eg:```sudo apt-get install tesseract-ocr-ben```
      ```sudo apt-get install tesseract-ocr-all ```

### Windows

 - Donwload python Installer from 
   Use [Installer](https://www.python.org/downloads/windows/) and isntall
 - After installing set python to system environment variable & set prefix.
 - Donwload tesseract Installer from
   [tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
   [tesseract](https://tesseract-ocr.github.io/tessdoc/Downloads.html)
 - After installing set tesseract to system environment variable.
 - Tesseract Language file from eg: for bengali language donwnload 'ben.traineddata' 
   and place it to 'C:\Program Files\Tesseract-OCR\tessdata'
   

## Feature  

### v1.0.0

* Text Recognition
* Language
* Area selection of screen
* Entire screen

## Image improving

For better text recognition performance from noisy image or colorod image etc, thresholding of an image [thresholding process is separating an image into       foreground values (black) and background values (white).] is good enough. By 'opencv-python' module in python this can be done. Installation
  ```pip install opencv-python``` 
 [Details thresholding](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html)
  

## Contributing

* Fork the project.
* [GitHub Issues](https://github.com/jabedparadox/Snipping-Tool-with-Text-Recognition/issues)
* For any suggestion :
* Facebook : [Md Jabed Ali](https://www.facebook.com/paradox.jabed)


# License

MIT license.

