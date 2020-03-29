import os
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from PIL import ImageTk, Image
from main import Main
import webbrowser

class GUI:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
  
        ################
        ##### img ###### BUTTON
        ################
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imgs', 'img.png')))
        img_label = Button(image=self.img)
        img_label.grid(row=0, column=0, columnspan=4)


        ####################
        ##### hotkeys ###### LABEL
        ####################
        self.titulo = Label(text="HOTKEYS:")
        self.titulo["font"] = ("Arial", "13", "bold")
        self.titulo.grid(row=2, column=0, sticky='nesw', columnspan=4, pady='5', padx='5')

        ################
        ##### char ##### LABEL + ENTRY
        ################
        self.foodLabel = Label(text="Character: ", font=self.fontePadrao)
        self.foodLabel.grid(row=1, column=0, columnspan=2, pady='10')
  
        self.food = Entry()
        # self.food["width"] = 23
        # self.food["font"] = self.fontePadrao
        self.food.grid(row=1, column=2, columnspan=2, sticky='w')
  
        ################
        ##### food ##### LABEL + ENTRY
        ################
        self.foodLabel = Label(text="Food: ", font=self.fontePadrao)
        self.foodLabel.grid(row=3, column=0, columnspan=1)
  
        self.food = Entry()
        self.food["width"] = 5
        self.food["font"] = self.fontePadrao
        self.food.grid(row=3, column=1, columnspan=1)

        ################
        ##### soft ##### LABEL + ENTRY
        ################
        self.softLabel = Label(text="Soft: ", font=self.fontePadrao)
        self.softLabel.grid(row=3, column=2, columnspan=1, sticky='we')

        self.soft = Entry()
        self.soft["width"] = 5
        # self.rune["font"] = self.fontePadrao
        self.soft.grid(row=3, column=3, columnspan=1, sticky='w')

        ################
        ##### ring ##### LABEL + ENTRY
        ################
        self.ringLabel = Label(text="Ring: ", font=self.fontePadrao)
        self.ringLabel.grid(row=4, column=0)
  
        self.ring = Entry()
        self.ring["width"] = 5
        self.ring["font"] = self.fontePadrao
        self.ring.grid(row=4, column=1,padx='5', sticky='w')

        ################
        ##### rune ##### LABEL + ENTRY
        ################
        self.runeLabel = Label(text="Rune: ", font=self.fontePadrao)
        self.runeLabel.grid(row=4, column=2)
  
        self.rune = Entry()
        self.rune["width"] = 5
        self.rune["font"] = self.fontePadrao
        self.rune.grid(row=4, column=3)

        ##################
        ##### browse ##### BUTTON
        ##################
        self.ssHotkeyLabel = Label(text="Screenshot: ")
        self.ssHotkeyLabel["font"] = ("Arial", "10")
        self.ssHotkeyLabel.grid(row=6, column=0, sticky='w')

        self.ssHotkey = Entry()
        self.ssHotkey["width"] = 5
        self.ssHotkey["font"] = self.fontePadrao
        self.ssHotkey.grid(row=6, column=1)

        self.Browse = Button()
        self.Browse["width"] = 10
        self.Browse["text"] = "Browse"
        self.Browse["font"] = ("Calibri", "8")
        self.Browse["command"] = self.browse_button
        self.Browse.grid(row=6, column=2, columnspan=4)

        ######################
        ##### CONFIG ######### LABEL
        ######################
        self.hotkeys = Label(text="CYCLE CONFIG:")
        self.hotkeys["font"] = ("Arial", "13", "bold")
        self.hotkeys.grid(row=7, columnspan= 4, sticky='nesw',padx='20',pady='5')

        self.ssHotkeyLabel = Label(text="Screenshot: ")
        self.ssHotkeyLabel["font"] = ("Arial", "10")
        self.ssHotkeyLabel.grid(row=8, column=0)

        self.ssHotkey = Entry()
        self.ssHotkey["width"] = 5
        self.ssHotkey["font"] = self.fontePadrao
        self.ssHotkey.grid(row=8, column=1)

        self.ssHotkeyLabel = Label(text="Cycle Time: ")
        self.ssHotkeyLabel["font"] = ("Arial", "10")
        self.ssHotkeyLabel.grid(row=8, column=0,padx='5', pady='5')

        self.ssHotkey = Entry()
        self.ssHotkey["width"] = 5
        self.ssHotkey["font"] = self.fontePadrao
        self.ssHotkey.grid(row=8, column=1)

        self.ssHotkeyLabel = Label(text="Runes p/ Cycle: ")
        self.ssHotkeyLabel["font"] = ("Arial", "10")
        self.ssHotkeyLabel.grid(row=8, column=2,padx='10')

        self.ssHotkey = Entry()
        self.ssHotkey["width"] = 5
        self.ssHotkey["font"] = self.fontePadrao
        self.ssHotkey.grid(row=8, column=3)

        self.hotkeys = Label(text="Need Help?")
        self.hotkeys["font"] = ("Arial", "11", "bold")
        self.hotkeys.grid(row=9, column=0, sticky='nesw',padx='20',pady='5', columnspan=2)

        # self.hotkeys = Label(text=":")
        # self.hotkeys["font"] = ("Arial", "13", "bold")
        # self.hotkeys.grid(row=9, column=1)

        self.hotkeys = Label(text="Ready?")
        self.hotkeys["font"] = ("Arial", "13", "bold")
        self.hotkeys.grid(row=9, column=2, sticky='nesw',padx='20',pady='10', columnspan=2)

        # self.hotkeys = Label(text=":")
        # self.hotkeys["font"] = ("Arial", "13", "bold")
        # self.hotkeys.grid(row=9, column= 3)


        self.Browse = Button()
        self.Browse["width"] = 20
        self.Browse["text"] = "Tutorial"
        self.Browse["font"] = ("Calibri", "10")
        self.Browse["bg"] = "green"
        self.Browse["fg"] = "white"
        self.Browse["command"] = self.browse_button
        self.Browse.grid(row=10, column=0, columnspan=2)

        self.Browse = Button()
        self.Browse["width"] = 20
        self.Browse["text"] = "Train"
        self.Browse["font"] = ("Calibri", "10")
        self.Browse["bg"] = "red"
        self.Browse["fg"] = "white"
        self.Browse["command"] = self.call_main
        self.Browse.grid(row=10, column=2, columnspan=2, pady='10')


    def call_main(self):
        self.quit()
        m = Main()
        m.main()

    def browse_button(self):
        webbrowser.open('http://www.github.com/samuelbfg/', new=2)

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

    def quit(self):
        self.root.destroy()
  
  
root = Tk()
GUI(root)
root.title('KUMAS 1.0')
# root.geometry("240x600")
root.iconbitmap(os.path.join(os.path.dirname(__file__), 'imgs', 'ico.ico'))
root.resizable(width=False, height=False)
root.mainloop()