# PDFTOAUDIO

PDFTOAUDIO is a program for turning your pdf files to audio files 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyPDF2 and pyttsx3.

```bash
pip install pyttsx3 PyPDF2
```

## Usage

```python
import PyPDF2
import pyttsx3

pdf = PdfFileReader(f) # reads a pdf
page = pdf.getPage(num)
text = page.extractText()
speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)