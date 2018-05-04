# #!/usr/bin/env python
# #-*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

COLUMNS = ('nClasse','IR','RMP','RH','ST','DTFS','SA','SD','fAHP')
LINES = ()

class SpreadSheet(QMainWindow):
    def __init__(self, rows, cols, parent = None):
        super(SpreadSheet, self).__init__(parent)

        self.r, self.c = rows, cols
        self.setWindowTitle("Tableau récapitulatif de la semaine")
        self.table = self.create_empty_table()
        self.button = QPushButton("Save")
        self.setCentralWidget(self.table)
        self.createActions()
        self.createContextMenu()

    def create_empty_table(self):
        table = QTableWidget(self.r, self.c)
        table.setHorizontalHeaderLabels(COLUMNS)
        table.setVerticalHeaderLabels(LINES)
        return table

    def createContextMenu(self):
        self.table.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.table.addAction(self.save)
        self.table.addAction(self.load)
        self.table.addAction(self.clear_all)

    def createActions(self):
        self.save = QAction(
                            "Sauver tout...", self,
                            shortcut="Ctrl+s", triggered=self.save_all
                           )

        self.load = QAction(
                            "Charger un fichier csv", self,
                            shortcut="Ctrl+o", triggered=self.open
                           )

        self.clear_all = QAction(
                                 "Effacer tableau", self,
                                 shortcut="Ctrl+n", triggered=self.clear
                                )

    def save_all(self):
        rows = list(range(self.table.rowCount()))
        columns = list(range(self.table.columnCount()))

        line = ''

        for i in rows:
            data = []
            for j in columns:
                s = self.table.item(i, j)
                if s:
                    data.append(s.text())
                else: data.append(' ')
            line += ', '.join(data) + '\n'

        fileName = QFileDialog.getSaveFileName(
                                               self.table,
                                               "Enregistrer sous...",
                                               "", "Values (*.csv)"
                                              )
        if fileName:
            with open(fileName, 'w') as f:
                f.write(line)

    def open(self):
        filename = QFileDialog.getOpenFileName(
                                               self.table,
                                               "Charger le fichier csv...",
                                               "", "Files CSV (*.csv)"
                                              )
        if filename:
            with open(filename, 'r') as f:
                for ind, line in enumerate(f):
                    if line:
                        cols = [li.strip().rstrip('\n') for li in line.split(',')]
                        for i, value in enumerate(cols):
                            self.table.setItem(ind, i, QTableWidgetItem(value))

    def clear(self):
        rows = list(range(self.table.rowCount()))
        columns = list(range(self.table.columnCount()))

        for i in rows:
            for j in columns:
                self.table.setItem(i, j, QTableWidgetItem(''))


app = QApplication(sys.argv)
sheet = SpreadSheet(len(LINES), len(COLUMNS))
sheet.resize(880, 420)
sheet.show()
sys.exit(app.exec_())
