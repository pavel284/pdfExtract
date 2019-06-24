import PyPDF2
import re

acuerdoPath='/Users/paulavendano/desktop/pdf/data/acuerdoTexto.txt'

def saveFile(path,str):
	savePdf = open(path,'w')
	savePdf.write(str)
	savePdf.close()

# pdf file object
# you can find find the pdf file with complete code in below
source ='/Users/paulavendano/desktop/pdf/data/acuerdo.pdf'

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

saveFile(acuerdoPath,textPdf)

#regex to import all the frequencies
pattern="[A-Z][A-Z]\s[0-9]+,[0-9]+"
#strtest="SISTEMA #2: TX 427,578125 MHz - RX 422,578125 MHz SISTEMA #4: TX 428,340625 MHz - RX 423,340625 MHz"

#test if my regex will match pattern
if re.findall(pattern,textPdf):
	print ("match")
else: 
	print ("Not a match")

#print all the regex coincidences
print(re.findall(pattern,textPdf))



