from tkinter import*
from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox
from tkinter import StringVar
from tkinter import IntVar
from tkinter import BooleanVar
from tkinter import Toplevel
from tkinter import Listbox
from tkinter import Frame

#***************srtingvar***********
def strvar():
    return StringVar()


#*****************intvar*********
def intvar():
    return IntVar()


#**************boolvar**********
def boolvar():
    return BooleanVar()

#************Radiobutton******************
def radio(form,text='Radio',value=0,variable=None):
    rdo=ttk.Radiobutton(form,text=text,value=value)
    if Variable!=None:
        rdo.config(variable=variable)
    return rdo
    
#**********Checkbutton************************

def checkbox(form,text='checkbutton',variable=None):
    cbx=ttk.Checkbutton(form,text=text)
    if variable!=None:
        cbx.config(variable=variable)
    return cbx

#*********combobox*************************
def combobox(form,values=None,readonly=False):
    cbx=ttk.Combobox(form)
    if values!=None:
        cbx.config(values=values)
    if readonly:
        cbx.config(state='readonly')
    return cbx
        
#**************Listbox*************
def listbox(form,values=None): 
    lbx=Listbox(form)
    if values !=None:
        i=0
        for x in values:
            lbx.insert(i, x)
            i+=1
    return lbx
   

#********************Make Form In center*************************
def tkcenter(form):
    form.update()
    sw=form.winfo_screenwidth()
    sh=form.winfo_screenheight()
    fw=form.winfo_width()
    fh=form.winfo_height()
    x=(sw-fw)/2
    y=(sh-fh)/2
    form.geometry('%dx%d+%d+%d'%(fw,fh,x,y))
    
    
#**********Make Form***************
def form(geometry='350x200',title='',is_center=True):
    f=Tk()
    f.geometry(geometry)
    f.title(title)
    if is_center:tkcenter(f)
    return f
    
#**************Toplevel************
def toplevel(geometry='350x200',title='',is_center=True):
    f=Toplevel()
    f.geometry(geometry)
    f.title(title)
    if is_center:tkcenter(f)
    return f
 
    
#**********Make Frame********************
 
def frame(form,bg=None):
    if bg!=None:
         return Frame(form,bg=bg)  
    else:
        return Frame(form)
 #**************Make Button******************

def button(form,text='Button',command=None):
    btn=ttk.Button(form,text=text)
    if command !=None:
        btn.config(command=command)
    return btn
    
#**********Make Label********************

def label(form,text='label'):
    return ttk.Label(form,text=text)
    
    
#******Textbox or Entry*************

def textbox(form,variable=None,is_number_only=False):
    def number_only(text):
        if str.isdigit(text):
            return True
        elif text is '':
            return True
        else:
            return False
    ret_fun=form.register(number_only)  
    txt=ttk.Entry(form)
    if is_number_only:
        txt.config(validate='key',validatecommand=(ret_fun,'%P'))
    if variable !=None:
        txt.config(textvariable=variable)
    return txt
    
   
#***************background color for all*************   
  
def bgall(form,bg):
    form.update()
    ctrls=form.winfo_children()
    form.config(background =bg)
    my=ttk.Style()
   # my.configure('TLabel', background =bg)
   # my.configure('TButton', background =bg)
    #my.configure('TEntry', background =bg)
    my.configure('TRadiobutton', background =bg)
    my.configure('TCheckbutton', background =bg)
    my.configure('TListbox', background =bg)
    for c in ctrls:
        if c.winfo_class()=='Frame':bgall(c,bg)
        try:
            c['background']=bg
        except:
            pass
        
       
            
            
#*************font size for all**********************
def fontall(form,font):
    form.update()
    ctrls=form.winfo_children()
    my=ttk.Style()
    #my.configure('TLabel', font=font)
    my.configure('TButton', font=font)
    my.configure('TRadiobutton', font=font)
    my.configure('TCheckbutton', font=font)
    my.configure('TListbox', font=font)
    for c in ctrls:
        if c.winfo_class()=='Frame':fontall(c,font)
        try:
            c['font']=font
        except:
            pass
            
# def fontall(form,font):
#     form.update()
#     ctrls=form.winfo_children()
#     for c in ctrls:
#         ci=c.winfo_class()
#         if (ci=='Label' or ci=='Button'or ci=='Entry' or ci=='TEntry'
#             or ci=='Radiobutton'or ci=='Checkbutton'):  #********TEntry 
#             c['font']=font
#         if( ci=='TLabel' or ci=='TButton'
#            or ci=='TRadiobutton'or ci=='TCheckbutton' ):   #****TEntry coudn't work here
#             my=ttk.Style()
#             my.configure('TLabel', font=font)
#             my.configure('TButton', font=font)
#             my.configure('TRadiobutton', font=font)
#             my.configure('TCheckbutton', font=font)
            
#*****************foreground color for all**************            
def fgall(form,fg):
    form.update()
    ctrls=form.winfo_children()
    my=ttk.Style()
   # my.configure('TLabel', foreground=fg)
    my.configure('TButton', foreground=fg)
    #my.configure('TEntry', foreground=fg)
    my.configure('TRadiobutton', foreground=fg)
    my.configure('TCheckbutton', foreground=fg)
    my.configure('TListbox', foreground=fg)
    for c in ctrls:
        if c.winfo_class()=='Frame':fgall(c,fg)
        try:
            c['foreground']=fg
        except:
            pass
    
            
       
           
            
            
#****************Messagebox******************
def msgbox(text):
    messagebox.showinfo('',text)
    
#**************ask yes no message************
def msgask(text):
   return messagebox.askyesno('',text)

#******************inbox************
def inbox(text,is_number_only=False):
    f=Toplevel()
    f.title(text)
    f.geometry('400x150')
    f.resizable(False,False)
    tkcenter(f)
    ttk.Label(f,text=text,font='None 15').pack(pady=10)
    sv=StringVar()
    def number_only(text):
        if str.isdigit(text):
            return True
        elif text is '':
            return True
        else:
            return False
    ret_fun=f.register(number_only)
    txt=ttk.Entry(f,text=text,font='None 15',width=25,textvariable=sv)
    if is_number_only:
        txt.config(validate='key',validatecommand=(ret_fun,'%P'))
    txt.pack(pady=10)
    
    txt.bind('<Return>',lambda my:f.destroy())
  
  #علشان ال button لما اجي اضغط عليه مش يصغر حجمه     
  #هحط قبل اسم TButtom اي اسم متغير علشان احدد الا style
   
    ttk.Style().configure('xxx.TButton', font='None 15')
    #put style ='xxx.TButton' in the button
    ttk.Button(f,text='OK',command=lambda:f.destroy(),style='xxx.TButton').pack(pady=10)
    txt.focus()
    f.grab_set()
    f.wait_window()
    return sv.get()

#**************Entry reseive Only Number**********
# def number_only(text):
#     if str.isdigit(text):
#         return True
#     elif text is '':
#         return True
#     else:
#         return False
# ret_fun=frm.register(number_only)
# txt=ttk.Entry(frm,validate='key',validatecommand=(ret_fun,'%P')) #****%P is the capital latter
# txt.pack(pady=20)
# txt.focus()


        
    
    


