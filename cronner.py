import time
from plyer import notification

# Configuración del cronómetro
total_time = 15 * 60  # 15 minutos en segundos
total_cuts = 50
cut_interval = total_time / total_cuts  # Intervalo de tiempo entre cortes

# Iniciar el cronómetro
for cut_number in range(1, total_cuts + 1):
    remaining_time = total_time - (cut_number - 1) * cut_interval
    minutes, seconds = divmod(int(remaining_time), 60)

    # Mostrar notificación
    notification_title = "Cronómetro"
    notification_message = f"Corte #{cut_number}: {minutes} minutos {seconds} segundos"
    notification.notify(
        title=notification_title,
        message=notification_message,
        app_name="CronometroApp",
    )

    if cut_number < total_cuts:
        # Esperar hasta el próximo corte
        time.sleep(cut_interval)

print("Cronómetro finalizado")
