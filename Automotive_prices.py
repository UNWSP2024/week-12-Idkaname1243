import tkinter
import tkinter.messagebox

class Gui:
    def __init__(self):
        self.mainwindow = tkinter.Tk()
        self.mainwindow.title('Automotive Prices')
        self.top_frame = tkinter.Frame(self.mainwindow)
        self.bottom_frame = tkinter.Frame(self.mainwindow)
        self.oil_var = tkinter.IntVar()
        self.lube_var = tkinter.IntVar()
        self.radiator_var = tkinter.IntVar()
        self.transmission_var = tkinter.IntVar()
        self.inspection_var = tkinter.IntVar()
        self.muffler_var = tkinter.IntVar()
        self.tire_var = tkinter.IntVar()
        self.oil = tkinter.Checkbutton(self.top_frame, text='Oil Change - $30.00', onvalue=30, offvalue=0, variable=self.oil_var)
        self.lube = tkinter.Checkbutton(self.top_frame, text='Lube Job - $20.00', onvalue=20, offvalue=0, variable=self.lube_var)
        self.radiator = tkinter.Checkbutton(self.top_frame, text='Radiator Flush - $40.00', onvalue=40, offvalue=0, variable=self.radiator_var)
        self.transmission = tkinter.Checkbutton(self.top_frame, text='Transmission Fluid - $100.00', onvalue=100, offvalue=0, variable=self.transmission_var)
        self.inspection = tkinter.Checkbutton(self.top_frame, text='Inspection - $35.00', onvalue=35, offvalue=0, variable=self.inspection_var)
        self.muffler = tkinter.Checkbutton(self.top_frame, text='Muffler Replacement - $200.00', onvalue=200, offvalue=0, variable=self.muffler_var)
        self.tire = tkinter.Checkbutton(self.top_frame, text='Tire Rotation - $20.00', onvalue=20, offvalue=0, variable=self.tire_var)
        self.okbutton = tkinter.Button(self.bottom_frame, text='Calculate Total', command=self.finish)
        self.exit_button = tkinter.Button(self.bottom_frame, text='Exit', command=self.mainwindow.destroy)
        self.oil.pack(anchor='w')
        self.lube.pack(anchor='w')
        self.radiator.pack(anchor='w')
        self.transmission.pack(anchor='w')
        self.inspection.pack(anchor='w')
        self.muffler.pack(anchor='w')
        self.tire.pack(anchor='w')
        self.top_frame.pack(pady=10)
        self.bottom_frame.pack(pady=10)
        self.okbutton.pack(side='left', padx=5)
        self.exit_button.pack(side='right', padx=5)
        tkinter.mainloop()
    def finish(self):
        total = (
            self.oil_var.get() +
            self.lube_var.get() +
            self.radiator_var.get() +
            self.transmission_var.get() +
            self.inspection_var.get() +
            self.muffler_var.get() +
            self.tire_var.get()
        )
        tkinter.messagebox.showinfo('Total Cost', f'Your total is ${total:.2f}')
if __name__ == '__main__':
    gui = Gui()
