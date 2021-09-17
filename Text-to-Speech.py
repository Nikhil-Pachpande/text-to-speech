# Importing the required libraries
from tkinter import *
from gtts import gTTS
from playsound import playsound

# Initializing the Tkinter GUI Window
root = Tk()
root.geometry('350x300')
root.resizable(0, 0)
root.config(bg='white')
root.title('Text-to-Speech-Conversion')

# Label_1/Heading
Label(root, text='TEXT_TO_SPEECH', font='arial 20 bold', bg='white smoke').pack()

# Label_2
Label(root, text='Enter some Text here:', font='arial 15 bold', bg='white smoke').place(x=20, y=60)

message = StringVar()

# Text-Field for user
entry_field = Entry(root, textvariable=message, width='50')
entry_field.place(x=20, y=100)


#This function will convert the text message from user into speech; using the gTTS package
def convert():
    text = entry_field.get()
    speech = gTTS(text=text)
    speech.save('result.mp3')
    playsound('result.mp3')


# Exit Function
def exit():
    root.destroy()


# Reset Function
def reset():
    message.set("")


# Buttons
Button(root, text="PLAY", font='arial 15 bold', command=convert, width=4).place(x=25, y=140)
Button(root, text='EXIT', font='arial 15 bold', command=exit, bg='OrangeRed1').place(x=100, y=140)
Button(root, text='RESET', font='arial 15 bold', command=reset).place(x=175, y=140)

# infinite loop to run program
root.mainloop()