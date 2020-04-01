import os
import tkinter as tk
from PIL import ImageTk, Image
import webbrowser
from main import Main
import pickle
import time

LARGE_FONT = ('Verdana', 12)

'''
variables
'''
# SS_HOTKEY = "f12"
# SS_DIRPATH = "D:/Games/Tibia/packages/Tibia/screenshots/"
# RING_HOTKEY = "f8"
# FOOD_HOTKEY = "f10"
# SOFT_HOTKEY = "-"
# RUNE_HOTKEY = "0"
# CHAR_NAME = "Biel Huntedz"
# CYCLE_TIME = 2
# RUNES_PER_CYCLE = 3




class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        globals = self.load_configs()
        # print(len(globals
        global SS_HOTKEY 
        global SS_DIRPATH 
        global RING_HOTKEY 
        global FOOD_HOTKEY 
        global SOFT_HOTKEY
        global RUNE_HOTKEY 
        global CHAR_NAME
        global CYCLE_TIME
        global RUNES_PER_CYCLE
        # self.SS_HOTKEY = globals[0]
        # self.SS_DIRPATH = globals[1]
        # self.RING_HOTKEY = globals[2]
        # self.FOOD_HOTKEY = globals[3]
        # self.SOFT_HOTKEY = globals[4]
        # self.RUNE_HOTKEY = globals[5]
        # self.CHAR_NAME = globals[6]
        # self.CYCLE_TIME = globals[7]
        # self.RUNES_PER_CYCLE = globals[8]
        SS_HOTKEY = globals[0]
        SS_DIRPATH = globals[1]
        RING_HOTKEY = globals[2]
        FOOD_HOTKEY = globals[3]
        SOFT_HOTKEY = globals[4]
        RUNE_HOTKEY = globals[5]
        CHAR_NAME = globals[6]
        CYCLE_TIME = globals[7]
        RUNES_PER_CYCLE = globals[8]
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.grid(row=16, column=1, columnspan=4, sticky='nswe', pady='10')
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

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
        m = Main()
        m.main()


    def load_configs(self):
        return pickle.load(open('vars.dat', 'rb'))

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
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
        controller.FOOD_HOTKEY = self.foodEntry.get()
        print(controller.FOOD_HOTKEY)
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
        # self.Browse["command"] = self.browse_button
        self.Browse.grid(row=6, column=2, columnspan=4)

        ######################
        ##### CONFIG ######### LABEL
        ######################
        self.cycleConfig = tk.Label(text="CYCLE CONFIG:")
        self.cycleConfig["font"] = ("Arial", "13", "bold")
        self.cycleConfig.grid(row=7, columnspan= 4, sticky='nesw',padx='20',pady='10')

        # ######################
        # ##### cycle time ##### LABEL + ENTRY
        # ######################
        # self.ssHotkeyLabel = tk.Label(text="Screenshot:")
        # self.ssHotkeyLabel["font"] = LARGE_FONT
        # self.ssHotkeyLabel.grid(row=8, column=0)

        # self.ssHotkey = tk.Entry()
        # self.ssHotkey["width"] = 5
        # self.ssHotkey["font"] = LARGE_FONT
        # self.ssHotkey.grid(row=8, column=1)

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

        ######################
        #### ~ ~space~ ~ ##### SPECIAL SPACE
        ######################
        self._space = tk.Label(text="- -"*20)
        self._space["font"] = ("Arial", "11", "bold")
        self._space.grid(row=13, column=0, sticky='nesw',padx='30',pady='5', columnspan=4)

        self.samukzLabel = tk.Label(text="KUMAS v0.1.0")
        self.samukzLabel["font"] = ("Verdana", "13", "italic")
        self.samukzLabel.grid(row=14, column=0, columnspan=2)

        self.samukzLabel = tk.Label(text="by samukZ")
        self.samukzLabel["font"] = ("Verdana", "13", "italic")
        self.samukzLabel.grid(row=14, column=2, columnspan=2)


    def browse_tutorial(self):
        webbrowser.open('http://www.github.com/samuelbfg/tibia-tools', new=2)

    def save_configs(self):
        # SS_HOTKEY = self.SS_HOTKEY
        variables = [self.ssHotkeyEntry.get(),SS_DIRPATH,RING_HOTKEY,FOOD_HOTKEY,
        SOFT_HOTKEY,RUNE_HOTKEY,CHAR_NAME,
        CYCLE_TIME,RUNES_PER_CYCLE]
        print(self.ssHotkeyEntry.get())
        # variables = [self.SS_HOTKEY,self.SS_DIRPATH,self.RING_HOTKEY,self.FOOD_HOTKEY,
        # self.SOFT_HOTKEY,self.RUNE_HOTKEY,self.CHAR_NAME,
        # self.CYCLE_TIME,self.RUNES_PER_CYCLE]
        pickle.dump(variables, open('vars.dat', 'wb'))
        # print(variables)

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