from tkinter import *
from tkinter import filedialog,messagebox
import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'C:\Users\Jennifer\Desktop\miniproject\tesseract.exe'
from PIL import Image,ImageOps,ImageFilter
from ttkbootstrap import Style
from tkinter import ttk
import threading
from gtts import gTTS
from playsound import playsound
import os
from tkinter import scrolledtext
import PyPDF2
import speech_recognition as sr





#AUDIO TO TEXT
def openAudiotoText(): 
    
#Gets file path and displays it in text box
    def audio_file_path():

            global filepath
            filepath = StringVar()
            if(filepath == ""):
                filepath = filedialog.askopenfilename( initialdir = os.getcwd() ,
                     title = "select a file", filetypes = [("All files", "*")])
                T1.insert(END, filepath)
                
            else:
                filepath = filedialog.askopenfilename( initialdir=filepath,
                     title = "select a file", filetypes = [("All files", "*")])
                T1.insert(END, filepath)
                
    
    def audiotransform():
        sound=filepath
        r = sr.Recognizer()
        with sr.AudioFile(sound) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)
            try:
                x = r.recognize_google(audio)
                print("Converted audio is :\n"+x)
            except sr.UnknownValueError:
                print("Sorry")
            except sr.RequestError:
                print("Could not request results ")

        #str1='C:/Users/Helios 300/Desktop/python/Projects/audio to image/'
        #st1=input("Enter the name of the file to store into:")
        str1=T2.get()
        str1=str1+'.txt'

        with open(str1, 'w') as f:
            f.write(x)
        newWindow.destroy()
    
        
        
        
    
    newWindow= Toplevel(root)
    newWindow.title("Audio to Text Conversion")
    newWindow.resizable(False, False)
    
    lb1 =ttk.Label(newWindow, text="Audio file: ")
    lb2 =ttk.Label(newWindow, text="Save As Text file: ")
    T1 = ttk.Entry(newWindow, width=30)
    T2 = ttk.Entry(newWindow, width=30)
    Browsebutton1 = ttk.Button(newWindow,width = 15,text= "Browse",command = audio_file_path)
    
    
    Convertbutton = ttk.Button(newWindow, width =15, text="Convert", command = audiotransform)
    Cancelbutton =ttk.Button(newWindow, width =15, text= "Cancel", command = newWindow.destroy)
    
    lb1.grid(row = 0, column = 0,padx=3,pady=20)
    T1.grid(row = 0, column = 1,padx=1,pady=5)
    Browsebutton1.grid(row=0, column=2, padx=3,pady=5)
    lb2.grid(row = 1, column = 0,padx=3,pady=5)
    T2.grid(row = 1, column = 1,padx=1,pady=5)
    
    Convertbutton.grid(row=2, column=1,pady=10)






# PDF MERGER
def openPDFMerger():
    def Second_file_path():

            global filepath2
            filepath2 = StringVar()
            if(filepath2 == ""):
                filepath2 = filedialog.askopenfilename( initialdir = os.getcwd() ,
                     title = "select a file", filetypes = [("All files", "*")])
                T2.insert(END, filepath2)
                
            else:
                filepath2 = filedialog.askopenfilename( initialdir=filepath2,
                     title = "select a file", filetypes = [("All files", "*")])
                T2.insert(END, filepath2)
    
    

#Gets file path and displays it in text box
    def First_file_path():

            global filepath
            filepath = StringVar()
            if(filepath == ""):
                filepath = filedialog.askopenfilename( initialdir = os.getcwd() ,
                     title = "select a file", filetypes = [("All files", "*")])
                T1.insert(END, filepath)
                
            else:
                filepath = filedialog.askopenfilename( initialdir=filepath,
                     title = "select a file", filetypes = [("All files", "*")])
                T1.insert(END, filepath)
                
    
    def PDFmerge():
        writer =PyPDF2.PdfFileWriter()

        f1=open(filepath,'rb')
        reader_1= PyPDF2.PdfFileReader(f1)
        for i in range(reader_1.numPages):
            page=reader_1.getPage(i)
            writer.addPage(page)

        f2=open(filepath2,'rb')
        reader_2= PyPDF2.PdfFileReader(f2)
        for i in range(reader_2.numPages):
            page=reader_2.getPage(i)
            writer.addPage(page)
        final = T3.get()
        final=final.strip()

        output = open(final,'wb')
        writer.write(output)
        output.close()
        f1.close()
        f2.close()
        newWindow.destroy()
        
    
    
    newWindow= Toplevel(root)
    newWindow.title("PDF Merger")
    newWindow.resizable(False, False)
    
    lb1 =ttk.Label(newWindow, text="PDF 1: ")
    lb2 =ttk.Label(newWindow, text="PDF 2: ")
    lb3 =ttk.Label(newWindow, text="Save Merged PDF as: ")
    T1 = ttk.Entry(newWindow, width=30)
    T2 = ttk.Entry(newWindow, width=30)
    T3 = ttk.Entry(newWindow, width=30)
    Browsebutton1 = ttk.Button(newWindow,width = 15,text= "Browse",command = First_file_path)
    Browsebutton2 = ttk.Button(newWindow,width = 15,text= "Browse",command =Second_file_path)
    #Browsebutton3 = Button(newWindow,width = 15,text= "Select",command =Third_file_path)
    
    Mergebutton = ttk.Button(newWindow, width =15, text="Merge", command = PDFmerge)
    
    lb1.grid(row = 0, column = 0,padx=3,pady=10)
    T1.grid(row = 0, column = 1,padx=1,pady=5)
    Browsebutton1.grid(row=0, column=2, padx=3,pady=5)
    lb2.grid(row = 1, column = 0,padx=3,pady=5)
    T2.grid(row = 1, column = 1,padx=1,pady=5)
    lb3.grid(row = 2, column = 0,padx=1,pady=5)
    T3.grid(row = 2, column = 1,padx=3,pady=10)
    Browsebutton2.grid(row=1, column=2, padx=3,pady=5)
    #Browsebutton3.grid(row=2, column=2, padx=3,pady=5)
    
    Mergebutton.grid(row=3, column=1,pady=10)






# TEXT TO SPEECH
def openTexttoSpeech():
    Voice = Toplevel(root)
    Voice.geometry("650x400")
    Voice.configure(bg='ghost white')
    Voice.title("Text to Speech Conversion")

    Label(Voice, text = "Text To Speech Converter", font = "arial 20 bold").place(x=10,y=10)
    Label(text ="", font = 'arial 15 bold', bg ='white smoke' , width = '20')

    Msg = StringVar()
    Label(Voice,text ="Enter Text: ", font = 'arial 15 bold').place(x=75,y=75)
    text_area = scrolledtext.ScrolledText(Voice,bg='white',width=40, height=8,font=("Times New Roman", 15))
    text_area.place(x=200,y=75)
    text_area.focus()
    #entry_field = Entry(Voice, textvariable = Msg ,width ='50')
    #entry_field.grid(row=2, column=0,padx=50,pady=20)

    def Text_to_speech():
        Message = text_area.get(1.0, END)
        speech = gTTS(text = Message)
        speech.save('output.mp3')
        playsound('output.mp3')
        os.remove('output.mp3')

    def Exit():
        Voice.destroy()

    def Reset():
        text_area.delete(0.0,END)
        
        
    Button(Voice, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=75,y=300)
    Button(Voice, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=150 , y = 300)

    Button(Voice, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=225 , y = 300)


  







# IMAGE TO TEXT
def openImagetoText():
    def text_file_path():

            global filepath2
            filepath2 = StringVar()
            if(filepath2 == ""):
                filepath2 = filedialog.askopenfilename( initialdir = os.getcwd() ,
                     title = "select a file", filetypes = [("txt files", "*.txt")])
                T2.insert(END, filepath2)
                
            else:
                filepath2 = filedialog.askopenfilename( initialdir=filepath2,
                     title = "select a file", filetypes = [("txt files", "*.txt")])
                T2.insert(END, filepath2)
    
    

#Gets file path and displays it in text box
    def image_file_path():

            global filepath
            filepath = StringVar()
            if(filepath == ""):
                filepath = filedialog.askopenfilename( initialdir = os.getcwd() ,
                     title = "select a file", filetypes = [("jpg files", "*.jpg")])
                T1.insert(END, filepath)
                
            else:
                filepath = filedialog.askopenfilename( initialdir=filepath,
                     title = "select a file", filetypes = [("jpg files", "*.jpg")])
                T1.insert(END, filepath)
                

#Transforms image 
    def imagetransform():
        z=filepath
        image=Image.open(z)

        img=ImageOps.grayscale(image)
        i1=img.filter(ImageFilter.MedianFilter(size = 3))

        text=tess.image_to_string(i1)
        print(text)

        with open(filepath2, 'w') as f:
            f.write(text)
        newWindow.destroy()       
        
        
    
    newWindow= Toplevel(root)
    newWindow.title("Image to Text Conversion")
    newWindow.resizable(False, False)
    
    lb1 =ttk.Label(newWindow, text="Image file: ")
    lb2 =ttk.Label(newWindow, text="Save As Text file: ")
    T1 = ttk.Entry(newWindow, width=30)
    T2 = ttk.Entry(newWindow, width=30)
    Browsebutton1 = ttk.Button(newWindow,width = 15,text= "Browse",command = image_file_path)
    Browsebutton2 = ttk.Button(newWindow,width = 15,text= "Select",command =text_file_path)
    
    Convertbutton = ttk.Button(newWindow, width =15, text="Convert", command = imagetransform)
    Cancelbutton =ttk.Button(newWindow, width =15, text= "Cancel", command = newWindow.destroy)
    
    lb1.grid(row = 0, column = 0,padx=3,pady=20)
    T1.grid(row = 0, column = 1,padx=1,pady=5)
    Browsebutton1.grid(row=0, column=2, padx=3,pady=5)
    lb2.grid(row = 1, column = 0,padx=3,pady=5)
    T2.grid(row = 1, column = 1,padx=1,pady=5)
    Browsebutton2.grid(row=1, column=2, padx=3,pady=5)
    
    Convertbutton.grid(row=2, column=1,pady=10)
    
    

    

#main window gui
style = Style()
style.configure('Outline.TButton', font=('Helvetica', 14))

#style.configure('TLabel', font=('Helvetica', 14))

root = style.master

root.title("Multimedia Converter")
root.resizable(False, False)

#to center the window
window_height = 470
window_width = 670
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


ttk.Label(root, text='  Multimedia Converter', style ='TLabel',font=("Helvetica", 30)).grid(row=0, column=0,padx=70,pady=20)
ttk.Label(root, text=' -  Select Operation - ', style ='TLabel',font=("Helvetica", 15)).grid(row=1, column=0,padx=10,pady=10)

ttk.Button(root, text="Image to Text", style='Outline.TButton',width=50,command = openImagetoText).grid(row=2, column=0,padx=50,pady=20) 
ttk.Button(root, text="Audio to Text", style='Outline.TButton',width=50,command=openAudiotoText).grid(row=3, column=0,padx=50,pady=20) 
ttk.Button(root, text="Text to Speech", style='Outline.TButton',width=50, command =openTexttoSpeech).grid(row=4, column=0,padx=50,pady=20) 
ttk.Button(root, text="PDF merger", style='Outline.TButton',width=50,command =openPDFMerger).grid(row=5, column=0,padx=50,pady=20) 

#.Button(root, text="Submit", style='success.Outline.TButton').pack(side='left', padx=5, pady=10)
root.mainloop()