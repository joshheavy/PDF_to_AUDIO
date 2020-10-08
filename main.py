from PyPDF2 import PdfFileReader
import pyttsx3
from tkinter.filedialog import askopenfilename


"""
Involves two functions the: 
    get_file(path) which reads a file from its path and returns the audio speaker
    reader_book function that basically opens your file explorer to let you choose
    the file that you want from your computer

The module also contains three packages that help us complete the tasks
two of them are third party packages(PyPDF2, pyttsx3) and one is built-in package
for python.

You can install pipenv through pip install pipenv and later install the Pipfile
to work with this module
"""
def get_file(path):
    with open(path, 'rb') as f: 
        pdf = PdfFileReader(f) # reads a pdf file
        info = pdf.getDocumentInfo() # gets the document info
        # number_of_pages = pdf.getNumPages()
        pages = pdf.numPages # calculate total number of pages

        print(pages)
        print(info)
 

        for num in range(0, pages):
            """
            The for loop basically iterates each page from page one to the end
            """
            page = pdf.getPage(num)
            text = page.extractText() # extracts each text in the page
            speaker = pyttsx3.init() # initialize the speaker
            speaker.say(text) # tell the speaker to say the words
            speaker.runAndWait() # runs and speaker starts to say the words

def reader_book():
    book = askopenfilename()
    pdf = PdfFileReader(book)
    pages = pdf.numPages

    for num in range(0, pages):
        page = pdf.getPage(num)
        text = page.extractText()
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()
 

if __name__ == '__main__':
    # path = 'Eric Windmill.pdf'
    # get_file(path) # call function with the path name
    reader_book()  # call the function with no argument