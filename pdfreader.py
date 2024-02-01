import pyttsx3 as tts
import PyPDF2 as ppdf

print('Starting soon...')
file_path = input("Insert your path: ")

with open(file_path, 'rb') as paper:
    pdfReader = ppdf.PdfReader(paper)
    voice = tts.init()
    
    for page_num in range(len(pdfReader.pages)):
        page = pdfReader.pages[page_num]
        text = page.extract_text()
        voice.say(text)

voice.runAndWait()
