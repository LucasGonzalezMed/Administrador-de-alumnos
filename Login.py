from tkinter import *
import time
import CRUD
import Alumno
from CRUD import *


class Login(Frame):
        
	Alumnos = Alumnos()
	def __init__(self, master, *args):
		super().__init__( master,*args)
		self.user_marcar = "Ingrese su usuario"
		self.contra_marcar = "Ingrese su contraseña"
		self.fila1  = ''
		self.fila2 = ''
		self.widgets()
	def entry_out(self, event, event_text):
		if event['fg'] == 'black' and len(event.get()) ==0:
			event.delete(0, END)
			event['fg'] = 'grey'
			event.insert(0, event_text)
		if self.entry2.get() != 'Ingrese su contraseña':
			self.entry2['show'] =""
		if self.entry2.get() != 'Ingrese su usuario':
			self.entry2['show'] ="*"
	def entry_in(self, event):		
	    if event['fg'] == 'grey':
	        event['fg'] = 'black'
	        event.delete(0, END)
           	
	    if self.entry2.get() != 'Ingrese su contraseña':
	    	self.entry2['show'] = "*"

	    if self.entry2.get() == 'Ingrese su contraseña':
	    	self.entry2['show'] = ""

	def salir(self):
		self.master.destroy()
		self.master.quit()

	def acceder_ventana_dos(self):
		for i in  range(101):
			self.barra['value'] +=1
			self.master.update()
			time.sleep(0.02)

		self.master.withdraw()
		self.ventana2 = CRUD.main()
                
		

	def verificacion_users(self):
		self.indica1['text'] = ''
		self.indica2['text'] = ''		
		users_entry = self.entry1.get()
		password_entry = self.entry2.get()

		if users_entry!= self.user_marcar or self.contra_marcar != password_entry:
			users_entry = str("'" + users_entry + "'")
			password_entry = str("'" + password_entry + "'")

			dato1 = self.Alumnos.busca_users(users_entry)
			dato2 = self.Alumnos.busca_password(password_entry)

			self.fila1 = dato1
			self.fila2 = dato2 

			if self.fila1 == self.fila2:	
				if dato1 == [] and dato2 ==[]:
					self.indica2['text'] = 'Contraseña incorrecta'
					self.indica1['text'] = 'Usuario incorrecto'
				else:

					if dato1 ==[]:
						self.indica1['text'] = 'Usuario incorrecto'
					else:
						dato1 = dato1[0][1]

					if dato2 ==[]:
						self.indica2['text'] = 'Contraseña incorrecta'
					else:
						dato2 = dato2[0][2]

					if dato1 != [] and dato2 != []:
						self.acceder_ventana_dos()
			else:
				self.indica1['text'] = 'Usuario incorrecto'
				self.indica2['text'] = 'Contraseña incorrecta'

	def widgets(self):
		self.logo = PhotoImage(file ='logo.png')
		Label(self.master, image= self.logo, bg='White',height=150, width=150).pack()
		Label(self.master, text= 'Usuario', bg='White', fg= 'black', font= ('Lucida Sans', 16, 'bold')).pack(pady=5)
		self.entry1 = Entry(self.master, font=('Comic Sans MS', 12),justify = 'center', fg='grey',highlightbackground = "#E65561", 
			highlightcolor= "green2", highlightthickness=5)
		self.entry1.insert(0, self.user_marcar)
		self.entry1.bind("<FocusIn>", lambda args: self.entry_in(self.entry1))
		self.entry1.bind("<FocusOut>", lambda args: self.entry_out(self.entry1, self.user_marcar))
		self.entry1.pack(pady=4)   

		self.indica1 = Label(self.master, bg='White', fg= 'black', font= ('Arial', 8, 'bold'))
		self.indica1.pack(pady=2)                             

		# contraseña y entry
		Label(self.master, text= 'Contraseña', bg='White', fg= 'black', font= ('Lucida Sans', 16, 'bold')).pack(pady=5)
		self.entry2 = Entry(self.master,font=('Comic Sans MS', 12),justify = 'center',  fg='grey',highlightbackground = "#E65561", 
			highlightcolor= "green2", highlightthickness=5)
		self.entry2.insert(0, self.contra_marcar)
		self.entry2.bind("<FocusIn>", lambda args: self.entry_in(self.entry2))
		self.entry2.bind("<FocusOut>", lambda args: self.entry_out(self.entry2, self.contra_marcar))
		self.entry2.pack(pady=4)
		self.indica2 = Label(self.master, bg='White', fg= 'black', font= ('Arial', 8, 'bold'))
		self.indica2.pack(pady=2)
		Button(self.master, text= 'Iniciar Sesion',  command = self.verificacion_users,activebackground='magenta', bg='#D64E40', font=('Arial', 12,'bold')).pack(pady=10)
		estilo = ttk.Style()
		estilo.theme_use('clam')
		estilo.configure("TProgressbar", foreground='red', background='black',troughcolor='White',
																bordercolor='#970BD9',lightcolor='#970BD9', darkcolor='black')
		self.barra = ttk.Progressbar(self.master, orient= HORIZONTAL, length=200, mode='determinate', maximum=100, style="TProgressbar")
		self.barra.pack()
		Button(self.master, text= 'Salir', bg='White',activebackground='White', bd=0, fg = 'black', font=('Lucida Sans', 15,'italic'),command= self.salir).pack(pady=10)


