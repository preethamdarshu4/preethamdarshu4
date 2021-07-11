from io import StringIO
import smtplib 
from email.message import EmailMessage
import ssl
import tkinter as tk
import timer
import mysql.connector as myc
import re
import datetime

sender = receiver = port = server_name = subject = content =  cdate = ctime =  ''
valid = 0
ret = [[]]

def new(type):
    if type == 0:
        entry_names['entry_Password'].delete(0, tk.END)
    elif type == 1:
        entry_names['entry_Sender'].delete(0, tk.END)
        entry_names['entry_Receiver'].delete(0, tk.END)
        entry_names['entry_Password'].delete(0, tk.END)
        entry_names['entry_Subject'].delete(0, tk.END)
        body.delete('1.0', tk.END)


def open_popup(type):
    if type == 0:
        top = tk.Toplevel(window)
        top.geometry('750x250')
        top.title('Email delivery popup')
        tk.Label(top, text='Email successfully delivered :)', font=('helvetica 15'), fg='33652a')
    
    elif  type == 1:
        global ret 
        top = tk.Toplevel(window)
        top.geometry('950x250')
        top.title('Email history popup')
        var = tk.StringVar()
        val = ''
        headings_txt = 'sender\treceiver\tport_num\tserver_name\tsubject\tsent_date\tsent_time\n\n'
        headings = tk.Label(top, text=headings_txt, font= ('arial 18'))
        
        label = tk.Label(top, textvariable=var, fg='#03324f', font=('helvetica 12'))
        for lst in ret:
            for ele in lst:
                val += str(ele) + '\t'
            val += '\n'
            var.set(val)
            val = ''
        
        headings.grid(row=0, pady=5)
        label.grid(row=1)

        
def store():
    global sender, receiver, port, server_name, subject, content, cdate, ctime
    try:
        con = myc.connect(host='localhost', user='root', password='mxs4yaM@40vz', database='pydb')
        cur = con.cursor()
        sql = "INSERT INTO emailDB (sender, receiver, port_num, server_name, subject, content, sent_date, sent_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

        cur.execute(sql, (sender, receiver, port, server_name, subject, content, cdate, ctime))
        con.commit()

    except Exception as sqlE:
        op_lbl['text'] = 'Store-DB: '+ str(sqlE)
        op_lbl.config(fg='red')

def history() :
    global ret
    try:
        con = myc.connect(host='localhost', user='root', password='mxs4yaM@40vz', database='pydb')
        cur = con.cursor()
        sql = "SELECT sender, receiver, port_num, server_name, subject, sent_date, sent_time FROM emailDB ORDER BY sent_date DESC;"
        cur.execute(sql)
        res = cur.fetchone()
        for ind, entry in enumerate(res):
            entry_list = list(entry)
            for item in entry_list:
                ret[ind].append(item)
        open_popup(1)
    except Exception as histE:
        op_lbl['text'] = 'Hist-DB: '+str(histE)
        op_lbl.config(fg='red')



def mail():

    global sender, receiver, port, server_name, subject, content, cdate, ctime
    server_name = 'smtp.gmail.com'  
    port = 465
    sender = entry_names['entry_Sender'].get()
    receiver = entry_names['entry_Receiver'].get()
    pwd = entry_names['entry_Password'].get()
    subject = entry_names['entry_Subject'].get()
    content = str(body.get('1.0', tk.END))

    email = EmailMessage()
    if re.search('^[a-zA-Z0-9]+@.+', sender) and re.search('^[a-zA-Z0-9]+@.+', receiver) :
        email['from'] = sender
        email['to'] = receiver
        email['subject'] = subject
        if  not content is None:
            email.set_content(content)
        else :
            op_lbl['text'] = 'Body is empty.'
            op_lbl.config(fg='red')
            new(0)
    else:
        op_lbl['text'] = ''
        op_lbl.config(fg='red')
        new(0)
    
    try:
        tobj = timer.Timer()
        tobj.start()
        ctx = ssl.create_default_context()
        with smtplib.SMTP_SSL(server_name, port, context=ctx) as server:
            server.login(sender, pwd)
            server.send_message(email)
        elapsed_time = tobj.stop()
        valid = 1
    except Exception as e:
        op_lbl['text'] = 'Smtp' + str(e)
        op_lbl.config(fg='red')
        new(1)
        valid = 0
    else:
        open_popup(0)
        op_lbl['text'] = f'Email sent successfully to: {receiver}\nElapsed Time: {elapsed_time}\n\nSent using smtplib and Gmail'
        op_lbl.config(fg='#33652a')
        if valid:
            cdateTime = datetime.datetime.now()
            cdate = cdateTime.strftime('%Y-%m-%d')
            ctime = cdateTime.strftime('%H:%M:%S')
            store()
        new(1)


def event(e):
    if e.keysym == 'Return':
        mail()
    elif e.keysym == 'n':
        new(1)

window  = tk.Tk()
window.title('Email Sender GUI')

options_frame = tk.Frame(window, relief=tk.RAISED, borderwidth=2)
options_frame.grid(row=0, rowspan=4, column=0, sticky='ns')
new_mail_btn = tk.Button(options_frame, text='New mail', font= ('Arial', 10), command=new)
new_mail_btn.grid(row=0, column=0, padx=10, pady=5, ipadx=15, ipady=2, sticky='ew')
history_btn = tk.Button(options_frame, text='Mail history', font= ('Arial', 10), command=history)
history_btn.grid(row=1, column=0, padx=10, ipadx=15, ipady=2, sticky='ew')

lbl = tk.Label(master=window, width=30, height=2, text='Send Emails using Python', font= ('times new roman bold', 18), justify='center')
lbl.grid(row=0, column=1, columnspan=2, sticky='ew')
lbl2 = tk.Label(window, text='Compose your Email: ', font= ('times new roman', 15), justify='left')
lbl2.grid(row=1, column=1, sticky='w', padx=10, pady=10)
frame = tk.Frame(window) 
frame.grid(row=2,column=1, padx=10, sticky='nsew')
details = ['Receiver','Sender','Password', 'Subject']
Password = tk.StringVar()
lbl_names = {}
entry_names = {}
for rind, lbl in enumerate(details, 1):
    lbl_names['label_'+lbl] = tk.Label(frame, height=2, text=f'{lbl}: ', font=('arial', 11))
    if lbl == 'Password':
        entry_names['entry_'+lbl] = tk.Entry(frame, textvariable=Password, show='*')
        
    else:
        entry_names['entry_'+lbl] = tk.Entry(frame)
        
    lbl_names['label_'+lbl].grid(row=rind, column=0, padx=4, sticky='w')
    entry_names['entry_'+lbl].grid(row=rind, column=1, ipadx=3, ipady=2, sticky='w')

body_lbl = tk.Label(frame, text='Enter the body of email: ', font=('arial', 12))
body_lbl.grid(row=5, column=0, columnspan=2, sticky='w', pady=15)
body = tk.Text(frame, width=50, height=10, font=('verdana', 10))
body.grid(row=6, column=0, columnspan=2, padx=10)

send = tk.Button(frame, text='send', width=10, command=mail, font=('arial', 13))
send.grid(row=7 , column=0, columnspan=2, ipady=4, pady=20)
op_lbl = tk.Label(window, font=('lucida console', 12), justify='left', padx=4, pady=10)
op_lbl.grid(row=3, column=1, columnspan=2, padx=10, sticky='ew')

window.bind('<Shift-Return>', event)
window.bind('<Control-n>', event)
window.mainloop()

""" preethamdarshu4411@gmail.comdabcdaga4@gmail.com """
""" This mail is sent from Preetham\'s laptop to test the \"sendEmail.py\" program which is developed in VS Code.\nPort number: 465\nThis mail is encrypted using standard  SSL encryption. """