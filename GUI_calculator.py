import tkinter as tk
import tkinter.font as font


expression = ''

def keyboard_event_handler(event):
    value = event.keysym
    calc_val = ['slash', 'asterisk', 'minus', 'plus', 'period']
    Val_dict = {'0':0, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9, 'slash':'/', 'asterisk':'*','minus':'-','plus':'+','period':'.'}
    
    if value == 'c':
        clear()
    elif value == 'BackSpace':
        backspace()
    elif value == 'Return':
        calc()
    elif value == str(Val_dict[value]) or value in str(calc_val):
        setExp(Val_dict[value])
    
    

def mouse_event_handler(event):
    text = event.widget.cget('text')

    if text == 'c':
        clear()
    elif text == '<-':
        backspace()
    elif text == '=':
        calc()
    else:
        setExp(text)

def setExp(text):
    global expression
    expression = expression + str(text)
    equation.set(expression)

def calc():
    global expression

    if not expression == '':
        try:
            result = str(eval(expression))
            equation.set((expression + ' = ' + result))
            expression = ''
        
        except:
            equation.set('Error')
            expression = ''
    else:
        equation.set('0')
        expression = ''

def backspace():
    global expression
    expression = expression[0:(len(expression)-1)]
    equation.set(expression)


def clear():
    global expression
    expression = ''
    equation.set('0')

if __name__ == '__main__':
    window = tk.Tk()
    window.title('Simple Calculator')
    window.configure(bg='#3b3b3b')
    window.columnconfigure(0, minsize=75, weight=1)
    window.rowconfigure(1, minsize=300, weight=1)

    equation = tk.StringVar()
    btn_font = font.Font(size=10)
    
    output_label = tk.Entry(window, fg='black', bg='#ece8e1', bd=2, font=('arial', 20), textvariable=equation, justify='right')
    output_label.grid(row=0, column=0, columnspan=4, sticky='ew', ipady=15)

    btns_frame = tk.Frame(window, bg='grey')
    btns_frame.grid(row=1,column=0, sticky='nsew')

    btns_lbl = [['c','','<-', '/'], [1,2,3,'*'], [4,5,6,'-'], [7,8,9,'+'], ['.',0,'=']]
    btns_names = {}

    for row_ind in range(len(btns_lbl)):

        btns_frame.rowconfigure([0,1,2,3,4], minsize=40,weight=1)
        btns_frame.columnconfigure([0,1,2,3], minsize=100,weight=1)

        for col_ind in range(len(btns_lbl[row_ind])):
            name = str(btns_lbl[row_ind][col_ind])
            special_names = ['c', '<-', '/', '*', '-', '+', '=']
            if not name in str(special_names) :
                btns_names['btn_'+name] = tk.Button(btns_frame, text=name, fg='black', bg='#fff', cursor='hand2', bd=0, font=btn_font)
            else:
                btns_names['btn_'+name] = tk.Button(btns_frame, text=name, fg='black', bg='#e9e9e9', cursor='hand2', bd=0, font=btn_font)
            
            
            if name == 'c' or name == '=':
                btns_names['btn_'+name].grid(row=row_ind, column=col_ind, columnspan=2, padx=1, pady=1, sticky='nsew')
            if row_ind == 0 and col_ind == 1:
                continue
            btns_names['btn_'+name].grid(row=row_ind, column=col_ind, padx=1, pady=1, sticky='nsew')

            btns_names['btn_'+name].bind('<Button-1>', mouse_event_handler)

    window.bind('<Key-c>', keyboard_event_handler)
    window.bind('<BackSpace>', keyboard_event_handler)
    window.bind('/', keyboard_event_handler)
    window.bind('*', keyboard_event_handler)
    window.bind('+', keyboard_event_handler)
    window.bind('-', keyboard_event_handler)
    window.bind('.', keyboard_event_handler)
    window.bind('<Return>', keyboard_event_handler)

    for key in range(10):
        window.bind(str(key), keyboard_event_handler)
    window.mainloop()
