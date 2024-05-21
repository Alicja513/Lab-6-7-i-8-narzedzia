from PyQt5.QtCore import QThread, pyqtSignal


class Worker(QThread):
    finished = pyqtSignal(str)

    def __init__(self, input_path, output_path):
        super().__init__()
        self.input_path = input_path
        self.output_path = output_path

    def run(self):
        # Tutaj powinien znaleźć się kod konwersji plików
        # Załóżmy, że zapisujemy ten sam plik z jakimiś zmianami
        with open(self.input_path, 'r') as file:
            content = file.read()  # Prosta operacja odczytu

        with open(self.output_path, 'w') as file:
            file.write(content)  # Prosta operacja zapisu
        self.finished.emit(f"Finished converting {self.input_path} to {self.output_path}")


def convert_files(self):
    self.worker = Worker(self.input_path.text(), self.output_path.text())
    self.worker.finished.connect(self.update_status)
    self.worker.start()


def
