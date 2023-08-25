from tkinter import *
import speech_recognition as sr
import translate as tr

# for showing correct the translated texts
global counter 
counter = 2

# main app
root = Tk()
root.title('Convertor')
root.minsize(400,800)
root.maxsize(400,800)

# widget & config
def widget():
    lbl1 = Label(root, text='Speak:')
    lbl1.config(font=('Titr',22,'bold') , bg='yellow' , width=22)
    lbl1.grid(row=0)

    btn_start = Button(root , text='Start Convert' , command=get_voice)
    btn_start.config(font=('calibri',17 , 'bold') , bg='navy blue' , fg='white')
    btn_start.grid(row=1 , pady=44)


# create an instance from modules
r = sr.Recognizer()
t = tr.Translator(to_lang='fa')

# function for getting voice & recognition
def get_voice():
    try:
        with sr.Microphone() as src:
            audio = r.listen(src)
            text = r.recognize_google(audio)
            translated_text = t.translate(text)
            show_text(translated_text)
    except Exception as e:
        print('error :' , e)

# function for showing the translated text
def show_text(translated_text):
    global counter
    lbl_name = f'lbl_{counter}'
    lbl_name = Label(text= translated_text)
    lbl_name.config(font= ('calibri',20))
    lbl_name.grid(row= counter)
    counter+=1 


# call the widget function for showing the app
widget()


root.mainloop()
