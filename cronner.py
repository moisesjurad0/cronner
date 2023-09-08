import tkinter as tk
from tkinter import messagebox
import time
import threading

class CronometroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronómetro")
        
        self.tiempo_total = tk.StringVar()
        self.tiempo_total.set("00:00")
        
        self.label_tiempo = tk.Label(root, textvariable=self.tiempo_total, font=("Helvetica", 48))
        self.label_tiempo.pack()
        
        self.configurar_btn = tk.Button(root, text="Configurar Tiempo", command=self.configurar_tiempo)
        self.configurar_btn.pack()
        
        self.iniciar_btn = tk.Button(root, text="Iniciar", command=self.iniciar_cronometro)
        self.iniciar_btn.pack()
        
        self.detener_btn = tk.Button(root, text="Detener", command=self.detener_cronometro, state=tk.DISABLED)
        self.detener_btn.pack()
        
        self.tiempo_transcurrido = 0
        self.tiempo_configurado = 0
        self.alertas_configuradas = []
        self.cronometro_activo = False

    def configurar_tiempo(self):
        if not self.cronometro_activo:
            tiempo_configurado = simpledialog.askstring("Configurar Tiempo", "Ingresa el tiempo total (en segundos):")
            if tiempo_configurado is not None:
                self.tiempo_configurado = int(tiempo_configurado)
                self.tiempo_total.set(self.formato_tiempo(self.tiempo_configurado))

    def iniciar_cronometro(self):
        if self.tiempo_configurado > 0 and not self.cronometro_activo:
            self.cronometro_activo = True
            self.detener_btn.config(state=tk.NORMAL)
            self.iniciar_btn.config(state=tk.DISABLED)
            self.alertas_configuradas = [self.tiempo_configurado // 4, self.tiempo_configurado // 2, self.tiempo_configurado * 3 // 4]
            self.actualizar_cronometro()

    def detener_cronometro(self):
        self.cronometro_activo = False
        self.detener_btn.config(state=tk.DISABLED)
        self.iniciar_btn.config(state=tk.NORMAL)

    def actualizar_cronometro(self):
        if self.cronometro_activo:
            self.tiempo_transcurrido += 1
            tiempo_restante = self.tiempo_configurado - self.tiempo_transcurrido
            self.tiempo_total.set(self.formato_tiempo(tiempo_restante))
            
            if self.tiempo_transcurrido in self.alertas_configuradas:
                messagebox.showinfo("Alerta", f"Ha transcurrido {self.tiempo_transcurrido} segundos.")
            
            if self.tiempo_transcurrido >= self.tiempo_configurado:
                self.cronometro_activo = False
                self.detener_btn.config(state=tk.DISABLED)
                self.iniciar_btn.config(state=tk.NORMAL)
            else:
                self.root.after(1000, self.actualizar_cronometro)

    def formato_tiempo(self, segundos):
        minutos = segundos // 60
        segundos = segundos % 60
        return f"{minutos:02d}:{segundos:02d}"

if __name__ == "__main__":
    root = tk.Tk()
    app = CronometroApp(root)
    root.mainloop()
