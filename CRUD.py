from tkinter import *
from tkinter import ttk
from Alumno import *
from tkinter import messagebox


class CRUD(Frame, object):
    
    Alumnos = Alumnos()
    
        
    def __init__(self, master=None):
        super().__init__(master,width=680, height=260)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenaDatos()
        self.habilitarCajas("disabled")  
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")  
        self.id=-1      
                   
    def habilitarCajas(self,estado):
        self.txtnombre.configure(state=estado)
        self.txtapellido.configure(state=estado)
        self.txtedad.configure(state=estado)
        self.txtcategoria.configure(state=estado)
        
    def habilitarBtnOper(self,estado):
        self.btnNuevo.configure(state=estado)                
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)
        
    def habilitarBtnGuardar(self,estado):
        self.btnGuardar.configure(state=estado)                
        self.btnCancelar.configure(state=estado)                
        
    def limpiarCajas(self):
        self.txtedad.delete(0,END)
        self.txtcategoria.delete(0,END)
        self.txtnombre.delete(0,END)
        self.txtapellido.delete(0,END)
        
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
                
    def llenaDatos(self):
        datos = self.Alumnos.consulta_alumno()        
        for row in datos:            
            self.grid.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4]))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set( self.grid.get_children()[0] )
            
    def fNuevo(self):         
        self.habilitarCajas("normal")  
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()        
        self.txtnombre.focus()
    
    def fGuardar(self): 
        if self.id ==-1:       
            self.Alumnos.inserta_alumno(self.txtnombre.get(),self.txtapellido.get(),self.txtedad.get(),self.txtcategoria.get())            
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.Alumnos.modifica_alumno(self.id,self.txtnombre.get(),self.txtapellido.get(),self.txtedad.get(),self.txtcategoria.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1            
        self.limpiaGrid()
        self.llenaDatos() 
        self.limpiarCajas() 
        self.habilitarBtnGuardar("disabled")      
        self.habilitarBtnOper("normal")
        self.habilitarCajas("disabled")
                    
    def fModificar(self):        
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id= clave  
            self.habilitarCajas("normal")                         
            valores = self.grid.item(selected,'values')
            self.limpiarCajas()            
            self.txtnombre.insert(0,valores[0])
            self.txtapellido.insert(0,valores[1])
            self.txtedad.insert(0,valores[2])
            self.txtcategoria.insert(0,valores[3])            
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")
            self.txtnombre.focus()
                                        
    def fEliminar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid.item(selected,'values')
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if r == messagebox.YES:
                n = self.Alumnos.elimina_alumno(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatos()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')
                            
    def fCancelar(self):
        r = messagebox.askquestion("Calcelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajas() 
            self.habilitarBtnGuardar("disabled")      
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disabled")

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0,width=93, height=259)        
        self.btnNuevo=Button(frame1,text="Nuevo", command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5,y=50,width=80, height=30 )        
        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=5,y=90,width=80, height=30)                
        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5,y=130,width=80, height=30)        
        frame2 = Frame(self,bg="#d3dde3" )
        frame2.place(x=95,y=0,width=150, height=259)                        
        lbl1 = Label(frame2,text="Nombre: ")
        lbl1.place(x=3,y=5)        
        #self.txtISO3=Entry(frame2,textvariable = self.ISO3)
        self.txtnombre=Entry(frame2)
        self.txtnombre.place(x=3,y=25,width=50, height=20)                
        lbl2 = Label(frame2,text="Apellido: ")
        lbl2.place(x=3,y=55)        
        self.txtapellido=Entry(frame2)
        self.txtapellido.place(x=3,y=75,width=100, height=20)        
        lbl3 = Label(frame2,text="Edad: ")
        lbl3.place(x=3,y=105)        
        self.txtedad=Entry(frame2)
        self.txtedad.place(x=3,y=125,width=100, height=20)        
        lbl4 = Label(frame2,text="Categoria: ")
        lbl4.place(x=3,y=155)        
        self.txtcategoria=Entry(frame2)
        self.txtcategoria.place(x=3,y=175,width=50, height=20)        
        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=10,y=210,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80,y=210,width=60, height=30)         
        frame3 = Frame(self,bg="yellow" )
        frame3.place(x=247,y=0,width=420, height=259)                      
        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4"))        
        self.grid.column("#0",width=60)
        self.grid.column("col1",width=70, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)        
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Apellido", anchor=CENTER)
        self.grid.heading("col3", text="Edad", anchor=CENTER)
        self.grid.heading("col4", text="Categoria", anchor=CENTER)                
        self.grid.pack(side=LEFT,fill = Y)        
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode']='browse'        
    def main():
        root = Tk()
        root.wm_title("Alumnos DOJO GONZALEZ")
        app = CRUD(root) 
        app.mainloop()
