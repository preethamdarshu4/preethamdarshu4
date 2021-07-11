import tkinter as tk

def temp_converter():
    ent = float(frnht_entry.get())
    cel_val = (5/9) * (ent - 32)
    val_label['text'] = f'{round(cel_val, 2)} \N{DEGREE CELSIUS}'

window = tk.Tk()
window.title('Temparature Converter')


frnht_entry = tk.Entry(master=window, width=7)
frnht_entry.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

frnht_label = tk.Label(master=window, text='\N{DEGREE FAHRENHEIT}')
frnht_label.grid(row=0, column=1, sticky='w', pady=10)

btn = tk.Button(master=window, text='\N{RIGHTWARDS BLACK ARROW}', command=temp_converter)
btn.grid(row=0, column=2, sticky='nsew', padx=10, pady=10)

val_label = tk.Label(master=window, width=10)
val_label.grid(row=0, column=3, sticky='nsew', padx=10, pady=10)

window.mainloop()