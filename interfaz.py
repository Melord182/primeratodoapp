import tkinter as tk
from tkinter import *
from tkinter import ttk
from manejo_tareas import *
from conexion_db import *
def change_treeview_colors(tree):
    style = ttk.Style()

    # Cambiar el color de fondo del encabezado
    style.configure('Treeview.Heading', background='red', foreground='black', font=('Georgia', 12, 'bold'))

    # Cambiar el color de fondo y texto de las filas
    style.configure('Treeview', background='snow', foreground='black', fieldbackground='lightgray')

    # Cambiar el color de fondo de las filas seleccionadas
    style.map('Treeview', background=[('selected', 'lightblue')])
def to_do_app_executable():
    #definir variables
    global entrada_usuario
    global entrada_nombre_tarea
    global entrada_descripcion
    global tree
    try:
        #Creacion interfaz principal
        
        interfaz = Tk()
        interfaz.title("To do App")
        interfaz.geometry("1270x700+150+50")
        interfaz.resizable(False,False)
        interfaz.config(
            bg='lightskyblue',
            padx=20,
            pady=20
        )
        interfaz.iconbitmap('C:\\Users\\jaime\\Documents\\Mi primera To Do App\\data\\images\\icono.ico')
        #Creacion de la estructura de datos y luego ingresarlos en la cuadrilla
        estructura_ingreso_datos= LabelFrame( interfaz,
            text='To do app',
            font=("Georgia",18),
            bg='lightskyblue',
            fg='blue2',
            padx=5,
            pady=5,
            width=450,
            height=600,
            borderwidth=5,
            relief="ridge",
        )
        estructura_ingreso_datos.grid(row=0,
                                      column=0,
                                      padx=5,
                                      pady=5)

        #Labels y entrys:
        
        #USUARIO
        label_usuario = Label(estructura_ingreso_datos,
                                text="Usuario:",
                                font=("Georgia",15),
                                bg='lightskyblue',
                                padx=5,
                                pady=5,
                                
                                ).grid(row=0,column=0,padx=5,pady=3,sticky="w")
        entrada_usuario = Entry(estructura_ingreso_datos,
                                width=28,
                                bg="snow",
                                font=("Arial",12))
        entrada_usuario.grid(row=0,column=1,padx=5,pady=3,sticky="w")
        
        #NOMBRE TAREA
        label_nombre_tarea = Label(estructura_ingreso_datos,
                                text="Nombre tarea:",
                                font=("Georgia",15),
                                bg='lightskyblue',
                                padx=5,
                                pady=5
                                ).grid(row=1,columnspan=2,padx=5,pady=3,sticky="w")
        
        entrada_nombre_tarea = Entry(estructura_ingreso_datos,
                                width=40,
                                bg="snow",
                                font=("Arial",12))
        entrada_nombre_tarea.grid(row=2,columnspan=2,padx=5,pady=3,sticky="w")
        
        #DESCRIPCION TAREA
        label_descripcion = Label(estructura_ingreso_datos,
                                  text="Descripcion:",
                                  font=("Georgia",15),
                                  bg='lightskyblue',
                                  padx=5,
                                  pady=5).grid(row=3,columnspan=2,padx=5,pady=3,sticky="w")
        
        entrada_descripcion = Text(estructura_ingreso_datos,
                                   width=40,
                                   height=20,
                                   bg="snow",
                                   font=("Arial",12))
        entrada_descripcion.grid(row=4,columnspan=2,padx=5,pady=3,sticky="w")

        #BOTONES
        #GUARDAR
        boton_guardar = Button(estructura_ingreso_datos,
                               text="Guardar",
                               font=("Georgia",12,"bold"),
                               bg="dodgerblue",
                               command=guardar_tarea,
                               ).grid(row=5,column=0,padx=5,pady=5,sticky="w")
        
        #Modificar
        boton_modificar = Button(estructura_ingreso_datos,
                               text="Modificar",
                               font=("Georgia",12,"bold"),
                               bg="dodgerblue",
                               command=modificar_tarea,
                               ).grid(row=5,column=1,padx=5,pady=5,sticky="w")
        
        #ELIMINAR
        boton_eliminar= Button(estructura_ingreso_datos,
                               text="Eliminar",
                               font=("Georgia",12,"bold"),
                               bg="tomato2",
                               command=eliminar_tarea
                               ).grid(row=6,column=0,padx=5,pady=5,sticky="w")
        
        #Creditos APP
        creditos = Label(estructura_ingreso_datos,
                         text="Creado por Jaime Lopez, 2024 v1.0",
                         bg='lightskyblue').grid(row=6,column=1,sticky="w")
    
 
        #Tree
        
        #COLOR
        
        estructura_muestra_datos = LabelFrame(interfaz,text="Lista de tareas",height=300,padx=5,pady=5,font=("Georgia",18),bg='lightskyblue', relief='ridge',borderwidth=5,fg='blue2')
        estructura_muestra_datos.grid(row=0,column=1,padx=5,pady=5)
        tree = ttk.Treeview(estructura_muestra_datos,columns=("idtarea","Usuario","Nombre tarea","Despcripción","fecha"),show='headings',height=30,)
        tree.column("# 1",anchor=CENTER,width=0,stretch=tk.NO)
        tree.heading("# 1", text="N°")
            
        tree.column("# 2",anchor=CENTER,width=100,)
        tree.heading("# 2", text="Usuario")
            
        tree.column("# 3",anchor=CENTER,width=200)
        tree.heading("# 3", text="Nombre Tarea")
        
        tree.column("# 4",anchor=CENTER,width=350)
        tree.heading("# 4", text="Descripción")
            
        tree.column("# 5",anchor=CENTER,width=150)
        tree.heading("# 5", text="Fecha")
        
        for row in Tareas.mostrar_tareas():
            tarea_truncada = row[3].split('\n')[0] if row[3] else""
            row_truncada = (row[0],row[1],row[2],tarea_truncada,row[4])
            tree.insert("","end",values=row_truncada)
        tree.bind("<<TreeviewSelect>>",seleccionar_tarea)
        change_treeview_colors(tree)
        tree.pack(expand=True, fill='both')
        
        
        #Mainloop
        interfaz.mainloop()
        
        
    except ValueError as error:
        print(f"Error al ejecutar programa")
        
#Actualizar pantalla
def actualizar_pantalla():
    global tree
    try: 
        tree.delete(*tree.get_children())
        datos = Tareas.mostrar_tareas()
        for row in Tareas.mostrar_tareas():
            tarea_truncada = row[3].split('\n')[0] if row[3] else""
            row_truncada = (row[0],row[1],row[2],tarea_truncada,row[4])
            tree.insert("","end",values=row_truncada)
    except ValueError as error:
        print(f"Error al actualizar pantalla {error}")
        
#Seleccionar fila de un tree:

def seleccionar_tarea(event):
    global id_seleccionada
    global entrada_descripcion
    global entrada_nombre_tarea
    global entrada_usuario
    try:
        item=tree.focus()
        if item:
            values = tree.item(item)["values"]
            id_seleccionada = values[0]
            entrada_usuario.delete(0,END)
            entrada_usuario.insert(0,values[1])
            
            entrada_nombre_tarea.delete(0,END)
            entrada_nombre_tarea.insert(0,values[2])
            
            tarea_completa = Tareas.obtener_tarea_completa(id_seleccionada)
            entrada_descripcion.delete(1.0, tk.END)
            entrada_descripcion.insert(1.0, tarea_completa)
            
            
    except ValueError as error:
        print(f"Error al selecionar {error}")
        
#GUARDAR TAREAs
def guardar_tarea():
    global entrada_usuario
    global entrada_nombre_tarea
    global entrada_descripcion
    try:
        usuario = entrada_usuario.get()
        nombre_tarea = entrada_nombre_tarea.get()
        descripcion = entrada_descripcion.get(1.0,tk.END)
        Tareas.guardar_tarea(usuario,nombre_tarea,descripcion)
        actualizar_pantalla()   
    except ValueError as error:
        print(f"Error al guardar tarea: {error}")

#Modificar tarea:
def modificar_tarea():
    global entrada_usuario
    global entrada_descripcion
    global entrada_nombre_tarea
    global id_seleccionada
    try:
        usuario = entrada_usuario.get()
        nombre_tarea = entrada_nombre_tarea.get()
        descripcion = entrada_descripcion.get(1.0,tk.END)
        Tareas.modificar_tareas(usuario,nombre_tarea,descripcion,id_seleccionada)
        actualizar_pantalla()
    except ValueError as error:
        print(f"Error al modificar tarea: {error}")
        
#Eliminar tarea
def eliminar_tarea():
    global entrada_descripcion
    global entrada_nombre_tarea
    global entrada_usuario
    global id_seleccionada
    
    try:
        Tareas.eliminar_tareas(id_seleccionada)
        
        entrada_usuario.delete(0,END)
        entrada_nombre_tarea.delete(0,END)
        entrada_descripcion.delete(1.0,END)
        actualizar_pantalla()
        
    except ValueError as error:
        print (f"Error al eliminar tarea {error}")
    
#EJECUTAR PROGRAMA
to_do_app_executable()