#File is updated.
# C:\Users\Sneha\PycharmProjects\Pdftotxtfilecoverterproject


# Command to install PyPDF2 : pip install PyPDF2
# After installing PyPDF2 import that package

import PyPDF2

read_pdf = open('Syllabus 2year.pdf', 'rb')  #We opened the Syllabus 2year.pdf in binary mode. and saved the file object as read_pdf.
reader_pdf = PyPDF2.PdfFileReader(read_pdf)  #Here, we create an object of PdfFileReader class of PyPDF2 module and  pass the pdf file object & get a pdf reader object.
num_pages = reader_pdf.numPages              #numPages property gives the number of pages in the pdf file. For example, in our case, it is 20 (see first line of output).
convert_pages = reader_pdf.getPage(num_pages - 1) #Now, we create an object of PageObject class of PyPDF2 module. pdf reader object has function getPage() which takes page number (starting form index 0) as argument and returns the page object.
extract_text = convert_pages.extractText()     #Page object has function extractText() to extract text from the pdf page.

location = open(r"C:\Users\Sneha\PycharmProjects\Pdftotxtfilecoverterproject\Syllabus 2year.txt", "a")
location.writelines(extract_text)
location.close()

