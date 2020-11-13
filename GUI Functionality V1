import backend
import tkinter as tk
from tkinter import ttk 

class mainPageFunctions:
    def unlockSongs(entry, var):
        if var.get() == 0:
            entry.configure(state='disabled')
        else:
            entry.configure(state='normal')
    
class IntEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        print(self.get())
        if self.get().isdigit() and int(self.get()) > 0 and int(self.get()) < 11: 
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this 
            self.set(self.old_value)
            
class MusicApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #Configuration of master window
        #self.title('Music Recommendation App')
        #self.configure(background = '#3BAD40')
        self.attributes("-fullscreen", True)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for f in (StartPage, ResultPage):
            pageName = f.__name__
            frame = f(parent = container, controller = self)
            self.frames[pageName] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        #Variable Defintions
        checkVar3 = tk.IntVar() #Variable of whether show recommended songs is checked
        checkVar4 = tk.IntVar() #Variable of whether show recommended artists is checked
        
        bgFrame = tk.Frame(self, bg = '#067625')
        bgFrame.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
        
        fullScreenButton = tk.Button(bgFrame, text = "fullscreen", command = lambda: root.attributes("-fullscreen", not root.attributes('-fullscreen')))
        exitButton = tk.Button(bgFrame, text = 'exit', command = lambda: root.destroy())
        
        leftFrame = tk.Frame(bgFrame, bg = '#5ACC72', highlightbackground="#4F8451", highlightthickness=2)
        topFrame = tk.Frame(leftFrame, bg = '#5ACC72')
        bottomFrame = tk.Frame(leftFrame, bg = '#52F059', highlightbackground="#4F8451", highlightthickness=2)

        
        titleLabel = tk.Label(topFrame, text = "A New Way to Discover Music",
                           fg ="#fcd8e9", font = ('Gadugi', 60, 'italic', 'bold'),
                           pady = 70, padx = 50, bg = '#5ACC72')
        titleLabel.grid(column = 0, row = 0, columnspan = 2, rowspan = 2, sticky = 'nw')

        validUsernameText = tk.Label(topFrame, text = "Invalid Username!", fg = 'red', bg = '#5ACC72', font =('Segoe UI', 22))
        #validUsernameText.grid(row = 3, column = 1, sticky = 'n', padx = (0, 90))
        
        enterTextLabel = tk.Label(topFrame, text = "Enter Spotify Username:",
                               font = ('Segoe UI', 32, 'bold'), bg = '#5ACC72', fg = '#383F38')
        enterTextLabel.grid(row = 2, column = 0)

        usernameEntry = tk.Entry(topFrame, bg = 'white', fg = '#5ACC72', font =('Segoe UI', 28), width = 25)
        usernameEntry.grid(row = 2, column = 1, sticky = 'w', pady = 10)

        self.musicNoteImage = tk.PhotoImage(file = r'C:\Users\M38853\Downloads\try1.png')
        musicLabel = tk.Label(topFrame, image = self.musicNoteImage, bg = '#5ACC72')
        musicLabel.grid(row = 0, column = 3, rowspan = 4, pady = (20, 0), padx = 20)

        topFrame.grid(row = 0, column = 0)

        numSongsEntry = IntEntry(bottomFrame, bg = '#E9F0EA', fg = 'black', state = tk.DISABLED, width = 8)
        numSongsLabel = tk.Label(bottomFrame, text = "= Number of Recommended Songs (1-10)", bg = "#52F059", font = ('Segoe UI', 18))
        numArtistsEntry = IntEntry(bottomFrame, bg = '#E9F0EA', fg = 'black', state = tk.DISABLED, width = 8)
        numArtistsLabel = tk.Label(bottomFrame, text = "= Number of Recommended Artists (1-10)", bg = "#52F059", font = ('Segoe UI', 18))

        toDisplayCheckButton1 = tk.Checkbutton( bottomFrame, text = "Show Top Genres", bg = "#52F059", font = ('Segoe UI', 18))
        toDisplayCheckButton2 = tk.Checkbutton( bottomFrame, text = "Show Top Artists", bg = "#52F059", font = ('Segoe UI', 18))
        toDisplayCheckButton3 = tk.Checkbutton( bottomFrame, text = "Show Recommended Songs", bg = "#52F059", variable = checkVar3,
                                                command =lambda e=numSongsEntry: mainPageFunctions.unlockSongs(e, checkVar3), font = ('Segoe UI', 18))
        toDisplayCheckButton4 = tk.Checkbutton( bottomFrame, text = "Show Recommended Artists", bg = "#52F059", variable = checkVar4,
                                                command =lambda e=numArtistsEntry: mainPageFunctions.unlockSongs(e, checkVar4), font = ('Segoe UI', 18))

        startButton = tk.Button(bottomFrame, text = "Get Your Music!", font = ('Segoi UI', 48, 'bold'),
                             fg = '#75F993', bg = '#383F38', relief = tk.RIDGE, activeforeground = '#5ACC72', command =lambda: validateUsername(usernameEntry.get(), validUsernameText))

        
        toDisplayCheckButton1.grid(row = 0, column = 0, sticky = 'w', padx = 30, pady = (40, 0), columnspan = 2)
        toDisplayCheckButton2.grid(row = 1, column = 0, sticky = 'w', padx = 30, columnspan = 2)
        toDisplayCheckButton3.grid(row = 2, column = 0, sticky = 'w', padx = 30, columnspan = 2)
        toDisplayCheckButton4.grid(row = 4, column = 0, sticky = 'w', padx = 30, columnspan = 2)
        
        numSongsEntry.grid(row = 3, column = 0, padx = (100,0))
        numSongsLabel.grid(row = 3, column = 1, padx = 0, sticky = 'w')
        numArtistsEntry.grid(row = 5, column = 0, padx = (100,0))
        numArtistsLabel.grid(row = 5, column = 1, padx = 0, sticky = 'w')

        fullScreenButton.place(relx = .94, rely = .01, relwidth = .03, relheight = .02)
        exitButton.place(relx = .975, rely = .01, relwidth = .02, relheight = .02)
        startButton.grid(row = 1, column = 2, rowspan = 6, sticky = 'w', padx = (160, 0))
        bottomFrame.grid(row = 1, column =0, pady  = (40, 60), ipadx = 60, ipady = 60, padx = 40)
        leftFrame.pack(expand = True)


        def validateUsername(username, errorText):
            isValid = backend.validateEntry(username)
            
            if isValid:
                controller.show_frame("ResultPage")
                errorText.grid_forget()

            else: 
                errorText.grid(row = 3, column = 1, sticky = 'n', padx = (0, 90))


class ResultPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        bgFrame = tk.Frame(self, bg = '#067625')
        nwFrame = tk.Frame(self, bg = '#5ACC72', highlightbackground="#383F38", highlightthickness=2)
        neFrame = tk.Frame(self, bg = '#5ACC72', highlightbackground="#383F38", highlightthickness=2)
        swFrame = tk.Frame(self, bg = '#5ACC72', highlightbackground="#383F38", highlightthickness=2)
        seFrame = tk.Frame(self, bg = '#5ACC72', highlightbackground="#383F38", highlightthickness=2)
        
        fullScreenButton = tk.Button(bgFrame, text = "fullscreen", command = lambda: root.attributes("-fullscreen", not root.attributes('-fullscreen')))
        exitButton = tk.Button(bgFrame, text = 'exit', command = lambda: root.destroy())
        
        mainLabel = tk.Label(self, text = "Aaaaaaand here you go!", bg = '#067625', font = ('Segoe UI', 32, 'bold'), fg = 'white')
        returnButton = tk.Button(self, text = 'Return to welcome page', command = lambda: controller.show_frame("StartPage"), bg = '#383F38', fg = "#75F993", font = ('Segoe UI', 12))
        exportButton = tk.Button(self, text = 'Export Results', bg = '#383F38', fg = "#75F993", font = ('Segoe UI', 12))
        
        nwLabel = tk.Label(nwFrame, text = "Your Top Genres", bg = "#383F38", fg = "#75F993", font = ('Segoe UI', 16))
        neLabel = tk.Label(neFrame, text = "Your Top Artists", bg = "#383F38", fg = "#75F993", font = ('Segoe UI', 16))
        swLabel = tk.Label(swFrame, text = "Recommended Songs", bg = "#383F38", fg = "#75F993", font = ('Segoe UI', 16))
        seLabel = tk.Label(seFrame, text = "Recommended Artists", bg = "#383F38", fg = "#75F993", font = ('Segoe UI', 16))

        nwLabel.grid(row = 0, column = 0, columnspan = 3)
        neLabel.grid(row = 0, column = 0, columnspan = 3)
        swLabel.grid(row = 0, column = 0, columnspan = 3)
        seLabel.grid(row = 0, column = 0, columnspan = 3)

        bgFrame.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)
        nwFrame.place(relx = .05, rely = .1, relheight = .4, relwidth = .44)
        neFrame.place(relx = .51, rely = .1, relheight = .4, relwidth = .44)
        swFrame.place(relx = .05, rely = .55, relheight = .4, relwidth = .44)
        seFrame.place(relx = .51, rely = .55, relheight = .4, relwidth = .44)
        mainLabel.place(relx = .35, rely = .02, relheight = .07, relwidth = .3)
        
        returnButton.place(relx = .705, rely = .03, relheight = .05, relwidth = .1)
        exportButton.place(relx = .82, rely = .03, relheight = .05, relwidth = .1)
        fullScreenButton.place(relx = .94, rely = .01, relwidth = .03, relheight = .02)
        exitButton.place(relx = .975, rely = .01, relwidth = .02, relheight = .02)

        
root = MusicApp()
def main(): 
    #feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__": main()
