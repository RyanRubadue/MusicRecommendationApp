from tkinter import *
from tkinter import ttk


class Feedback:

    def __init__(self, master):
        
        master.title('Music Recommendation App')
        master.configure(background = '#3BAD40')
        #master.attributes('-fullscreen', True)
        
        nwFrame = Frame(master, bg = '#5ACC72', highlightbackground="#383F38", highlightthickness=2)
        neFrame = Frame(master, bg = '#5ACC72', highlightbackground="#383F38", highlightthickness=2)
        swFrame = Frame(master, bg = '#5ACC72', highlightbackground="#383F38", highlightthickness=2)
        seFrame = Frame(master, bg = '#5ACC72', highlightbackground="#383F38", highlightthickness=2)
        
        mainLabel = Label(master, text = "Aaaaaaand here you go!", bg = '#3BAD40', font = ('Segoe UI', 32, 'bold'), fg = 'white')
        returnButton = Button(master, text = 'Return to welcome page')
        exportButton = Button(master, text = 'Export Results')
        
        nwLabel = Label(nwFrame, text = "Your Top Genres", bg = "#383F38", fg = "#75F993", font = ('Segoe UI', 16))
        neLabel = Label(neFrame, text = "Your Top Artists", bg = "#383F38", fg = "#75F993", font = ('Segoe UI', 16))
        swLabel = Label(swFrame, text = "Recommended Songs", bg = "#383F38", fg = "#75F993", font = ('Segoe UI', 16))
        seLabel = Label(seFrame, text = "Recommended Artists", bg = "#383F38", fg = "#75F993", font = ('Segoe UI', 16))

        nwLabel.grid(row = 0, column = 0, columnspan = 3)
        neLabel.grid(row = 0, column = 0, columnspan = 3)
        swLabel.grid(row = 0, column = 0, columnspan = 3)
        seLabel.grid(row = 0, column = 0, columnspan = 3)

        nwFrame.place(relx = .05, rely = .1, relheight = .4, relwidth = .44)
        neFrame.place(relx = .51, rely = .1, relheight = .4, relwidth = .44)
        swFrame.place(relx = .05, rely = .55, relheight = .4, relwidth = .44)
        seFrame.place(relx = .51, rely = .55, relheight = .4, relwidth = .44)
        mainLabel.place(relx = .35, rely = .02, relheight = .07, relwidth = .3)
        returnButton.place(relx = .735, rely = .03, relheight = .05, relwidth = .1)
        exportButton.place(relx = .85, rely = .03, relheight = .05, relwidth = .1)


def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == "__main__": main()
