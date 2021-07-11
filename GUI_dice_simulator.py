import random 
import tkinter

def generator():
    val = random.randint(1,6)
    value_label['text'] = f'Dice roll value is: {val}'


window = tkinter.Tk()
window.title('Dice Simulator GUI')


window.columnconfigure(0, weight=1, minsize = 300)
window.rowconfigure([0,1,2], weight=1, minsize=60)

frame = tkinter.Frame(master=window, relief=tkinter.RAISED, borderwidth=3, bg='#003040', padx=30, pady=20)
frame.grid(pady=20)
name_label = tkinter.Label(master=frame, text='Dice Simulator', width=10, fg='#ff5040', padx=20, pady=10)
name_label.grid(row=0, column=0, pady=5)

value_label = tkinter.Label(master=frame, fg='#003040', relief=tkinter.RIDGE, borderwidth=2, padx=10, pady=10)
value_label.grid(row=1,column=0, pady=5)

btn = tkinter.Button(master=frame, text='Roll', padx=20, pady=10, command=generator)
btn.grid(row=2, column=0)

window.mainloop()