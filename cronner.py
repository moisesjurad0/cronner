import tkinter as tk
from tkinter import ttk
import time
from plyer import notification

class CronometroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronómetro")
        
        self.tiempo_total = tk.StringVar()
        self.cantidad_cortes = tk.StringVar()
        self.tipo_configuracion = tk.StringVar()
        self.tipo_configuracion.set("Cantidad de Cortes")
        
        self.inicializar_interfaz()
        
    def inicializar_interfaz(self):
        # Etiqueta y entrada para configurar el tiempo total
        ttk.Label(self.root, text="Tiempo Total (segundos):").grid(row=0, column=0)
        ttk.Entry(self.root, textvariable=self.tiempo_total).grid(row=0, column=1)
        
        # Etiqueta y entrada para configurar la cantidad de cortes
        ttk.Label(self.root, text="Cantidad de Cortes:").grid(row=1, column=0)
        ttk.Entry(self.root, textvariable=self.cantidad_cortes).grid(row=1, column=1)
        
        # RadioButtons para seleccionar el tipo de configuración
        ttk.Radiobutton(self.root, text="Cantidad de Cortes", variable=self.tipo_configuracion, value="Cantidad de Cortes").grid(row=2, column=0)
        ttk.Radiobutton(self.root, text="Segundos entre Cortes", variable=self.tipo_configuracion, value="Segundos entre Cortes").grid(row=2, column=1)
        
        # Botón para iniciar el cronómetro
        ttk.Button(self.root, text="Iniciar", command=self.iniciar_cronometro).grid(row=3, columnspan=2)
        
    def iniciar_cronometro(self):
        tiempo_total = int(self.tiempo_total.get())
        cantidad_cortes = int(self.cantidad_cortes.get())
        tipo_configuracion = self.tipo_configuracion.get()
        
        if tipo_configuracion == "Cantidad de Cortes":
            tiempo_entre_cortes = tiempo_total / cantidad_cortes
        else:
            tiempo_entre_cortes = int(self.tiempo_entre_cortes.get())
        
        for i in range(cantidad_cortes):
            tiempo_restante = tiempo_total - i * tiempo_entre_cortes
            self.mostrar_notificacion(f"Corte {i+1}", f"Tiempo Restante: {tiempo_restante} segundos")
            time.sleep(tiempo_entre_cortes)
        
        self.mostrar_notificacion("Cronómetro Finalizado", "Tiempo Total Agotado")
        
    def mostrar_notificacion(self, titulo, mensaje):
        notification.notify(
            title=titulo,
            message=mensaje,
            app_name="Cronómetro App"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = CronometroApp(root)
    root.mainloop()
