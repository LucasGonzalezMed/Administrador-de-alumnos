
from tkinter import *
from Login import *


if __name__ == "__main__":
	ventana = Tk()
	ventana.config(bg='White')
	ventana.geometry('350x500+500+50')
	ventana.wm_title("Alumnos DOJO GONZALEZ")
	#ventana.overrideredirect(1)
	ventana.resizable(0,0)
	app = Login(ventana)
	app.mainloop()
