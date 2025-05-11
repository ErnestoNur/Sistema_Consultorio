import tkinter as tk


def iniciar_aplicacion():
    # Crear la ventana principal
    aplicacion = tk.Tk()

    # Configuración de la ventana principal
    aplicacion.geometry("800x600")
    aplicacion.resizable(False, False)
    aplicacion.config(bg="black")
    # Título de la ventana
    aplicacion.title("Sistema de Gestión de Pacientes")
    # Icono de la ventana
    # aplicacion.iconbitmap("icono.ico")  # Reemplaza con la ruta de tu icono
    # Color de fondo
    aplicacion.config(bg="#f0f0f0")

    # Lanzar el bucle principal
    aplicacion.mainloop()


# Punto de entrada principal del programa
if __name__ == "__main__":
    iniciar_aplicacion()