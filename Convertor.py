from tkinter import *
import speech_recognition as sr
from translate import Translator

global counter 
counter = 2

# MAIN 

root=Tk()
root.title('Convertor')
root.minsize(400,800)
root.maxsize(400,800)


# WIDGET & CONFIG 

def widget():

    lb1=Label(root, text='Speak:')
    lb1.config(font=('Titr',22,'bold'), bg='lime', width=22)
    lb1.grid(row=0)

    btn_start=Button(root, text='Start Convert' , command=get_voice)
    btn_start.config(font=('Calibri',17,'bold'),bg='blue',fg='white', width=10)
    btn_start.grid(row=1, pady=44)



#GET VOICE & RECOGNITION


r = sr.Recognizer()

def get_voice():
    try:
        with sr.Microphone() as src:           # ABBREVATION
            audio = r.listen(src)
            text = r.recognize_google(audio)
            translator = Translator(to_lang='fa')
            text = translator.translate(text)
            show_text(text)
    except Exception as e:
        print('error:',e)
        

# FUCTION FOR SHOWING THE TRANSLATED TEXT

def show_text(text):
    global counter
    lbl_name= f"lbl_{counter}"
    lbl_name = Label(text = text)
    lbl_name.config(font=('Calibri',20))
    lbl_name.grid(row = counter)
    counter +=1



# CALL THE WIDGET FUNCTION 

widget()

root.mainloop()