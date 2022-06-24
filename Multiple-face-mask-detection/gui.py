import tkinter as tk

def startC():
    top = tk.Toplevel(window)
    top.geometry('600x300')
    top.title('Multiple Face Mask Dtector Using OpenCV')
    lbl = tk.Label(top, text = 'Success')
    lbl.pack()


window = tk.Tk()
window.geometry('800x400')
window.title('Multiple Face Mask Dtector Using OpenCV')
window.config(bg='#111b21')
frame = tk.Frame(window, relief= tk.RAISED, borderwidth=2, bg='#2a3942')
lbl = tk.Label(frame, text='Click on the button to run code: ', foreground='white', background='#2a3942', width=40, height=2)
button = tk.Button(frame, text='Start code', width=15, height=1, foreground='white', background='#2a3942', command= lambda: startC())
lbl.grid(row=1, ipady=5)
button.grid(row=2, ipady=5, pady=10)
frame.place(relx=.5, rely=.5, anchor='c')

window.mainloop()