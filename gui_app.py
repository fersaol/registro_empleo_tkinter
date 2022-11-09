import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import pandas as pd
from PIL import Image, ImageTk
from pathlib import Path


# ------primero vamos a crear un objeto ventana que va a tener todos los elementos de la interfaz de la app--------
# indica el inicio de nuestra interface
root = tk.Tk()
root.title("Job Tracker")
root.grid_columnconfigure(5)
root.grid_rowconfigure(14)
root.configure(bg="#424242")
root.geometry("390x550")
#-------------------------------------------------------------------------------------------------------------------
# AÑADIMOS EL LOGO A NUESTRA APP:

ruta_logo = Path(os.getcwd()+"/logo_smaller.png")
logo = Image.open(ruta_logo) # insertamos el logo que queremos para nuestra app con PIL
logo = ImageTk.PhotoImage(logo) # convertimos el logo en una imagen para tkinter tk
logo_label = tk.Label(image=logo,bg="#424242") # ahora metemos el logo dentro de un widget label
# pero para que el logo funcione tenemos que añadir la siguiente línea de código que no podemos obviar, aunque parezca que no hace nada:
logo_label.image = logo
logo_label.grid(row=0,column=1) # y ahora posicionamos nuestro logo en la ventana de la app
# ------------------------------------------------------------------------------------------------------------------

# AHORA CREAMOS ALGUNAS INSTRUCCIONES PARA NUESTRA APP:

info_label = tk.Label(root,text="Fill in the form below:", font="Raleway",bg="#424242")# creamos otro widget label para ello
info_label.grid(row=1,column=1) # posicionamos el texto en la fila 1 de la columna 0 y le decimos con
                                                     # columnspan que el texto se expanda por las tres columnas al ser grande

# Campo de entrada 1:
l1=tk.Label(root,text='Date',font=('Raleway', 11,'bold'),bg="#424242")
l1.grid(row=2,column=0)
e1_helptext = tk.StringVar(value = 'DD/MM/AAAA')
e1=tk.Entry(root,textvariable=e1_helptext ,width=25,fg="#BDBDBD",font=('Raleway', 9),bg="#757575")
e1.grid(row=2,column=1)

# Campo de entrada 2:
l2=tk.Label(root,text='Company',font=('Raleway', 11,'bold'),bg="#424242")
l2.grid(row=3,column=0)
e2_helptext = tk.StringVar(value = 'Name of the Company')
e2=tk.Entry(root,textvariable=e2_helptext ,width=25,fg="#BDBDBD",font=('Raleway', 9),bg="#757575")
e2.grid(row=3,column=1)

# Campo de entrada 3:
l3=tk.Label(root,text='Position',font=('Raleway', 11,'bold'),bg="#424242")
l3.grid(row=4,column=0)
e3_helptext = tk.StringVar(value = 'Job Title')
e3=tk.Entry(root,textvariable=e3_helptext ,width=25,fg="#BDBDBD",font=('Raleway', 9),bg="#757575")
e3.grid(row=4,column=1)

# Campo de entrada 4:
l4=tk.Label(root,text='Channel',font=('Raleway', 11,'bold'),bg="#424242")
l4.grid(row=5,column=0)
e4_helptext = tk.StringVar(value = 'How Have you applied for it?')
e4=tk.Entry(root,textvariable=e4_helptext ,width=25,fg="#BDBDBD",font=('Raleway', 9),bg="#757575")
e4.grid(row=5,column=1)

# Campo de entrada 5:
l5=tk.Label(root,text='Python Skill',font=('Raleway', 11,'bold'),bg="#424242")
l5.grid(row=6,column=0)
e5_helptext = tk.StringVar(value = '1 or 0 if True or False')
e5=tk.Entry(root,textvariable=e5_helptext ,width=25,fg="#BDBDBD",font=('Raleway', 9),bg="#757575")
e5.grid(row=6,column=1)

# Campo de entrada 6:
l6=tk.Label(root,text='Excel Skill',font=('Raleway', 11,'bold'),bg="#424242")
l6.grid(row=7,column=0)
e6_helptext = tk.StringVar(value = '1 or 0 if True or False')
e6=tk.Entry(root,textvariable=e6_helptext ,width=25,fg="#BDBDBD",font=('Raleway', 9),bg="#757575")
e6.grid(row=7,column=1)

# Campo de entrada 7:
l7=tk.Label(root,text='SQL Skill',font=('Raleway', 11,'bold'),bg="#424242")
l7.grid(row=8,column=0)
e7_helptext = tk.StringVar(value = '1 or 0 if True or False')
e7=tk.Entry(root,textvariable=e7_helptext ,width=25,fg="#BDBDBD",font=('Raleway', 9),bg="#757575")
e7.grid(row=8,column=1)

# Campo de entrada 8:
l8=tk.Label(root,text='R Skill',font=('Raleway', 11,'bold'),bg="#424242")
l8.grid(row=9,column=0)
e8_helptext = tk.StringVar(value = '1 or 0 if True or False')
e8=tk.Entry(root,textvariable=e8_helptext ,width=25,fg="#BDBDBD",font=('Raleway', 9),bg="#757575")
e8.grid(row=9,column=1)

# Campo de entrada 9:
l9=tk.Label(root,text='Power BI Skill',font=('Raleway', 11,'bold'),bg="#424242")
l9.grid(row=10,column=0)
e9_helptext = tk.StringVar(value = 'True or False if True or False')
e9=tk.Entry(root,textvariable=e9_helptext ,width=25,fg="#BDBDBD",font=('Raleway', 9),bg="#757575")
e9.grid(row=10,column=1)

# Campo de entrada 10:
l10=tk.Label(root,text='Others',font=('Raleway', 11,'bold'),bg="#424242")
l10.grid(row=11,column=0)
e10_helptext = tk.StringVar(value = 'Whatever other information')
e10=tk.Entry(root,textvariable=e10_helptext ,width=25,fg="#BDBDBD",font=('Raleway', 9),bg="#757575")
e10.grid(row=11,column=1)

# Campo de entrada 11:
l11 = tk.Label(root,text="index",font=("Raleway",9),bg="#424242")
l11.place(x=40,y=450)
e11 = tk.Entry(root,width=3,bg="#757575")
e11.place(x=45,y=470)

# CREAMOS LA FUNCIÓN PARA EL BOTÓN DE AÑADIR:
def new_entry():
    try:
        file = pd.read_pickle(os.getcwd()+"\\data\\my_job_search_db.pkl")
        file.loc[len(file)] = [e1.get(),str(e2.get()).lower(),str(e3.get()).lower(),
                                str(e4.get()).lower(),str(e5.get()),str(e6.get()),
                                str(e7.get()),str(e8.get()),str(
                                    e9.get()),
                                str(e10.get()).lower()]
        file.to_pickle(os.getcwd()+"\\data\\my_job_search_db.pkl")
        messagebox.showinfo(message=' data added correctly',title ='Info')
    except:
        messagebox.showwarning(message='check the data again',title ='Despistao')

# PONEMOS UN BOTÓN PARA AÑADIR LOS DATOS AL DATAFRAME:

add_button = tk.Button(root,text="Add Data",activebackground="#067B26",
                        activeforeground="#20BEBE",command=new_entry,font="Raleway",bg="#20BEBE",
                        fg="black",height=2,width=15,cursor="heart")
add_button.grid(row=12,column=1)# ahora metemos nuestro botón dentro del grid de la aplicación

# CREAMOS Y PONEMOS UN BOTÓN PARA BORRAR EL ÚLTIMO REGISTRO INTRODUCIDO EN CASO DE ERROR:
def remove_entry():
    try:
        file = pd.read_pickle(os.getcwd()+"\\data\\my_job_search_db.pkl")
        if e11.get():
            row = int(e11.get())
            file = file.drop(index=row)
        else:
            row = len(file)-1
            file = file.drop(index=row)
        file.to_pickle(os.getcwd()+"\\data\\my_job_search_db.pkl")
        messagebox.showinfo(message=f'{row} row deleted',title = 'Info')
    except KeyError as e:
        messagebox.showwarning(message=f'{e}',title = 'Info')

delete_button = tk.Button(root,text="Delete",command=remove_entry, cursor="pirate",
                            font="Raleway",bg="#CE2A36",fg="black",height=2,
                            width=7,activebackground="#700C12",activeforeground="#F22E39")
delete_button.place(x=113,y=450)

# FUNCIÓN PARA MOSTRAR EL DATAFRAME:
def show_data(data=None): 
    window = tk.Tk()
    window.geometry("1000x400")
    window.configure(bg="#424242")
    window.pack_propagate(False)
    window.resizable(width=0,height=0)

    # First we create the container where we are going to place the widget that contains the data
    text_frame = tk.LabelFrame(window,text="DataFrame Data",bg="#424242",fg="white")
    # we set the dimmensions and the place inside the window
    text_frame.place(width=990,height=240,x=5,y=0)

    # with the tree view we tell tkinter how to visualize the file
    tv = ttk.Treeview(text_frame)
    tv.place(relheight=1,relwidth=1) # this relative measures tells tkinter to fill all the space in the frame with the view

    # Now we create the scrollbars to our tree view:

    treescrolly = tk.Scrollbar(text_frame,orient="vertical",command=tv.yview,bg="#424242")
    treescrollx = tk.Scrollbar(text_frame,orient="horizontal",command=tv.xview,bg="#424242")

    # as they are created we added them to the tree view:
    tv.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)

    # then we pack the scrollbars into the container configuring the place and the with
    treescrolly.pack(side="right",fill="y")
    treescrollx.pack(side="bottom",fill="x")

    # cargamos el dataframe

    df = pd.read_pickle(os.getcwd()+"\\data\\my_job_search_db.pkl")
    df = df.reset_index(drop=True)

    def clear_data():
        tv.delete(*tv.get_children())
        
    clear_data()
    
    # creamos el header de nuestro tree view
    tv["columns"] = list(df.columns)
    tv["show"] = "headings"
    for column in tv["columns"]:
        tv.heading(column,text=column)

    # convertimos las filas del dataframe listas, y luego las añadimos a la vista
    rows = df.values.tolist()
    for row in rows:
        tv.insert("","end",values=row)

    filter_frame = tk.LabelFrame(window,text="Opciones de Filtrado",bg="#424242",fg="white")
    filter_frame.place(x=290,y=245,width=705,height=150)

    # creamos las opciones:
    options = ["date","company","channel","position","python","R","Excel","PowerBI","SQL"]

    # creamos el primer dropmenu:
    name_filter1 = tk.StringVar(filter_frame,value="Filter 1")
    filter1 = tk.OptionMenu(filter_frame,name_filter1,*options)
    filter1.configure(width=14)
    filter1.place(x=50,y=40)

# metemos la primera entrada de valor:
    v1_helptext = tk.StringVar(filter_frame,value="Enter a Value")
    value1=tk.Entry(filter_frame,textvariable=v1_helptext ,width=18,fg="#BDBDBD",font=('Raleway', 9),bg="#757575")
    value1.place(x=50,y=77)
# creamos el segundo dropmenu:
    name_filter2 = tk.StringVar(filter_frame,value="Filter 2")
    filter2 = tk.OptionMenu(filter_frame,name_filter2,*options)
    filter2.configure(width=14)
    filter2.place(x=220,y=40)

# metemos la segunda entrada de valor:
    v2_helptext = tk.StringVar(filter_frame,value="Enter a Value")
    value2=tk.Entry(filter_frame,textvariable=v2_helptext ,width=18,fg="#BDBDBD",font=('Raleway', 9),bg="#757575")
    value2.place(x=220,y=77)

# creamos el tercer dropmenu:
    name_filter3 = tk.StringVar(filter_frame,value="Filter 3")
    filter3 = tk.OptionMenu(filter_frame,name_filter3,*options)
    filter3.configure(width=14)
    filter3.place(x=390,y=40)

# metemos la tercera entrada de valor:
    v3_helptext = tk.StringVar(filter_frame,value="Enter a Value")
    value3=tk.Entry(filter_frame,textvariable=v3_helptext ,width=18,fg="#BDBDBD",font=('Raleway', 9),bg="#757575")
    value3.place(x=390,y=77)

# creamos la función para el filtrado del dataframe:
    def filtrado():
        features = [name_filter1.get(),name_filter2.get(),name_filter3.get()]
        values = [value1.get(),value2.get(),value3.get()]
        filtros = dict(zip(features,values))
        not_allowed = ["Enter a Value",""]

        def comprobacion():
            while not_allowed[0] in filtros.values() or not_allowed[1] in filtros.values():
                try:
                    if not_allowed[0] in filtros.values():
                        del filtros[[i[0] for i in filtros.items() if not_allowed[0] in i][0]]
                    else:
                        del filtros[[i[0] for i in filtros.items() if not_allowed[1] in i][0]]
                except:
                    continue
            return filtros

        new_dic = comprobacion()
        tipo_filtro = list(new_dic.keys())
        valores_filtro = list(new_dic.values())
        numero_filtros = len(tipo_filtro)

        if numero_filtros == 1:
            new_df = df[(df[tipo_filtro[0]]==valores_filtro[0])]
        elif numero_filtros == 2:
            new_df = df[(df[tipo_filtro[0]]==valores_filtro[0]) & \
                    (df[tipo_filtro[1]]==valores_filtro[1]) ]
        else:
            new_df = df[(df[tipo_filtro[0]]==valores_filtro[0]) & \
                    (df[tipo_filtro[1]]==valores_filtro[1]) & \
                    (df[tipo_filtro[2]]==valores_filtro[2])]
        new_df = new_df.reset_index(drop=True)

        def ventana_filtrada(data):
            window = tk.Tk()
            window.geometry("1000x250")
            window.configure(bg="#424242")
            window.pack_propagate(False)
            window.resizable(width=0,height=0)

            # First we create the container where we are going to place the widget that contains the data
            text_frame = tk.LabelFrame(window,text="DataFrame Filtered",bg="#424242",fg="white")
            # we set the dimmensions and the place inside the window
            text_frame.place(width=990,height=240,x=5,y=0)

            # with the tree view we tell tkinter how to visualize the file
            tv = ttk.Treeview(text_frame)
            tv.place(relheight=1,relwidth=1) # this relative measures tells tkinter to fill all the space in the frame with the view

            # Now we create the scrollbars to our tree view:

            treescrolly = tk.Scrollbar(text_frame,orient="vertical",command=tv.yview,bg="#424242")
            treescrollx = tk.Scrollbar(text_frame,orient="horizontal",command=tv.xview,bg="#424242")

            # as they are created we added them to the tree view:
            tv.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)

            # then we pack the scrollbars into the container configuring the place and the with
            treescrolly.pack(side="right",fill="y")
            treescrollx.pack(side="bottom",fill="x")

            # cargamos el dataframe
            df = data

            def clear_data():
                tv.delete(*tv.get_children())
                
            clear_data()
            
            # creamos el header de nuestro tree view
            tv["columns"] = list(df.columns)
            tv["show"] = "headings"
            for column in tv["columns"]:
                tv.heading(column,text=column)

            # convertimos las filas del dataframe listas, y luego las añadimos a la vista
            rows = df.values.tolist()
            for row in rows:
                tv.insert("","end",values=row)

        return ventana_filtrada(new_df)
        

# creamos el botón para el filtrado:
    filter_button = tk.Button(filter_frame,text="Filter",activebackground="#067B26",
                        activeforeground="#20BEBE",command=filtrado,font="Raleway",bg="#20BEBE",
                        fg="black",height=2,width=15,cursor="heart")
    filter_button.place(x=525,y=65)

    window.mainloop()
# BOTÓN PARA LLAMAR A LA FUNCIÓN QUE MUESTRA EL DATAFRAME:
show_button = tk.Button(root,text="Show",command=show_data, cursor="sizing",
                            font="Raleway",bg="#432EF2",fg="white",height=2,
                            width=7,activebackground="#160687",activeforeground="#9281F6")
show_button.place(x=200,y=450)

# AHORA VAMOS A AÑADIR UN POCO DE ESPACIO POR DEBAJO DEL BOTÓN:

# canvas = tk.Canvas(root,width=100,height=100,bg="darkgrey",border=None) # Simplemente copiamos canvas, eliminamos rowspan y reducimos la altura
# canvas.grid(row=13,column=5)

root.mainloop() # indica el final de nuestra interface