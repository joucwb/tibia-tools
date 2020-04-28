import os
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import webbrowser
import settings
from main import Main
from dummy import Dummy
import win32api
import pickle
import time

LARGE_FONT = ('Verdana', 12)

class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        globals = self.load_configs()
        global SS_HOTKEY 
        global SS_DIRPATH 
        global RING_HOTKEY 
        global FOOD_HOTKEY 
        global SOFT_HOTKEY
        global RUNE_HOTKEY 
        global CHAR_NAME
        global CYCLE_TIME
        global RUNES_PER_CYCLE
        global EXERCISE_WEAPON_HOTKEY

        SS_HOTKEY = globals[0]
        SS_DIRPATH = globals[1]
        RING_HOTKEY = globals[2]
        FOOD_HOTKEY = globals[3]
        SOFT_HOTKEY = globals[4]
        RUNE_HOTKEY = globals[5]
        CHAR_NAME = globals[6]
        CYCLE_TIME = globals[7]
        RUNES_PER_CYCLE = globals[8]
        EXERCISE_WEAPON_HOTKEY = globals[9]

        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)
        container.grid(row=16, column=1, columnspan=4, sticky='nswe', pady='10')

        self.frames = {}

        for F in (StartPage, PageOne):
            frame = F(parent=container, controller=self)
            self.frames[F] = frame
            frame.grid(row=12, column=2, sticky='nsew')
            
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def quit(self):
        GUI.destroy(self)

    def call_main(self):
        m = Main(SS_HOTKEY, SS_DIRPATH, RING_HOTKEY, 
            FOOD_HOTKEY, SOFT_HOTKEY, RUNE_HOTKEY, CHAR_NAME, CYCLE_TIME, RUNES_PER_CYCLE)
        m.main()

    def load_configs(self):
        return pickle.load(open('vars.dat', 'rb'))

    def enable_mouseposition(self):
    	print('~'*30)
    	print('AGUARDANDO O CLIQUE NO DUMMY...')
    	print('APÓS USAR O DUMMY NÃO SE MEXA!')
    	settings.get_tibia_active(CHAR_NAME)
    	self.after(10, self.get_mouseposition)

    def get_mouseposition(self):
    	state_left = win32api.GetKeyState(0x01)
    	if state_left == -127 or state_left == -128:
    		xclick, yclick = win32api.GetCursorPos()
    		dummy_pos = xclick, yclick
    		d = Dummy(EXERCISE_WEAPON_HOTKEY, CHAR_NAME, dummy_pos)
    		self.quit()
    		d.main()
    	else:
    		self.after(10, self.get_mouseposition)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.ssDirPath = SS_DIRPATH
        ################
        ##### img ###### BUTTON
        ################
        self.img = ImageTk.PhotoImage(Image.open(os.path.join(os.path.dirname(__file__), 'imgs', 'img.png')))
        self.img_label = tk.Button(image=self.img)
        self.img_label.grid(row=0, column=0, columnspan=4)

        ################
        ##### char ##### LABEL + ENTRY
        ################
        self.charLabel = tk.Label(text="Character Name: ", font=LARGE_FONT)
        self.charLabel.grid(row=1, column=0, columnspan=2, pady='10')
        self.charEntry = tk.StringVar(parent, value=CHAR_NAME)
        self.char = tk.Entry(textvariable=self.charEntry)
        # self.char["width"] = 23
        self.char["font"] = LARGE_FONT
        self.char.grid(row=1, column=2, columnspan=2, sticky='w', padx=10)

        ####################
        ##### HOTKEYS ###### LABEL
        ####################
        self.titulo = tk.Label(text="HOTKEYS:")
        self.titulo["font"] = ("Arial", "13", "bold")
        self.titulo.grid(row=2, column=0, sticky='nesw', columnspan=4, pady='5', padx='5')

        ################
        ##### food ##### LABEL + ENTRY
        ################
        self.foodLabel = tk.Label(text="Food:", font=LARGE_FONT)
        self.foodLabel.grid(row=3, column=0, columnspan=1)
        self.foodEntry = tk.StringVar(parent, value=FOOD_HOTKEY)
        self.food = tk.Entry(textvariable = self.foodEntry)
        self.food["width"] = 5
        self.food["font"] = LARGE_FONT
        self.food.grid(row=3, column=1, columnspan=1)

        ################
        ##### soft ##### LABEL + ENTRY
        ################
        self.softLabel = tk.Label(text="Soft:", font=LARGE_FONT)
        self.softLabel.grid(row=3, column=2, columnspan=1, sticky='we')
        self.softEntry = tk.StringVar(parent, value=SOFT_HOTKEY)
        self.soft = tk.Entry(textvariable=self.softEntry)
        self.soft["width"] = 6
        self.soft["font"] = LARGE_FONT
        self.soft.grid(row=3, column=3, columnspan=1, sticky='w')

        ################
        ##### ring ##### LABEL + ENTRY
        ################
        self.ringLabel = tk.Label(text="Ring:", font=LARGE_FONT)
        self.ringLabel.grid(row=4, column=0)
        self.ringEntry = tk.StringVar(parent, value=RING_HOTKEY)
        self.ring = tk.Entry(textvariable=self.ringEntry)
        self.ring["width"] = 5
        self.ring["font"] = LARGE_FONT
        self.ring.grid(row=4, column=1, padx='5', sticky='w')

        ################
        ##### rune ##### LABEL + ENTRY
        ################
        self.runeLabel = tk.Label(text="Rune:", font=LARGE_FONT)
        self.runeLabel.grid(row=4, column=2)
        self.runeEntry = tk.StringVar(parent, value=RUNE_HOTKEY)
        self.rune = tk.Entry(textvariable=self.runeEntry)
        self.rune["width"] = 6
        self.rune["font"] = LARGE_FONT
        self.rune.grid(row=4, column=3, sticky='w')

        ##################
        ### screenshot ### LABEL + ENTRY
        ##################
        self.ssHotkeyLabel = tk.Label(text="Screenshot:")
        self.ssHotkeyLabel["font"] = LARGE_FONT
        self.ssHotkeyLabel.grid(row=6, column=0, sticky='w')
        self.ssHotkeyEntry = tk.StringVar(parent, value=SS_HOTKEY)
        self.ssHotkey = tk.Entry(textvariable=self.ssHotkeyEntry)
        self.ssHotkey["width"] = 5
        self.ssHotkey["font"] = LARGE_FONT
        self.ssHotkey.grid(row=6, column=1)

        ##################
        ##### browse ##### BUTTON
        ##################
        self.Browse = tk.Button()
        self.Browse["width"] = 10
        self.Browse["text"] = "Browse"
        self.Browse["font"] = ("Calibri", "10")
        self.Browse["command"] = self.browse_dirpath
        self.Browse.grid(row=6, column=2, columnspan=4)

        ######################
        ##### CONFIG ######### LABEL
        ######################
        self.cycleConfig = tk.Label(text="CYCLE CONFIG:")
        self.cycleConfig["font"] = ("Arial", "13", "bold")
        self.cycleConfig.grid(row=7, columnspan= 4, sticky='nesw',padx='20',pady='10')

        ######################
        ##### cycle time ##### LABEL + ENTRY
        ######################
        self.cycleTimeLabel = tk.Label(text="Cycle Time:")
        self.cycleTimeLabel["font"] = LARGE_FONT
        self.cycleTimeLabel.grid(row=8, column=0,padx='5', pady='5')
        self.cycleTimeEntry = tk.StringVar(parent, value=CYCLE_TIME)
        self.cycleTime = tk.Entry(textvariable=self.cycleTimeEntry)
        self.cycleTime["width"] = 5
        self.cycleTime["font"] = LARGE_FONT
        self.cycleTime.grid(row=8, column=1)

        ######################
        ### runes p/ cycle ### LABEL + ENTRY
        ######################
        self.runesCycleLabel = tk.Label(text="Runes p/ Cycle:")
        self.runesCycleLabel["font"] = LARGE_FONT
        self.runesCycleLabel.grid(row=8, column=2)

        self.runesCycleLabel = tk.Label(text="(in minutes)")
        self.runesCycleLabel["font"] = "Verdana", 9
        self.runesCycleLabel.grid(row=9, column=0, sticky='n')
        self.runesCycleEntry = tk.StringVar(parent, value=RUNES_PER_CYCLE)
        self.runesCycle = tk.Entry(textvariable=self.runesCycleEntry)
        self.runesCycle["width"] = 5
        self.runesCycle["font"] = LARGE_FONT
        self.runesCycle.grid(row=8, column=3, columnspan=1, padx='10', sticky='w')

        ######################
        #### save configs #### BUTTON
        ######################
        self.saveConfigsButton = tk.Button()
        self.saveConfigsButton["width"] = 20
        self.saveConfigsButton["text"] = "Save Configs"
        self.saveConfigsButton["font"] = ("Calibri", "10")
        self.saveConfigsButton["command"] = self.save_configs
        self.saveConfigsButton.grid(row=9, column=1, columnspan=4)

        ######################
        #### ~ ~space~ ~ ##### SPECIAL SPACE
        ######################
        self._space = tk.Label(text="- -"*20)
        self._space["font"] = ("Arial", "11", "bold")
        self._space.grid(row=10, column=0, sticky='nesw',padx='30',pady='5', columnspan=4)

        ######################
        ##### need help? ##### LABEL
        ######################
        self.needHelpLabel = tk.Label(text="Need Help?")
        self.needHelpLabel["font"] = ("Arial", "11", "bold")
        self.needHelpLabel.grid(row=11, column=0, sticky='nesw',padx='30',pady='5', columnspan=2)

        ######################
        ####### ready? ####### LABEL
        ######################
        self.trainLabel = tk.Label(text="Ready?")
        self.trainLabel["font"] = ("Arial", "11", "bold")
        self.trainLabel.grid(row=11, column=2, sticky='nesw',padx='30',pady='5', columnspan=2)

        ######################
        ###### tutorial ###### BUTTON
        ######################
        self.tutorialButton = tk.Button()
        self.tutorialButton["width"] = 20
        self.tutorialButton["text"] = "Tutorial"
        self.tutorialButton["font"] = ("Calibri", "10")
        self.tutorialButton["bg"] = "green"
        self.tutorialButton["fg"] = "white"
        self.tutorialButton["command"] = self.browse_tutorial
        self.tutorialButton.grid(row=12, column=0, columnspan=2)

        ######################
        ####### train ######## BUTTON
        ######################
        self.trainButton = tk.Button()
        self.trainButton["width"] = 20
        self.trainButton["text"] = "Train"
        self.trainButton["font"] = ("Calibri", "10")
        self.trainButton["bg"] = "red"
        self.trainButton["fg"] = "white"
        self.trainButton["command"] = lambda:[controller.quit(), controller.call_main()]
        self.trainButton.grid(row=12, column=2, columnspan=2, pady='10')

        ################################
        ####### Training with Dummys? ####### LABEL
        ################################
        self.dummyLabel = tk.Label(text="Training with Dummys?")
        self.dummyLabel["font"] = ("Arial", "11", "bold")
        self.dummyLabel.grid(row=13,columnspan=4)

        #####################
        ### weapon hotkey ### LABEL + ENTRY
        #####################
        self.weaponHotkeyLabel = tk.Label(text="Weapon Hotkey:")
        self.weaponHotkeyLabel["font"] = LARGE_FONT
        self.weaponHotkeyLabel.grid(row=14, column=0, sticky='w')
        self.weaponHotkeyEntry = tk.StringVar(parent, value=EXERCISE_WEAPON_HOTKEY)
        self.weaponHotkey = tk.Entry(textvariable=self.weaponHotkeyEntry)
        self.weaponHotkey["width"] = 5
        self.weaponHotkey["font"] = LARGE_FONT
        self.weaponHotkey.grid(row=14, column=1)

        ################################
        ####### Exercise Weapon ######## BUTTON
        ################################
        self.weaponButton = tk.Button()
        self.weaponButton["width"] = 20
        self.weaponButton["text"] = "Exercise Weapon"
        self.weaponButton["font"] = ("Calibri", "10")
        self.weaponButton["bg"] = "red"
        self.weaponButton["fg"] = "white"
        # self.weaponButton["command"] = lambda:[controller.quit(), controller.call_main()]
        self.weaponButton["command"] = lambda:[controller.enable_mouseposition()]
        self.weaponButton.grid(row=14,column=2,columnspan=3, pady='10')
        

        ######################
        #### ~ ~space~ ~ ##### SPECIAL SPACE
        ######################
        self._space = tk.Label(text="- -"*20)
        self._space["font"] = ("Arial", "11", "bold")
        self._space.grid(row=15, column=0, sticky='nesw',padx='30',pady='5', columnspan=4)

        self.samukzLabel = tk.Label(text="KUMAS v0.1.1")
        self.samukzLabel["font"] = ("Verdana", "13", "italic")
        self.samukzLabel.grid(row=16, column=0, columnspan=2)

        self.samukzLabel = tk.Label(text="by samukZ")
        self.samukzLabel["font"] = ("Verdana", "13", "italic")
        self.samukzLabel.grid(row=16, column=2, columnspan=2)


    def browse_tutorial(self):
        webbrowser.open('http://www.github.com/samuelbfg/tibia-tools', new=2)

    def save_configs(self):
        variables = [self.ssHotkeyEntry.get(),self.ssDirPath,self.ringEntry.get(),self.foodEntry.get(),
        self.softEntry.get(),self.runeEntry.get(),self.charEntry.get(),
        self.cycleTimeEntry.get(),self.runesCycleEntry.get(),self.weaponHotkeyEntry.get()]
        pickle.dump(variables, open('vars.dat', 'wb'))
        print('- -- -'*10)
        print('Configurações Atualizadas:')
        print('Char - '+(self.charEntry.get()))
        print('Diretório - '+(self.ssDirPath))
        print('Food Hotkey - '+str(self.foodEntry.get()))
        print('Ring Hotkey - '+str(self.ringEntry.get()))
        print('Soft Hotkey - '+str(self.softEntry.get()))
        print('Rune Hotkey - '+str(self.runeEntry.get()))       
        print('Screenshot Hotkey - '+str(self.ssHotkeyEntry.get()))
        print('Tempo de Ciclo (minutos) - '+str(self.cycleTimeEntry.get()))       
        print('Runas por Ciclo - '+str(self.runesCycleEntry.get()))
        print('Hotkey da Exercise Weapon - '+str(self.weaponHotkeyEntry.get()))
        print('- -- -'*10)

    def browse_dirpath(self):
        filename = filedialog.askdirectory()
        self.ssDirPath = filename
        print('Diretório de Screenshots Atualizado!')

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.trainButton = tk.Button(self)
        self.trainButton["width"] = 20
        self.trainButton["text"] = "Stop Trainer"
        self.trainButton["font"] = ("Calibri", "10")
        self.trainButton["bg"] = "red"
        self.trainButton["fg"] = "white"
        # self.trainButton["command"] = self.terminate
        self.trainButton.grid()


if __name__ == "__main__":
    app = GUI()
    app.title('KUMAS Trainer')
    app.iconbitmap(os.path.join(os.path.dirname(__file__), 'imgs', 'be.ico'))
    app.resizable(width=False, height=False)
    app.mainloop()