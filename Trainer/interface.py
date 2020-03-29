import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from PIL import ImageTk, Image

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
  

        self.img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imgs', 'img.png')))
        img_label = Button(image=self.img)
        img_label.grid(row=0, column=0, columnspan=4)

        self.titulo = Label(text="HOTKEYS")
        self.titulo["font"] = ("Arial", "13", "bold")
        self.titulo.grid(row=1, column=0, sticky='nesw', columnspan=4)

        # self.space = Label(text='            ')
        # self.space.grid(row=0, column=1)
  
        ################
        ##### food #####
        ################
        self.foodLabel = Label(text="Food: ", font=self.fontePadrao, anchor="e")
        self.foodLabel.grid(sticky='nesw', row=2, column=0)
  
        self.food = Entry()
        self.food["width"] = 5
        self.food["font"] = self.fontePadrao
        self.food.grid(sticky='nesw', row=2, column=1)
        ################
        ##### soft #####
        ################
        self.softLabel = Label(text="Soft: ", font=self.fontePadrao)
        self.softLabel.grid(sticky='nesw',row=2, column=2)
  
        self.soft = Entry()
        self.soft["width"] = 5
        self.soft["font"] = self.fontePadrao
        self.soft.grid(sticky='nesw',row=2, column=3)
        ################
        ##### ring #####
        ################
        self.ringLabel = Label(text="Ring: ", font=self.fontePadrao)
        self.ringLabel.grid(sticky='nesw', row=3, column=0)
  
        self.ring = Entry()
        self.ring["width"] = 5
        self.ring["font"] = self.fontePadrao
        self.ring.grid(sticky='nesw', row=3, column=1)
        ################
        ##### rune #####
        ################
        self.runeLabel = Label(text="Rune: ", font=self.fontePadrao)
        self.runeLabel.grid(sticky='nesw',row=3, column=2)
  
        self.rune = Entry()
        self.rune["width"] = 5
        self.rune["font"] = self.fontePadrao
        self.rune.grid(sticky='nesw', row=3, column=3)
        ######################
        ##### SCREENSHOT #####
        ######################
        self.hotkeys = Label(text="SCREENSHOT")
        self.hotkeys["font"] = ("Arial", "13", "bold")
        self.hotkeys.grid(row=4, column=1, columnspan=2, sticky='nesw')
        ##################
        ##### browse #####
        ##################
        self.Browse = Button()
        self.Browse.config( height = 1  , width = 1 )
        self.Browse["width"] = 10
        self.Browse["text"] = "Browse"
        self.Browse["font"] = ("Calibri", "8")
        self.Browse["command"] = self.browse_button
        self.Browse.grid(row=5, column=2, columnspan=2)

        self.ssHotkeyLabel = Label(text="SS Hotkey: ")
        self.ssHotkeyLabel["font"] = ("Arial", "10")
        self.ssHotkeyLabel.grid(row=5, column=0, columnspan=2, sticky='w')

        self.ssHotkey = Entry()
        self.ssHotkey["width"] = 5
        self.ssHotkey["font"] = self.fontePadrao
        self.ssHotkey.grid(sticky='nesw', row=5, column=1)
  
    def browse_button(self):

        # Allow user to select a directory and store it in global var
        # called folder_path
        # global folder_path
        filename = filedialog.askdirectory()
        # folder_path.set(filename)
        print(filename)

    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
            path = askdirectory(title='Select Folder') # shows dialog box and return the path
            print(path)  
        else:
            self.mensagem["text"] = "Erro na autenticação"
  
  
root = Tk()
Application(root)
root.title('Penis Alado')
root.iconbitmap(os.path.join(os.path.dirname(__file__), 'imgs', 'ico.ico'))


root.mainloop()