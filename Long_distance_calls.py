import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        self.mainwindow = tkinter.Tk()
        self.topframe = tkinter.Frame(self.mainwindow)
        self.bottomframe = tkinter.Frame(self.mainwindow)
        self.radiovar = tkinter.IntVar()
        self.radiovar.set(1)
        self.rb1 = tkinter.Radiobutton(self.topframe,
                                       text='Daytime(6:00 A.M. through 5:59 P.M.)',variable=self.radiovar,value=1)
        self.rb2 = tkinter.Radiobutton(self.topframe,
                                       text='Evening (6:00 P.M.  through 11:59 P.M.)',variable=self.radiovar,value=2)
        self.rb3 = tkinter.Radiobutton(self.topframe,
                                       text='Off-Peak (midnight through 5:59 P.M.)',variable=self.radiovar,value=3)
        self.min=tkinter.Entry(self.bottomframe)
        self.mlabel=tkinter.Label(self.bottomframe,text='Minutes called: ')
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.mlabel.pack(side='left')
        self.min.pack(side='right')
        self.ok_button = tkinter.Button(self.mainwindow,
                                        text='Ok', command=self.show_choice)
        self.quit_button = tkinter.Button(self.mainwindow,
                                          text='Quit', command=self.mainwindow.destroy)
        self.topframe.pack(pady=10)
        self.bottomframe.pack(pady=10)
        self.ok_button.pack(padx=5)
        self.quit_button.pack(padx=5)
        tkinter.mainloop()
    def show_choice(self):
        rate=0
        if self.radiovar.get()== 1:
            rate=0.02
        if self.radiovar.get()==2:
            rate=0.12
        if self.radiovar.get()==3:
            rate=0.05
        total = (rate*float(self.min.get()))
        tkinter.messagebox.showinfo('Total owed','you owe $'+str(total))
if __name__ == '__main__':
    gui=GUI()
