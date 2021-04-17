#!/usr/bin/python
#!/usr/bin/python3
#!/usr/bin/env python
#!/usr/bin/env python3
# -*- coding: utf8 -*-


# author               :- Md Jabed Ali(jabed)


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import subprocess
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re
import shlex
import sys
import os
import io
import time
import glob
import platform
from PyQt5.QtCore import Qt
import pyscreenshot as ImageGrab

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(542, 360)
        Form.setFixedSize(542, 386)
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(21, 20, 90, 25))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(431, 20, 90, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setToolTip('Entire Screen.')  
        
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 20, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setToolTip('Select region.')  
        
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(125, 20, 110, 25))
        self.comboBox.setObjectName("comboBox")
        #language_list = ["Select ", "Afrikaans", "Amharic", "Arabic", "Assamese", "Bengali"]
        a = '''['Select Language', '', 'afr', 'Afrikaans', '', 'amh', 'Amharic', '', 'ara', 'Arabic', '', 'asm', 'Assamese', '', 'aze', 'Azerbaijani', '', 'aze_cyrl', 'Azerbaijani - Cyrillic', '', 'bel', 'Belarusian', '', 'ben', 'Bengali', '', 'bod', 'Tibetan', '', 'bos', 'Bosnian', '', 'bul', 'Bulgarian', '', 'cat', 'Catalan; Valencian', '', 'ceb', 'Cebuano', '', 'ces', 'Czech', '', 'chi_sim', 'Chinese - Simplified', '', 'chi_tra', 'Chinese - Traditional', '', 'chr', 'Cherokee', '', 'cym', 'Welsh', '', 'dan', 'Danish', '', 'deu', 'German', '', 'dzo', 'Dzongkha', '', 'ell', 'Greek, Modern (1453-)', '', 'eng', 'English', '', 'enm', 'English, Middle (1100-1500)', '', 'epo', 'Esperanto', '', 'est', 'Estonian', '', 'eus', 'Basque', '', 'fas', 'Persian', '', 'fin', 'Finnish', '', 'fra', 'French', '', 'frk', 'German Fraktur', '', 'frm', 'French, Middle (ca. 1400-1600)', '', 'gle', 'Irish', '', 'glg', 'Galician', '', 'grc', 'Greek, Ancient (-1453)', '', 'guj', 'Gujarati', '', 'hat', 'Haitian; Haitian Creole', '', 'heb', 'Hebrew', '', 'hin', 'Hindi', '', 'hrv', 'Croatian', '', 'hun', 'Hungarian', '', 'iku', 'Inuktitut', '', 'ind', 'Indonesian', '', 'isl', 'Icelandic', '', 'ita', 'Italian', '', 'ita_old', 'Italian - Old', '', 'jav', 'Javanese', '', 'jpn', 'Japanese', '', 'kan', 'Kannada', '', 'kat', 'Georgian', '', 'kat_old', 'Georgian - Old', '', 'kaz', 'Kazakh', '', 'khm', 'Central Khmer', '', 'kir', 'Kirghiz; Kyrgyz', '', 'kor', 'Korean', '', 'kur', 'Kurdish', '', 'lao', 'Lao', '', 'lat', 'Latin', '', 'lav', 'Latvian', '', 'lit', 'Lithuanian', '', 'mal', 'Malayalam', '', 'mar', 'Marathi', '', 'mkd', 'Macedonian', '', 'mlt', 'Maltese', '', 'msa', 'Malay', '', 'mya', 'Burmese', '', 'nep', 'Nepali', '', 'nld', 'Dutch; Flemish', '', 'nor', 'Norwegian', '', 'ori', 'Oriya', '', 'pan', 'Panjabi; Punjabi', '', 'pol', 'Polish', '', 'por', 'Portuguese', '', 'pus', 'Pushto; Pashto', '', 'ron', 'Romanian; Moldavian; Moldovan', '', 'rus', 'Russian', '', 'san', 'Sanskrit', '', 'sin', 'Sinhala; Sinhalese', '', 'slk', 'Slovak', '', 'slv', 'Slovenian', '', 'spa', 'Spanish; Castilian', '', 'spa_old', 'Spanish; Castilian - Old', '', 'sqi', 'Albanian', '', 'srp', 'Serbian', '', 'srp_latn', 'Serbian - Latin', '', 'swa', 'Swahili', '', 'swe', 'Swedish', '', 'syr', 'Syriac', '', 'tam', 'Tamil', '', 'tel', 'Telugu', '', 'tgk', 'Tajik', '', 'tgl', 'Tagalog', '', 'tha', 'Thai', '', 'tir', 'Tigrinya', '', 'tur', 'Turkish', '', 'uig', 'Uighur; Uyghur', '', 'ukr', 'Ukrainian', '', 'urd', 'Urdu', '', 'uzb', 'Uzbek', '', 'uzb_cyrl', 'Uzbek - Cyrillic', '', 'vie', 'Vietnamese', '', 'yid', 'Yiddish', '']'''
        a = a.split(', \'\',')
        
        for language_list in a:
            language  = str(language_list).replace('\'',' ').replace('[',' ').replace(']',' ')
            #language_list_ = str(re.findall('\', \'(.*?)\'', str(language_list), re.DOTALL)[0])
            
            self.comboBox.addItem(language)
        self.comboBox.setCurrentIndex(1)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(19, 68, 501, 251))
        self.textEdit.setObjectName("textEdit")

        self.textEdit.setPlainText('Snipping tools with region select supported and (OCR) optical character recognition supported ')
        
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 350, 89, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 350, 89, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 330, 411, 17))
        self.label.setObjectName("label")
        self.label.setText('''<b> Source : </b><a href='https://github.com/jabedparadox' style=\"text-decoration:none;\">Snipping Tool (tesseract ocr ). </a>''')
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 354, 180, 20))
        self.label_2.setObjectName("label")
        self.label_2.setText('''<b> Prepared : </b><a href='https://github.com/jabedparadox' style=\"text-decoration:none;\">Jabed. </a>''')
        self.label_2.setOpenExternalLinks(True)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.pushButton.clicked.connect(self.osinfo)
        self.pushButton_2.clicked.connect(self.Snipsht)
        self.pushButton_3.clicked.connect(self.Snip)
        self.pushButton_4.clicked.connect(self.exit_app)
        self.pushButton_5.clicked.connect(self.tesscart)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Snipping Tool. v1.0.0"))
        self.pushButton.setText(_translate("Form", "Os Info"))
        self.pushButton_2.setText(_translate("Form", "Screenshot"))
        self.pushButton_3.setText(_translate("Form", "Take Snip"))
        self.pushButton_4.setText(_translate("Form", "Exit"))
        self.pushButton_5.setText(_translate("Form", "Get Text")) 
        
    def osinfo(self):
        info = 'Platform : ' + platform.system() + '\n' + 'Platform release : ' + platform.release() + '\n' + 'Platform version : ' +    platform.version() + '\n' + 'Architecture : ' + platform.machine()
        self.textEdit.setPlainText(info)
    
    def Snip(self):
        #escrotum --select  FILENAME.png
        #pip install escrotum
	#pip install vext
	#pip install vext.gi
        self.snipper = Snipper()
        #self.snipper.showFullScreen()
        self.snipper.show()
       
   
    def tesscart (self):
        #self.scrnsht = subprocess.Popen(shlex.split('gnome-screenshot -a filename.png'), stdout=subprocess.PIPE)
        #self.scrnsht.communicate()
        a = os.getcwd()+'/*.png'
        list_of_files = glob.glob(a)
        latest_file =  max(list_of_files, key=os.path.getctime).split('/')[-1]
        lang = str(self.comboBox.currentText()).split(',')[0]   
        #https://ocrmypdf.readthedocs.io/en/latest/languages.html
        #https://github.com/tesseract-ocr/tessdata/ and place it in C:\\Program Files\\Tesseract-OCR\\tessdata   
        #sudo apt-get install tesseract-ocr-language eg: eng / all  
        #
        shell = 'tesseract ' + latest_file + ' stdout ' + '-l ' + lang
        self.proc_=subprocess.Popen(shlex.split(shell), stdout=subprocess.PIPE)
        self.proc_ = self.proc_.communicate()
        self.textEdit.setPlainText(list(self.proc_)[0].decode("utf-8"))
    
    def exit_app(self):
        sys.exit()
    
    def Snipsht (self):
        img = ImageGrab.grab()
        fname = "Screenshot from {}.png".format(time.strftime("%Y%m%d-%H.%M.%S"))
        #loc = 'Image Location : ' + os.getcwd() + '/' + fname
        #self.textEdit.setPlainText(loc)
        
        msg = QMessageBox()
        
        msg.setIcon(QMessageBox.Information)
        msg.setText("Image Saved At - ")
        loca = os.getcwd()
        loca += "\n\n"+ fname
        msg.setInformativeText(loca)
        msg.setWindowTitle("Info")
        msg.exec_()
        
        #self.label_2.setWordWrap(True)
        #print ()
        img.save(fname)


class Snipper(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.setWindowTitle("TextShot")
        self.setWindowFlags(
            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Dialog
        )
        self.setWindowState(self.windowState() | Qt.WindowFullScreen)

        self.screen = QtWidgets.QApplication.screenAt(QtGui.QCursor.pos()).grabWindow(0)
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(self.screen))
        self.setPalette(palette)

        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))

        self.start, self.end = QtCore.QPoint(), QtCore.QPoint()
        self.close()
           
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            QtWidgets.QApplication.quit()

        return super().keyPressEvent(event)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QtGui.QColor(0, 0, 0, 100))
        painter.drawRect(0, 0, self.width(), self.height())

        if self.start == self.end:
            return super().paintEvent(event)

        painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255), 3))
        painter.setBrush(painter.background())
        painter.drawRect(QtCore.QRect(self.start, self.end))
        return super().paintEvent(event)

    def mousePressEvent(self, event):
        self.start = self.end = event.pos()
        self.update()
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if self.start == self.end:
            return super().mouseReleaseEvent(event)

        self.hide()
        QtWidgets.QApplication.processEvents()
        shot = self.screen.copy(QtCore.QRect(self.start, self.end))
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QBuffer.ReadWrite)
        shot.save(buffer, "PNG")
        self.pil_img = Image.open(io.BytesIO(buffer.data()))
        self.f_name = "Snip_shot_{}.png".format(time.strftime("%Y%m%d-%H.%M.%S"))
        self.pil_img.save(self.f_name)
        buffer.close()
        QtWidgets.QApplication.restoreOverrideCursor();
        self.close()

        msg = QMessageBox()
        
        msg.setIcon(QMessageBox.Information)
        msg.setText("Image Saved At.")
        loca = os.getcwd()
        loca += "\n\n"+ self.f_name
        msg.setInformativeText(loca)
        msg.setWindowTitle("Info")
        msg.exec_()
        #QtWidgets.QApplication.quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
 
