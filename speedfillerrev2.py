# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'speedfiller.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pdf_funcions
import csv
import shutil
import os
import pandas
import myres
from PyQt5.QtCore import (pyqtSignal, QBuffer, QByteArray, QFileInfo, QIODevice, QMimeData, QPoint, QSize, Qt)
from PyQt5.QtGui import (qBlue, QColor, QDrag, qGreen, QImage, QKeySequence, QPalette, QPixmap, qRed)
from PyQt5.QtWidgets import (QApplication, QColorDialog, QFileDialog, QFrame, QGridLayout, QLabel, QLayout, QMainWindow, QMenu, QMessageBox, QPushButton, QVBoxLayout)
########small change to test git############
class Ui_Rob(object):
    def setupUi(self, Rob):
        Rob.setObjectName("Rob")
        Rob.resize(546, 690)
        self.centralwidget = QtWidgets.QWidget(Rob)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 30, 271, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, -10, 221, 171))
        self.logo.setObjectName("logo")
        self.Generate = QtWidgets.QPushButton(self.centralwidget)
        self.Generate.setGeometry(QtCore.QRect(180, 590, 171, 31))
        self.Generate.setObjectName("Generate")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 160, 481, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.csvtopdf = QtWidgets.QRadioButton(self.groupBox_2)
        self.csvtopdf.setGeometry(QtCore.QRect(90, 30, 117, 22))
        self.csvtopdf.setObjectName("csvtopdf")
        self.pdftocsv = QtWidgets.QRadioButton(self.groupBox_2)
        self.pdftocsv.setGeometry(QtCore.QRect(280, 30, 117, 22))
        self.pdftocsv.setObjectName("pdftocsv")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 460, 481, 101))
        self.groupBox.setObjectName("groupBox")
        self.generateall = QtWidgets.QRadioButton(self.groupBox)
        self.generateall.setGeometry(QtCore.QRect(10, 30, 117, 22))
        self.generateall.setObjectName("generateall")
        self.generateonly = QtWidgets.QRadioButton(self.groupBox)
        self.generateonly.setGeometry(QtCore.QRect(10, 60, 131, 22))
        self.generateonly.setObjectName("generateonly")
        self.recipelinedit = QtWidgets.QLineEdit(self.groupBox)
        self.recipelinedit.setGeometry(QtCore.QRect(160, 60, 301, 27))
        self.recipelinedit.setText("")
        self.recipelinedit.setObjectName("recipelinedit")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(160, 30, 301, 17))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 240, 481, 191))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pdfselect = QtWidgets.QPushButton(self.groupBox_3)
        self.pdfselect.setGeometry(QtCore.QRect(10, 40, 171, 31))
        self.pdfselect.setObjectName("pdfselect")
        self.csvselect = QtWidgets.QPushButton(self.groupBox_3)
        self.csvselect.setGeometry(QtCore.QRect(10, 90, 171, 31))
        self.csvselect.setObjectName("csvselect")
        self.outputfolder = QtWidgets.QPushButton(self.groupBox_3)
        self.outputfolder.setGeometry(QtCore.QRect(10, 140, 171, 31))
        self.outputfolder.setObjectName("outputfolder")
        self.csvlabel = QtWidgets.QLabel(self.groupBox_3)
        self.csvlabel.setGeometry(QtCore.QRect(200, 100, 261, 17))
        self.csvlabel.setText("")
        self.csvlabel.setObjectName("csvlabel")
        self.pdflabel = QtWidgets.QLabel(self.groupBox_3)
        self.pdflabel.setGeometry(QtCore.QRect(200, 50, 261, 17))
        self.pdflabel.setText("")
        self.pdflabel.setObjectName("pdflabel")
        self.outputlabel = QtWidgets.QLabel(self.groupBox_3)
        self.outputlabel.setGeometry(QtCore.QRect(200, 150, 261, 17))
        self.outputlabel.setText("")
        self.outputlabel.setObjectName("outputlabel")
        Rob.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Rob)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 25))
        self.menubar.setObjectName("menubar")
        Rob.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Rob)
        self.statusbar.setObjectName("statusbar")
        Rob.setStatusBar(self.statusbar)
        self.retranslateUi(Rob)
        QtCore.QMetaObject.connectSlotsByName(Rob)



########################COMMANDS#################################
        self.Generate.setDisabled(True)
        self.csvtopdf.setChecked(True)
        self.generateall.setChecked(True)
        self.pdfselect.clicked.connect(self.getfilepdfpath)
        self.csvselect.clicked.connect(self.getfilecsvpath)
        self.csvtopdf.clicked.connect(self.outputfolder.setEnabled)
        self.pdftocsv.clicked.connect(self.outputfolder.setDisabled)
        self.csvtopdf.clicked.connect(self.groupBox.setEnabled)
        self.pdftocsv.clicked.connect(self.groupBox.setDisabled)
        self.outputfolder.clicked.connect(self.getoutputfolder)
        self.Generate.clicked.connect(self.genbut)
        global pdfpath
        global csvpath
        global outputpath
        pdfpath = None
        csvpath = None
        outputpath = None


    def getfilepdfpath(self, master):
        global pdfpath
        if self.csvtopdf.isChecked():
            extensions = "PDF (*.pdf)"
            pdfpath, x = QtWidgets.QFileDialog.getOpenFileName(None, "Open files","", extensions)
            name = os.path.basename(pdfpath)
            self.pdflabel.setText(name)
        else:
            pdfpath = QtWidgets.QFileDialog.getExistingDirectory(None,"Select PDF Folder")
            name = os.path.basename(pdfpath)
            self.pdflabel.setText(name)
        self.checkforfiles(master)


    def getfilecsvpath(self, master):
        global csvpath
        extensions = "CSV (*.csv)"
        csvpath, x = QtWidgets.QFileDialog.getOpenFileName(None, "Open files","", extensions)
        name = os.path.basename(csvpath)
        self.csvlabel.setText(name)
        if self.csvtopdf.isChecked() and self.isNotEmpty(csvpath):
            csvfile = open(csvpath)
            reader = csv.DictReader(csvfile)
            counter = 0
            for row in reader:
                counter += 1
            counter = counter-1
            self.label_7.setText(str(counter) + " PDF's will be generated")
        self.checkforfiles(master)

    def getoutputfolder(self, master):
        global outputpath
        outputpath = QtWidgets.QFileDialog.getExistingDirectory(None,"Specify Output Destination")
        name = os.path.basename(outputpath)
        self.outputlabel.setText(name)
        self.checkforfiles(master)

    def genbut(self, master):
        global txtinpt
        txtinpt = self.recipelinedit.text()

        if self.csvtopdf.isChecked():
            if self.generateall.isChecked():
                self.csv_pdf(3)
            else:
                if not txtinpt:
                    self.showMessageBox("Error","Missing recipe name")
                else:
                    self.csv_pdf(4)
                    #Run the program for only this recipe
        else:
            self.pdf_csv(3)


    def csv_pdf(self, master):
        current_directory = os.getcwd()
        final_directory = outputpath
        #if outputpath == "asdasd":
            #error = QtGui.QMessageBOX.question(self, 'Error', "Output Folder not specified.",QtGui.QMessageBox.Ok)
        csvfile = open(csvpath)
        reader = csv.DictReader(csvfile)
        if master == 3:
            for row in reader:
                pdf_funcions.write_pdf(pdfpath, row, row['untitled1'] + '.pdf')
        else:
            for row in reader:
               if row['untitled1'] == self.recipelinedit.text():
                  pdf_funcions.write_pdf(pdf_path, row, row['untitled1'] + '.pdf')
        for fname in os.listdir(current_directory):
            if fname.endswith('.pdf') and fname != os.path.basename(pdfpath) and fname != 'field_names.pdf':
                shutil.move(os.path.join(current_directory, fname), final_directory)
        #os.remove(os.path.join(outputpath, 'Part Number.pdf'))



        #error_dialog = QtWidgets.QErrorMessage()
        #error_dialog.showMessage('PDF(s) are finished generating' )
        #error_dialog.exec_()


    def pdf_csv(self, master):
        pdf_directory = os.getcwd()
        listylist = []
        mydict2 = pdf_funcions.get_fields('BRGDOP22427.pdf')
        d2 = mydict2.keys()
        listylist.append(d2)
        for fname in os.listdir(pdf_directory):
            if fname.endswith('.pdf'):
                mydict = pdf_funcions.get_fields(fname)
                d = mydict.values()
                listylist.append(d)
        with open("parts.csv", 'w') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerows(listylist)

    def fieldnames(self, master):
         fdict = pdf_funcions.get_fields("Robco_Prod_Recipe_Sheet_REV5.pdf")
         listylist = []
         d2 = fdict.keys()
         listylist.append(d2)
         pdf_funcions.write_pdf("Robco_Prod_Recipe_Sheet_REV5.pdf", listylist, "fieldnames.pdf")

    #def updatelabel():


    def checkforfiles(self,master):
        if self.isNotEmpty(pdfpath) and self.isNotEmpty(csvpath) and self.isNotEmpty(outputpath) and self.csvtopdf.isChecked():
            self.Generate.setDisabled(False)
        elif self.isNotEmpty(pdfpath) and self.isNotEmpty(csvpath)and self.pdftocsv.isChecked():
            self.Generate.setDisabled(False)
            print("tru")
        else:
            print("nothing ready")

    def isNotEmpty(self,s):
        return bool(s and s.strip())







    def showMessageBox(self, title, message):
        msgBox=QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Close)
        msgBox.exec_()






















    def retranslateUi(self, Rob):
        _translate = QtCore.QCoreApplication.translate
        Rob.setWindowTitle(_translate("Rob", "sPeeDFiller"))
        self.label.setText(_translate("Rob", "<html><head/><body><p><span style=\" font-size:28pt;\">s</span><span style=\" font-size:36pt; color:#ff0000;\">P</span><span style=\" font-size:28pt;\">ee</span><span style=\" font-size:36pt; color:#ff0000;\">DF</span><span style=\" font-size:28pt;\">iller</span></p></body></html>"))
        self.logo.setText(_translate("Rob", "<html><head/><body><p><img src=\":/pics/R-robco-web2.png\"/></p></body></html>"))
        self.Generate.setText(_translate("Rob", "Generate"))
        self.groupBox_2.setTitle(_translate("Rob", "Operations"))
        self.csvtopdf.setText(_translate("Rob", "CSV to PDF"))
        self.pdftocsv.setText(_translate("Rob", "PDF to CSV"))
        self.groupBox.setTitle(_translate("Rob", "CSV to PDF Options"))
        self.generateall.setText(_translate("Rob", "Generate All"))
        self.generateonly.setText(_translate("Rob", "Generate only:"))
        self.groupBox_3.setTitle(_translate("Rob", "File/Folder Select"))
        self.pdfselect.setText(_translate("Rob", "PDF Template/Folder"))
        self.csvselect.setText(_translate("Rob", "CSV"))
        self.outputfolder.setText(_translate("Rob", "Output Folder"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Rob = QtWidgets.QMainWindow()
    ui = Ui_Rob()
    ui.setupUi(Rob)
    Rob.show()
    sys.exit(app.exec_())




        #def buttonfunctions(self):

            #sender2 = self.sender()

            #if sender2.text() == "pdfselect":
                #print("pdf")

            #elif sender.text() == "csvselect":
                #print("csv")
