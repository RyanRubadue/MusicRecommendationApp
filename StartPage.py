from tkinter import *
from tkinter import ttk


class mainPageFunctions:
    def unlockSongs(entry, var):
        if var.get() == 0:
            entry.configure(state='disabled')
        else:
            entry.configure(state='normal')


class IntEntry(Entry):
    def __init__(self, master=None, **kwargs):
        self.var = StringVar()
        Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ''
        self.var.trace('w', self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        print(self.get())
        if self.get().isdigit() and int(self.get()) < 11: 
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this 
            self.set(self.old_value)


class Feedback:

    def __init__(self, master):
        
        #Configuration of master window
        master.title('Music Recommendation App')
        master.configure(background = '#3BAD40')

        
        #Variable Defintions
        checkVar3 = IntVar() #Variable of whether show recommended songs is checked
        checkVar4 = IntVar() #Variable of whether show recommended artists is checked
        
        
        leftFrame = Frame(master, bg = '#5ACC72', highlightbackground="#4F8451", highlightthickness=2)
        rightFrame = Frame(master, bg = '#5ACC72', highlightbackground="white", highlightthickness=2)
        
        topFrame = Frame(leftFrame, bg = '#5ACC72')
        bottomFrame = Frame(leftFrame, bg = '#52F059', highlightbackground="#4F8451", highlightthickness=2)

        
        titleLabel = Label(topFrame, text = "A New Way to Discover Music",
                           fg ="#fcd8e9", font = ('Gadugi', 25, 'italic', 'bold'),
                           pady = 45, padx = 25, bg = '#5ACC72')
        titleLabel.grid(column = 0, row = 0, columnspan = 2, rowspan = 2, sticky = 'nw')

        
        enterTextLabel = Label(topFrame, text = "Enter Spotify Username:",
                               font = ('Segoe UI', 16, 'bold'), bg = '#5ACC72')
        enterTextLabel.grid(row = 2, column = 0)

        usernameEntry = Entry(topFrame, bg = 'white', fg = '#5ACC72', font =('Segoe UI', 14), width = 22)
        usernameEntry.grid(row = 2, column = 1, sticky = 'w', pady = 5)

        self.musicNoteImage = PhotoImage(file = 'musicNoteImage.png').subsample(2, 2)
        musicLabel = Label(topFrame, image = self.musicNoteImage, bg = '#5ACC72')
        musicLabel.grid(row = 0, column = 3, rowspan = 4, pady = (10, 0), padx = 10)

        validUsernameText = Label(topFrame, text = "Invalid Username!", fg = 'red', bg = '#5ACC72' )
        validUsernameText.grid(row = 3, column = 1, sticky = 'n', padx = (0, 45))

        topFrame.grid(row = 0, column = 0)

        numSongsEntry = IntEntry(bottomFrame, bg = '#E9F0EA', fg = 'black', state = DISABLED, width = 4)
        numSongsLabel = Label(bottomFrame, text = "= Number of Recommended Songs (1-10)", bg = "#52F059")
        numArtistsEntry = IntEntry(bottomFrame, bg = '#E9F0EA', fg = 'black', state = DISABLED, width = 4)
        numArtistsLabel = Label(bottomFrame, text = "= Number of Recommended Artists (1-10)", bg = "#52F059")

        toDisplayCheckButton1 = Checkbutton( bottomFrame, text = "Show Top Genres", bg = "#52F059")
        toDisplayCheckButton2 = Checkbutton( bottomFrame, text = "Show Top Artists", bg = "#52F059")
        toDisplayCheckButton3 = Checkbutton( bottomFrame, text = "Show Recommended Songs", bg = "#52F059", variable = checkVar3, command =lambda e=numSongsEntry: mainPageFunctions.unlockSongs(e, checkVar3))
        toDisplayCheckButton4 = Checkbutton( bottomFrame, text = "Show Recommended Artists", bg = "#52F059", variable = checkVar4, command =lambda e=numArtistsEntry: mainPageFunctions.unlockSongs(e, checkVar4))

        startButton = Button(bottomFrame, text = "Get Your Music!", font = ('Segoi UI', 24, 'bold'),
                             fg = 'white', bg = '#3BAD40', relief = RIDGE, activeforeground = '#5ACC72')

        
        toDisplayCheckButton1.grid(row = 0, column = 0, sticky = 'w', padx = 15, pady = (20, 0), columnspan = 2)
        toDisplayCheckButton2.grid(row = 1, column = 0, sticky = 'w', padx = 15, columnspan = 2)
        toDisplayCheckButton3.grid(row = 2, column = 0, sticky = 'w', padx = 15, columnspan = 2)
        toDisplayCheckButton4.grid(row = 4, column = 0, sticky = 'w', padx = 15, columnspan = 2)
        
        numSongsEntry.grid(row = 3, column = 0, padx = (50,0))
        numSongsLabel.grid(row = 3, column = 1, padx = 0, sticky = 'w')
        numArtistsEntry.grid(row = 5, column = 0, padx = (50,0))
        numArtistsLabel.grid(row = 5, column = 1, padx = 0, sticky = 'w')

        startButton.grid(row = 1, column = 2, rowspan = 5, sticky = 'w', padx = (80, 0))

        bottomFrame.grid(row = 1, column =0, sticky = 'w', pady  = (20, 30), ipadx = 30, ipady = 30, padx = 20)

        leftFrame.pack(padx = 20, pady = 20)

def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()


if __name__ == "__main__": main()

