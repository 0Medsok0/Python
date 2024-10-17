from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog
import docx
import PyPDF2

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def extract_text_from_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    num_pages = pdf_reader.numPages
    text = ""
    for page_num in range(num_pages):
        page_obj = pdf_reader.getPage(page_num)
        text += page_obj.extractText()
    pdf_file_obj.close()
    return text

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

if file_path.endswith('.txt'):
    with open(file_path, 'r') as f:
        text = f.read()
elif file_path.endswith('.docx'):
    text = extract_text_from_docx(file_path)
elif file_path.endswith('.pdf'):
    text = extract_text_from_pdf(file_path)
else:
    print("Unsupported file type")
    exit()

audio = 'audio.mp3'
lang = 'ru'
sp = gTTS(text=text, lang=lang, slow=False)
sp.save(audio)
