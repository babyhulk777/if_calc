from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi

from sys import argv, exit


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        loadUi('if_med.ui', self)

        # Carrega imagem
        logo_img = QPixmap('logo_if.jpeg')
        logo_img = logo_img.scaled(self.logo.width(), self.logo.height())
        self.logo.setPixmap(logo_img)

        # Conecta o botão a função
        self.calcular.clicked.connect(self.calc)

        self.show()

    @pyqtSlot()
    def calc(self):
        if self.tamanho_materia.currentText() == '2 bimestres':
            # 1 bimestre: peso 2, 2 bimestre: peso 3
            notas = [int(x) for x in [self.nota1.strip(), self.nota2.strip()]]
            resultado = (notas[0] * 2 + notas[1] * 3) / 5
            if resultado < 60:
                # Substitui a menor nota por um valor que faça com que
                # o resultado seja 60
                prova_final = 
            self.situacao.setText('Aprovado')
            self.media_final.setText(str(resultado))
        else:



app = QApplication(argv)
window = Window()
exit(app.exec_())
