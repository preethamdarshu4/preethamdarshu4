import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def key_press(event):
    if int(event.keycode) == 79: file_open()
    if int(event.keycode) == 83: file_save()


def file_open():
    filepath = askopenfilename(filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if not filepath:
        return
    textEntry.delete('1.0', tk.END)
    with open(filepath, 'r') as file_handle:
        text = file_handle.read()
        textEntry.insert(tk.END, text)
    window.title(f'Tkinter Simple Text Editor - {filepath}')


def file_save():
    filepath = asksaveasfilename(defaultextension='txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if not filepath:
        return
    with open(filepath, 'w') as file_handle:
        text = textEntry.get(1.0, tk.END)
        file_handle.write(text)
    window.title(f'Tkinter Simple Text Editor - {filepath}')


window = tk.Tk()
window.title('Tkinter Simple Text Editor')
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

optionsFrame = tk.Frame(window)
openBtn = tk.Button(optionsFrame, text='Open', command=file_open)
saveBTn = tk.Button(optionsFrame, text='Save as', command=file_save)
textEntry = tk.Text(window)

openBtn.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
saveBTn.grid(row=1, column=0, sticky='ew', padx=5)
optionsFrame.grid(row=0, column=0, sticky='ns')
textEntry.grid(row=0, column=1, sticky='nsew')
window.bind('<Control-s>', key_press)
window.bind('<Control-o>', key_press)
window.mainloop()