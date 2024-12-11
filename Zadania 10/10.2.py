import tkinter as tk
import random

root = tk.Tk()
root.geometry('400x400')
root.title('Kamień, papier, nożyce')

computer = ['Kamień', 'Papier', 'Nożyce']

def ResetGame():
    button1['state'] = 'active'
    button2['state'] = 'active'
    button3['state'] = 'active'
    label1.config(text='Gracz')
    label2.config(text='')
    label3.config(text='Komputer')

def DisableButtons():
    button1['state'] = 'disable'
    button2['state'] = 'disable'
    button3['state'] = 'disable'

def Rock():
    computer_choice = computer[(random.randint(0, 2))]
    if computer_choice == 'Kamień':
        result = 'Remis!'
    elif computer_choice == 'Nożyce':
        result = 'Wygrana!'
    else:
        result = 'Przegrana!'
    label1.config(text='Kamień')
    label2.config(text=result)
    label3.config(text=computer_choice)
    DisableButtons()

def Paper():
    computer_choice = computer[(random.randint(0, 2))]
    if computer_choice == 'Papier':
        result = 'Remis!'
    elif computer_choice == 'Kamień':
        result = 'Wygrana!'
    else:
        result = 'Przegrana!'
    label1.config(text='Papier')
    label2.config(text=result)
    label3.config(text=computer_choice)
    DisableButtons()

def Scissors():
    computer_choice = computer[(random.randint(0, 2))]
    if computer_choice == 'Nożyce':
        result = 'Remis!'
    elif computer_choice == 'Papier':
        result = 'Wygrana!'
    else:
        result = 'Przegrana!'
    label1.config(text='Nożyce')
    label2.config(text=result)
    label3.config(text=computer_choice)
    DisableButtons()

labelframe = tk.LabelFrame(root, text='Kamień, papier, nożyce!',
                           font='Consolas 20 bold', bg='white',
                           labelanchor='n', bd=10, width=370, height=370)
labelframe.pack(expand=True)

label1 = tk.Label(labelframe, text='Gracz', font='Consolas 15 bold')
label2 = tk.Label(labelframe, text='', font='Consolas 20 bold', bg='white',
                  width=15, borderwidth=3, relief='solid')
label3 = tk.Label(labelframe, text='Komputer', font='Consolas 15 bold')
label1.place(relx=0.10, rely=0.1)
label2.place(relx=0.15, rely=0.35)
label3.place(relx=0.60, rely=0.1)

button1 = tk.Button(labelframe, text='Kamień', font='Consolas 10 bold', width=8,
                    command=Rock)
button2 = tk.Button(labelframe, text='Papier', font='Consolas 10 bold', width=8,
                    command=Paper)
button3 = tk.Button(labelframe, text='Nożyce', font='Consolas 10 bold', width=8,
                    command=Scissors)
button1.place(relx=0.10, rely=0.60)
button2.place(relx=0.40, rely=0.60)
button3.place(relx=0.70, rely=0.60)

tk.Button(root, text='Reset', font='Consolas 8 bold', fg='red', bg='black',
          command=ResetGame).place(relx=0.43, rely=0.8)

root.mainloop()
