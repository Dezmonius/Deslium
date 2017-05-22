import tkinter as Tk

class About_Window(object):

	def __init__(self, master):
		top=self.top=Tk.Toplevel(master)
		self.master = master
		top.title("About Us")

    # Info
		self.label = Tk.Label(top, text="Address Book by Karmitsky K.S \n Version 1.0\n Copyright © 2017")
		self.label.grid(row=1, column=0, padx=10, pady=10)