import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, Qt, QSize

class ExamCronometro(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cronómetro de Examen")
        self.setGeometry(100, 100, int(300 * 1.3), int(300 * 0.7))
        self.setFixedSize(int(300 * 1.3), int(300 * 0.7))
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

        self.control_buttons = QWidget()
        self.control_layout = QHBoxLayout()  # Cambiar a un diseño horizontal
        self.control_buttons.setLayout(self.control_layout)

        # Botón de pausar / reanudar
        self.pause_resume_button = QPushButton()
        self.pause_resume_button.setIcon(QIcon("pause_resume.png"))  # Proporcionar la ruta absoluta del icono
        self.pause_resume_button.setIconSize(QSize(32, 32))
        self.pause_resume_button.clicked.connect(self.pause_resume_timer)
        self.control_layout.addWidget(self.pause_resume_button)

        # Botón de detener
        self.stop_button = QPushButton()
        self.stop_button.setIcon(QIcon("stop.png"))  # Proporcionar la ruta absoluta del icono
        self.stop_button.setIconSize(QSize(32, 32))
        self.stop_button.clicked.connect(self.stop_timer)
        self.control_layout.addWidget(self.stop_button)

        # Botón de reiniciar
        self.restart_button = QPushButton()
        self.restart_button.setIcon(QIcon("restart.png"))  # Proporcionar la ruta absoluta del icono
        self.restart_button.setIconSize(QSize(32, 32))
        self.restart_button.clicked.connect(self.restart_timer)
        self.control_layout.addWidget(self.restart_button)

        # Botón de apagar
        self.shutdown_button = QPushButton()
        self.shutdown_button.setIcon(QIcon("shutdown.png"))  # Proporcionar la ruta absoluta del icono
        self.shutdown_button.setIconSize(QSize(32, 32))
        self.shutdown_button.clicked.connect(self.shutdown_app)
        self.control_layout.addWidget(self.shutdown_button)

        self.layout.addWidget(self.control_buttons)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.total_time = 15 * 60
        self.remaining_time = self.total_time
        self.total_questions = 50
        self.question_number = 0
        self.timer_running = True

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.init_timer()  # Inicializa el cronómetro

    def init_timer(self):
        self.timer.start(1000)
        self.timer_running = True

    def pause_resume_timer(self):
        if self.timer_running:
            self.timer.stop()
        else:
            self.init_timer()
        self.timer_running = not self.timer_running

    def stop_timer(self):
        self.timer.stop()
        self.remaining_time = self.total_time
        self.question_number = 0
        self.update_labels()

    def restart_timer(self):
        self.remaining_time = self.total_time
        self.question_number = 0
        self.update_labels()
        self.init_timer()

    def shutdown_app(self):
        sys.exit()

    def update_labels(self):
        if self.remaining_time <= 0:
            self.timer_label.setText("Tiempo transcurrido: 15:00")
            self.time_per_question_label.setText("Tiempo por pregunta: 00:00")
        else:
            minutes, seconds = divmod(self.remaining_time, 60)
            time_display = f"Tiempo transcurrido: {minutes:02}:{seconds:02}"
            self.timer_label.setText(time_display)

            time_per_question = self.total_time / self.total_questions
            questions_completed = (self.total_time - self.remaining_time) / time_per_question
            self.question_number = int(questions_completed) + 1
            self.question_label.setText(f"Pregunta actual: {self.question_number}/{self.total_questions}")

            remaining_per_question = self.remaining_time % time_per_question
            minutes, seconds = divmod(int(remaining_per_question), 60)
            time_per_question_display = f"Tiempo por pregunta: {minutes:02}:{seconds:02}"
            self.time_per_question_label.setText(time_per_question_display)

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_labels()
        else:
            self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExamCronometro()
    window.show()
    sys.exit(app.exec_())
