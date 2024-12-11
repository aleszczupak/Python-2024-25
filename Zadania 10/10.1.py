import tkinter as tk
import random 
   
root = tk.Tk()
root.configure(bg='black')
root.geometry('350x350')
root.title('Rzut kostką!')
root.resizable(0, 0) 
  
def RollTheDice(): 
    dots = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    dice.configure(text=f'{random.choice(dots)}') 
    dice.pack() 

button = tk.Button(root, text='Rzut', width=5, height=2,
                   font='Consolas 20 bold', bg='white', bd=2,
                   command=RollTheDice) 
button.pack(padx=10, pady=15)    
dice = tk.Label(root, font='Consolas 250 bold', bg='black', fg='white') 
  
root.mainloop()
