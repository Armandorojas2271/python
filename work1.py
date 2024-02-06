from tkinter import *
from tkinter import messagebox

class Ventana:
    def __init__(self):
        self.ventana = Tk()
        self.dato_campo = StringVar()
        self.ventana.geometry("550x200+100+100")
        self.ventana.title("Cargar Localidades")
        Label(self.ventana, text="Localidad").grid(pady=10, row=0, column=0)
        self.nombre_localidad = Entry(self.ventana, textvariable=self.dato_campo, width=50)
        self.nombre_localidad.grid(padx=10, row=0, column=1)
        Button(self.ventana, text='Guardar', width=10, command=self.cargar_lista).grid(pady=10, row=0, column=2)
        Label(self.ventana, text="Lista de localidades").grid(pady=10, row=1, column=0)
        self.lista_frame = Frame(self.ventana)
        self.lista_frame.grid(row=1, column=1)
        self.lista_localidades = []

    def mostrar(self):
        self.ventana.mainloop()

    def cargar_lista(self):
        localidad = self.dato_campo.get().strip()  # Eliminar espacios en blanco al principio y al final
        if localidad:  # Verificar si la localidad no está vacía
            self.lista_localidades.append(localidad)
            self.actualizar_tabla()
        else:
            messagebox.showwarning("Campo vacío", "Por favor ingrese una localidad válida.")
            self.nombre_localidad.delete(0, 'end')  # Limpiar el campo de entrada

    def actualizar_tabla(self):
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

        if self.lista_localidades:
            for i, localidad in enumerate(self.lista_localidades, start=1):
                Label(self.lista_frame, text=localidad).grid(row=i, column=0)
        else:
            Label(self.lista_frame, text="Ninguna localidad ingresada").grid(row=0, column=0)

if __name__ == "__main__":
    ventana_localidad = Ventana()
    ventana_localidad.mostrar()
