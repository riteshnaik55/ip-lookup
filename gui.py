from pathlib import Path
from tkinter import *
import tkinter.messagebox as MessageBox
import whois
import socket

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def display(dom_info,ip,dom_addr):
    crit=['domain_name','org','dnssec','country']
    field_type=['Domain Name','DNS Security','Organization','Country']
    res={}
    i=0
    for key, value in dom_info.items():
        if key in crit:
            res[field_type[i]]=dom_info[key]
            i+=1
    window.geometry("583x600")
    label1=Label(window,text=('--------------------Results--------------------'),fg='#FBFF43',bg='#525276',font=('bold',18)).place(x=90,y=380)
    label1=Label(window,text=(field_type[0]+' - '+res[field_type[0]][0]),fg='#FFFFFF',bg='#525276',font=('bold',15)).place(x=70,y=425)
    label2=Label(window,text=(field_type[1]+' - '+res[field_type[1]]),fg='#FFFFFF',bg='#525276',font=('bold',15)).place(x=70,y=450)
    label3=Label(window,text=(field_type[2]+' - '+res[field_type[2]]),fg='#FFFFFF',bg='#525276',font=('bold',15)).place(x=70,y=475)
    label4=Label(window,text=(field_type[3]+' - '+res[field_type[3]]),fg='#FFFFFF',bg='#525276',font=('bold',15)).place(x=70,y=500)
    label5=Label(window,text=('IP Address'+' - '+ip),fg='#FFFFFF',bg='#525276',font=('bold',15)).place(x=70,y=525)
    label6=Label(window,text=('Domain Address'+' - '+dom_addr),fg='#FFFFFF',bg='#525276',font=('bold',15)).place(x=70,y=550)

def generate():
    try:
        url=entry_1.get()
        dom_info = whois.whois(url)
        ip=socket.gethostbyname(url)
        dom_addr=socket.gethostbyaddr(url)[0]
        display(dom_info, ip, dom_addr)
    except:
        MessageBox.showerror('Error','Invalid URL or IP Address') 

window = Tk()
window.geometry("583x400")
window.title("IP Lookup")
window.configure(bg = "#525276")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 400,
    width = 583,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    291.0,
    200.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=generate,
    relief="flat"
)
button_1.place(
    x=206.66665649414062,
    y=301.6666564941406,
    width=166.66665649414062,
    height=50.0
)

canvas.create_text(
    100,
    95.5,
    anchor="nw",
    text="IP LOOKUP",
    fill="#FFC700",
    font=("Arial",55,"bold")
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    297.14747619628906,
    240,
    image=entry_image_1
)

entry_1 = Entry(
    bd=0,
    bg="#FFF",
    fg="#000000",
    highlightthickness=0,
    font=("Arial",17,"bold")
)
entry_1.place(
    x=110,
    y=225,
    width=370,
    height=30
)
window.resizable(False, False)
window.mainloop()
