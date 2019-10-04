import PyPDF2
import re
import PySimpleGUI as sg

acuerdoPath='C:/Users/paul.avendano/Desktop/AcuerdosBA/acuerdoTexto.txt'

def saveFile(path,str):
    savePdf = open(path,'w')
    savePdf.write(str)
    savePdf.close()

sg.Popup('Favor seleccionar un archivo PDF')
source = sg.PopupGetFile('Favor seleccionar un archivo PDF',default_path='', default_extension='.xlsx', save_as=False, file_types=(('PDF', '.pdf'),), no_window=False, font=None, no_titlebar=False, grab_anywhere=False)

def PDF (source):
    # pdf file object
    pdf = open(source, 'rb')
    # pdf reader object
    pdfDoc = PyPDF2.PdfFileReader(pdf)
    # number of pages in pdf
    pagesPdf = pdfDoc.numPages
    #declare variables for while
    page = 0
    textPdf =""
    #read every page and extact text for every page
    while page < pagesPdf:
        # a page object
        pageObj = pdfDoc.getPage(page)
        #extract text from a page PDF
        text = pageObj.extractText()
        #concat the strings
        textPdf += text
        page +=1
    return textPdf    

def patterns (searching,doc):
    result = re.findall(searching,doc)
    return result

def unique (lista):
    element = lista[0]
    return element

def removeDuplicate (lista):
    finalList = []
    for item in lista:
        if item not in finalList:
            finalList.append(item)
    return finalList

def cleanFreq (freqList):
#    save all the frequencies in a string
    frequencies = ""    
    for freq in freqList:
        frequencies += freq + " "

#erase the words TX TX CD
    frequencies = frequencies.replace("TX","")
    frequencies = frequencies.replace ("CD","")
    freqClean = frequencies.replace("RX","")
#    print(freqClean)

#separete the string by the spaces    
    freqClean = freqClean.split(' ')
#    print(freqClean)

#remove duplicates from list
    listFreq = removeDuplicate(freqClean)

#remove "" from list
    listFreq.remove("")
#    print(listFreq)

#save every frequencie in on string 
    freqFinalList = ""
    for freq in listFreq:
        freqFinalList += freq + "\n"
#    print (freqFinalList)
    
    return freqFinalList

#regex to import all coincidences
patternFreq="[A-Z][A-Z]\s[0-9]+,[0-9]+"
patternCD = "CD\s[0-9]+"
patternTx = "TX\s[0-9]+"
patternRx = "RX\s[0-9]+"
patternName = "[a-zA-Z]ermisionari[a-z]+\s[a-zA-Zá-úÁ-ÚñÑ\s.]+\sC"
patternId = "N°\s[0-9]-[0-9]+-[0-9]+"
patternNum = "[0-9]+\-[0-9]+\-TEL\-MICITT"
patternLat = "[8|9]\,[0-9][0-9][0-9][0-9]+"
patternLong = "[8][0-9]\,[0-9]+"

#extract the text from pdf
textPdf = PDF(source)
print()

freqList =patterns(patternFreq, textPdf)
names =  patterns(patternName, textPdf)
ced = patterns(patternId,textPdf)
acuerdo = patterns (patternNum,textPdf)
lat = patterns(patternLat,textPdf)
long =  patterns(patternLong,textPdf)

#unique clean name
uniqueName = unique(names)
nameObj1 = uniqueName.replace("Permisionario\n","")
nombre = nameObj1.replace("\nC","")

print (freqList)
print (nombre)
print (ced)
print (acuerdo)
print (lat)
print (long) 

#unique values from coincidences
cedJurTest = unique(ced).replace("N° ","")
cedJur = cedJurTest.replace("-","")
numAcuer = unique(acuerdo)

print (cedJur)
print (numAcuer)

#adding - to longitutde
longitud = []
for lon in long:
    longitud.append ("-" + lon)

print (lat)
print (longitud)

freqFinalList = cleanFreq (freqList)
print(freqFinalList)
