import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, Qt

class ExamCronometro(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cronómetro de Examen")

        # Ajusta el tamaño de la ventana reduciendo un 30% la altura y aumentando un 30% el ancho
        self.setGeometry(100, 100, int(300 * 1.3), int(300 * 0.7))

        # Impide la maximización de la ventana
        self.setFixedSize(int(300 * 1.3), int(300 * 0.7))

        # Mantén la ventana siempre en la parte superior
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.timer_label = QLabel("Tiempo transcurrido: 00:00")
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("font-size: 24px; font-family: Arial;")

        self.time_per_question_label = QLabel("Tiempo por pregunta: 00:00")
        self.time_per_question_label.setAlignment(Qt.AlignCenter)
        self.time_per_question_label.setStyleSheet("font-size: 24px; font-family: Arial;")

        self.question_label = QLabel("Pregunta actual: 0/50")
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setStyleSheet("font-size: 24px; font-family: Arial;")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.timer_label)
        self.layout.addWidget(self.time_per_question_label)
        self.layout.addWidget(self.question_label)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.total_time = 15 * 60
        self.remaining_time = self.total_time
        self.total_questions = 50
        self.question_number = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

    def update_timer(self):
        if self.remaining_time <= 0:
            self.timer.stop()
            self.timer_label.setText("Tiempo transcurrido: 15:00")
            self.time_per_question_label.setText("Tiempo por pregunta: 00:00")
            return

        minutes, seconds = divmod(self.remaining_time, 60)
        time_display = f"Tiempo transcurrido: {minutes:02}:{seconds:02}"
        self.timer_label.setText(time_display)
        self.remaining_time -= 1

        # Actualiza el número de pregunta proporcionalmente
        time_per_question = self.total_time / self.total_questions
        questions_completed = (self.total_time - self.remaining_time) / time_per_question
        self.question_number = int(questions_completed) + 1
        self.question_label.setText(f"Pregunta actual: {self.question_number}/{self.total_questions}")

        # Actualiza el tiempo por pregunta
        remaining_per_question = self.remaining_time % time_per_question
        minutes, seconds = divmod(int(remaining_per_question), 60)  # Convertir a enteros
        time_per_question_display = f"Tiempo por pregunta: {minutes:02}:{seconds:02}"
        self.time_per_question_label.setText(time_per_question_display)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExamCronometro()
    window.show()
    sys.exit(app.exec_())
