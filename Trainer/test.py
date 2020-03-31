import os
import tkinter as tk
from PIL import ImageTk, Image
import webbrowser

LARGE_FONT = ('Verdana', 12)


class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)

        self.frames = {}

        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
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
  
        self.char = tk.Entry()
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
        self.foodLabel = tk.Label(text="Food: ", font=LARGE_FONT)
        self.foodLabel.grid(row=3, column=0, columnspan=1)
  
        self.food = tk.Entry()
        self.food["width"] = 5
        self.food["font"] = LARGE_FONT
        self.food.grid(row=3, column=1, columnspan=1)

        ################
        ##### soft ##### LABEL + ENTRY
        ################
        self.softLabel = tk.Label(text="Soft: ", font=LARGE_FONT)
        self.softLabel.grid(row=3, column=2, columnspan=1, sticky='we')

        self.soft = tk.Entry()
        self.soft["width"] = 6
        self.soft["font"] = LARGE_FONT
        self.soft.grid(row=3, column=3, columnspan=1, sticky='w')

        ################
        ##### ring ##### LABEL + ENTRY
        ################
        self.ringLabel = tk.Label(text="Ring: ", font=LARGE_FONT)
        self.ringLabel.grid(row=4, column=0)
  
        self.ring = tk.Entry()
        self.ring["width"] = 5
        self.ring["font"] = LARGE_FONT
        self.ring.grid(row=4, column=1, padx='5', sticky='w')

        ################
        ##### rune ##### LABEL + ENTRY
        ################
        self.runeLabel = tk.Label(text="Rune: ", font=LARGE_FONT)
        self.runeLabel.grid(row=4, column=2)
  
        self.rune = tk.Entry()
        self.rune["width"] = 6
        self.rune["font"] = LARGE_FONT
        self.rune.grid(row=4, column=3, sticky='w')

        ##################
        ### screenshot ### LABEL + ENTRY
        ##################
        self.ssHotkeyLabel = tk.Label(text="Screenshot: ")
        self.ssHotkeyLabel["font"] = LARGE_FONT
        self.ssHotkeyLabel.grid(row=6, column=0, sticky='w')

        self.ssHotkey = tk.Entry()
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

        ######################
        ##### cycle time ##### LABEL + ENTRY
        ######################
        self.ssHotkeyLabel = tk.Label(text="Screenshot: ")
        self.ssHotkeyLabel["font"] = LARGE_FONT
        self.ssHotkeyLabel.grid(row=8, column=0)

        self.ssHotkey = tk.Entry()
        self.ssHotkey["width"] = 5
        self.ssHotkey["font"] = LARGE_FONT
        self.ssHotkey.grid(row=8, column=1)

        ######################
        ##### cycle time ##### LABEL + ENTRY
        ######################
        self.cycleTimeLabel = tk.Label(text="Cycle Time: ")
        self.cycleTimeLabel["font"] = LARGE_FONT
        self.cycleTimeLabel.grid(row=8, column=0,padx='5', pady='5')

        self.cycleTime = tk.Entry()
        self.cycleTime["width"] = 5
        self.cycleTime["font"] = LARGE_FONT
        self.cycleTime.grid(row=8, column=1)

        ######################
        ### runes p/ cycle ### LABEL + ENTRY
        ######################
        self.runesCycleLabel = tk.Label(text="Runes p/ Cycle: ")
        self.runesCycleLabel["font"] = LARGE_FONT
        self.runesCycleLabel.grid(row=8, column=2)

        self.runesCycleLabel = tk.Label(text="(in minutes)")
        self.runesCycleLabel["font"] = "Verdana", 9
        self.runesCycleLabel.grid(row=9, column=0, sticky='n')

        self.runesCycle = tk.Entry()
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
        # self.saveConfigsButton["command"] = self.browse_tutorial
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
        self.trainButton["command"] = lambda:controller.show_frame(PageOne)
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


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.trainButton = tk.Button()
        self.trainButton["width"] = 20
        self.trainButton["text"] = "Train"
        self.trainButton["font"] = ("Calibri", "10")
        self.trainButton["bg"] = "red"
        self.trainButton["fg"] = "white"
        self.trainButton["command"] = lambda:controller.show_frame(StartPage)
        self.trainButton.grid(row=0, column=0, columnspan=2, pady='10')



app = GUI()
app.title('KUMAS Trainer')
app.iconbitmap(os.path.join(os.path.dirname(__file__), 'imgs', 'be.ico'))
app.resizable(width=False, height=False)
app.mainloop()