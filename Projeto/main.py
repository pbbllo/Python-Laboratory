from tkinter import *
from amazon_polly import execute

def main():

    def generateAudio():
        execute(txt.get('1.0', END))

    window = Tk()

    window.title('Text to Speech Conversor')
    window.geometry('400x500')
        
    label = Label(window, text="Insert your text")
    txt = Text(window, borderwidth=2)

    button = Button(window, text='Generate Audio', command=generateAudio)

    label.place(x=150, y=50)
    txt.place(x=100, y=150, width=200, height=200)
    button.place(x=150, y=450)
    
    window.mainloop()

if __name__ == "__main__":
    main()
