from tkinter import filedialog
import backend
import tkinter as tk
from tkinter import ttk 

### Music Recommendation App - 2020
### Made by: Ryan Rubadue

class mainPageFunctions:
    #Takes in checkbox and entry widgets. Unlocks/locks the text box for user entry based on status of checkbox
    def unlockSongs(entry, var):
        if var.get() == 0:
            entry.configure(state='disabled')
        else:
            entry.configure(state='normal')

    def exportToFile():
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        textToSave = backend.getTextToSave()
        f.write(textToSave)
        f.close()

        
#Inherits from the Entry widget class, but only allows for input of characters that can be numerically represented    
class IntEntry(tk.Entry):

    #Initialize IntEntry and call check function on value
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    #Ensure current entry value is valid in nature
    def check(self, *args):
        print(self.get())
        if self.get().isdigit() and int(self.get()) > 0 and int(self.get()) < 11: 
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this 
            self.set(self.old_value)

#High Level Creation of application page          
class MusicApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #Configure the page to be fullscreen and fill scale 1:1 to fit the screen if it is resized
        self.attributes("-fullscreen", True)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        #Create start and result pages and show the start page upon application launch
        self.frames = {}
        for f in (StartPage, ResultPage):
            pageName = f.__name__
            frame = f(parent = container, controller = self)
            self.frames[pageName] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')
        self.show_frame("StartPage")

    #Raise the frame corresponding to the name passed in. This will cause only this frame to be visible and all other non-child frames to be stacked below
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


#Contains all initialization and fucntionalities of the start page the user initially sees upon launching application.
#Inherits from tk.Frame class 
class StartPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        #Variable Defintions
        checkVar3 = tk.IntVar() #Variable of whether show recommended songs is checked
        checkVar4 = tk.IntVar() #Variable of whether show recommended artists is checked

        #Define and set a frame for the background to display a desired background color across the entire page behind all other widgets
        bgFrame = tk.Frame(self, bg = '#067625')
        bgFrame.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)

        #This button serves to toggle fullscreen mode for the application
        fullScreenButton = tk.Button(bgFrame, text = "fullscreen", command = lambda: root.attributes("-fullscreen", not root.attributes('-fullscreen')))
        #This button serves to provide a convenient way to exit the application
        exitButton = tk.Button(bgFrame, text = 'exit', command = lambda: root.destroy())

        #Hierarchy of frames for this page is as follows: bgFrame <- leftFrame <- (topFrame , bottom Frame) <- individual widgets contained within the top and bottom frame
        leftFrame = tk.Frame(bgFrame, bg = '#5ACC72', highlightbackground="#4F8451", highlightthickness=2)
        topFrame = tk.Frame(leftFrame, bg = '#5ACC72')
        bottomFrame = tk.Frame(leftFrame, bg = '#52F059', highlightbackground="#4F8451", highlightthickness=2)

        #Definition of topFrame elements
        titleLabel = tk.Label(topFrame, text = "A New Way to Discover Music",
                           fg ="#fcd8e9", font = ('Gadugi', 60, 'italic', 'bold'),
                           pady = 70, padx = 50, bg = '#5ACC72')
        titleLabel.grid(column = 0, row = 0, columnspan = 2, rowspan = 2, sticky = 'nw')

        validUsernameText = tk.Label(topFrame, text = "Invalid Username!", fg = 'red', bg = '#5ACC72', font =('Segoe UI', 22))
        
        enterTextLabel = tk.Label(topFrame, text = "Enter Spotify Username:",
                               font = ('Segoe UI', 32, 'bold'), bg = '#5ACC72', fg = '#383F38')
        enterTextLabel.grid(row = 2, column = 0)

        usernameEntry = tk.Entry(topFrame, bg = 'white', fg = '#5ACC72', font =('Segoe UI', 28), width = 25)
        usernameEntry.grid(row = 2, column = 1, sticky = 'w', pady = 10)

        self.musicNoteImage = tk.PhotoImage(file = r'C:\Users\M38853\Downloads\try1.png')
        musicLabel = tk.Label(topFrame, image = self.musicNoteImage, bg = '#5ACC72')
        musicLabel.grid(row = 0, column = 3, rowspan = 4, pady = (20, 0), padx = 20)
        #add top level frame to page
        topFrame.grid(row = 0, column = 0)

        #Definition of bottomFrame elements
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
        
        #When clicked the start button checks that the user has entered a valid username and either display an error message or changes to the result page appropriately. 
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
        #add bottomFrame to page
        bottomFrame.grid(row = 1, column =0, pady  = (40, 60), ipadx = 60, ipady = 60, padx = 40)
        #add leftFrame to page
        leftFrame.pack(expand = True)

        #Checks that the user inputted a valid username to the program. Takes in the user input and an error text widget to display in the case of invalid input. 
        def validateUsername(username, errorText):
            #Check validity in backend module
            isValid = backend.validateEntry(username)

            #Transition to results page and hide the error message in case the user previously entered bad input           
            if isValid:
                controller.show_frame("ResultPage")
                errorText.grid_forget()

            #Display error message
            else: 
                errorText.grid(row = 3, column = 1, sticky = 'n', padx = (0, 90))


#Contains all initialization and fucntionalities of the start page the user initially sees upon launching application.
#Inherits from tk.Frame class 
class ResultPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #bgFrame is the background for the whole page and displays an appropriate background color. 
        bgFrame = tk.Frame(self, bg = '#067625')
        
        #these four frames are children of the background frame and display categories of results found
        nwFrame = tk.Frame(self, bg = '#5ACC72', highlightbackground="#383F38", highlightthickness=2)
        neFrame = tk.Frame(self, bg = '#5ACC72', highlightbackground="#383F38", highlightthickness=2)
        swFrame = tk.Frame(self, bg = '#5ACC72', highlightbackground="#383F38", highlightthickness=2)
        seFrame = tk.Frame(self, bg = '#5ACC72', highlightbackground="#383F38", highlightthickness=2)

        #This button serves to toggle fullscreen mode for the application
        fullScreenButton = tk.Button(bgFrame, text = "fullscreen", command = lambda: root.attributes("-fullscreen", not root.attributes('-fullscreen')))
        #This button serves to provide a convenient way to exit the application
        exitButton = tk.Button(bgFrame, text = 'exit', command = lambda: root.destroy())
        
        mainLabel = tk.Label(self, text = "Aaaaaaand here you go!", bg = '#067625', font = ('Segoe UI', 32, 'bold'), fg = 'white')
        #Button to return to the start page
        returnButton = tk.Button(self, text = 'Return to welcome page', command = lambda: controller.show_frame("StartPage"), bg = '#383F38', fg = "#75F993", font = ('Segoe UI', 12))
        #This button causes a dialog screen to appear for the user to save their generated results to a text file
        exportButton = tk.Button(self, text = 'Export Results', bg = '#383F38', fg = "#75F993", font = ('Segoe UI', 12), command = lambda: mainPageFunctions.exportToFile())
        
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

#Program entry point and main loop         
root = MusicApp()
def main(): 
    root.mainloop()

if __name__ == "__main__": main()
